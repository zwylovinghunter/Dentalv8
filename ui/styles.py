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
.detection-completion-marker,
#compare-progress:has(.detection-completion-marker) {
  display: none !important;
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
.dental-comparison-fullscreen-layer {
  position: fixed;
  inset: 0;
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  padding: 68px 24px 30px;
  background: rgba(2,6,23,0.92);
  backdrop-filter: blur(14px);
  z-index: 10050;
  color: #f8fafc;
}
.dental-comparison-fullscreen-layer.visible { display: flex; }
.dental-comparison-fullscreen-toolbar {
  position: absolute;
  top: 18px;
  left: 24px;
  right: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  color: #e2e8f0;
  font-size: 16px;
  font-weight: 700;
}
.dental-comparison-fullscreen-close {
  width: 42px;
  height: 42px;
  border: 1px solid rgba(255,255,255,0.28);
  border-radius: 999px;
  background: rgba(15,23,42,0.76);
  color: #fff;
  cursor: pointer;
  font-size: 26px;
  line-height: 1;
}
.dental-comparison-fullscreen-close:hover {
  background: rgba(37,99,235,0.9);
}
.dental-comparison-fullscreen-frame {
  --compare-split: 50%;
  position: relative;
  width: min(94vw, 1720px);
  height: min(80vh, 980px);
  min-height: 280px;
  overflow: hidden;
  border: 1px solid rgba(148,163,184,0.45);
  border-radius: 14px;
  background: #020617;
  box-shadow: 0 28px 80px rgba(0,0,0,0.5);
  touch-action: none;
  cursor: ew-resize;
}
.dental-comparison-fullscreen-frame > img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  user-select: none;
  pointer-events: none;
}
.dental-comparison-fullscreen-result {
  clip-path: inset(0 0 0 var(--compare-split));
}
.dental-comparison-fullscreen-divider {
  position: absolute;
  top: 0;
  bottom: 0;
  left: calc(var(--compare-split) - 1px);
  width: 2px;
  background: #fff;
  box-shadow: 0 0 0 1px rgba(15,23,42,0.28), 0 0 16px rgba(255,255,255,0.65);
  pointer-events: none;
}
.dental-comparison-fullscreen-divider span {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 34px;
  height: 34px;
  transform: translate(-50%, -50%);
  border: 2px solid #fff;
  border-radius: 999px;
  background: rgba(37,99,235,0.9);
  box-shadow: 0 4px 14px rgba(0,0,0,0.34);
}
.dental-comparison-fullscreen-range {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 16px;
  width: calc(100% - 36px);
  accent-color: #60a5fa;
  opacity: 0.9;
  cursor: ew-resize;
}
.dental-comparison-fullscreen-hint {
  color: #cbd5e1;
  font-size: 13px;
  text-align: center;
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
  position: fixed;
  z-index: 10000;
  display: none;
  grid-template-columns: 190px minmax(320px, 1fr);
  width: min(720px, calc(100vw - 24px));
  margin: 0;
  padding: 9px;
  overflow: hidden;
  border: 1px solid rgba(148, 184, 204, .72);
  border-radius: 16px;
  background: rgba(255, 255, 255, .98);
  color: #18364c;
  box-shadow: 0 20px 48px rgba(15, 42, 60, .2), 0 2px 8px rgba(15, 42, 60, .08);
  backdrop-filter: blur(14px);
  box-sizing: border-box;
  transform-origin: top left;
  animation: ask-ai-selection-enter .16s ease-out;
}
#ask-ai-selection-popover.visible { display: grid; }
.ask-ai-selection-brand {
  position: relative;
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr);
  align-items: center;
  gap: 10px;
  min-width: 0;
  padding: 10px 12px;
  overflow: hidden;
  border-radius: 11px;
  background: linear-gradient(135deg, #0c2f47, #0f6070);
  color: #fff;
}
.ask-ai-selection-brand::after {
  content: "";
  position: absolute;
  right: -18px;
  bottom: -28px;
  width: 78px;
  height: 78px;
  border: 14px solid rgba(255, 255, 255, .06);
  border-radius: 50%;
}
.ask-ai-selection-mark {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  border: 1px solid rgba(153, 246, 228, .26);
  border-radius: 10px;
  background: rgba(255, 255, 255, .1);
  color: #a7f3e6;
}
.ask-ai-selection-mark svg { width: 23px; height: 23px; fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.ask-ai-selection-brand-copy { position: relative; z-index: 1; display: grid; min-width: 0; gap: 2px; }
.ask-ai-selection-brand-copy strong { overflow: hidden; color: #fff; font-size: 13px; font-weight: 900; text-overflow: ellipsis; white-space: nowrap; }
.ask-ai-selection-brand-copy small { color: #b9d7df; font-size: 10px; font-weight: 650; }
.ask-ai-selection-form {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: stretch;
  min-width: 0;
  margin-left: 9px;
  padding: 4px;
  border: 1px solid #cbdbe5;
  border-radius: 11px;
  background: #f7fafc;
  box-shadow: inset 0 1px 2px rgba(15, 42, 60, .035);
  transition: border-color .16s ease, box-shadow .16s ease, background .16s ease;
}
.ask-ai-selection-form:focus-within {
  border-color: #29a6b2;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(20, 184, 166, .12), inset 0 1px 2px rgba(15, 42, 60, .025);
}
#ask-ai-selection-question {
  width: 100%;
  min-width: 0;
  min-height: 44px;
  margin: 0;
  padding: 0 12px;
  border: 0;
  outline: 0;
  background: transparent;
  color: #152f43;
  font: inherit;
  font-size: 13px;
  line-height: 1.45;
  box-shadow: none;
  box-sizing: border-box;
}
#ask-ai-selection-question::placeholder { color: #91a2b2; opacity: 1; }
#ask-ai-selection-question[aria-invalid="true"]::placeholder { color: #c2413a; }
#ask-ai-selection-send {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-width: 84px;
  min-height: 44px;
  margin: 0;
  padding: 0 14px;
  border: 1px solid #0d536f;
  border-radius: 8px;
  background: linear-gradient(135deg, #103f60, #0f6b78);
  color: #fff;
  font-size: 12px;
  font-weight: 850;
  cursor: pointer;
  box-shadow: 0 7px 16px rgba(15, 79, 112, .18);
  transition: transform .15s ease, box-shadow .15s ease, opacity .15s ease;
}
#ask-ai-selection-send svg { width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
#ask-ai-selection-send:hover:not(:disabled) { transform: translateY(-1px); box-shadow: 0 10px 20px rgba(15, 79, 112, .23); }
#ask-ai-selection-send:focus-visible,
.ask-ai-selection-close:focus-visible {
  outline: 3px solid rgba(14, 165, 233, .22);
  outline-offset: 2px;
}
#ask-ai-selection-send:disabled { border-color: #cbd5dd; background: #e7edf1; color: #91a0ac; cursor: not-allowed; box-shadow: none; }
.ask-ai-selection-context {
  position: relative;
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 8px;
  min-width: 0;
  min-height: 36px;
  margin-top: 7px;
  padding: 6px 44px 3px 5px;
  color: #63798a;
}
.ask-ai-selection-context-label {
  padding: 3px 7px;
  border: 1px solid #c7e6e2;
  border-radius: 999px;
  background: #eefbf8;
  color: #0f766e;
  font-size: 10px;
  font-weight: 850;
  white-space: nowrap;
}
.ask-ai-selection-context p {
  min-width: 0;
  margin: 0;
  overflow: hidden;
  color: #63798a;
  font-size: 11px;
  line-height: 1.45;
  text-overflow: ellipsis;
  white-space: nowrap;
}
#ask-ai-selection-feedback { color: #c2413a; font-size: 10px; font-weight: 750; white-space: nowrap; }
.ask-ai-selection-close {
  position: absolute;
  right: 0;
  bottom: 0;
  display: grid;
  place-items: center;
  width: 40px;
  height: 36px;
  padding: 0;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: #8293a0;
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
}
.ask-ai-selection-close:hover { background: #edf3f6; color: #304c60; }
#ask-ai-selection-popover.has-error .ask-ai-selection-form { border-color: #e16b61; box-shadow: 0 0 0 3px rgba(225, 107, 97, .11); }
@keyframes ask-ai-selection-enter {
  from { opacity: 0; transform: translateY(-4px) scale(.985); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  #ask-ai-selection-popover { animation: none; }
}
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
  #ask-ai-selection-popover {
    grid-template-columns: 1fr;
    width: calc(100vw - 20px);
    padding: 8px;
    border-radius: 14px;
  }
  .ask-ai-selection-brand {
    grid-template-columns: 30px minmax(0, 1fr);
    min-height: 44px;
    padding: 7px 9px;
  }
  .ask-ai-selection-mark { width: 30px; height: 30px; border-radius: 8px; }
  .ask-ai-selection-mark svg { width: 19px; height: 19px; }
  .ask-ai-selection-brand-copy { display: flex; align-items: baseline; gap: 7px; }
  .ask-ai-selection-form { grid-template-columns: minmax(0, 1fr) auto; margin: 8px 0 0; }
  #ask-ai-selection-question { font-size: 16px; }
  #ask-ai-selection-send { min-width: 74px; padding-inline: 11px; }
  .ask-ai-selection-context { margin-top: 5px; }
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

/* Detection workspace layout and dropdown positioning.
   Gradio renders dropdown menus as fixed-position descendants. A filtered
   ancestor creates a new fixed-position containing block and offsets the menu. */
#page-image .detection-controls.sticky-actionbar,
#page-compare .detection-controls.sticky-actionbar,
#page-batch .detection-controls.sticky-actionbar {
  position: static !important;
  inset: auto !important;
  overflow: visible !important;
  transform: none !important;
  filter: none !important;
  -webkit-backdrop-filter: none !important;
  backdrop-filter: none !important;
  contain: none !important;
  will-change: auto !important;
}
.gradio-container ul.options[role="listbox"] {
  z-index: 10050 !important;
}

#page-image .detection-setup-grid,
#page-compare .detection-setup-grid,
#page-batch .detection-setup-grid {
  grid-template-columns: minmax(0, .96fr) minmax(0, 1.04fr) !important;
  align-items: stretch !important;
  gap: 14px !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  margin: 0 0 18px !important;
  padding: 12px !important;
  overflow: visible !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 12px !important;
  background: #f4f7fb !important;
  box-shadow: none !important;
}
#page-image .detection-setup-grid > .detection-upload-panel,
#page-image .detection-setup-grid > .detection-parameter-panel,
#page-compare .detection-setup-grid > .detection-upload-panel,
#page-compare .detection-setup-grid > .detection-parameter-panel,
#page-batch .detection-setup-grid > .detection-upload-panel,
#page-batch .detection-setup-grid > .detection-parameter-panel {
  display: flex !important;
  flex-direction: column !important;
  align-self: stretch !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  padding: 14px !important;
  overflow: visible !important;
  border: 1px solid #d8e2ee !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: 0 5px 16px rgba(15, 23, 42, .045) !important;
}
#page-image .detection-panel-heading,
#page-compare .detection-panel-heading,
#page-batch .detection-panel-heading {
  flex: 0 0 auto !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  margin: 0 0 11px !important;
  padding: 0 0 10px !important;
  border-bottom: 1px solid #e7edf4 !important;
  background: transparent !important;
}
#page-image .detection-panel-heading > *,
#page-image .detection-panel-heading .prose,
#page-image .detection-panel-heading .markdown,
#page-compare .detection-panel-heading > *,
#page-compare .detection-panel-heading .prose,
#page-compare .detection-panel-heading .markdown,
#page-batch .detection-panel-heading > *,
#page-batch .detection-panel-heading .prose,
#page-batch .detection-panel-heading .markdown {
  height: auto !important;
  min-height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
}
#page-image .detection-panel-heading h3,
#page-compare .detection-panel-heading h3,
#page-batch .detection-panel-heading h3 {
  margin: 0 !important;
  color: #172033 !important;
  font-size: 18px !important;
  line-height: 1.35 !important;
}
#page-image .detection-stage-heading,
#page-compare .detection-stage-heading,
#page-batch .detection-stage-heading {
  margin: 4px 0 12px !important;
  padding: 11px 14px !important;
  border: 1px solid #dbe5ef !important;
  border-left: 4px solid #2563eb !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
}
#page-image .detection-stage-heading h3,
#page-compare .detection-stage-heading h3,
#page-batch .detection-stage-heading h3 {
  margin: 0 !important;
  color: #1e3a5f !important;
  font-size: 17px !important;
}

#page-image #single-upload,
#page-compare #compare-upload,
#page-batch .batch-upload-composite {
  flex: 1 1 320px !important;
  width: 100% !important;
  height: auto !important;
  min-height: 300px !important;
  max-height: none !important;
}
#page-image #single-upload > *,
#page-image #single-upload .image-container,
#page-image #single-upload .upload-container,
#page-compare #compare-upload > *,
#page-compare #compare-upload .image-container,
#page-compare #compare-upload .upload-container {
  height: 100% !important;
  min-height: 0 !important;
  max-height: none !important;
}
#page-batch .batch-upload-composite,
#page-batch .batch-upload-composite > .styler {
  display: flex !important;
  flex-direction: column !important;
  width: 100% !important;
  height: auto !important;
  min-height: 300px !important;
  max-height: none !important;
  overflow: hidden !important;
}
#page-batch .batch-upload-composite > .styler {
  flex: 1 1 auto !important;
  height: 100% !important;
  min-height: 0 !important;
}
#page-batch .batch-upload-composite #batch-upload {
  flex: 1 1 auto !important;
  width: 100% !important;
  height: auto !important;
  min-height: 110px !important;
  max-height: none !important;
}
#page-batch .batch-upload-composite #batch-upload .wrap,
#page-batch .batch-upload-composite #batch-upload .upload-container {
  flex: 1 1 auto !important;
  width: 100% !important;
  height: 100% !important;
  min-height: 0 !important;
  max-height: none !important;
}
#page-batch .batch-upload-composite #batch-upload .file-preview,
#page-batch .batch-upload-composite #batch-upload .file-preview-holder {
  flex: 0 1 auto !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: min(240px, 42%) !important;
}
#page-batch .batch-upload-composite:has(#batch-upload-preview) #batch-upload {
  flex: 0 0 88px !important;
  height: 88px !important;
  min-height: 88px !important;
  max-height: 88px !important;
}
#page-batch .batch-upload-composite #batch-upload-preview {
  flex: 1 1 220px !important;
  width: 100% !important;
  height: auto !important;
  min-height: 220px !important;
  max-height: none !important;
}

