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
    let initialSyncAttempts = 0;
    const initialSyncTimer = setInterval(() => {
      initialSyncAttempts += 1;
      if (userNavigated || document.querySelector(".dental-page-nav-item.active") || initialSyncAttempts >= 40) {
        clearInterval(initialSyncTimer);
        return;
      }
      if (document.querySelector(".dental-page-nav-item[data-page]")) {
        activateDentalPage(initialPage, false);
      }
    }, 250);
    document.addEventListener("click", e => {
      const btn = e.target && e.target.closest && e.target.closest(".dental-page-nav-item[data-page]");
      if (!btn) return;
      e.preventDefault();
      e.stopPropagation();
      userNavigated = true;
      activateDentalPage(btn.dataset.page || "learn");
      const nav = document.querySelector(".dental-page-nav");
      const toggle = document.querySelector(".dental-nav-toggle");
      nav?.classList.remove("nav-open");
      toggle?.setAttribute("aria-expanded", "false");
    }, true);
    document.addEventListener("click", e => {
      const toggle = e.target && e.target.closest && e.target.closest(".dental-nav-toggle");
      if (!toggle) return;
      const nav = toggle.closest(".dental-page-nav");
      const open = !nav.classList.contains("nav-open");
      nav.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    });
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
      if (img.closest('.linked-region-row')) return false;
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

  function installComparisonFullscreen() {
    if (window.__dentalComparisonFullscreenInstalled) return;
    window.__dentalComparisonFullscreenInstalled = true;

    const layer = document.createElement('div');
    layer.id = 'dental-comparison-fullscreen-layer';
    layer.className = 'dental-comparison-fullscreen-layer';
    layer.innerHTML = `
      <div class="dental-comparison-fullscreen-toolbar">
        <span>原图 / 检测结果滑动对比</span>
        <button type="button" class="dental-comparison-fullscreen-close" aria-label="关闭全屏">×</button>
      </div>
      <div class="dental-comparison-fullscreen-frame" role="application" aria-label="全屏滑动对比">
        <img class="dental-comparison-fullscreen-original" alt="原图">
        <img class="dental-comparison-fullscreen-result" alt="检测结果">
        <div class="dental-comparison-fullscreen-divider" aria-hidden="true">
          <span></span>
        </div>
        <input class="dental-comparison-fullscreen-range" type="range" min="0" max="100" value="50" aria-label="调整原图和检测结果分割位置">
      </div>
      <div class="dental-comparison-fullscreen-hint">拖动中间分割线，或使用下方滑块调整对比位置 · 双击图片复位</div>
    `;
    document.body.appendChild(layer);
    const frame = layer.querySelector('.dental-comparison-fullscreen-frame');
    const originalImage = layer.querySelector('.dental-comparison-fullscreen-original');
    const resultImage = layer.querySelector('.dental-comparison-fullscreen-result');
    const range = layer.querySelector('.dental-comparison-fullscreen-range');
    const close = layer.querySelector('.dental-comparison-fullscreen-close');
    let activeSlider = null;

    const setSplit = value => {
      const numeric = Math.max(0, Math.min(100, Number(value) || 0));
      frame.style.setProperty('--compare-split', `${numeric}%`);
      range.value = String(numeric);
    };

    const sourceImages = slider => {
      const seen = new Set();
      return Array.from(slider?.querySelectorAll?.('img') || []).filter(img => {
        const src = img.currentSrc || img.src;
        if (!src || seen.has(src)) return false;
        seen.add(src);
        return true;
      }).slice(0, 2);
    };

    const isFullscreenButton = target => {
      const button = target?.closest?.('.result-compare-slider button, .result-compare-slider [role="button"]');
      if (!button) return null;
      const label = [
        button.getAttribute('aria-label'),
        button.getAttribute('title'),
        button.dataset?.testid,
        button.textContent
      ].filter(Boolean).join(' ').toLowerCase();
      if (!/(fullscreen|full screen|全屏|放大)/i.test(label)) return null;
      return button.closest('.result-compare-slider');
    };

    const open = slider => {
      const images = sourceImages(slider);
      if (!slider || images.length < 2) return false;
      activeSlider = slider;
      originalImage.src = images[0].currentSrc || images[0].src;
      resultImage.src = images[1].currentSrc || images[1].src;
      originalImage.alt = images[0].alt || '原图';
      resultImage.alt = images[1].alt || '检测结果';
      setSplit(50);
      layer.classList.add('visible');
      try {
        if (layer.requestFullscreen && !document.fullscreenElement) layer.requestFullscreen().catch(() => {});
      } catch (_) {}
      return true;
    };

    const closeLayer = () => {
      layer.classList.remove('visible');
      originalImage.removeAttribute('src');
      resultImage.removeAttribute('src');
      activeSlider = null;
      try {
        if (document.fullscreenElement === layer) document.exitFullscreen().catch(() => {});
      } catch (_) {}
    };

    const setSplitFromPointer = event => {
      const rect = frame.getBoundingClientRect();
      if (!rect.width) return;
      setSplit(((event.clientX - rect.left) / rect.width) * 100);
    };

    frame.addEventListener('pointerdown', event => {
      if (event.target === range || event.target.closest?.('button, input')) return;
      frame.setPointerCapture?.(event.pointerId);
      setSplitFromPointer(event);
    });
    frame.addEventListener('pointermove', event => {
      if (frame.hasPointerCapture?.(event.pointerId)) setSplitFromPointer(event);
    });
    frame.addEventListener('pointerup', event => {
      frame.releasePointerCapture?.(event.pointerId);
    });
    frame.addEventListener('dblclick', event => {
      if (event.target.closest?.('button, input')) return;
      setSplit(50);
    });
    range.addEventListener('input', event => setSplit(event.target.value));
    close.addEventListener('click', event => {
      event.preventDefault();
      event.stopPropagation();
      closeLayer();
    });
    layer.addEventListener('click', event => {
      if (event.target === layer) closeLayer();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && layer.classList.contains('visible')) closeLayer();
    });
    document.addEventListener('click', event => {
      const slider = isFullscreenButton(event.target);
      if (!slider) return;
      if (!open(slider)) return;
      event.preventDefault();
      event.stopPropagation();
      event.stopImmediatePropagation?.();
    }, true);
    document.addEventListener('fullscreenchange', () => {
      if (!document.fullscreenElement && layer.classList.contains('visible')) layer.classList.add('visible');
    });
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

  function installSynchronizedComparisonViewer() {
    if (window.__dentalSyncViewerInstalled) return;
    window.__dentalSyncViewerInstalled = true;
    let scale = 1;
    let origin = "50% 50%";
    const images = () => Array.from(document.querySelectorAll(".sync-model-viewer img")).filter(img => img.src);
    const apply = () => images().forEach(img => {
      img.style.transformOrigin = origin;
      img.style.transform = `scale(${scale})`;
    });
    document.addEventListener("wheel", event => {
      const image = event.target?.closest?.(".sync-model-viewer img");
      if (!image) return;
      event.preventDefault();
      scale = Math.min(3, Math.max(1, scale + (event.deltaY < 0 ? 0.2 : -0.2)));
      apply();
    }, {capture: true, passive: false});
    document.addEventListener("pointermove", event => {
      const image = event.target?.closest?.(".sync-model-viewer img");
      if (!image || scale <= 1) return;
      const rect = image.getBoundingClientRect();
      origin = `${Math.max(0, Math.min(100, (event.clientX - rect.left) / rect.width * 100))}% ${Math.max(0, Math.min(100, (event.clientY - rect.top) / rect.height * 100))}%`;
      apply();
    }, true);
    document.addEventListener("dblclick", event => {
      if (!event.target?.closest?.(".sync-model-viewer img")) return;
      scale = 1;
      origin = "50% 50%";
      apply();
    }, true);
  }

  function installDiseaseLearningFilters() {
    if (window.__dentalEducationFiltersInstalled) return;
    window.__dentalEducationFiltersInstalled = true;
    let category = "all";
    const apply = () => {
      const input = document.getElementById("disease-search-input");
      const clear = document.getElementById("disease-search-clear");
      const count = document.getElementById("education-result-count");
      const query = (input?.value || "").trim().toLowerCase();
      let visible = 0;
      const cards = Array.from(document.querySelectorAll(".education-card[data-disease]"));
      cards.forEach(card => {
        const matchesCategory = category === "all" || card.dataset.disease === category;
        const matchesQuery = !query || (card.dataset.search || card.textContent || "").toLowerCase().includes(query);
        card.hidden = !(matchesCategory && matchesQuery);
        if (!card.hidden) visible += 1;
      });
      const empty = document.querySelector(".education-no-result");
      if (empty) empty.hidden = visible > 0;
      if (clear) clear.hidden = !query;
      if (count) count.textContent = `显示 ${visible} / ${cards.length} 类`;
    };
    document.addEventListener("input", event => {
      if (event.target?.id === "disease-search-input") apply();
    });
    document.addEventListener("click", event => {
      const clear = event.target?.closest?.("#disease-search-clear");
      if (clear) {
        const input = document.getElementById("disease-search-input");
        if (input) {
          input.value = "";
          input.focus();
        }
        apply();
        return;
      }
      const button = event.target?.closest?.("[data-disease-filter]");
      if (!button) return;
      category = button.dataset.diseaseFilter || "all";
      document.querySelectorAll("[data-disease-filter]").forEach(item => {
        const active = item === button;
        item.classList.toggle("active", active);
        item.setAttribute("aria-pressed", String(active));
      });
      apply();
    });
    document.addEventListener("keydown", event => {
      if (event.key !== "Escape" || event.target?.id !== "disease-search-input") return;
      event.target.value = "";
      apply();
    });
    apply();
  }

  function installDetectionWorkflowState() {
    if (window.__dentalWorkflowStateInstalled) return;
    window.__dentalWorkflowStateInstalled = true;
    const configs = {
      single: {
        upload: "single-upload",
        run: "single-run",
        progress: "single-progress",
        ready: "single-result-summary",
        shell: ".single-results-shell"
      },
      compare: {
        upload: "compare-upload",
        run: "compare-run",
        progress: "compare-progress",
        ready: "compare-result-summary",
        shell: ".compare-results-shell"
      },
      batch: {
        upload: "batch-upload",
        run: "batch-run",
        progress: "batch-progress",
        ready: "batch-image-selector",
        shell: ".batch-results-shell"
      }
    };
    const visible = node => {
      if (!node) return false;
      const style = getComputedStyle(node);
      const rect = node.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
    };
    const hasUpload = (kind, root) => {
      if (!root) return false;
      if (kind === "batch") return /\.(png|jpe?g|bmp|webp)/i.test(root.textContent || "");
      return Array.from(root.querySelectorAll("img")).some(img => visible(img) && img.naturalWidth > 80);
    };
    const componentShown = node => {
      if (!node || node.hidden || node.getAttribute("aria-hidden") === "true") return false;
      const style = getComputedStyle(node);
      return style.display !== "none" && style.visibility !== "hidden";
    };
    const render = kind => {
      const config = configs[kind];
      const workflow = document.querySelector(`.detection-workflow[data-workflow-kind="${kind}"]`);
      if (!workflow) return;
      const uploadRoot = document.getElementById(config.upload);
      const progressRoot = document.getElementById(config.progress);
      const readyRoot = document.getElementById(config.ready);
      const uploaded = hasUpload(kind, uploadRoot);
      // The result shell is hidden before the first run, so layout dimensions
      // cannot be used to discover a streamed progress update inside it.
      const running = Boolean(progressRoot?.querySelector(".detection-progress-state"));
      const explicitlyCompleted = Boolean(
        progressRoot?.querySelector(`[data-detection-complete="${kind}"]`)
      );
      // Only backend-controlled result markers can complete a workflow.
      // File upload previews also contain images/tables and must never count.
      // Multi-model comparison uses an explicit marker outside all result tabs
      // so its first final frame cannot be hidden by the analysis panel.
      const completed = !running && (
        explicitlyCompleted ||
        (kind !== "compare" && componentShown(readyRoot))
      );
      let step = completed ? 4 : (running ? 3 : (uploaded ? 2 : 1));
      if (workflow.dataset.forceRun === "true" && !completed) step = 3;
      if (!uploaded && !running && !completed) workflow.dataset.forceRun = "false";
      if (completed || !running && step !== 3) workflow.dataset.forceRun = "false";
      workflow.dataset.activeStep = String(step);
      workflow.querySelectorAll("li").forEach((item, index) => {
        const itemStep = index + 1;
        item.classList.toggle("is-active", itemStep === step && !completed);
        item.classList.toggle("is-done", itemStep < step || (completed && itemStep === 4));
        if (itemStep === step) item.setAttribute("aria-current", "step");
        else item.removeAttribute("aria-current");
      });
    };
    const renderAll = () => Object.keys(configs).forEach(render);
    document.addEventListener("click", event => {
      for (const [kind, config] of Object.entries(configs)) {
        if (event.target?.closest?.(`#${config.run}`)) {
          const workflow = document.querySelector(`.detection-workflow[data-workflow-kind="${kind}"]`);
          if (workflow) workflow.dataset.forceRun = "true";
          setTimeout(() => render(kind), 0);
        }
      }
    }, true);
    document.addEventListener("input", () => setTimeout(renderAll, 0), true);
    document.addEventListener("change", () => setTimeout(renderAll, 0), true);
    let scheduled = false;
    const observer = new MutationObserver(() => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => { scheduled = false; renderAll(); });
    });
    observer.observe(document.body, {subtree: true, childList: true, attributes: true, attributeFilter: ["style", "class", "hidden"]});
    renderAll();
    setTimeout(renderAll, 600);
  }

  function installDetectionResultTabs() {
    if (window.__dentalDetectionResultTabsInstalled) return;
    window.__dentalDetectionResultTabsInstalled = true;
    const configs = {
      single: {
        page: '#page-image',
        shell: '.single-results-shell',
        progress: '#single-progress',
        ready: '#single-result-summary',
        run: '#single-run',
        reportTrigger: '#single-report-trigger',
        targets: {
          overview: '.single-result-overview',
          structured: '.structured-result-panel',
          review: '.detection-support-grid',
          report: '.single-report-panel'
        }
      },
      compare: {
        page: '#page-compare',
        shell: '.compare-results-shell',
        progress: '#compare-progress',
        ready: '#compare-result-summary',
        run: '#compare-run',
        reportTrigger: '#comparison-report-trigger',
        targets: {
          models: '.compare-result-models-panel',
          analysis: '.compare-result-analysis-panel',
          review: '.compare-result-review-panel',
          report: '.compare-report-panel'
        }
      },
      batch: {
        page: '#page-batch',
        shell: '.batch-results-shell',
        progress: '#batch-progress',
        ready: '#batch-image-selector',
        run: '#batch-run',
        reportTrigger: '#batch-report-trigger',
        targets: {
          review: '.batch-review-grid',
          table: '.structured-result-panel',
          support: '.detection-support-grid',
          report: '.batch-report-panel'
        }
      }
    };
    const componentShown = node => {
      if (!node || node.hidden || node.getAttribute('aria-hidden') === 'true') return false;
      const style = getComputedStyle(node);
      return style.display !== 'none' && style.visibility !== 'hidden';
    };
    const hasResult = config => {
      const page = document.querySelector(config.page);
      if (!page) return false;
      const progress = page.querySelector(config.progress);
      const kind = config.page === '#page-compare'
        ? 'compare'
        : (config.page === '#page-batch' ? 'batch' : 'single');
      if (progress?.querySelector(`[data-detection-complete="${kind}"]`)) return true;
      // Each marker is hidden by Gradio until the corresponding backend job
      // reaches its final yield.  This avoids treating the batch uploader's
      // own file table as a completed detection result.
      return kind !== 'compare' && componentShown(page.querySelector(config.ready));
    };
    const isRunning = config => {
      const progress = document.querySelector(config.progress);
      // The progress component initially lives inside a hidden result shell.
      // Detect its streamed state by content rather than by layout visibility,
      // then the shell can be revealed consistently on all three pages.
      return Boolean(progress?.querySelector('.detection-progress-state'));
    };
    const reportPanel = (kind, config = configs[kind]) => {
      const page = document.querySelector(config?.page);
      const shell = page?.querySelector(config?.shell);
      return shell?.querySelector(config?.targets?.report || '');
    };
    const reportHasContent = panel => {
      if (!panel) return false;
      const previewText = (panel.querySelector('.detection-report-preview')?.textContent || '').trim();
      const placeholder = /尚未生成|首次打开|暂无可生成|生成失败|未能生成/i.test(previewText);
      const hasDownload = Array.from(panel.querySelectorAll('.report-download-action a[href]')).some(link => {
        const href = link.getAttribute('href') || '';
        return href && href !== '#';
      });
      return hasDownload || (!placeholder && previewText.length > 80);
    };
    const reportSignature = panel => {
      if (!panel) return '';
      const previewText = (panel.querySelector('.detection-report-preview')?.textContent || '').trim();
      const links = Array.from(panel.querySelectorAll('.report-download-action a[href]'))
        .map(link => link.getAttribute('href') || '')
        .filter(Boolean)
        .join('|');
      return `${previewText.slice(0, 240)}|${previewText.length}|${links}`;
    };
    const syncReportState = kind => {
      const panel = reportPanel(kind);
      if (!panel) return;
      const progressText = (panel.querySelector('.detection-progress-state')?.textContent || '').trim();
      if (panel.dataset.reportBusy === 'true') {
        if (/失败|无法生成|暂时无法/i.test(progressText)) {
          panel.dataset.reportBusy = 'false';
          panel.setAttribute('aria-busy', 'false');
          return;
        }
        if (
          reportHasContent(panel) &&
          reportSignature(panel) !== (panel.dataset.reportPreviousSignature || '')
        ) {
          panel.dataset.reportGenerated = 'true';
          panel.dataset.reportBusy = 'false';
          panel.dataset.reportInvalidated = 'false';
          panel.setAttribute('aria-busy', 'false');
        }
        return;
      }
      if (panel.dataset.reportInvalidated === 'true') return;
      if (reportHasContent(panel)) {
        panel.dataset.reportGenerated = 'true';
        panel.dataset.reportBusy = 'false';
        panel.setAttribute('aria-busy', 'false');
        return;
      }
      if (/失败|无法生成|暂时无法/i.test(progressText)) {
        panel.dataset.reportBusy = 'false';
        panel.setAttribute('aria-busy', 'false');
      }
    };
    const resetReportState = kind => {
      const panel = reportPanel(kind);
      if (!panel) return;
      panel.dataset.reportGenerated = 'false';
      panel.dataset.reportBusy = 'false';
      panel.dataset.reportInvalidated = 'true';
      panel.setAttribute('aria-busy', 'false');
    };
    const startReportOnce = kind => {
      const config = configs[kind];
      const panel = reportPanel(kind, config);
      if (!config || !panel) return;
      syncReportState(kind);
      if (panel.dataset.reportGenerated === 'true' || panel.dataset.reportBusy === 'true') return;
      const triggerRoot = document.querySelector(config.reportTrigger);
      const trigger = triggerRoot?.matches?.('button') ? triggerRoot : triggerRoot?.querySelector?.('button');
      if (!trigger) return;
      panel.dataset.reportPreviousSignature = reportSignature(panel);
      panel.dataset.reportBusy = 'true';
      panel.dataset.reportInvalidated = 'false';
      panel.setAttribute('aria-busy', 'true');
      requestAnimationFrame(() => trigger.click());
    };
    const render = (kind, forceDefault = false) => {
      const config = configs[kind];
      const page = document.querySelector(config.page);
      const shell = page?.querySelector(config.shell);
      const tabs = shell?.querySelector('.detection-result-tabs');
      if (!page || !shell || !tabs) return;
      const running = isRunning(config);
      const ready = !running && hasResult(config);
      shell.classList.toggle('detection-before-run', !running && !ready);
      shell.classList.toggle('detection-running', running);
      tabs.hidden = !ready;
      const buttons = Array.from(tabs.querySelectorAll('.detection-result-tab'));
      const targetKeys = buttons.map(button => button.dataset.resultTab).filter(Boolean);
      if (forceDefault || running) {
        tabs.dataset.activeTab = targetKeys[0] || '';
        tabs.dataset.userCollapsed = 'false';
      } else if (tabs.dataset.userCollapsed !== 'true' && !targetKeys.includes(tabs.dataset.activeTab || '')) {
        tabs.dataset.activeTab = targetKeys[0] || '';
      }
      const active = ready && tabs.dataset.userCollapsed !== 'true' ? tabs.dataset.activeTab : '';
      buttons.forEach(button => {
        const selected = ready && button.dataset.resultTab === active;
        button.classList.toggle('active', selected);
        button.setAttribute('aria-selected', String(selected));
        button.setAttribute('aria-expanded', String(selected));
      });
      Object.entries(config.targets).forEach(([key, selector]) => {
        const panel = shell.querySelector(selector);
        if (!panel) return;
        panel.classList.add('detection-result-panel');
        panel.classList.toggle('is-active', ready && key === active);
      });
    };
    const renderAll = forceDefault => Object.keys(configs).forEach(kind => render(kind, forceDefault));
    document.addEventListener('click', event => {
      for (const [kind, config] of Object.entries(configs)) {
        if (event.target?.closest?.(config.run)) resetReportState(kind);
      }
      const button = event.target?.closest?.('.detection-result-tab');
      if (!button) return;
      const tabs = button.closest('.detection-result-tabs');
      if (!tabs) return;
      event.preventDefault();
      if (button.dataset.resultTab === tabs.dataset.activeTab && tabs.dataset.userCollapsed !== 'true') {
        tabs.dataset.activeTab = '';
        tabs.dataset.userCollapsed = 'true';
      } else {
        tabs.dataset.activeTab = button.dataset.resultTab || '';
        tabs.dataset.userCollapsed = 'false';
      }
      const kind = tabs.dataset.resultTabsKind;
      if (configs[kind]) {
        render(kind);
        if (button.dataset.resultTab === 'report' && tabs.dataset.userCollapsed !== 'true') {
          setTimeout(() => startReportOnce(kind), 0);
        }
      }
    }, true);
    document.addEventListener('load', () => renderAll(false), true);
    let scheduled = false;
    const observer = new MutationObserver(() => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => {
        scheduled = false;
        renderAll(false);
        Object.keys(configs).forEach(syncReportState);
      });
    });
    observer.observe(document.body, {
      subtree: true,
      childList: true,
      attributes: true,
      attributeFilter: ['style', 'class', 'hidden', 'aria-selected']
    });
    renderAll(true);
    setTimeout(() => {
      renderAll(false);
      Object.keys(configs).forEach(syncReportState);
    }, 700);
  }

  function setGradioChoice(targetId, choice) {
    const root = document.getElementById(targetId);
    const input = root?.querySelector("input");
    if (!input) return false;
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value")?.set;
    setter ? setter.call(input, choice) : (input.value = choice);
    input.dispatchEvent(new Event("input", {bubbles: true}));
    input.dispatchEvent(new Event("change", {bubbles: true}));
    input.dispatchEvent(new KeyboardEvent("keydown", {key: "Enter", bubbles: true}));
    input.dispatchEvent(new KeyboardEvent("keyup", {key: "Enter", bubbles: true}));
    return true;
  }

  window.dentalJumpEvidence = evidence => {
    if (!evidence) return;
    activateDentalPage(evidence.page || "image");
    setTimeout(() => {
      const target = document.getElementById(evidence.target || "");
      if (target) {
        setGradioChoice(evidence.target, evidence.choice || "");
        target.scrollIntoView({behavior: "smooth", block: "center"});
      }
    }, 350);
  };

  function install() {
    document.documentElement.lang = "zh-CN";
    delete document.body.dataset.dentalTheme;
    delete document.body.dataset.dentalLang;
    try {
      localStorage.removeItem("dental-ui-theme");
      localStorage.removeItem("dental-ui-language");
    } catch (_) {}
    installPageNavigation();
    installImageMagnifier();
    installBatchPreviewFullscreen();
    installComparisonFullscreen();
    installSynchronizedComparisonViewer();
    installDiseaseLearningFilters();
    installDetectionWorkflowState();
    installDetectionResultTabs();
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
