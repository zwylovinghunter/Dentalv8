# YOLOv8n + SPDConv-neck-P4 mosaic0.5 e50

## Experiment Purpose

Lower mosaic strength on the P4 SPDConv experiment.

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/v3_exp01g_yolov8n_spdconv_neck_p4_mosaic05_e50_i960_b40` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | 50 |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | 43 |
| Precision | 0.61573 |
| Recall | 0.68427 |
| mAP50 | 0.68177 |
| mAP50-95 | 0.40780 |
| F1 | 0.64819 |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.61766 | 0.69082 | 0.69010 | 0.40449 | 0.65219 |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | 0.61978 | 0.73119 | 0.69773 | 0.42022 | 0.67089 |
| This experiment | 0.61573 | 0.68427 | 0.68177 | 0.40780 | 0.64819 |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | -0.00405 |
| Recall | -0.04692 |
| mAP50 | -0.01596 |
| mAP50-95 | -0.01242 |
| F1 | -0.02270 |

## Analysis

This tested whether heavy mosaic augmentation hurt dental localization.

This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result.

## Closed-Loop Next Step

The result did not beat baseline, so this augmentation setting was not continued.