#page-image .detection-controls,
#page-image .detection-controls > .styler,
#page-compare .detection-controls,
#page-compare .detection-controls > .styler,
#page-batch .detection-controls,
#page-batch .detection-controls > .styler {
  display: flex !important;
  flex: 1 1 auto !important;
  flex-direction: column !important;
  width: 100% !important;
  min-width: 0 !important;
  min-height: 0 !important;
  overflow: visible !important;
}
#page-image #single-run,
#page-compare #compare-run,
#page-batch #batch-run {
  flex: 0 0 auto !important;
  width: 100% !important;
  margin-top: auto !important;
  padding-top: 9px !important;
}
#page-image .result-filter-bar {
  display: grid !important;
  grid-template-columns: minmax(220px, 1.35fr) repeat(3, minmax(150px, 1fr)) !important;
  align-items: end !important;
  gap: 10px !important;
  padding: 10px !important;
}
#page-image .result-filter-bar > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: minmax(220px, 1.35fr) repeat(3, minmax(150px, 1fr)) !important;
  align-items: end !important;
  gap: 10px !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-image .result-filter-bar > .form > * {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
}
#page-image .result-filter-bar > *,
#page-image .linked-region-row > *,
#page-compare .linked-region-row > *,
#page-batch .linked-region-row > * {
  width: 100% !important;
  min-width: 0 !important;
}
#page-image .linked-region-row,
#page-compare .linked-region-row,
#page-batch .linked-region-row {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: stretch !important;
  gap: 12px !important;
}

@media (max-width: 900px) {
  #page-image .detection-setup-grid,
  #page-compare .detection-setup-grid,
  #page-batch .detection-setup-grid {
    grid-template-columns: 1fr !important;
    padding: 8px !important;
  }
  #page-image #single-upload,
  #page-compare #compare-upload,
  #page-batch .batch-upload-composite {
    flex: none !important;
    height: 300px !important;
    min-height: 300px !important;
    max-height: 300px !important;
  }
  #page-image .result-filter-bar {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
  #page-image .result-filter-bar > .form {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}
@media (max-width: 560px) {
  #page-image .result-filter-bar,
  #page-image .result-filter-bar > .form,
  #page-image .linked-region-row,
  #page-compare .linked-region-row,
  #page-batch .linked-region-row {
    grid-template-columns: 1fr !important;
  }
}

/* Detection workspace v3: shared information hierarchy, denser workbench and
   result layouts. These rules intentionally affect layout only. */
#page-image,
#page-compare,
#page-batch {
  padding: 12px !important;
}
.detection-page-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: center;
  gap: 24px;
  margin: 0 0 12px;
  padding: 20px 22px;
  overflow: hidden;
  border: 1px solid #d7e3f1;
  border-radius: 12px;
  background:
    radial-gradient(circle at 92% 0%, rgba(37, 99, 235, .11), transparent 34%),
    linear-gradient(135deg, #f8fbff 0%, #ffffff 58%, #f7fafc 100%);
}
.detection-page-hero-copy { min-width: 0; }
.detection-page-hero-copy small {
  display: block;
  margin-bottom: 5px;
  color: #2563eb;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .09em;
}
.detection-page-hero-copy h2 {
  margin: 0;
  color: #10213a;
  font-size: clamp(24px, 2vw, 31px);
  line-height: 1.2;
}
.detection-page-hero-copy p {
  max-width: 840px;
  margin: 8px 0 0;
  color: #5b6b80;
  font-size: 14px;
  line-height: 1.7;
}
.detection-page-badges {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  gap: 8px;
  justify-content: end;
}
.detection-page-badges span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 30px;
  padding: 5px 10px;
  border: 1px solid #cfe0f6;
  border-radius: 7px;
  background: rgba(255, 255, 255, .86);
  color: #33506f;
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
}
.detection-workflow-shell {
  margin: 0 0 12px !important;
  padding: 6px !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 10px !important;
  background: #f8fafc !important;
  box-shadow: none !important;
}
.detection-workflow-shell .detection-workflow {
  margin: 0 !important;
  border: 0 !important;
  background: transparent !important;
}

#page-image .detection-workbench,
#page-compare .detection-workbench,
#page-batch .detection-workbench {
  display: grid !important;
  grid-template-columns: minmax(350px, 5fr) minmax(500px, 7fr) !important;
  align-items: stretch !important;
  gap: 14px !important;
  margin: 0 0 14px !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-image .detection-workbench > .detection-upload-panel,
#page-image .detection-workbench > .detection-parameter-panel,
#page-compare .detection-workbench > .detection-upload-panel,
#page-compare .detection-workbench > .detection-parameter-panel,
#page-batch .detection-workbench > .detection-upload-panel,
#page-batch .detection-workbench > .detection-parameter-panel {
  padding: 16px !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 8px 22px rgba(15, 23, 42, .05) !important;
}
.detection-model-preset-row,
.detection-threshold-row {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: end !important;
  gap: 12px !important;
  width: 100% !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.detection-model-preset-row > .form,
.detection-threshold-row > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 12px !important;
  width: 100% !important;
  min-width: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
}
.detection-model-preset-row > *,
.detection-model-preset-row > .form > *,
.detection-threshold-row > *,
.detection-threshold-row > .form > * {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
}

.detection-results-shell {
  width: 100% !important;
  margin: 0 !important;
  padding: 14px !important;
  overflow: visible !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 12px !important;
  background: #f7f9fc !important;
  box-shadow: none !important;
}
.detection-results-shell > .styler {
  overflow: visible !important;
}
.detection-results-shell .detection-stage-heading {
  margin: 0 0 12px !important;
  background: #fff !important;
}
.detection-result-overview {
  width: 100% !important;
  min-height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.single-result-overview {
  display: grid !important;
  grid-template-columns: minmax(0, 2fr) minmax(290px, 1fr) !important;
  align-items: start !important;
  gap: 14px !important;
}
.single-result-overview > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: minmax(0, 2fr) minmax(290px, 1fr) !important;
  align-items: start !important;
  gap: 14px !important;
  width: 100% !important;
}
.single-result-visual,
.single-result-insights {
  width: 100% !important;
  min-width: 0 !important;
  min-height: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
.single-result-visual .detection-result-stack {
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-image .single-result-visual .result-compare-slider {
  height: clamp(430px, 48vw, 650px) !important;
  min-height: 430px !important;
  max-height: 650px !important;
}
#page-image .single-result-insights .result-cards {
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 8px !important;
  margin: 0 0 10px !important;
}
#page-image .single-result-insights .result-card {
  min-height: 72px !important;
  padding: 10px !important;
}
#page-image .single-result-insights .result-card span {
  overflow-wrap: anywhere;
  font-size: 15px !important;
}
#page-image .single-result-insights .det-explain {
  max-height: 430px !important;
  margin: 0 !important;
  padding: 14px !important;
  overflow-y: auto !important;
  border: 1px solid #dbe5ef !important;
  background: #fff !important;
}
.structured-result-panel,
.compare-analysis-panel {
  width: 100% !important;
  margin: 12px 0 0 !important;
  padding: 12px !important;
  overflow: visible !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: none !important;
}
.structured-result-panel .result-filter-bar {
  margin-top: 0 !important;
}

#page-compare .compare-model-grid {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 12px !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
}
#page-compare .compare-model-grid > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 12px !important;
  width: 100% !important;
}
#page-compare .compare-model-card {
  width: 100% !important;
  min-width: 0 !important;
  padding: 10px !important;
  overflow: hidden !important;
  border: 1px solid #dbe5ef !important;
  border-top: 3px solid #64748b !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: 0 7px 20px rgba(15, 23, 42, .045) !important;
}
#page-compare .compare-model-precision { border-top-color: #2563eb !important; }
#page-compare .compare-model-recall { border-top-color: #0f9f78 !important; }
#page-compare .compare-model-card .model-tag {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  gap: 3px !important;
  width: 100% !important;
  margin: 0 0 8px !important;
  padding: 5px 3px 9px !important;
  border: 0 !important;
  border-bottom: 1px solid #e6edf5 !important;
  border-radius: 0 !important;
  background: transparent !important;
  color: #20344d !important;
}
#page-compare .compare-model-card .model-tag b {
  font-size: 14px;
  line-height: 1.35;
}
#page-compare .compare-model-card .model-tag span {
  color: #718096;
  font-size: 12px;
  font-weight: 600;
}
#page-compare .compare-model-card .result-compare-slider {
  height: clamp(300px, 28vw, 420px) !important;
  min-height: 300px !important;
  max-height: 420px !important;
  border: 0 !important;
  border-radius: 8px !important;
}
.compare-summary-panel {
  margin-top: 10px !important;
  padding: 14px !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
}

.batch-review-grid {
  display: grid !important;
  grid-template-columns: minmax(290px, 4fr) minmax(0, 8fr) !important;
  align-items: start !important;
  gap: 14px !important;
}
.batch-review-grid > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: minmax(290px, 4fr) minmax(0, 8fr) !important;
  align-items: start !important;
  gap: 14px !important;
  width: 100% !important;
}
.batch-result-sidebar,
.batch-result-main {
  width: 100% !important;
  min-width: 0 !important;
  min-height: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
.batch-result-sidebar > * {
  margin-bottom: 10px !important;
}
#page-batch .batch-result-sidebar .batch-task-panel,
#page-batch .batch-result-sidebar #batch-result-preview-gallery,
#page-batch .batch-result-sidebar .batch-retry-panel {
  border: 1px solid #dbe5ef !important;
  border-radius: 9px !important;
  background: #fff !important;
}
#page-batch .batch-result-sidebar #batch-result-preview-gallery {
  height: min(360px, 42vh) !important;
  min-height: 260px !important;
}
#page-batch .batch-result-main #batch-result-slider {
  height: clamp(430px, 48vw, 650px) !important;
  min-height: 430px !important;
  max-height: 650px !important;
  margin: 0 0 10px !important;
}
#page-batch .batch-result-main .det-explain {
  max-height: 320px !important;
  margin: 0 0 10px !important;
  overflow-y: auto !important;
}

.detection-support-grid {
  display: grid !important;
  grid-template-columns: minmax(0, 7fr) minmax(300px, 5fr) !important;
  align-items: start !important;
  gap: 12px !important;
  width: 100% !important;
  margin: 12px 0 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.detection-support-grid > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: minmax(0, 7fr) minmax(300px, 5fr) !important;
  align-items: start !important;
  gap: 12px !important;
  width: 100% !important;
}
.detection-support-primary,
.detection-support-secondary {
  width: 100% !important;
  min-width: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
.detection-support-primary > .accordion,
.detection-support-secondary > .accordion {
  margin: 0 !important;
}
.detection-support-secondary .report-download-row {
  display: grid !important;
  grid-template-columns: 1fr !important;
}
.detection-support-grid.detection-support-review-only,
.detection-support-grid.detection-support-review-only > .form {
  grid-template-columns: minmax(0, 1fr) !important;
}

.detection-report-panel {
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 16px !important;
  overflow: visible !important;
  border: 1px solid #dbe5ef !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-image .detection-report-panel,
#page-compare .detection-report-panel,
#page-batch .detection-report-panel {
  display: block !important;
  grid-template-columns: minmax(0, 1fr) !important;
}
#page-image .detection-report-panel .block,
#page-image .detection-report-panel .form,
#page-compare .detection-report-panel .block,
#page-compare .detection-report-panel .form,
#page-batch .detection-report-panel .block,
#page-batch .detection-report-panel .form {
  grid-template-columns: minmax(0, 1fr) !important;
  min-width: 0 !important;
  max-width: none !important;
}
#page-image .detection-report-panel .report-generation-controls,
#page-image .detection-report-panel .report-generation-controls > .form,
#page-compare .detection-report-panel .report-generation-controls,
#page-compare .detection-report-panel .report-generation-controls > .form {
  display: grid !important;
  grid-template-columns: minmax(220px, 1fr) minmax(220px, .7fr) !important;
  align-items: end !important;
  gap: 12px !important;
  width: 100% !important;
  margin: 0 0 12px !important;
}
.detection-report-panel .detection-progress-state {
  position: relative !important;
  top: auto !important;
  z-index: 1 !important;
  margin: 0 0 12px !important;
}
#page-image .detection-report-panel .report-download-row,
#page-image .detection-report-panel .report-download-row > .form,
#page-compare .detection-report-panel .report-download-row,
#page-compare .detection-report-panel .report-download-row > .form {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 10px !important;
  width: 100% !important;
}
#page-batch .detection-report-panel .report-download-row,
#page-batch .detection-report-panel .report-download-row > .form {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 10px !important;
  width: 100% !important;
}

@media (max-width: 1280px) {
  #page-compare .compare-model-grid,
  #page-compare .compare-model-grid > .form {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
  #page-compare .compare-model-recall {
    grid-column: 1 / -1 !important;
  }
  #page-compare .compare-model-recall .result-compare-slider {
    height: clamp(340px, 42vw, 480px) !important;
    max-height: 480px !important;
  }
}
@media (max-width: 1080px) {
  #page-image .detection-workbench,
  #page-compare .detection-workbench,
  #page-batch .detection-workbench,
  .single-result-overview,
  .single-result-overview > .form,
  .batch-review-grid,
  .batch-review-grid > .form,
  .detection-support-grid,
  .detection-support-grid > .form {
    grid-template-columns: 1fr !important;
  }
  .single-result-insights {
    display: grid !important;
    grid-template-columns: minmax(280px, .8fr) minmax(0, 1.2fr) !important;
    gap: 12px !important;
  }
  .detection-support-primary,
  .detection-support-secondary {
    grid-column: 1 !important;
  }
}
@media (max-width: 760px) {
  #page-image,
  #page-compare,
  #page-batch {
    padding: 7px !important;
  }
  .detection-page-hero {
    grid-template-columns: 1fr;
    gap: 14px;
    padding: 16px;
  }
  .detection-page-badges {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    justify-content: stretch;
  }
  .detection-page-badges span { white-space: normal; text-align: center; }
  .detection-results-shell { padding: 8px !important; }
  .detection-model-preset-row,
  .detection-model-preset-row > .form,
  .detection-threshold-row,
  .detection-threshold-row > .form,
  .single-result-insights,
  #page-compare .compare-model-grid,
  #page-compare .compare-model-grid > .form {
    grid-template-columns: 1fr !important;
  }
  #page-image .detection-report-panel .report-generation-controls,
  #page-image .detection-report-panel .report-generation-controls > .form,
  #page-compare .detection-report-panel .report-generation-controls,
  #page-compare .detection-report-panel .report-generation-controls > .form,
  #page-image .detection-report-panel .report-download-row,
  #page-image .detection-report-panel .report-download-row > .form,
  #page-compare .detection-report-panel .report-download-row,
  #page-compare .detection-report-panel .report-download-row > .form,
  #page-batch .detection-report-panel .report-download-row,
  #page-batch .detection-report-panel .report-download-row > .form {
    grid-template-columns: 1fr !important;
  }
  #page-compare .compare-model-recall { grid-column: 1 !important; }
  #page-image .single-result-visual .result-compare-slider,
  #page-batch .batch-result-main #batch-result-slider {
    height: 360px !important;
    min-height: 320px !important;
    max-height: 420px !important;
  }
  #page-compare .compare-model-card .result-compare-slider,
  #page-compare .compare-model-recall .result-compare-slider {
    height: 340px !important;
    min-height: 300px !important;
    max-height: 380px !important;
  }
}

/* Result tabs: the result workspace is hidden before a run and becomes a
   single-panel answer view after the streamed job settles. */
