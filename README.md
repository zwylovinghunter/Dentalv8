<div align="center">

# DentalV8 牙齿病变目标区域识别与辅助分析平台

面向口腔影像的 YOLO 疑似病变区域检测、模型复核、智能解释与报告编排平台

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://www.gradio.app/"><img src="https://img.shields.io/badge/Gradio-Blocks-F97316" alt="Gradio Blocks"></a>
  <a href="https://github.com/ultralytics/ultralytics"><img src="https://img.shields.io/badge/YOLOv8-Ultralytics-111827" alt="YOLOv8"></a>
  <a href="https://pytorch.org/"><img src="https://img.shields.io/badge/运行设备-CPU%20默认-0F766E" alt="CPU default"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue" alt="AGPL-3.0"></a>
</p>

</div>

> [!WARNING]
> 本系统只用于牙齿病变疑似区域的辅助识别、科研展示和人工复核准备，不能替代口腔医生的临床诊断。置信度不是患病概率，也不代表病变严重程度；请始终结合原始影像、病史和专业医生意见。

## 目录

- [项目定位](#项目定位)
- [核心功能](#核心功能)
- [识别类别与模型](#识别类别与模型)
- [系统工作流](#系统工作流)
- [环境要求](#环境要求)
- [安装与启动](#安装与启动)
- [智诊管家与 AI 服务](#智诊管家与-ai-服务)
- [典型使用流程](#典型使用流程)
- [输出文件与隐私](#输出文件与隐私)
- [代码结构](#代码结构)
- [分支定位](#分支定位)
- [部署与安全边界](#部署与安全边界)
- [验证与回归检查](#验证与回归检查)
- [常见问题](#常见问题)
- [许可证与贡献](#许可证与贡献)

## 项目定位

DentalV8 是一个基于 Gradio Blocks、FastAPI 和 Ultralytics YOLO 的本科毕业设计/科研演示平台。主分支保留完整的研究展示闭环：

1. 上传口腔影像并进行单模型检测；
2. 用三种模型对同一影像进行并列复核；
3. 对多张影像进行批量初筛和失败项重试；
4. 在结构化结果、局部放大和人工复核建议之间联动；
5. 让智诊管家依据当前检测上下文解释结果；
6. 将单图、对比和批量结果编排为 Markdown、PDF、Word 报告，并在报告中心归档回看。

项目默认面向本机、实验室内网和答辩演示。主分支没有登录注册，也没有多用户身份认证，不应直接暴露在公网。

## 核心功能

| 工作区 | 主要能力 | 典型输出 |
| --- | --- | --- |
| 牙病学习 | 展示三类疑似病变的影像特征、复核关注点、就诊前准备和权威科普链接 | 类别知识卡片、复核提示 |
| 首页概览 | 汇总任务数量、疑似区域、风险等级、平均置信度、模型耗时和权重状态 | 指标卡、趋势图、近期任务 |
| 图像检测 | 单张影像上传、模型选择、置信度/IoU 阈值、框线样式和局部放大 | 标注图、结构化表、区域解释、单项报告 |
| 多模型对比 | 同一影像运行三种模型，计算相近区域的一致性与分歧 | 并列结果、融合图、一致性表、对比报告 |
| 批量检测 | 多张影像逐张处理、任务队列、失败项重试、图片级筛选 | 预览图、优先级表、CSV/Markdown 报告 |
| 历史记录 | 按任务类型和复核等级筛选、分页浏览、缩略图查看、CSV 导出或清空 | 可追溯任务列表 |
| 智诊管家 | 选择分析范围和回答视图，结合检测上下文进行问答、追问和反馈 | Markdown 回答、追问建议、会话导出 |
| 报告中心 | 汇总当前单图、多模型和批量结果，统一预览、下载和归档 | Markdown、PDF、Word、图片资产 |

检测页面内部还提供“结果总览 / 结构化结果 / 联动复核 / 检测报告”四个子页。结果表、检测框、局部放大和复核说明会同步定位，减少在长页面中反复查找的成本。

## 识别类别与模型

### 检测类别

模型原始类别名会在界面中转换为更适合复核的中文名称，同时保留英文标识便于追溯：

| 模型类别 | 界面名称 | 复核含义 |
| --- | --- | --- |
| <code>Caries</code> | 疑似龋坏（Caries） | 需要结合牙体结构和临床检查复核 |
| <code>Periapical_Lesion</code> | 疑似根尖周异常（Periapical Lesion） | 需要结合根尖区影像与病史复核 |
| <code>Impacted</code> | 疑似阻生或埋伏牙（Impacted） | 需要结合牙位、萌出情况和全景片复核 |

默认使用“按类别配色”，同一类别在不同目标编号下保持一致颜色；后处理会在 YOLO NMS 后抑制同类高度重叠候选框，降低重复框对人工阅读的干扰。

### 展示模型

系统会递归扫描 <code>.pt</code> 权重，并依据目录名、README、<code>args.yaml</code> 和关键词匹配三个展示角色：

| 角色 | 当前首选权重 | 用途 |
| --- | --- | --- |
| 均衡型基线模型 | <code>results/yolov8n+baseline_e50/weights/best.pt</code> | 速度与基础效果的对照基线 |
| 高精度牙齿病变定位模型 | <code>results/yolov8m+PIoU/weights/best.pt</code> | 强调定位精度和结果稳定性 |
| 高召回牙齿病变检测模型 | <code>results/yolov8n+Gated-SPDConv-neck-P4/weights/best.pt</code> | 初筛时尽量减少漏检 |

权重缺失、加载失败或推理失败时，页面会展示可读的失败原因，不会伪造检测框。实际效果仍取决于训练数据、影像质量、阈值和设备性能。

## 系统工作流

~~~mermaid
flowchart LR
    A[上传 JPG/PNG 口腔影像] --> B[RGB 预处理与尺寸规范化]
    B --> C[自动匹配 YOLO 权重]
    C --> D[CPU 推理]
    D --> E[置信度筛选与 NMS/重叠抑制]
    E --> F[中文类别、框线和结构化结果]
    F --> G[联动复核与智诊管家]
    F --> H[Markdown/PDF/Word 报告]
    G --> I[历史记录与报告归档]
    H --> I
~~~

多模型对比会把三个模型的结果按类别和 IoU 进行对照，区分全模型共识、部分共识和模型分歧；批量检测则逐张处理并保留失败项，以便单独重试。

## 环境要求

- Windows 10/11 或 Linux；
- Python 3.10–3.12（当前开发环境已验证 Python 3.12.3）；
- 建议 8 GB 以上内存；CPU 可运行，GPU 不是必需条件；
- 依赖见 <code>requirements.txt</code>，其中包含 Gradio、PyTorch、Ultralytics、OpenCV、Pillow、Pandas、ReportLab 和 python-docx；
- 三个展示模型权重需要存在于仓库或可被自动扫描到的结果目录中。

> CPU 全景片推理可能需要数秒到数十秒。首次启动还会加载和预热模型，请不要把首次等待误认为页面卡死。

## 安装与启动

### 1. 创建环境并安装依赖

~~~bash
git clone https://github.com/zwylovinghunter/Dentalv8.git
cd Dentalv8
python -m venv .venv
~~~

Windows PowerShell：

~~~powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
~~~

Linux/macOS：

~~~bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
~~~

### 2. 启动应用

Windows 推荐使用带缓存隔离和安全清理逻辑的启动器：

~~~powershell
.\start_project.cmd
~~~

或：

~~~powershell
.\start_project.ps1 -Port 7860 -ListenAddress 127.0.0.1
~~~

在 Linux/macOS 或需要直接调试时：

~~~bash
python app.py
~~~

应用默认监听本机地址，并从 7860 开始寻找可用端口。以终端打印的 URL 为准。Windows 启动器会把临时文件和 Gradio/PyTorch 缓存放到 <code>.runtime</code>，退出时只清理受控的临时目录；如果项目放在系统盘，启动器的安全检查可能拒绝运行，此时请将项目移到非系统盘或直接使用开发命令。

## 智诊管家与 AI 服务

智诊管家支持三种云端平台，并始终保留本地规则模式作为降级路径：

| 平台 | 环境变量选择 | 模型策略 |
| --- | --- | --- |
| Google Gemini | <code>DENTAL_AI_PROVIDER=google</code> | <code>GOOGLE_MODEL=auto</code> 时先发现可用的最新 Flash，再按 3.8 → 3.7 → 3.6 Flash 回退 |
| 阿里云百炼 | <code>DENTAL_AI_PROVIDER=aliyun</code> | 查询可用文本模型，优先尝试 Qwen/DeepSeek/GLM/Kimi 等配置列表，再遍历其他可用模型 |
| Ollama | <code>DENTAL_AI_PROVIDER=ollama</code> | 依次尝试主模型和 <code>OLLAMA_FALLBACK_MODELS</code> |
| 本地规则 | 在页面关闭云端调用或云端失败时自动启用 | 不需要 API Key，不影响检测和报告功能 |

示例（仅使用占位符，真实密钥不要写入仓库）：

~~~powershell
$env:DENTAL_AI_PROVIDER = "google"
$env:GOOGLE_API_KEY = "REPLACE_ME"
$env:GOOGLE_MODEL = "auto"
$env:GOOGLE_FALLBACK_MODELS = "gemini-3.8-flash,gemini-3.7-flash,gemini-3.6-flash"

# 如改用阿里云百炼：
# $env:DENTAL_AI_PROVIDER = "aliyun"
# $env:DASHSCOPE_API_KEY = "REPLACE_ME"
# $env:DASHSCOPE_PREFERRED_MODELS = "qwen3.8-flash,qwen3.7-plus,qwen3.7-flash,deepseek-v4-flash,glm-5.2,kimi-k3"

# 如改用 Ollama：
# $env:DENTAL_AI_PROVIDER = "ollama"
# $env:OLLAMA_API_KEY = "REPLACE_ME"
# $env:OLLAMA_BASE_URL = "https://ollama.com/api/chat"
# $env:OLLAMA_MODEL = "gpt-oss:20b"
# $env:OLLAMA_FALLBACK_MODELS = "qwen3.5:397b,deepseek-v4-flash"
~~~

云端请求包含超时、重试和模型遍历；所有候选模型不可用、密钥缺失或网络异常时，页面会明确显示原因并切换到本地规则分析。AI 只负责解释已有检测上下文，不会生成替代检测框，也不应被当作临床诊断工具。

## 典型使用流程

1. 在“牙病学习”了解类别释义和人工复核注意事项；
2. 在“图像检测”上传一张清晰影像，选择模型和阈值，查看标注图、结构化结果及局部放大；
3. 需要比较稳定性时进入“多模型对比”，重点查看一致性与分歧区域；
4. 需要处理多张影像时进入“批量检测”，先看任务状态和复核优先级，再对失败项重试；
5. 打开“智诊管家”，选择当前单图、当前多模型、当前批量或全部最新结果，使用推荐追问或自定义问题；
6. 在“报告中心”选择报告范围和语言，预览并下载 Markdown、PDF、Word，或从归档列表重新打开；
7. 在“历史记录”按任务类型/复核等级追溯结果，必要时导出 CSV。

智诊管家消息区右侧的问答位置导航只在有问题时出现：横杠用于定位历史提问，悬浮显示问题全文，点击只滚动消息区域，不会保存到服务器的永久对话库。

## 输出文件与隐私

运行产物默认位于：

~~~text
outputs/
├── history.json          # 单图、对比、批量任务索引
├── chat_feedback.json    # 云端回答反馈
├── reports/              # Markdown、PDF、Word、CSV 等报告
└── report_assets/        # 报告引用的标注图和局部图
~~~

<code>OUTPUT_RETENTION_DAYS</code>、<code>OUTPUT_MAX_GB</code>、<code>OUTPUT_KEEP_RECENT_FILES</code> 和 <code>OUTPUT_CLEANUP_INTERVAL_SECONDS</code> 可控制自动清理。请在提交代码、截图或答辩材料前检查输出目录，不要上传患者影像、姓名、绝对路径、报告或 API Key。

主分支没有登录注册和多用户身份隔离：历史文件、反馈文件和部分 AI 上下文由单个应用实例共享。若需要多位老师通过网络独立体验，请使用 [show 分支](https://github.com/zwylovinghunter/Dentalv8/tree/show) 的会话隔离和排队部署方案，而不是直接增加 Uvicorn worker。

## 代码结构

~~~text
app.py                  Gradio/FastAPI 入口、页面布局、事件绑定和推理流程
assistant/config.py      智诊管家范围、角色、追问和上下文限制
detection/constants.py  类别别名、类别知识和安全文案
reports/                报告常量与 Markdown/PDF/Word 导出
services/                运行缓存、文件和服务层辅助逻辑
ui/                     CSS、空状态、页面头部脚本和交互样式
pages/                  后续页面拆分预留目录
results/                实验结果、模型权重和说明
docs/screenshots/       脱敏运行截图的建议目录
start_project.*         Windows 运行缓存隔离启动器
~~~

## 分支定位

| 分支 | 适用场景 | 关键边界 |
| --- | --- | --- |
| <code>main</code> | 完整开发、科研展示和功能迭代 | 功能最全，但无登录和多用户身份隔离，适合本机/受控内网 |
| <code>show</code> | 答辩现场或云服务器精简部署 | 只保留必要资源，提供匿名会话软隔离、健康检查和多人检测排队提示 |

切换答辩版本：

~~~bash
git switch show
~~~

## 部署与安全边界

本分支适合本机或受控内网。若要对外提供访问，请至少：

- 使用 HTTPS 反向代理和额外的访问控制（校园 VPN、Basic Auth 或网关）；
- 将应用绑定在 <code>127.0.0.1</code>，不要直接暴露 Gradio 端口；
- 通过环境变量注入密钥，轮换曾经在聊天、日志或截图中出现过的密钥；
- 对上传影像和报告设置保留期限，并在答辩后删除；
- 只使用脱敏样本，遵守医院/学校的数据合规要求；
- 不将 <code>outputs/</code>、模型缓存或真实患者资料提交到 Git。

面向答辩服务器的完整 systemd、Nginx、健康检查和匿名会话说明请直接阅读 [show README](https://github.com/zwylovinghunter/Dentalv8/blob/show/README.md)。

## 验证与回归检查

提交前至少执行：

~~~bash
python -m py_compile app.py assistant/config.py detection/constants.py reports/constants.py ui/empty_states.py ui/styles.py ui/head.py
git diff --check
~~~

手动回归建议覆盖：

- 八个顶部工作区导航及桌面悬浮展开/移动端折叠；
- 单图检测的上传、阈值、中文类别标签、按类别配色、重叠框抑制和联动放大；
- 多模型一致性/分歧分析；
- 批量进度、失败重试、预览和 CSV/Markdown 报告；
- 智诊管家的范围切换、推荐追问、问答位置导航、复制/反馈和导出；
- 报告中心的 Markdown/PDF/Word 生成、图片预览、归档回看；
- 历史分页、筛选、缩略图、CSV 导出和清空。

## 常见问题

### 为什么第一次启动很慢？

首次启动需要导入 PyTorch/Ultralytics、扫描权重并预热模型。CPU 环境下首个任务也可能比后续任务慢。

### 为什么 AI 显示“已切换为本地规则模式”？

通常是密钥缺失、模型暂时高负载、接口超时或余额/权限不足。检查对应环境变量和网络；检测、报告和历史功能不依赖云端 AI。

### 为什么看不到检测框？

先确认图片格式和清晰度，再查看页面中的模型状态、阈值和失败原因。权重未匹配或推理失败时，系统不会用示例框冒充真实结果。

### 多模型结果不一致是不是系统出错？

不一定。模型训练策略、阈值和召回目标不同，结果可能存在差异；应查看一致性/分歧说明并交由专业人员复核。

### 可以让多位老师同时使用主分支吗？

主分支没有身份隔离，不建议多人直接共享一个实例。答辩场景请使用 show 分支；即使在 show 中，YOLO CPU 推理也按队列串行，浏览器会看到排队提示。

### 结果和报告是否能作为诊断结论？

不能。系统只输出疑似区域和复核建议，最终判断必须由专业口腔医生结合原始影像和临床资料完成。

## 许可证与贡献

仓库包含 Ultralytics 相关代码和模型运行组件，请遵守仓库中的 [LICENSE](LICENSE) 及其适用的 AGPL-3.0 条款；训练数据、权重和第三方资源还应遵守各自的授权要求。

欢迎通过 Issue 或 Pull Request 提交界面改进、文档修正和可复现的 bug 报告。提交前请移除真实影像、API Key、报告和本地绝对路径。

项目地址：[github.com/zwylovinghunter/Dentalv8](https://github.com/zwylovinghunter/Dentalv8)
