from __future__ import annotations

from typing import Any
from xml.sax.saxutils import escape as xml_escape

import gradio as gr

DETECTION_EMPTY_STATES = {
    "single": {
        "title": "单图精检",
        "description": "适合对单张牙齿影像进行快速定位与细致解读，比多模型对比更轻量，比批量检测更适合逐张查看重点区域。",
        "hint": "上传一张牙齿影像开始检测｜支持 JPG / PNG",
        "icon": "single",
    },
    "compare": {
        "title": "多模型会诊",
        "description": "适合对同一张影像进行多模型复核，帮助比较不同模型的检测差异，比单图检测更稳健，比批量检测更适合结果可信度判断。",
        "hint": "上传一张影像进行多模型对比｜支持 JPG / PNG",
        "icon": "compare",
    },
    "batch": {
        "title": "批量筛查",
        "description": "适合一次处理多张牙齿影像并快速汇总结果，比单图检测效率更高，比多模型对比更适合大批量初筛。",
        "hint": "上传多张影像开始批量检测｜支持 JPG / PNG",
        "icon": "batch",
    },
}

DETECTION_EMPTY_ICONS = {
    "single": """
      <svg viewBox="0 0 48 48" aria-hidden="true">
        <rect x="8" y="10" width="32" height="28" rx="8"></rect>
        <path d="M17 26c2.1-4 5.4-4 7-1.8 1.6-2.2 4.9-2.2 7 1.8"></path>
        <path d="M19 26.5c.6 5 1.9 8.5 4 8.5 1.1 0 1-2.8 1-4.3 0 1.5-.1 4.3 1 4.3 2.1 0 3.4-3.5 4-8.5"></path>
        <path d="M14 18h6M28 18h6M14 30v4h4M34 30v4h-4"></path>
      </svg>
    """,
    "compare": """
      <svg viewBox="0 0 48 48" aria-hidden="true">
        <rect x="9" y="12" width="22" height="18" rx="6"></rect>
        <rect x="17" y="18" width="22" height="18" rx="6"></rect>
        <path d="M15 24h10M23 30h10M25 12l5-5M30 7h5v5"></path>
      </svg>
    """,
    "batch": """
      <svg viewBox="0 0 48 48" aria-hidden="true">
        <rect x="8" y="9" width="22" height="26" rx="6"></rect>
        <rect x="16" y="15" width="22" height="26" rx="6"></rect>
        <path d="M14 18h8M22 24h10M22 30h10M22 36h7"></path>
      </svg>
    """,
}

DETECTION_READY_STATES = {
    "single": ("影像已就绪", "确认模型与阈值后运行单图精检。"),
    "compare": ("影像已就绪", "确认阈值后运行三个模型，结果将以滑动对比方式展示。"),
    "batch": ("任务已就绪", "确认模型与阈值后开始批量筛查，系统将逐张更新任务状态。"),
}

def build_detection_empty_state(kind: str) -> str:
    state = DETECTION_EMPTY_STATES.get(kind, DETECTION_EMPTY_STATES["single"])
    icon = DETECTION_EMPTY_ICONS.get(state.get("icon", ""), DETECTION_EMPTY_ICONS["single"])
    return "\n".join(
        [
            f"<div class='detection-empty-state detection-empty-{xml_escape(kind)}'>",
            f"  <div class='detection-empty-icon'>{icon}</div>",
            "  <div class='detection-empty-copy'>",
            f"    <div class='detection-empty-title'>{xml_escape(state['title'])}</div>",
            f"    <div class='detection-empty-desc'>{xml_escape(state['description'])}</div>",
            f"    <div class='detection-empty-hint'>{xml_escape(state['hint'])}</div>",
            "  </div>",
            "</div>",
        ]
    )

def build_detection_progress_state(percent: float, title: str, detail: str) -> str:
    bounded_percent = max(0, min(100, int(round(float(percent)))))
    return "\n".join(
        [
            f"<div class='detection-progress-state' role='status' aria-live='polite' aria-label='{xml_escape(title)}，进度 {bounded_percent}%'>",
            "  <div class='detection-progress-head'>",
            f"    <span>{xml_escape(title)}</span>",
            f"    <b>{bounded_percent}%</b>",
            "  </div>",
            "  <div class='detection-progress-track' aria-hidden='true'>",
            f"    <div class='detection-progress-fill' style='width: {bounded_percent}%;'></div>",
            "  </div>",
            f"  <div class='detection-progress-detail'>{xml_escape(detail)}</div>",
            "</div>",
        ]
    )

def build_detection_ready_state(kind: str) -> str:
    title, detail = DETECTION_READY_STATES.get(kind, DETECTION_READY_STATES["single"])
    return "\n".join(
        [
            f"<div class='detection-ready-state' role='status' data-ready-kind='{xml_escape(kind)}'>",
            "  <span class='detection-ready-check' aria-hidden='true'>✓</span>",
            "  <div>",
            f"    <b>{xml_escape(title)}</b>",
            f"    <small>{xml_escape(detail)}</small>",
            "  </div>",
            "</div>",
        ]
    )

def detection_progress_update(percent: float, title: str, detail: str) -> Any:
    return gr.update(value=build_detection_progress_state(percent, title, detail), visible=True)

def detection_progress_hide() -> Any:
    return gr.update(value="", visible=False)

def detection_empty_state_update(kind: str, visible: bool) -> Any:
    return gr.update(value=build_detection_empty_state(kind) if visible else "", visible=visible)

def detection_empty_state_for_upload(value: Any, kind: str) -> Any:
    if value:
        return gr.update(value=build_detection_ready_state(kind), visible=True)
    return detection_empty_state_update(kind, True)

def single_empty_state_for_upload(image: Any) -> Any:
    return detection_empty_state_for_upload(image, "single")

def compare_empty_state_for_upload(image: Any) -> Any:
    return detection_empty_state_for_upload(image, "compare")

def batch_empty_state_for_upload(files: list[Any] | None) -> Any:
    return detection_empty_state_for_upload(files, "batch")
