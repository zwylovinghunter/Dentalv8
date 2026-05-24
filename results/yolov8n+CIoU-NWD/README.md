# CIoU + Class-aware NWD Auxiliary Loss

## 目的

本实验承接 Hybrid CIoU+PIoU 的失败原因：Hybrid 可以恢复 Impacted，但 Periapical_Lesion 和 Recall/F1 明显下降，说明继续沿 PIoU 主线收益不稳。因此本实验不再使用 PIoU，主 box loss 回到原始 CIoU，只额外加入较弱的 NWD auxiliary loss。

NWD 只作用于 class 0 Caries 和 class 1 Periapical_Lesion，class 2 Impacted 的 NWD 权重为 0，目标是改善小病灶定位，同时尽量不扰动 Impacted。

## Loss 设计

- 主损失：`ciou_loss = 1 - CIoU`
- 辅助损失：`nwd_loss = 1 - exp(-distance / 12.8)`
- class 0 Caries：`CIoU + 0.2 * NWD`
- class 1 Periapical_Lesion：`CIoU + 0.2 * NWD`
- class 2 Impacted：`CIoU only`

## 训练设置

- 模型：YOLOv8n baseline 结构
- box_loss：ciou_nwd_cls01
- epochs：200
- patience：30
- cache：False
- workers：8
- 是否早停：是
- 实际训练 epoch：80
- best epoch：50
- 结果目录：`/root/yolov8/results/v3_exp03_loss_ciou_nwd_cls01_yolov8n_e200_i960_b40_p30`
- 独立验证目录：`best_val/`
- 日志：`logs/v3_exp03_loss_ciou_nwd_cls01_yolov8n_e200_i960_b40_p30.log`

## best.pt 独立验证指标

| 类别 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| all | 0.7251 | 0.6103 | 0.6985 | 0.4074 | 0.6627 |
| Caries | 0.6064 | 0.5188 | 0.6120 | 0.4226 | 0.5592 |
| Periapical_Lesion | 0.7752 | 0.4467 | 0.5960 | 0.2546 | 0.5668 |
| Impacted | 0.7936 | 0.8653 | 0.8875 | 0.5450 | 0.8279 |

## 总体对比

| 方案 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| baseline | 0.6109 | 0.7002 | 0.6767 | 0.4121 | 0.6525 |
| PIoU | 0.6234 | 0.7217 | 0.7030 | 0.4088 | 0.6690 |
| Hybrid CIoU+PIoU | 0.6356 | 0.6477 | 0.6863 | 0.4104 | 0.6416 |
| CIoU+NWD cls01 | 0.7251 | 0.6103 | 0.6985 | 0.4074 | 0.6627 |

## 差值分析

| 对比 | ΔPrecision | ΔRecall | ΔmAP50 | ΔmAP50-95 | ΔF1 |
|---|---:|---:|---:|---:|---:|
| NWD - baseline | +0.1142 | -0.0899 | +0.0218 | -0.0047 | +0.0102 |
| NWD - PIoU | +0.1017 | -0.1114 | -0.0045 | -0.0014 | -0.0063 |
| NWD - Hybrid | +0.0895 | -0.0374 | +0.0122 | -0.0030 | +0.0211 |

## 关键类别分析

| 类别 | baseline mAP50-95 | PIoU mAP50-95 | Hybrid mAP50-95 | NWD mAP50-95 | 结论 |
|---|---:|---:|---:|---:|---|
| Caries | 0.3580 | 0.4063 | 0.3779 | 0.4226 | 明显最好，NWD 对 Caries 有效 |
| Periapical_Lesion | 0.2750 | 0.2773 | 0.2443 | 0.2546 | 低于 baseline，NWD 没解决 Periapical 定位问题 |
| Impacted | 0.6030 | 0.5428 | 0.6090 | 0.5450 | 仍明显低于 baseline/Hybrid，虽然未直接加 NWD 但训练动态仍影响该类 |

## 指标分析

CIoU+NWD cls01 的 Precision 很高，F1 和 mAP50 也超过 baseline，说明模型预测更保守、更准，粗定位能力提升。但 Recall 明显下降，mAP50-95 未超过 baseline。类别上，Caries 获得今天最高 mAP50-95，说明 NWD 对龋齿小目标定位有效；Periapical_Lesion 和 Impacted 下降，导致总体 mAP50-95 仍失败。

## 和上一步的闭环关系

上一步 Hybrid 的目的，是验证“只保护 Impacted、对 Caries/Periapical 继续用 PIoU”能否保留 PIoU 的收益。结果显示 Impacted 被救回来了，但 Periapical_Lesion 和 Recall/F1 下降。因此本实验把 PIoU 完全撤掉，改为更温和的 NWD 辅助 loss。

本实验进一步证明：Caries 的确能从定位辅助项受益，但 Periapical_Lesion 并没有被 NWD 修复，Impacted 也没有像预期那样保持 baseline 水平。这样形成了完整闭环：PIoU 能帮 Caries 但伤 Impacted；Hybrid 能救 Impacted 但伤 Periapical；NWD 能进一步帮 Caries，但仍无法同时保住 Periapical 和 Impacted。

## 最终结论

不建议把 CIoU+NWD cls01 作为当前 loss 优化主结果。它证明 NWD 对 Caries 有价值，但没有解决 Periapical_Lesion，并且 Impacted 未保持住 baseline 水平。后续如果继续 loss 方向，应考虑只针对 Caries 使用更弱辅助项；否则建议回到结构优化或数据/预处理优化。
