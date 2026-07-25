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
body[data-dental-theme="dark"] .native-ai-suggestion-title,
body[data-dental-theme="dark"] .native-ai-export-btn small {
  color: #cbd5e1 !important;
}
body[data-dental-theme="dark"] .native-ai-assistant button.native-ai-suggestion,
body[data-dental-theme="dark"] .native-ai-export-btn,
body[data-dental-theme="dark"] #ask-ai-input textarea {
  background: rgba(15,23,42,0.9) !important;
  border-color: rgba(71,85,105,0.82) !important;
  color: #e5e7eb !important;
}
body[data-dental-theme="dark"] .native-ai-export-btn::before {
  background: rgba(30,41,59,0.92) !important;
  border-color: rgba(96,165,250,0.42) !important;
  color: #93c5fd !important;
  box-shadow: inset 0 0 0 4px rgba(15,23,42,0.42) !important;
}
body[data-dental-theme="dark"] .native-ai-export-btn.export-pdf::before {
  border-color: rgba(251,146,60,0.42) !important;
  color: #fdba74 !important;
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
.quality-grid {
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
.det-input-row, .det-result-row {
  align-items: stretch !important;
}
.det-input-row,
.det-result-row,
.compare-threshold-row,
.compare-model-row,
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
.report-download-row .report-download-action {
  flex: 1 1 180px !important;
  min-width: 0 !important;
}
.report-download-row .report-download-action a,
.report-download-row .report-download-action button {
  width: 100% !important;
  min-height: 44px !important;
  justify-content: center !important;
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

/* 2026 workflow, responsive and accessibility refinements */
.dental-nav-items {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  width: 100%;
}
.dental-nav-toggle { display: none; }
.detection-workflow {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0;
  margin: 0 0 14px;
  padding: 0;
  list-style: none;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #fff;
  overflow: hidden;
}
.detection-workflow li {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 44px;
  color: #64748b;
  border-right: 1px solid #e2e8f0;
}
.detection-workflow li:last-child { border-right: 0; }
.detection-workflow li span {
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #f1f5f9;
  font-size: 12px;
  font-weight: 800;
}
.detection-workflow li.is-active { color: #1d4ed8; background: #eff6ff; }
.detection-workflow li.is-active span { color: #fff; background: #2563eb; }
.detection-workflow li.is-done { color: #047857; background: #f0fdf4; }
.detection-workflow li.is-done span { color: #fff; background: #10b981; }
.detection-ready-state {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 72px;
  margin: 0 0 14px;
  padding: 12px 16px;
  border: 1px solid #bfdbfe;
  border-radius: 8px;
  background: #f8fbff;
  color: #1e3a5f;
}
.detection-ready-check {
  display: grid;
  place-items: center;
  flex: 0 0 34px;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #dbeafe;
  color: #1d4ed8;
  font-weight: 900;
}
.detection-ready-state b,
.detection-ready-state small { display: block; }
.detection-ready-state small { margin-top: 3px; color: #64748b; line-height: 1.45; }
.sticky-actionbar {
  position: sticky !important;
  top: 76px;
  z-index: 80;
  align-self: flex-start;
  border: 1px solid #dbe5f1 !important;
  border-radius: 8px !important;
  background: rgba(255,255,255,.97) !important;
  box-shadow: 0 8px 22px rgba(15,23,42,.08) !important;
  backdrop-filter: blur(10px);
}
.solid-primary-action button,
button.solid-primary-action,
.gradio-container button.primary {
  border: 1px solid #1d4ed8 !important;
  border-radius: 8px !important;
  background: #2563eb !important;
  color: #fff !important;
  box-shadow: 0 5px 14px rgba(37,99,235,.18) !important;
}
.result-filter-bar {
  align-items: end !important;
  gap: 10px !important;
  margin: 10px 0 6px;
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: #f8fafc;
}
.result-filter-bar > * { min-width: 170px; }
.result-compare-slider {
  height: min(620px, 66vh) !important;
  min-height: 420px !important;
  max-height: 620px !important;
  overflow: hidden !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
}
.result-compare-slider .image-container,
.result-compare-slider [data-testid="image-slider"] { height: 100% !important; min-height: 0 !important; }
.result-compare-slider img { object-fit: contain !important; }
.det-output-data { display: none !important; }
.sync-model-viewer { overflow: hidden !important; min-height: 300px; }
.sync-model-viewer img {
  object-fit: contain !important;
  transition: transform .12s ease-out;
  will-change: transform;
}
.batch-task-list {
  border: 1px solid #dbe5f1;
  border-radius: 8px;
  background: #fff;
  overflow: hidden;
}
.batch-task-panel { max-height: 320px !important; overflow-y: auto !important; overflow-x: hidden !important; }
.batch-task-list header,
.report-recent-list header,
.dashboard-compact-panel header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 11px 14px;
  border-bottom: 1px solid #e2e8f0;
}
.batch-task-list header span,
.report-recent-list header span,
.dashboard-compact-panel header span { color: #64748b; font-size: 12px; }
.batch-task-row {
  display: grid;
  grid-template-columns: 36px minmax(0,1fr) auto;
  align-items: center;
  gap: 10px;
  min-height: 56px;
  padding: 8px 14px;
  border-bottom: 1px solid #eef2f7;
}
.batch-task-row:last-child { border-bottom: 0; }
.batch-task-index { color: #64748b; font-size: 12px; font-weight: 800; }
.batch-task-main { min-width: 0; }
.batch-task-main b { display: block; overflow: hidden; color: #1e293b; font-size: 13px; text-overflow: ellipsis; white-space: nowrap; }
.batch-task-track { height: 4px; margin-top: 7px; border-radius: 4px; background: #e2e8f0; overflow: hidden; }
.batch-task-track i { display: block; height: 100%; background: #2563eb; }
.batch-task-row.done .batch-task-track i { background: #10b981; }
.batch-task-row.failed .batch-task-track i { background: #ef4444; }
.batch-task-status { color: #64748b; font-size: 12px; font-weight: 800; }
.batch-task-row.done .batch-task-status { color: #047857; }
.batch-task-row.failed .batch-task-status { color: #b91c1c; }
.batch-retry-panel {
  margin: 0 0 12px !important;
  padding: 10px 12px !important;
  border: 1px solid #fecaca !important;
  border-radius: 8px !important;
  background: #fffafa !important;
  box-shadow: none !important;
}
.batch-retry-panel h4 { margin: 0 0 8px !important; color: #991b1b !important; font-size: 14px !important; }
.batch-retry-actions { align-items: end !important; gap: 8px !important; }
.batch-retry-actions > *:first-child { flex: 1 1 auto !important; }
.batch-retry-actions > *:last-child { flex: 0 0 150px !important; }

/* Detection result rows: prevent inherited stretch/min-height from creating gray voids. */
#page-image .det-result-row,
#page-compare .compare-model-row,
#page-batch .batch-work-row {
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-items: flex-start !important;
  overflow: visible !important;
}
#page-image .det-result-row > *,
#page-compare .compare-model-row > *,
#page-batch .batch-work-row > *,
#page-batch .batch-left-column,
#page-batch .batch-right-column {
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-self: flex-start !important;
  flex-grow: 0 !important;
}
#page-image .det-result-row { align-items: stretch !important; }
#page-image .det-result-row > * { flex: 1 1 0 !important; }
#page-image .det-result-row .det-explain {
  height: min(620px, 66vh) !important;
  min-height: 420px !important;
  max-height: 620px !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}
#page-compare .compare-slider-row { align-items: stretch !important; }
#page-compare .compare-slider-row > * { flex: 1 1 0 !important; }
#page-compare .compare-slider-row .result-compare-slider {
  height: clamp(300px, 34vw, 470px) !important;
  min-height: 300px !important;
  max-height: 470px !important;
}
#page-batch #batch-result-slider {
  height: min(560px, 62vh) !important;
  min-height: 380px !important;
  max-height: 560px !important;
  margin-bottom: 10px !important;
}
#page-batch .batch-left-column,
#page-batch .batch-right-column { background: transparent !important; }
#page-batch .batch-left-column { flex: 0 0 min(420px, 32%) !important; }
#page-batch .batch-right-column { flex: 1 1 0 !important; width: auto !important; }
#page-batch .batch-setup-row > * {
  flex: 1 1 0 !important;
  width: auto !important;
  height: auto !important;
  min-height: 0 !important;
  align-self: flex-start !important;
}
#page-batch .batch-upload-column,
#page-batch #batch-upload {
  height: 327px !important;
  min-height: 327px !important;
  max-height: 327px !important;
}
#page-batch #batch-upload > *,
#page-batch #batch-upload .wrap,
#page-batch #batch-upload .file-preview,
#page-batch #batch-upload .upload-container {
  height: 100% !important;
  min-height: 0 !important;
}
#page-batch #batch-upload .file-preview { overflow-y: auto !important; overflow-x: hidden !important; }
#page-batch .batch-work-row { background: transparent !important; box-shadow: none !important; padding: 0 !important; }
#page-batch .batch-item-actions { margin: 0 0 8px !important; padding: 0 !important; border: 0 !important; box-shadow: none !important; }
#page-batch .det-explain {
  height: auto !important;
  min-height: 0 !important;
  max-height: 620px !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}
.dashboard-operations-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
.dashboard-compact-panel { border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; }
.dashboard-trend { display: flex; align-items: end; gap: 8px; height: 150px; padding: 18px 16px 12px; }
.dashboard-trend-bar { display: flex; flex: 1; flex-direction: column; justify-content: end; align-items: center; height: 100%; gap: 6px; }
.dashboard-trend-bar i { width: min(38px, 70%); min-height: 8px; border-radius: 4px 4px 0 0; background: #2563eb; }
.dashboard-trend-bar span { color: #64748b; font-size: 11px; }
.dashboard-anomaly-list { display: grid; gap: 0; margin: 0; padding: 4px 14px; list-style: none; }
.dashboard-anomaly-list li { display: grid; grid-template-columns: 10px minmax(0,1fr); gap: 2px 8px; padding: 9px 0; border-bottom: 1px solid #eef2f7; }
.dashboard-anomaly-list li:last-child { border-bottom: 0; }
.dashboard-anomaly-list small { grid-column: 2; color: #64748b; }
.status-dot { width: 8px; height: 8px; margin-top: 5px; border-radius: 50%; background: #f59e0b; }
.status-dot.status-failed { background: #ef4444; }
.report-recent-list { margin-top: 12px; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; overflow: hidden; }
.report-recent-item { display: grid; grid-template-columns: 42px minmax(0,1fr) auto; align-items: center; gap: 12px; padding: 10px 14px; border-bottom: 1px solid #eef2f7; }
.report-recent-item:last-child { border-bottom: 0; }
.report-cover-mini { display: grid; place-items: center; width: 40px; height: 48px; border: 1px solid #bfdbfe; border-radius: 6px; background: #eff6ff; color: #1d4ed8; font-size: 10px; font-weight: 900; }
.report-recent-item div:nth-child(2) { min-width: 0; }
.report-recent-item div:nth-child(2) b { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.report-recent-item div:nth-child(2) span { display: block; margin-top: 3px; color: #64748b; font-size: 12px; }
.report-recent-item strong { color: #047857; font-size: 12px; }
.education-toolbar { position: sticky; top: 72px; z-index: 70; display: grid; grid-template-columns: auto minmax(220px,1fr) auto; align-items: center; gap: 12px; margin-bottom: 12px; padding: 10px 12px; border: 1px solid #dbe5f1; border-radius: 8px; background: rgba(255,255,255,.97); box-shadow: 0 7px 18px rgba(15,23,42,.07); }
.education-toolbar label { font-weight: 800; }
.education-toolbar input { min-height: 42px; padding: 0 12px; border: 1px solid #cbd5e1; border-radius: 8px; }
.education-directory { display: flex; gap: 6px; }
.education-directory button { min-height: 38px; padding: 0 10px; border: 1px solid #cbd5e1; border-radius: 8px; background: #fff; color: #334155; font-weight: 700; }
.education-directory button.active { border-color: #2563eb; background: #eff6ff; color: #1d4ed8; }
.education-card[hidden] { display: none !important; }
.education-no-result { padding: 28px; text-align: center; color: #64748b; }
.native-ai-heading { margin-top: 18px !important; padding: 7px 10px; border-left: 4px solid #64748b; border-radius: 4px; background: #f8fafc; }
.native-ai-heading-conclusion { border-left-color: #2563eb; background: #eff6ff; }
.native-ai-heading-evidence { border-left-color: #0f766e; background: #f0fdfa; }
.native-ai-heading-risk { border-left-color: #ea580c; background: #fff7ed; }
.native-ai-heading-next { border-left-color: #7c3aed; background: #faf5ff; }
.native-ai-evidence-links { display: flex; flex-wrap: wrap; gap: 7px; margin: 14px 0 4px; padding-top: 12px; border-top: 1px solid #e2e8f0; }
.native-ai-evidence-link { min-height: 36px; padding: 6px 10px; border: 1px solid #bfdbfe; border-radius: 8px; background: #eff6ff; color: #1d4ed8; font-size: 12px; font-weight: 800; cursor: pointer; }
.native-ai-evidence-link:hover { border-color: #2563eb; background: #dbeafe; }
.gradio-container button,
.gradio-container input,
.gradio-container textarea,
.gradio-container select { letter-spacing: 0 !important; }
.gradio-container button:focus-visible,
.gradio-container input:focus-visible,
.gradio-container textarea:focus-visible,
.gradio-container select:focus-visible,
[tabindex]:focus-visible { outline: 3px solid rgba(37,99,235,.32) !important; outline-offset: 2px !important; }
.gradio-container .table-wrap { overflow-x: auto !important; }
.gradio-container table { min-width: 760px; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { scroll-behavior: auto !important; transition-duration: .01ms !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; }
}
@media (max-width: 900px) {
  .dental-page-nav { display: block; padding: 8px; }
  .dental-nav-toggle { display: flex; width: 100%; min-height: 44px; align-items: center; justify-content: space-between; border: 0; background: transparent; color: #1e293b; font-weight: 900; }
  .dental-nav-items { display: none; grid-template-columns: 1fr 1fr; gap: 6px; padding-top: 8px; }
  .dental-page-nav.nav-open .dental-nav-items { display: grid; }
  .dental-page-nav-item { width: 100%; border-radius: 8px; text-align: left; }
  .sticky-actionbar { position: static !important; }
  .education-toolbar { position: static; grid-template-columns: 1fr; }
  .education-directory { display: grid; grid-template-columns: 1fr 1fr; }
  .dashboard-operations-grid { grid-template-columns: 1fr; }
  .result-filter-bar { display: grid !important; grid-template-columns: 1fr 1fr; }
  .compare-model-row { display: grid !important; grid-template-columns: 1fr; }
  .result-compare-slider,
  #page-image .det-result-row .det-explain,
  #page-batch #batch-result-slider {
    height: min(520px, 62vh) !important;
    min-height: 320px !important;
    max-height: 520px !important;
  }
  #page-image .det-result-row { display: grid !important; grid-template-columns: 1fr; }
  #page-batch .batch-upload-column,
  #page-batch #batch-upload {
    height: auto !important;
    min-height: 240px !important;
    max-height: none !important;
  }
}
@media (max-width: 560px) {
  .detection-workflow li { min-height: 40px; gap: 4px; font-size: 12px; }
  .detection-workflow li span { width: 20px; height: 20px; }
  .result-filter-bar { grid-template-columns: 1fr; }
  .education-directory { grid-template-columns: 1fr; }
  .report-recent-item { grid-template-columns: 38px minmax(0,1fr); }
  .report-recent-item strong { grid-column: 2; }
  .batch-task-row { grid-template-columns: 30px minmax(0,1fr); }
  .batch-task-status { grid-column: 2; }
  .result-compare-slider,
  #page-image .det-result-row .det-explain,
  #page-batch #batch-result-slider {
    min-height: 280px !important;
  }
  .batch-retry-actions { display: grid !important; grid-template-columns: 1fr; }
  .batch-retry-actions > * { width: 100% !important; flex: 1 1 auto !important; }
}

/* Unified detection workspace: intrinsic-height cards and full-width result flow. */
#page-image,
#page-compare,
#page-batch,
#page-image > *,
#page-compare > *,
#page-batch > * {
  min-height: 0 !important;
}
.detection-setup-grid {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: stretch !important;
  gap: 16px !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
}
.detection-setup-grid > * {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
  height: 100% !important;
  min-height: 0 !important;
  align-self: stretch !important;
  flex: none !important;
}
.detection-upload-panel,
.detection-parameter-panel {
  padding: 14px !important;
  border: 1px solid #dbe5f1 !important;
  border-radius: 8px !important;
  background: #fff !important;
  box-shadow: 0 8px 22px rgba(15, 23, 42, .06) !important;
  overflow: visible !important;
}
.detection-upload-panel h3,
.detection-parameter-panel h3 {
  margin: 0 0 10px !important;
  font-size: 17px !important;
  line-height: 1.35 !important;
}
.detection-controls,
.detection-controls > *,
.detection-controls .form,
.detection-controls .wrap {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  height: auto !important;
  min-height: 0 !important;
}
.detection-controls.sticky-actionbar {
  position: static !important;
  inset: auto !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-compare .compare-threshold-row {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 12px !important;
  width: 100% !important;
  max-width: none !important;
}
#page-compare .detection-parameter-panel .detection-controls,
#page-compare .detection-parameter-panel .detection-controls > div,
#page-compare .detection-parameter-panel .detection-controls > div > div,
#page-compare .compare-threshold-row > * {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  flex: 1 1 auto !important;
}
#page-image #single-upload,
#page-compare #compare-upload {
  height: 300px !important;
  min-height: 300px !important;
  max-height: 300px !important;
}
#page-batch #batch-upload {
  width: 100% !important;
  height: 88px !important;
  min-height: 88px !important;
  max-height: 88px !important;
}
#page-batch #batch-upload-preview {
  width: 100% !important;
  height: 204px !important;
  min-height: 204px !important;
  max-height: 204px !important;
  overflow: hidden !important;
}
#page-batch #batch-upload-preview .grid-wrap,
#page-batch #batch-upload-preview .grid-container {
  height: 100% !important;
  min-height: 0 !important;
}
#page-batch #batch-upload-preview img {
  object-fit: contain !important;
  background: #f8fafc !important;
}
#page-batch .detection-setup-grid > .batch-upload-column {
  height: 100% !important;
  min-height: 0 !important;
  max-height: none !important;
  align-self: stretch !important;
}
.detection-result-stack,
.detection-result-stack > * {
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-self: start !important;
  flex: none !important;
  overflow: visible !important;
}
#page-image .detection-result-stack .result-compare-slider,
#page-batch #batch-result-slider {
  height: clamp(380px, 52vw, 620px) !important;
  min-height: 380px !important;
  max-height: 620px !important;
}
#page-batch .batch-item-actions {
  width: 100% !important;
  margin: 0 0 10px !important;
}
#page-batch .batch-item-actions > * {
  width: 100% !important;
  max-width: none !important;
  flex: 1 1 auto !important;
}
#page-image .detection-result-stack .det-explain,
#page-batch .det-explain,
#page-compare .det-explain {
  height: auto !important;
  min-height: 0 !important;
  max-height: 620px !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}
#page-compare .compare-slider-row {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 12px !important;
  height: auto !important;
  min-height: 0 !important;
}
#page-compare .compare-slider-row > * {
  width: 100% !important;
  min-width: 0 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-self: start !important;
}
#page-compare .compare-slider-row .result-compare-slider {
  height: clamp(300px, 30vw, 440px) !important;
  min-height: 300px !important;
  max-height: 440px !important;
}
/* Gradio wraps both comparison sliders in one .form. Let that wrapper span
   the full parameter grid, then lay its two real controls out evenly. */
#page-compare #compare-controls,
#page-compare #compare-controls > .styler {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  align-items: stretch !important;
}
#page-compare #compare-threshold-row > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 12px !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
}
#page-compare #compare-threshold-row > .form > * {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
}

/* Keep the batch uploader and its thumbnails in one stable upload surface. */
#page-batch .batch-upload-composite,
#page-batch .batch-upload-composite > .styler {
  display: flex !important;
  flex-direction: column !important;
  gap: 0 !important;
  width: 100% !important;
  height: 300px !important;
  min-height: 300px !important;
  max-height: 300px !important;
  padding: 0 !important;
  overflow: hidden !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
}
#page-batch .batch-upload-composite #batch-upload {
  flex: 1 1 auto !important;
  width: 100% !important;
  height: 300px !important;
  min-height: 0 !important;
  max-height: none !important;
  border-radius: 8px !important;
}
#page-batch .batch-upload-composite:has(#batch-upload-preview) #batch-upload {
  flex: 0 0 76px !important;
  height: 76px !important;
  min-height: 76px !important;
  max-height: 76px !important;
  border-radius: 8px 8px 0 0 !important;
}
#page-batch .batch-upload-composite #batch-upload-preview {
  flex: 1 1 auto !important;
  width: 100% !important;
  height: 224px !important;
  min-height: 224px !important;
  max-height: 224px !important;
  margin: 0 !important;
  padding: 8px !important;
  border: 1px solid #dbe5f1 !important;
  border-top: 0 !important;
  border-radius: 0 0 8px 8px !important;
  background: #fff !important;
}
#page-batch .batch-upload-composite #batch-upload-preview .grid-wrap,
#page-batch .batch-upload-composite #batch-upload-preview .grid-container {
  height: 100% !important;
  min-height: 0 !important;
  overflow: hidden !important;
}

/* ImageSlider labels are supplied by the surrounding model tags/dropdown.
   Keep Gradio's internal layers full width and reset the divider on updates. */
#page-compare .compare-slider-row .result-compare-slider,
#page-batch #batch-result-slider {
  width: 100% !important;
  max-width: none !important;
}
#page-compare .compare-slider-row .result-compare-slider .image-container,
#page-compare .compare-slider-row .result-compare-slider [data-testid="image-slider"],
#page-batch #batch-result-slider .image-container,
#page-batch #batch-result-slider [data-testid="image-slider"] {
  width: 100% !important;
  max-width: none !important;
}

@media (max-width: 900px) {
  .detection-setup-grid,
  #page-compare .compare-slider-row { grid-template-columns: 1fr !important; }
  #page-image #single-upload,
  #page-compare #compare-upload {
    height: auto !important;
    min-height: 240px !important;
    max-height: none !important;
  }
  #page-batch .batch-upload-composite,
  #page-batch .batch-upload-composite > .styler { height: 280px !important; min-height: 280px !important; max-height: 280px !important; }
  #page-batch .batch-upload-composite #batch-upload { height: 280px !important; }
  #page-batch .batch-upload-composite:has(#batch-upload-preview) #batch-upload { height: 72px !important; min-height: 72px !important; max-height: 72px !important; }
  #page-batch .batch-upload-composite #batch-upload-preview { height: 208px !important; min-height: 208px !important; max-height: 208px !important; }
  #page-batch .detection-setup-grid > .batch-upload-column {
    height: auto !important;
    align-self: start !important;
  }
  #page-compare .compare-threshold-row,
  #page-compare #compare-threshold-row > .form { grid-template-columns: 1fr !important; }
  .detection-setup-grid > * { height: auto !important; align-self: start !important; }
}

/* 2026 restrained workspace polish. Keep this block last so legacy theme rules
   cannot reintroduce oversized radii, decorative gradients or uneven controls. */
:root {
  --surface-canvas: #f3f6fa;
  --surface-panel: #ffffff;
  --surface-subtle: #f8fafc;
  --surface-selected: #eff6ff;
  --text-strong: #172033;
  --text-body: #334155;
  --text-soft: #64748b;
  --border-soft: #dfe6ef;
  --border-strong: #cbd5e1;
  --action: #2563eb;
  --action-hover: #1d4ed8;
  --medical-accent: #f97316;
  --success: #059669;
  --danger: #dc2626;
  --radius-panel: 8px;
  --shadow-panel: 0 8px 24px rgba(15, 23, 42, 0.055);
}

.gradio-container {
  background: var(--surface-canvas) !important;
  color: var(--text-body) !important;
}
.app-hero {
  padding: 18px 22px 16px !important;
  margin: 8px auto 12px !important;
  border: 1px solid var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: var(--shadow-panel) !important;
  backdrop-filter: none !important;
}
.app-hero h1 {
  margin-bottom: 5px !important;
  color: var(--text-strong) !important;
  font-size: clamp(27px, 2.2vw, 34px) !important;
  font-weight: 850 !important;
}
.app-hero p { color: var(--text-soft) !important; line-height: 1.55 !important; }
.app-pref-btn {
  min-height: 38px !important;
  border-color: var(--border-soft) !important;
  border-radius: 8px !important;
  background: var(--surface-subtle) !important;
  box-shadow: none !important;
}
.app-pref-btn:hover {
  transform: none !important;
  border-color: #93c5fd !important;
  background: var(--surface-selected) !important;
}

.dental-page-nav {
  gap: 5px !important;
  margin-bottom: 12px !important;
  padding: 7px !important;
  border: 1px solid var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: rgba(255, 255, 255, 0.96) !important;
  box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06) !important;
}
.dental-nav-items { gap: 5px !important; }
.dental-page-nav-item {
  min-height: 39px !important;
  padding: 8px 13px !important;
  border: 1px solid transparent !important;
  border-radius: 7px !important;
  background: transparent !important;
  box-shadow: none !important;
  color: #475569 !important;
  font-weight: 750 !important;
}
.dental-page-nav-item:hover {
  transform: none !important;
  border-color: var(--border-soft) !important;
  background: var(--surface-subtle) !important;
  color: var(--text-strong) !important;
  box-shadow: none !important;
}
.dental-page-nav-item.active {
  border-color: #1d4ed8 !important;
  background: var(--action) !important;
  color: #fff !important;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
}
body[data-dental-page="learn"] .dental-page-nav-item[data-page="learn"],
body[data-dental-page="dashboard"] .dental-page-nav-item[data-page="dashboard"],
body[data-dental-page="image"] .dental-page-nav-item[data-page="image"],
body[data-dental-page="compare"] .dental-page-nav-item[data-page="compare"],
body[data-dental-page="batch"] .dental-page-nav-item[data-page="batch"],
body[data-dental-page="history"] .dental-page-nav-item[data-page="history"],
body[data-dental-page="assistant"] .dental-page-nav-item[data-page="assistant"],
body[data-dental-page="report"] .dental-page-nav-item[data-page="report"] {
  border-color: #1d4ed8 !important;
  background: var(--action) !important;
  color: #fff !important;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
}

.dental-page,
#page-image,
#page-compare,
#page-batch {
  padding: 10px !important;
  border: 1px solid var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: var(--shadow-panel) !important;
}
.section-note {
  margin-bottom: 10px !important;
  padding: 12px 14px !important;
  border: 1px solid #fed7aa !important;
  border-left: 4px solid var(--medical-accent) !important;
  border-radius: var(--radius-panel) !important;
  background: #fffaf5 !important;
  box-shadow: none !important;
}
.section-note::before { content: none !important; }
.section-note b { color: #c2410c !important; }

.det-input-row,
.det-result-row,
.compare-threshold-row,
.compare-model-row,
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
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: none !important;
}
.detection-setup-grid,
.detection-result-stack,
.compare-slider-row { gap: 12px !important; }
.detection-workflow {
  margin-bottom: 10px !important;
  border-color: var(--border-soft) !important;
  box-shadow: none !important;
}
.detection-workflow li { color: var(--text-soft) !important; font-weight: 700 !important; }
.detection-workflow li.is-active { background: var(--surface-selected) !important; color: #1d4ed8 !important; }
.detection-workflow li.is-done { background: #ecfdf5 !important; color: #047857 !important; }
.detection-ready-state {
  border-color: #bfdbfe !important;
  background: #f8fbff !important;
  box-shadow: none !important;
}
.sticky-actionbar {
  border-color: var(--border-soft) !important;
  background: rgba(255, 255, 255, 0.98) !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.065) !important;
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
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: none !important;
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
  border-color: var(--border-soft) !important;
  border-radius: 7px !important;
  background: var(--surface-subtle) !important;
  box-shadow: none !important;
}
.detection-empty-state {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-subtle) !important;
  box-shadow: none !important;
}
.detection-empty-icon {
  border-color: #bfdbfe !important;
  border-radius: 8px !important;
  background: var(--surface-selected) !important;
  color: var(--action) !important;
}
.result-compare-slider,
.det-explain,
.batch-knowledge-content,
.report-preview-panel {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: none !important;
}
.model-tag,
.quality-card,
.result-card,
.metric-card,
.knowledge-card {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: var(--surface-panel) !important;
  box-shadow: none !important;
}

.gradio-container input:not([type="range"]):not([type="checkbox"]):not([type="radio"]),
.gradio-container textarea,
.gradio-container select {
  border-color: var(--border-strong) !important;
  border-radius: 7px !important;
  background: #fff !important;
  color: var(--text-strong) !important;
  box-shadow: none !important;
}
.gradio-container textarea { line-height: 1.6 !important; }
.gradio-container input::placeholder,
.gradio-container textarea::placeholder { color: #94a3b8 !important; opacity: 1 !important; }
.gradio-container button.primary,
.solid-primary-action button,
button.solid-primary-action {
  min-height: 44px !important;
  border-color: var(--action) !important;
  border-radius: 7px !important;
  background: var(--action) !important;
  box-shadow: none !important;
  font-weight: 800 !important;
}
.gradio-container button.primary:hover,
.solid-primary-action button:hover,
button.solid-primary-action:hover {
  border-color: var(--action-hover) !important;
  background: var(--action-hover) !important;
  transform: none !important;
}
.gradio-container button.secondary {
  min-height: 42px !important;
  border-color: var(--border-strong) !important;
  border-radius: 7px !important;
  background: #fff !important;
  color: var(--text-body) !important;
  box-shadow: none !important;
}
.gradio-container button.secondary:hover { border-color: #93c5fd !important; background: var(--surface-selected) !important; }
.gradio-container .accordion {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: #fff !important;
  box-shadow: none !important;
}

.gradio-container .table-wrap,
.gradio-container .table-container {
  border: 1px solid var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: #fff !important;
}
.gradio-container table { border-collapse: separate !important; border-spacing: 0 !important; background: #fff !important; }
.gradio-container table thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 11px 12px !important;
  border-color: var(--border-soft) !important;
  background: #f1f5f9 !important;
  color: var(--text-strong) !important;
  font-size: 13px !important;
  font-weight: 800 !important;
}
.gradio-container table tbody td { padding: 10px 12px !important; border-color: #edf1f6 !important; color: var(--text-body) !important; }
.gradio-container table tbody tr:hover td { background: #f8fbff !important; }

/* Learning page: clinical atlas layout */
#page-learn .education-shell {
  --edu-navy: #102a43;
  --edu-blue: #2563eb;
  --edu-teal: #0f766e;
  --edu-amber: #d97706;
  display: grid;
  gap: 20px;
}
#page-learn .education-toolbar {
  position: sticky;
  top: 72px;
  z-index: 70;
  display: grid;
  grid-template-columns: auto minmax(260px, 1fr) auto;
  align-items: center;
  gap: 14px;
  margin: 0;
  padding: 12px 14px;
  border: 1px solid rgba(203, 213, 225, 0.84) !important;
  border-radius: 14px !important;
  background: rgba(255, 255, 255, 0.94) !important;
  box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08) !important;
  backdrop-filter: blur(16px);
}
#page-learn .education-search-label { min-width: 110px; }
#page-learn .education-search-label b,
#page-learn .education-search-label span { display: block; }
#page-learn .education-search-label b { color: var(--edu-navy); font-size: 13px; }
#page-learn .education-search-label span { margin-top: 2px; color: #64748b; font-size: 11px; }
#page-learn .education-search-box {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  min-height: 44px;
  padding: 0 8px 0 13px;
  border: 1px solid #cbd5e1;
  border-radius: 10px;
  background: #f8fafc;
  transition: border-color .18s ease, box-shadow .18s ease, background .18s ease;
}
#page-learn .education-search-box:focus-within {
  border-color: #60a5fa;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.11);
}
#page-learn .education-search-box > span { color: #64748b; font-size: 20px; line-height: 1; }
#page-learn .education-search-box input {
  min-width: 0;
  min-height: 42px;
  padding: 0 10px;
  border: 0 !important;
  outline: 0;
  background: transparent;
  color: #0f172a;
  box-shadow: none !important;
}
#page-learn .education-search-box button {
  min-height: 30px;
  padding: 0 10px;
  border: 0;
  border-radius: 7px;
  background: #e2e8f0;
  color: #475569;
  font-size: 12px;
  font-weight: 800;
  cursor: pointer;
}
#page-learn .education-directory { display: flex; gap: 6px; }
#page-learn .education-directory button {
  min-height: 38px;
  padding: 0 11px;
  border: 1px solid #cbd5e1;
  border-radius: 8px !important;
  background: #fff;
  color: #475569;
  font-size: 12px;
  font-weight: 800;
  cursor: pointer;
}
#page-learn .education-directory button:hover { border-color: #93c5fd; background: #f8fbff; }
#page-learn .education-directory button.active {
  border-color: #2563eb;
  background: #2563eb;
  color: #fff;
  box-shadow: 0 5px 14px rgba(37, 99, 235, 0.18);
}
#page-learn .education-hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.16fr) minmax(330px, .84fr);
  gap: 18px;
  padding: 26px;
  overflow: hidden;
  border: 1px solid #cbdced !important;
  border-radius: 18px !important;
  background:
    radial-gradient(circle at 8% 5%, rgba(14, 165, 233, .15), transparent 34%),
    radial-gradient(circle at 94% 88%, rgba(20, 184, 166, .13), transparent 30%),
    linear-gradient(135deg, #f8fbff 0%, #ffffff 55%, #f0fdfa 100%) !important;
  box-shadow: 0 18px 46px rgba(15, 42, 67, 0.08) !important;
}
#page-learn .education-panel h2 { color: var(--edu-navy); font-size: clamp(32px, 3.7vw, 50px); letter-spacing: -.025em; }
#page-learn .education-panel h2 span { color: var(--edu-blue); }
#page-learn .education-lead { max-width: 800px; color: #3f5368; font-size: 15px; line-height: 1.85; }
#page-learn .education-eyebrow {
  border-color: #bae6fd;
  border-radius: 7px;
  background: #f0f9ff;
  color: #0369a1;
  letter-spacing: .06em;
  text-transform: uppercase;
}
#page-learn .education-metric {
  border-color: rgba(186, 230, 253, .9);
  border-radius: 10px;
  background: rgba(255, 255, 255, .8);
}
#page-learn .education-metric b { color: var(--edu-teal); font-size: 20px; }
#page-learn .education-insight-panel {
  padding: 16px;
  border: 1px solid #cbdced;
  border-radius: 14px;
  background: rgba(255, 255, 255, .84);
  box-shadow: none;
}
#page-learn .education-insight-visual {
  min-height: 180px;
  border-color: #dbeafe;
  border-radius: 10px;
  background: linear-gradient(145deg, #f8fafc, #eff6ff 58%, #ecfeff);
}
#page-learn .education-review-strip { gap: 10px; }
#page-learn .education-review-step {
  min-height: 94px;
  border-color: #dbe5f1;
  border-radius: 12px;
  background: #fff;
  box-shadow: none;
}
#page-learn .education-review-step b { border-radius: 8px; }
#page-learn .education-section-heading {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  padding: 2px 2px 0;
}
#page-learn .education-section-heading > div > span {
  display: block;
  margin-bottom: 5px;
  color: #0f766e;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .12em;
  text-transform: uppercase;
}
#page-learn .education-section-heading h3 { margin: 0; color: var(--edu-navy); font-size: 24px; line-height: 1.25; }
#page-learn .education-section-heading p { max-width: 560px; margin: 0; color: #64748b; font-size: 13px; line-height: 1.65; }
#page-learn .education-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
#page-learn .education-card {
  --edu-accent: #2563eb;
  --edu-accent-soft: #eff6ff;
  gap: 12px;
  padding: 16px;
  border: 1px solid #dbe5f1 !important;
  border-top: 4px solid var(--edu-accent) !important;
  border-radius: 14px !important;
  background: #fff !important;
  box-shadow: 0 9px 26px rgba(15, 42, 67, .055) !important;
}
#page-learn .education-card--amber { --edu-accent: #d97706; --edu-accent-soft: #fff7ed; }
#page-learn .education-card--blue { --edu-accent: #2563eb; --edu-accent-soft: #eff6ff; }
#page-learn .education-card--teal { --edu-accent: #0f766e; --edu-accent-soft: #f0fdfa; }
#page-learn .education-card::before { content: none; }
#page-learn .education-card-top { grid-template-columns: 88px minmax(0, 1fr); gap: 12px; align-items: center; }
#page-learn .education-visual {
  min-height: 88px;
  border-color: color-mix(in srgb, var(--edu-accent) 25%, #e2e8f0);
  border-radius: 10px !important;
  background: var(--edu-accent-soft) !important;
}
#page-learn .education-card-kicker { display: flex; align-items: center; gap: 7px; margin-bottom: 6px; }
#page-learn .education-badge,
#page-learn .education-code {
  display: inline-flex;
  width: fit-content;
  padding: 3px 7px;
  border-radius: 6px;
  font-size: 10px;
  font-weight: 900;
  line-height: 1.3;
}
#page-learn .education-badge { margin: 0; border-color: transparent; background: var(--edu-accent); color: #fff; }
#page-learn .education-code { background: #f1f5f9; color: #64748b; letter-spacing: .06em; }
#page-learn .education-card h3 { font-size: 18px; }
#page-learn .education-card .subtitle { margin-top: 4px; color: #52667a; font-size: 12px; }
#page-learn .education-card-snapshot {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
#page-learn .education-card-snapshot > div {
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 9px;
  background: #f8fafc;
}
#page-learn .education-card-snapshot span,
#page-learn .education-card-snapshot b { display: block; }
#page-learn .education-card-snapshot span { color: var(--edu-accent); font-size: 10px; font-weight: 900; }
#page-learn .education-card-snapshot b { margin-top: 4px; color: #334155; font-size: 11px; line-height: 1.5; }
#page-learn .education-detail {
  border: 1px solid #e2e8f0;
  border-radius: 9px;
  background: #fff;
  overflow: hidden;
}
#page-learn .education-detail summary {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 11px;
  color: #23364d;
  background: #f8fafc;
  font-size: 12px;
  font-weight: 900;
  cursor: pointer;
  list-style: none;
}
#page-learn .education-detail summary::-webkit-details-marker { display: none; }
#page-learn .education-detail summary::after { content: "+"; margin-left: auto; color: #64748b; font-size: 16px; }
#page-learn .education-detail[open] summary { border-bottom: 1px solid #e2e8f0; background: var(--edu-accent-soft); }
#page-learn .education-detail[open] summary::after { content: "−"; color: var(--edu-accent); }
#page-learn .education-detail summary span {
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 6px;
  background: var(--edu-accent);
  color: #fff;
  font-size: 10px;
}
#page-learn .education-detail-grid { display: grid; grid-template-columns: 1fr; gap: 0; padding: 2px 11px 9px; }
#page-learn .education-detail-grid > div { padding: 9px 0; border-bottom: 1px dashed #e2e8f0; }
#page-learn .education-detail-grid > div:last-child { border-bottom: 0; }
#page-learn .education-detail-grid b { color: var(--edu-accent); font-size: 11px; }
#page-learn .education-detail-grid p { margin: 4px 0 0; color: #40546a; font-size: 11px; line-height: 1.62; }
#page-learn .education-myth { margin: 3px 0; padding: 9px !important; border: 0 !important; border-left: 3px solid #f59e0b !important; border-radius: 0 7px 7px 0; background: #fffbeb; }
#page-learn .education-card-note {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 8px;
  align-items: start;
  padding: 10px;
  border-color: #dbeafe;
  border-radius: 9px;
  background: #f8fbff;
}
#page-learn .education-card-note b { color: #1d4ed8; font-size: 11px; }
#page-learn .education-card-note span { color: #475569; font-size: 11px; line-height: 1.55; }
#page-learn .education-no-result { margin: 0; border: 1px dashed #cbd5e1; border-radius: 12px; background: #f8fafc; }
#page-learn .education-triage {
  display: grid;
  gap: 16px;
  padding: 20px;
  border-radius: 16px;
  background: linear-gradient(135deg, #102a43, #163b5c 60%, #0f4c5c);
  color: #fff;
}
#page-learn .education-section-heading--inverse > div > span { color: #7dd3fc; }
#page-learn .education-section-heading--inverse h3 { color: #fff; }
#page-learn .education-section-heading--inverse p { color: #e5f1ff !important; }
#page-learn .education-triage-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
#page-learn .education-triage-card { padding: 14px; border: 1px solid rgba(255,255,255,.2); border-radius: 11px; background: rgba(255,255,255,.11); }
#page-learn .education-triage-card > span { display: inline-flex; padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: 900; }
#page-learn .education-triage-card h4 { margin: 9px 0 7px; color: #fff !important; font-size: 15px; }
#page-learn .education-triage-card ul { margin: 0; padding-left: 18px; color: #edf6ff !important; font-size: 12px; line-height: 1.75; }
#page-learn .education-triage-card li { color: #edf6ff !important; font-weight: 650; }
#page-learn .education-triage-card li::marker { color: #7dd3fc !important; }
#page-learn .education-triage-card--emergency > span { background: #fee2e2; color: #b91c1c; }
#page-learn .education-triage-card--urgent > span { background: #fef3c7; color: #92400e; }
#page-learn .education-triage-card--routine > span { background: #ccfbf1; color: #115e59; }
#page-learn .education-prep-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
#page-learn .education-prep-card {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 13px;
  padding: 16px;
  border: 1px solid #dbe5f1;
  border-radius: 13px;
  background: #fff;
}
#page-learn .education-prep-card--prevention { background: #f8fffd; border-color: #ccfbf1; }
#page-learn .education-prep-index { display: grid; place-items: center; width: 36px; height: 36px; border-radius: 9px; background: #dbeafe; color: #1d4ed8; font-weight: 900; }
#page-learn .education-prep-card--prevention .education-prep-index { background: #ccfbf1; color: #0f766e; }
#page-learn .education-prep-card h3 { margin: 2px 0 8px; color: var(--edu-navy); font-size: 16px; }
#page-learn .education-prep-card ul { margin: 0; padding-left: 18px; color: #52667a; font-size: 12px; line-height: 1.75; }
#page-learn .education-evidence {
  display: grid;
  grid-template-columns: minmax(260px, .9fr) minmax(0, 1.1fr);
  gap: 18px;
  padding: 17px;
  border: 1px solid #dbe5f1;
  border-radius: 13px;
  background: #f8fafc;
}
#page-learn .education-evidence > div > span { color: #0f766e; font-size: 10px; font-weight: 900; letter-spacing: .1em; }
#page-learn .education-evidence h3 { margin: 4px 0 5px; color: var(--edu-navy); font-size: 17px; }
#page-learn .education-evidence p { margin: 0; color: #64748b; font-size: 11px; line-height: 1.65; }
#page-learn .education-evidence nav { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
#page-learn .education-evidence a { display: flex; align-items: center; min-height: 42px; padding: 8px 10px; border: 1px solid #dbe5f1; border-radius: 8px; background: #fff; color: #1d4ed8; font-size: 11px; font-weight: 800; text-decoration: none; }
#page-learn .education-evidence a:hover { border-color: #93c5fd; background: #eff6ff; }
#page-learn .education-disclaimer { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 12px; padding: 14px 16px; border-left: 4px solid #f59e0b; border-radius: 8px; background: #fffbeb; }
#page-learn .education-disclaimer b { color: #92400e; font-size: 12px; }
#page-learn .education-disclaimer p { margin: 0; color: #604b2d; font-size: 11px; line-height: 1.65; }
@media (prefers-reduced-motion: no-preference) {
  #page-learn .education-card { transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease; }
  #page-learn .education-card:hover { transform: translateY(-2px); border-color: color-mix(in srgb, var(--edu-accent) 36%, #dbe5f1) !important; box-shadow: 0 14px 32px rgba(15,42,67,.09) !important; }
}
@media (max-width: 1180px) {
  #page-learn .education-toolbar { grid-template-columns: auto minmax(240px, 1fr); }
  #page-learn .education-directory { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(4, 1fr); }
  #page-learn .education-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  #page-learn .education-card:last-child { grid-column: 1 / -1; }
  #page-learn .education-card:last-child .education-detail-grid { grid-template-columns: 1fr 1fr; gap: 0 16px; }
  #page-learn .education-card:last-child .education-detail-wide { grid-column: 1 / -1; }
}
@media (max-width: 820px) {
  #page-learn .education-toolbar { position: static; grid-template-columns: 1fr; }
  #page-learn .education-directory { grid-column: auto; grid-template-columns: 1fr 1fr; }
  #page-learn .education-hero { grid-template-columns: 1fr; padding: 18px; }
  #page-learn .education-review-strip { grid-template-columns: 1fr 1fr; }
  #page-learn .education-grid { grid-template-columns: 1fr; }
  #page-learn .education-card:last-child { grid-column: auto; }
  #page-learn .education-card:last-child .education-detail-grid { grid-template-columns: 1fr; }
  #page-learn .education-triage-grid,
  #page-learn .education-prep-grid,
  #page-learn .education-evidence { grid-template-columns: 1fr; }
  #page-learn .education-section-heading { align-items: start; flex-direction: column; gap: 7px; }
}
@media (max-width: 560px) {
  #page-learn .education-panel h2 { font-size: 30px; }
  #page-learn .education-metrics,
  #page-learn .education-review-strip,
  #page-learn .education-directory,
  #page-learn .education-card-snapshot,
  #page-learn .education-evidence nav { grid-template-columns: 1fr; }
  #page-learn .education-card-top { grid-template-columns: 72px minmax(0, 1fr); }
  #page-learn .education-visual { min-height: 72px; }
  #page-learn .education-triage { padding: 15px; }
  #page-learn .education-disclaimer { grid-template-columns: 1fr; gap: 5px; }
}

