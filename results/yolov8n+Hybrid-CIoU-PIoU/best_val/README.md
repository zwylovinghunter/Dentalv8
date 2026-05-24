# Hybrid best.pt Independent Validation

该目录保存 Class-aware Hybrid CIoU+PIoU 实验 `best.pt` 的独立重新验证结果。验证使用同一数据集、`imgsz=960`、`batch=40`、`plots=False`。

核心结果：all Precision 0.6356，Recall 0.6477，mAP50 0.6863，mAP50-95 0.4104，F1 0.6416。

该验证结果显示 Hybrid 恢复了 Impacted，但 Periapical_Lesion 明显下降，因此没有超过 baseline 的总体 mAP50-95。
