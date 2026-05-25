# yolov8m + P2-highRecall + mosaic0.5

## 训练目标

构建一个偏高召回率的 YOLOv8m 牙齿病变检测模型，同时尽量保证 Precision、mAP50、mAP50-95 不低于 baseline 或只出现极小损失。

## 主要改动

- 模型结构：在 YOLOv8m baseline 基础上加入 P2/4 小目标检测头。
- 检测尺度：由 P3/P4/P5 改为 P2/P3/P4/P5 四尺度输出。
- 训练策略：`imgsz=960`，`mosaic=0.5`，`cos_lr=True`，`patience=30`。
- 结果目录：`results/yolov8m+P2-highRecall_mosaic05_e200_p30`。

## 训练结果

- 训练停止：EarlyStopping，第 56 epoch 停止。
- 最佳 epoch：26。
- 最佳权重：`weights/best.pt`。

## 与 yolov8m baseline 对比

| 指标 | yolov8m baseline | yolov8m + P2-highRecall | 差值 |
|---|---:|---:|---:|
| Precision | 0.63287 | 0.63668 | +0.00381 |
| Recall | 0.69198 | 0.69893 | +0.00695 |
| mAP50 | 0.67715 | 0.68744 | +0.01029 |
| mAP50-95 | 0.42257 | 0.42339 | +0.00082 |

## 结论

该模型相比 yolov8m baseline 在 Recall、Precision、mAP50、mAP50-95 上均为小幅提升，符合“高召回率，同时其他指标不降低或只极小波动”的目标。更适合作为牙齿病变初筛或漏检敏感场景的候选权重。
