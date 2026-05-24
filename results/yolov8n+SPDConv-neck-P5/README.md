# YOLOv8n + SPDConv-neck-P5 e50

## Experiment Purpose

Test whether placing SPDConv on the higher-level P5 path helps large-object localization.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01e_yolov8n_spdconv_neck_p5_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 44 |
| Precision | 0.62976 |
| Recall | 0.68492 |
| mAP50 | 0.68025 |
| mAP50-95 | 0.40119 |
| F1 | 0.65618 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.62212 | 0.68160 | 0.66911 | 0.38328 | 0.65050 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.62976 | 0.68492 | 0.68025 | 0.40119 | 0.65618 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.00998 |
| Recall | -0.04627 |
| mAP50 | -0.01748 |
| mAP50-95 | -0.01903 |
| F1 | -0.01471 |

## Analysis

This is the P5 placement control for the P4 SPDConv direction.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

It underperformed the P4 setting, so P5 placement was not continued.
