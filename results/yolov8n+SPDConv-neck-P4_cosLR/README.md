# YOLOv8n + SPDConv-neck-P4 e80 cos_lr

## Experiment Purpose

Extend the P4 SPDConv experiment to 80 epochs with cosine LR.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01f_yolov8n_spdconv_neck_p4_e80_cos_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 80 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 44 |
| Precision | 0.64266 |
| Recall | 0.70941 |
| mAP50 | 0.67811 |
| mAP50-95 | 0.40257 |
| F1 | 0.67439 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 80 | 0.58032 | 0.73065 | 0.64316 | 0.36345 | 0.64687 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.64266 | 0.70941 | 0.67811 | 0.40257 | 0.67439 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.02288 |
| Recall | -0.02178 |
| mAP50 | -0.01962 |
| mAP50-95 | -0.01765 |
| F1 | +0.00350 |

## Analysis

This tested whether training schedule changes could stabilize the P4 gain.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

The result did not improve the best P4 e50 result, so this schedule was not retained.
