from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def read_grayscale(path: Path) -> np.ndarray:
    image = cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Cannot read image: {path}")
    return image


def write_image(path: Path, image: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ok, buffer = cv2.imencode(path.suffix, image)
    if not ok:
        raise ValueError(f"Cannot encode image: {path}")
    buffer.tofile(str(path))


def normalize_gray(image: np.ndarray) -> np.ndarray:
    return cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)


def remove_black_border(image: np.ndarray, threshold: int = 8, margin: int = 8) -> np.ndarray:
    mask = image > threshold
    coords = cv2.findNonZero(mask.astype(np.uint8))
    if coords is None:
        return image

    x, y, w, h = cv2.boundingRect(coords)
    x0 = max(x - margin, 0)
    y0 = max(y - margin, 0)
    x1 = min(x + w + margin, image.shape[1])
    y1 = min(y + h + margin, image.shape[0])
    return image[y0:y1, x0:x1]


def enhance_dental_panorama(
    image: np.ndarray,
    *,
    clahe_clip: float = 2.0,
    clahe_grid: int = 8,
    denoise_h: float = 7.0,
    gamma: float = 1.0,
    sharpen_amount: float = 0.65,
) -> dict[str, np.ndarray]:
    image = normalize_gray(image)

    if gamma != 1.0:
        inv_gamma = 1.0 / gamma
        lut = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)], dtype=np.uint8)
        image = cv2.LUT(image, lut)

    denoised = cv2.fastNlMeansDenoising(image, None, h=denoise_h, templateWindowSize=7, searchWindowSize=21)

    clahe = cv2.createCLAHE(clipLimit=clahe_clip, tileGridSize=(clahe_grid, clahe_grid))
    contrast = clahe.apply(denoised)

    # Unsharp masking strengthens tooth boundaries and lesion texture without binarizing the image.
    blurred = cv2.GaussianBlur(contrast, (0, 0), sigmaX=1.2)
    sharpened = cv2.addWeighted(contrast, 1.0 + sharpen_amount, blurred, -sharpen_amount, 0)
    sharpened = normalize_gray(sharpened)

    threshold = cv2.adaptiveThreshold(
        sharpened,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        35,
        5,
    )

    edges = cv2.Canny(sharpened, threshold1=35, threshold2=110)

    return {
        "01_input_norm": image,
        "02_denoised": denoised,
        "03_clahe": contrast,
        "04_enhanced": sharpened,
        "05_threshold": threshold,
        "06_edges": edges,
    }


def collect_images(input_path: Path) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() not in IMAGE_EXTS:
            raise ValueError(f"Unsupported image suffix: {input_path.suffix}")
        return [input_path]

    if not input_path.is_dir():
        raise FileNotFoundError(f"Input path not found: {input_path}")

    return sorted(p for p in input_path.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS)


def preprocess_one(path: Path, input_root: Path, output_root: Path, args: argparse.Namespace) -> None:
    image = read_grayscale(path)
    if args.crop_border:
        image = remove_black_border(image, threshold=args.border_threshold, margin=args.crop_margin)

    outputs = enhance_dental_panorama(
        image,
        clahe_clip=args.clahe_clip,
        clahe_grid=args.clahe_grid,
        denoise_h=args.denoise_h,
        gamma=args.gamma,
        sharpen_amount=args.sharpen_amount,
    )

    rel = path.name if input_root.is_file() else str(path.relative_to(input_root))
    rel_path = Path(rel)
    main_out = output_root / rel_path.with_suffix(".png")
    write_image(main_out, outputs["04_enhanced"])

    if args.save_debug:
        stem_dir = output_root / (rel_path.parent / rel_path.stem)
        for name, image_out in outputs.items():
            write_image(stem_dir / f"{name}.png", image_out)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="OpenCV preprocessing for grayscale dental panoramic images.",
    )
    parser.add_argument("--input", required=True, type=Path, help="Input image file or image directory.")
    parser.add_argument("--output", required=True, type=Path, help="Output directory.")
    parser.add_argument("--save-debug", action="store_true", help="Save intermediate preprocessing images.")
    parser.add_argument("--crop-border", action="store_true", help="Remove black panoramic-image border.")
    parser.add_argument("--border-threshold", type=int, default=8, help="Pixel threshold for black-border crop.")
    parser.add_argument("--crop-margin", type=int, default=8, help="Margin kept after border crop.")
    parser.add_argument("--clahe-clip", type=float, default=2.0, help="CLAHE contrast clip limit.")
    parser.add_argument("--clahe-grid", type=int, default=8, help="CLAHE grid size.")
    parser.add_argument("--denoise-h", type=float, default=7.0, help="Non-local means denoising strength.")
    parser.add_argument("--gamma", type=float, default=1.0, help="Gamma correction value.")
    parser.add_argument("--sharpen-amount", type=float, default=0.65, help="Unsharp masking strength.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input.resolve()
    output_root = args.output.resolve()
    images = collect_images(input_path)
    if not images:
        raise SystemExit(f"No images found in: {input_path}")

    input_root = input_path if input_path.is_file() else input_path
    for image_path in images:
        preprocess_one(image_path, input_root, output_root, args)

    print(f"Processed {len(images)} image(s). Output: {output_root}")


if __name__ == "__main__":
    main()
