from __future__ import annotations

import json
import socket
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import gradio as gr
import numpy as np
import pandas as pd
import requests
import torch
import yaml
from PIL import Image, ImageDraw, ImageFont

# Hardcoded API key is only for local coursework demonstration.
# Do not commit this pattern to public repositories or production systems.
DEEPSEEK_API_KEY = "sk-553b2bf62c484ecb899b4c1fbc4ee9f3"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-v4-flash"
DEEPSEEK_TIMEOUT_SECONDS = 45

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "outputs"
REPORT_DIR = OUTPUT_DIR / "reports"
HISTORY_PATH = OUTPUT_DIR / "history.json"
DEVICE = "cpu"
DISCLAIMER = "本系统仅用于牙齿病变疑似区域的辅助识别与科研展示，不作为临床诊断依据，最终结果应由专业人员复核。"
STATUS_LABELS = {
    "success": "成功",
    "load_failed": "权重未加载",
    "inference_failed": "推理失败",
    "missing_dependency": "依赖缺失",
    "no_weight_matched": "未匹配权重",
}
MODEL_NOT_LOADED_MSG = "该模型权重未成功加载，请检查权重文件。"
MODEL_INFERENCE_FAILED_MSG = "该模型推理失败，请检查模型格式、类别配置或输入图像。"
MODEL_UNAVAILABLE_MSG = "当前模型不可用，未生成检测结果。"
SAFE_TERMS = "请仅使用“疑似区域”“辅助识别结果”“建议人工复核”等非医疗结论表述。"


@dataclass
class ModelSpec:
    key: str
    name: str
    model_type: str
    description: str
    preferred_terms: tuple[str, ...]
    fallback_terms: tuple[str, ...] = ()


MODEL_SPECS = [
    ModelSpec(
        key="lightweight",
        name="均衡型基线模型",
        model_type="YOLOv8n baseline e50",
        description="使用 yolov8n+baseline_e50 权重，作为其它优化模型的对照基线。",
        preferred_terms=("yolov8n+baseline_e50",),
    ),
    ModelSpec(
        key="high_precision",
        name="高精度牙齿病变定位模型",
        model_type="YOLOv8m + PIoU",
        description="强调定位精度和结果稳定性，适合高精度辅助分析展示。",
        preferred_terms=("yolov8m+piou",),
        fallback_terms=("yolov8m", "piou"),
    ),
    ModelSpec(
        key="high_recall",
        name="高召回牙齿病变检测模型",
        model_type="YOLOv8m + P2-highRecall",
        description="强调尽量减少漏检，适合初筛和复核优先的展示场景。",
        preferred_terms=("yolov8m+p2-highrecall_mosaic05_e200_p30", "p2-highrecall"),
        fallback_terms=("yolov8m", "p2", "highrecall", "mosaic05"),
    ),
]


MODEL_CACHE: dict[str, Any] = {}
MODEL_REGISTRY: dict[str, dict[str, Any]] = {}


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)


def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def safe_read_text(path: Path, limit: int = 6000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except Exception:
        return ""


def load_history() -> dict[str, Any]:
    ensure_dirs()
    if not HISTORY_PATH.exists():
        data = {"events": []}
        HISTORY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data
    try:
        data = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("events", []), list):
            raise ValueError("invalid history")
        return data
    except Exception:
        data = {"events": []}
        HISTORY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data


def save_history(history: dict[str, Any]) -> None:
    ensure_dirs()
    HISTORY_PATH.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")


def append_history(event: dict[str, Any]) -> dict[str, Any]:
    history = load_history()
    history.setdefault("events", []).append(event)
    history["events"] = history["events"][-300:]
    save_history(history)
    return history


def clear_history() -> dict[str, Any]:
    history = {"events": []}
    save_history(history)
    return history


def scan_weight_candidates() -> list[dict[str, Any]]:
    candidates = []
    for path in ROOT.rglob("*.pt"):
        rel = path.relative_to(ROOT)
        parts = [p.lower() for p in rel.parts]
        is_result_best = "results" in parts and path.name.lower() == "best.pt"
        score_base = 50 if is_result_best else 0
        context = " ".join(parts)
        for near in [path.parent, path.parent.parent, path.parent.parent.parent]:
            if near.exists():
                context += " " + safe_read_text(near / "README.md")
                context += " " + safe_read_text(near / "args.yaml")
        candidates.append(
            {
                "path": path,
                "rel": str(rel),
                "context": context.lower().replace("\\", "/"),
                "score_base": score_base,
                "size": path.stat().st_size,
            }
        )
    return candidates


def score_candidate(candidate: dict[str, Any], spec: ModelSpec) -> int:
    context = candidate["context"]
    score = candidate["score_base"]
    if "last.pt" in context:
        score -= 20
    for term in spec.preferred_terms:
        if term.lower() in context:
            score += 120
    for term in spec.fallback_terms:
        if term.lower() in context:
            score += 20
    if "best.pt" in context:
        score += 15
    return score


def discover_models() -> dict[str, dict[str, Any]]:
    candidates = scan_weight_candidates()
    registry: dict[str, dict[str, Any]] = {}
    for spec in MODEL_SPECS:
        ranked = sorted(candidates, key=lambda c: score_candidate(c, spec), reverse=True)
        best = ranked[0] if ranked else None
        matched = bool(best and score_candidate(best, spec) >= 80)
        registry[spec.key] = {
            "spec": spec,
            "weight_path": best["path"] if matched else None,
            "weight_rel": best["rel"] if matched else "",
            "match_score": score_candidate(best, spec) if best else 0,
            "match_status": "已匹配真实权重" if matched else "未匹配权重",
            "load_status": "not_loaded",
            "load_error": "",
            "model": None,
        }
    return registry


def refresh_model_registry() -> dict[str, dict[str, Any]]:
    global MODEL_REGISTRY
    MODEL_REGISTRY = discover_models()
    return MODEL_REGISTRY


def get_registry() -> dict[str, dict[str, Any]]:
    if not MODEL_REGISTRY:
        return refresh_model_registry()
    return MODEL_REGISTRY


def model_options() -> list[str]:
    return [spec.name for spec in MODEL_SPECS]


def model_name_to_key(name: str) -> str:
    for spec in MODEL_SPECS:
        if spec.name == name:
            return spec.key
    return MODEL_SPECS[0].key