.detection-results-shell.detection-before-run {
  display: none !important;
}
.detection-results-shell.detection-running .detection-result-tabs,
.detection-results-shell.detection-running .detection-result-panel {
  display: none !important;
}
.detection-results-shell .detection-result-tabs[hidden] {
  display: none !important;
}
.detection-result-tabs {
  display: block;
  width: 100%;
  margin: 0 0 14px;
  padding: 9px;
  overflow: hidden;
  border: 1px solid #d7e3f0;
  border-radius: 13px;
  background: linear-gradient(135deg, #f8fbff 0%, #ffffff 62%, #fffaf5 100%);
  box-shadow: 0 8px 22px rgba(15, 23, 42, .055);
}

/* Compact parameter composition: the model consumes one full row and the
   three presets share the next row, avoiding the empty lower-left half. */
#page-image .detection-model-preset-row,
#page-image .detection-model-preset-row > .form {
  grid-template-columns: 1fr !important;
  align-items: start !important;
  gap: 10px !important;
}
#page-image .threshold-preset-control .wrap {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  align-items: stretch !important;
  gap: 8px !important;
  width: 100% !important;
}
#page-image .threshold-preset-control .wrap > label {
  display: flex !important;
  align-items: center !important;
  width: 100% !important;
  min-width: 0 !important;
  min-height: 42px !important;
  margin: 0 !important;
  padding: 8px 10px !important;
  white-space: normal !important;
}
.visual-option-grid,
.visual-option-grid > .form {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: end !important;
  gap: 10px 12px !important;
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.visual-option-grid > *,
.visual-option-grid > .form > * {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
}

/* The page-level .form rule above is intentionally broad for the main
   workbench, so override it inside the visualization row.  Keep the two
   toggles on the first row and give line width / color mode a full half-width
   track on the second row. */
#page-image .visual-option-grid,
#page-compare .visual-option-grid,
#page-batch .visual-option-grid {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 10px 12px !important;
  width: 100% !important;
  min-width: 0 !important;
}
#page-image .visual-option-grid > .form,
#page-compare .visual-option-grid > .form,
#page-batch .visual-option-grid > .form {
  grid-column: 1 / -1 !important;
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 10px 12px !important;
  width: 100% !important;
  min-width: 0 !important;
}
#page-image .visual-option-grid > .form > *,
#page-compare .visual-option-grid > .form > *,
#page-batch .visual-option-grid > .form > * {
  display: block !important;
  grid-column: auto !important;
  grid-template-columns: 1fr !important;
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
  align-self: start !important;
}
#page-image .visual-option-grid .wrap,
#page-compare .visual-option-grid .wrap,
#page-batch .visual-option-grid .wrap {
  width: 100% !important;
  min-width: 0 !important;
}
@media (max-width: 760px) {
  #page-image .visual-option-grid,
  #page-image .visual-option-grid > .form,
  #page-compare .visual-option-grid,
  #page-compare .visual-option-grid > .form,
  #page-batch .visual-option-grid,
  #page-batch .visual-option-grid > .form {
    grid-template-columns: 1fr !important;
  }
}
.visual-option-control {
  display: flex !important;
  flex-direction: column !important;
  grid-template-columns: 1fr !important;
  align-items: stretch !important;
  justify-content: flex-start !important;
  gap: 5px !important;
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
}
.visual-option-control .wrap,
.visual-option-control > .wrap,
.visual-option-control .label-wrap,
.visual-option-control select {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
}
.visual-option-toggle {
  min-height: 42px !important;
  justify-content: center !important;
}
.visual-option-toggle .checkbox-container {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 10px !important;
  width: 100% !important;
  min-width: 0 !important;
}
.visual-option-toggle input[type="checkbox"] {
  width: 20px !important;
  min-width: 20px !important;
  max-width: 20px !important;
  height: 20px !important;
  flex: 0 0 20px !important;
}
.visual-option-toggle .label-text {
  width: auto !important;
  min-width: 0 !important;
  max-width: none !important;
  white-space: nowrap !important;
  overflow: visible !important;
}
.visual-option-line-width,
.visual-option-color-mode {
  min-height: 88px !important;
}
.visual-option-line-width input[type="range"],
.visual-option-color-mode input,
.visual-option-color-mode [role="combobox"] {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
}
#page-image .visual-option-grid .visual-option-control,
#page-compare .visual-option-grid .visual-option-control,
#page-batch .visual-option-grid .visual-option-control {
  display: flex !important;
  flex-direction: column !important;
  grid-template-columns: 1fr !important;
}
.detection-result-tab-list {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 8px;
  width: 100%;
  counter-reset: result-tab;
}
.detection-result-tab {
  position: relative;
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr) auto;
  align-items: center;
  gap: 9px;
  width: 100%;
  min-width: 0;
  min-height: 58px;
  padding: 9px 11px;
  overflow: hidden;
  border: 1px solid #dfe8f2;
  border-radius: 10px;
  background: rgba(255, 255, 255, .94);
  color: #344861;
  cursor: pointer;
  font-size: 14px;
  font-weight: 800;
  line-height: 1.35;
  text-align: left;
  white-space: normal;
  overflow-wrap: anywhere;
  box-shadow: 0 3px 10px rgba(15, 23, 42, .035);
  transition:
    transform .16s ease,
    background .16s ease,
    color .16s ease,
    border-color .16s ease,
    box-shadow .16s ease;
}
.detection-result-tab::before {
  counter-increment: result-tab;
  content: counter(result-tab, decimal-leading-zero);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 1px solid #d7e6f7;
  border-radius: 9px;
  background: #eff6ff;
  color: #2563eb;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .03em;
  transition: inherit;
}
.detection-result-tab::after {
  content: "查看";
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 34px;
  min-height: 24px;
  padding: 3px 7px;
  border-radius: 999px;
  background: #f1f5f9;
  color: #718096;
  font-size: 10px;
  font-weight: 800;
  line-height: 1;
  white-space: nowrap;
  transition: inherit;
}
.detection-result-tab:hover {
  transform: translateY(-1px);
  border-color: #b9d4f4;
  background: #f8fbff;
  color: #1d4ed8;
  box-shadow: 0 8px 18px rgba(37, 99, 235, .09);
}
.detection-result-tab.active {
  transform: translateY(-1px);
  border-color: #2563eb;
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 70%, #1e40af 100%);
  color: #fff;
  box-shadow: 0 10px 22px rgba(37, 99, 235, .22);
}
.detection-result-tab.active::before {
  border-color: rgba(255, 255, 255, .42);
  background: rgba(255, 255, 255, .16);
  color: #fff;
}
.detection-result-tab.active::after {
  content: "收起";
  background: rgba(255, 255, 255, .17);
  color: #fff;
}
.detection-result-tab:focus-visible {
  outline: 3px solid rgba(37, 99, 235, .25);
  outline-offset: 2px;
}
@media (max-width: 1100px) {
  .detection-result-tab-list {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
.detection-results-shell .detection-result-panel {
  width: 100% !important;
  min-width: 0 !important;
  min-height: 0 !important;
}
.detection-results-shell .detection-result-panel:not(.is-active) {
  display: none !important;
}
.detection-results-shell .detection-result-panel.is-active {
  display: block !important;
}
.detection-results-shell .detection-result-panel.is-active > .form {
  min-width: 0 !important;
}
#page-image .detection-results-shell .detection-result-panel:not(.is-active),
#page-compare .detection-results-shell .detection-result-panel:not(.is-active),
#page-batch .detection-results-shell .detection-result-panel:not(.is-active) {
  display: none !important;
}

/* Expanded result views: give every tab body a deliberate workspace surface
   instead of exposing a loose stack of raw Gradio components. */
@keyframes detection-result-panel-enter {
  from { opacity: 0; }
  to { opacity: 1; }
}
.detection-results-shell .detection-result-panel.is-active {
  animation: detection-result-panel-enter .2s ease-out both;
  transform: none !important;
  filter: none !important;
  contain: none !important;
}
#page-image .single-result-overview,
#page-image .structured-result-panel,
#page-image .detection-support-review-only,
#page-image .detection-report-panel,
#page-compare .compare-result-models-panel,
#page-compare .compare-result-analysis-panel,
#page-compare .detection-support-review-only,
#page-compare .detection-report-panel,
#page-batch .batch-review-grid,
#page-batch .structured-result-panel,
#page-batch .detection-support-review-only,
#page-batch .detection-report-panel {
  position: relative !important;
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 14px !important;
  overflow: visible !important;
  border: 1px solid #dbe5ef !important;
  border-top-width: 3px !important;
  border-radius: 13px !important;
  background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%) !important;
  box-shadow: 0 8px 22px rgba(15, 23, 42, .055) !important;
}
#page-image .single-result-overview,
#page-compare .compare-result-models-panel,
#page-batch .batch-review-grid {
  border-top-color: #2563eb !important;
}
#page-image .structured-result-panel,
#page-compare .compare-result-analysis-panel,
#page-batch .structured-result-panel {
  border-top-color: #7c3aed !important;
}
#page-image .detection-support-review-only,
#page-compare .detection-support-review-only,
#page-batch .detection-support-review-only {
  border-top-color: #0f9f78 !important;
  background: linear-gradient(180deg, #ffffff 0%, #f8fffc 100%) !important;
}
#page-image .detection-report-panel,
#page-compare .detection-report-panel,
#page-batch .detection-report-panel {
  border-top-color: #f97316 !important;
  background: linear-gradient(180deg, #ffffff 0%, #fffaf5 100%) !important;
}

/* Single-result overview: separate the visual evidence and text summary into
   two readable cards while retaining the existing two-column relationship. */
#page-image .single-result-overview,
#page-image .single-result-overview > .form {
  gap: 14px !important;
}
#page-image .single-result-visual,
#page-image .single-result-insights {
  min-width: 0 !important;
  padding: 12px !important;
  overflow: hidden !important;
  border: 1px solid #e0e9f3 !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, .04) !important;
}
#page-image .single-result-visual .result-compare-slider,
#page-batch .batch-result-main .result-compare-slider {
  overflow: hidden !important;
  border: 1px solid #dce7f2 !important;
  border-radius: 10px !important;
  background: #f8fafc !important;
}
#page-image .single-result-insights .result-card {
  border: 1px solid #e1eaf4 !important;
  border-radius: 9px !important;
  background: linear-gradient(145deg, #fff, #f8fbff) !important;
  box-shadow: none !important;
}

/* Structured result and comparison analysis views. */
#page-image .structured-result-panel .result-filter-bar,
#page-image .structured-result-panel .result-filter-bar > .form {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  align-items: end !important;
  gap: 10px !important;
  width: 100% !important;
  margin: 0 0 12px !important;
  padding: 12px !important;
  border: 1px solid #e4e7f5 !important;
  border-radius: 10px !important;
  background: #faf9ff !important;
  box-shadow: none !important;
}
#page-image .structured-result-panel .result-filter-bar > *,
#page-image .structured-result-panel .result-filter-bar > .form > * {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
}
.structured-result-panel .dataframe,
.compare-analysis-panel .dataframe {
  margin: 0 0 12px !important;
  overflow: hidden !important;
  border: 1px solid #e0e7f0 !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: 0 3px 12px rgba(15, 23, 42, .035) !important;
}
.structured-result-panel table,
.compare-analysis-panel table {
  width: 100% !important;
  border-collapse: separate !important;
  border-spacing: 0 !important;
}
.structured-result-panel thead th,
.compare-analysis-panel thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  background: #f3f0ff !important;
  color: #4338ca !important;
  font-size: 12px !important;
  font-weight: 850 !important;
}
.structured-result-panel tbody tr:nth-child(even),
.compare-analysis-panel tbody tr:nth-child(even) {
  background: #fafbff !important;
}
.structured-result-panel tbody tr:hover,
.compare-analysis-panel tbody tr:hover {
  background: #f3f7ff !important;
}
#page-compare .compare-analysis-panel .compare-summary-panel {
  margin: 0 !important;
  border-color: #ddd6fe !important;
  background: #faf9ff !important;
}

/* Multi-model overview cards. */
#page-compare .compare-result-models-panel,
#page-compare .compare-result-models-panel > .form {
  gap: 14px !important;
}
#page-compare .compare-model-card {
  padding: 12px !important;
  border-radius: 11px !important;
  box-shadow: 0 5px 16px rgba(15, 23, 42, .05) !important;
  transition: transform .16s ease, border-color .16s ease, box-shadow .16s ease;
}
#page-compare .compare-model-card:hover {
  transform: translateY(-2px);
  border-color: #bfd4ee !important;
  box-shadow: 0 10px 22px rgba(37, 99, 235, .09) !important;
}

/* Batch review: make the queue and current image read as two sibling cards. */
#page-batch .batch-result-sidebar,
#page-batch .batch-result-main {
  padding: 12px !important;
  overflow: hidden !important;
  border: 1px solid #e0e9f3 !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, .04) !important;
}
#page-batch .batch-result-sidebar > *:last-child,
#page-batch .batch-result-main > *:last-child {
  margin-bottom: 0 !important;
}

