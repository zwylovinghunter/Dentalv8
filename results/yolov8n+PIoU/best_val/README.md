# PIoU best.pt Independent Validation

该目录保存 PIoU 实验 `best.pt` 的独立重新验证结果。验证使用同一数据集、`imgsz=960`、`batch=40`、`plots=False`，用于和 baseline 进行公平对比。

核心结果：all Precision 0.6234，Recall 0.7217，mAP50 0.7030，mAP50-95 0.4088，F1 0.6690。

该验证结果支撑了后续 Hybrid 设计：PIoU 提高 Caries 和 Periapical_Lesion，但 Impacted 明显下降。