def registry_status_markdown() -> str:
    lines = ["| 模型 | 类型 | 匹配状态 | 权重 |", "|---|---|---|---|"]
    for spec in MODEL_SPECS:
        item = get_registry().get(spec.key, {})
        weight = item.get("weight_rel") or "-"
        status = item.get("match_status", "未匹配权重")
        if item.get("load_status") == "loaded":
            status = "已加载"
        elif item.get("load_status") == "failed":
            status = "加载失败"
        lines.append(f"| {spec.name} | {spec.model_type} | {status} | `{weight}` |")
    return "\n".join(lines)


def get_yolo_class():
    try:
        from ultralytics import YOLO

        return YOLO, None
    except Exception as exc:
        return None, str(exc)


def load_model(model_key: str) -> tuple[Any, str]:
    registry = get_registry()
    item = registry.get(model_key)
    if not item or not item.get("weight_path"):
        return None, "no_weight_matched"
    if item.get("load_status") == "loaded" and item.get("model") is not None:
        return item["model"], "success"
    if item.get("load_status") == "failed":
        return None, "load_failed"

    YOLO, err = get_yolo_class()
    if YOLO is None:
        item["load_status"] = "failed"
        item["load_error"] = "缺少 ultralytics 依赖。"
        return None, "missing_dependency"

    try:
        model = YOLO(str(item["weight_path"]))
        item["model"] = model
        item["load_status"] = "loaded"
        item["load_error"] = ""
        MODEL_CACHE[model_key] = model
        return model, "success"
    except Exception:
        item["load_status"] = "failed"
        item["load_error"] = MODEL_NOT_LOADED_MSG
        return None, "load_failed"


def start_step(process_steps: list[dict[str, Any]], name: str) -> float:
    return time.perf_counter()


def finish_step(process_steps: list[dict[str, Any]], name: str, started: float, status: str = "完成", message: str = "") -> None:
    process_steps.append(
        {
            "步骤": name,
            "状态": status,
            "耗时(ms)": round((time.perf_counter() - started) * 1000, 2),
            "说明": message,
        }
    )


def empty_result(
    model_key: str,
    status: str,
    image: Image.Image | None,
    process_steps: list[dict[str, Any]],
    error_message: str,
) -> dict[str, Any]:
    spec = next(s for s in MODEL_SPECS if s.key == model_key)
    width, height = (image.size if image is not None else (0, 0))
    return {
        "model_key": model_key,
        "model_name": spec.name,
        "model_type": spec.model_type,
        "status": status,
        "runtime_mode": "unavailable",
        "device": DEVICE,
        "image_info": {"width": width, "height": height, "mode": image.mode if image else ""},
        "box_count": 0,
        "avg_confidence": 0.0,
        "max_confidence": 0.0,
        "boxes": [],
        "inference_time_ms": 0.0,
        "process_steps": process_steps,
        "created_at": now_iso(),
        "review_suggestions": [],
        "error_message": error_message,
    }


def risk_level(confidence: float) -> tuple[str, str]:
    if confidence >= 0.75:
        return "可信度较高", "该疑似区域可信度较高，仍建议由专业人员复核。"
    if confidence >= 0.45:
        return "建议人工复核", "该疑似区域可信度中等，建议人工复核。"
    return "强烈建议人工复核", "该疑似区域可信度较低，强烈建议人工复核。"


def normalize_image(image: Any) -> Image.Image:
    if image is None:
        raise ValueError("请先上传图像。")
    if isinstance(image, Image.Image):
        return image.convert("RGB")
    return Image.fromarray(np.asarray(image)).convert("RGB")


def draw_boxes(image: Image.Image, boxes: list[dict[str, Any]]) -> Image.Image:
    out = image.copy().convert("RGB")
    draw = ImageDraw.Draw(out)
    font = ImageFont.load_default()
    colors = [(255, 80, 80), (80, 180, 255), (80, 220, 130), (255, 190, 80)]
    for idx, box in enumerate(boxes):
        x1, y1, x2, y2 = box["bbox_xyxy"]
        color = colors[idx % len(colors)]
        draw.rectangle([x1, y1, x2, y2], outline=color, width=3)
        label = f"{idx + 1}. {box['class_name']} {box['confidence']:.2f}"
        tw = max(80, len(label) * 7)
        draw.rectangle([x1, max(0, y1 - 18), x1 + tw, y1], fill=color)
        draw.text((x1 + 3, max(0, y1 - 16)), label, fill=(0, 0, 0), font=font)
    return out


def result_to_box_rows(result: dict[str, Any]) -> list[list[Any]]:
    rows = []
    for i, box in enumerate(result.get("boxes", []), 1):
        rows.append(
            [
                i,
                box["class_name"],
                round(box["confidence"], 4),
                box["bbox_xyxy"],
                f"{box['area_ratio']:.2%}",
                box["risk_level"],
                box["review_suggestion"],
            ]
        )
    return rows


def steps_to_rows(result: dict[str, Any]) -> list[list[Any]]:
    return [[s["步骤"], s["状态"], s["耗时(ms)"], s["说明"]] for s in result.get("process_steps", [])]


def explanation_markdown(result: dict[str, Any]) -> str:
    if result.get("status") != "success":
        return f"### 检测未完成\n\n{result.get('error_message') or MODEL_UNAVAILABLE_MSG}\n\n{DISCLAIMER}"
    lines = [
        "### 检测结果解释",
        f"- 模型：{result['model_name']}",
        f"- 运行模式：{result['runtime_mode']}，设备：CPU",
        f"- 疑似区域数量：{result['box_count']}",
        f"- 平均置信度：{result['avg_confidence']:.3f}",
        "",
    ]
    if not result.get("boxes"):
        lines.append("未检测到满足当前阈值的疑似区域，建议结合原图进行人工复核。")
    for i, box in enumerate(result.get("boxes", []), 1):
        lines.extend(
            [
                f"**目标 {i}：{box['class_name']}**",
                f"- 置信度：{box['confidence']:.3f}",
                f"- 坐标：{box['bbox_xyxy']}",
                f"- 面积占比：{box['area_ratio']:.2%}",
                f"- 风险等级：{box['risk_level']}",
                f"- 复核建议：{box['review_suggestion']}",
                "",
            ]
        )
    lines.append(DISCLAIMER)
    return "\n".join(lines)