/* Linked review view. */
.detection-support-review-only .detection-support-primary {
  width: 100% !important;
  padding: 0 !important;
}
.detection-support-review-only,
.detection-support-review-only .detection-support-primary,
.detection-support-review-only .linked-review-box,
#det-region-selector,
#cmp-region-selector,
#batch-region-selector {
  overflow: visible !important;
  transform: none !important;
  filter: none !important;
  contain: none !important;
  will-change: auto !important;
}
.detection-support-review-only .linked-review-box {
  display: block !important;
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 14px !important;
  border: 1px solid #cfe9df !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 4px 14px rgba(15, 118, 110, .045) !important;
}
.detection-support-review-only .linked-review-heading {
  margin: 0 0 4px !important;
  padding: 9px 11px !important;
  border: 1px solid #d4eee4 !important;
  border-radius: 9px !important;
  background: #f0fdf8 !important;
}
.detection-support-review-only .linked-review-heading h4 {
  margin: 0 !important;
  color: #0f766e !important;
  font-size: 17px !important;
  font-weight: 850 !important;
  line-height: 1.35 !important;
}
#det-region-selector,
#cmp-region-selector,
#batch-region-selector {
  position: relative !important;
  z-index: 30 !important;
  width: 100% !important;
  min-width: 0 !important;
  margin: 10px 0 4px !important;
}
#det-region-selector .wrap,
#cmp-region-selector .wrap,
#batch-region-selector .wrap {
  position: relative !important;
  overflow: visible !important;
  transform: none !important;
  filter: none !important;
  contain: none !important;
}
.gradio-container ul.options[role="listbox"] {
  margin-top: 2px !important;
}
.detection-support-review-only .accordion {
  width: 100% !important;
  margin: 0 !important;
  overflow: hidden !important;
  border: 1px solid #cfe9df !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 4px 14px rgba(15, 118, 110, .045) !important;
}
.detection-support-review-only .accordion .label-wrap {
  min-height: 46px !important;
  padding: 10px 12px !important;
  background: #f0fdf8 !important;
  color: #0f766e !important;
  font-weight: 850 !important;
}
.detection-support-review-only .linked-region-row,
.detection-support-review-only .linked-region-row > .form {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 12px !important;
  width: 100% !important;
  margin: 10px 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.detection-support-review-only .linked-region-row > *,
.detection-support-review-only .linked-region-row > .form > * {
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
  overflow: hidden !important;
  border: 1px solid #d9ebe4 !important;
  border-radius: 10px !important;
  background: #f8fffc !important;
}

/* Report view. */
.detection-report-panel h4 {
  margin: 0 0 6px !important;
  color: #9a3412 !important;
  font-size: 19px !important;
  line-height: 1.35 !important;
}
.detection-report-panel .auto-report-controls {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  min-height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
  border: 0 !important;
}
.detection-report-panel .report-generation-controls,
.detection-report-panel .report-generation-controls > .form {
  padding: 12px !important;
  border: 1px solid #fed7aa !important;
  border-radius: 10px !important;
  background: #fff7ed !important;
}
.detection-report-panel .gallery {
  overflow: hidden !important;
  border: 1px solid #e7eaf0 !important;
  border-radius: 10px !important;
  background: #fff !important;
}
.detection-report-panel .detection-report-display {
  display: block !important;
  width: 100% !important;
  min-width: 0 !important;
  margin: 0 0 12px !important;
  padding: 12px !important;
  overflow: visible !important;
  border: 1px solid #fed7aa !important;
  border-radius: 11px !important;
  background: #fff !important;
  box-shadow: 0 5px 16px rgba(154, 52, 18, .045) !important;
}
.detection-report-panel .detection-report-display .gallery {
  margin: 12px 0 0 !important;
}
.detection-report-panel .detection-report-preview {
  margin: 0 !important;
  padding: 0 !important;
  overflow: auto !important;
  border: 1px solid #e5e7eb !important;
  border-radius: 10px !important;
  background: #fff !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .75) !important;
}
.detection-report-panel .detection-report-preview .prose {
  margin: 0 !important;
  padding: 14px !important;
  border: 0 !important;
  background: transparent !important;
}
.detection-report-panel .report-download-row {
  margin-bottom: 0 !important;
  padding-top: 12px !important;
  border-color: #fed7aa !important;
  background: #fffaf5 !important;
}

@media (max-width: 1080px) {
  #page-image .structured-result-panel .result-filter-bar,
  #page-image .structured-result-panel .result-filter-bar > .form {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  .detection-results-shell .detection-result-panel.is-active {
    animation: none !important;
  }
}
@media (max-width: 760px) {
  #page-image .threshold-preset-control .wrap,
  .visual-option-grid,
  .visual-option-grid > .form {
    grid-template-columns: 1fr !important;
  }
  .detection-result-tab-list {
    grid-template-columns: 1fr;
  }
  .detection-result-tab {
    min-height: 52px;
    padding: 8px 10px;
  }
  #page-image .single-result-overview,
  #page-image .structured-result-panel,
  #page-image .detection-support-review-only,
  #page-image .detection-report-panel,
  #page-compare .compare-result-models-panel,
  #page-compare .compare-result-analysis-panel,
  #page-compare .detection-support-review-only,
  #page-compare .detection-report-panel,
  #page-batch .batch-review-grid,
  #page-batch .structured-result-panel,
  #page-batch .detection-support-review-only,
  #page-batch .detection-report-panel {
    padding: 9px !important;
    border-radius: 10px !important;
  }
  #page-image .structured-result-panel .result-filter-bar,
  #page-image .structured-result-panel .result-filter-bar > .form,
  .detection-support-review-only .linked-region-row,
  .detection-support-review-only .linked-region-row > .form {
    grid-template-columns: 1fr !important;
  }
}

/* ===========================================================================
   Dental Vision UI v4 — unified application shell and page workspaces.
   This final layer intentionally targets the current DOM only.  Component
   ids, visibility rules and event hooks remain owned by app.py/ui/head.py.
   ========================================================================== */
:root {
  --dv-navy-950: #071a2b;
  --dv-navy-900: #0b2239;
  --dv-navy-800: #123654;
  --dv-blue-600: #2563eb;
  --dv-blue-500: #3b82f6;
  --dv-cyan-500: #0ea5e9;
  --dv-teal-600: #0f766e;
  --dv-teal-500: #14b8a6;
  --dv-orange-500: #f97316;
  --dv-ink: #142033;
  --dv-body: #3d4c61;
  --dv-muted: #718096;
  --dv-line: #dce5ee;
  --dv-line-strong: #c8d4e1;
  --dv-canvas: #edf3f8;
  --dv-panel: #ffffff;
  --dv-panel-soft: #f7fafc;
  --dv-blue-soft: #eef6ff;
  --dv-teal-soft: #edfdf9;
  --dv-orange-soft: #fff7ed;
  --dv-radius-sm: 9px;
  --dv-radius-md: 14px;
  --dv-radius-lg: 20px;
  --dv-shadow-sm: 0 5px 16px rgba(15, 35, 55, .055);
  --dv-shadow-md: 0 14px 34px rgba(15, 35, 55, .09);
  --dv-shadow-lg: 0 24px 60px rgba(7, 26, 43, .15);
}

