#!/usr/bin/env bash
set -euo pipefail
cd /root/autodl-tmp/yolov8
while screen -ls | grep -q 'v3_exp00_baseline'; do
  sleep 60
done
if [ -d /root/autodl-tmp/yolov8/v3_exp00_yolov8n_baseline_e50_i960_b40 ] && [ ! -e /root/autodl-tmp/yolov8/v3_exp01_yolov8n_spdconv_e50_i960_b40 ]; then
  bash scripts/run_v3_exp01_yolov8n_spdconv_e50.sh
else
  echo "baseline missing or exp01 already exists; not starting exp01"
fi