/* Dashboard: clinical operations overview */
#page-dashboard {
  --dashboard-navy: #102a43;
  --dashboard-blue: #2563eb;
  --dashboard-cyan: #0891b2;
  --dashboard-amber: #d97706;
  --dashboard-teal: #0f766e;
}
#page-dashboard .dashboard-overview-html,
#page-dashboard .dashboard-overview-html > *,
#page-dashboard .dashboard-overview-html .html-container {
  min-height: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-dashboard .dashboard-shell {
  display: grid;
  gap: 18px;
}
#page-dashboard .dashboard-overview {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(290px, .7fr);
  gap: 20px;
  padding: 24px;
  overflow: hidden;
  border: 1px solid #d8e5f2;
  border-radius: 16px;
  background:
    radial-gradient(circle at 82% 8%, rgba(14,165,233,.13), transparent 30%),
    linear-gradient(135deg, #f8fbff 0%, #eef6ff 58%, #f0fdfa 100%);
}
#page-dashboard .dashboard-overview::after {
  content: "";
  position: absolute;
  right: -72px;
  bottom: -104px;
  width: 250px;
  height: 250px;
  border: 48px solid rgba(37,99,235,.055);
  border-radius: 50%;
  pointer-events: none;
}
#page-dashboard .dashboard-overview-copy {
  position: relative;
  z-index: 1;
  min-width: 0;
}
#page-dashboard .dashboard-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #1d4ed8;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .12em;
}
#page-dashboard .dashboard-eyebrow > span {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 0 5px rgba(16,185,129,.12);
}
#page-dashboard .dashboard-overview h2 {
  margin: 11px 0 0;
  color: #0f2942;
  font-size: clamp(28px, 3.1vw, 43px);
  line-height: 1.12;
  letter-spacing: -.035em;
}
#page-dashboard .dashboard-overview h2 > span { color: var(--dashboard-blue); }
#page-dashboard .dashboard-overview-copy > p {
  max-width: 760px;
  margin: 13px 0 0;
  color: #496176;
  font-size: 14px;
  line-height: 1.75;
}
#page-dashboard .dashboard-quick-actions {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 9px;
  margin-top: 18px;
}
#page-dashboard .dashboard-quick-link.dental-page-nav-item {
  display: grid !important;
  grid-template-columns: auto minmax(0, 1fr) !important;
  gap: 2px 9px !important;
  align-items: center !important;
  min-height: 72px !important;
  padding: 11px 12px !important;
  border: 1px solid rgba(191,219,254,.95) !important;
  border-radius: 10px !important;
  background: rgba(255,255,255,.86) !important;
  color: #17324d !important;
  text-align: left !important;
  box-shadow: 0 8px 22px rgba(15,42,67,.055) !important;
}
#page-dashboard .dashboard-quick-link.dental-page-nav-item:hover {
  transform: translateY(-1px) !important;
  border-color: #60a5fa !important;
  background: #fff !important;
  box-shadow: 0 12px 24px rgba(37,99,235,.1) !important;
}
#page-dashboard .dashboard-quick-link > span {
  grid-row: 1 / span 2;
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: #dbeafe;
  color: #1d4ed8;
  font-size: 11px;
  font-weight: 900;
}
#page-dashboard .dashboard-quick-link > b {
  color: #17324d !important;
  font-size: 13px;
  line-height: 1.2;
}
#page-dashboard .dashboard-quick-link > small {
  overflow: hidden;
  color: #647b90 !important;
  font-size: 10px;
  line-height: 1.35;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#page-dashboard .dashboard-runtime-card {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  padding: 17px;
  border: 1px solid rgba(147,197,253,.24);
  border-radius: 13px;
  background: linear-gradient(145deg, #102a43, #123c5a);
  box-shadow: 0 18px 38px rgba(15,42,67,.16);
}
#page-dashboard .dashboard-runtime-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding-bottom: 13px;
  border-bottom: 1px solid rgba(255,255,255,.12);
}
#page-dashboard .dashboard-runtime-head > span {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: #fff !important;
  font-size: 13px;
  font-weight: 850;
}
#page-dashboard .dashboard-runtime-head i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 0 4px rgba(52,211,153,.13);
}
#page-dashboard .dashboard-runtime-head > b {
  color: #bae6fd !important;
  font-size: 10px;
}
#page-dashboard .dashboard-runtime-card dl {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  margin: 6px 0 0;
}
#page-dashboard .dashboard-runtime-card dl > div {
  min-width: 0;
  padding: 11px 8px 10px 0;
  border-bottom: 1px solid rgba(255,255,255,.09);
}
#page-dashboard .dashboard-runtime-card dl > div:nth-child(even) { padding-left: 12px; }
#page-dashboard .dashboard-runtime-card dt {
  color: #a9c4dc !important;
  font-size: 10px;
}
#page-dashboard .dashboard-runtime-card dd {
  margin: 4px 0 0;
  color: #fff !important;
  font-size: 13px;
  font-weight: 850;
}
#page-dashboard .dashboard-runtime-card dd.dashboard-runtime-alert { color: #fca5a5 !important; }
#page-dashboard .dashboard-runtime-foot {
  display: grid;
  gap: 3px;
  margin-top: auto;
  padding-top: 13px;
}
#page-dashboard .dashboard-runtime-foot > span { color: #a9c4dc !important; font-size: 10px; }
#page-dashboard .dashboard-runtime-foot > b { color: #e6f4ff !important; font-size: 12px; }
#page-dashboard .dashboard-history-link.dental-page-nav-item {
  justify-self: start;
  min-height: 0 !important;
  margin-top: 7px;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  color: #7dd3fc !important;
  font-size: 10px;
  box-shadow: none !important;
}
#page-dashboard .dashboard-history-link.dental-page-nav-item:hover {
  color: #fff !important;
  text-decoration: underline;
}
#page-dashboard .dashboard-section-title {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 18px;
  margin: 2px 1px -5px;
}
#page-dashboard .dashboard-section-title > div > span {
  color: #1d4ed8;
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .11em;
}
#page-dashboard .dashboard-section-title h3 {
  margin: 3px 0 0;
  color: #16324a;
  font-size: 20px;
  line-height: 1.25;
}
#page-dashboard .dashboard-section-title > p {
  max-width: 520px;
  margin: 0;
  color: #64748b;
  font-size: 11px;
  line-height: 1.5;
  text-align: right;
}
#page-dashboard .dashboard-kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
}
#page-dashboard .dashboard-kpi-card {
  --kpi-accent: var(--dashboard-blue);
  position: relative;
  min-width: 0;
  min-height: 166px;
  padding: 15px;
  overflow: hidden;
  border: 1px solid #dbe5ef;
  border-top: 3px solid var(--kpi-accent);
  border-radius: 12px;
  background: #fff;
}
#page-dashboard .dashboard-kpi-card::after {
  content: "";
  position: absolute;
  right: -32px;
  top: -42px;
  width: 106px;
  height: 106px;
  border-radius: 50%;
  background: color-mix(in srgb, var(--kpi-accent) 8%, transparent);
  pointer-events: none;
}
#page-dashboard .dashboard-kpi-card--cyan { --kpi-accent: var(--dashboard-cyan); }
#page-dashboard .dashboard-kpi-card--amber { --kpi-accent: var(--dashboard-amber); }
#page-dashboard .dashboard-kpi-card--teal { --kpi-accent: var(--dashboard-teal); }
#page-dashboard .dashboard-kpi-card header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}
#page-dashboard .dashboard-kpi-card header > span {
  display: grid;
  place-items: center;
  width: 27px;
  height: 27px;
  border-radius: 7px;
  background: color-mix(in srgb, var(--kpi-accent) 11%, white);
  color: var(--kpi-accent);
  font-size: 10px;
  font-weight: 900;
}
#page-dashboard .dashboard-kpi-card header > em {
  color: #718096;
  font-size: 10px;
  font-style: normal;
}
#page-dashboard .dashboard-kpi-card > strong {
  display: block;
  margin-top: 14px;
  color: var(--kpi-accent);
  font-size: clamp(27px, 2.3vw, 36px);
  line-height: 1;
  letter-spacing: -.035em;
}
#page-dashboard .dashboard-kpi-card h3 {
  margin: 8px 0 0;
  color: #20384f;
  font-size: 13px;
}
#page-dashboard .dashboard-kpi-card p {
  margin: 5px 0 0;
  color: #6b7f91;
  font-size: 10px;
  line-height: 1.5;
}
#page-dashboard .dashboard-operations-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, .92fr);
  gap: 10px;
  margin: 0;
}
#page-dashboard .dashboard-compact-panel {
  min-width: 0;
  overflow: hidden;
  border: 1px solid #dbe5ef !important;
  border-radius: 12px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-dashboard .dashboard-compact-panel > header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 59px;
  padding: 11px 14px;
  border-bottom: 1px solid #e7edf4;
  background: #f8fafc;
}
#page-dashboard .dashboard-compact-panel > header > div { display: grid; gap: 2px; }
#page-dashboard .dashboard-compact-panel > header span {
  color: #2563eb !important;
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .08em;
}
#page-dashboard .dashboard-compact-panel > header b {
  color: #1c3348 !important;
  font-size: 13px;
}
#page-dashboard .dashboard-compact-panel > header em {
  color: #718096 !important;
  font-size: 9px;
  font-style: normal;
}
#page-dashboard .dashboard-trend {
  display: flex;
  align-items: end;
  gap: 9px;
  height: 190px;
  padding: 24px 18px 13px;
}
#page-dashboard .dashboard-trend-bar {
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: end;
  align-items: center;
  min-width: 0;
  height: 100%;
  gap: 5px;
}
#page-dashboard .dashboard-trend-bar > b {
  color: #32506a;
  font-size: 10px;
}
#page-dashboard .dashboard-trend-bar > i {
  width: min(44px, 72%);
  min-height: 8px;
  border-radius: 6px 6px 2px 2px;
  background: linear-gradient(180deg, #60a5fa, #2563eb) !important;
}
#page-dashboard .dashboard-trend-bar > span {
  color: #718096;
  font-size: 9px;
  white-space: nowrap;
}
#page-dashboard .dashboard-empty-state {
  display: grid;
  place-items: center;
  align-self: center;
  width: 100%;
  gap: 5px;
  color: #64748b;
  text-align: center;
}
#page-dashboard .dashboard-empty-state b { color: #334155; font-size: 13px; }
#page-dashboard .dashboard-empty-state span { font-size: 10px; }
#page-dashboard .dashboard-anomaly-list {
  display: grid;
  gap: 0;
  max-height: 190px;
  margin: 0;
  padding: 2px 14px;
  overflow-y: auto;
  list-style: none;
}
#page-dashboard .dashboard-anomaly-list li {
  display: grid;
  grid-template-columns: 10px minmax(0, 1fr) auto;
  gap: 3px 9px;
  align-items: center;
  min-height: 58px;
  padding: 8px 0;
  border-bottom: 1px solid #edf2f7;
}
#page-dashboard .dashboard-anomaly-list li:last-child { border-bottom: 0; }
#page-dashboard .dashboard-anomaly-list li > div { min-width: 0; }
#page-dashboard .dashboard-anomaly-list li b {
  display: block;
  overflow: hidden;
  color: #243c52;
  font-size: 11px;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#page-dashboard .dashboard-anomaly-list li small {
  display: block;
  margin-top: 3px;
  overflow: hidden;
  color: #718096;
  font-size: 9px;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#page-dashboard .dashboard-anomaly-list li > em {
  padding: 4px 7px;
  border-radius: 999px;
  background: #fff7ed;
  color: #b45309;
  font-size: 9px;
  font-style: normal;
  font-weight: 800;
  white-space: nowrap;
}
#page-dashboard .dashboard-anomaly-list .status-dot {
  width: 8px;
  height: 8px;
  margin: 0;
  border-radius: 50%;
  background: #f59e0b;
}
#page-dashboard .dashboard-anomaly-list .status-dot.status-failed { background: #ef4444; }
#page-dashboard .dashboard-empty-row { grid-template-columns: 1fr !important; }
#page-dashboard .dashboard-empty-row div { text-align: center; }
#page-dashboard .dashboard-actions-row {
  justify-content: flex-end !important;
  align-items: center !important;
  gap: 8px !important;
  margin: 14px 0 17px !important;
  padding: 9px !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 10px !important;
  background: #f8fafc !important;
}
#page-dashboard .dashboard-actions-row > * {
  flex: 0 0 176px !important;
  width: auto !important;
}
#page-dashboard .dashboard-actions-row button { min-height: 40px !important; }
#page-dashboard .dashboard-refresh-action button,
#page-dashboard button.dashboard-refresh-action {
  border-color: #1d4ed8 !important;
  background: #2563eb !important;
  color: #fff !important;
}
#page-dashboard .dashboard-clear-action button,
#page-dashboard button.dashboard-clear-action {
  border-color: #fecaca !important;
  background: #fff !important;
  color: #b91c1c !important;
}
#page-dashboard .dashboard-chart-heading { margin: 0 1px 10px; }
#page-dashboard .dashboard-analytics-panel,
#page-dashboard .dashboard-status-panel {
  margin-bottom: 12px !important;
  overflow: hidden !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-dashboard .dashboard-chart-row {
  gap: 10px !important;
  margin: 0 0 10px !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
}
#page-dashboard .dashboard-chart-row:last-child { margin-bottom: 0 !important; }
#page-dashboard .dashboard-chart-row > * {
  min-width: 0 !important;
  padding: 8px !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  background: #fff !important;
}
#page-dashboard .dashboard-status-panel .markdown {
  overflow-x: auto;
}
#page-dashboard .dashboard-status-panel table { min-width: 820px; }
#page-dashboard .dashboard-status-panel .markdown:last-child {
  margin-top: 8px;
  padding: 10px 12px;
  border-radius: 8px;
  background: #f8fafc;
  color: #52667a;
}

