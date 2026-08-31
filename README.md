# 牙齿病变目标区域识别与辅助分析平台

这是一个基于 Gradio Blocks 的牙齿影像辅助识别平台，用于课程验收、科研展示和模型效果复核。系统聚焦三类常见疑似病变与牙周风险相关提示，提供单图检测、多模型对比、批量筛查、智诊管家、报告中心和历史记录等功能。

> 本系统仅用于牙齿病变疑似区域的辅助识别与科研展示，不作为临床诊断依据，最终结果应由专业口腔医生结合原始影像和其他临床资料复核。

## 快速启动

```bash
pip install -r requirements.txt
python app.py
```

启动后打开控制台显示的地址。默认会从 `7860` 开始寻找可用端口，例如：

```text
http://127.0.0.1:7860/
```

如果本地已有服务占用端口，程序会自动尝试后续端口。

## 功能概览

- 牙病学习：展示三类常见疑似病变与牙周风险说明、复核关注点和安全声明。
- 首页 Dashboard：统计检测图片数、疑似区域数、失败任务、平均置信度、模型耗时和近期记录。
- 图像检测：上传单张影像，选择模型、阈值和检测框样式，输出标注图、结构化表格和解释。
- 多模型对比：同一张影像运行多个模型，展示模型差异、一致性区域和融合叠加图。
- 批量检测：一次处理多张影像，生成预览、单图解释、牙病类别卡片、CSV/Markdown 报告。
- 智诊管家：基于当前检测上下文回答问题，并实时生成推荐追问。
- 报告中心：生成 Markdown、PDF、Word 报告，包含封面、摘要、风险分级、图片和复核说明。
- 历史记录：保存近期检测、对比和批量任务，支持筛选、查看详情和导出。

## 功能截图

建议将真实运行截图保存到 `docs/screenshots/`，命名如下，便于论文、答辩或部署文档引用：

| 页面 | 建议文件名 | 截图重点 |
|---|---|---|
| 牙病学习 | `docs/screenshots/learn.png` | 三类病变介绍与复核关注点 |
| 图像检测 | `docs/screenshots/single-detection.png` | 上传区、检测结果、解释卡片 |
| 多模型对比 | `docs/screenshots/model-comparison.png` | 三模型结果、一致性表、融合图 |
| 批量检测 | `docs/screenshots/batch-detection.png` | 批量预览、牙病卡片、汇总表 |
| 智诊管家 | `docs/screenshots/assistant.png` | 对话、推荐追问、输入框 |
| 报告中心 | `docs/screenshots/report-center.png` | 报告预览和下载入口 |

当前仓库不提交运行截图，避免把本地患者影像、路径或临时报告误传到远程仓库。

## 模型与权重

系统会递归扫描项目中的 `.pt` 权重，并结合目录名、`README`、`args.yaml` 和文件名关键词自动匹配模型：

- 均衡型基线模型：速度和基础检测效果平衡。
- 高精度牙齿病变定位模型：强调定位精度和结果稳定性。
- 高召回轻量化牙齿病变检测模型：强调减少漏检，适合初筛。

如果权重未匹配、加载失败或推理失败，页面会显示明确状态，不会伪造检测框，也不会让单个模型失败影响其他模型。

## 智诊管家配置

联网问答使用 Ollama Cloud 兼容接口。可选环境变量：

```powershell
$env:OLLAMA_API_KEY = "你的密钥"
$env:OLLAMA_BASE_URL = "https://ollama.com/api/chat"
$env:OLLAMA_MODEL = "gpt-oss:20b"
$env:OLLAMA_FALLBACK_MODELS = "qwen3.5:397b,deepseek-v4-flash"
.\start_project.cmd
```

如果未配置密钥、网络异常或云端模型不可用，系统会降级为本地规则回答，不影响检测、对比、批量处理和报告生成。

## 报告与数据

- 报告输出：`outputs/reports/`
- 报告图片资产：`outputs/report_assets/`
- 历史记录：`outputs/history.json`
- 智诊反馈：`outputs/chat_feedback.json`

`outputs/` 为运行产物目录，通常不应提交到远程仓库。

## Windows 启动与运行缓存

推荐直接双击根目录的 `start_project.cmd`，或在 PowerShell 中运行：

```powershell
.\start_project.ps1
```

启动器会在 Python、Gradio 和 PyTorch 加载前，将临时文件及框架缓存定向到项目的 `.runtime/`（D 盘）。按 `Ctrl+C` 正常关闭后，只会自动清理 `.runtime/temp` 与 `.runtime/gradio`；模型缓存、检测结果和报告会保留。为避免缓存重新写入 C 盘，不再推荐直接执行旧的 `python app.py` 或裸 `uvicorn` 命令。

## 代码结构

当前主入口仍为 `app.py`，为了降低回归风险，本次先拆分纯配置、样式和 UI 常量：

```text
app.py                  Gradio 应用入口、组件布局、事件绑定
assistant/config.py     智诊管家文案、追问主题、上下文数量限制
detection/constants.py  牙病类别知识与类别别名
reports/constants.py    报告免责声明文本
ui/empty_states.py      检测空状态与进度条 UI 生成函数
ui/styles.py            全局 CSS 与设计变量
ui/head.py              页面导航、主题、截图放大等前端脚本
pages/                  后续页面级拆分目录
services/               后续模型、历史、文件、云端接口服务目录
```

更详细的拆分策略见 [docs/architecture.md](docs/architecture.md)。

## 部署建议

本项目默认使用 CPU 推理，适合课程展示和普通 Windows 开发环境。

```powershell
.\start_project.cmd
```

生产或内网部署时建议：

- 使用固定 Python 虚拟环境；
- 将模型权重和运行产物目录放在明确路径；
- 通过反向代理或内网网关提供访问；
- 不在代码中硬编码任何 API Key；
- 定期清理 `outputs/reports/` 中的临时报告。

## 常见问题

**检测很慢怎么办？**

CPU 推理对大尺寸全景片会较慢。可适当降低输入图片尺寸、减少批量图片数量，或后续接入 GPU 推理服务。

**为什么结果只写“疑似区域”？**

系统只做辅助识别和科研展示，不能替代临床诊断，因此统一使用“疑似区域”“建议人工复核”等安全表述。

**多模型结果不一致是否代表错误？**

不一定。不同权重、阈值和目标召回策略会产生差异。多模型对比页面用于帮助人工复核这些差异。

**批量检测报告在哪里？**

批量检测完成后页面可下载 Markdown 和 CSV，文件同时保存在 `outputs/reports/`。

**推荐追问为什么会变化？**

智诊管家会结合最新用户问题、最新助手回答和当前检测上下文生成追问；云端不可用时会回退到本地规则推荐。

## 开发验证

```bash
python -m py_compile app.py assistant/config.py detection/constants.py reports/constants.py ui/empty_states.py ui/styles.py ui/head.py
python app.py
```

浏览器打开页面后重点检查：

- 三个检测页面上传、清空、检测、进度条和报告按钮；
- 批量检测左右栏布局、牙病卡片、结果解释和汇总表；
- 多模型融合图标注、筛选和联动放大；
- 智诊管家提问、推荐追问和导出；
- 报告中心 Markdown/PDF/Word 下载。
