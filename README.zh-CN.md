<div align="center">

# DentalV8 中文项目说明

这是 DentalV8 牙齿病变目标区域识别与辅助分析平台的中文入口文档。

<p>
  <a href="README.md"><img src="https://img.shields.io/badge/主文档-README.md-2563EB" alt="主文档"></a>
  <a href="https://github.com/zwylovinghunter/Dentalv8/tree/show"><img src="https://img.shields.io/badge/答辩部署版-show-0F766E" alt="show branch"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue" alt="AGPL-3.0"></a>
</p>

</div>

> [!WARNING]
> 本项目只用于科研展示、课程验收和人工复核准备，不是医疗器械，也不能替代专业口腔医生的诊断。所有“疑似区域”和置信度都必须结合原始影像、病史和临床检查解释。

## 项目简介

DentalV8 使用 Gradio Blocks、FastAPI、PyTorch 和 Ultralytics YOLO 构建，围绕口腔影像提供：

- 单图检测、三模型对比和批量筛查；
- 疑似龋坏、疑似根尖周异常、疑似阻生或埋伏牙三类目标展示；
- 中文类别标签、按类别配色、重叠框抑制、局部放大和联动复核；
- 智诊管家问答、推荐追问、问答位置导航和安全降级；
- Markdown、PDF、Word、CSV 报告及历史归档。

完整功能矩阵、工作流、配置项和回归清单请阅读主文档：[README.md](README.md)。

## 八个工作区

| 工作区 | 用途 |
| --- | --- |
| 牙病学习 | 查看类别知识、影像特征和复核注意事项 |
| 首页概览 | 查看任务数量、风险等级、模型状态和运行趋势 |
| 图像检测 | 对单张影像进行模型推理和区域级复核 |
| 多模型对比 | 对照三个模型的一致区域和分歧区域 |
| 批量检测 | 按任务队列逐张筛查并重试失败项 |
| 历史记录 | 筛选、分页查看和导出近期任务 |
| 智诊管家 | 结合选定检测范围进行解释性问答 |
| 报告中心 | 汇总结果并生成、预览和归档报告 |

检测页面还提供“结果总览、结构化结果、联动复核、检测报告”四个子页。顶部导航和结果导航支持桌面端悬浮说明，移动端会折叠为紧凑布局。

## 快速开始

推荐 Python 3.10–3.12，当前开发环境使用 Python 3.12.3。CPU 可以运行完整流程，首次启动会扫描并预热模型。

~~~bash
git clone https://github.com/zwylovinghunter/Dentalv8.git
cd Dentalv8
python -m venv .venv
~~~

Windows PowerShell：

~~~powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
.\start_project.cmd
~~~

Linux/macOS：

~~~bash
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
python app.py
~~~

以终端输出的本机 URL 为准。Windows 启动器会把临时缓存放到 <code>.runtime</code> 并在退出时安全清理受控目录。

## 智诊管家配置

云端平台由 <code>DENTAL_AI_PROVIDER</code> 选择：

| 值 | 平台 | 回退行为 |
| --- | --- | --- |
| <code>google</code> | Google Gemini | 自动发现最新 Flash，失败时按 3.8、3.7、3.6 Flash 尝试 |
| <code>aliyun</code> | 阿里云百炼 | 发现可用文本模型，优先尝试 Qwen、DeepSeek、GLM、Kimi 等模型 |
| <code>ollama</code> | Ollama | 依次尝试主模型和备用模型 |
| 页面关闭云端调用 | 本地规则模式 | 不需要密钥，云端超时或不可用时自动启用 |

示例：

~~~powershell
$env:DENTAL_AI_PROVIDER = "google"
$env:GOOGLE_API_KEY = "REPLACE_ME"
$env:GOOGLE_MODEL = "auto"

# $env:DENTAL_AI_PROVIDER = "aliyun"
# $env:DASHSCOPE_API_KEY = "REPLACE_ME"
~~~

不要将真实 API Key 写入源代码、README、截图或 Git 历史。云端 AI 只解释检测上下文，不会改变 YOLO 检测结果。

## 数据边界

主分支没有登录注册和多用户身份认证。检测结果、历史记录、报告和部分反馈会写入本地 <code>outputs/</code>；因此主分支适合本机或受控内网，不适合直接公开部署。答辩现场或云服务器请使用精简的 [show 分支](https://github.com/zwylovinghunter/Dentalv8/tree/show)，该分支提供匿名会话软隔离、<code>/healthz</code> 健康检查和检测排队提示。

## 识别类别

| 原始类别 | 界面名称 |
| --- | --- |
| <code>Caries</code> | 疑似龋坏（Caries） |
| <code>Periapical_Lesion</code> | 疑似根尖周异常（Periapical Lesion） |
| <code>Impacted</code> | 疑似阻生或埋伏牙（Impacted） |

类别颜色默认固定，后处理会抑制同类高度重叠框；这些显示优化只改善复核体验，不等于提高临床诊断准确率。

## 许可证

仓库包含 Ultralytics 相关代码和运行组件，请阅读 [LICENSE](LICENSE) 并遵守适用的 AGPL-3.0 条款；模型权重、数据集、图片和第三方资源还需遵守其独立授权。

问题反馈和功能建议请提交 GitHub Issue，并在提交前删除真实患者资料、API Key、报告和本地绝对路径。