def run_detection_core(image: Any, model_key: str, conf: float, iou: float) -> tuple[dict[str, Any], Image.Image | None]:
    process_steps: list[dict[str, Any]] = []
    total_start = time.perf_counter()

    step = start_step(process_steps, "图片上传完成")
    try:
        pil_image = normalize_image(image)
        finish_step(process_steps, "图片上传完成", step, message="已读取上传图像。")
    except Exception as exc:
        finish_step(process_steps, "图片上传完成", step, "失败", "图像读取失败。")
        return empty_result(model_key, "inference_failed", None, process_steps, str(exc)), None

    step = start_step(process_steps, "图像预处理")
    np_image = np.asarray(pil_image)
    finish_step(process_steps, "图像预处理", step, message="已转换为 RGB 输入。")

    step = start_step(process_steps, "模型加载或模型检查")
    model, load_status = load_model(model_key)
    if load_status != "success":
        msg = MODEL_NOT_LOADED_MSG if load_status == "load_failed" else MODEL_UNAVAILABLE_MSG
        if load_status == "missing_dependency":
            msg = "缺少模型推理依赖，请检查 ultralytics 是否可用。"
        elif load_status == "no_weight_matched":
            msg = "未匹配到该模型的可用权重。"
        finish_step(process_steps, "模型加载或模型检查", step, "失败", msg)
        result = empty_result(model_key, load_status, pil_image, process_steps, msg)
        return result, pil_image
    finish_step(process_steps, "模型加载或模型检查", step, message="真实权重已加载或缓存可用。")

    step = start_step(process_steps, "模型推理")
    inference_start = time.perf_counter()
    try:
        predictions = model.predict(source=np_image, conf=float(conf), iou=float(iou), device=DEVICE, verbose=False)
    except Exception:
        finish_step(process_steps, "模型推理", step, "失败", MODEL_INFERENCE_FAILED_MSG)
        result = empty_result(model_key, "inference_failed", pil_image, process_steps, MODEL_INFERENCE_FAILED_MSG)
        return result, pil_image
    inference_time_ms = round((time.perf_counter() - inference_start) * 1000, 2)
    finish_step(process_steps, "模型推理", step, message="CPU 推理完成。")

    step = start_step(process_steps, "NMS 后处理")
    pred = predictions[0] if predictions else None
    width, height = pil_image.size
    boxes: list[dict[str, Any]] = []
    names = getattr(model, "names", {}) or getattr(pred, "names", {}) or {}
    if pred is not None and getattr(pred, "boxes", None) is not None:
        for raw in pred.boxes:
            cls_id = int(raw.cls.detach().cpu().numpy()[0])
            confidence = float(raw.conf.detach().cpu().numpy()[0])
            xyxy = raw.xyxy.detach().cpu().numpy()[0].tolist()
            x1, y1, x2, y2 = [round(float(v), 2) for v in xyxy]
            area_ratio = max(0.0, (x2 - x1) * (y2 - y1) / max(1, width * height))
            level, suggestion = risk_level(confidence)
            boxes.append(
                {
                    "class_id": cls_id,
                    "class_name": str(names.get(cls_id, f"class_{cls_id}")),
                    "confidence": confidence,
                    "bbox_xyxy": [x1, y1, x2, y2],
                    "area_ratio": area_ratio,
                    "risk_level": level,
                    "review_suggestion": suggestion,
                }
            )
    finish_step(process_steps, "NMS 后处理", step, message=f"保留 {len(boxes)} 个疑似区域。")

    step = start_step(process_steps, "结果渲染")
    rendered = draw_boxes(pil_image, boxes)
    finish_step(process_steps, "结果渲染", step, message="已绘制真实检测框。")

    step = start_step(process_steps, "结果解释生成")
    review_suggestions = [b["review_suggestion"] for b in boxes if b["risk_level"] != "可信度较高"]
    finish_step(process_steps, "结果解释生成", step, message="解释面板已准备。")

    step = start_step(process_steps, "报告数据准备完成")
    confidences = [b["confidence"] for b in boxes]
    spec = next(s for s in MODEL_SPECS if s.key == model_key)
    result = {
        "model_key": model_key,
        "model_name": spec.name,
        "model_type": spec.model_type,
        "status": "success",
        "runtime_mode": "real_yolo_cpu",
        "device": DEVICE,
        "image_info": {"width": width, "height": height, "mode": pil_image.mode},
        "box_count": len(boxes),
        "avg_confidence": float(sum(confidences) / len(confidences)) if confidences else 0.0,
        "max_confidence": float(max(confidences)) if confidences else 0.0,
        "boxes": boxes,
        "inference_time_ms": inference_time_ms,
        "process_steps": process_steps,
        "created_at": now_iso(),
        "review_suggestions": review_suggestions,
        "error_message": "",
    }
    finish_step(process_steps, "报告数据准备完成", step, message="结构化结果已生成。")
    result["total_time_ms"] = round((time.perf_counter() - total_start) * 1000, 2)
    return result, rendered


def record_detection_history(result: dict[str, Any], task_kind: str) -> dict[str, Any]:
    event = {
        "type": task_kind,
        "created_at": now_iso(),
        "result": result,
    }
    return append_history(event)


def run_single_detection(image: Any, model_name: str, conf: float, iou: float):
    model_key = model_name_to_key(model_name)
    result, rendered = run_detection_core(image, model_key, conf, iou)
    record_detection_history(result, "single_detection")
    image_out = rendered if rendered is not None else None
    return (
        image_out,
        result_to_box_rows(result),
        explanation_markdown(result),
        steps_to_rows(result),
        result,
        *dashboard_outputs(),
        registry_status_markdown(),
    )


def reset_single_detection_outputs():
    return (
        None,
        [],
        "等待检测。",
        [],
        {},
        *dashboard_outputs(),
        registry_status_markdown(),
    )


def successful_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [r for r in results if r.get("status") == "success" and r.get("runtime_mode") == "real_yolo_cpu"]


