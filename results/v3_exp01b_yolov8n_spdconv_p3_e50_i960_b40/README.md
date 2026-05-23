# YOLOv8n + SPDConv-P3 e50

## Experiment Purpose

Test SPDConv around the P3 small-object branch.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01b_yolov8n_spdconv_p3_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 32 |
| Precision | 0.64215 |
| Recall | 0.62196 |
| mAP50 | 0.65561 |
| mAP50-95 | 0.40418 |
| F1 | 0.63189 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.63090 | 0.70975 | 0.66795 | 0.38740 | 0.66801 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.64215 | 0.62196 | 0.65561 | 0.40418 | 0.63189 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.02237 |
| Recall | -0.10923 |
| mAP50 | -0.04212 |
| mAP50-95 | -0.01604 |
| F1 | -0.03900 |

## Analysis

This narrowed the SPDConv placement after the direct SPDConv result was unstable.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

Because it still did not beat baseline, the next step moved SPDConv to the Neck P3-to-P4 path.
