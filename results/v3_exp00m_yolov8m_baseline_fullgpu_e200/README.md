# YOLOv8m Baseline Full-GPU e200

## Experiment Purpose

This experiment establishes the YOLOv8m baseline on the Dentex YOLOv8 3-class v3 dataset. It keeps the network as the standard YOLOv8m P3/P4/P5 detector and does not add PIoU, SPDConv, CoordAtt, DyHead, P2, NWD, Focal, or other optimization modules.

The purpose is to provide a stronger-model baseline after the YOLOv8n experiments. This result is used as the direct reference for the following YOLOv8m + Powerful-IoU box loss experiment.

## Configuration

| Item | Value |
|---|---|
| Model | YOLOv8m baseline |
| Config | `configs/yolov8m-dental-none-standard.yaml` |
| Pretrained weight | `yolov8m.pt` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Epochs | 200 planned |
| Image size | 960 |
| Batch | 24 |
| Box loss | CIoU, original YOLOv8 default |
| Project | `results` |
| Result name | `v3_exp00m_yolov8m_baseline_fullgpu_e200` |

## Training Notes

The first run was started with `patience=0` to run the full 200-epoch schedule. After observing that the best result had appeared much earlier and later epochs did not improve, training was resumed with early-stop settings and then manually stopped at epoch 133.

Important notes:

- The result should be interpreted by the saved best checkpoint and the best valid row in `results.csv`, not the final `last.pt`.
- `results.csv` contains resume/interruption artifacts around epochs 123 and 124, where invalid `0/nan` rows appeared after stopping and resuming. These rows are not used for best-result analysis.
- Logs are stored in this folder:
  - `train_initial_patience0.log`
  - `resume_patience30.log`
  - `resume_patience2.log`

## Best Result From results.csv

The project fitness rule uses mAP50-95 as the best criterion. The best valid row is epoch 23.

| Metric | Value |
|---|---:|
| Best epoch | 23 |
| Precision | 0.63287 |
| Recall | 0.69198 |
| mAP50 | 0.67715 |
| mAP50-95 | 0.42257 |
| F1 | 0.66111 |

The last recorded epoch was 133, but its mAP50-95 was lower than the best epoch:

| Epoch | Precision | Recall | mAP50 | mAP50-95 |
|---:|---:|---:|---:|---:|
| 133 | 0.55615 | 0.63577 | 0.61139 | 0.36008 |

## Comparison Role

This experiment is the YOLOv8m baseline for the next result:

`v3_exp01m_yolov8m_piou_fullgpu_e200_p30`

The motivation for the next experiment is that previous YOLOv8n PIoU tests showed PIoU can improve localization-related metrics, especially mAP50 and sometimes mAP50-95, but may trade off recall or class balance. Therefore, the next step tests whether Powerful-IoU provides a measurable gain on the stronger YOLOv8m backbone.

## Conclusion

This baseline reached mAP50-95 `0.42257` at epoch 23. It is the reference point for judging whether YOLOv8m + PIoU improves localization quality. Because the later epochs did not improve the best value, subsequent comparison should use the epoch-23 best result, not the final interrupted epoch.