def compare_summary(results: list[dict[str, Any]]) -> str:
    ok = successful_results(results)
    if not ok:
        return f"### 多模型对比总结\n\n当前没有可用于统计的成功推理结果。\n\n{DISCLAIMER}"
    fastest = min(ok, key=lambda r: r.get("inference_time_ms", float("inf")))
    most_boxes = max(ok, key=lambda r: r.get("box_count", 0))
    best_conf = max(ok, key=lambda r: r.get("avg_confidence", 0.0))
    lines = [
        "### 多模型对比总结",
        f"- 速度最快：{fastest['model_name']}，耗时 {fastest['inference_time_ms']:.2f} ms。",
        f"- 检出目标最多：{most_boxes['model_name']}，疑似区域 {most_boxes['box_count']} 个。",
        f"- 平均置信度最高：{best_conf['model_name']}，平均置信度 {best_conf['avg_confidence']:.3f}。",
        "- 快速筛查更适合选择高召回牙齿病变检测模型；常规对照可选择均衡型基线模型。",
        "- 高精度定位展示更适合选择高精度牙齿病变定位模型。",
    ]
    review_count = sum(len(r.get("review_suggestions", [])) for r in ok)
    if review_count:
        lines.append(f"- 当前共有 {review_count} 条结果建议人工复核。")
    else:
        lines.append("- 当前成功模型未生成中低可信度复核建议。")
    failed = [r for r in results if r.get("status") != "success"]
    for item in failed:
        lines.append(f"- {item['model_name']} 未参与有效统计：{item.get('error_message') or STATUS_LABELS[item['status']]}。")
    lines.append("")
    lines.append(DISCLAIMER)
    return "\n".join(lines)


def compare_rows(results: list[dict[str, Any]]) -> list[list[Any]]:
    rows = []
    for result in results:
        success = result.get("status") == "success" and result.get("runtime_mode") == "real_yolo_cpu"
        rows.append(
            [
                result["model_name"],
                result["model_type"],
                STATUS_LABELS.get(result["status"], result["status"]),
                result["box_count"] if success else 0,
                f"{result['avg_confidence']:.3f}" if success and result["box_count"] else "-",
                f"{result['max_confidence']:.3f}" if success and result["box_count"] else "-",
                f"{result['inference_time_ms']:.2f}" if success else "-",
                len(result.get("review_suggestions", [])) if success else 0,
                next(s.description for s in MODEL_SPECS if s.key == result["model_key"]),
                result.get("error_message", ""),
            ]
        )
    return rows


def run_model_comparison(image: Any, conf: float, iou: float):
    results = []
    rendered_images = []
    for spec in MODEL_SPECS:
        result, rendered = run_detection_core(image, spec.key, conf, iou)
        results.append(result)
        rendered_images.append(rendered)
    append_history({"type": "model_comparison", "created_at": now_iso(), "results": results})
    return (
        rendered_images[0],
        rendered_images[1],
        rendered_images[2],
        compare_rows(results),
        compare_summary(results),
        results,
        *dashboard_outputs(),
        registry_status_markdown(),
    )


def reset_model_comparison_outputs():
    return (
        None,
        None,
        None,
        [],
        "等待对比。",
        [],
        *dashboard_outputs(),
        registry_status_markdown(),
    )


def chat_content_to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        if "text" in value:
            return str(value.get("text") or "")
        if "content" in value:
            return chat_content_to_text(value.get("content"))
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        parts: list[str] = []
        for item in value:
            text = chat_content_to_text(item).strip()
            if text:
                parts.append(text)
        return "\n".join(parts)
    if hasattr(value, "text"):
        return str(value.text)
    if hasattr(value, "content"):
        return chat_content_to_text(value.content)
    return str(value)


def is_treatment_question(question: str) -> bool:
    return any(term in question for term in ("治疗", "用药", "手术", "怎么办", "怎么做", "处理", "拔牙", "治疗规划"))


