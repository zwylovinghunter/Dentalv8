# Scheme 1E: SPDConv Neck P5

Test direction 4: keep baseline backbone, P3 output, and P3->P4 neck path unchanged. Replace only neck/head P4->P5 downsampling Conv with SPDConv.

Training command:

```bash
bash scripts/run_v3_exp01e_yolov8n_spdconv_neck_p5_e50.sh
```
