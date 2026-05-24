# YOLOv8n baseline e50

## Experiment Purpose

Build the early YOLOv8n e50 reference without structural or loss changes.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp00_yolov8n_baseline_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 31 |
| Precision | 0.61978 |
| Recall | 0.73119 |
| mAP50 | 0.69773 |
| mAP50-95 | 0.42022 |
| F1 | 0.67089 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.63340 | 0.67913 | 0.69225 | 0.40750 | 0.65547 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.00000 |
| Recall | +0.00000 |
| mAP50 | +0.00000 |
| mAP50-95 | +0.00000 |
| F1 | +0.00000 |

## Analysis

This is the starting point for the early structural ablation chain.

This is the early YOLOv8n e50 reference for later structural ablations.

## Closed-Loop Next Step

Next, SPDConv was tested as the first structural enhancement.
