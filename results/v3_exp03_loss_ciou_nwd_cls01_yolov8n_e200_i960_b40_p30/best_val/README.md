# CIoU+NWD cls01 best.pt Independent Validation

该目录保存 CIoU + class-aware NWD auxiliary loss 实验 `best.pt` 的独立重新验证结果。验证使用同一数据集、`imgsz=960`、`batch=40`、`plots=False`。

核心结果：all Precision 0.7251，Recall 0.6103，mAP50 0.6985，mAP50-95 0.4074，F1 0.6627。

该验证结果显示 NWD 明显提升 Caries 的 mAP50-95，但 Periapical_Lesion 和 Impacted 下降，总体 mAP50-95 未超过 baseline。
