# SPDConv-neck-P4 e200

## 目的
测试结构优化方向：在 Neck 的 P4 相关下采样位置引入 SPDConv，尝试补充细粒度信息，同时观察它是否能超过 baseline e200。

## 训练设置
- 模型：YOLOv8n + SPDConv-neck-P4
- epochs：200
- 初始 patience：0，后续按要求改为 patience=30 并从 last.pt 继续
- best epoch：83
- 实际停止 epoch：113
- 是否早停：是，连续 30 epoch 无提升后停止
- 结果目录：`/root/results/v3_exp01c2_yolov8n_spdconv_neck_p4_e200_i960_b40`
- 日志：`logs/v3_e200_pair_baseline_spdconvp4.log`，`logs/v3_exp01c2_resume_patience30.log`

## best.pt 重新验证指标
| 类别 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| all | 0.5770 | 0.7160 | 0.6750 | 0.4080 | 0.6389 |
| Caries | 0.4320 | 0.6620 | 0.5910 | 0.4040 | 0.5228 |
| Periapical_Lesion | 0.6170 | 0.5610 | 0.5740 | 0.2520 | 0.5877 |
| Impacted | 0.6820 | 0.9250 | 0.8600 | 0.5680 | 0.7851 |

## 与 baseline 对比
| 指标 | SPDConv-neck-P4 | baseline | 差值 |
|---|---:|---:|---:|
| Precision | 0.5770 | 0.6109 | -0.0339 |
| Recall | 0.7160 | 0.7002 | +0.0158 |
| mAP50 | 0.6750 | 0.6767 | -0.0017 |
| mAP50-95 | 0.4080 | 0.4121 | -0.0041 |
| F1 | 0.6389 | 0.6525 | -0.0136 |

## 指标分析
SPDConv-neck-P4 提高了 Recall，并且 Caries 的 mAP50-95 从 0.3580 提升到 0.4040，说明细粒度信息对龋齿类别有帮助。但 Precision、总体 mAP50-95 和 Periapical_Lesion 均低于 baseline，Impacted 也从 0.6030 降到 0.5680。

## 推动的下一步
因为结构侧 SPDConv 没有稳定超过 baseline，下一步转向 bbox regression loss：PIoU。目标是直接改善高 IoU 定位质量，而不是继续增加结构扰动。
