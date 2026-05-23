# Class-aware Hybrid CIoU + PIoU Loss p30

## 目的

基于 PIoU 的指标表现，新增类别感知混合 box loss：Caries 和 Periapical_Lesion 使用 50% CIoU + 50% PIoU；Impacted 使用 100% CIoU。目标是保留 PIoU 对 Caries/Periapical_Lesion 的定位收益，同时避免 Impacted 被 PIoU 拉低。

## 训练设置

- 模型：YOLOv8n baseline 结构
- box_loss：hybrid_piou
- epochs：200
- patience：30
- cache：False
- workers：8
- 是否早停：是
- 实际训练 epoch：66
- best epoch：36
- 结果目录：`/root/yolov8/results/v3_exp02_loss_hybrid_ciou_piou_yolov8n_e200_i960_b40_p30`
- 独立验证目录：`best_val/`
- 日志：`logs/v3_exp02_loss_hybrid_ciou_piou_yolov8n_e200_i960_b40_p30.log`

## best.pt 重新验证指标

| 类别 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| all | 0.6356 | 0.6477 | 0.6863 | 0.4104 | 0.6416 |
| Caries | 0.5458 | 0.5338 | 0.5784 | 0.3779 | 0.5398 |
| Periapical_Lesion | 0.6695 | 0.4592 | 0.5734 | 0.2443 | 0.5447 |
| Impacted | 0.6914 | 0.9500 | 0.9072 | 0.6090 | 0.8003 |

## 与前序实验对比

| 方案 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| baseline | 0.6109 | 0.7002 | 0.6767 | 0.4121 | 0.6525 |
| PIoU | 0.6234 | 0.7217 | 0.7030 | 0.4088 | 0.6690 |
| Hybrid | 0.6356 | 0.6477 | 0.6863 | 0.4104 | 0.6416 |

| 对比 | ΔPrecision | ΔRecall | ΔmAP50 | ΔmAP50-95 | ΔF1 |
|---|---:|---:|---:|---:|---:|
| Hybrid - baseline | +0.0247 | -0.0525 | +0.0096 | -0.0017 | -0.0109 |
| Hybrid - PIoU | +0.0122 | -0.0740 | -0.0167 | +0.0016 | -0.0274 |

## 关键类别分析

| 类别 | baseline mAP50-95 | PIoU mAP50-95 | Hybrid mAP50-95 | 结论 |
|---|---:|---:|---:|---|
| Caries | 0.3580 | 0.4063 | 0.3779 | 仍高于 baseline，但低于 PIoU |
| Periapical_Lesion | 0.2750 | 0.2773 | 0.2443 | 低于 baseline 和 PIoU，是 Hybrid 失败主因 |
| Impacted | 0.6030 | 0.5428 | 0.6090 | 成功恢复并略超 baseline |

## 指标分析

Hybrid 达到了恢复 Impacted 的目标，Impacted mAP50-95 从 PIoU 的 0.5428 提升到 0.6090，说明对 Impacted 关闭 PIoU 是有效的。但 Caries 的收益被削弱，Periapical_Lesion 下降明显，导致总体 mAP50-95 仍低于 baseline 0.4121。

## 推动的下一步

该结果形成了一个明确判断：PIoU 的问题不是单纯类别权重不足，而是会让 Periapical_Lesion 和整体召回变得不稳定。既然 Hybrid 已经能保护 Impacted，但仍无法解决 Periapical_Lesion，下一步不应继续 PIoU 主线。因此后续实验转为 `CIoU + Class-aware NWD Auxiliary Loss`：主 box loss 回到原始 CIoU，只对 Caries/Periapical_Lesion 添加较弱 NWD 辅助项，并让 Impacted 完全不参与 NWD。

## 后续验证结果

后续 `CIoU+NWD cls01` 的验证结果为：总体 Precision 0.7251、Recall 0.6103、mAP50 0.6985、mAP50-95 0.4074、F1 0.6627。Caries mAP50-95 提升到 0.4226，是今天最高；但 Periapical_Lesion 降到 0.2546，Impacted 降到 0.5450，总体仍低于 baseline。

这说明 Hybrid 后续选择 NWD 是合理的排查步骤，但结果证明当前 loss 优化主线仍没有闭环成功。下一步应停止扩大 loss 组合，转回结构优化、数据/预处理优化，或只做更弱的 Caries-specific 辅助 loss。
