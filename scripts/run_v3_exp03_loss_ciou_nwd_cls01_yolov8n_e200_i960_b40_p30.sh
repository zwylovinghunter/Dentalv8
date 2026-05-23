#!/usr/bin/env bash
set -euo pipefail

cd /root/yolov8

EXP_NAME="v3_exp03_loss_ciou_nwd_cls01_yolov8n_e200_i960_b40_p30"
PROJECT="/root/results"
RESULT_DIR="${PROJECT}/${EXP_NAME}"
TMP_LOG="/tmp/${EXP_NAME}.log"
BASE_ARGS="/root/results/v3_exp00b_yolov8n_baseline_e200_i960_b40/args.yaml"
OLD_RUN_LINK="/root/autodl-tmp/work/yolo8/runs/detect/${EXP_NAME}"

if [ -e "${RESULT_DIR}" ] || [ -e "${OLD_RUN_LINK}" ]; then
  echo "Result directory already exists, refusing to overwrite: ${RESULT_DIR} or ${OLD_RUN_LINK}" >&2
  exit 1
fi
rm -f "${TMP_LOG}"

screen -dmS v3_exp03_loss_ciou_nwd_cls01 bash -lc "cd /root/yolov8 && /root/miniconda3/bin/python - <<'PYTRAIN' > '${TMP_LOG}' 2>&1
import sys
from pathlib import Path
import yaml

sys.path.insert(0, '/root/yolov8')
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
    'data', 'imgsz', 'batch', 'device', 'seed', 'optimizer', 'lr0', 'lrf', 'momentum',
    'weight_decay', 'warmup_epochs', 'box', 'cls', 'dfl', 'mosaic', 'mixup', 'copy_paste',
    'close_mosaic', 'cos_lr', 'rect', 'deterministic', 'single_cls', 'fraction', 'val'
]
train_args = {k: base[k] for k in keys if k in base}
train_args['data'] = '/root/yolov8/data/dentex_yolov8_3cls_v3.yaml'
train_args.update({
    'epochs': 200,
    'patience': 30,
    'workers': 8,
    'amp': True,
    'cache': False,
    'project': project,
    'name': name,
    'plots': False,
    'exist_ok': False,
    'box_loss': 'ciou_nwd_cls01',
    'pretrained': '/root/yolov8/yolov8n.pt',
})
model = YOLO('/root/yolov8/configs/yolov8n-dentex-v3-baseline.yaml')
model.load('/root/yolov8/yolov8n.pt')
model.train(**train_args)
PYTRAIN
status=\$?
if [ -d '${RESULT_DIR}' ]; then
  mkdir -p '${RESULT_DIR}/logs'
  mv '${TMP_LOG}' '${RESULT_DIR}/logs/${EXP_NAME}.log'
  [ -e '${OLD_RUN_LINK}' ] || ln -s '${RESULT_DIR}' '${OLD_RUN_LINK}'
else
  mkdir -p /root/results/_failed_logs
  mv '${TMP_LOG}' '/root/results/_failed_logs/${EXP_NAME}.log'
fi
exit \$status"

echo "started screen=v3_exp03_loss_ciou_nwd_cls01 temp_log=${TMP_LOG} result=${RESULT_DIR}"