body[data-dental-theme="dark"] #page-dashboard .dashboard-overview {
  border-color: #334155;
  background: linear-gradient(135deg, #0f2539, #102f49 60%, #123b45);
}
body[data-dental-theme="dark"] #page-dashboard .dashboard-overview h2,
body[data-dental-theme="dark"] #page-dashboard .dashboard-section-title h3 { color: #f8fafc; }
body[data-dental-theme="dark"] #page-dashboard .dashboard-overview-copy > p,
body[data-dental-theme="dark"] #page-dashboard .dashboard-section-title > p { color: #cbd5e1; }
body[data-dental-theme="dark"] #page-dashboard .dashboard-quick-link.dental-page-nav-item,
body[data-dental-theme="dark"] #page-dashboard .dashboard-kpi-card,
body[data-dental-theme="dark"] #page-dashboard .dashboard-compact-panel {
  border-color: #405268 !important;
  background: #111f30 !important;
}
body[data-dental-theme="dark"] #page-dashboard .dashboard-quick-link > b,
body[data-dental-theme="dark"] #page-dashboard .dashboard-kpi-card h3,
body[data-dental-theme="dark"] #page-dashboard .dashboard-compact-panel > header b,
body[data-dental-theme="dark"] #page-dashboard .dashboard-anomaly-list li b,
body[data-dental-theme="dark"] #page-dashboard .dashboard-empty-state b { color: #f1f5f9 !important; }
body[data-dental-theme="dark"] #page-dashboard .dashboard-quick-link > small,
body[data-dental-theme="dark"] #page-dashboard .dashboard-kpi-card p,
body[data-dental-theme="dark"] #page-dashboard .dashboard-anomaly-list li small,
body[data-dental-theme="dark"] #page-dashboard .dashboard-trend-bar > span { color: #aebed0 !important; }
body[data-dental-theme="dark"] #page-dashboard .dashboard-compact-panel > header {
  border-bottom-color: #334155;
  background: #16263a;
}
body[data-dental-theme="dark"] #page-dashboard .dashboard-trend-bar > b { color: #dbeafe; }
body[data-dental-theme="dark"] #page-dashboard .dashboard-actions-row,
body[data-dental-theme="dark"] #page-dashboard .dashboard-analytics-panel,
body[data-dental-theme="dark"] #page-dashboard .dashboard-status-panel,
body[data-dental-theme="dark"] #page-dashboard .dashboard-chart-row > * {
  border-color: #405268 !important;
  background: #111f30 !important;
}

