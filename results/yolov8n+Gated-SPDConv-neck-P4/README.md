# YOLOv8n + gated SPDConv-neck-P4 e50

## Experiment Purpose

Test a gated SPDConv branch that keeps the original Conv path and adds weak SPDConv information.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01d_yolov8n_gated_spdconv_neck_p4_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 31 |
| Precision | 0.60302 |
| Recall | 0.69132 |
| mAP50 | 0.66872 |
| mAP50-95 | 0.40477 |
| F1 | 0.64416 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.65885 | 0.64792 | 0.66290 | 0.38127 | 0.65334 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.60302 | 0.69132 | 0.66872 | 0.40477 | 0.64416 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | -0.01676 |
| Recall | -0.03987 |
| mAP50 | -0.02901 |
| mAP50-95 | -0.01545 |
| F1 | -0.02673 |

## Analysis

This was designed to reduce disruption from direct SPDConv insertion.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

It did not beat baseline or the plain P4 variant, so it was not kept as the main branch.
