# YOLOv8m + Powerful-IoU Box Loss e200 p30

## Experiment Purpose

This experiment tests Powerful-IoU / PIoU box regression loss on YOLOv8m while keeping the network structure unchanged.

The goal is to check whether replacing the original YOLOv8 CIoU box loss with PIoU improves localization quality on the Dentex YOLOv8 3-class v3 dataset, especially mAP50-95, when using the stronger YOLOv8m model.

This experiment follows the YOLOv8m baseline:

`v3_exp00m_yolov8m_baseline_fullgpu_e200`

## Configuration

| Item | Value |
|---|---|
| Model | YOLOv8m baseline structure |
| Config | `configs/yolov8m-dental-none-standard.yaml` |
| Pretrained weight | `yolov8m.pt` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Epochs | 200 planned |
| Early stopping | `patience=30` |
| Actual stop | epoch 68, early stopped |
| Image size | 960 |
| Batch | 24 |
| Box loss | `box_loss=piou` |
| Project | `results` |
| Result name | `v3_exp01m_yolov8m_piou_fullgpu_e200_p30` |

## Training Notes

Training used the same YOLOv8m architecture as the baseline. Only the bbox regression loss was changed from original CIoU to PIoU. Classification loss and DFL loss remained unchanged.

Early stopping was explicitly enabled:

```text
patience=30
```

The run stopped early at epoch 68. The best result was observed at epoch 38, and `best.pt` was saved in `weights/best.pt`.

Log file:

`train.log`

## Best Result From results.csv

| Metric | Value |
|---|---:|
| Best epoch | 38 |
| Precision | 0.66846 |
| Recall | 0.66527 |
| mAP50 | 0.69270 |
| mAP50-95 | 0.42560 |
| F1 | 0.66686 |

Final early-stop epoch:

| Epoch | Precision | Recall | mAP50 | mAP50-95 |
|---:|---:|---:|---:|---:|
| 68 | 0.56380 | 0.66071 | 0.57324 | 0.32686 |

The final epoch is not used as the result because the best checkpoint is selected by mAP50-95.

## Comparison With YOLOv8m Baseline

| Scheme | Best epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|---:|
| YOLOv8m baseline | 23 | 0.63287 | 0.69198 | 0.67715 | 0.42257 | 0.66111 |
| YOLOv8m + PIoU | 38 | 0.66846 | 0.66527 | 0.69270 | 0.42560 | 0.66686 |

## Delta: PIoU - Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.03559 |
| Recall | -0.02671 |
| mAP50 | +0.01555 |
| mAP50-95 | +0.00303 |
| F1 | +0.00575 |

## Analysis

PIoU produced a small but positive improvement over the YOLOv8m baseline in the main localization metric:

- mAP50-95 improved from `0.42257` to `0.42560`.
- mAP50 improved from `0.67715` to `0.69270`.
- Precision improved from `0.63287` to `0.66846`.
- F1 improved slightly from `0.66111` to `0.66686`.
- Recall decreased from `0.69198` to `0.66527`.

This means PIoU improves localization confidence and precision, but it trades off some recall. The mAP50-95 gain is real but small, so this is not a strong standalone improvement.

## Closed-Loop Relation To Previous Results

The earlier YOLOv8n PIoU experiment showed that PIoU could improve some localization and precision metrics, but the gain was not stable across classes. The YOLOv8m PIoU experiment was therefore used to test whether the same loss change becomes more useful when the backbone capacity is increased.

The result closes this step as follows:

1. YOLOv8m baseline established a stronger reference at mAP50-95 `0.42257`.
2. YOLOv8m + PIoU improved mAP50-95 to `0.42560` and mAP50 to `0.69270`.
3. The improvement is positive but small, while recall dropped.
4. PIoU can be reported as a mild localization improvement, but it should not be treated as a decisive main optimization by itself.

## Conclusion

YOLOv8m + PIoU has a measurable but limited improvement over the YOLOv8m baseline. It is suitable as a supporting loss-ablation result showing that Powerful-IoU slightly improves localization quality, but the small mAP50-95 gain and recall drop mean further optimization should focus on balancing recall and localization rather than simply continuing to strengthen PIoU alone.
