#!/usr/bin/env bash
set -euo pipefail

PROJECT_FILES="${PROJECT_FILES:-/today_yolov8_work/repo_files}"
REPO_ROOT="${REPO_ROOT:-/root/autodl-tmp/yolov8}"
PYTHON_BIN="${PYTHON_BIN:-/root/miniconda3/bin/python}"

if [ ! -d "${REPO_ROOT}" ]; then
  echo "Training source directory does not exist: ${REPO_ROOT}"
  exit 1
fi

mkdir -p "${REPO_ROOT}/configs" "${REPO_ROOT}/data" "${REPO_ROOT}/logs"
cp "${PROJECT_FILES}/configs/yolov8n-dentex-v3-gated-spdconv-neck-p4.yaml" "${REPO_ROOT}/configs/yolov8n-dentex-v3-gated-spdconv-neck-p4.yaml"
cp "${PROJECT_FILES}/data/dentex_yolov8_3cls_v3.yaml" "${REPO_ROOT}/data/dentex_yolov8_3cls_v3.yaml"

cd "${REPO_ROOT}"
RUN_NAME="v3_exp01d_yolov8n_gated_spdconv_neck_p4_e50_i960_b40"
SCREEN_NAME="v3_exp01d_gated_spdconv_neck_p4"
RESULT_DIR="${REPO_ROOT}/${RUN_NAME}"
LOG_PATH="${REPO_ROOT}/logs/${RUN_NAME}.log"

if [ -e "${RESULT_DIR}" ]; then
  echo "Result directory already exists: ${RESULT_DIR}"
  exit 1
fi
if screen -list | grep -q "${SCREEN_NAME}"; then
  echo "Screen already exists: ${SCREEN_NAME}"
  exit 1
fi

screen -dmS "${SCREEN_NAME}" bash -lc "cd ${REPO_ROOT} && ${PYTHON_BIN} scripts/train_ablation.py --model configs/yolov8n-dentex-v3-gated-spdconv-neck-p4.yaml --weights yolov8n.pt --data data/dentex_yolov8_3cls_v3.yaml --epochs 50 --imgsz 960 --batch 40 --device 0 --workers 16 --project ${REPO_ROOT} --name ${RUN_NAME} --seed 42 --patience 0 --optimizer auto --cos-lr False --amp True --cache ram --close-mosaic 10 --plots False > ${LOG_PATH} 2>&1"
echo "started ${SCREEN_NAME}"
echo "log: ${LOG_PATH}"
echo "tail -f ${LOG_PATH}"
