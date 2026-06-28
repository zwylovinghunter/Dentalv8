from __future__ import annotations

ASK_AI_HEAD = r"""
<script>
(function () {
  if (window.__dentalAskAiInstalledV6) return;
  window.__dentalAskAiInstalledV6 = true;
  window.__dentalAskAiInstalledV5 = true;
  window.__dentalAskAiInstalledV4 = true;
  window.__dentalAskAiInstalledV3 = true;
  window.__dentalAskAiInstalledV2 = true;
  window.__dentalAskAiInstalled = true;

  function selectedText() {
    const text = (window.getSelection && window.getSelection().toString() || "").trim();
    return text.replace(/\s+/g, " ").slice(0, 1200);
  }

  const DENTAL_PAGES = new Set(["learn", "dashboard", "image", "compare", "batch", "history", "assistant", "report"]);
  const DENTAL_I18N = {
    zh: {
      app_title: "牙齿病变目标区域识别与辅助分析平台",
      app_subtitle: "面向口腔影像的疑似牙齿病变区域辅助识别、模型对比与报告生成系统。",
      nav_learn: "牙病学习",
      nav_dashboard: "首页 Dashboard",
      nav_image: "图像检测",
      nav_compare: "多模型对比",
      nav_batch: "批量检测",
      nav_history: "历史记录",
      nav_assistant: "智诊管家",
      nav_report: "报告中心"
    },
    en: {
      app_title: "Dental Lesion Candidate-region Detection Platform",
      app_subtitle: "Auxiliary recognition, model comparison and report generation for dental and oral images.",
      nav_learn: "Learning",
      nav_dashboard: "Dashboard",
      nav_image: "Single Image",
      nav_compare: "Model Review",
      nav_batch: "Batch Screening",
      nav_history: "History",
      nav_assistant: "AI Assistant",
      nav_report: "Reports"
    }
  };

  function applyDentalLanguage(lang) {
    const next = lang === "en" ? "en" : "zh";
    const copy = DENTAL_I18N[next] || DENTAL_I18N.zh;
    document.body.dataset.dentalLang = next;
    document.documentElement.lang = next === "en" ? "en" : "zh-CN";
    document.querySelectorAll("[data-i18n]").forEach(node => {
      const key = node.dataset.i18n;
      if (copy[key]) node.textContent = copy[key];
    });
    const toggle = document.getElementById("dental-lang-toggle");
    if (toggle) {
      toggle.textContent = next === "en" ? "中文" : "EN";
      toggle.title = next === "en" ? "切换为中文界面" : "Switch to English";
    }
    try { window.localStorage.setItem("dental-ui-language", next); } catch (_) {}
  }

  function applyDentalTheme(theme) {
    const next = theme === "dark" ? "dark" : "light";
    document.body.dataset.dentalTheme = next;
    const toggle = document.getElementById("dental-theme-toggle");
    if (toggle) {
      toggle.textContent = next === "dark" ? "浅色" : "暗色";
      toggle.title = next === "dark" ? "切换为浅色模式" : "切换为暗色模式";
    }
    try { window.localStorage.setItem("dental-ui-theme", next); } catch (_) {}
  }

  function installPreferences() {
    let lang = "zh";
    let theme = "light";
    try {
      lang = window.localStorage.getItem("dental-ui-language") || lang;
      theme = window.localStorage.getItem("dental-ui-theme") || theme;
    } catch (_) {}
    applyDentalLanguage(lang);
    applyDentalTheme(theme);
    const langBtn = document.getElementById("dental-lang-toggle");
    const themeBtn = document.getElementById("dental-theme-toggle");
    if (langBtn && langBtn.dataset.installed !== "true") {
      langBtn.dataset.installed = "true";
      langBtn.addEventListener("click", () => applyDentalLanguage(document.body.dataset.dentalLang === "en" ? "zh" : "en"));
    }
    if (themeBtn && themeBtn.dataset.installed !== "true") {
      themeBtn.dataset.installed = "true";
      themeBtn.addEventListener("click", () => applyDentalTheme(document.body.dataset.dentalTheme === "dark" ? "light" : "dark"));
    }
    setTimeout(() => applyDentalLanguage(document.body.dataset.dentalLang || lang), 400);
    setTimeout(() => applyDentalLanguage(document.body.dataset.dentalLang || lang), 1200);
  }

  function activateDentalPage(page, shouldScroll = true) {
    const nextPage = DENTAL_PAGES.has(page) ? page : "learn";
    document.body.dataset.dentalPage = nextPage;
    document.querySelectorAll(".dental-page-nav-item[data-page]").forEach(btn => {
      const active = btn.dataset.page === nextPage;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-current", active ? "page" : "false");
    });
    if (shouldScroll) {
      const target = document.getElementById(`page-${nextPage}`);
      const nav = document.querySelector(".dental-page-nav");
      if (target && nav) {
        setTimeout(() => nav.scrollIntoView({ behavior: "smooth", block: "start" }), 0);
      }
    }
    document.dispatchEvent(new CustomEvent("dental-page-change", { detail: { page: nextPage } }));
  }

  window.dentalActivatePage = activateDentalPage;

  function preferredInitialPage() {
    try {
      const params = new URLSearchParams(window.location.search || "");
      const fromQuery = params.get("dental_page");
      if (DENTAL_PAGES.has(fromQuery)) return fromQuery;
      const fromHash = (window.location.hash || "").replace(/^#\/?/, "");
      if (DENTAL_PAGES.has(fromHash)) return fromHash;
    } catch (_) {}
    return "learn";
  }

  function installPageNavigation() {
    let userNavigated = false;
    const initialPage = preferredInitialPage();
    activateDentalPage(initialPage, false);
    setTimeout(() => { if (!userNavigated) activateDentalPage(initialPage, false); }, 300);
    setTimeout(() => { if (!userNavigated) activateDentalPage(initialPage, false); }, 1000);
    document.addEventListener("click", e => {
      const btn = e.target && e.target.closest && e.target.closest(".dental-page-nav-item[data-page]");
      if (!btn) return;
      e.preventDefault();
      e.stopPropagation();
      userNavigated = true;
      activateDentalPage(btn.dataset.page || "learn");
    }, true);
  }

  function installImageMagnifier() {
    if (window.__dentalImageMagnifierInstalled) return;
    window.__dentalImageMagnifierInstalled = true;
    const selector = '#page-image img, #page-compare img, #page-batch img, #page-report img, .dental-image-fullscreen-layer img';
    const zoom = 2.4;
    let loupe = document.getElementById('dental-image-loupe');

    if (!loupe) {
      loupe = document.createElement('div');
      loupe.id = 'dental-image-loupe';
      loupe.className = 'dental-image-loupe';
      document.body.appendChild(loupe);
    }

    function usableImage(img) {
      if (!img || !img.src || img.naturalWidth < 40 || img.naturalHeight < 40) return false;
      const rect = img.getBoundingClientRect();
      return rect.width >= 80 && rect.height >= 80;
    }

    function placeNearCursor(el, x, y, size, offset) {
      const gap = offset || 18;
      let left = x + gap;
      let top = y + gap;
      if (left + size > window.innerWidth - 12) left = x - size - gap;
      if (top + size > window.innerHeight - 12) top = y - size - gap;
      el.style.left = `${Math.max(12, left)}px`;
      el.style.top = `${Math.max(12, top)}px`;
    }

    function updateLoupe(event, img) {
      const rect = img.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      if (x < 0 || y < 0 || x > rect.width || y > rect.height) {
        hideLoupe();
        return;
      }
      const src = img.currentSrc || img.src;
      const size = 190;
      loupe.style.backgroundImage = `url("${src}")`;
      loupe.style.backgroundSize = `${rect.width * zoom}px ${rect.height * zoom}px`;
      loupe.style.backgroundPosition = `${size / 2 - x * zoom}px ${size / 2 - y * zoom}px`;
      placeNearCursor(loupe, event.clientX, event.clientY, size, 18);
      loupe.classList.add('visible');
    }

    function hideLoupe() {
      loupe.classList.remove('visible');
    }

    document.addEventListener('mousemove', event => {
      const target = event.target && event.target.closest ? event.target.closest(selector) : null;
      if (usableImage(target)) updateLoupe(event, target);
      else hideLoupe();
    }, true);
    document.addEventListener('scroll', hideLoupe, true);
    document.addEventListener('mouseleave', hideLoupe);
  }

  function installBatchPreviewFullscreen() {
    if (window.__dentalBatchFullscreenInstalled) return;
    window.__dentalBatchFullscreenInstalled = true;
    let activeImage = null;
    const btn = document.createElement('button');
    btn.id = 'dental-batch-fullscreen-btn';
    btn.className = 'dental-batch-fullscreen-btn';
    btn.type = 'button';
    btn.title = '全屏查看批量预览图';
    btn.setAttribute('aria-label', '全屏查看批量预览图');
    btn.textContent = '⛶';
    document.body.appendChild(btn);

    const layer = document.createElement('div');
    layer.id = 'dental-image-fullscreen-layer';
    layer.className = 'dental-image-fullscreen-layer';
    layer.innerHTML = '<button type="button" class="dental-image-fullscreen-close" aria-label="关闭全屏">×</button><img alt="批量检测结果全屏预览">';
    document.body.appendChild(layer);
    const fullImage = layer.querySelector('img');
    const close = layer.querySelector('.dental-image-fullscreen-close');

    function targetImage(node) {
      const img = node && node.closest ? node.closest('#batch-result-preview-gallery img') : null;
      if (!img || !img.src || img.naturalWidth < 40 || img.naturalHeight < 40) return null;
      return img;
    }

    function positionButton(img) {
      const rect = img.getBoundingClientRect();
      if (rect.width < 80 || rect.height < 70) {
        hideButton();
        return;
      }
      activeImage = img;
      btn.style.left = `${Math.max(12, rect.right - 46)}px`;
      btn.style.top = `${Math.max(12, rect.top + 10)}px`;
      btn.classList.add('visible');
    }

    function hideButton() {
      btn.classList.remove('visible');
      activeImage = null;
    }

    function openFullscreen(img) {
      if (!img) return;
      fullImage.src = img.currentSrc || img.src;
      fullImage.alt = img.alt || '批量检测结果全屏预览';
      layer.classList.add('visible');
      try {
        if (layer.requestFullscreen && !document.fullscreenElement) {
          layer.requestFullscreen().catch(() => {});
        }
      } catch (_) {}
    }

    function closeFullscreen() {
      layer.classList.remove('visible');
      fullImage.removeAttribute('src');
      try {
        if (document.fullscreenElement === layer) document.exitFullscreen().catch(() => {});
      } catch (_) {}
    }

    document.addEventListener('mousemove', event => {
      const img = targetImage(event.target);
      if (img) positionButton(img);
      else if (event.target !== btn && !btn.contains(event.target)) hideButton();
    }, true);
    btn.addEventListener('click', event => {
      event.preventDefault();
      event.stopPropagation();
      openFullscreen(activeImage);
    });
    layer.addEventListener('click', event => {
      if (event.target === layer || event.target === close) closeFullscreen();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && layer.classList.contains('visible')) closeFullscreen();
    });
    document.addEventListener('scroll', () => {
      if (activeImage) positionButton(activeImage);
    }, true);
  }

  function findAiTabButton() {
    const roleTabs = Array.from(document.querySelectorAll('[role="tab"]'));
    const roleByText = roleTabs.find(el => (el.textContent || '').replace(/\s+/g, '').includes('智诊管家'));
    if (roleByText) return roleByText;
    const direct = document.querySelector('[aria-controls*="ai-assistant-tab"], [id*="ai-assistant-tab"] button');
    if (direct) return direct;
    const tabButtons = Array.from(document.querySelectorAll('[role="tab"], button[aria-selected]'));
    const tabButtonByText = tabButtons.find(el => (el.textContent || '').replace(/\s+/g, '').includes('智诊管家'));
    if (tabButtonByText) return tabButtonByText;
    const candidates = Array.from(document.querySelectorAll('button, [role="tab"]'));
    const byText = candidates.find(el => (el.textContent || '').replace(/\s+/g, '').includes('智诊管家'));
    if (byText) return byText.closest('button, [role="tab"]') || byText;
    const xpath = document.evaluate("//*[contains(normalize-space(.), '智诊管家')]", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
    for (let i = 0; i < xpath.snapshotLength; i++) {
      const node = xpath.snapshotItem(i);
      const clickable = node.closest && node.closest('button, [role="tab"]');
      if (clickable) return clickable;
    }
    return null;
  }

  function findInput() {
    return document.querySelector('#ask-ai-input textarea, #ask-ai-input input, textarea[aria-label="问题"], input[aria-label="问题"]');
  }

  function findSendButton() {
    return document.querySelector('#ask-ai-send button, #ask-ai-send');
  }

  function writeAssistantInput(el, value) {
    el.value = value;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }

  function jumpToAssistant() {
    activateDentalPage("assistant", false);
    const clickTab = () => {
      const tab = findAiTabButton();
      if (tab) {
        tab.click();
      }
    };
    clickTab();
    setTimeout(() => {
      const input = findInput();
      if (!input) clickTab();
    }, 180);
    setTimeout(() => {
      const input = findInput();
      if (input) {
        input.scrollIntoView({ behavior: 'smooth', block: 'center' });
        input.focus({ preventScroll: true });
      }
    }, 420);
  }

  function askAi(text) {
    const picked = (text || selectedText()).trim();
    jumpToAssistant();
    if (!picked) return;
    const question = `请解释我在页面上选中的这段内容，并在需要时结合当前检测结果、多模型对比、批量检测和报告上下文回答：\n\n「${picked}」`;
    setTimeout(() => {
      const input = findInput();
      const send = findSendButton();
      if (!input || !send) return;
      writeAssistantInput(input, question);
      setTimeout(() => send.click(), 120);
    }, 650);
  }

  function ensureUi() {
    const oldQuickNav = document.getElementById('dental-quick-nav');
    if (oldQuickNav) oldQuickNav.remove();
    if (!document.getElementById('ask-ai-floating-button')) {
      const btn = document.createElement('button');
      btn.id = 'ask-ai-floating-button';
      btn.type = 'button';
      btn.title = '智诊管家：点击跳转，拖入高亮文字可提问';
      btn.innerHTML = `
        <svg viewBox="0 0 64 64" aria-hidden="true">
          <path d="M32 7v7" stroke="white" stroke-width="4" stroke-linecap="round"/>
          <circle cx="32" cy="6" r="4" fill="#fde68a"/>
          <rect x="12" y="16" width="40" height="34" rx="13" fill="rgba(255,255,255,0.96)" stroke="#bfdbfe" stroke-width="3"/>
          <circle cx="25" cy="32" r="5" fill="#2563eb"/><circle cx="39" cy="32" r="5" fill="#2563eb"/>
          <path d="M24 42c5 4 11 4 16 0" stroke="#0f172a" stroke-width="3" stroke-linecap="round" fill="none"/>
          <path d="M15 23l-6-4M49 23l6-4" stroke="white" stroke-width="4" stroke-linecap="round"/>
          <path d="M47 48l8 8M52 47l5 5" stroke="#fde68a" stroke-width="4" stroke-linecap="round"/>
        </svg>
        <span class="robot-label">智诊管家</span>`;
      btn.addEventListener('click', () => askAi(selectedText()));
      btn.addEventListener('dragover', e => { e.preventDefault(); btn.classList.add('drag-over'); });
      btn.addEventListener('dragleave', () => btn.classList.remove('drag-over'));
      btn.addEventListener('drop', e => {
        e.preventDefault();
        btn.classList.remove('drag-over');
        askAi(e.dataTransfer.getData('text/plain') || selectedText());
      });
      document.body.appendChild(btn);
    }
    if (!document.getElementById('ask-ai-selection-popover')) {
      const pop = document.createElement('button');
      pop.id = 'ask-ai-selection-popover';
      pop.type = 'button';
      pop.textContent = '问问智诊管家';
      pop.addEventListener('click', () => askAi(pop.dataset.text || selectedText()));
      document.body.appendChild(pop);
    }
  }

  function showSelectionPopover() {
    ensureUi();
    const text = selectedText();
    const pop = document.getElementById('ask-ai-selection-popover');
    if (!text || text.length < 3) {
      pop.classList.remove('visible');
      return;
    }
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) return;
    const rect = selection.getRangeAt(0).getBoundingClientRect();
    if (!rect || (!rect.width && !rect.height)) return;
    pop.dataset.text = text;
    pop.style.left = `${Math.min(window.innerWidth - 150, Math.max(12, rect.right + window.scrollX + 8))}px`;
    pop.style.top = `${Math.max(12, rect.top + window.scrollY - 8)}px`;
    pop.classList.add('visible');
  }

  function install() {
    installPageNavigation();
    installPreferences();
    installImageMagnifier();
    installBatchPreviewFullscreen();
    ensureUi();
    document.addEventListener('mouseup', () => setTimeout(showSelectionPopover, 60));
    document.addEventListener('touchend', () => setTimeout(showSelectionPopover, 180));
    document.addEventListener('selectionchange', () => setTimeout(showSelectionPopover, 80));
    document.addEventListener('dragstart', e => {
      const text = selectedText();
      if (text && e.dataTransfer) {
        e.dataTransfer.setData('text/plain', text);
        e.dataTransfer.effectAllowed = 'copy';
      }
    }, true);
    document.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'a') {
        e.preventDefault();
        askAi(selectedText());
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', install);
  else install();
})();
</script>
"""
