<div align="center">

# DentalV8 show

面向毕业答辩和受控内网的牙齿病变辅助识别部署版

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12"></a>
  <a href="https://www.gradio.app/"><img src="https://img.shields.io/badge/Gradio-6.14-F97316" alt="Gradio 6.14"></a>
  <a href="https://github.com/ultralytics/ultralytics"><img src="https://img.shields.io/badge/YOLOv8-CPU%20队列-111827" alt="YOLOv8 CPU"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue" alt="AGPL-3.0"></a>
</p>

</div>

> [!WARNING]
> 仅用于科研展示、课程验收和答辩演示，不作为临床诊断依据。请使用脱敏影像，并由专业口腔医生复核疑似区域。

这是从 <code>main</code> 裁剪出的最小可部署版本：保留八个工作区、三个展示权重、报告导出、会话级软隔离、健康检查和多人检测排队提示；不包含训练数据、实验文档和旧报告。

## 快速部署

~~~bash
git clone -b show https://github.com/zwylovinghunter/Dentalv8.git /srv/Dentalv8
cd /srv/Dentalv8
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements-show.txt
cp .env.example .env
# 编辑 .env 后启动
python app.py
~~~

默认地址为 <code>http://127.0.0.1:7860</code>，健康检查：

~~~bash
curl http://127.0.0.1:7860/healthz
~~~

返回 <code>{"ok": true}</code> 即表示进程可用。正式服务器请使用仓库内的 <code>deploy/dentalv8.service</code> 和 <code>deploy/nginx.conf.example</code>，通过 HTTPS 反向代理访问。

## 功能

| 模块 | 能力 |
| --- | --- |
| 图像检测 | 单图 YOLO 推理、中文类别、按类别配色、重叠框抑制、联动放大 |
| 多模型对比 | 基线/高精度/高召回三个模型的一致性与分歧分析 |
| 批量检测 | 逐张队列、进度、失败重试、CSV/Markdown 报告 |
| 智诊管家 | Gemini、阿里云百炼、Ollama 和本地规则回退；问答位置导航 |
| 报告中心 | Markdown、PDF、Word 生成、预览、下载和会话归档 |
| 历史记录 | 会话内筛选、分页、缩略图和导出 |

识别类别为“疑似龋坏、疑似根尖周异常、疑似阻生或埋伏牙”。检测结果页包含“结果总览、结构化结果、联动复核、检测报告”四个子页。

## 多人检测行为

单图、多模型、批量和批量重试共用 <code>yolo_inference</code> 队列，CPU 推理并发上限为 1。点击后会先立即显示“已加入检测队列”，再等待 Gradio 队列执行；心跳、<code>finally</code> 清理和默认 900 秒超时用于避免异常任务卡死。多个浏览器可以同时提交，但实际推理按顺序完成，不是多 GPU 并行。

## 会话与安全

- 每个浏览器会话使用请求头/HttpOnly Cookie 分配独立输出目录；
- 会话数据仅用于答辩期间的临时查看和导出，不提供账号、注册或跨设备永久档案；
- <code>DENTAL_SESSION_COOKIE_SECURE=1</code> 只能配合 HTTPS；
- API Key 只能写入服务器环境文件，不能提交到 Git；
- 公网访问必须叠加 Nginx、校园 VPN 或 Basic Auth；
- 答辩后删除 <code>outputs/</code> 中的影像、报告和历史记录。

## 关键配置

| 变量 | 说明 |
| --- | --- |
| <code>DENTAL_HOST</code> / <code>DENTAL_PORT</code> | 监听地址和端口，默认 127.0.0.1:7860 |
| <code>DENTAL_AI_PROVIDER</code> | <code>google</code>、<code>aliyun</code> 或 <code>ollama</code> |
| <code>GOOGLE_API_KEY</code> | Gemini 密钥；<code>GOOGLE_MODEL=auto</code> 自动发现 Flash |
| <code>DASHSCOPE_API_KEY</code> | 阿里云百炼密钥，按可用文本模型遍历 |
| <code>OLLAMA_API_KEY</code> / <code>OLLAMA_BASE_URL</code> | Ollama 接口配置 |
| <code>INFERENCE_TIME_LIMIT_SECONDS</code> | 单任务超时保护，默认 900 秒 |
| <code>OUTPUT_RETENTION_DAYS</code> / <code>OUTPUT_MAX_GB</code> | 输出自动清理策略 |

完整配置、systemd、Nginx、答辩验收流程和 FAQ 请阅读 [README_SHOW.md](README_SHOW.md)。

## 资源建议

4 核/8 GB 是受控答辩的最低建议，8 核/16 GB 更稳；CPU 即可运行。保持单 Uvicorn worker，避免模型重复加载和跨会话状态混乱。

## 许可证

请阅读 [LICENSE](LICENSE)，并遵守 Ultralytics 相关 AGPL-3.0 条款及模型、数据集和第三方资源的独立许可。