html { background: var(--dv-canvas) !important; }
body { color: var(--dv-body) !important; }
.gradio-container {
  width: 100% !important;
  max-width: none !important;
  min-height: 100vh !important;
  padding: 12px clamp(10px, 1.8vw, 30px) 42px !important;
  background:
    radial-gradient(circle at 3% 2%, rgba(14, 165, 233, .09), transparent 24rem),
    radial-gradient(circle at 96% 10%, rgba(20, 184, 166, .075), transparent 26rem),
    linear-gradient(180deg, #f7fafc 0, var(--dv-canvas) 36rem, #eef3f7 100%) !important;
  color: var(--dv-body) !important;
  font-family: Inter, "PingFang SC", "Microsoft YaHei", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}
.gradio-container h1,
.gradio-container h2,
.gradio-container h3,
.gradio-container h4,
.gradio-container h5 { color: var(--dv-ink); letter-spacing: -.015em; }

/* Application masthead */
.app-hero {
  position: relative !important;
  isolation: isolate;
  max-width: 1560px !important;
  min-height: 138px;
  margin: 0 auto 12px !important;
  padding: 24px 28px !important;
  overflow: hidden !important;
  border: 1px solid rgba(255, 255, 255, .14) !important;
  border-radius: var(--dv-radius-lg) !important;
  background:
    linear-gradient(100deg, rgba(11, 34, 57, .99), rgba(14, 53, 77, .97) 58%, rgba(15, 118, 110, .92)) !important;
  box-shadow: var(--dv-shadow-lg) !important;
}
.app-hero::before {
  content: "" !important;
  position: absolute;
  z-index: -1;
  width: 420px;
  height: 420px;
  top: -270px;
  right: 13%;
  border: 74px solid rgba(255, 255, 255, .055);
  border-radius: 50%;
  pointer-events: none;
}
.app-hero::after {
  content: "" !important;
  position: absolute;
  z-index: -1;
  inset: auto -70px -110px auto;
  width: 290px;
  height: 230px;
  border-radius: 50%;
  background: rgba(14, 165, 233, .12);
  filter: blur(1px);
  pointer-events: none;
}
.app-hero-top {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) minmax(390px, auto) !important;
  align-items: center !important;
  gap: 28px !important;
}
.app-brand-lockup { display: flex; align-items: center; gap: 19px; min-width: 0; }
.app-brand-mark {
  display: grid;
  flex: 0 0 74px;
  width: 74px;
  height: 74px;
  place-items: center;
  border: 1px solid rgba(255, 255, 255, .24);
  border-radius: 20px;
  background: linear-gradient(145deg, rgba(255, 255, 255, .18), rgba(255, 255, 255, .07));
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .18), 0 18px 34px rgba(0, 0, 0, .16);
}
.app-brand-mark svg { width: 45px; height: 45px; overflow: visible; }
.app-brand-mark svg path:first-child { fill: rgba(255, 255, 255, .96); stroke: rgba(255, 255, 255, .96); stroke-width: 1.4; }
.app-brand-mark svg path:last-child { fill: none; stroke: var(--dv-teal-600); stroke-width: 3; stroke-linecap: round; }
.app-hero-copy { min-width: 0; }
.app-hero-kicker {
  display: block;
  margin-bottom: 6px;
  color: #7dd3fc;
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .19em;
}
.app-hero h1 {
  margin: 0 0 6px !important;
  color: #fff !important;
  font-size: clamp(25px, 2.2vw, 36px) !important;
  font-weight: 860 !important;
  line-height: 1.2 !important;
}
.app-hero p {
  max-width: 820px;
  margin: 0 !important;
  color: #c9d7e5 !important;
  font-size: 14px !important;
  line-height: 1.65 !important;
}
.app-hero-status { display: grid; gap: 10px; min-width: 0; }
.app-live-status {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 42px;
  padding: 8px 12px;
  border: 1px solid rgba(255, 255, 255, .16);
  border-radius: 11px;
  background: rgba(7, 26, 43, .24);
  backdrop-filter: blur(6px);
}
.app-live-status > i {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #5eead4;
  box-shadow: 0 0 0 5px rgba(94, 234, 212, .12);
}
.app-live-status span { display: grid; gap: 1px; }
.app-live-status b { color: #fff; font-size: 12px; }
.app-live-status small { color: #9fb5c8; font-size: 10px; }
.app-hero-facts {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 7px;
}
.app-hero-facts > span {
  display: grid;
  gap: 1px;
  padding: 8px 10px;
  border: 1px solid rgba(255, 255, 255, .13);
  border-radius: 10px;
  background: rgba(255, 255, 255, .065);
}
.app-hero-facts b { color: #fff; font-size: 13px; line-height: 1.2; }
.app-hero-facts small { color: #a9bccd; font-size: 9px; white-space: nowrap; }

/* Eight-workspace command navigation */
.dental-page-nav {
  position: sticky !important;
  top: 8px !important;
  z-index: 9000 !important;
  display: block !important;
  max-width: 1560px !important;
  margin: 0 auto 14px !important;
  padding: 7px !important;
  border: 1px solid rgba(200, 212, 225, .92) !important;
  border-radius: 16px !important;
  background: rgba(255, 255, 255, .92) !important;
  box-shadow: 0 10px 30px rgba(15, 35, 55, .095) !important;
  backdrop-filter: blur(14px) saturate(1.15) !important;
}
.dental-nav-toggle { display: none !important; }
.dental-nav-items {
  display: grid !important;
  grid-template-columns: repeat(8, minmax(0, 1fr));
  gap: 5px !important;
  width: 100%;
}
.dental-page-nav-item {
  display: flex !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 9px !important;
  min-width: 0 !important;
  min-height: 54px !important;
  padding: 7px 9px !important;
  border: 1px solid transparent !important;
  border-radius: 10px !important;
  background: transparent !important;
  color: #4b5d70 !important;
  box-shadow: none !important;
  text-align: left !important;
  transition: background .16s ease, border-color .16s ease, color .16s ease, transform .16s ease !important;
}
.dental-nav-icon {
  display: grid;
  flex: 0 0 29px;
  width: 29px;
  height: 29px;
  place-items: center;
  border: 1px solid var(--dv-line);
  border-radius: 8px;
  background: var(--dv-panel-soft);
  color: #718096;
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .04em;
}
.dental-nav-copy { display: grid; min-width: 0; gap: 1px; }
.dental-nav-copy b { overflow: hidden; font-size: 12px; line-height: 1.2; text-overflow: ellipsis; white-space: nowrap; }
.dental-nav-copy small { overflow: hidden; color: #8a99aa; font-size: 9px; line-height: 1.2; text-overflow: ellipsis; white-space: nowrap; }
.dental-page-nav-item:hover {
  transform: translateY(-1px) !important;
  border-color: #cbdcf1 !important;
  background: var(--dv-blue-soft) !important;
  color: #163e67 !important;
}
.dental-page-nav-item:hover .dental-nav-icon { border-color: #bfdbfe; background: #fff; color: var(--dv-blue-600); }
.dental-page-nav-item.active,
body[data-dental-page="learn"] .dental-page-nav-item[data-page="learn"],
body[data-dental-page="dashboard"] .dental-page-nav-item[data-page="dashboard"],
body[data-dental-page="image"] .dental-page-nav-item[data-page="image"],
body[data-dental-page="compare"] .dental-page-nav-item[data-page="compare"],
body[data-dental-page="batch"] .dental-page-nav-item[data-page="batch"],
body[data-dental-page="history"] .dental-page-nav-item[data-page="history"],
body[data-dental-page="assistant"] .dental-page-nav-item[data-page="assistant"],
body[data-dental-page="report"] .dental-page-nav-item[data-page="report"] {
  transform: none !important;
  border-color: #174c78 !important;
  background: linear-gradient(135deg, var(--dv-navy-900), var(--dv-navy-800)) !important;
  color: #fff !important;
  box-shadow: 0 7px 16px rgba(11, 34, 57, .18) !important;
}
.dental-page-nav-item.active .dental-nav-icon,
body[data-dental-page] .dental-page-nav-item.active .dental-nav-icon {
  border-color: rgba(255, 255, 255, .18);
  background: rgba(255, 255, 255, .12);
  color: #7dd3fc;
}
.dental-page-nav-item.active .dental-nav-copy small { color: #b8c9d8; }
.dental-page-nav-item.active .dental-nav-copy b,
.dental-page-nav-item.active .dental-nav-copy small { color: #fff !important; }
.dental-page-nav-item.active .dental-nav-copy small { color: #b8c9d8 !important; }

/* Shared page canvas and page headers */
.dental-page,
#page-image,
#page-compare,
#page-batch {
  width: 100% !important;
  max-width: 1560px !important;
  margin: 0 auto !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.workspace-page-hero,
.detection-page-hero {
  position: relative;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 18px;
  min-height: 118px;
  margin: 0 0 14px !important;
  padding: 22px 24px !important;
  overflow: hidden;
  border: 1px solid #c9d7e5 !important;
  border-radius: 18px !important;
  background:
    linear-gradient(112deg, #fff 0%, #f6fbff 58%, #edfdf9 100%) !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
.workspace-page-hero::after,
.detection-page-hero::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 7px;
  height: 100%;
  background: linear-gradient(180deg, var(--dv-cyan-500), var(--dv-teal-500));
}
.detection-page-hero { grid-template-columns: minmax(0, 1fr) auto; }
.workspace-page-index {
  display: grid;
  width: 58px;
  height: 58px;
  place-items: center;
  border-radius: 16px;
  background: var(--dv-navy-900);
  color: #7dd3fc;
  box-shadow: 0 10px 22px rgba(11, 34, 57, .15);
  font-size: 15px;
  font-weight: 900;
  letter-spacing: .08em;
}
.workspace-page-copy,
.detection-page-hero-copy { min-width: 0; }
.workspace-page-copy > small,
.detection-page-hero-copy > small {
  display: block;
  margin-bottom: 4px;
  color: var(--dv-teal-600) !important;
  font-size: 10px !important;
  font-weight: 900 !important;
  letter-spacing: .13em;
  text-transform: uppercase;
}
.workspace-page-copy h2,
.detection-page-hero-copy h2 {
  margin: 0 0 5px !important;
  color: var(--dv-navy-900) !important;
  font-size: clamp(27px, 2.4vw, 37px) !important;
  line-height: 1.16 !important;
}
.workspace-page-copy p,
.detection-page-hero-copy p {
  max-width: 820px;
  margin: 0 !important;
  color: #607185 !important;
  font-size: 13px !important;
  line-height: 1.7 !important;
}
.workspace-page-badges,
.detection-page-badges {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: flex-end !important;
  gap: 7px !important;
  max-width: 390px;
}
.workspace-page-badges span,
.detection-page-badges span {
  display: inline-flex !important;
  align-items: center !important;
  min-height: 30px;
  padding: 5px 10px !important;
  border: 1px solid #cfe1ef !important;
  border-radius: 999px !important;
  background: rgba(255, 255, 255, .82) !important;
  color: #36516b !important;
  font-size: 10px !important;
  font-weight: 800 !important;
  white-space: nowrap;
}

/* Shared panel language */
.workspace-panel-heading {
  display: flex;
  align-items: flex-start;
  gap: 11px;
  margin: 0 0 12px;
}
.workspace-panel-heading > span {
  flex: 0 0 auto;
  padding: 5px 8px;
  border-radius: 7px;
  background: var(--dv-blue-soft);
  color: var(--dv-blue-600);
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .06em;
}
.workspace-panel-heading > div { min-width: 0; }
.workspace-panel-heading h3 { margin: 0 0 2px; font-size: 17px; line-height: 1.25; }
.workspace-panel-heading p { margin: 0; color: var(--dv-muted); font-size: 11px; line-height: 1.55; }
.workspace-panel-heading--compact { margin-bottom: 9px; }
.workspace-panel-heading--compact h3 { font-size: 15px; }

.gradio-container input:not([type="range"]):not([type="checkbox"]):not([type="radio"]),
.gradio-container textarea,
.gradio-container select {
  border-color: var(--dv-line-strong) !important;
  border-radius: var(--dv-radius-sm) !important;
  background: #fff !important;
  color: var(--dv-ink) !important;
  box-shadow: 0 1px 0 rgba(255, 255, 255, .9) !important;
}
.gradio-container button.primary,
.solid-primary-action button,
button.solid-primary-action,
.report-generate-action button {
  min-height: 44px !important;
  border: 1px solid #174d78 !important;
  border-radius: 10px !important;
  background: linear-gradient(135deg, var(--dv-navy-900), #174d78) !important;
  color: #fff !important;
  box-shadow: 0 8px 18px rgba(11, 34, 57, .16) !important;
  font-weight: 820 !important;
}
.gradio-container button.primary:hover,
.solid-primary-action button:hover,
button.solid-primary-action:hover,
.report-generate-action button:hover {
  transform: translateY(-1px) !important;
  border-color: #0c5f86 !important;
  background: linear-gradient(135deg, #123654, #0c6683) !important;
}

/* Detection, comparison and batch workspaces */
.detection-workflow-shell {
  margin: 0 0 12px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.detection-workflow {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0 !important;
  margin: 0 !important;
  padding: 8px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 14px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
.detection-workflow li {
  position: relative;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px;
  min-height: 40px;
  border-radius: 9px !important;
  color: #8190a2 !important;
}
.detection-workflow li:not(:last-child)::after {
  content: "";
  position: absolute;
  right: -1px;
  width: 1px;
  height: 20px;
  background: var(--dv-line);
}
.detection-workflow li span {
  display: grid;
  width: 23px;
  height: 23px;
  place-items: center;
  border: 1px solid var(--dv-line);
  border-radius: 7px;
  background: var(--dv-panel-soft);
  font-size: 9px;
}
.detection-workflow li.is-active { background: var(--dv-blue-soft) !important; color: #1d4f91 !important; }
.detection-workflow li.is-active span { border-color: #93c5fd; background: #fff; color: var(--dv-blue-600); }
.detection-workflow li.is-done { background: var(--dv-teal-soft) !important; color: var(--dv-teal-600) !important; }
.detection-workflow li.is-done span { border-color: #99f6e4; background: #fff; color: var(--dv-teal-600); }

#page-image .detection-workbench,
#page-compare .detection-workbench,
#page-batch .detection-workbench {
  display: grid !important;
  grid-template-columns: minmax(320px, .86fr) minmax(480px, 1.34fr) !important;
  gap: 14px !important;
  align-items: stretch !important;
  margin: 0 0 14px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-image .detection-workbench > .form,
#page-compare .detection-workbench > .form,
#page-batch .detection-workbench > .form {
  display: contents !important;
}
#page-image .detection-upload-panel,
#page-image .detection-parameter-panel,
#page-compare .detection-upload-panel,
#page-compare .detection-parameter-panel,
#page-batch .detection-upload-panel,
#page-batch .detection-parameter-panel {
  min-width: 0 !important;
  height: 100% !important;
  padding: 16px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 16px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-image .detection-upload-panel,
#page-compare .detection-upload-panel,
#page-batch .detection-upload-panel { border-top: 4px solid var(--dv-cyan-500) !important; }
#page-image .detection-parameter-panel,
#page-compare .detection-parameter-panel,
#page-batch .detection-parameter-panel { border-top: 4px solid var(--dv-teal-500) !important; }
.detection-panel-heading {
  margin: 0 0 12px !important;
  padding: 0 0 10px !important;
  border-bottom: 1px solid #e8eef4 !important;
  background: transparent !important;
}
.detection-panel-heading h3 { margin: 0 !important; color: var(--dv-navy-900) !important; font-size: 16px !important; }
.detection-controls,
.detection-controls > .styler {
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#single-upload,
#compare-upload,
#page-batch .batch-upload-composite {
  overflow: hidden !important;
  border: 1px dashed #9ebbd2 !important;
  border-radius: 13px !important;
  background: linear-gradient(180deg, #f9fcff, #f3f8fb) !important;
}
#page-image #single-upload > label.float,
#page-compare #compare-upload > label.float,
#page-batch #batch-upload > label.float {
  inset: 10px auto auto 10px !important;
  width: auto !important;
  max-width: calc(100% - 20px) !important;
  height: auto !important;
  min-height: 30px !important;
  padding: 6px 9px !important;
  border: 1px solid #cbdbe8 !important;
  border-radius: 8px !important;
  background: rgba(255, 255, 255, .95) !important;
  box-shadow: 0 5px 14px rgba(15, 38, 60, .08) !important;
}
#page-image #single-upload .upload-container button > .wrap,
#page-compare #compare-upload .upload-container button > .wrap,
#page-batch #batch-upload .upload-container button > .wrap {
  width: min(240px, 82%) !important;
  max-width: 82% !important;
}
.detection-stage-heading {
  margin: 0 !important;
  padding: 16px 18px 10px !important;
  border: 0 !important;
  background: transparent !important;
}
.detection-stage-heading h3 { margin: 0 !important; font-size: 19px !important; }
.detection-results-shell {
  overflow: hidden !important;
  margin: 0 0 14px !important;
  padding: 0 0 14px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 18px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-md) !important;
}
.detection-result-tabs {
  margin: 0 16px 14px !important;
  padding: 5px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 12px !important;
  background: #f3f7fa !important;
}
.detection-result-tab-list { gap: 5px !important; }
.detection-result-tab {
  min-height: 44px !important;
  border: 1px solid transparent !important;
  border-radius: 9px !important;
  background: transparent !important;
  color: #617287 !important;
  font-weight: 780 !important;
}
.detection-result-tab:hover { border-color: #d2dfeb !important; background: #fff !important; color: var(--dv-navy-900) !important; }
.detection-result-tab.active {
  border-color: #173f63 !important;
  background: var(--dv-navy-900) !important;
  color: #fff !important;
  box-shadow: 0 6px 14px rgba(11, 34, 57, .14) !important;
}
#page-image .single-result-overview,
#page-image .structured-result-panel,
#page-image .detection-support-review-only,
#page-image .detection-report-panel,
#page-compare .compare-result-models-panel,
#page-compare .compare-result-analysis-panel,
#page-compare .detection-support-review-only,
#page-compare .detection-report-panel,
#page-batch .batch-review-grid,
#page-batch .structured-result-panel,
#page-batch .detection-support-review-only,
#page-batch .detection-report-panel {
  width: auto !important;
  margin: 0 16px !important;
  padding: 16px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 14px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-image .single-result-overview,
#page-image .single-result-overview > .form {
  display: grid !important;
  grid-template-columns: minmax(0, 1.65fr) minmax(300px, .75fr) !important;
  gap: 14px !important;
}
#page-image .single-result-visual,
#page-image .single-result-insights,
#page-batch .batch-result-sidebar,
#page-batch .batch-result-main {
  padding: 12px !important;
  border: 1px solid #e3eaf1 !important;
  border-radius: 12px !important;
  background: var(--dv-panel-soft) !important;
}
#page-compare .compare-model-grid,
#page-compare .compare-model-grid > .form {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 12px !important;
}
#page-compare .compare-model-card {
  overflow: hidden !important;
  min-width: 0 !important;
  padding: 11px !important;
  border: 1px solid var(--dv-line) !important;
  border-top: 4px solid var(--dv-cyan-500) !important;
  border-radius: 13px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-compare .compare-model-precision { border-top-color: var(--dv-blue-600) !important; }
#page-compare .compare-model-recall { border-top-color: var(--dv-teal-500) !important; }
#page-batch .batch-review-grid,
#page-batch .batch-review-grid > .form {
  display: grid !important;
  grid-template-columns: minmax(290px, .72fr) minmax(0, 1.55fr) !important;
  gap: 14px !important;
  align-items: start !important;
}
.linked-review-box {
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.linked-review-heading { margin-bottom: 5px !important; }
.linked-region-row,
.linked-region-row > .form { display: grid !important; grid-template-columns: repeat(2, minmax(0, 1fr)) !important; gap: 12px !important; }

/* Dashboard */
#page-dashboard .dashboard-shell { display: grid; gap: 15px; }
#page-dashboard .dashboard-overview {
  overflow: hidden;
  padding: clamp(22px, 3vw, 38px) !important;
  border: 1px solid rgba(255, 255, 255, .12) !important;
  border-radius: 19px !important;
  background:
    radial-gradient(circle at 82% 0, rgba(20, 184, 166, .17), transparent 27rem),
    linear-gradient(118deg, var(--dv-navy-950), #103451 68%, #0e5f63) !important;
  box-shadow: var(--dv-shadow-lg) !important;
}
#page-dashboard .dashboard-eyebrow { color: #7dd3fc !important; }
#page-dashboard .dashboard-overview h2 { color: #fff !important; font-size: clamp(30px, 3.2vw, 48px) !important; }
#page-dashboard .dashboard-overview h2 span { color: #99f6e4 !important; }
#page-dashboard .dashboard-overview-copy > p { color: #c2d3e1 !important; }
#page-dashboard .dashboard-quick-link.dental-page-nav-item {
  min-height: 72px !important;
  border: 1px solid rgba(255, 255, 255, .14) !important;
  border-radius: 12px !important;
  background: rgba(255, 255, 255, .07) !important;
  color: #fff !important;
  box-shadow: none !important;
}
#page-dashboard .dashboard-quick-link.dental-page-nav-item:hover { transform: translateY(-2px) !important; background: rgba(255, 255, 255, .13) !important; }
#page-dashboard .dashboard-quick-link b { color: #fff !important; }
#page-dashboard .dashboard-quick-link small { color: #b9cad8 !important; }
#page-dashboard .dashboard-runtime-card {
  border: 1px solid rgba(255, 255, 255, .17) !important;
  border-radius: 15px !important;
  background: rgba(5, 25, 42, .36) !important;
  box-shadow: none !important;
  backdrop-filter: blur(8px);
}
#page-dashboard .dashboard-runtime-card * { color: #d8e4ee; }
#page-dashboard .dashboard-runtime-card dd,
#page-dashboard .dashboard-runtime-card b { color: #fff !important; }
#page-dashboard .dashboard-kpi-grid { gap: 12px !important; }
#page-dashboard .dashboard-kpi-card,
#page-dashboard .dashboard-compact-panel {
  border: 1px solid var(--dv-line) !important;
  border-radius: 15px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-dashboard .dashboard-kpi-card { position: relative; overflow: hidden; }
#page-dashboard .dashboard-kpi-card::after { content: ""; position: absolute; inset: 0 0 auto; height: 4px; background: var(--dv-blue-600); }
#page-dashboard .dashboard-kpi-card--cyan::after { background: var(--dv-cyan-500); }
#page-dashboard .dashboard-kpi-card--amber::after { background: var(--dv-orange-500); }
#page-dashboard .dashboard-kpi-card--teal::after { background: var(--dv-teal-500); }
#page-dashboard .dashboard-actions-row {
  display: flex !important;
  justify-content: flex-end !important;
  gap: 9px !important;
  margin: 12px 0 4px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-dashboard .dashboard-actions-row > * { flex: 0 0 auto !important; min-width: 150px !important; }
#page-dashboard .dashboard-analytics-panel,
#page-dashboard .dashboard-status-panel {
  overflow: hidden !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 15px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}

/* Learning atlas */
#page-learn .education-shell { gap: 15px !important; }
#page-learn .education-toolbar {
  top: 82px !important;
  padding: 10px 12px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 14px !important;
  background: rgba(255, 255, 255, .94) !important;
  box-shadow: var(--dv-shadow-sm) !important;
  backdrop-filter: blur(12px);
}
#page-learn .education-hero {
  overflow: hidden;
  padding: clamp(24px, 3.5vw, 46px) !important;
  border: 1px solid #c8d9e7 !important;
  border-radius: 19px !important;
  background:
    radial-gradient(circle at 87% 12%, rgba(20, 184, 166, .13), transparent 24rem),
    linear-gradient(125deg, #fff, #f4faff 64%, #edfcf8) !important;
  box-shadow: var(--dv-shadow-md) !important;
}
#page-learn .education-grid { gap: 13px !important; }
#page-learn .education-card {
  overflow: hidden;
  border: 1px solid var(--dv-line) !important;
  border-radius: 15px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease !important;
}
#page-learn .education-card:hover { transform: translateY(-3px) !important; border-color: #b9d3e7 !important; box-shadow: var(--dv-shadow-md) !important; }
#page-learn .education-review-strip,
#page-learn .education-evidence,
#page-learn .education-disclaimer {
  border-radius: 15px !important;
  box-shadow: var(--dv-shadow-sm) !important;
}

/* History workspace */
#page-history .history-metric-grid { gap: 11px !important; margin-bottom: 14px !important; }
#page-history .history-summary-card,
#page-history .metric-card {
  border: 1px solid var(--dv-line) !important;
  border-radius: 14px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-history .history-command-deck,
#page-history .history-command-deck > .form,
#page-history .history-detail-workspace,
#page-history .history-detail-workspace > .form {
  display: grid !important;
  grid-template-columns: minmax(0, 1.55fr) minmax(320px, .72fr) !important;
  gap: 14px !important;
  align-items: stretch !important;
  margin: 0 0 14px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-history .history-visual-panel,
#page-history .history-control-panel,
#page-history .history-table-panel,
#page-history .history-detail-controls,
#page-history .history-detail-preview {
  min-width: 0 !important;
  padding: 15px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 15px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-history .history-visual-panel { border-top: 4px solid var(--dv-cyan-500) !important; }
#page-history .history-control-panel { border-top: 4px solid var(--dv-teal-500) !important; }
#page-history .history-action-row,
#page-history .history-action-row > .form {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 7px !important;
  margin: 0 0 10px !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-history .history-action-row button {
  min-width: 0 !important;
  min-height: 44px !important;
  padding-inline: 7px !important;
  border: 1px solid #b9cede !important;
  border-radius: 9px !important;
  background: #fff !important;
  color: #24435e !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  text-align: center !important;
}
#page-history .history-action-row button.primary,
#page-history .history-action-row button[variant="primary"] {
  border-color: #174d78 !important;
  background: linear-gradient(135deg, var(--dv-navy-900), #174d78) !important;
  color: #fff !important;
  box-shadow: 0 7px 16px rgba(11, 34, 57, .16) !important;
}
#page-history .history-action-row button:hover {
  border-color: #0c6683 !important;
  background: var(--dv-blue-soft) !important;
  color: var(--dv-navy-900) !important;
}
#page-history .history-action-row button.primary:hover,
#page-history .history-action-row button[variant="primary"]:hover {
  background: linear-gradient(135deg, #123654, #0c6683) !important;
  color: #fff !important;
}
#page-history .history-export-download {
  display: block !important;
  width: 100% !important;
  min-height: 44px !important;
  margin-top: 12px !important;
}
#page-history button.history-export-download,
#page-history a.history-export-download,
#page-history .history-export-download a,
#page-history .history-export-download button {
  width: 100% !important;
  min-height: 44px !important;
  justify-content: center !important;
  border: 1px solid #174d78 !important;
  border-radius: 9px !important;
  background: linear-gradient(135deg, var(--dv-navy-900), #174d78) !important;
  color: #fff !important;
  font-size: 13px !important;
  font-weight: 800 !important;
  box-shadow: 0 7px 16px rgba(11, 34, 57, .16) !important;
}
#page-history button.history-export-download:hover,
#page-history a.history-export-download:hover,
#page-history .history-export-download a:hover,
#page-history .history-export-download button:hover {
  background: linear-gradient(135deg, #123654, #0c6683) !important;
  color: #fff !important;
}
#page-history .history-export-download [data-testid="file"] {
  min-height: 0 !important;
}
#page-history .history-filter-stack,
#page-history .history-filter-stack > .styler { display: grid !important; gap: 8px !important; padding: 0 !important; border: 0 !important; background: transparent !important; }
#page-history .history-thumbnail-gallery { overflow: hidden !important; border: 1px solid #e3eaf1 !important; border-radius: 11px !important; background: var(--dv-panel-soft) !important; }
#page-history .history-table-panel { margin-bottom: 14px !important; }
#page-history .history-pagination-bar,
#page-history .history-pagination-bar > .form {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 16px !important;
  width: auto !important;
  min-height: 62px !important;
  margin: 12px -15px -15px !important;
  padding: 11px 15px !important;
  border: 0 !important;
  border-top: 1px solid #e1e8ee !important;
  border-radius: 0 0 14px 14px !important;
  background: #f7f9fb !important;
  box-shadow: none !important;
}
#page-history .history-pagination-bar > .form {
  flex: 1 1 auto !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-history .history-pagination,
#page-history .history-pagination > .form,
#page-history .history-pagination > .styler {
  display: flex !important;
  align-items: center !important;
  justify-content: flex-end !important;
  flex: 0 0 auto !important;
  flex-wrap: nowrap !important;
  gap: 6px !important;
  width: auto !important;
  min-width: 0 !important;
  min-height: 40px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-history .history-pagination button {
  flex: 0 0 auto !important;
  width: auto !important;
  min-width: 88px !important;
  min-height: 40px !important;
  padding: 0 15px !important;
  border-radius: 7px !important;
  font-size: 12px !important;
  font-weight: 800 !important;
  line-height: 1 !important;
  box-shadow: none !important;
}
#page-history .history-pagination button:not(.primary) {
  border: 1px solid #c5d2dc !important;
  background: #fff !important;
  color: #24435e !important;
}
#page-history .history-pagination button:not(.primary):hover {
  border-color: #174d78 !important;
  color: #174d78 !important;
}
#page-history .history-pagination button.primary {
  min-width: 68px !important;
  border-color: #174d78 !important;
  background: #174d78 !important;
  color: #fff !important;
}
#page-history .history-pagination button.primary:hover { background: #123f63 !important; }
#page-history .history-pagination button:disabled {
  border-color: #d9e2e9 !important;
  background: #eef2f5 !important;
  color: #9aa8b3 !important;
  opacity: 1 !important;
  cursor: not-allowed !important;
}
#page-history #history-page-prefix,
#page-history #history-page-total {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex: 0 0 auto !important;
  width: auto !important;
  min-width: 0 !important;
  min-height: 40px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
  color: #536b80 !important;
  font-size: 12px !important;
  font-weight: 750 !important;
  line-height: 1 !important;
  box-shadow: none !important;
}
#page-history #history-page-total b { color: var(--dv-navy-900) !important; }
#page-history #history-page-input {
  flex: 0 0 72px !important;
  width: 72px !important;
  min-width: 72px !important;
  max-width: 72px !important;
  min-height: 40px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-history #history-page-input > .wrap,
