# Scheme 1C Revision After v3 exp01b

Evidence so far:

| Scheme | Best mAP50-95 | Best mAP50 | Best Recall | Notes |
|---|---:|---:|---:|---|
| baseline | 0.420220 | 0.697730 | 0.747080 | no SPDConv |
| SPDConv P1/P2 | 0.396050 | 0.679840 | 0.729680 | too invasive in shallow stem |
| SPDConv P3 backbone | 0.404180 | 0.694290 | 0.743370 | closer, but still below baseline |

Revision 1C: `yolov8n-dentex-v3-spdconv-neck-p4.yaml`

- Keep the whole backbone identical to baseline.
- Keep P3 small-object feature output unchanged.
- Replace only the neck/head P3->P4 downsampling Conv with SPDConv.
- This tests whether SPDConv helps after feature fusion without disrupting pretrained backbone extraction.

Training command:

```bash
bash scripts/run_v3_exp01c_yolov8n_spdconv_neck_p4_e50.sh
```
