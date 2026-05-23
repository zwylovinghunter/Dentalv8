# YOLOv8n + hybrid SPDConv-neck-P4 e50

## Experiment Purpose

Test a hybrid SPDConv-neck-P4 structure to balance gain and perturbation.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01h_yolov8n_hybrid_spdconv_neck_p4_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 31 |
| Precision | 0.64833 |
| Recall | 0.66538 |
| mAP50 | 0.69329 |
| mAP50-95 | 0.41573 |
| F1 | 0.65674 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.61372 | 0.70654 | 0.67371 | 0.38776 | 0.65687 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.64833 | 0.66538 | 0.69329 | 0.41573 | 0.65674 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.02855 |
| Recall | -0.06581 |
| mAP50 | -0.00444 |
| mAP50-95 | -0.00449 |
| F1 | -0.01415 |

## Analysis

This was a compromise between direct P4 SPDConv and the gated variant.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

It was close but below baseline, so later work moved away from this structure.
