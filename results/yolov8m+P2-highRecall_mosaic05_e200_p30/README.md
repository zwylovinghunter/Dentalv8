# YOLOv8m + P2 High-Recall Head e200 p30

## Experiment Purpose

This experiment tests a YOLOv8m high-recall variant for dental lesion detection on the Dentex YOLOv8 3-class v3 dataset.

The main change is adding a P2/4 small-object detection head. The original YOLOv8m baseline detects on P3/P4/P5. This experiment changes the detector to P2/P3/P4/P5 so that small and low-contrast lesion candidates can be represented at a finer feature scale.

The goal is not only to raise recall, but also to keep the other main metrics from dropping. This run is therefore judged against the YOLOv8m baseline with the requirement that Precision, mAP50, and mAP50-95 should stay stable or improve.

## Configuration

| Item | Value |
|---|---|
| Model | YOLOv8m + P2 high-recall head |
| Config | `configs/yolov8m-dentex-v3-p2-highrecall.yaml` |
| Pretrained weight | `yolov8m.pt` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Epochs | 200 planned |
| Early stopping | `patience=30` |
| Actual stop | epoch 56, early stopped |
| Image size | 960 |
| Batch | AutoBatch, recorded as `batch=0.9` |
| Detection heads | P2/P3/P4/P5 |
| Box loss | CIoU, original YOLOv8 default |
| Mosaic | `mosaic=0.5` |
| Cosine LR | `cos_lr=True` |
| Project | `results` |
| Result name | `yolov8m+P2-highRecall_mosaic05_e200_p30` |

## Training Notes

The model keeps the YOLOv8m backbone close to the baseline and adds an extra P2 branch in the head. This makes the model more sensitive to small lesion candidates, which is useful for a high-recall screening-oriented detector.

Training used the same dataset and image size as the YOLOv8m baseline. Mosaic augmentation was reduced to `0.5` to keep augmentation useful without overly disturbing panoramic dental structures. Early stopping was enabled:

```text
patience=30
```

The run stopped early at epoch 56. The best result was observed at epoch 26, and `best.pt` was saved in `weights/best.pt`.

Log file:

`train.log`

## Best Result From results.csv

| Metric | Value |
|---|---:|
| Best epoch | 26 |
| Precision | 0.63668 |
| Recall | 0.69893 |
| mAP50 | 0.68744 |
| mAP50-95 | 0.42339 |
| F1 | 0.66635 |

Final early-stop epoch:

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| 56 | 0.59634 | 0.62755 | 0.64812 | 0.36804 | 0.61155 |

The final epoch is not used as the result because the best checkpoint is selected by mAP50-95.

## Final Validation Snapshot

The final validation of `weights/best.pt` reported the following class-level metrics in `train.log`:

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| all | 0.638 | 0.699 | 0.688 | 0.424 |
| Caries | 0.488 | 0.610 | 0.553 | 0.381 |
| Periapical_Lesion | 0.690 | 0.563 | 0.640 | 0.276 |
| Impacted | 0.736 | 0.925 | 0.871 | 0.616 |

## Comparison With YOLOv8m Baseline

| Scheme | Best epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|---:|
| YOLOv8m baseline | 23 | 0.63287 | 0.69198 | 0.67715 | 0.42257 | 0.66111 |
| YOLOv8m + P2 high-recall | 26 | 0.63668 | 0.69893 | 0.68744 | 0.42339 | 0.66635 |

## Delta: P2 High-Recall - Baseline

| Metric | Delta |
|---|---:|
| Precision | +0.00381 |
| Recall | +0.00695 |
| mAP50 | +0.01029 |
| mAP50-95 | +0.00082 |
| F1 | +0.00524 |

## Analysis

The P2 high-recall variant gives the best closed-loop improvement among the YOLOv8m high-recall attempts because it raises recall without sacrificing the other headline metrics:

- Recall improved from `0.69198` to `0.69893`.
- Precision improved from `0.63287` to `0.63668`.
- mAP50 improved from `0.67715` to `0.68744`.
- mAP50-95 improved slightly from `0.42257` to `0.42339`.
- F1 improved from `0.66111` to `0.66635`.

The improvement is small, but it is balanced. This is important because previous YOLOv8m optimization results could improve localization while reducing recall. This run is more suitable for a dental lesion screening scenario because recall improves and the localization metrics do not regress.

Class-level validation shows that `Impacted` has the strongest recall and mAP50-95. `Caries` and `Periapical_Lesion` remain harder categories, especially for high-quality localization, but the all-class result is still better than the YOLOv8m baseline.

## Closed-Loop Relation To Previous Results

The YOLOv8m baseline established the reference at mAP50-95 `0.42257` and recall `0.69198`. The YOLOv8m + PIoU experiment improved precision and localization metrics, but recall dropped. The YOLOv8m + SPDConv-neck-P4 experiment improved mAP metrics, but it also did not provide a clear high-recall gain over the baseline.

This P2 high-recall experiment closes that gap:

1. It directly targets small-object sensitivity by adding a P2/4 detection head.
2. It improves recall over the YOLOv8m baseline.
3. It does not trade off Precision, mAP50, mAP50-95, or F1.
4. It is therefore the most suitable YOLOv8m result for a high-recall dental lesion detection role.

## Conclusion

YOLOv8m + P2 high-recall is a valid high-recall model candidate for this project. Compared with the YOLOv8m baseline, it improves Recall, Precision, mAP50, mAP50-95, and F1 at the selected best checkpoint. The gains are modest, but the result is balanced and suitable for use as the high-recall dental lesion detection model in the Gradio demonstration platform.
