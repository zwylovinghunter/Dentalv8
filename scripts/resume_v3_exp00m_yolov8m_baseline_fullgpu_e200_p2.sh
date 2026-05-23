#!/usr/bin/env bash
set -euo pipefail
cd /root/yolov8

RUN_NAME="v3_exp00m_yolov8m_baseline_fullgpu_e200"
RESULT_DIR="results/${RUN_NAME}"
LOG_PATH="${RESULT_DIR}/resume_patience2.log"
PYTHON="/root/miniconda3/bin/python"
LAST_PT="${RESULT_DIR}/weights/last.pt"

if [ ! -f "${LAST_PT}" ]; then
  echo "Missing checkpoint: ${LAST_PT}" >&2
  exit 1
fi

screen -dmS "${RUN_NAME}" bash -lc "cd /root/yolov8 && ${PYTHON} - <<'PY' > '${LOG_PATH}' 2>&1
from ultralytics import YOLO

model = YOLO('results/v3_exp00m_yolov8m_baseline_fullgpu_e200/weights/last.pt')
model.train(
    resume=True,
    patience=2,
    batch=24,
    workers=16,
    cache='ram',
    plots=False,
    save_dir='results/v3_exp00m_yolov8m_baseline_fullgpu_e200',
)
PY"

echo "resumed ${RUN_NAME} with patience=2"
echo "screen: ${RUN_NAME}"
echo "log: ${LOG_PATH}"
echo "result: ${RESULT_DIR}"
