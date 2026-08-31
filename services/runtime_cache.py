from __future__ import annotations

import os
import tempfile
import threading
from pathlib import Path
from typing import Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent
MANAGED_MARKER_NAME: Final[str] = ".managed-by-dentalv8"
MANAGED_MARKER_TEXT: Final[str] = "DentalV8 managed runtime cache\n"

_CONFIG_LOCK = threading.Lock()
_CONFIGURED_PATHS: dict[str, Path] | None = None
_DIRECT_RUNTIME_LOCK = None


def _runtime_root() -> Path:
    configured = os.getenv("DENTAL_RUNTIME_ROOT", "").strip()
    candidate = Path(configured).expanduser() if configured else PROJECT_ROOT / ".runtime"
    if not candidate.is_absolute():
        candidate = PROJECT_ROOT / candidate
    return candidate.resolve()


def _reject_reparse_directory(path: Path) -> None:
    is_junction = getattr(path, "is_junction", lambda: False)
    if path.is_symlink() or is_junction():
        raise RuntimeError(f"运行缓存目录不能是符号链接或目录联接：{path}")


def _prepare_managed_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    _reject_reparse_directory(path)
    marker = path / MANAGED_MARKER_NAME
    if marker.exists():
        if not marker.is_file() or marker.is_symlink():
            raise RuntimeError(f"运行缓存管理标记类型不安全：{marker}")
        # ``utf-8-sig`` also accepts markers created by Windows PowerShell 5.1,
        # whose legacy ``-Encoding UTF8`` writer prepends a BOM.
        if marker.read_text(encoding="utf-8-sig").strip() != MANAGED_MARKER_TEXT.strip():
            raise RuntimeError(f"运行缓存管理标记不匹配：{marker}")
        return

    # Never claim a non-empty directory that was not created for DentalV8.
    if any(path.iterdir()):
        raise RuntimeError(f"拒绝接管未标记且非空的运行缓存目录：{path}")
    marker.write_text(MANAGED_MARKER_TEXT, encoding="utf-8")


def _acquire_direct_runtime_lock(runtime_root: Path) -> None:
    """Protect direct Python/uvicorn starts from a concurrent managed launcher."""

    global _DIRECT_RUNTIME_LOCK
    if os.getenv("DENTAL_MANAGED_RUNTIME", "").strip() == "1" or _DIRECT_RUNTIME_LOCK is not None:
        return

    lock_path = runtime_root / "dentalv8-runtime.lock"
    handle = lock_path.open("a+b")
    try:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except (OSError, BlockingIOError) as exc:
        handle.close()
        raise RuntimeError("另一个 DentalV8 实例正在运行，已拒绝共享运行缓存。") from exc
    _DIRECT_RUNTIME_LOCK = handle


def configure_runtime_environment() -> dict[str, Path]:
    """Route this process' temporary/cache files to project-local D-drive paths.

    This function intentionally performs no deletion. Deletion is owned by the
    guarded PowerShell launcher after the application process has fully exited.
    """

    global _CONFIGURED_PATHS
    with _CONFIG_LOCK:
        if _CONFIGURED_PATHS is not None:
            return dict(_CONFIGURED_PATHS)

        runtime_root = _runtime_root()
        paths = {
            "runtime": runtime_root,
            "temp": runtime_root / "temp",
            "gradio": runtime_root / "gradio",
            "torch": runtime_root / "torch",
            "huggingface": runtime_root / "huggingface",
            "cache": runtime_root / "cache",
            "ultralytics": runtime_root / "ultralytics",
            "matplotlib": runtime_root / "matplotlib",
            "cuda": runtime_root / "cuda",
            "joblib": runtime_root / "joblib",
        }

        runtime_root.mkdir(parents=True, exist_ok=True)
        _reject_reparse_directory(runtime_root)
        if os.name == "nt":
            system_root = Path(os.environ.get("SystemRoot", r"C:\Windows")).resolve()
            if runtime_root.anchor.casefold() == system_root.anchor.casefold():
                raise RuntimeError(f"运行缓存不能位于系统盘：{runtime_root}")
        _acquire_direct_runtime_lock(runtime_root)
        _prepare_managed_directory(paths["temp"])
        _prepare_managed_directory(paths["gradio"])
        for name in ("torch", "huggingface", "cache", "ultralytics", "matplotlib", "cuda", "joblib"):
            paths[name].mkdir(parents=True, exist_ok=True)
            _reject_reparse_directory(paths[name])

        environment = {
            "DENTAL_RUNTIME_ROOT": paths["runtime"],
            "TEMP": paths["temp"],
            "TMP": paths["temp"],
            "TMPDIR": paths["temp"],
            "GRADIO_TEMP_DIR": paths["gradio"],
            "TORCH_HOME": paths["torch"],
            "HF_HOME": paths["huggingface"],
            "HUGGINGFACE_HUB_CACHE": paths["huggingface"] / "hub",
            "XDG_CACHE_HOME": paths["cache"],
            "YOLO_CONFIG_DIR": paths["ultralytics"],
            "MPLCONFIGDIR": paths["matplotlib"],
            "CUDA_CACHE_PATH": paths["cuda"],
            "JOBLIB_TEMP_FOLDER": paths["joblib"],
        }
        huggingface_hub = paths["huggingface"] / "hub"
        huggingface_hub.mkdir(parents=True, exist_ok=True)
        _reject_reparse_directory(huggingface_hub)
        for name, path in environment.items():
            os.environ[name] = str(path)
        os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")

        # tempfile may already have cached the system C-drive location in the
        # uvicorn bootstrap process, so update its process-local cache as well.
        tempfile.tempdir = str(paths["temp"])

        _CONFIGURED_PATHS = paths
        return dict(paths)
