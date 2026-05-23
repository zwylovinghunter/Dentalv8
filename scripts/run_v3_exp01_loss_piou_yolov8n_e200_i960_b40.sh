#!/usr/bin/env bash
set -euo pipefail

cd /root/autodl-tmp/yolov8
mkdir -p logs

EXP_NAME="v3_exp01_loss_piou_yolov8n_e200_i960_b40"
PROJECT="/root/autodl-tmp/work/yolo8/runs/detect"
RESULT_DIR="${PROJECT}/${EXP_NAME}"
LOG="logs/${EXP_NAME}.log"
BASE_ARGS="/root/autodl-tmp/work/yolo8/runs/detect/v3_exp00b_yolov8n_baseline_e200_i960_b40/args.yaml"

if [ -d "${RESULT_DIR}" ]; then
  echo "Result directory already exists, refusing to overwrite: ${RESULT_DIR}" >&2
  exit 1
fi

screen -dmS v3_exp01_loss_piou bash -lc "cd /root/autodl-tmp/yolov8 && /root/miniconda3/bin/python - <<'PY' > '${LOG}' 2>&1
import sys
from pathlib import Path
import yaml

sys.path.insert(0, '/root/autodl-tmp/yolov8')
from ultralytics import YOLO

base_path = Path('${BASE_ARGS}')
with base_path.open() as f:
    base = yaml.safe_load(f)

name = '${EXP_NAME}'
project = '${PROJECT}'
result_dir = Path(project) / name
if result_dir.exists():
    raise SystemExit(f'Result directory already exists, refusing to overwrite: {result_dir}')

keys = [
    'data', 'epochs', 'imgsz', 'batch', 'device', 'workers', 'seed', 'patience', 'optimizer',
    'lr0', 'lrf', 'momentum', 'weight_decay', 'warmup_epochs', 'box', 'cls', 'dfl', 'mosaic',
    'mixup', 'copy_paste', 'close_mosaic', 'cos_lr', 'amp', 'cache', 'rect', 'deterministic',
    'single_cls', 'fraction', 'val'
]
train_args = {k: base[k] for k in keys if k in base}
train_args.update({
    'project': project,
    'name': name,
    'plots': False,
    'exist_ok': False,
    'box_loss': 'piou',
    'pretrained': base.get('pretrained'),
})
model = YOLO(base['model'])
pretrained = base.get('pretrained')
if pretrained:
    model.load(pretrained)
model.train(**train_args)
PY"

echo "started screen=v3_exp01_loss_piou log=${LOG} result=${RESULT_DIR}"
