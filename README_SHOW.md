<div align="center">

# DentalV8 show｜答辩与云服务器精简部署版

基于主分支运行代码裁剪的、面向答辩现场和受控内网的 YOLO 牙齿病变辅助识别平台

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12"></a>
  <a href="https://www.gradio.app/"><img src="https://img.shields.io/badge/Gradio-6.14-F97316" alt="Gradio 6.14"></a>
  <a href="https://github.com/ultralytics/ultralytics"><img src="https://img.shields.io/badge/YOLOv8-CPU%20推理-111827" alt="YOLOv8 CPU"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue" alt="AGPL-3.0"></a>
</p>

</div>

> [!WARNING]
> 本分支只用于课程验收、毕业答辩和科研演示，不是医疗器械，也不能替代专业口腔医生的诊断。检测结果是疑似区域提示，置信度不是患病概率；请使用脱敏影像并由专业人员复核。

> 主分支：[完整研发版](https://github.com/zwylovinghunter/Dentalv8/tree/main) · 当前分支：[show](https://github.com/zwylovinghunter/Dentalv8/tree/show)

## 目录

- [分支定位](#分支定位)
- [功能概览](#功能概览)
- [识别类别与模型](#识别类别与模型)
- [部署拓扑](#部署拓扑)
- [多人检测队列](#多人检测队列)
- [环境要求](#环境要求)
- [快速启动](#快速启动)
- [AI 服务配置](#ai-服务配置)
- [会话、数据与隐私](#会话数据与隐私)
- [Linux systemd 与 Nginx](#linux-systemd-与-nginx)
- [配置参考](#配置参考)
- [验证与答辩流程](#验证与答辩流程)
- [常见问题](#常见问题)
- [许可证](#许可证)

## 分支定位

show 分支只保留答辩实际需要的入口、三个展示权重、报告导出、历史记录和智诊管家，不包含训练数据、实验文档、旧报告和无关脚本。它适合：

- 一台云服务器上供几位老师按顺序或同时提交任务；
- 一台答辩电脑本地运行并投屏；
- 通过 HTTPS 反向代理提供临时、受控的浏览器访问。

这里的“匿名会话隔离”是软隔离，不是登录认证。系统不建立用户账号，也不提供审计身份；公开部署仍必须在 Nginx、校园 VPN 或网关层增加访问控制。

## 功能概览

| 工作区 | show 版能力 |
| --- | --- |
| 牙病学习 | 三类疑似病变知识、复核重点、就诊准备和安全声明 |
| 首页概览 | 任务量、疑似区域、风险等级、模型耗时和权重状态 |
| 图像检测 | 单图上传、阈值设置、按类别配色、中文标签、局部联动复核 |
| 多模型对比 | 三个 YOLO 模型并列推理、一致性/分歧分析和融合图 |
| 批量检测 | 多图队列、逐张进度、失败项重试、CSV/Markdown 报告 |
| 历史记录 | 会话内筛选、分页、缩略图和导出 |
| 智诊管家 | 单图/对比/批量/全部结果范围、推荐追问、问答位置导航和安全回退 |
| 报告中心 | 单项和综合 Markdown、PDF、Word 报告的预览、下载与归档 |

检测结果页提供“结果总览、结构化结果、联动复核、检测报告”四个子页。模型类别会显示为“疑似龋坏、疑似根尖周异常、疑似阻生或埋伏牙”，同一类别默认使用一致颜色；后处理会抑制同类高度重叠框。

## 识别类别与模型

| 类别 | 界面名称 |
| --- | --- |
| <code>Caries</code> | 疑似龋坏（Caries） |
| <code>Periapical_Lesion</code> | 疑似根尖周异常（Periapical Lesion） |
| <code>Impacted</code> | 疑似阻生或埋伏牙（Impacted） |

show 版随仓库保留三个展示权重：

~~~text
results/yolov8n+baseline_e50/weights/best.pt
results/yolov8m+PIoU/weights/best.pt
results/yolov8n+Gated-SPDConv-neck-P4/weights/best.pt
~~~

分别对应均衡基线、高精度定位和高召回初筛角色。模型缺失或失败时页面会显示原因，不会生成替代框。

## 部署拓扑

~~~mermaid
flowchart LR
    U[老师浏览器/手机] --> N[HTTPS Nginx<br/>访问控制与 WebSocket]
    N --> S[单个 Uvicorn 进程]
    S --> G[Gradio Blocks 队列]
    G --> Y[YOLO CPU 推理]
    S --> O[按会话划分的 outputs]
    S --> A[Gemini / 阿里云百炼 / Ollama<br/>失败时本地规则]
~~~

推荐只运行一个 Uvicorn worker：模型只加载一份，进程内检测锁、报告状态和会话上下文保持一致。不要为了“并行”直接启动多个 worker；那会重复占用内存，也会让答辩现场更难追踪问题。

## 多人检测队列

四个检测入口（单图精检、多模型会诊、批量筛查、批量单项重试）共用 <code>yolo_inference</code> 并发组，实际 YOLO 推理上限为 1：

1. 用户点击按钮后，<code>queue=False</code> 的前置回调立即更新进度卡，显示“已加入检测队列”以及当前正在处理的任务；
2. 真正的推理回调进入 Gradio 队列，按顺序执行，不让 CPU 模型互相抢占；
3. 推理过程中刷新心跳，避免长批量任务被旧的短时 watchdog 错误清除；
4. 每个任务默认最长运行 900 秒，超时或异常会通过 <code>finally</code> 释放活动状态，后续任务不会永久等待；
5. 页面只滚动当前浏览器的消息/结果区域，排队提示不会改变其他工作区布局。

因此，几位老师可以同时打开页面并提交任务，但检测本身是“多人提交、单队列串行推理”，不是多 GPU 并行。答辩现场建议准备脱敏图片和一份本地备用截图；若需要真实并行吞吐，应另行设计多进程/多 GPU 服务并压测。

## 环境要求

- Python 3.12（<code>requirements-show.txt</code> 已锁定答辩环境依赖）；
- Linux 服务器建议最低 4 核/8 GB，推荐 8 核/16 GB；CPU 可运行，不要求 GPU；
- 服务器应能访问需要的 AI 平台，或准备本地规则模式；
- 上传文件和报告目录需要可写权限；
- Nginx 示例将上传体积限制为 50 MB，可按实际影像大小调整。

## 快速启动

### Linux 直接运行

~~~bash
git clone -b show https://github.com/zwylovinghunter/Dentalv8.git /srv/Dentalv8
cd /srv/Dentalv8
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-show.txt
cp .env.example .env
# 编辑 .env，至少配置 DENTAL_HOST、DENTAL_PORT 和需要使用的 AI 密钥
python app.py
~~~

默认只监听 <code>127.0.0.1:7860</code>。启动后可先执行：

~~~bash
curl http://127.0.0.1:7860/healthz
~~~

返回 <code>{"ok": true}</code> 代表应用进程可用。

### Windows 本地答辩

~~~powershell
.\start_project.cmd
~~~

或者：

~~~powershell
.\start_project.ps1 -Port 7860 -ListenAddress 127.0.0.1
~~~

启动器会把临时缓存放到项目的 <code>.runtime</code>，并拒绝清理未标记目录。以终端打印的 URL 为准。

## AI 服务配置

不要把真实密钥提交到 Git。建议复制 <code>.env.example</code> 后在服务器私有环境文件中填写：

| 平台 | 关键变量 | 模型回退策略 |
| --- | --- | --- |
| Google Gemini | <code>GOOGLE_API_KEY</code>、<code>GOOGLE_MODEL=auto</code> | 自动发现最新 Flash → <code>gemini-3.8-flash</code> → <code>gemini-3.7-flash</code> → <code>gemini-3.6-flash</code> |
| 阿里云百炼 | <code>DASHSCOPE_API_KEY</code> | 先查询可用文本模型，再按 Qwen/DeepSeek/GLM/Kimi 优先列表遍历 |
| Ollama | <code>OLLAMA_API_KEY</code>、<code>OLLAMA_BASE_URL</code> | 主模型 → <code>OLLAMA_FALLBACK_MODELS</code> |
| 本地规则 | 页面关闭云端或云端不可用 | 不需要密钥，继续提供检测结果解释和复核提示 |

示例：

~~~bash
DENTAL_AI_PROVIDER=aliyun
DASHSCOPE_API_KEY=REPLACE_ME
DENTAL_SESSION_COOKIE_SECURE=1
~~~

<code>DENTAL_SESSION_COOKIE_SECURE=1</code> 只应在 HTTPS 已启用时设置；本地 HTTP 演示保持 <code>0</code>。云端超时、HTTP 503、余额/权限异常都会显示来源说明，并自动回到本地规则模式，不会阻塞检测功能。

## 会话、数据与隐私

show 使用请求头、HttpOnly Cookie 和浏览器标签页会话标识，为每个演示会话划分输出目录：

~~~text
outputs/
├── sessions/<session-key>/
│   ├── history.json
│   └── chat_feedback.json
├── reports/<session-key>/
└── report_assets/<session-key>/
~~~

这是答辩场景的软隔离和临时落盘，不是永久账号档案。会话刷新期间可继续查看自己的历史，文件按保留策略自动清理；系统不使用 <code>localStorage</code> 保存身份，也不提供登录、注册和跨设备恢复。

部署前请：

- 只使用脱敏影像；
- 把密钥放在 <code>/etc/dentalv8/dentalv8.env</code> 等受限文件，不放进代码和日志；
- 在 Nginx/校园 VPN/Basic Auth 层增加访问控制；
- 答辩结束后删除 <code>outputs/</code> 中的影像、报告和历史，并轮换临时密钥；
- 不要把 <code>outputs/</code>、截图、报告和本地绝对路径提交到仓库。

## Linux systemd 与 Nginx

### 1. 创建服务账号和目录

~~~bash
sudo useradd --system --home /srv/Dentalv8 --shell /usr/sbin/nologin dentalv8
sudo install -d -o dentalv8 -g dentalv8 /etc/dentalv8 /var/lib/dentalv8
sudo chown -R dentalv8:dentalv8 /srv/Dentalv8
sudo install -o dentalv8 -g dentalv8 -m 600 .env.example /etc/dentalv8/dentalv8.env
sudoedit /etc/dentalv8/dentalv8.env
~~~

至少检查 <code>DENTAL_RUNTIME_ROOT=/var/lib/dentalv8/runtime</code>、端口和密钥；不要直接把示例占位符用于生产。

### 2. 启用 systemd

~~~bash
sudo cp deploy/dentalv8.service /etc/systemd/system/dentalv8.service
sudo systemctl daemon-reload
sudo systemctl enable --now dentalv8
sudo systemctl status dentalv8 --no-pager
curl http://127.0.0.1:7860/healthz
~~~

服务定义使用单进程、自动重启和受限写入目录。查看日志：

~~~bash
sudo journalctl -u dentalv8 -f
~~~

### 3. 配置 HTTPS 反向代理

复制 <code>deploy/nginx.conf.example</code>，替换域名和证书路径：

~~~bash
sudo cp deploy/nginx.conf.example /etc/nginx/sites-available/dentalv8
sudo ln -s /etc/nginx/sites-available/dentalv8 /etc/nginx/sites-enabled/dentalv8
sudo nginx -t
sudo systemctl reload nginx
~~~

示例已配置 WebSocket 升级、关闭代理缓冲和 600 秒读写超时。公网使用前请配置真实证书、域名、访问控制和防火墙，只开放 443（以及必要的 80 → 443 跳转）。

## 配置参考

| 变量 | 默认值 | 作用 |
| --- | --- | --- |
| <code>DENTAL_HOST</code> | <code>127.0.0.1</code> | Uvicorn 监听地址 |
| <code>DENTAL_PORT</code> | <code>7860</code> | Uvicorn 监听端口 |
| <code>DENTAL_AI_PROVIDER</code> | <code>aliyun</code>（示例文件） | <code>google</code>、<code>aliyun</code> 或 <code>ollama</code> |
| <code>DENTAL_SESSION_MAX_AGE</code> | <code>86400</code> | 会话 Cookie 最大秒数 |
| <code>DENTAL_SESSION_COOKIE_SECURE</code> | <code>0</code> | HTTPS 下是否仅通过安全 Cookie |
| <code>DENTAL_RUNTIME_ROOT</code> | 无 | 运行缓存、会话和临时数据根目录 |
| <code>OUTPUT_RETENTION_DAYS</code> | <code>3</code>（示例文件） | 输出保留天数 |
| <code>OUTPUT_MAX_GB</code> | <code>1</code>（示例文件） | 输出目录大小上限 |
| <code>INFERENCE_TIME_LIMIT_SECONDS</code> | <code>900</code> | 单个检测任务超时保护 |

完整变量和默认模型优先级以仓库中的 <code>.env.example</code> 与 <code>app.py</code> 为准。

## 验证与答辩流程

部署后建议按以下顺序验收：

1. <code>/healthz</code> 返回 <code>{"ok": true}</code>；
2. 从电脑和手机分别打开 HTTPS 地址，确认会话提示和页面导航正常；
3. 上传脱敏 JPG/PNG，完成一次单图检测；
4. 依次验证多模型对比、批量检测、失败项重试和报告下载；
5. 在智诊管家切换 Gemini/阿里云百炼/Ollama 或本地规则，确认云端失败能降级；
6. 用两个浏览器同时点击检测，确认后提交者立即看到“已加入检测队列”，前一任务完成后自动执行；
7. 检查历史和报告是否按会话分开，并在演示结束后清理输出。

静态检查：

~~~bash
python -m py_compile app.py
git diff --check
~~~

## 常见问题

### 几位老师能否同时检测？

可以同时打开和提交。show 会立即显示排队提示，但 CPU YOLO 推理仍按一个队列串行执行；这保证模型不互相抢占，也避免多个浏览器覆盖同一进程状态。

### 为什么任务一直显示排队？

先查看当前任务是否仍在运行、服务器 CPU/内存和 <code>journalctl</code> 日志。单任务超过 900 秒会被超时保护释放；如果频繁超时，应减少批量图片、换轻量模型或升级服务器，而不是启动多个 worker。

### AI 返回 HTTP 503 会影响检测吗？

不会。云端问答失败会记录原因并回退本地规则分析，YOLO 检测、历史和报告仍可使用。

### 是否需要 GPU？

答辩规模不需要。CPU 方案更容易部署；若要大规模并行或低延迟服务，应另行设计 GPU 推理服务并进行压力测试。

### 是否可以把服务器直接暴露到公网？

不建议。应用本身没有账号系统；至少使用 HTTPS、Basic Auth/校园 VPN、最小防火墙规则和脱敏数据。

## 许可证

请阅读仓库中的 [LICENSE](LICENSE)，并遵守 Ultralytics 相关 AGPL-3.0 条款。模型权重、数据集、影像和第三方资源还需遵守各自许可。问题和改进建议请通过 GitHub Issue 提交，提交前请删除真实影像、密钥、报告和本地路径。