def safe_treatment_answer(question: str, detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> str:
    ctx_results = comparison if comparison else ([detection] if detection else [])
    ok = successful_results([r for r in ctx_results if isinstance(r, dict)])
    target_terms = {
        "Caries": ("Caries", "龋", "蛀牙"),
        "Periapical_Lesion": ("Periapical", "根尖", "根尖周"),
        "Impacted": ("Impacted", "阻生", "埋伏"),
    }
    requested_classes = [
        class_name
        for class_name, aliases in target_terms.items()
        if any(alias.lower() in question.lower() for alias in aliases)
    ]

    lines = ["以下是基于当前检测结果整理的复核重点：", ""]
    if not ok:
        lines.append("- 当前没有成功的真实模型推理结果可用于整理疑似区域。")
    else:
        any_box = False
        for result in ok:
            boxes = result.get("boxes", [])
            if requested_classes:
                boxes = [b for b in boxes if b.get("class_name") in requested_classes]
            if not boxes:
                continue
            any_box = True
            lines.append(f"- {result['model_name']}：")
            for class_name in sorted({b.get("class_name", "-") for b in boxes}):
                class_boxes = [b for b in boxes if b.get("class_name") == class_name]
                review_count = sum(1 for b in class_boxes if b.get("risk_level") != "可信度较高")
                confs = ", ".join(f"{float(b.get('confidence', 0.0)):.2f}" for b in class_boxes)
                lines.append(
                    f"  - {class_name} 疑似区域 {len(class_boxes)} 个，置信度：{confs}；"
                    f"建议人工复核 {review_count} 个。"
                )
        if not any_box:
            target_text = "、".join(requested_classes) if requested_classes else "相关类别"
            lines.append(f"- 当前成功推理结果中没有检出 {target_text} 的疑似区域。")
    lines.extend(
        [
            "",
            "就诊复核时可以准备这些信息：疑似区域截图、模型对比结果、是否有疼痛或不适、既往口腔治疗史。后续处理应由专业口腔医生结合临床检查、影像资料和个人情况判断。",
            "",
            DISCLAIMER,
        ]
    )
    return "\n".join(lines)


def compact_result_for_chat(result: dict[str, Any]) -> dict[str, Any]:
    boxes = []
    for box in result.get("boxes", []):
        boxes.append(
            {
                "class_name": box.get("class_name"),
                "confidence": box.get("confidence"),
                "bbox_xyxy": box.get("bbox_xyxy"),
                "area_ratio": box.get("area_ratio"),
                "risk_level": box.get("risk_level"),
                "review_suggestion": box.get("review_suggestion"),
            }
        )
    return {
        "model_name": result.get("model_name"),
        "model_type": result.get("model_type"),
        "status": result.get("status"),
        "runtime_mode": result.get("runtime_mode"),
        "device": result.get("device"),
        "box_count": result.get("box_count", 0),
        "avg_confidence": result.get("avg_confidence", 0.0),
        "max_confidence": result.get("max_confidence", 0.0),
        "inference_time_ms": result.get("inference_time_ms", 0.0),
        "boxes": boxes,
        "review_suggestions": result.get("review_suggestions", []),
        "error_message": result.get("error_message", ""),
    }


def chat_context_payload(detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> dict[str, Any]:
    current_detection = compact_result_for_chat(detection) if isinstance(detection, dict) and detection else None
    model_comparison = [
        compact_result_for_chat(item)
        for item in (comparison or [])
        if isinstance(item, dict)
    ]
    return {
        "current_detection": current_detection,
        "model_comparison": model_comparison,
        "disclaimer": DISCLAIMER,
    }


def is_lifestyle_question(question: str) -> bool:
    keywords = (
        "生活", "日常", "平时", "注意", "护理", "饮食", "刷牙", "牙线", "含氟", "漱口", "口腔卫生",
        "怎么保护", "如何保护", "怎么应对", "如何应对", "需要注意什么", "注意什么",
        "避免", "习惯", "复查", "就诊前", "就诊后", "为什么", "原因", "好处",
    )
    return any(word in question for word in keywords)


def lifestyle_guidance_answer(question: str, detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> str:
    question = chat_content_to_text(question)
    ctx_results = comparison if comparison else ([detection] if detection else [])
    ok = successful_results([r for r in ctx_results if isinstance(r, dict)])
    detected_classes: list[str] = []
    for result in ok:
        for box in result.get("boxes", []):
            class_name = box.get("class_name")
            if class_name and class_name not in detected_classes:
                detected_classes.append(class_name)

    lines = ["云端问答暂不可用，已切换为本地规则分析。", ""]
    if any(word in question for word in ("为什么", "原因", "好处")):
        lines.extend(
            [
                "保持良好口腔卫生的核心目的，是减少牙菌斑和食物残渣长期停留在牙面、牙缝和牙龈边缘，从而降低龋坏和牙龈问题继续发展的风险。",
                "",
                "- 早晚刷牙：可以清除牙面和牙龈边缘的牙菌斑，减少细菌持续产酸对牙齿硬组织的影响。",
                "- 含氟牙膏：氟化物有助于增强牙釉质抗酸能力，并促进早期脱矿区域再矿化。",
                "- 每次至少 2 分钟：时间太短容易漏刷牙齿内侧、咬合面和后牙区域，清洁不充分。",
                "- 清洁各个牙面：龋坏和牙龈问题常出现在不易刷到的位置，只刷正面不够。",
                "- 饭后漱口：可以减少食物残渣和酸性环境停留时间，但不能替代刷牙和牙线。",
                "- 牙线或牙缝刷：牙刷很难进入牙缝，牙线可以帮助清除邻面残渣和菌斑。",
                "",
            ]
        )
    lines.append("结合当前检测结果，可以参考下面的复核和护理重点：")
    if detected_classes:
        lines.append(f"- 当前模型提示的疑似类别包括：{'、'.join(detected_classes)}。建议带着检测截图和原始影像尽快让口腔医生复核。")
    else:
        lines.append("- 当前没有可用于归纳疑似类别的成功检测结果，建议先完成检测或直接就医复核。")
    lines.extend(
        [
            "- 保持口腔清洁：每天早晚刷牙，使用牙线或牙缝刷清洁牙缝，饭后可用清水漱口。",
            "- 减少刺激：少吃高糖、过黏、过硬食物，避免频繁冷热刺激；如果咀嚼疼痛，先减少患侧咀嚼。",
            "- 观察症状：记录疼痛、肿胀、出血、口臭、牙齿松动、冷热敏感等变化，便于复诊沟通。",
            "- 不自行处理：不要自行挤压肿胀部位，不要随意服用或停用抗生素、止痛药，药物使用应听从医生建议。",
            "- 及时复核：如果出现明显疼痛、面部肿胀、发热、流脓、张口受限或症状快速加重，应尽快到正规口腔科就诊。",
            "",
            DISCLAIMER,
        ]
    )
    return "\n".join(lines)


def local_rule_answer(question: str, detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> str:
    question = chat_content_to_text(question)
    ctx_results = comparison if comparison else ([detection] if detection else [])
    ok = successful_results([r for r in ctx_results if isinstance(r, dict)])
    lines = ["云端问答暂不可用，已切换为本地规则分析。"]
    if is_treatment_question(question):
        return safe_treatment_answer(question, detection, comparison)
    elif is_lifestyle_question(question):
        return lifestyle_guidance_answer(question, detection, comparison)
    elif not ok:
        lines.append("当前没有成功的真实模型推理结果可用于分析。")
    elif "哪些" in question or "检测" in question or "区域" in question:
        for result in ok:
            lines.append(f"{result['model_name']} 检出 {result['box_count']} 个疑似区域。")
            for i, box in enumerate(result.get("boxes", []), 1):
                lines.append(f"- 目标 {i}：{box['class_name']}，置信度 {box['confidence']:.3f}，{box['risk_level']}。")
    elif "复核" in question:
        for result in ok:
            review_boxes = [b for b in result.get("boxes", []) if b["risk_level"] != "可信度较高"]
            lines.append(f"{result['model_name']} 有 {len(review_boxes)} 个疑似区域建议人工复核。")
    elif "哪个模型" in question or "适合" in question or "对比" in question:
        lines.append(compare_summary(ok).replace("### 多模型对比总结\n\n", ""))
    elif "报告" in question:
        lines.append("可在报告中心生成 Markdown 报告，内容会包含模型、疑似区域明细、耗时和人工复核建议。")
    else:
        lines.append("请围绕当前检测结果、复核建议、模型对比或报告描述提问。")
    lines.append("")
    lines.append(DISCLAIMER)
    return "\n".join(lines)


def cloud_chat(question: str, detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> tuple[str, bool]:
    question = chat_content_to_text(question)
    context = chat_context_payload(detection, comparison)
    messages = [
        {
            "role": "system",
            "content": (
                "你是口腔影像辅助识别平台中的智能问答助手。"
                "检测上下文 JSON 是患者当前辅助识别结果，回答时应优先结合这些上下文；"
                "如果用户问的是通用口腔健康、护理习惯、原理解释、术语解释或报告描述，也要直接回答，"
                "不要说自己只是展示助手、不能解释好处、不能回答健康知识。"
                "不得编造检测结果；不要把疑似区域说成确诊。"
                "若问题涉及治疗、用药、手术或处置，可以给出就诊沟通、复核重点、通用护理和风险提示，"
                "但不要给出处方、剂量、手术决策或替代医生的个体化治疗方案。"
                "请用自然、简洁、适合患者阅读的中文回答。"
            ),
        },
        {
            "role": "user",
            "content": f"检测上下文 JSON：{json.dumps(context, ensure_ascii=False)}\n\n用户问题：{question}",
        },
    ]
    try:
        response = requests.post(
            DEEPSEEK_BASE_URL,
            headers={
                "Authorization": "Bearer " + DEEPSEEK_API_KEY,
                "Content-Type": "application/json",
            },
            json={"model": DEEPSEEK_MODEL, "messages": messages, "stream": False},
            timeout=DEEPSEEK_TIMEOUT_SECONDS,
        )
        if response.status_code in {401, 403, 404} or response.status_code >= 500:
            return "", False
        response.raise_for_status()
        data = response.json()
        choices = data.get("choices")
        if not isinstance(choices, list) or not choices:
            return "", False
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if not content or not isinstance(content, str):
            return "", False
        if DISCLAIMER not in content:
            content = content.rstrip() + "\n\n" + DISCLAIMER
        return content, True
    except Exception:
        return "", False


def answer_question(message: str, history: list[Any], detection: dict[str, Any], comparison: list[dict[str, Any]]):
    user_message = chat_content_to_text(message)
    content, ok = cloud_chat(user_message, detection, comparison)
    if not ok:
        content = local_rule_answer(user_message, detection, comparison)
    history = history or []
    normalized_history: list[dict[str, str]] = []
    for item in history:
        if isinstance(item, dict) and {"role", "content"} <= set(item):
            normalized_history.append({"role": str(item["role"]), "content": chat_content_to_text(item["content"])})
        elif hasattr(item, "role") and hasattr(item, "content"):
            normalized_history.append({"role": str(item.role), "content": chat_content_to_text(item.content)})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            normalized_history.extend(
                [
                    {"role": "user", "content": chat_content_to_text(item[0])},
                    {"role": "assistant", "content": chat_content_to_text(item[1])},
                ]
            )
    normalized_history.extend(
        [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": content},
        ]
    )
    return normalized_history, ""


def make_report_markdown(detection: dict[str, Any] | None, comparison: list[dict[str, Any]] | None) -> str:
    lines = [
        "# 牙齿病变疑似区域辅助识别报告",
        "",
        f"- 检测时间：{now_iso()}",
        "- 项目名称：牙齿病变目标区域识别与辅助分析平台",
        "- 运行设备：CPU",
        "",
    ]
    if detection:
        lines.extend(
            [
                "## 当前检测结果",
                f"- 使用模型：{detection.get('model_name', '-')}",
                f"- 模型运行模式：{detection.get('runtime_mode', '-')}",
                f"- 推理状态：{STATUS_LABELS.get(detection.get('status'), '-')}",
                f"- 图像信息：{detection.get('image_info', {})}",
                f"- 疑似区域数量：{detection.get('box_count', 0)}",
                f"- 推理耗时：{detection.get('inference_time_ms', 0)} ms",
                "",
                "### 检测目标明细",
                "| 序号 | 类别 | 置信度 | 坐标 | 面积占比 | 风险等级 | 复核建议 |",
                "|---:|---|---:|---|---:|---|---|",
            ]
        )
        for i, box in enumerate(detection.get("boxes", []), 1):
            lines.append(
                f"| {i} | {box['class_name']} | {box['confidence']:.3f} | {box['bbox_xyxy']} | "
                f"{box['area_ratio']:.2%} | {box['risk_level']} | {box['review_suggestion']} |"
            )
        if not detection.get("boxes"):
            lines.append("| - | - | - | - | - | - | 未生成检测目标 |")
        lines.append("")
    if comparison:
        lines.extend(
            [
                "## 多模型对比结果",
                "| 模型 | 类型 | 状态 | 检测框数量 | 平均置信度 | 最高置信度 | 推理耗时(ms) |",
                "|---|---|---|---:|---:|---:|---:|",
            ]
        )
        for row in compare_rows(comparison):
            lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |")
        lines.extend(["", compare_summary(comparison), ""])
    lines.extend(
        [
            "## 系统自动分析",
            "本报告根据模型输出的疑似区域、置信度和复核规则自动生成，仅用于科研展示和辅助识别。",
            "",
            "## 人工复核建议",
            "建议由专业人员结合原始影像和其他资料对疑似区域进行复核。",
            "",
            "## 免责声明",
            DISCLAIMER,
        ]
    )
    return "\n".join(lines)


def generate_report(detection: dict[str, Any], comparison: list[dict[str, Any]]):
    ensure_dirs()
    markdown = make_report_markdown(detection, comparison)
    filename = f"dental_aux_report_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.md"
    path = REPORT_DIR / filename
    path.write_text(markdown, encoding="utf-8")
    return markdown, str(path)


def dashboard_stats() -> dict[str, Any]:
    history = load_history()
    events = history.get("events", [])
    image_tasks = len([e for e in events if e.get("type") in {"single_detection", "model_comparison"}])
    failure_count = 0
    target_count = 0
    confs = []
    times_by_model: dict[str, list[float]] = {}
    conf_by_model: dict[str, list[float]] = {}
    risk_counts = {"可信度较高": 0, "建议人工复核": 0, "强烈建议人工复核": 0}
    last_detection = None
    last_comparison = None

    def visit(result: dict[str, Any]) -> None:
        nonlocal failure_count, target_count, last_detection
        if not isinstance(result, dict):
            return
        if result.get("status") == "success" and result.get("runtime_mode") == "real_yolo_cpu":
            last_detection = result
            target_count += int(result.get("box_count", 0))
            if result.get("box_count", 0):
                confs.append(float(result.get("avg_confidence", 0.0)))
                conf_by_model.setdefault(result["model_name"], []).append(float(result.get("avg_confidence", 0.0)))
            times_by_model.setdefault(result["model_name"], []).append(float(result.get("inference_time_ms", 0.0)))
            for box in result.get("boxes", []):
                risk_counts[box.get("risk_level", "建议人工复核")] = risk_counts.get(box.get("risk_level"), 0) + 1
        else:
            failure_count += 1

    for event in events:
        if event.get("type") == "single_detection":
            visit(event.get("result", {}))
        elif event.get("type") == "model_comparison":
            last_comparison = event.get("results", [])
            for result in event.get("results", []):
                visit(result)

    return {
        "image_tasks": image_tasks,
        "target_count": target_count,
        "failure_count": failure_count,
        "avg_confidence": sum(confs) / len(confs) if confs else 0.0,
        "times_by_model": {k: sum(v) / len(v) for k, v in times_by_model.items() if v},
        "conf_by_model": {k: sum(v) / len(v) for k, v in conf_by_model.items() if v},
        "risk_counts": risk_counts,
        "last_detection": last_detection,
        "last_comparison": last_comparison,
    }


def dashboard_markdown() -> str:
    stats = dashboard_stats()
    lines = [
        "## 首页 Dashboard",
        f"- 当前运行设备：CPU",
        f"- 累计检测图片任务数：{stats['image_tasks']}",
        f"- 累计真实检测目标数：{stats['target_count']}",
        f"- 失败次数：{stats['failure_count']}",
        f"- 成功结果平均置信度：{stats['avg_confidence']:.3f}" if stats["avg_confidence"] else "- 成功结果平均置信度：-",
        "",
        "### 三个模型平均推理耗时",
    ]
    if stats["times_by_model"]:
        for name, value in stats["times_by_model"].items():
            lines.append(f"- {name}：{value:.2f} ms")
    else:
        lines.append("- 暂无成功推理记录")
    lines.extend(["", "### 三个模型平均置信度"])
    if stats["conf_by_model"]:
        for name, value in stats["conf_by_model"].items():
            lines.append(f"- {name}：{value:.3f}")
    else:
        lines.append("- 暂无成功推理记录")
    lines.extend(["", "### 风险等级统计"])
    for key, value in stats["risk_counts"].items():
        lines.append(f"- {key}：{value}")
    lines.extend(["", "### 最近一次检测摘要"])
    if stats["last_detection"]:
        r = stats["last_detection"]
        lines.append(f"- {r['model_name']}：{r['box_count']} 个疑似区域，状态 {STATUS_LABELS.get(r['status'], r['status'])}")
    else:
        lines.append("- 暂无成功检测摘要")
    lines.extend(["", "### 最近一次多模型对比摘要"])
    if stats["last_comparison"]:
        lines.append(compare_summary(stats["last_comparison"]).replace("### 多模型对比总结\n", ""))
    else:
        lines.append("- 暂无多模型对比记录")
    return "\n".join(lines)


def dashboard_chart_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    stats = dashboard_stats()
    kpi_rows = [
        {"指标": "累计检测图片任务数", "数值": int(stats["image_tasks"])},
        {"指标": "累计真实检测目标数", "数值": int(stats["target_count"])},
        {"指标": "失败次数", "数值": int(stats["failure_count"])},
        {"指标": "成功结果平均置信度(%)", "数值": round(float(stats["avg_confidence"]) * 100, 2)},
    ]
    risk_rows = [{"风险等级": key, "数量": int(value)} for key, value in stats["risk_counts"].items()]
    time_rows = [
        {"模型": name, "平均耗时(ms)": round(float(value), 2)}
        for name, value in stats["times_by_model"].items()
    ]
    conf_rows = [
        {"模型": name, "平均置信度(%)": round(float(value) * 100, 2)}
        for name, value in stats["conf_by_model"].items()
    ]
    if not time_rows:
        time_rows = [{"模型": "暂无成功推理", "平均耗时(ms)": 0.0}]
    if not conf_rows:
        conf_rows = [{"模型": "暂无成功推理", "平均置信度(%)": 0.0}]
    return (
        pd.DataFrame(kpi_rows),
        pd.DataFrame(risk_rows),
        pd.DataFrame(time_rows),
        pd.DataFrame(conf_rows),
    )


def dashboard_outputs():
    return (dashboard_markdown(), *dashboard_chart_data())


def reset_dashboard_records():
    clear_history()
    return (*dashboard_outputs(), registry_status_markdown(), {}, [])


def project_intro_markdown() -> str:
    return f"""
# 牙齿病变目标区域识别与辅助分析平台

本系统用于课程验收、科研展示和牙齿病变疑似区域辅助识别。系统会自动扫描当前仓库已有 YOLO 权重，并在 CPU 环境下运行真实推理。

## 使用方式

```bash
python app.py
```

## 权重发现

系统会递归扫描当前项目中的 `.pt` 文件，优先使用 `results/**/weights/best.pt`，并结合目录名、README、args.yaml 和关键词自动匹配三个展示模型。

## 云端问答

演示版本使用代码内配置的 API Key，正式部署建议改为环境变量或密钥管理服务。没有大模型接口、接口不可用或网络异常时，会自动降级为本地规则问答。

## CPU 推理说明

所有 YOLO 推理显式使用 CPU，不要求 GPU。

## 免责声明

{DISCLAIMER}
"""


def build_app() -> gr.Blocks:
    refresh_model_registry()
    with gr.Blocks(title="牙齿病变目标区域识别与辅助分析平台") as demo:
        current_detection = gr.State({})
        current_comparison = gr.State([])

        gr.Markdown("# 牙齿病变目标区域识别与辅助分析平台\n面向课程验收和科研展示的辅助识别系统。")

        with gr.Tab("首页 Dashboard"):
            dashboard_initial, kpi_initial, risk_initial, time_initial, conf_initial = dashboard_outputs()
            dashboard = gr.Markdown(dashboard_initial)
            with gr.Row():
                kpi_chart = gr.BarPlot(
                    kpi_initial,
                    x="指标",
                    y="数值",
                    title="核心指标总览",
                    y_title="数值",
                    height=260,
                    x_label_angle=-20,
                )
                risk_chart = gr.BarPlot(
                    risk_initial,
                    x="风险等级",
                    y="数量",
                    title="风险等级数量统计",
                    y_title="数量",
                    height=260,
                )
            with gr.Row():
                time_chart = gr.BarPlot(
                    time_initial,
                    x="模型",
                    y="平均耗时(ms)",
                    title="模型平均推理耗时",
                    y_title="ms",
                    height=280,
                    x_label_angle=-20,
                )
                conf_chart = gr.BarPlot(
                    conf_initial,
                    x="模型",
                    y="平均置信度(%)",
                    title="模型平均置信度",
                    y_title="%",
                    height=280,
                    x_label_angle=-20,
                )
            model_status = gr.Markdown(registry_status_markdown())
            with gr.Row():
                refresh_btn = gr.Button("刷新 Dashboard")
                clear_history_btn = gr.Button("清空所有记录，回到初始记录")
            refresh_btn.click(
                lambda: (*dashboard_outputs(), registry_status_markdown()),
                outputs=[dashboard, kpi_chart, risk_chart, time_chart, conf_chart, model_status],
            )
            clear_history_btn.click(
                reset_dashboard_records,
                outputs=[
                    dashboard,
                    kpi_chart,
                    risk_chart,
                    time_chart,
                    conf_chart,
                    model_status,
                    current_detection,
                    current_comparison,
                ],
            )

        with gr.Tab("图像检测"):
            with gr.Row():
                with gr.Column(scale=1):
                    det_image = gr.Image(type="pil", label="上传牙齿或口腔图像")
                    det_model = gr.Dropdown(model_options(), value=model_options()[0], label="选择模型")
                    det_conf = gr.Slider(0.05, 0.95, value=0.25, step=0.05, label="置信度阈值")
                    det_iou = gr.Slider(0.1, 0.9, value=0.7, step=0.05, label="IoU 阈值")
                    det_btn = gr.Button("运行检测", variant="primary")
                with gr.Column(scale=2):
                    det_output = gr.Image(type="pil", label="检测结果图")
                    det_explain = gr.Markdown("等待检测。")
            det_table = gr.Dataframe(
                headers=["序号", "类别", "置信度", "坐标", "面积占比", "风险等级", "复核建议"],
                label="结构化检测结果",
                wrap=True,
            )
            det_steps = gr.Dataframe(headers=["步骤", "状态", "耗时(ms)", "说明"], label="检测过程可视化", wrap=True)
            det_btn.click(
                run_single_detection,
                inputs=[det_image, det_model, det_conf, det_iou],
                outputs=[
                    det_output,
                    det_table,
                    det_explain,
                    det_steps,
                    current_detection,
                    dashboard,
                    kpi_chart,
                    risk_chart,
                    time_chart,
                    conf_chart,
                    model_status,
                ],
            )
            det_image.clear(
                reset_single_detection_outputs,
                outputs=[
                    det_output,
                    det_table,
                    det_explain,
                    det_steps,
                    current_detection,
                    dashboard,
                    kpi_chart,
                    risk_chart,
                    time_chart,
                    conf_chart,
                    model_status,
                ],
            )

        with gr.Tab("多模型对比"):
            cmp_image = gr.Image(type="pil", label="上传同一张图像")
            with gr.Row():
                cmp_conf = gr.Slider(0.05, 0.95, value=0.25, step=0.05, label="置信度阈值")
                cmp_iou = gr.Slider(0.1, 0.9, value=0.7, step=0.05, label="IoU 阈值")
            cmp_btn = gr.Button("一键运行三个模型", variant="primary")
            with gr.Row():
                cmp_img1 = gr.Image(type="pil", label="均衡型基线模型")
                cmp_img2 = gr.Image(type="pil", label="高精度牙齿病变定位模型")
                cmp_img3 = gr.Image(type="pil", label="高召回牙齿病变检测模型")
            cmp_table = gr.Dataframe(
                headers=[
                    "模型名称",
                    "模型类型",
                    "推理状态",
                    "检测框数量",
                    "平均置信度",
                    "最高置信度",
                    "推理耗时(ms)",
                    "复核建议数量",
                    "模型特点说明",
                    "失败原因",
                ],
                label="多模型对比表",
                wrap=True,
            )
            cmp_summary = gr.Markdown("等待对比。")
            cmp_btn.click(
                run_model_comparison,
                inputs=[cmp_image, cmp_conf, cmp_iou],
                outputs=[
                    cmp_img1,
                    cmp_img2,
                    cmp_img3,
                    cmp_table,
                    cmp_summary,
                    current_comparison,
                    dashboard,
                    kpi_chart,
                    risk_chart,
                    time_chart,
                    conf_chart,
                    model_status,
                ],
            )
            cmp_image.clear(
                reset_model_comparison_outputs,
                outputs=[
                    cmp_img1,
                    cmp_img2,
                    cmp_img3,
                    cmp_table,
                    cmp_summary,
                    current_comparison,
                    dashboard,
                    kpi_chart,
                    risk_chart,
                    time_chart,
                    conf_chart,
                    model_status,
                ],
            )

        with gr.Tab("智能问答助手"):
            gr.Markdown("可围绕当前检测结果或多模型对比结果提问。")
            chatbot = gr.Chatbot(label="智能问答助手")
            chat_input = gr.Textbox(label="问题", placeholder="例如：哪些目标需要人工复核？")
            chat_btn = gr.Button("发送")
            chat_btn.click(answer_question, inputs=[chat_input, chatbot, current_detection, current_comparison], outputs=[chatbot, chat_input])
            chat_input.submit(answer_question, inputs=[chat_input, chatbot, current_detection, current_comparison], outputs=[chatbot, chat_input])

        with gr.Tab("报告中心"):
            report_btn = gr.Button("生成报告", variant="primary")
            report_preview = gr.Markdown("尚未生成报告。")
            report_file = gr.File(label="下载 Markdown 报告")
            report_btn.click(generate_report, inputs=[current_detection, current_comparison], outputs=[report_preview, report_file])

        with gr.Tab("项目说明"):
            gr.Markdown(project_intro_markdown())

    return demo


def find_free_port(start_port: int = 7860, attempts: int = 20) -> int:
    for port in range(start_port, start_port + attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return start_port


if __name__ == "__main__":
    ensure_dirs()
    app = build_app()
    app.launch(server_name="127.0.0.1", server_port=find_free_port())
