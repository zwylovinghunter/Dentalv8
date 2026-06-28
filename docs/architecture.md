# 项目结构与拆分策略

本文档说明当前 Gradio 应用的模块边界。目标是让 `app.py` 继续作为稳定入口，同时把低风险、可复用、不会改变展示逻辑的内容逐步外置。

## 当前模块

```text
app.py                  应用入口、页面布局、事件绑定、核心业务流程
assistant/config.py     智诊管家配置、推荐追问主题、回答限制
detection/constants.py  牙病类别知识、类别别名
reports/constants.py    报告和页面统一免责声明
ui/empty_states.py      检测空状态、进度条 HTML 生成函数
ui/styles.py            Gradio 全局 CSS、设计变量、页面样式
ui/head.py              导航、主题切换、全屏预览、悬浮放大等前端脚本
pages/                  页面级组件拆分的预留目录
services/               权重发现、历史记录、云端问答等服务拆分的预留目录
```

## 本次拆分原则

- 优先迁移纯常量、纯 HTML/CSS/JS 字符串和无状态 UI 函数。
- 不改变 Gradio 组件创建顺序。
- 不改变任何 `.click()`、`.change()`、`.clear()` 的输入输出列表。
- 不改变检测推理、报告生成、历史记录和智诊问答逻辑。
- 不用全局 CSS 重写所有 Markdown、textarea 或 image，尽量保留现有选择器。

## 后续推荐拆分顺序

1. `services/model_registry.py`

   迁移权重扫描、模型注册表、指纹计算和状态 Markdown。

2. `detection/core.py`

   迁移图片归一化、YOLO 推理、检测框渲染、区域裁剪和联动放大。

3. `reports/generator.py`

   迁移 Markdown/PDF/Word 报告生成、图片资产写入和报告预览处理。

4. `assistant/runtime.py`

   迁移检测上下文压缩、云端问答请求、追问生成和反馈逻辑。

5. `pages/*.py`

   在业务函数稳定后，再按页面拆出 `build_dashboard_page()`、`build_detection_page()`、`build_batch_page()` 等页面构建函数。

## 注意事项

- Gradio 组件变量在事件绑定中大量复用，拆页面时必须确保组件引用仍然返回给 `build_app()`。
- 多个检测事件共享 `concurrency_id="yolo_inference"`，不能在拆分时丢失。
- 批量检测、报告中心和智诊管家共享最新检测上下文，拆服务时要保留同一份状态更新入口。
- CSS 修改应优先放在 `ui/styles.py`，避免在页面函数中散落内联样式。
- 前端脚本修改应优先放在 `ui/head.py`，并保持幂等安装标记，避免重复绑定事件。
