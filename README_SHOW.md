# DentalV8 show 分支

这是面向项目答辩现场的精简部署分支，基于 `main` 的运行代码构建，保留首页、单图检测、多模型对比、批量检测、历史记录、智诊管家和报告中心所需的最小资源。

## 分支边界

- 不需要登录注册。Gradio 检测请求使用其会话哈希，智诊管家请求使用当前标签页的 `sessionStorage` 标识并由服务端 HttpOnly Cookie 兜底；检测结果、历史、对话上下文和导出报告按会话目录隔离。该机制用于答辩演示的软隔离，不等同于身份认证。
- 不使用 `localStorage` 保存会话标识；前端仅用 `sessionStorage` 生成智诊管家请求标识，服务端按请求会话标识分桶，Cookie 只作兜底。
- 不保存真实 API 密钥。AI 密钥只从服务器环境变量读取，参考 `.env.example`。
- 仅保留三个实际运行模型权重，训练数据、实验文档、旧报告和无关脚本不在此分支。
- `outputs/` 是运行时目录，不应提交到仓库；可通过 `OUTPUT_RETENTION_DAYS` 和 `OUTPUT_MAX_GB` 自动清理。

## Linux 服务器部署

```bash
git clone -b show https://github.com/zwylovinghunter/Dentalv8.git /srv/Dentalv8
cd /srv/Dentalv8
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements-show.txt
sudo install -D -m 600 .env.example /etc/dentalv8/dentalv8.env
# 编辑 /etc/dentalv8/dentalv8.env，至少填写需要使用的平台密钥
python app.py
```

正式答辩建议使用 systemd 与 Nginx：

```bash
sudo useradd --system --home /srv/Dentalv8 --shell /usr/sbin/nologin dentalv8
sudo install -d -o dentalv8 -g dentalv8 /etc/dentalv8 /var/lib/dentalv8
sudo cp deploy/dentalv8.service /etc/systemd/system/dentalv8.service
sudo systemctl daemon-reload
sudo systemctl enable --now dentalv8
```

将 `deploy/nginx.conf.example` 配置到 HTTPS 站点后，老师使用浏览器访问域名即可。健康检查地址为 `/healthz`，返回 `{"ok": true}` 即表示进程可用。

## 答辩现场建议

单进程、CPU 推理、`INFERENCE_CONCURRENCY_LIMIT=1` 可以避免多位老师同时操作时模型互相抢占；不同浏览器或隐私窗口拥有独立会话。若需要同时处理更多图片，应升级服务器 CPU/内存并另行压测，不建议直接改成多 worker，因为模型会重复占用内存。

本分支保留 Ultralytics 的许可证与版权文件；部署者应继续遵守其许可证要求。