#page-history #history-page-input .wrap {
  min-height: 40px !important;
  border: 1px solid #aebfcd !important;
  border-radius: 7px !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-history #history-page-input input {
  min-height: 38px !important;
  padding: 6px 8px !important;
  color: var(--dv-navy-900) !important;
  font-size: 13px !important;
  font-weight: 850 !important;
  text-align: center !important;
  appearance: textfield !important;
  -moz-appearance: textfield !important;
}
#page-history #history-page-input input::-webkit-inner-spin-button,
#page-history #history-page-input input::-webkit-outer-spin-button { margin: 0 !important; appearance: none !important; }
#page-history #history-page-feedback {
  flex: 1 1 auto !important;
  width: auto !important;
  min-width: 150px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  color: #60778a !important;
  font-size: 12px !important;
  text-align: left !important;
  box-shadow: none !important;
}
#page-history #history-page-feedback .prose { max-width: none !important; }
#page-history #history-page-feedback p { margin: 0 !important; }
#page-history .history-detail-workspace,
#page-history .history-detail-workspace > .form { grid-template-columns: minmax(300px, .7fr) minmax(0, 1.5fr) !important; }
#page-history .history-detail-preview .prose { max-width: none !important; }

/* Assistant workspace */
#page-assistant .native-ai-assistant {
  min-height: 720px !important;
  padding: 0 !important;
  gap: 14px !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-top {
  padding: 22px !important;
  border: 1px solid rgba(255, 255, 255, .12) !important;
  border-radius: 18px !important;
  background:
    radial-gradient(circle at 88% 0, rgba(20, 184, 166, .18), transparent 22rem),
    linear-gradient(118deg, var(--dv-navy-950), #123a58 70%, #0e6467) !important;
  box-shadow: var(--dv-shadow-lg) !important;
}
#page-assistant .native-ai-title { color: #fff !important; }
#page-assistant .native-ai-subtitle { color: #c4d4e1 !important; }
#page-assistant .native-ai-kicker { border-color: rgba(153, 246, 228, .25) !important; background: rgba(20, 184, 166, .12) !important; color: #99f6e4 !important; }
#page-assistant .native-ai-disclaimer { border-color: rgba(255, 255, 255, .13) !important; background: rgba(255, 255, 255, .07) !important; color: #adbfce !important; }
#page-assistant .native-ai-control {
  border-color: rgba(190, 222, 238, .3) !important;
  border-radius: 11px !important;
  background: linear-gradient(180deg, rgba(7, 34, 53, .62), rgba(8, 46, 65, .5)) !important;
  color: #f2f8fc !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .05) !important;
}
#page-assistant .native-ai-control-label {
  color: #f2f8fc !important;
  text-shadow: 0 1px 1px rgba(0, 0, 0, .24) !important;
}
#page-assistant .native-ai-control select,
#page-assistant .native-ai-cloud-toggle {
  border-color: rgba(196, 222, 236, .34) !important;
  background: #0a2d47 !important;
  color: #fff !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .06) !important;
}
#page-assistant .native-ai-control select option { background: #fff !important; color: #12283c !important; }
#page-assistant .native-ai-control-hint { color: #c6dbe9 !important; }
#page-assistant .native-ai-workbench { grid-template-columns: minmax(0, 1fr) minmax(350px, 410px) !important; gap: 14px !important; }
#page-assistant .native-ai-messages,
#page-assistant .native-ai-composer {
  border: 1px solid var(--dv-line) !important;
  border-radius: 16px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-assistant .native-ai-empty-card,
#page-assistant .native-ai-msg.assistant .native-ai-bubble,
#page-assistant .native-ai-export-panel {
  border-color: var(--dv-line) !important;
  border-radius: 13px !important;
  background: var(--dv-panel-soft) !important;
  box-shadow: none !important;
}
#page-assistant .native-ai-msg.user .native-ai-bubble { border-radius: 13px 13px 3px 13px !important; background: linear-gradient(135deg, var(--dv-blue-600), #1d4ed8) !important; }
#page-assistant .native-ai-assistant button.native-ai-suggestion { border-color: #d7e3ed !important; border-radius: 10px !important; background: #fff !important; }

/* Report workspace */
#page-report .report-workspace-grid,
#page-report .report-workspace-grid > .form {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) !important;
  gap: 14px !important;
  align-items: stretch !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-command-column,
#page-report .report-preview-column { display: grid !important; width: 100% !important; gap: 14px !important; min-width: 0 !important; }
#page-report .report-workspace-grid:has(.report-empty-state),
#page-report .report-workspace-grid:has(.report-empty-state) > .form { align-items: stretch !important; }
#page-report .report-workspace-grid:has(.report-empty-state) .report-command-column,
#page-report .report-workspace-grid:has(.report-empty-state) .report-command-panel { height: 100% !important; }
#page-report .report-command-panel,
#page-report .report-recent-panel,
#page-report .report-preview-column {
  padding: 16px !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 15px !important;
  background: #fff !important;
  box-shadow: var(--dv-shadow-sm) !important;
}
#page-report .report-command-panel > .form,
#page-report .report-recent-panel > .form {
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-command-panel { border-top: 4px solid var(--dv-teal-500) !important; }
#page-report .report-preview-column { border-top: 4px solid var(--dv-cyan-500) !important; }
#page-report .report-recent-panel { margin-top: 14px !important; }
#page-report .report-controls-row {
  display: block !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: 9px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-controls-row > .styler,
#page-report .report-controls-row > .form,
#page-report .report-controls-row > .styler > .form {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(220px, 1fr)) !important;
  align-items: end !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: 9px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-controls-row > .styler { grid-column: 1 / -1 !important; }
#page-report .report-controls-row > .form > *,
#page-report .report-controls-row > .styler > .form > * { width: 100% !important; max-width: none !important; min-width: 0 !important; }
#page-report .report-command-panel .workspace-panel-heading { margin-bottom: 6px !important; }
#page-report .report-command-panel .report-controls-row { align-content: start !important; }
#page-report .report-generate-action { align-self: end !important; width: 100% !important; min-height: 52px !important; margin: 0 !important; }
#page-report .report-generate-action button { width: 100% !important; min-height: 52px !important; }
#page-report .report-preview-panel {
  min-height: 360px !important;
  margin: 0 !important;
  overflow: auto !important;
  border: 1px solid #dbe4ed !important;
  border-radius: 12px !important;
  background: #fbfcfe !important;
  box-shadow: inset 0 1px 0 #fff !important;
}
#page-report .report-preview-panel .prose { max-width: 920px !important; margin: 0 auto !important; padding: 22px !important; }
#page-report .report-preview-panel:has(.report-empty-state) {
  display: grid !important;
  min-height: 360px !important;
  place-items: center !important;
  overflow: hidden !important;
  border-style: dashed !important;
  border-color: #cbd9e4 !important;
  background:
    radial-gradient(circle at 50% 18%, rgba(14, 165, 233, .08), transparent 13rem),
    linear-gradient(180deg, #fbfdff, #f7fafc) !important;
}
#page-report .report-preview-panel:has(.report-empty-state) .prose {
  width: 100% !important;
  max-width: none !important;
  padding: 18px !important;
}
#page-report .report-empty-state {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-direction: column !important;
  min-height: 300px !important;
  max-width: 560px !important;
  margin: 0 auto !important;
  padding: 18px 28px !important;
  text-align: center !important;
}
#page-report .report-empty-icon {
  position: relative !important;
  display: grid !important;
  place-items: end center !important;
  width: 54px !important;
  height: 64px !important;
  margin-bottom: 13px !important;
  padding-bottom: 9px !important;
  border: 2px solid #91bad3 !important;
  border-radius: 9px !important;
  background: linear-gradient(145deg, #fff, #eaf5fb) !important;
  color: #16739b !important;
  box-shadow: 0 10px 24px rgba(20, 96, 132, .12) !important;
}
#page-report .report-empty-icon::before {
  content: "" !important;
  position: absolute !important;
  top: -2px !important;
  right: -2px !important;
  width: 17px !important;
  height: 17px !important;
  border-bottom: 2px solid #91bad3 !important;
  border-left: 2px solid #91bad3 !important;
  border-radius: 0 7px 0 5px !important;
  background: #dff1f8 !important;
}
#page-report .report-empty-icon span { font-size: 9px !important; font-weight: 900 !important; letter-spacing: .08em !important; }
#page-report .report-empty-kicker {
  margin: 0 0 5px !important;
  color: #0f7b83 !important;
  font-size: 10px !important;
  font-weight: 850 !important;
  letter-spacing: .12em !important;
}
#page-report .report-empty-state h4 {
  margin: 0 !important;
  color: var(--dv-navy-900) !important;
  font-size: 19px !important;
  font-weight: 900 !important;
}
#page-report .report-empty-description {
  max-width: 460px !important;
  margin: 8px 0 14px !important;
  color: #60778a !important;
  font-size: 12px !important;
  line-height: 1.7 !important;
}
#page-report .report-empty-formats { display: flex !important; justify-content: center !important; flex-wrap: wrap !important; gap: 7px !important; }
#page-report .report-empty-formats span {
  min-width: 66px !important;
  padding: 5px 10px !important;
  border: 1px solid #d4e2eb !important;
  border-radius: 999px !important;
  background: rgba(255, 255, 255, .82) !important;
  color: #49677d !important;
  font-size: 10px !important;
  font-weight: 800 !important;
}
#page-report .report-download-row,
#page-report .report-download-row > .form {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 8px !important;
  margin: 0 !important;
  padding: 10px 0 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-report .report-download-action { min-width: 0 !important; }