@media (max-width: 1180px) {
  #page-dashboard .dashboard-overview { grid-template-columns: minmax(0, 1.2fr) minmax(280px, .8fr); }
  #page-dashboard .dashboard-quick-actions { grid-template-columns: 1fr; }
  #page-dashboard .dashboard-quick-link.dental-page-nav-item { min-height: 58px !important; }
  #page-dashboard .dashboard-kpi-grid { grid-template-columns: 1fr 1fr; }
  #page-dashboard .dashboard-operations-grid { grid-template-columns: 1fr; }
}
@media (max-width: 820px) {
  #page-dashboard .dashboard-overview { grid-template-columns: 1fr; padding: 18px; }
  #page-dashboard .dashboard-quick-actions { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  #page-dashboard .dashboard-section-title { align-items: start; flex-direction: column; gap: 5px; }
  #page-dashboard .dashboard-section-title > p { text-align: left; }
}
@media (max-width: 620px) {
  #page-dashboard .dashboard-quick-actions,
  #page-dashboard .dashboard-kpi-grid { grid-template-columns: 1fr; }
  #page-dashboard .dashboard-actions-row { display: grid !important; grid-template-columns: 1fr 1fr; }
  #page-dashboard .dashboard-actions-row > * { width: 100% !important; min-width: 0 !important; }
  #page-dashboard .dashboard-anomaly-list li { grid-template-columns: 10px minmax(0, 1fr); }
  #page-dashboard .dashboard-anomaly-list li > em { grid-column: 2; justify-self: start; }
}
@media (max-width: 460px) {
  #page-dashboard .dashboard-overview { padding: 15px; }
  #page-dashboard .dashboard-overview h2 { font-size: 27px; }
  #page-dashboard .dashboard-runtime-card dl { grid-template-columns: 1fr; }
  #page-dashboard .dashboard-runtime-card dl > div:nth-child(even) { padding-left: 0; }
  #page-dashboard .dashboard-actions-row { grid-template-columns: 1fr; }
}

