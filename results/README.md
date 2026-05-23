# 2026-05-23 YOLOv8 Dental Results

本目录集中保存今天的核心实验结果、训练日志和说明文档。项目源码当前在 `/root/yolov8`，本结果目录实际位置为 `/root/yolov8/results`。`/root/results` 保留为软链接，原 runs 目录下的结果路径也保留软链接，便于旧路径继续访问。

## 实验链路

| 顺序 | 结果目录 | 目的 | 结论 | 下一步依据 |
|---:|---|---|---|---|
| 1 | `v3_exp00b_yolov8n_baseline_e200_i960_b40` | 建立 YOLOv8n 200 epoch baseline | 总体 mAP50-95 为 0.4121；Caries 和 Periapical_Lesion 的高 IoU 定位偏弱 | 先尝试结构侧 SPDConv-neck-P4 和 loss 侧定位优化 |
| 2 | `v3_exp01c2_yolov8n_spdconv_neck_p4_e200_i960_b40` | 用 SPDConv-neck-P4 增强 Neck 下采样信息 | Recall 和 Caries 有提升，但 Precision、Periapical、总体 mAP50-95 低于 baseline | 结构扰动收益不足，转向 bbox regression loss |
| 3 | `v3_exp01_loss_piou_yolov8n_e200_i960_b40` | 用 PIoU 提升定位质量 | Precision/Recall/mAP50/F1 提升，Caries 和 Periapical 有收益，但 Impacted 明显下降 | 说明 PIoU 不适合全类别使用，设计 class-aware Hybrid 保护 Impacted |
| 4 | `v3_exp02_loss_hybrid_ciou_piou_yolov8n_e200_i960_b40_p30` | Caries/Periapical 使用 CIoU+PIoU，Impacted 保持 CIoU | Impacted 成功回升并超过 baseline，但 Periapical 和 Recall/F1 明显下降 | 证明 PIoU 主线不稳，改用原始 CIoU + NWD 辅助 loss |
| 5 | `v3_exp03_loss_ciou_nwd_cls01_yolov8n_e200_i960_b40_p30` | 主 loss 保持 CIoU，只对 Caries/Periapical 添加 NWD 辅助项 | Caries 达到今日最高 mAP50-95，但 Periapical 和 Impacted 下降，总体 mAP50-95 未超 baseline | loss 主线暂不成立，后续应回到结构优化、数据/预处理，或只针对 Caries 做更弱辅助 loss |

## 总体指标对比

| 方案 | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| baseline e200 | 0.6109 | 0.7002 | 0.6767 | 0.4121 | 0.6525 |
| SPDConv-neck-P4 e200 | 0.5770 | 0.7160 | 0.6750 | 0.4080 | 0.6389 |
| PIoU e200 | 0.6234 | 0.7217 | 0.7030 | 0.4088 | 0.6690 |
| Hybrid CIoU+PIoU p30 | 0.6356 | 0.6477 | 0.6863 | 0.4104 | 0.6416 |
| CIoU+NWD cls01 p30 | 0.7251 | 0.6103 | 0.6985 | 0.4074 | 0.6627 |

## 关键类别 mAP50-95 对比

| 方案 | Caries | Periapical_Lesion | Impacted |
|---|---:|---:|---:|
| baseline e200 | 0.3580 | 0.2750 | 0.6030 |
| SPDConv-neck-P4 e200 | 0.4040 | 0.2520 | 0.5680 |
| PIoU e200 | 0.4063 | 0.2773 | 0.5428 |
| Hybrid CIoU+PIoU p30 | 0.3779 | 0.2443 | 0.6090 |
| CIoU+NWD cls01 p30 | 0.4226 | 0.2546 | 0.5450 |

## 闭环结论

今天的实验链路是逐步收敛的：baseline 暴露 Caries/Periapical 的高 IoU 定位不足；SPDConv-neck-P4 说明单点结构增强能提高部分小目标类但会牺牲整体稳定性；PIoU 证明定位 loss 对 Caries 有效，但会明显伤害 Impacted；Hybrid 验证了类别保护可以恢复 Impacted，但 Periapical 和 Recall/F1 下降；CIoU+NWD cls01 进一步证明 NWD 对 Caries 更有效，却仍无法同时保住 Periapical 和 Impacted。

因此，当前证据不支持继续把 PIoU/Hybrid/NWD 作为统一 loss 主线。最有价值的发现是：Caries 对定位增强较敏感，Impacted 对 PIoU/NWD 类 loss 扰动敏感，Periapical_Lesion 不是简单 bbox loss 就能稳定改善。下一步更合理的是回到结构优化或数据/预处理优化；如果继续 loss 方向，应只做更弱、更窄的 Caries-specific auxiliary loss，而不是继续扩大到多类别。
