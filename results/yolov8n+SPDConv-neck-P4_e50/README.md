# YOLOv8n + SPDConv-neck-P4 e50

## Experiment Purpose

Test SPDConv at the Neck P3-to-P4 downsampling position.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01c_yolov8n_spdconv_neck_p4_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 31 |
| Precision | 0.56867 |
| Recall | 0.70052 |
| mAP50 | 0.71195 |
| mAP50-95 | 0.42731 |
| F1 | 0.62775 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.60213 | 0.66958 | 0.65596 | 0.38549 | 0.63407 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.56867 | 0.70052 | 0.71195 | 0.42731 | 0.62775 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | -0.05111 |
| Recall | -0.03067 |
| mAP50 | +0.01422 |
| mAP50-95 | +0.00709 |
| F1 | -0.04314 |

## Analysis

This became the strongest early e50 structural result and suggested the P4 neck position was valuable.

This run beats the e50 baseline on mAP50-95, so it had follow-up value.

## Closed-Loop Next Step

This result motivated the later e200 SPDConv-neck-P4 experiment.