/* History and reports */
#page-history .history-summary-card,
#page-report .report-recent-list,
#page-report .report-preview-panel {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-history .gallery,
#page-report .gallery { border-radius: var(--radius-panel) !important; overflow: hidden !important; }
#page-history .history-action-row,
#page-history .history-filter-row,
#page-report .report-controls-row,
#page-report .report-download-row { padding: 10px !important; }
#page-report .report-cover-mini { border-radius: 6px !important; background: var(--surface-selected) !important; }

/* Assistant: stronger message hierarchy without changing its custom events. */
#page-assistant .native-ai-assistant {
  border: 1px solid var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-top {
  border: 0 !important;
  border-bottom: 1px solid var(--border-soft) !important;
  border-radius: 0 !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-control,
#page-assistant .native-ai-messages,
#page-assistant .native-ai-composer,
#page-assistant .native-ai-empty-card,
#page-assistant .native-ai-msg.assistant .native-ai-bubble {
  border-color: var(--border-soft) !important;
  border-radius: var(--radius-panel) !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-workbench { gap: 10px !important; }
#page-assistant .native-ai-msg.user .native-ai-bubble {
  border-radius: 8px 8px 2px 8px !important;
  background: var(--action) !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-assistant button.native-ai-suggestion {
  border-color: var(--border-soft) !important;
  border-radius: 7px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-assistant button.native-ai-suggestion:hover {
  transform: none !important;
  border-color: #93c5fd !important;
  background: var(--surface-selected) !important;
}
#page-assistant .native-ai-export-btn {
  border-color: var(--border-soft) !important;
  border-radius: 7px !important;
  background: var(--surface-subtle) !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-input-row textarea {
  border-color: var(--border-strong) !important;
  border-radius: 8px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-heading { border-radius: 4px !important; }

* { scrollbar-color: #b8c2cf transparent; scrollbar-width: thin; }
.gradio-container button:focus-visible,
.dental-page-nav-item:focus-visible,
.native-ai-suggestion:focus-visible,
.native-ai-export-btn:focus-visible {
  outline: 3px solid rgba(37, 99, 235, 0.28) !important;
  outline-offset: 2px !important;
}

@media (max-width: 900px) {
  .app-hero { padding: 15px 16px !important; }
  .dental-page-nav { border-radius: 8px !important; }
  .dental-nav-items { gap: 4px !important; }
  .dental-page-nav-item { min-height: 42px !important; }
  .dental-page { padding: 7px !important; }
  #page-assistant .native-ai-top { padding: 16px !important; }
}

@media (max-width: 560px) {
  .gradio-container { padding-inline: 6px !important; }
  .app-hero h1 { font-size: 25px !important; }
  .app-hero p { font-size: 13px !important; }
  .dental-nav-items { grid-template-columns: 1fr !important; }
  .section-note { padding: 10px 12px !important; }
  .detection-workflow li { padding: 5px 2px !important; }
  .gradio-container table { min-width: 680px !important; }
}
"""
