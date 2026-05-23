# YOLOv8n Baseline e200

## 目的
建立当前 dentex_yolov8_3cls_v3 数据集上的 200 epoch YOLOv8n baseline，作为后续所有结构优化和 loss 优化的统一对照。该实验不改 Backbone、Neck、Head，也不使用额外 loss。

## 训练设置
- 模型：YOLOv8n baseline yaml
- epochs：200
- imgsz：960
- batch：40
- patience：0
- 数据：`/root/yolov8/data/dentex_yolov8_3cls_v3.yaml`
- 结果目录：`/root/results/v3_exp00b_yolov8n_baseline_e200_i960_b40`
- 日志：`logs/v3_e200_pair_baseline_spdconvp4.log`

## best 信息
训练 CSV 中 best epoch 为 59。重新验证 `best.pt` 后采用以下指标作为 baseline 对照。

## 总体指标
| Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|
| 0.6109 | 0.7002 | 0.6767 | 0.4121 | 0.6525 |

## 各类别指标
| 类别 | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| Caries | 0.4220 | 0.6620 | 0.5170 | 0.3580 |
| Periapical_Lesion | 0.6540 | 0.5890 | 0.6220 | 0.2750 |
| Impacted | 0.7570 | 0.8500 | 0.8910 | 0.6030 |

## 指标分析
总体 mAP50-95 为 0.4121，是今天所有实验需要超过的核心阈值。Caries 和 Periapical_Lesion 的 mAP50-95 偏低，尤其 Periapical_Lesion 的 mAP50 为 0.6220，但 mAP50-95 只有 0.2750，说明粗定位尚可，高 IoU 定位质量不足。

## 推动的下一步
基于这个问题，后续先尝试两条路线：结构侧 SPDConv-neck-P4，希望增强 Neck 下采样中的细粒度信息；loss 侧 PIoU，希望直接提升 bbox regression 的定位质量。
