#!/usr/bin/env bash
set -euo pipefail
cd /root/yolov8

RUN_NAME="v3_exp01m_yolov8m_piou_fullgpu_e200_p30"
PROJECT="results"
RESULT_DIR="${PROJECT}/${RUN_NAME}"
LOG_TMP="${PROJECT}/${RUN_NAME}.log"
PYTHON="/root/miniconda3/bin/python"

if [ -e "${RESULT_DIR}" ]; then
  echo "Result directory already exists, refusing to overwrite: ${RESULT_DIR}" >&2
  exit 1
fi

mkdir -p "${PROJECT}"
rm -f "${LOG_TMP}"

screen -dmS "${RUN_NAME}" bash -lc "cd /root/yolov8 && set -o pipefail && ${PYTHON} - <<'PY' > '${LOG_TMP}' 2>&1
from ultralytics import YOLO

model = YOLO('configs/yolov8m-dental-none-standard.yaml')
model.load('yolov8m.pt')
model.train(
    data='data/dentex_yolov8_3cls_v3.yaml',
    epochs=200,
    imgsz=960,
    batch=24,
    device='0',
    workers=16,
    project='results',
    name='v3_exp01m_yolov8m_piou_fullgpu_e200_p30',
    save_dir='results/v3_exp01m_yolov8m_piou_fullgpu_e200_p30',
    seed=42,
    patience=30,
    optimizer='auto',
    cos_lr=False,
    amp=True,
    cache='ram',
    close_mosaic=10,
    plots=False,
    exist_ok=False,
    box_loss='piou',
)
PY
status=\$?
if [ -d '${RESULT_DIR}' ] && [ -f '${LOG_TMP}' ]; then mv '${LOG_TMP}' '${RESULT_DIR}/train.log'; fi
exit \$status"

echo "started ${RUN_NAME}"
echo "screen: ${RUN_NAME}"
echo "log: ${LOG_TMP} until training finishes, then ${RESULT_DIR}/train.log"
echo "result: ${RESULT_DIR}"