#page-report .report-recent-empty {
  display: grid !important;
  min-height: 86px !important;
  place-items: center !important;
  border: 1px dashed #d4e0e9 !important;
  border-radius: 11px !important;
  background: #f8fafc !important;
  color: #708596 !important;
  font-size: 12px !important;
}
#page-report .report-recent-list {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 8px 14px !important;
  border: 0 !important;
  border-radius: 0 !important;
  background: transparent !important;
}
#page-report .report-recent-list > header { grid-column: 1 / -1; }
#page-report .report-recent-item { grid-template-columns: auto minmax(0, 1fr) auto !important; gap: 8px !important; padding: 9px 0 !important; border-bottom: 1px solid #edf1f5 !important; }
#page-report .report-cover-mini { border-radius: 8px !important; background: var(--dv-blue-soft) !important; color: var(--dv-blue-600) !important; }
#page-report .report-source-overview-panel,
#page-report .report-source-overview-panel .html-container { margin: 0 !important; padding: 0 !important; }
#page-report .report-source-overview {
  display: grid;
  gap: 10px;
  margin: 10px 0 12px;
  padding: 12px;
  border: 1px solid #dbe6ee;
  border-radius: 12px;
  background: #f8fbfc;
}
#page-report .report-source-overview-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
#page-report .report-source-overview-head > div { display: grid; gap: 2px; }
#page-report .report-source-overview-head b { color: #18364c; font-size: 12px; font-weight: 900; }
#page-report .report-source-overview-head span { color: #718697; font-size: 10px; }
#page-report .report-source-overview-head em {
  padding: 4px 8px;
  border: 1px solid #bfe7df;
  border-radius: 999px;
  background: #edfdf8;
  color: #0f766e;
  font-size: 9px;
  font-style: normal;
  font-weight: 850;
}
#page-report .report-source-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 7px; }
#page-report .report-source-card {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 9px;
  min-height: 54px;
  padding: 8px 9px;
  border: 1px solid #dfe8ef;
  border-radius: 10px;
  background: #fff;
}
#page-report .report-source-card.is-ready { border-color: #b9e2d9; background: #f6fffc; }
#page-report .report-source-index {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: #eef3f7;
  color: #718397;
  font-size: 9px;
  font-weight: 900;
}
#page-report .report-source-card.is-ready .report-source-index { background: #dff8f1; color: #0f766e; }
#page-report .report-source-card > div { display: grid; gap: 2px; min-width: 0; }
#page-report .report-source-card b { color: #243d52; font-size: 11px; }
#page-report .report-source-card small { overflow: hidden; color: #778b9b; font-size: 9px; text-overflow: ellipsis; white-space: nowrap; }
#page-report .report-source-card strong { color: #8b9aa7; font-size: 9px; }
#page-report .report-source-card.is-ready strong { color: #0f766e; }
#page-report .report-source-note { margin: 0; color: #6e8292; font-size: 10px; line-height: 1.55; }
#page-report .report-archive-grid,
#page-report .report-archive-grid > .form {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) !important;
  gap: 14px !important;
  align-items: stretch !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-report .report-archive-grid > .form {
  grid-column: 1 / -1 !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  background: transparent !important;
}
#page-report .report-archive-command {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) !important;
  align-items: stretch !important;
  gap: 9px !important;
  min-width: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: #fff !important;
  box-shadow: none !important;
}
#page-report .report-archive-toolbar,
#page-report .report-archive-toolbar > .form {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) auto !important;
  align-items: end !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: 9px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-archive-toolbar > .form { grid-column: 1 / -1 !important; }
#page-report .report-archive-preview-column { display: grid !important; width: 100% !important; gap: 9px !important; min-width: 0 !important; }
#page-report .report-archive-selector { min-width: 0 !important; }
#page-report .report-archive-refresh { min-width: 132px !important; min-height: 38px !important; }
#page-report .report-archive-summary-panel,
#page-report .report-archive-download-row { grid-column: 1 / -1 !important; }
#page-report .report-archive-summary {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding: 11px;
  border: 1px solid #dce6ed;
  border-radius: 11px;
  background: #f8fafc;
}
#page-report .report-archive-summary > div { display: grid; gap: 3px; min-width: 0; }
#page-report .report-archive-summary small { color: #8091a0; font-size: 9px; }
#page-report .report-archive-summary b { overflow: hidden; color: #263f55; font-size: 11px; text-overflow: ellipsis; white-space: nowrap; }
#page-report .report-archive-formats { grid-column: 1 / -1; }
#page-report .report-archive-formats p { display: flex; flex-wrap: wrap; gap: 5px; margin: 0; }
#page-report .report-archive-formats span { padding: 3px 7px; border-radius: 999px; background: #eaf2ff; color: #2563eb; font-size: 9px; font-weight: 850; }
#page-report .report-archive-empty { display: grid; gap: 4px; padding: 18px; border: 1px dashed #cedce6; border-radius: 11px; background: #f8fafc; text-align: center; }
#page-report .report-archive-empty b { color: #3b5266; font-size: 12px; }
#page-report .report-archive-empty span { color: #8192a0; font-size: 10px; }
#page-report .report-archive-download-row,
#page-report .report-archive-download-row > .form {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 7px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
}
#page-report .report-archive-download-row button { min-width: 0 !important; min-height: 38px !important; padding-inline: 8px !important; }
#page-report .report-archive-preview {
  min-height: 280px !important;
  max-height: 560px !important;
  overflow: auto !important;
  border: 1px solid #dbe4ed !important;
  border-radius: 12px !important;
  background: #fbfcfe !important;
}
#page-report .report-archive-preview .prose { max-width: 900px !important; margin: 0 auto !important; padding: 18px !important; }

/* Tables and galleries */
.gradio-container .table-wrap,
.gradio-container .table-container {
  overflow: auto !important;
  border: 1px solid var(--dv-line) !important;
  border-radius: 11px !important;
  background: #fff !important;
}
.gradio-container table thead th {
  padding: 11px 12px !important;
  border-color: #dde6ee !important;
  background: #edf3f8 !important;
  color: #29425b !important;
  font-size: 11px !important;
  font-weight: 850 !important;
}
.gradio-container table tbody td { padding: 10px 12px !important; border-color: #edf1f5 !important; }
.gradio-container table tbody tr:nth-child(even) td { background: #fafcfd !important; }
.gradio-container table tbody tr:hover td { background: var(--dv-blue-soft) !important; }

/* Responsive behavior */
@media (max-width: 1260px) {
  .app-hero-top { grid-template-columns: minmax(0, 1fr) 340px !important; }
  .dental-nav-copy small { display: none; }
  .dental-page-nav-item { justify-content: center !important; gap: 6px !important; }
  #page-compare .compare-model-grid,
  #page-compare .compare-model-grid > .form { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
  #page-compare .compare-model-recall { grid-column: 1 / -1 !important; }
}
@media (max-width: 1040px) {
  .app-hero-top { grid-template-columns: 1fr !important; gap: 16px !important; }
  .app-hero-status { grid-template-columns: minmax(220px, .7fr) minmax(0, 1fr); align-items: stretch; }
  .dental-nav-items { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .dental-nav-copy small { display: block; }
  .dental-page-nav-item { justify-content: flex-start !important; }
  #page-image .detection-workbench,
  #page-compare .detection-workbench,
  #page-batch .detection-workbench,
  #page-image .single-result-overview,
  #page-image .single-result-overview > .form,
  #page-batch .batch-review-grid,
  #page-batch .batch-review-grid > .form,
  #page-history .history-command-deck,
  #page-history .history-command-deck > .form,
  #page-history .history-detail-workspace,
  #page-history .history-detail-workspace > .form,
  #page-report .report-workspace-grid,
  #page-report .report-workspace-grid > .form,
  #page-report .report-archive-grid,
  #page-report .report-archive-grid > .form { grid-template-columns: 1fr !important; }
  #page-history .history-control-panel { order: -1; }
  #page-report .report-command-column { grid-template-columns: 1fr !important; align-items: start !important; }
  #page-assistant .native-ai-top { grid-template-columns: 1fr !important; }
  #page-assistant .native-ai-controls { min-width: 0 !important; }
  #page-learn .education-toolbar { position: static !important; top: auto !important; }
}
@media (max-width: 760px) {
  html,
  body,
  .gradio-container,
  .gradio-container > div,
  .gradio-container .main,
  .gradio-container .wrap { min-width: 0 !important; max-width: 100vw !important; }
  html,
  body,
  .gradio-container { overflow-x: hidden !important; }
  .gradio-container { width: 100vw !important; padding: 7px 7px 28px !important; box-sizing: border-box !important; }
  .column:has(> .block:first-child .app-hero) {
    flex: 0 0 calc(100% + 48px) !important;
    width: calc(100% + 48px) !important;
    max-width: calc(100% + 48px) !important;
    margin-left: -24px !important;
    margin-right: -24px !important;
  }
  .app-hero,
  .dental-page-nav,
  .dental-page { width: 100% !important; max-width: 100% !important; box-sizing: border-box !important; margin-left: 0 !important; margin-right: 0 !important; }
  .app-hero { min-height: 0; padding: 18px !important; border-radius: 15px !important; }
  .app-brand-lockup { align-items: flex-start; gap: 13px; }
  .app-brand-mark { flex-basis: 52px; width: 52px; height: 52px; border-radius: 14px; }
  .app-brand-mark svg { width: 34px; height: 34px; }
  .app-hero h1 { max-width: 100% !important; overflow-wrap: anywhere !important; font-size: 23px !important; }
  .app-hero-status { grid-template-columns: 1fr; }
  .app-live-status { display: none; }
  .dental-page-nav { top: 4px !important; padding: 6px !important; border-radius: 13px !important; }
  .dental-nav-toggle {
    display: flex !important;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    min-height: 48px;
    padding: 7px 10px;
    border: 0;
    border-radius: 9px;
    background: var(--dv-navy-900);
    color: #fff;
    text-align: left;
  }
  .dental-nav-toggle > span { display: grid; gap: 1px; }
  .dental-nav-toggle b { font-size: 12px; }
  .dental-nav-toggle small { color: #adc1d1; font-size: 9px; }
  .dental-nav-toggle strong { font-size: 19px; }
  .dental-nav-items { display: none !important; grid-template-columns: repeat(2, minmax(0, 1fr)); padding-top: 6px; }
  .dental-page-nav.nav-open .dental-nav-items { display: grid !important; }
  .dental-page-nav-item { min-height: 48px !important; }
  .workspace-page-hero,
  .detection-page-hero { grid-template-columns: auto minmax(0, 1fr); min-height: 0; padding: 17px !important; border-radius: 15px !important; }
  .workspace-page-index { width: 46px; height: 46px; border-radius: 12px; }
  .workspace-page-badges,
  .detection-page-badges { grid-column: 1 / -1; justify-content: flex-start !important; max-width: none; }
  .workspace-page-copy h2,
  .detection-page-hero-copy h2 { font-size: 25px !important; }
  .detection-workflow { padding: 5px !important; }
  .detection-workflow li { gap: 4px; min-height: 38px; font-size: 10px !important; }
  .detection-workflow li span { width: 20px; height: 20px; }
  #page-image .detection-workbench,
  #page-compare .detection-workbench,
  #page-batch .detection-workbench { grid-template-columns: 1fr !important; }
  #page-compare .compare-model-grid,
  #page-compare .compare-model-grid > .form { grid-template-columns: 1fr !important; }
  #page-compare .compare-model-recall { grid-column: 1 !important; }
  #page-image .single-result-overview,
  #page-image .structured-result-panel,
  #page-image .detection-support-review-only,
  #page-image .detection-report-panel,
  #page-compare .compare-result-models-panel,
  #page-compare .compare-result-analysis-panel,
  #page-compare .detection-support-review-only,
  #page-compare .detection-report-panel,
  #page-batch .batch-review-grid,
  #page-batch .structured-result-panel,
  #page-batch .detection-support-review-only,
  #page-batch .detection-report-panel { margin-inline: 8px !important; padding: 10px !important; }
  .linked-region-row,
  .linked-region-row > .form { grid-template-columns: 1fr !important; }
  #page-dashboard .dashboard-actions-row { display: grid !important; grid-template-columns: 1fr !important; }
  #page-dashboard .dashboard-actions-row > * { min-width: 0 !important; width: 100% !important; }
  #page-report .report-command-column { grid-template-columns: 1fr !important; }
  #page-report .report-controls-row,
  #page-report .report-controls-row > .styler,
  #page-report .report-controls-row > .form,
  #page-report .report-controls-row > .styler > .form,
  #page-report .report-archive-command,
  #page-report .report-archive-toolbar,
  #page-report .report-archive-toolbar > .form { grid-template-columns: 1fr !important; }
  #page-report .report-source-grid { grid-template-columns: 1fr !important; }
  #page-report .report-archive-refresh,
  #page-report .report-archive-summary-panel,
  #page-report .report-archive-download-row { grid-column: 1 !important; width: 100% !important; }
  #page-report .report-download-row,
  #page-report .report-download-row > .form { grid-template-columns: 1fr !important; }
  #page-report .report-preview-panel,
  #page-report .report-preview-panel:has(.report-empty-state) { min-height: 300px !important; }
  #page-report .report-empty-state { min-height: 250px !important; padding: 14px !important; }
  #page-report .report-recent-list { grid-template-columns: 1fr !important; }
  #page-history .history-action-row,
  #page-history .history-action-row > .form { grid-template-columns: 1fr !important; }
  #page-history .history-pagination-bar,
  #page-history .history-pagination-bar > .form {
    align-items: stretch !important;
    flex-direction: column !important;
    gap: 8px !important;
  }
  #page-history .history-pagination,
  #page-history .history-pagination > .form {
    justify-content: center !important;
    flex-wrap: wrap !important;
    gap: 6px !important;
  }
  #page-history #history-page-feedback { text-align: center !important; }
  #page-history .history-pagination button { min-width: 78px !important; }
  #page-assistant .native-ai-top { padding: 17px !important; }
  #page-assistant .native-ai-controls { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
  #page-assistant .native-ai-workbench { grid-template-columns: 1fr !important; }
}
@media (max-width: 460px) {
  .app-hero-facts { grid-template-columns: 1fr 1fr; }
  .app-hero-facts > span:last-child { grid-column: 1 / -1; }
  .dental-nav-items { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .workspace-page-hero,
  .detection-page-hero { grid-template-columns: 1fr; }
  .workspace-page-index { width: 42px; height: 42px; }
  .workspace-page-badges span,
  .detection-page-badges span { min-height: 27px; }
  .detection-workflow li b { display: none; }
  #page-history .history-pagination button { min-width: 72px !important; padding-inline: 10px !important; }
  #page-history #history-page-input { flex-basis: 64px !important; width: 64px !important; min-width: 64px !important; max-width: 64px !important; }
  #page-assistant .native-ai-controls { grid-template-columns: 1fr !important; }
}
@media (max-width: 460px) {
  .ask-ai-selection-brand-copy small { display: none; }
  #ask-ai-selection-send span { display: none; }
  #ask-ai-selection-send { min-width: 46px; padding-inline: 10px; }
  .ask-ai-selection-context { grid-template-columns: auto minmax(0, 1fr); padding-right: 32px; }
  #ask-ai-selection-feedback { grid-column: 1 / -1; }
}

/* Report center: compact two-stage workspace */
#page-report .report-command-panel,
#page-report .report-command-panel > .form {
  display: grid !important;
  grid-template-columns: minmax(230px, .36fr) minmax(0, 1.64fr) !important;
  grid-template-areas:
    "report-intro report-sources"
    "report-intro report-actions" !important;
  align-items: stretch !important;
  gap: 12px 18px !important;
}
#page-report .report-command-panel {
  padding: 18px !important;
  overflow: hidden !important;
  border: 1px solid #d6e3eb !important;
  border-top: 4px solid #16b8a7 !important;
  border-radius: 16px !important;
  background: #f6fafc !important;
  box-shadow: 0 8px 26px rgba(31, 59, 82, .07) !important;
}
#page-report .report-command-panel > .form {
  grid-column: 1 / -1 !important;
  width: 100% !important;
  padding: 0 !important;
  background: transparent !important;
}
#page-report .report-command-heading {
  grid-area: report-intro !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-command-heading .html-container { height: 100% !important; margin: 0 !important; padding: 0 !important; }
