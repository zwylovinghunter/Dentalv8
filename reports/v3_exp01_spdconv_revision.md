# Scheme 1 Revision After v3 exp01

Previous scheme 1: `yolov8n-dentex-v3-spdconv.yaml`
- SPDConv replaced the first two downsampling layers: P1/2 and P2/4.
- Result against baseline after 50 epochs: precision, recall, mAP50, and mAP50-95 all decreased.

Revision: `yolov8n-dentex-v3-spdconv-p3.yaml`
- Keep YOLOv8n stem layers P1/2 and P2/4 as standard Conv to preserve pretrained low-level feature extraction.
- Use SPDConv only at P3/8 downsampling, after early features are more stable.
- Keep P4/P5 and Detect path unchanged for a controlled single-module comparison.

Training command:

```bash
bash scripts/run_v3_exp01b_yolov8n_spdconv_p3_e50.sh
```
