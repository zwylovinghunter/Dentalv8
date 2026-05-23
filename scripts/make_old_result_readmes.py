import csv, math
from pathlib import Path

experiments = [
    ("v3_exp00_yolov8n_baseline_e50_i960_b40", "YOLOv8n baseline e50", "Build the early YOLOv8n e50 reference without structural or loss changes.", "This is the starting point for the early structural ablation chain.", "Next, SPDConv was tested as the first structural enhancement."),
    ("v3_exp01_yolov8n_spdconv_e50_i960_b40", "YOLOv8n + SPDConv e50", "Test a direct SPDConv structure change for finer downsampling information.", "This was the first SPDConv trial after the e50 baseline.", "Because it did not beat baseline, later experiments narrowed the insertion position."),
    ("v3_exp01b_yolov8n_spdconv_p3_e50_i960_b40", "YOLOv8n + SPDConv-P3 e50", "Test SPDConv around the P3 small-object branch.", "This narrowed the SPDConv placement after the direct SPDConv result was unstable.", "Because it still did not beat baseline, the next step moved SPDConv to the Neck P3-to-P4 path."),
    ("v3_exp01c_yolov8n_spdconv_neck_p4_e50_i960_b40", "YOLOv8n + SPDConv-neck-P4 e50", "Test SPDConv at the Neck P3-to-P4 downsampling position.", "This became the strongest early e50 structural result and suggested the P4 neck position was valuable.", "This result motivated the later e200 SPDConv-neck-P4 experiment."),
    ("v3_exp01d_yolov8n_gated_spdconv_neck_p4_e50_i960_b40", "YOLOv8n + gated SPDConv-neck-P4 e50", "Test a gated SPDConv branch that keeps the original Conv path and adds weak SPDConv information.", "This was designed to reduce disruption from direct SPDConv insertion.", "It did not beat baseline or the plain P4 variant, so it was not kept as the main branch."),
    ("v3_exp01e_yolov8n_spdconv_neck_p5_e50_i960_b40", "YOLOv8n + SPDConv-neck-P5 e50", "Test whether placing SPDConv on the higher-level P5 path helps large-object localization.", "This is the P5 placement control for the P4 SPDConv direction.", "It underperformed the P4 setting, so P5 placement was not continued."),
    ("v3_exp01f_yolov8n_spdconv_neck_p4_e80_cos_i960_b40", "YOLOv8n + SPDConv-neck-P4 e80 cos_lr", "Extend the P4 SPDConv experiment to 80 epochs with cosine LR.", "This tested whether training schedule changes could stabilize the P4 gain.", "The result did not improve the best P4 e50 result, so this schedule was not retained."),
    ("v3_exp01g_yolov8n_spdconv_neck_p4_mosaic05_e50_i960_b40", "YOLOv8n + SPDConv-neck-P4 mosaic0.5 e50", "Lower mosaic strength on the P4 SPDConv experiment.", "This tested whether heavy mosaic augmentation hurt dental localization.", "The result did not beat baseline, so this augmentation setting was not continued."),
    ("v3_exp01h_yolov8n_hybrid_spdconv_neck_p4_e50_i960_b40", "YOLOv8n + hybrid SPDConv-neck-P4 e50", "Test a hybrid SPDConv-neck-P4 structure to balance gain and perturbation.", "This was a compromise between direct P4 SPDConv and the gated variant.", "It was close but below baseline, so later work moved away from this structure."),
    ("v3_exp02a_yolov8n_head_channel_attn_e50_i960_b40", "YOLOv8n + Head Channel Attention e50", "Test Head Channel Attention as an alternative to SPDConv.", "This switched from spatial downsampling changes to head channel weighting.", "It was close to baseline but not better, which helped motivate the later loss-optimization direction."),
]

def read_metrics(name):
    p = Path("results") / name / "results.csv"
    rows = []
    for row in csv.DictReader(p.open()):
        row = {k.strip(): v for k, v in row.items()}
        try:
            vals = {
                "epoch": int(float(row["epoch"])),
                "P": float(row["metrics/precision(B)"]),
                "R": float(row["metrics/recall(B)"]),
                "mAP50": float(row["metrics/mAP50(B)"]),
                "mAP50_95": float(row["metrics/mAP50-95(B)"]),
            }
        except Exception:
            continue
        if all(math.isfinite(vals[k]) for k in ["P", "R", "mAP50", "mAP50_95"]):
            vals["F1"] = 2 * vals["P"] * vals["R"] / (vals["P"] + vals["R"]) if vals["P"] + vals["R"] else 0.0
            rows.append(vals)
    return max(rows, key=lambda x: x["mAP50_95"]), rows[-1], len(rows)

baseline_best, _, _ = read_metrics("v3_exp00_yolov8n_baseline_e50_i960_b40")

for name, title, purpose, relation, next_step in experiments:
    best, last, epochs = read_metrics(name)
    delta = {k: best[k] - baseline_best[k] for k in ["P", "R", "mAP50", "mAP50_95", "F1"]}
    is_base = name == "v3_exp00_yolov8n_baseline_e50_i960_b40"
    conclusion = "This is the early YOLOv8n e50 reference for later structural ablations." if is_base else (
        "This run beats the e50 baseline on mAP50-95, so it had follow-up value." if best["mAP50_95"] > baseline_best["mAP50_95"] else
        "This run does not beat the e50 baseline on mAP50-95, so it was not suitable as the main result."
    )
    md = f"""# {title}

## Experiment Purpose

{purpose}

## Configuration

| Item | Value |
|---|---|
| Result folder | `results/{name}` |
| Dataset | `data/dentex_yolov8_3cls_v3.yaml` |
| Image size | 960 |
| Recorded epochs | {epochs} |
| Log file | `train.log` |
| Selection rule | best mAP50-95 row in `results.csv` |

## Best Result

| Metric | Value |
|---|---:|
| Best epoch | {best['epoch']} |
| Precision | {best['P']:.5f} |
| Recall | {best['R']:.5f} |
| mAP50 | {best['mAP50']:.5f} |
| mAP50-95 | {best['mAP50_95']:.5f} |
| F1 | {best['F1']:.5f} |

## Last Recorded Epoch

| Epoch | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---:|---:|---:|---:|---:|---:|
| {last['epoch']} | {last['P']:.5f} | {last['R']:.5f} | {last['mAP50']:.5f} | {last['mAP50_95']:.5f} | {last['F1']:.5f} |

## Comparison With YOLOv8n e50 Baseline

| Scheme | Precision | Recall | mAP50 | mAP50-95 | F1 |
|---|---:|---:|---:|---:|---:|
| YOLOv8n e50 baseline | {baseline_best['P']:.5f} | {baseline_best['R']:.5f} | {baseline_best['mAP50']:.5f} | {baseline_best['mAP50_95']:.5f} | {baseline_best['F1']:.5f} |
| This experiment | {best['P']:.5f} | {best['R']:.5f} | {best['mAP50']:.5f} | {best['mAP50_95']:.5f} | {best['F1']:.5f} |

## Delta To Baseline

| Metric | Delta |
|---|---:|
| Precision | {delta['P']:+.5f} |
| Recall | {delta['R']:+.5f} |
| mAP50 | {delta['mAP50']:+.5f} |
| mAP50-95 | {delta['mAP50_95']:+.5f} |
| F1 | {delta['F1']:+.5f} |

## Analysis

{relation}

{conclusion}

## Closed-Loop Next Step

{next_step}
"""
    (Path("results") / name / "README.md").write_text(md, encoding="utf-8")

print("wrote", len(experiments), "README files")
