from __future__ import annotations

APP_CSS = """
:root {
  --orange: #f97316;
  --orange-dark: #c2410c;
  --blue: #2563eb;
  --sky: #38bdf8;
  --violet: #7c3aed;
  --green: #10b981;
  --ink: #1f2937;
  --muted: #6b7280;
  --line: #e5e7eb;
  --panel: #ffffff;
  --soft: #f8fafc;
  --shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
  --shadow-lg: 0 24px 60px rgba(15, 23, 42, 0.13);
}
.gradio-container {
  min-height: 100vh;
  padding: 0 clamp(10px, 1.4vw, 24px) 28px !important;
  background:
    radial-gradient(circle at 8% 4%, rgba(56, 189, 248, 0.22), transparent 28%),
    radial-gradient(circle at 88% 10%, rgba(249, 115, 22, 0.22), transparent 30%),
    radial-gradient(circle at 70% 88%, rgba(124, 58, 237, 0.13), transparent 35%),
    linear-gradient(180deg, #fff7ed 0%, #f8fafc 270px, #eef6ff 100%);
  color: var(--ink);
}
.app-hero {
  position: relative;
  overflow: hidden;
  padding: 24px 26px 18px;
  max-width: 1480px;
  margin: 8px auto 16px;
  border: 1px solid rgba(255,255,255,0.75);
  border-radius: 22px;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,247,237,0.78)),
    radial-gradient(circle at 94% 18%, rgba(56,189,248,0.26), transparent 28%);
  box-shadow: var(--shadow-lg);
  backdrop-filter: blur(8px);
}
.app-hero::after {
  content: none;
}
.app-hero-top {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 18px;
}
.app-hero-copy {
  min-width: 0;
}
.app-preferences {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  flex: none;
}
.app-pref-btn {
  appearance: none;
  min-height: 36px;
  border: 1px solid rgba(226,232,240,0.92);
  border-radius: 999px;
  background: rgba(255,255,255,0.88);
  color: #334155;
  padding: 0 13px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 900;
  box-shadow: 0 8px 18px rgba(15,23,42,0.06);
  transition: transform 0.16s ease, background 0.16s ease, color 0.16s ease, border-color 0.16s ease;
}
.app-pref-btn:hover {
  transform: translateY(-1px);
  border-color: rgba(37,99,235,0.32);
  background: #eff6ff;
  color: #1d4ed8;
}
.app-hero h1 {
  position: relative;
  z-index: 1;
  margin: 0 0 6px;
  font-size: 34px;
  line-height: 1.2;
  letter-spacing: 0;
  color: #172033;
}
.app-hero p {
  position: relative;
  z-index: 1;
  margin: 0;
  color: var(--muted);
  font-size: 15px;
}
.section-note {
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,250,245,0.92));
  border: 1px solid rgba(254, 215, 170, 0.95);
  border-left: 6px solid var(--orange);
  border-radius: 16px;
  padding: 14px 16px;
  margin-bottom: 14px;
  box-shadow: var(--shadow);
}
.section-note::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 46%;
  background: linear-gradient(90deg, rgba(249,115,22,0.08), transparent);
  pointer-events: none;
}
.section-note b {
  color: #9a3412;
}
.dental-page-nav {
  position: sticky;
  top: 0;
  z-index: 9000;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  max-width: 1480px;
  margin: 0 auto 16px;
  padding: 10px;
  border: 1px solid rgba(255,255,255,0.82);
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(255,255,255,0.96), rgba(239,246,255,0.92));
  box-shadow: var(--shadow);
  backdrop-filter: blur(10px);
}
.dental-page-nav-title {
  padding: 0 8px;
  color: #475569;
  font-size: 13px;
  font-weight: 800;
}
.dental-page-nav-item {
  appearance: none;
  border: 1px solid rgba(226,232,240,0.95);
  border-radius: 999px;
  background: rgba(255,255,255,0.9);
  color: #334155;
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  box-shadow: 0 5px 14px rgba(15,23,42,0.05);
  transition: transform 0.16s ease, background 0.16s ease, color 0.16s ease, box-shadow 0.16s ease;
}
.dental-page-nav-item:hover {
  transform: translateY(-1px);
  background: #eff6ff;
  color: var(--blue);
  box-shadow: 0 9px 20px rgba(15,23,42,0.10);
}
.dental-page-nav-item.active {
  border-color: transparent;
  background: linear-gradient(135deg, var(--orange), var(--blue));
  color: #ffffff;
  box-shadow: 0 10px 24px rgba(37, 99, 235, 0.23);
}
body[data-dental-theme="dark"] .gradio-container {
  background:
    radial-gradient(circle at 12% 0%, rgba(14,165,233,0.16), transparent 30%),
    radial-gradient(circle at 88% 8%, rgba(249,115,22,0.13), transparent 32%),
    linear-gradient(180deg, #0f172a 0%, #111827 320px, #020617 100%) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .app-hero,
body[data-dental-theme="dark"] .dental-page,
body[data-dental-theme="dark"] .dental-page-nav,
body[data-dental-theme="dark"] .section-note,
body[data-dental-theme="dark"] .gradio-container .block,
body[data-dental-theme="dark"] .gradio-container .form,
body[data-dental-theme="dark"] .gradio-container .panel,
body[data-dental-theme="dark"] .gradio-container .accordion {
  background: linear-gradient(180deg, rgba(15,23,42,0.94), rgba(17,24,39,0.88)) !important;
  border-color: rgba(71,85,105,0.78) !important;
  color: #e5e7eb !important;
  box-shadow: 0 18px 42px rgba(0,0,0,0.28) !important;
}
body[data-dental-theme="dark"] .app-hero h1,
body[data-dental-theme="dark"] .app-hero p,
body[data-dental-theme="dark"] .gradio-container h1,
body[data-dental-theme="dark"] .gradio-container h2,
body[data-dental-theme="dark"] .gradio-container h3,
body[data-dental-theme="dark"] .gradio-container label,
body[data-dental-theme="dark"] .gradio-container .prose,
body[data-dental-theme="dark"] .gradio-container .markdown,
body[data-dental-theme="dark"] .gradio-container [data-testid="markdown"] {
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .dental-page-nav-item,
body[data-dental-theme="dark"] .app-pref-btn,
body[data-dental-theme="dark"] .gradio-container input,
body[data-dental-theme="dark"] .gradio-container textarea,
body[data-dental-theme="dark"] .gradio-container select {
  background: rgba(15,23,42,0.9) !important;
  border-color: rgba(71,85,105,0.82) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .dental-page-nav-item:hover,
body[data-dental-theme="dark"] .app-pref-btn:hover {
  background: rgba(30,41,59,0.96) !important;
  color: #93c5fd !important;
}
body[data-dental-theme="dark"] .result-card,
body[data-dental-theme="dark"] .metric-card,
body[data-dental-theme="dark"] .knowledge-card,
body[data-dental-theme="dark"] .quality-card,
body[data-dental-theme="dark"] .report-preview-panel,
body[data-dental-theme="dark"] .batch-knowledge-content,
body[data-dental-theme="dark"] .det-explain {
  background: linear-gradient(180deg, rgba(15,23,42,0.96), rgba(30,41,59,0.86)) !important;
  border-color: rgba(71,85,105,0.76) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .native-ai-assistant {
  background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(17,24,39,0.96)) !important;
  border-color: rgba(71,85,105,0.78) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .native-ai-top,
body[data-dental-theme="dark"] .native-ai-messages,
body[data-dental-theme="dark"] .native-ai-composer,
body[data-dental-theme="dark"] .native-ai-empty-card,
body[data-dental-theme="dark"] .native-ai-msg.assistant .native-ai-bubble {
  background: linear-gradient(180deg, rgba(15,23,42,0.94), rgba(30,41,59,0.86)) !important;
  border-color: rgba(71,85,105,0.76) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .native-ai-subtitle,
body[data-dental-theme="dark"] .native-ai-empty-card p,
body[data-dental-theme="dark"] .native-ai-md,
body[data-dental-theme="dark"] .native-ai-suggestion-title {
  color: #cbd5e1 !important;
}
body[data-dental-theme="dark"] .native-ai-assistant button.native-ai-suggestion,
body[data-dental-theme="dark"] .native-ai-export-btn,
body[data-dental-theme="dark"] #ask-ai-input textarea {
  background: rgba(15,23,42,0.9) !important;
  border-color: rgba(71,85,105,0.82) !important;
  color: #e5e7eb !important;
}
.dental-page {
  display: none !important;
}
.dental-page {
  border-radius: 24px;
  background: rgba(255,255,255,0.58);
  border: 1px solid rgba(255,255,255,0.70);
  padding: 12px;
  box-shadow: 0 10px 30px rgba(15,23,42,0.04);
  max-width: 1480px;
  margin: 0 auto;
}
#page-image,
#page-compare,
#page-batch {
  background:
    radial-gradient(circle at 8% 2%, rgba(56, 189, 248, 0.12), transparent 30%),
    radial-gradient(circle at 94% 8%, rgba(249, 115, 22, 0.10), transparent 34%),
    linear-gradient(180deg, rgba(255,255,255,0.86), rgba(255,251,247,0.74) 42%, rgba(239,246,255,0.70) 100%);
  border: 1px solid rgba(255,255,255,0.88);
  box-shadow: 0 18px 48px rgba(15,23,42,0.065);
}
#page-image .block,
#page-image .form,
#page-image .panel,
#page-image .accordion,
#page-compare .block,
#page-compare .form,
#page-compare .panel,
#page-compare .accordion,
#page-batch .block,
#page-batch .form,
#page-batch .panel,
#page-batch .accordion {
  background: rgba(255,255,255,0.94) !important;
  border-color: rgba(226,232,240,0.78) !important;
  box-shadow: 0 10px 28px rgba(15,23,42,0.045) !important;
}
#page-image .image-container,
#page-image .file-preview,
#page-image .upload-container,
#page-compare .image-container,
#page-compare .file-preview,
#page-compare .upload-container,
#page-batch .image-container,
#page-batch .file-preview,
#page-batch .upload-container {
  background: linear-gradient(180deg, #ffffff, #f8fbff) !important;
  border: 1px solid rgba(226,232,240,0.78) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 8px 22px rgba(15,23,42,0.04) !important;
}
#page-image table,
#page-compare table,
#page-batch table {
  background: #ffffff !important;
  border-color: rgba(226,232,240,0.72) !important;
}
#page-image table thead th,
#page-compare table thead th,
#page-batch table thead th {
  background: linear-gradient(180deg, #ffffff, #f8fbff) !important;
  color: #1e293b !important;
  border-color: rgba(226,232,240,0.72) !important;
}
#page-image table tbody tr:nth-child(even),
#page-compare table tbody tr:nth-child(even),
#page-batch table tbody tr:nth-child(even) {
  background: rgba(248,250,252,0.46) !important;
}
#page-image .markdown,
#page-compare .markdown,
#page-batch .markdown {
  color: #243044;
}
body:not([data-dental-page]) #page-learn,
body[data-dental-page="learn"] #page-learn,
body[data-dental-page="dashboard"] #page-dashboard,
body[data-dental-page="image"] #page-image,
body[data-dental-page="compare"] #page-compare,
body[data-dental-page="batch"] #page-batch,
body[data-dental-page="history"] #page-history,
body[data-dental-page="assistant"] #page-assistant,
body[data-dental-page="report"] #page-report {
  display: block !important;
}
.detection-empty-state {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  min-height: 162px;
  max-height: 220px;
  margin: 8px 0 12px;
  padding: 20px 22px;
  border: 1px solid rgba(226, 232, 240, 0.86);
  border-radius: 18px;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.98), rgba(239,246,255,0.88)),
    linear-gradient(90deg, rgba(249,115,22,0.07), rgba(56,189,248,0.08));
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.055);
}
.detection-empty-icon {
  flex: 0 0 52px;
  width: 52px;
  height: 52px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
  background: linear-gradient(135deg, #fff7ed, #eff6ff);
  border: 1px solid rgba(254, 215, 170, 0.86);
  color: var(--blue);
}
.detection-empty-icon svg {
  width: 34px;
  height: 34px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.3;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.detection-empty-copy {
  max-width: 820px;
  min-width: 0;
}
.detection-empty-title {
  margin: 0 0 6px;
  color: #0f172a;
  font-size: 22px;
  line-height: 1.25;
  font-weight: 900;
  letter-spacing: 0;
}
.detection-empty-desc {
  color: #475569;
  font-size: 14px;
  line-height: 1.65;
}
.detection-empty-hint {
  display: inline-flex;
  margin-top: 8px;
  padding: 5px 10px;
  border-radius: 999px;
  background: rgba(255, 247, 237, 0.86);
  border: 1px solid rgba(254, 215, 170, 0.82);
  color: #9a3412;
  font-size: 12px;
  font-weight: 800;
  line-height: 1.35;
}
.detection-empty-compare .detection-empty-icon {
  color: #0f766e;
  background: linear-gradient(135deg, #ecfeff, #f8fafc);
  border-color: rgba(125, 211, 252, 0.72);
}
.detection-empty-batch .detection-empty-icon {
  color: #7c3aed;
  background: linear-gradient(135deg, #f5f3ff, #fff7ed);
  border-color: rgba(196, 181, 253, 0.72);
}
.detection-progress-state {
  position: sticky;
  top: 10px;
  z-index: 20;
  margin: 8px 0 12px;
  padding: 14px 16px;
  border: 1px solid rgba(191, 219, 254, 0.92);
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(239,246,255,0.92));
  box-shadow: 0 10px 24px rgba(37, 99, 235, 0.08);
}
.detection-progress-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  color: #0f172a;
  font-size: 14px;
  font-weight: 900;
  line-height: 1.35;
}
.detection-progress-head b {
  color: #1d4ed8;
  font-size: 13px;
}
.detection-progress-track {
  height: 9px;
  margin: 10px 0 8px;
  overflow: hidden;
  border-radius: 999px;
  background: rgba(226, 232, 240, 0.92);
  box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.08);
}
.detection-progress-fill {
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, var(--orange), var(--blue));
  transition: width 0.28s ease;
}
.detection-progress-detail {
  color: #64748b;
  font-size: 12px;
  line-height: 1.5;
}
.dental-image-loupe {
  position: fixed;
  left: 0;
  top: 0;
  width: 190px;
  height: 190px;
  display: none;
  border-radius: 22px;
  border: 1px solid rgba(191, 219, 254, 0.95);
  background-repeat: no-repeat;
  background-color: rgba(255, 255, 255, 0.96);
  box-shadow: 0 22px 48px rgba(15, 23, 42, 0.22);
  pointer-events: none;
  z-index: 10020;
  overflow: hidden;
}
.dental-image-loupe.visible {
  display: block;
}
.dental-batch-fullscreen-btn {
  position: fixed;
  display: none;
  align-items: center;
  justify-content: center;
  min-width: 34px;
  height: 34px;
  border-radius: 999px;
  border: 1px solid rgba(191,219,254,0.9);
  background: rgba(15,23,42,0.78);
  color: #ffffff;
  cursor: pointer;
  font-size: 15px;
  font-weight: 900;
  line-height: 1;
  box-shadow: 0 12px 26px rgba(15,23,42,0.24);
  backdrop-filter: blur(10px);
  z-index: 10022;
  transition: transform 0.16s ease, background 0.16s ease;
}
.dental-batch-fullscreen-btn.visible {
  display: inline-flex;
}
.dental-batch-fullscreen-btn:hover {
  transform: translateY(-1px) scale(1.03);
  background: rgba(37,99,235,0.88);
}
.dental-image-fullscreen-layer {
  position: fixed;
  inset: 0;
  display: none;
  place-items: center;
  padding: 38px;
  background: rgba(2,6,23,0.86);
  backdrop-filter: blur(12px);
  z-index: 10040;
}
.dental-image-fullscreen-layer.visible {
  display: grid;
}
.dental-image-fullscreen-layer img {
  max-width: min(96vw, 1480px);
  max-height: 90vh;
  object-fit: contain;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 28px 76px rgba(0,0,0,0.42);
}
.dental-image-fullscreen-close {
  position: fixed;
  right: 24px;
  top: 22px;
  width: 42px;
  height: 42px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.24);
  background: rgba(15,23,42,0.72);
  color: #ffffff;
  cursor: pointer;
  font-size: 24px;
  line-height: 1;
  box-shadow: 0 14px 30px rgba(0,0,0,0.28);
}
#page-batch .batch-work-row {
  align-items: flex-start !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-batch .batch-work-row > * {
  min-height: 0;
  align-self: flex-start !important;
}
#page-batch .batch-empty-state-panel {
  display: flex !important;
  flex-direction: column !important;
}
#page-batch .batch-empty-state-panel,
#page-batch .batch-empty-state-panel > *,
#page-batch .batch-empty-state-panel .html-container {
  flex: 0 0 auto !important;
  height: auto !important;
  min-height: 0 !important;
}
#page-batch .batch-empty-state-panel .detection-empty-state {
  min-height: 210px;
  max-height: none;
  margin: 8px 0 0;
  padding: 28px 30px;
}
#page-batch .batch-empty-state-panel .detection-empty-copy {
  flex: 0 1 auto;
  max-width: none;
  width: 100%;
}
#page-batch .batch-empty-state-panel .detection-empty-desc {
  max-width: 100%;
}
.metric-grid {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 12px;
  margin: 10px 0 16px;
}
.metric-card {
  position: relative;
  overflow: hidden;
  background: linear-gradient(160deg, #ffffff, #f8fbff);
  border: 1px solid rgba(226, 232, 240, 0.95);
  border-radius: 16px;
  padding: 14px;
  box-shadow: var(--shadow);
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}
.metric-card::after {
  content: none;
}
.metric-card:hover {
  transform: translateY(-3px);
  border-color: rgba(249, 115, 22, 0.42);
  box-shadow: var(--shadow-lg);
}
.metric-label {
  color: var(--muted);
  font-size: 13px;
}
.metric-value {
  margin-top: 6px;
  font-size: 24px;
  font-weight: 700;
  color: var(--orange-dark);
}
.metric-sub {
  margin-top: 4px;
  color: var(--muted);
  font-size: 12px;
}
.result-cards {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 10px;
  margin: 8px 0 12px;
}
.result-card {
  background: linear-gradient(180deg, #ffffff, #f8fafc);
  border: 1px solid rgba(226, 232, 240, 0.9);
  border-radius: 14px;
  padding: 12px;
  min-height: 78px;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.055);
}
.result-card b {
  display: block;
  color: var(--muted);
  font-size: 12px;
  font-weight: 500;
}
.result-card span {
  display: block;
  margin-top: 6px;
  font-size: 18px;
  font-weight: 700;
  color: var(--ink);
}
.model-tag {
  background: linear-gradient(135deg, #fff7ed, #eff6ff);
  border: 1px solid #fed7aa;
  border-radius: 999px;
  padding: 8px 12px;
  color: #9a3412;
  font-weight: 600;
  margin-bottom: 8px;
  display: inline-flex;
  box-shadow: 0 6px 16px rgba(249, 115, 22, 0.10);
}
.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin: 10px 0 14px;
}
.knowledge-card {
  background: linear-gradient(180deg, #ffffff, #f8fbff);
  border: 1px solid rgba(226, 232, 240, 0.95);
  border-radius: 16px;
  padding: 14px;
  box-shadow: var(--shadow);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.knowledge-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.knowledge-card b {
  display: block;
  color: var(--orange-dark);
  font-size: 15px;
  margin-bottom: 6px;
}
.knowledge-card span {
  display: inline-block;
  color: var(--muted);
  font-size: 12px;
  margin-bottom: 8px;
}
.knowledge-card p {
  margin: 6px 0;
  color: var(--ink);
  font-size: 13px;
  line-height: 1.55;
}
.quality-grid, .fusion-legend {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin: 8px 0 12px;
}
.quality-card {
  background: linear-gradient(180deg, #ffffff, #f8fafc);
  border: 1px solid rgba(226, 232, 240, 0.95);
  border-radius: 14px;
  padding: 12px;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
}
.quality-card b { display: block; color: var(--muted); font-size: 12px; }
.quality-card span { display: block; margin-top: 5px; font-weight: 700; }
.quality-ok { color: #15803d; }
.quality-warn { color: #b45309; }
.quality-bad { color: #b91c1c; }
.fusion-legend { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.legend-high, .legend-low { border-radius: 8px; padding: 9px 11px; font-size: 13px; }
.legend-high { background: linear-gradient(135deg, #ecfdf5, #f0fdf4); border: 1px solid #86efac; color: #166534; }
.legend-low { background: linear-gradient(135deg, #fff1f2, #fff7ed); border: 1px solid #fda4af; color: #9f1239; }
.det-input-row, .det-result-row {
  align-items: stretch !important;
}
.det-input-row,
.det-result-row,
.compare-threshold-row,
.compare-model-row,
.compare-fusion-row,
.batch-work-row,
.batch-output-row,
.batch-download-row,
.linked-region-row,
.dashboard-actions-row,
.dashboard-chart-row,
.history-action-row,
.history-filter-row,
.history-detail-row,
.report-controls-row,
.report-download-row {
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid rgba(226,232,240,0.70) !important;
  border-radius: 22px !important;
  padding: 12px !important;
  gap: 12px !important;
  margin: 0 0 14px !important;
  box-shadow: 0 14px 34px rgba(15,23,42,0.055) !important;
}
#page-image .det-input-row > *,
#page-image .det-result-row > *,
#page-compare .compare-threshold-row > *,
#page-compare .compare-model-row > *,
#page-compare .compare-fusion-row > *,
#page-batch .batch-work-row > *,
#page-batch .batch-output-row > *,
#page-batch .batch-download-row > *,
#page-image .linked-region-row > *,
#page-compare .linked-region-row > *,
#page-batch .linked-region-row > *,
#page-dashboard .dashboard-actions-row > *,
#page-dashboard .dashboard-chart-row > *,
#page-history .history-action-row > *,
#page-history .history-filter-row > *,
#page-history .history-detail-row > *,
#page-report .report-controls-row > *,
#page-report .report-download-row > * {
  background: transparent !important;
  min-width: 0 !important;
}
#page-dashboard .dashboard-actions-row,
#page-history .history-action-row,
#page-report .report-controls-row {
  align-items: end !important;
}
#page-dashboard .dashboard-actions-row button,
#page-history .history-action-row button,
#page-report .report-controls-row button {
  min-height: 44px !important;
}
.solid-primary-action,
.solid-primary-action > *,
.solid-primary-action button,
.solid-primary-action .wrap {
  background: transparent !important;
  box-shadow: none !important;
}
.solid-primary-action button,
button.solid-primary-action {
  width: 100% !important;
  min-height: 44px !important;
  border: 0 !important;
  background: linear-gradient(135deg, var(--orange), var(--blue)) !important;
  color: #ffffff !important;
  box-shadow: 0 12px 26px rgba(37, 99, 235, 0.18) !important;
}
#page-report .report-controls-row > *:first-child {
  flex: 1 1 420px !important;
}
#page-report .report-controls-row > *:last-child {
  flex: 0 0 220px !important;
}
#page-dashboard .dashboard-chart-row {
  align-items: stretch !important;
}
#page-report .report-download-row {
  align-items: stretch !important;
}
#page-report .report-download-row .block,
#page-report .report-download-row .file-preview,
#page-report .report-download-row .upload-container {
  min-height: 96px !important;
  max-height: 128px !important;
}
#page-report .report-download-row .file-preview,
#page-report .report-download-row .upload-container {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.report-preview-panel {
  margin: 0 0 12px !important;
  padding: 14px 16px !important;
  border: 1px solid rgba(226,232,240,0.82) !important;
  border-radius: 16px !important;
  background: rgba(255,255,255,0.94) !important;
  box-shadow: 0 10px 24px rgba(15,23,42,0.045) !important;
}
#page-image .det-input-row .markdown h3,
#page-image .det-result-row .markdown h3,
#page-compare .markdown h3,
#page-batch .markdown h3 {
  margin-top: 0 !important;
  margin-bottom: 8px !important;
  font-size: 18px !important;
  line-height: 1.35 !important;
  letter-spacing: 0 !important;
}
.compare-model-row .model-tag {
  justify-content: center;
  width: 100%;
  white-space: normal;
  text-align: center;
}
#page-compare .det-upload .image-container,
#page-compare .det-upload .upload-container {
  min-height: 0 !important;
}
#page-image .wrap,
#page-image .contain,
#page-image .padded,
#page-compare .wrap,
#page-compare .contain,
#page-compare .padded,
#page-batch .wrap,
#page-batch .contain,
#page-batch .padded {
  background-color: transparent !important;
}
#page-image .block:not(.det-explain),
#page-compare .block,
#page-batch .block {
  background: rgba(255,255,255,0.96) !important;
}
.det-explain {
  max-height: 390px;
  overflow-y: auto;
  padding-right: 8px;
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid rgba(226,232,240,0.88) !important;
  border-radius: 18px !important;
  padding: 16px 18px !important;
  line-height: 1.75 !important;
  box-shadow: 0 10px 28px rgba(15,23,42,0.06) !important;
}
.batch-knowledge-panel {
  margin-top: 12px !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 0 !important;
  padding: 0 !important;
  box-shadow: none !important;
  overflow: visible !important;
}
.batch-knowledge-content {
  min-height: 0 !important;
  height: auto !important;
  max-height: min(620px, 70vh) !important;
  flex: none !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid rgba(226,232,240,0.88) !important;
  border-radius: 18px !important;
  padding: 14px !important;
  box-shadow: 0 10px 28px rgba(15,23,42,0.06) !important;
  scrollbar-gutter: stable;
}
.batch-knowledge-placeholder {
  display: none !important;
}
.batch-knowledge-panel .knowledge-grid {
  grid-template-columns: 1fr !important;
  gap: 10px !important;
  margin: 0 !important;
}
.batch-knowledge-panel .knowledge-card {
  box-shadow: 0 8px 20px rgba(15,23,42,0.045) !important;
}
.batch-knowledge-panel .section-note {
  margin: 10px 0 0 !important;
  box-shadow: none !important;
}
.batch-work-row .det-explain {
  min-height: 0 !important;
  height: auto !important;
  max-height: min(620px, 70vh) !important;
  flex: none !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  scrollbar-gutter: stable;
}
#batch-result-preview-gallery {
  margin-bottom: 10px !important;
}
#batch-result-preview-gallery img {
  cursor: zoom-in;
}
.batch-work-row .det-explain > *,
.batch-work-row .det-explain .prose,
.batch-work-row .det-explain .markdown,
.batch-work-row .det-explain .md,
.batch-work-row .det-explain [data-testid="markdown"],
.batch-knowledge-panel .prose,
.batch-knowledge-panel .markdown,
.batch-knowledge-panel .html-container {
  max-height: none !important;
  height: auto !important;
  overflow: visible !important;
}
#page-batch .batch-knowledge-panel .batch-knowledge-content {
  max-height: min(620px, 70vh) !important;
  height: auto !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) {
  align-items: flex-start !important;
  height: auto !important;
  min-height: 0 !important;
  overflow: visible !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-left-column,
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-right-column {
  height: auto !important;
  max-height: none !important;
  min-height: 0 !important;
  align-self: flex-start !important;
  display: block !important;
  overflow: visible !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-left-column .batch-knowledge-panel,
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-right-column .det-explain {
  display: block !important;
  min-height: 0 !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-knowledge-panel {
  display: block !important;
  overflow: visible !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-knowledge-panel .html-container {
  height: auto !important;
  max-height: none !important;
  min-height: 0 !important;
  overflow: visible !important;
  display: block !important;
}
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-knowledge-content,
#page-batch .batch-work-row:has(.batch-knowledge-content) .batch-right-column .det-explain {
  display: block !important;
  height: auto !important;
  max-height: min(620px, 70vh) !important;
  min-height: 0 !important;
  flex: none !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}
#page-batch .batch-left-column .accordion,
#page-batch .batch-left-column .accordion > *,
#page-batch .batch-left-column .accordion .wrap,
#page-batch .batch-left-column .accordion .form {
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  overflow: visible !important;
}
#page-batch .batch-left-column .block:not(.batch-knowledge-panel),
#page-batch .batch-right-column .block:not(.det-explain):not(#batch-result-preview-gallery) {
  height: auto !important;
  min-height: 0 !important;
  flex: none !important;
  overflow: visible !important;
}
.batch-knowledge-title {
  margin: 0 0 12px;
  color: #0f172a;
  font-weight: 900;
  line-height: 1.45;
}
.det-upload .image-container, .det-output .image-container {
  min-height: 0 !important;
}
.task-status {
  margin: 4px 0 10px;
}
.dashboard-detail-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin: 12px 0 16px;
}
.dashboard-detail-card {
  min-height: 170px;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
  border: 1px solid rgba(226,232,240,0.95);
  border-top: 4px solid transparent;
  border-image: linear-gradient(90deg, var(--orange), var(--sky), var(--violet)) 1;
  border-radius: 16px;
  padding: 14px 16px;
  box-shadow: var(--shadow);
}
.dashboard-detail-card h3 {
  margin: 0 0 9px;
  font-size: 16px;
  color: var(--ink);
}
.dashboard-detail-card ul {
  margin: 0;
  padding-left: 18px;
}
.dashboard-detail-card li {
  margin: 6px 0;
  line-height: 1.5;
  color: var(--ink);
}
.dashboard-detail-card .empty { color: var(--muted); }
.gradio-container .block,
.gradio-container .form,
.gradio-container .panel {
  border-color: rgba(226, 232, 240, 0.92) !important;
  border-radius: 16px !important;
  background: rgba(255,255,255,0.92) !important;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.045);
}
.gradio-container input,
.gradio-container textarea,
.gradio-container select {
  border-radius: 12px !important;
}
.gradio-container label,
.gradio-container .label-wrap {
  color: #334155 !important;
  font-weight: 700 !important;
}
.education-shell {
  display: grid;
  gap: 16px;
}
.education-hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.18fr) minmax(320px, 0.82fr);
  gap: 18px;
  align-items: stretch;
  padding: 22px;
  margin-bottom: 0;
  overflow: hidden;
  border: 1px solid rgba(191, 219, 254, 0.82);
  border-radius: 28px;
  background:
    linear-gradient(120deg, rgba(255,255,255,0.98), rgba(239,246,255,0.86) 48%, rgba(240,253,250,0.72)),
    repeating-linear-gradient(90deg, rgba(148,163,184,0.08) 0, rgba(148,163,184,0.08) 1px, transparent 1px, transparent 36px);
  box-shadow: 0 24px 58px rgba(15, 23, 42, 0.075);
}
.education-panel {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-width: 0;
  padding: 2px 4px;
  background: transparent;
  border: 0;
  border-radius: 0;
  box-shadow: none;
}
.education-eyebrow {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  gap: 8px;
  margin-bottom: 10px;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(14, 165, 233, 0.22);
  background: rgba(240, 249, 255, 0.84);
  color: #0369a1;
  font-size: 12px;
  font-weight: 800;
}
.education-eyebrow::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 999px;
  background: #14b8a6;
  box-shadow: 0 0 0 4px rgba(20, 184, 166, 0.14);
}
.education-panel h2 {
  margin: 0;
  max-width: 760px;
  color: #0f172a;
  font-size: clamp(30px, 4vw, 48px);
  line-height: 1.08;
  letter-spacing: 0;
}
.education-lead {
  max-width: 780px;
  margin: 14px 0 0;
  color: #334155;
  font-size: 16px;
  line-height: 1.8;
}
.education-metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin-top: 18px;
}
.education-metric {
  min-width: 0;
  padding: 12px;
  border: 1px solid rgba(226, 232, 240, 0.82);
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.72);
}
.education-metric b {
  display: block;
  color: #0f766e;
  font-size: 22px;
  line-height: 1.1;
}
.education-metric span {
  display: block;
  margin-top: 5px;
  color: #64748b;
  font-size: 12px;
  line-height: 1.35;
}
.education-insight-panel,
.education-tip {
  border: 1px solid rgba(226, 232, 240, 0.86);
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.86);
  box-shadow: 0 16px 38px rgba(15, 23, 42, 0.065);
}
.education-insight-panel {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 14px;
  padding: 16px;
}
.education-insight-visual {
  min-height: 178px;
  border-radius: 18px;
  border: 1px solid rgba(191, 219, 254, 0.82);
  background: linear-gradient(145deg, #ffffff, #eff6ff 58%, #f0fdfa);
  overflow: hidden;
}
.education-insight-panel h3 {
  margin: 0;
  color: #0f172a;
  font-size: 18px;
}
.education-insight-list {
  display: grid;
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.education-insight-list li {
  display: flex;
  align-items: center;
  gap: 9px;
  color: #334155;
  font-size: 13px;
  line-height: 1.45;
}
.education-insight-list li::before {
  content: "";
  flex: 0 0 8px;
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: linear-gradient(135deg, var(--orange), var(--blue));
}
.education-review-strip {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}
.education-review-step {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 10px;
  align-items: start;
  padding: 14px;
  border: 1px solid rgba(226,232,240,0.9);
  border-radius: 18px;
  background: rgba(255,255,255,0.9);
  box-shadow: 0 10px 24px rgba(15,23,42,0.045);
}
.education-review-step b {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 12px;
  color: #1d4ed8;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  font-size: 13px;
}
.education-review-step span {
  display: block;
  color: #0f172a;
  font-weight: 800;
  line-height: 1.25;
}
.education-review-step small {
  display: block;
  margin-top: 4px;
  color: #64748b;
  line-height: 1.45;
}
.education-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(260px, 1fr));
  gap: 16px;
  align-items: stretch;
}
.education-card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 100%;
  padding: 16px;
  overflow: hidden;
  border: 1px solid rgba(226, 232, 240, 0.92);
  border-radius: 22px;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.94));
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.058);
}
.education-card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 4px;
  background: linear-gradient(90deg, var(--orange), var(--sky), var(--teal));
}
.education-card h3 {
  margin: 0;
  color: #0f172a;
  font-size: 19px;
  line-height: 1.25;
}
.education-card .subtitle {
  color: #64748b;
  font-size: 13px;
  line-height: 1.55;
}
.education-card-top {
  display: grid;
  grid-template-columns: 96px minmax(0, 1fr);
  gap: 12px;
  align-items: center;
}
.education-badge {
  display: inline-flex;
  width: fit-content;
  margin-bottom: 6px;
  padding: 4px 8px;
  border-radius: 999px;
  color: #9a3412;
  background: #fff7ed;
  border: 1px solid #fed7aa;
  font-size: 12px;
  font-weight: 800;
}
.education-visual {
  aspect-ratio: 1 / 1;
  min-height: 96px;
  border-radius: 18px;
  background:
    linear-gradient(145deg, #fff7ed, #eff6ff 58%, #f0fdfa);
  border: 1px solid rgba(254, 215, 170, 0.82);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.education-visual svg {
  width: 100%;
  height: 100%;
}
.education-card dl {
  margin: 0;
  display: grid;
  gap: 10px;
}
.education-card dl > div {
  padding: 10px;
  border: 1px solid rgba(226,232,240,0.76);
  border-radius: 14px;
  background: rgba(248,250,252,0.72);
}
.education-card dt {
  font-weight: 800;
  color: #0f766e;
  font-size: 13px;
}
.education-card dd {
  margin: 4px 0 0;
  color: #1e293b;
  line-height: 1.62;
  font-size: 13px;
}
.education-card-note {
  margin-top: auto;
  padding: 10px 12px;
  border-radius: 14px;
  border: 1px solid rgba(191, 219, 254, 0.88);
  background: #eff6ff;
  color: #1e3a8a;
  font-size: 12px;
  line-height: 1.5;
}
.education-footer-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}
.education-tip {
  padding: 16px;
  background: linear-gradient(180deg, #ffffff, #fff7ed);
}
.education-tip b {
  display: block;
  margin-bottom: 8px;
  color: #9a3412;
  font-size: 15px;
}
.education-tip p,
.education-tip li {
  color: #334155;
  line-height: 1.65;
}
.education-tip ul {
  margin: 0;
  padding-left: 18px;
}
#ask-ai-floating-button {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 9999;
  width: 82px;
  height: 82px;
  border-radius: 999px;
  border: 3px solid rgba(255,255,255,0.95);
  background: radial-gradient(circle at 30% 20%, #ecfeff 0%, #38bdf8 32%, #2563eb 68%, #1e1b4b 100%);
  color: #ffffff;
  box-shadow: 0 18px 42px rgba(37, 99, 235, 0.38);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1px;
  font-weight: 800;
  cursor: pointer;
  transition: transform 0.18s ease, box-shadow 0.18s ease, outline 0.18s ease;
}
#ask-ai-floating-button svg { width: 43px; height: 43px; filter: drop-shadow(0 3px 7px rgba(15,23,42,0.25)); }
#ask-ai-floating-button .robot-label { font-size: 11px; line-height: 1; letter-spacing: 0; }
#ask-ai-floating-button:hover, #ask-ai-floating-button.drag-over {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 22px 52px rgba(37, 99, 235, 0.48);
  outline: 5px solid rgba(56, 189, 248, 0.25);
}
body[data-dental-page="assistant"] #ask-ai-floating-button {
  display: none !important;
}
#ask-ai-selection-popover {
  position: absolute;
  z-index: 10000;
  display: none;
  border: 1px solid #fed7aa;
  border-radius: 999px;
  background: #fff7ed;
  color: #9a3412;
  padding: 8px 13px;
  font-size: 13px;
  font-weight: 800;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
  cursor: pointer;
}
#ask-ai-selection-popover.visible { display: block; }
#ask-ai-selection-popover::after { content: " → 拖高亮文字到右下角也可提问"; color: #64748b; font-weight: 600; }
.ai-thinking {
  display: inline-flex;
  flex-direction: column;
  gap: 5px;
  padding: 8px 10px;
  border: 1px solid #dbeafe;
  border-radius: 12px;
  background: linear-gradient(135deg, #eff6ff 0%, #fff7ed 100%);
  color: #334155;
  font-size: 13px;
  line-height: 1.45;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
}
.ai-thinking-main {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-weight: 700;
}
.ai-thinking-sub {
  color: #64748b;
  font-size: 12px;
}
.ai-thinking-dots {
  display: inline-flex;
  gap: 3px;
  align-items: center;
}
.ai-thinking-dots span {
  width: 5px;
  height: 5px;
  border-radius: 999px;
  background: #2563eb;
  animation: ai-thinking-bounce 1s infinite ease-in-out;
}
.ai-thinking-dots span:nth-child(2) { animation-delay: 0.16s; }
.ai-thinking-dots span:nth-child(3) { animation-delay: 0.32s; }
@keyframes ai-thinking-bounce {
  0%, 80%, 100% { transform: translateY(0); opacity: 0.45; }
  40% { transform: translateY(-4px); opacity: 1; }
}
.chat-input-row {
  align-items: end !important;
  gap: 10px !important;
  margin-top: 8px;
}
.chat-input-row button {
  min-height: 44px !important;
}
.followup-question,
.followup-question button {
  min-height: 56px !important;
  border-radius: 18px !important;
  border: 1px solid rgba(226,232,240,0.82) !important;
  background: linear-gradient(180deg, #ffffff, #fff7ed) !important;
  color: #0f172a !important;
  box-shadow: 0 10px 24px rgba(15,23,42,0.06) !important;
  font-weight: 800 !important;
  line-height: 1.35 !important;
  white-space: normal !important;
}
.followup-question:hover,
.followup-question button:hover {
  border-color: rgba(249,115,22,0.45) !important;
  background: linear-gradient(135deg, #fff7ed, #eff6ff) !important;
  color: #1d4ed8 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 14px 30px rgba(37,99,235,0.12) !important;
}
.feedback-inline {
  align-items: end !important;
  gap: 10px !important;
  padding: 0;
  border: 0;
  border-radius: 16px;
  background: transparent;
  box-shadow: none;
  min-height: 0 !important;
}
#chat-feedback-panel {
  display: none !important;
}
body.dental-show-feedback-reason #chat-feedback-panel {
  display: flex !important;
  padding: 10px 12px;
  border: 1px solid rgba(226, 232, 240, 0.72);
  background: rgba(255,255,255,0.74);
  box-shadow: 0 8px 20px rgba(15,23,42,0.04);
}
#chat-feedback-reason,
#chat-feedback-notice {
  min-width: 220px !important;
}
.gradio-container button.primary, .gradio-container button[variant="primary"] {
  background: linear-gradient(135deg, var(--orange), var(--blue)) !important;
  border-color: transparent !important;
  color: #ffffff !important;
  box-shadow: 0 12px 26px rgba(249, 115, 22, 0.24) !important;
}
.gradio-container button {
  border-radius: 12px !important;
  font-weight: 700 !important;
  transition: transform 0.16s ease, box-shadow 0.16s ease, background 0.16s ease !important;
}
.gradio-container button:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(15, 23, 42, 0.10) !important;
}
.gradio-container .dataframe,
.gradio-container table {
  border-radius: 14px !important;
  overflow: hidden !important;
}
.gradio-container .image-container,
.gradio-container .file-preview,
.gradio-container .upload-container {
  border-radius: 16px !important;
}
.gradio-container .chatbot,
.gradio-container [data-testid="chatbot"] {
  border-radius: 18px !important;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96)) !important;
  box-shadow: var(--shadow) !important;
}
#dental-chatbot {
  border: 1px solid rgba(226,232,240,0.88) !important;
}
#dental-chatbot .message-row {
  margin: 10px 0 !important;
}
#dental-chatbot .message-row.bot-row .message,
#dental-chatbot .message-row.assistant-row .message {
  background: #ffffff !important;
  border: 1px solid rgba(226,232,240,0.9) !important;
  border-radius: 18px !important;
  box-shadow: 0 10px 28px rgba(15,23,42,0.06) !important;
  color: #111827 !important;
}
#dental-chatbot .message-row.user-row .message {
  background: linear-gradient(135deg, #2563eb, #7c3aed) !important;
  color: #ffffff !important;
  border-radius: 18px !important;
}
#dental-chatbot .message-content {
  line-height: 1.75 !important;
  font-size: 15px !important;
}
.chat-thinking-time {
  margin: 0 0 8px;
  color: #94a3b8;
  font-size: 12px;
  line-height: 1.4;
}
#dental-chatbot .message-content h1,
#dental-chatbot .message-content h2,
#dental-chatbot .message-content h3 {
  margin: 12px 0 8px !important;
  font-weight: 800 !important;
  color: #0f172a !important;
}
#dental-chatbot .message-content p {
  margin: 8px 0 !important;
}
#dental-chatbot .message-content ul,
#dental-chatbot .message-content ol {
  margin: 8px 0 10px !important;
  padding-left: 1.35em !important;
}
#dental-chatbot .thought-group {
  margin: 0 0 8px !important;
  border: 0 !important;
  background: transparent !important;
  color: #94a3b8 !important;
  font-size: 12px !important;
}
#dental-chatbot .thought-group .title {
  padding: 0 !important;
  cursor: default !important;
  color: #94a3b8 !important;
}
#dental-chatbot .thought-group .arrow {
  display: none !important;
}
#dental-chatbot .message-buttons {
  display: none !important;
}
.chat-action-row {
  display: flex !important;
  gap: 8px !important;
  align-items: center !important;
  justify-content: flex-start !important;
  margin: 8px 0 4px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#chat-action-row:has(#chat-copy-btn button:disabled):has(#chat-like-btn button:disabled):has(#chat-dislike-btn button:disabled),
#chat-action-row:has(#chat-copy-btn button[aria-disabled="true"]):has(#chat-like-btn button[aria-disabled="true"]):has(#chat-dislike-btn button[aria-disabled="true"]) {
  display: none !important;
}
.chat-action-btn {
  flex: 0 0 auto !important;
  min-width: 40px !important;
}
.chat-action-btn button {
  min-height: 34px !important;
  height: 34px !important;
  min-width: 40px !important;
  width: 40px !important;
  padding: 7px !important;
  border-radius: 999px !important;
  border: 0 !important;
  background: transparent !important;
  color: #475569 !important;
  font-size: 0 !important;
  font-weight: 800 !important;
  line-height: 1 !important;
  box-shadow: none !important;
  white-space: nowrap !important;
}
.chat-action-btn button::before {
  content: "";
  display: block;
  width: 21px;
  height: 21px;
  margin: auto;
  background: currentColor;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  -webkit-mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center;
  mask-size: contain;
}
#chat-copy-btn button::before {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Crect%20width='14'%20height='14'%20x='8'%20y='8'%20rx='2'%20ry='2'/%3E%3Cpath%20d='M4%2016c-1.1%200-2-.9-2-2V4c0-1.1.9-2%202-2h10c1.1%200%202%20.9%202%202'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Crect%20width='14'%20height='14'%20x='8'%20y='8'%20rx='2'%20ry='2'/%3E%3Cpath%20d='M4%2016c-1.1%200-2-.9-2-2V4c0-1.1.9-2%202-2h10c1.1%200%202%20.9%202%202'/%3E%3C/svg%3E");
}
#chat-like-btn button::before {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Cpath%20d='M7%2010v12'/%3E%3Cpath%20d='M15%205.88%2014%2010h5.83a2%202%200%200%201%201.92%202.56l-2.33%208A2%202%200%200%201%2017.5%2022H4a2%202%200%200%201-2-2v-8a2%202%200%200%201%202-2h2.76a2%202%200%200%200%201.79-1.11L12%202h0a3.13%203.13%200%200%201%203%203.88Z'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Cpath%20d='M7%2010v12'/%3E%3Cpath%20d='M15%205.88%2014%2010h5.83a2%202%200%200%201%201.92%202.56l-2.33%208A2%202%200%200%201%2017.5%2022H4a2%202%200%200%201-2-2v-8a2%202%200%200%201%202-2h2.76a2%202%200%200%200%201.79-1.11L12%202h0a3.13%203.13%200%200%201%203%203.88Z'/%3E%3C/svg%3E");
}
#chat-dislike-btn button::before {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Cpath%20d='M17%2014V2'/%3E%3Cpath%20d='M9%2018.12%2010%2014H4.17a2%202%200%200%201-1.92-2.56l2.33-8A2%202%200%200%201%206.5%202H20a2%202%200%200%201%202%202v8a2%202%200%200%201-2%202h-2.76a2%202%200%200%200-1.79%201.11L12%2022h0a3.13%203.13%200%200%201-3-3.88Z'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%20fill='none'%20stroke='black'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'%3E%3Cpath%20d='M17%2014V2'/%3E%3Cpath%20d='M9%2018.12%2010%2014H4.17a2%202%200%200%201-1.92-2.56l2.33-8A2%202%200%200%201%206.5%202H20a2%202%200%200%201%202%202v8a2%202%200%200%201-2%202h-2.76a2%202%200%200%200-1.79%201.11L12%2022h0a3.13%203.13%200%200%201-3-3.88Z'/%3E%3C/svg%3E");
}
.chat-action-btn button:hover {
  background: rgba(241,245,249,0.96) !important;
  color: #1f2937 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 8px 18px rgba(15,23,42,0.08) !important;
}
.chat-action-btn button.primary,
.chat-action-btn button[variant="primary"] {
  background: #eff6ff !important;
  color: #2563eb !important;
  border-color: transparent !important;
}
#chat-copy-btn[data-copied="true"] button,
#chat-copy-btn button[data-copied="true"] {
  background: #ecfdf5 !important;
  color: #047857 !important;
  border-color: #a7f3d0 !important;
}
.chat-status-line {
  color: #64748b !important;
  font-size: 13px !important;
  line-height: 1.5 !important;
}
.chat-status-line p {
  margin: 4px 0 !important;
}
.feedback-hidden {
  display: none !important;
}
.gradio-container .prose {
  color: #243044;
}
.gradio-container .accordion {
  border-radius: 16px !important;
  border-color: rgba(226,232,240,0.9) !important;
  background: rgba(255,255,255,0.82) !important;
}
@media (max-width: 1100px) {
  .metric-grid, .result-cards, .knowledge-grid, .quality-grid, .dashboard-detail-grid, .education-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .education-hero { grid-template-columns: 1fr; }
  .education-review-strip { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .det-input-row,
  .det-result-row,
  .compare-model-row,
  .compare-fusion-row,
  .batch-work-row,
  .linked-region-row,
  .dashboard-actions-row,
  .dashboard-chart-row,
  .history-action-row,
  .history-filter-row,
  .history-detail-row,
  .report-controls-row,
  .report-download-row {
    flex-direction: column !important;
  }
  .det-input-row > *,
  .det-result-row > *,
  .compare-model-row > *,
  .compare-fusion-row > *,
  .batch-work-row > *,
  .linked-region-row > *,
  .dashboard-actions-row > *,
  .dashboard-chart-row > *,
  .history-action-row > *,
  .history-filter-row > *,
  .history-detail-row > *,
  .report-controls-row > *,
  .report-download-row > * {
    width: 100% !important;
    flex: 1 1 auto !important;
  }
}
@media (max-width: 720px) {
  #ask-ai-floating-button { right: 14px; bottom: 14px; width: 70px; height: 70px; }
  #ask-ai-floating-button svg { width: 36px; height: 36px; }
  #ask-ai-selection-popover::after { content: ""; }
  .knowledge-grid, .dashboard-detail-grid, .education-grid, .education-footer-grid { grid-template-columns: 1fr; }
  .education-hero { padding: 16px; border-radius: 20px; }
  .education-panel h2 { font-size: 30px; }
  .education-metrics,
  .education-review-strip { grid-template-columns: 1fr; }
  .education-card-top { grid-template-columns: 78px minmax(0, 1fr); }
  .education-visual { min-height: 78px; border-radius: 15px; }
  .education-insight-visual { min-height: 150px; }
  .app-hero {
    padding: 18px 16px 14px;
    border-radius: 18px;
  }
  .app-hero-top {
    flex-direction: column;
    gap: 12px;
  }
  .app-preferences {
    width: 100%;
  }
  .app-pref-btn {
    flex: 1 1 0;
  }
  .app-hero h1 { font-size: 27px; line-height: 1.22; }
  .dental-page-nav {
    gap: 6px;
    padding: 8px;
    border-radius: 16px;
  }
  .dental-page-nav-item {
    flex: 1 1 calc(50% - 6px);
    padding: 8px 9px;
    text-align: center;
  }
  .dental-page {
    padding: 10px;
    border-radius: 18px;
  }
  .detection-empty-state {
    gap: 10px;
    min-height: 146px;
    padding: 16px;
    text-align: center;
    flex-direction: column;
  }
  .detection-empty-icon {
    flex-basis: 44px;
    width: 44px;
    height: 44px;
    border-radius: 14px;
  }
  .detection-empty-icon svg { width: 29px; height: 29px; }
  .detection-empty-title { font-size: 20px; margin-bottom: 4px; }
  .detection-empty-desc { font-size: 13px; line-height: 1.55; }
  .detection-empty-hint { margin-top: 7px; }
  #page-batch .batch-empty-state-panel .detection-empty-state {
    min-height: 210px;
    padding: 18px;
  }
  .det-explain { max-height: none; }
}
"""
