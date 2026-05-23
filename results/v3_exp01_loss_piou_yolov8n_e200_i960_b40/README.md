# YOLOv8n + PIoU Loss e200

## 目的
测试 loss 优化方向：保持 YOLOv8n Backbone、Neck、Detect 完全不变，仅将 bbox regression loss 从默认 CIoU 可选替换为 PIoU。目标是改善 Caries 和 Periapical_Lesion 的高 IoU 定位质量。

## 训练设置
- 模型：YOLOv8n baseline 结构
- box_loss：piou
- epochs：200
- patience：0
- best epoch：42
- 结果目录：`/root/results/v3_exp01_loss_piou_yolov8n_e200_i960_b40`
- 独立验证目录：`best_val/`
- 日志：`logs/v3_exp01_loss_piou_yolov8n_e200_i960_b40.log`

## best.pt 重新验证指标
| 类别 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| all | 0.6234 | 0.7217 | 0.7030 | 0.4088 | 0.6690 |
| Caries | 0.4154 | 0.7267 | 0.6114 | 0.4063 | 0.5286 |
| Periapical_Lesion | 0.6631 | 0.5830 | 0.6269 | 0.2773 | 0.6205 |
| Impacted | 0.7917 | 0.8554 | 0.8708 | 0.5428 | 0.8223 |

## 与 baseline 对比
| 指标 | PIoU | baseline | 差值 |
|---|---:|---:|---:|
| Precision | 0.6234 | 0.6109 | +0.0125 |
| Recall | 0.7217 | 0.7002 | +0.0215 |
| mAP50 | 0.7030 | 0.6767 | +0.0263 |
| mAP50-95 | 0.4088 | 0.4121 | -0.0033 |
| F1 | 0.6690 | 0.6525 | +0.0165 |

## 关键类别对比
| 类别 | PIoU mAP50-95 | baseline mAP50-95 | 差值 |
|---|---:|---:|---:|
| Caries | 0.4063 | 0.3580 | +0.0483 |
| Periapical_Lesion | 0.2773 | 0.2750 | +0.0023 |
| Impacted | 0.5428 | 0.6030 | -0.0602 |

## 指标分析
PIoU 明显提升了 Precision、Recall、mAP50 和 F1，也显著提升 Caries 的 mAP50-95，并让 Periapical_Lesion 略高于 baseline。但 Impacted 的 mAP50-95 从 0.6030 降到 0.5428，拖低了总体 mAP50-95，导致整体仍没有超过 baseline。

## 推动的下一步
PIoU 的结果说明：PIoU 对 Caries 和 Periapical_Lesion 有价值，但不适合直接作用于所有类别。下一步因此设计 Class-aware Hybrid CIoU+PIoU：Caries 和 Periapical_Lesion 使用 50% PIoU，Impacted 使用 100% CIoU，目标是保留前两类收益并恢复 Impacted。