#page-report .report-command-heading .workspace-panel-heading {
  position: relative !important;
  display: flex !important;
  align-items: flex-start !important;
  justify-content: center !important;
  flex-direction: column !important;
  height: 100% !important;
  min-height: 156px !important;
  margin: 0 !important;
  padding: 20px !important;
  overflow: hidden !important;
  border: 0 !important;
  border-radius: 14px !important;
  background: linear-gradient(145deg, #0c2940 0%, #123c55 62%, #0f766e 140%) !important;
  box-shadow: 0 14px 30px rgba(12, 41, 64, .16) !important;
}
#page-report .report-command-heading .workspace-panel-heading::after {
  content: "" !important;
  position: absolute !important;
  right: -34px !important;
  bottom: -42px !important;
  width: 132px !important;
  height: 132px !important;
  border: 22px solid rgba(255, 255, 255, .06) !important;
  border-radius: 50% !important;
}
#page-report .report-command-heading .workspace-panel-heading > span {
  position: relative !important;
  z-index: 1 !important;
  margin-bottom: 16px !important;
  border-color: rgba(125, 211, 252, .28) !important;
  background: rgba(255, 255, 255, .1) !important;
  color: #9fe7df !important;
}
#page-report .report-command-heading .workspace-panel-heading > div { position: relative !important; z-index: 1 !important; }
#page-report .report-command-heading .workspace-panel-heading h3 { margin: 0 !important; color: #fff !important; font-size: 20px !important; }
#page-report .report-command-heading .workspace-panel-heading p { max-width: 290px !important; margin-top: 7px !important; color: #c2d6e3 !important; line-height: 1.65 !important; }
#page-report .report-source-overview-panel { grid-area: report-sources !important; min-width: 0 !important; }
#page-report .report-source-overview {
  height: 100% !important;
  margin: 0 !important;
  padding: 13px 14px !important;
  border: 1px solid #dce8ee !important;
  border-radius: 13px !important;
  background: #fff !important;
}
#page-report .report-source-overview-head b { font-size: 13px !important; }
#page-report .report-source-overview-head span { font-size: 11px !important; }
#page-report .report-source-overview-head em { padding: 5px 9px !important; font-size: 10px !important; }
#page-report .report-source-grid { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; gap: 9px !important; }
#page-report .report-source-card { min-height: 60px !important; padding: 10px !important; border-radius: 11px !important; }
#page-report .report-source-card b { font-size: 12px !important; }
#page-report .report-source-card small,
#page-report .report-source-note { font-size: 10px !important; }
#page-report .report-source-card strong { font-size: 10px !important; }
#page-report .report-controls-row { grid-area: report-actions !important; }
#page-report .report-controls-row,
#page-report .report-controls-row > .form,
#page-report .report-controls-row > .styler,
#page-report .report-controls-row > .styler > .form {
  display: grid !important;
  grid-template-columns: minmax(200px, 280px) minmax(220px, 300px) !important;
  justify-content: end !important;
  align-items: end !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: 10px !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-controls-row > .form,
#page-report .report-controls-row > .styler { grid-column: 1 / -1 !important; }
#page-report .report-generate-action,
#page-report .report-generate-action button { min-height: 50px !important; border-radius: 10px !important; }

#page-report .report-preview-column {
  padding: 18px !important;
  border-radius: 16px !important;
  box-shadow: 0 8px 26px rgba(31, 59, 82, .07) !important;
}
#page-report .report-preview-heading,
#page-report .report-preview-heading .html-container,
#page-report .report-archive-heading,
#page-report .report-archive-heading .html-container {
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}
#page-report .report-preview-panel { min-height: 320px !important; border-radius: 13px !important; }
#page-report .report-preview-panel:has(.report-empty-state) { min-height: 260px !important; }
#page-report .report-empty-state { min-height: 210px !important; }

#page-report .report-archive-panel {
  margin-top: 16px !important;
  padding: 18px !important;
  overflow: hidden !important;
  border: 1px solid #d6e3eb !important;
  border-top: 4px solid #0ea5e9 !important;
  border-radius: 16px !important;
  background: #fff !important;
  box-shadow: 0 8px 26px rgba(31, 59, 82, .07) !important;
}
#page-report .report-archive-panel::before,
#page-report .report-archive-panel::after,
#page-report .report-command-panel::before,
#page-report .report-command-panel::after { display: none !important; }
#page-report .report-archive-heading .workspace-panel-heading {
  margin: 0 0 14px !important;
  padding: 0 0 14px !important;
  border-bottom: 1px solid #e4ecf1 !important;
}
#page-report .report-archive-grid,
#page-report .report-archive-grid > .form {
  gap: 12px !important;
  padding: 0 !important;
  background: transparent !important;
}
#page-report .report-archive-grid > .form { grid-column: 1 / -1 !important; }
#page-report .report-archive-command {
  gap: 10px !important;
  padding: 13px !important;
  border: 1px solid #dce8ee !important;
  border-radius: 13px !important;
  background: #f7fbfd !important;
}
#page-report .report-archive-toolbar,
#page-report .report-archive-toolbar > .form {
  grid-template-columns: minmax(0, 1fr) 142px !important;
  gap: 10px !important;
}
#page-report .report-archive-toolbar > .form { grid-column: 1 / -1 !important; }
#page-report .report-archive-refresh,
#page-report .report-archive-refresh button { width: 100% !important; min-width: 0 !important; min-height: 48px !important; border-radius: 10px !important; }
#page-report .report-archive-summary-panel,
#page-report .report-archive-summary-panel .html-container { margin: 0 !important; padding: 0 !important; }
#page-report .report-archive-summary {
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
  border: 1px solid #dce6ed !important;
  border-radius: 11px !important;
  background: #fff !important;
}
#page-report .report-archive-summary > div {
  min-height: 62px !important;
  padding: 11px 13px !important;
  border-right: 1px solid #e6edf2 !important;
}
#page-report .report-archive-summary > div:last-child { border-right: 0 !important; }
#page-report .report-archive-summary small { font-size: 10px !important; }
#page-report .report-archive-summary b { font-size: 12px !important; }
#page-report .report-archive-formats { grid-column: auto !important; }
#page-report .report-archive-download-row,
#page-report .report-archive-download-row > .form {
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 8px !important;
}
#page-report .report-archive-download-row > .form { grid-column: 1 / -1 !important; }
#page-report .report-archive-download-row button {
  min-height: 42px !important;
  border: 1px solid #cfe0eb !important;
  border-radius: 9px !important;
  background: #fff !important;
  color: #29425b !important;
  box-shadow: none !important;
}
#page-report .report-archive-download-row button:hover { border-color: #7db9dd !important; background: #eff8fd !important; }
#page-report .report-archive-preview-column {
  gap: 12px !important;
  padding-top: 2px !important;
  background: #fff !important;
}
#page-report .report-archive-preview {
  max-height: 680px !important;
  border-radius: 13px !important;
  background: #fff !important;
}
#page-report .report-archive-preview-column .gallery { border: 1px solid #dce6ed !important; border-radius: 13px !important; background: #f8fbfd !important; }

@media (max-width: 1040px) {
  #page-report .report-command-panel,
  #page-report .report-command-panel > .form {
    grid-template-columns: 1fr !important;
    grid-template-areas:
      "report-intro"
      "report-sources"
      "report-actions" !important;
  }
  #page-report .report-command-heading .workspace-panel-heading { min-height: 132px !important; }
}
@media (max-width: 760px) {
  #page-report .report-command-panel,
  #page-report .report-preview-column,
  #page-report .report-archive-panel { padding: 12px !important; border-radius: 13px !important; }
  #page-report .report-source-grid,
  #page-report .report-controls-row,
  #page-report .report-controls-row > .form,
  #page-report .report-controls-row > .styler,
  #page-report .report-controls-row > .styler > .form,
  #page-report .report-archive-toolbar,
  #page-report .report-archive-toolbar > .form { grid-template-columns: 1fr !important; }
  #page-report .report-archive-summary { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
  #page-report .report-archive-summary > div:nth-child(2) { border-right: 0 !important; }
  #page-report .report-archive-summary > div:nth-child(-n + 2) { border-bottom: 1px solid #e6edf2 !important; }
  #page-report .report-archive-download-row,
  #page-report .report-archive-download-row > .form { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
}
@media (max-width: 460px) {
  #page-report .report-archive-summary,
  #page-report .report-archive-download-row,
  #page-report .report-archive-download-row > .form { grid-template-columns: 1fr !important; }
  #page-report .report-archive-summary > div { border-right: 0 !important; border-bottom: 1px solid #e6edf2 !important; }
  #page-report .report-archive-summary > div:last-child { border-bottom: 0 !important; }
}

/* Report center: action visibility and natural-height correction */
#page-report .report-workspace-grid,
#page-report .report-workspace-grid > .form { align-items: start !important; }
#page-report .report-workspace-grid:has(.report-empty-state) .report-command-column,
#page-report .report-workspace-grid:has(.report-empty-state) .report-command-panel,
#page-report .report-command-column,
#page-report .report-command-panel {
  align-self: start !important;
  height: auto !important;
  min-height: 0 !important;
}
#page-report .report-controls-row,
#page-report .report-controls-row > .form,
#page-report .report-controls-row > .styler,
#page-report .report-controls-row > .styler > .form {
  display: flex !important;
  align-items: flex-end !important;
  justify-content: flex-end !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  width: 100% !important;
  max-width: none !important;
  min-width: 0 !important;
  gap: 10px !important;
}
#page-report .report-controls-row > .form,
#page-report .report-controls-row > .styler { flex: 1 1 100% !important; }
#page-report .report-language-control {
  flex: 1 1 260px !important;
  width: auto !important;
  max-width: 320px !important;
  min-width: 220px !important;
  margin: 0 !important;
}
#page-report .report-generate-action,
#page-report button.report-generate-action,
#page-report .report-generate-action button {
  flex: 0 0 260px !important;
  width: 260px !important;
  max-width: 260px !important;
  min-width: 260px !important;
  min-height: 50px !important;
  margin: 0 !important;
  border: 1px solid #0b4f70 !important;
  border-radius: 10px !important;
  background: linear-gradient(135deg, #103f60 0%, #0f6280 100%) !important;
  color: #fff !important;
  font-weight: 850 !important;
  opacity: 1 !important;
  box-shadow: 0 9px 20px rgba(15, 79, 112, .2) !important;
}
#page-report .report-generate-action *,
#page-report button.report-generate-action * { color: #fff !important; opacity: 1 !important; }
#page-report .report-generate-action:hover,
#page-report button.report-generate-action:hover,
#page-report .report-generate-action button:hover {
  border-color: #083c58 !important;
  background: linear-gradient(135deg, #0b3552 0%, #0d5874 100%) !important;
}
#page-report .report-preview-panel:has(.report-empty-state) { min-height: 230px !important; }
#page-report .report-empty-state { min-height: 180px !important; }

@media (max-width: 760px) {
  #page-report .report-controls-row,
  #page-report .report-controls-row > .form,
  #page-report .report-controls-row > .styler,
  #page-report .report-controls-row > .styler > .form {
    align-items: stretch !important;
    flex-direction: column !important;
  }
  #page-report .report-language-control,
  #page-report .report-generate-action,
  #page-report button.report-generate-action,
  #page-report .report-generate-action button {
    flex: 1 1 auto !important;
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
  }
}

/* Detection linked review: large, complete and equally sized source/result crops. */
.detection-support-review-only .linked-region-row,
.detection-support-review-only .linked-region-row > .form {
  align-items: stretch !important;
  width: min(100%, 1280px) !important;
  max-width: 1280px !important;
  margin: 14px auto 10px !important;
  overflow: visible !important;
}
.detection-support-review-only .linked-region-row > *,
.detection-support-review-only .linked-region-row > .form > * {
  align-self: stretch !important;
  overflow: visible !important;
}
.detection-support-review-only .linked-region-image {
  height: clamp(360px, 28vw, 440px) !important;
  min-height: 360px !important;
  overflow: visible !important;
  border: 1px solid #cbdfe7 !important;
  border-radius: 13px !important;
  background: #eef4f7 !important;
  box-shadow: 0 8px 20px rgba(15, 43, 63, .08) !important;
}
.detection-support-review-only .linked-region-image .image-container,
.detection-support-review-only .linked-region-image .image-frame {
  width: 100% !important;
  height: 100% !important;
  min-height: 0 !important;
  background: #eef4f7 !important;
}
.detection-support-review-only .linked-region-image .image-frame img,
.detection-support-review-only .linked-region-image .image-container:fullscreen img {
  width: 100% !important;
  height: 100% !important;
  max-width: 100% !important;
  max-height: 100% !important;
  object-fit: contain !important;
  object-position: center !important;
  image-rendering: auto !important;
}
.detection-support-review-only .linked-region-image .image-container:fullscreen {
  width: 100vw !important;
  height: 100vh !important;
  background: #07131d !important;
}

@media (max-width: 900px) {
  :is(#page-image, #page-compare, #page-batch) .detection-support-review-only .linked-region-row,
  :is(#page-image, #page-compare, #page-batch) .detection-support-review-only .linked-region-row > .form {
    grid-template-columns: 1fr !important;
  }
  .detection-support-review-only .linked-region-image {
    height: clamp(280px, 58vw, 380px) !important;
    min-height: 280px !important;
  }
}

@media (max-width: 460px) {
  .detection-support-review-only .linked-region-image {
    height: clamp(240px, 70vw, 310px) !important;
    min-height: 240px !important;
  }
}
"""
