# YOLOv8n + SPDConv e50

## Experiment Purpose

Test a direct SPDConv structure change for finer downsampling information.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01_yolov8n_spdconv_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 39 |
| Precision | 0.57768 |
| Recall | 0.71941 |
| mAP50 | 0.67984 |
| mAP50-95 | 0.39605 |
| F1 | 0.64080 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.60682 | 0.65345 | 0.65221 | 0.36891 | 0.62927 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.57768 | 0.71941 | 0.67984 | 0.39605 | 0.64080 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | -0.04210 |
| Recall | -0.01178 |
| mAP50 | -0.01789 |
| mAP50-95 | -0.02417 |
| F1 | -0.03009 |

## Analysis

This was the first SPDConv trial after the e50 baseline.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

Because it did not beat baseline, later experiments narrowed the insertion position.
