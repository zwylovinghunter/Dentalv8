# YOLOv8n + Head Channel Attention e50

## Experiment Purpose

Test Head Channel Attention as an alternative to SPDConv.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp02a_yolov8n_head_channel_attn_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 31 |
| Precision | 0.62164 |
| Recall | 0.67699 |
| mAP50 | 0.67907 |
| mAP50-95 | 0.41924 |
| F1 | 0.64814 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.68202 | 0.60957 | 0.67219 | 0.39078 | 0.64376 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.62164 | 0.67699 | 0.67907 | 0.41924 | 0.64814 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.00186 |
| Recall | -0.05420 |
| mAP50 | -0.01866 |
| mAP50-95 | -0.00098 |
| F1 | -0.02276 |

## Analysis

This switched from spatial downsampling changes to head channel weighting.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

It was close to baseline but not better, which helped motivate the later loss-optimization direction.
