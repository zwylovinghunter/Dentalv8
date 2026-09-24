from __future__ import annotations

CLASS_KNOWLEDGE = {
    "Caries": {
        "title": "疑似龋坏（Caries）",
        "meaning": "模型在影像中发现可能与牙体硬组织缺损或龋坏相关的局部表现。",
        "review": "建议结合原始影像、邻面关系、临床探诊和症状进行人工复核。",
        "note": "低置信度结果可能来自影像重叠、金属修复体边缘或局部噪声。",
    },
    "Periapical_Lesion": {
        "title": "疑似根尖周异常（Periapical Lesion）",
        "meaning": "模型在牙根尖周围发现可能需要关注的局部影像异常。",
        "review": "建议重点核对对应牙根、根尖周骨质表现、既往根管治疗史和临床症状。",
        "note": "模型只能提示疑似影像区域，不能判断感染、炎症阶段或治疗方案。",
    },
    "Impacted": {
        "title": "疑似阻生或埋伏牙（Impacted）",
        "meaning": "模型在影像中发现可能与阻生牙、埋伏牙或异常萌出位置相关的区域。",
        "review": "建议结合牙列位置、邻牙关系、萌出方向和全景片整体结构进行复核。",
        "note": "重叠结构、拍摄角度和牙列拥挤可能影响模型定位。",
    },
}
CLASS_ALIASES = {
    "caries": "Caries",
    "cavity": "Caries",
    "periapical": "Periapical_Lesion",
    "periapical_lesion": "Periapical_Lesion",
    "impacted": "Impacted",
}
