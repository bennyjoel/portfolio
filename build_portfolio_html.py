import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Benny Joel Lakamana | Visual Design, Production Decks & Motion Systems</title>
  <meta name="description" content="Executive Visual Design, Feature Film VFX Technical Decks, Real-Time 3D Environments, and Programmatic Motion Graphics by Benny Joel Lakamana.">

  <!-- Inter & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       DARK LUXURY MATTE DESIGN SYSTEM (WCAG AAA ACCESSIBLE & TACTILE)
       ========================================================================== */
    :root {
      --bg-canvas: #090B0E;
      --bg-surface: #11141A;
      --bg-surface-elevated: #161A22;
      --bg-card: #131720;
      --bg-glass: rgba(17, 20, 26, 0.85);

      --border-matte: #202633;
      --border-highlight: #313A4D;
      --border-interactive: #424F69;

      --text-pure: #FFFFFF;
      --text-primary: #ECEFF4;
      --text-secondary: #9DA7B8;
      --text-muted: #647087;

      --accent-emerald: #00F5A0;
      --accent-emerald-subtle: rgba(0, 245, 160, 0.10);
      --accent-emerald-border: rgba(0, 245, 160, 0.28);

      --accent-cyan: #00E5FF;
      --accent-cyan-subtle: rgba(0, 229, 255, 0.10);
      --accent-cyan-border: rgba(0, 229, 255, 0.28);

      --accent-amber: #F59E0B;
      --accent-purple: #A78BFA;

      --deloitte-green: #86BC25;
      --deloitte-green-subtle: rgba(134, 188, 37, 0.12);
      --deloitte-green-border: rgba(134, 188, 37, 0.35);

      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-pill: 9999px;

      --shadow-matte: 0 4px 20px rgba(0, 0, 0, 0.45);
      --shadow-elevated: 0 10px 30px rgba(0, 0, 0, 0.65);
      --shadow-glow-emerald: 0 0 24px rgba(0, 245, 160, 0.16);
      --shadow-glow-green: 0 0 24px rgba(134, 188, 37, 0.18);

      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', SFMono-Regular, Consolas, monospace;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-canvas);
      color: var(--text-primary);
      font-family: var(--font-sans);
      font-size: 15px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
      background-image: 
        radial-gradient(ellipse at 50% 0%, rgba(134, 188, 37, 0.04) 0%, transparent 65%),
        radial-gradient(circle at 100% 20%, rgba(0, 229, 255, 0.02) 0%, transparent 50%);
      background-attachment: fixed;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    .font-mono {
      font-family: var(--font-mono);
    }

    /* ==========================================================================
       NAVIGATION BAR (EXECUTIVE, MINIMAL, TACTILE)
       ========================================================================== */
    .nav-bar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(9, 11, 14, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-matte);
      padding: 14px 0;
      transition: border-color 0.2s ease;
    }

    .nav-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }

    .nav-brand {
      display: flex;
      align-items: baseline;
      gap: 12px;
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: -0.02em;
      color: var(--text-pure);
    }

    .nav-brand-title {
      font-size: 0.75rem;
      font-weight: 500;
      color: var(--text-muted);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .nav-menu {
      display: flex;
      align-items: center;
      gap: 24px;
      list-style: none;
    }

    .nav-link {
      font-size: 0.84rem;
      font-weight: 500;
      color: var(--text-secondary);
      transition: color 0.15s ease;
    }

    .nav-link:hover {
      color: var(--text-pure);
    }

    .nav-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 5px 14px;
      background: var(--deloitte-green-subtle);
      border: 1px solid var(--deloitte-green-border);
      border-radius: var(--radius-pill);
      font-size: 0.74rem;
      font-weight: 600;
      color: #A3E635;
      font-family: var(--font-mono);
      letter-spacing: 0.02em;
    }

    .ping-circle {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--deloitte-green);
      box-shadow: 0 0 8px var(--deloitte-green);
    }

    /* ==========================================================================
       HERO ARCHITECTURE (AUTHORITATIVE, TYPOGRAPHIC, ZERO AVATARS)
       ========================================================================== */
    .hero-section {
      padding: 72px 0 54px;
      border-bottom: 1px solid var(--border-matte);
      position: relative;
    }

    .hero-eyebrow {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--deloitte-green);
      margin-bottom: 16px;
      background: var(--deloitte-green-subtle);
      border: 1px solid var(--deloitte-green-border);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
    }

    .hero-headline {
      font-size: 2.85rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.035em;
      color: var(--text-pure);
      max-width: 900px;
      margin-bottom: 20px;
    }

    .hero-headline span {
      background: linear-gradient(135deg, #FFFFFF 30%, #9DA7B8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-summary {
      font-size: 1.05rem;
      line-height: 1.65;
      color: var(--text-secondary);
      max-width: 820px;
      margin-bottom: 34px;
    }

    .hero-stats-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 36px;
      padding-top: 28px;
      border-top: 1px solid var(--border-matte);
    }

    .hero-stat-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      transition: all 0.2s ease;
    }

    .hero-stat-card:hover {
      border-color: var(--border-highlight);
      transform: translateY(-2px);
      box-shadow: var(--shadow-matte);
    }

    .hero-stat-num {
      font-family: var(--font-mono);
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 4px;
    }

    .hero-stat-label {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 9px;
      padding: 10px 20px;
      border-radius: var(--radius-sm);
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid transparent;
    }

    .btn-primary {
      background: var(--text-pure);
      color: #0B0E14;
      border-color: #FFFFFF;
    }

    .btn-primary:hover {
      background: #E2E8F0;
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(255, 255, 255, 0.2);
    }

    .btn-matte {
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      border-color: var(--border-matte);
    }

    .btn-matte:hover {
      background: var(--bg-surface);
      border-color: var(--border-highlight);
      color: var(--text-pure);
      transform: translateY(-1px);
    }

    .btn-emerald {
      background: var(--deloitte-green-subtle);
      color: #A3E635;
      border-color: var(--deloitte-green-border);
    }

    .btn-emerald:hover {
      background: rgba(134, 188, 37, 0.22);
      border-color: var(--deloitte-green);
      transform: translateY(-1px);
    }

    /* ==========================================================================
       SECTION HEADERS
       ========================================================================== */
    .section {
      padding: 72px 0;
      border-bottom: 1px solid var(--border-matte);
    }

    .section-header {
      margin-bottom: 38px;
    }

    .section-eyebrow {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--deloitte-green);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      display: inline-block;
      margin-bottom: 8px;
    }

    .section-title {
      font-size: 1.85rem;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: var(--text-pure);
      margin-bottom: 10px;
    }

    .section-desc {
      font-size: 0.94rem;
      color: var(--text-secondary);
      max-width: 780px;
      line-height: 1.6;
    }

    /* ==========================================================================
       PITCH DECKS SECTION
       ========================================================================== */
    .deck-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }

    .deck-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-lg);
      overflow: hidden;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }

    .deck-card:hover {
      border-color: var(--border-highlight);
      box-shadow: var(--shadow-elevated);
      transform: translateY(-3px);
    }

    .deck-preview-carousel {
      background: #06080B;
      padding: 16px;
      border-bottom: 1px solid var(--border-matte);
    }

    .carousel-track {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }

    .slide-thumb {
      aspect-ratio: 16 / 9;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-sm);
      overflow: hidden;
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
    }

    .slide-thumb:hover {
      border-color: var(--deloitte-green);
      transform: scale(1.02);
    }

    .slide-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .deck-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .deck-tag-row {
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .deck-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--bg-surface-elevated);
      color: var(--text-secondary);
      border: 1px solid var(--border-matte);
    }

    .deck-tag.primary {
      background: var(--deloitte-green-subtle);
      color: #A3E635;
      border-color: var(--deloitte-green-border);
    }

    .deck-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 10px;
    }

    .deck-summary {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .deck-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid var(--border-matte);
    }

    .deck-meta {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--text-muted);
    }

    /* ==========================================================================
       PRODUCT DESIGN & INTERACTIVE UI ARCHITECTURE (IMPROVED, CLEAR, TACTILE)
       ========================================================================== */
    .interactive-ui-showcase {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-matte);
    }

    .ui-showcase-bar {
      background: var(--bg-surface-elevated);
      border-bottom: 1px solid var(--border-matte);
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .ui-tabs-selector {
      display: flex;
      gap: 8px;
      background: rgba(8, 10, 14, 0.6);
      padding: 4px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-matte);
    }

    .ui-tab-btn {
      background: transparent;
      border: 1px solid transparent;
      border-radius: 4px;
      padding: 8px 18px;
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .ui-tab-btn:hover {
      color: var(--text-pure);
      background: rgba(255, 255, 255, 0.05);
    }

    .ui-tab-btn.active {
      background: var(--bg-card);
      border-color: var(--border-highlight);
      color: var(--text-pure);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    .ui-tab-btn.active .tab-indicator {
      background: var(--deloitte-green);
      box-shadow: 0 0 6px var(--deloitte-green);
    }

    .tab-indicator {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--text-muted);
    }

    .ui-demo-prompt-pill {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: #A3E635;
      background: var(--deloitte-green-subtle);
      border: 1px solid var(--deloitte-green-border);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .ui-stage-canvas {
      padding: 28px;
      min-height: 420px;
    }

    /* Sub-Module 1: Telemetry HUD */
    .hud-grid {
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
    }

    .hud-metrics-column {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .hud-metric-card {
      background: var(--bg-canvas);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      transition: all 0.2s ease;
    }

    .hud-metric-card:hover {
      border-color: var(--border-highlight);
    }

    .hud-metric-label {
      font-size: 0.72rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-family: var(--font-mono);
      margin-bottom: 4px;
    }

    .hud-metric-value {
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-pure);
    }

    .hud-console-panel {
      background: var(--bg-canvas);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-sm);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .hud-console-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-matte);
      padding-bottom: 10px;
    }

    .hud-console-title {
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--text-pure);
    }

    .hud-log-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      padding: 8px 12px;
      border-radius: 4px;
      background: var(--bg-surface);
      border: 1px solid rgba(255, 255, 255, 0.03);
    }

    /* Sub-Module 2: Design System Specs */
    .tokens-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }

    .token-card {
      background: var(--bg-canvas);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-sm);
      padding: 18px;
    }

    .token-title {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 12px;
      font-family: var(--font-mono);
      text-transform: uppercase;
    }

    .color-swatch-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
      font-size: 0.78rem;
    }

    .swatch-box {
      width: 20px;
      height: 20px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .interactive-btn-previewer {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 10px;
    }

    /* Sub-Module 3: VFX Ingest Table */
    .vfx-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
    }

    .vfx-table th {
      text-align: left;
      padding: 10px 14px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-matte);
      text-transform: uppercase;
    }

    .vfx-table td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-secondary);
    }

    .vfx-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
      color: var(--text-pure);
    }

    .status-badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: var(--radius-pill);
      font-weight: 600;
    }

    .status-badge.pass {
      background: var(--deloitte-green-subtle);
      color: #A3E635;
      border: 1px solid var(--deloitte-green-border);
    }

    .status-badge.subpixel {
      background: var(--accent-cyan-subtle);
      color: var(--accent-cyan);
      border: 1px solid var(--accent-cyan-border);
    }

    /* ==========================================================================
       MOTION GRAPHICS SECTION (GENUINE HONEST ARCHITECTURE & CLEAN AUDIO)
       ========================================================================== */
    .motion-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }

    .motion-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }

    .motion-card:hover {
      border-color: var(--border-highlight);
      box-shadow: var(--shadow-elevated);
      transform: translateY(-3px);
    }

    .video-viewport {
      aspect-ratio: 9 / 16;
      max-height: 540px;
      background: #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .video-viewport video {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #050709;
    }

    .motion-body {
      padding: 22px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .motion-badge {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--deloitte-green);
      font-weight: 600;
      margin-bottom: 8px;
    }

    .motion-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 8px;
    }

    .motion-desc {
      font-size: 0.86rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }

    .motion-stack-box {
      background: var(--bg-canvas);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      font-size: 0.76rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }

    .motion-stack-box strong {
      color: var(--text-secondary);
    }

    .disclosure-banner {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-left: 3px solid var(--deloitte-green);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 30px;
    }

    .disclosure-banner h4 {
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 4px;
    }

    .disclosure-banner p {
      font-size: 0.85rem;
      color: var(--text-secondary);
      line-height: 1.55;
    }

    /* ==========================================================================
       3D ENVIRONMENTS & VIRTUAL SETS (INSTAGRAM PRIMITIVE-BASED CAPTURES)
       ========================================================================== */
    .spatial-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    .spatial-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-md);
      overflow: hidden;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }

    .spatial-card:hover {
      border-color: var(--border-highlight);
      transform: translateY(-3px);
      box-shadow: var(--shadow-matte);
    }

    .spatial-img-box {
      aspect-ratio: 16 / 10;
      background: #05070A;
      overflow: hidden;
      cursor: pointer;
      position: relative;
    }

    .spatial-img-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
      display: block;
    }

    .spatial-img-box:hover img {
      transform: scale(1.03);
    }

    .spatial-body {
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    /* ==========================================================================
       PRODUCTION RECORDS & CREDENTIALS (HUMAN, CLEAN, UNIQUE, AESTHETIC)
       ========================================================================== */
    .dossier-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 36px;
    }

    .dossier-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-lg);
      padding: 26px 24px;
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }

    .dossier-card:hover {
      border-color: var(--border-highlight);
      box-shadow: var(--shadow-matte);
      transform: translateY(-2px);
    }

    .dossier-card-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 600;
      color: var(--deloitte-green);
      letter-spacing: 0.04em;
      margin-bottom: 12px;
      text-transform: uppercase;
    }

    .dossier-card-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 12px;
      line-height: 1.3;
    }

    .dossier-card-desc {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .dossier-pills-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: auto;
    }

    .dossier-pill {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      background: var(--bg-canvas);
      border: 1px solid var(--border-matte);
      padding: 3px 8px;
      border-radius: 4px;
      color: var(--text-muted);
    }

    /* Dual Education & Availability Box */
    .dual-credentials-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    .credential-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-matte);
      border-radius: var(--radius-lg);
      padding: 26px;
    }

    .credential-box-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .edu-item {
      padding-bottom: 16px;
      margin-bottom: 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .edu-item:last-child {
      padding-bottom: 0;
      margin-bottom: 0;
      border-bottom: none;
    }

    .edu-deg {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-pure);
      margin-bottom: 3px;
    }

    .edu-inst {
      font-size: 0.84rem;
      color: var(--deloitte-green);
      font-family: var(--font-mono);
      margin-bottom: 4px;
    }

    .edu-note {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* Availability items */
    .avail-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      font-size: 0.86rem;
    }

    .avail-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }

    .avail-label {
      color: var(--text-secondary);
    }

    .avail-val {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--text-pure);
    }

    /* ==========================================================================
       MODAL & LIGHTBOX
       ========================================================================== */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(5, 7, 10, 0.92);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .modal-overlay.active {
      display: flex;
    }

    .modal-container {
      background: var(--bg-surface);
      border: 1px solid var(--border-highlight);
      border-radius: var(--radius-lg);
      max-width: 1000px;
      width: 100%;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
    }

    .modal-header {
      padding: 16px 22px;
      border-bottom: 1px solid var(--border-matte);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .modal-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-pure);
    }

    .modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
      padding: 4px;
      transition: color 0.15s ease;
    }

    .modal-close:hover {
      color: var(--text-pure);
    }

    .modal-body {
      padding: 22px;
      overflow-y: auto;
      text-align: center;
    }

    .modal-body img {
      max-width: 100%;
      max-height: 70vh;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-matte);
      object-fit: contain;
    }

    .modal-desc {
      margin-top: 14px;
      font-size: 0.88rem;
      color: var(--text-secondary);
      text-align: left;
      line-height: 1.6;
    }

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .site-footer {
      padding: 48px 0;
      border-top: 1px solid var(--border-matte);
      background: var(--bg-surface);
    }

    .footer-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .footer-info {
      font-size: 0.84rem;
      color: var(--text-muted);
    }

    .footer-links {
      display: flex;
      gap: 18px;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .deck-grid, .motion-grid, .dual-credentials-row {
        grid-template-columns: 1fr;
      }
      .spatial-grid, .dossier-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .hero-stats-row {
        grid-template-columns: repeat(2, 1fr);
      }
      .hud-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 640px) {
      .spatial-grid, .dossier-grid {
        grid-template-columns: 1fr;
      }
      .hero-stats-row {
        grid-template-columns: 1fr;
      }
      .nav-menu {
        display: none;
      }
      .hero-headline {
        font-size: 2.1rem;
      }
    }
  </style>
</head>
<body>

  <!-- NAVIGATION -->
  <nav class="nav-bar">
    <div class="container nav-inner">
      <a href="#" class="nav-brand">
        <span>Benny Joel Lakamana</span>
        <span class="nav-brand-title">Visual Designer & Technical Director</span>
      </a>

      <ul class="nav-menu">
        <li><a href="#pitch-decks" class="nav-link">Pitch Decks</a></li>
        <li><a href="#interface-design" class="nav-link">UI Architecture</a></li>
        <li><a href="#motion-graphics" class="nav-link">Motion Systems</a></li>
        <li><a href="#virtual-sets" class="nav-link">3D & Virtual Sets</a></li>
        <li><a href="#credentials" class="nav-link">Production Dossier</a></li>
      </ul>

      <div class="nav-status-pill">
        <span class="ping-circle"></span>
        <span>Available for Immediate Placement • Hyderabad, India</span>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section class="hero-section">
    <div class="container">
      <span class="hero-eyebrow">Visual Design • Real-Time 3D Architecture • Programmatic Motion</span>
      <h1 class="hero-headline">
        Executive Visual Design, Feature Film Pitch Decks & <span>Motion Production Systems</span>
      </h1>
      <p class="hero-summary">
        Synthesizing high-stakes visual communication, 140+ feature film VFX shot coordination, real-time Unreal Engine 5 virtual set extensions, and code-driven 60fps kinetic motion graphics. Engineered for enterprise precision and immediate rotational shift deployment.
      </p>

      <div class="hero-actions">
        <a href="assets/docs/Benny_Joel_Lakamana_Resume_Deloitte.pdf" target="_blank" class="btn btn-primary">
          <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span>Download Executive Resume (PDF)</span>
        </a>
        <a href="assets/docs/Benny_Joel_Lakamana_Cover_Letter_Deloitte.pdf" target="_blank" class="btn btn-matte">
          <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span>View Cover Letter (PDF)</span>
        </a>
        <a href="https://github.com/bennyjoel/portfolio" target="_blank" class="btn btn-emerald">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
          <span>Verified GitHub Repository</span>
        </a>
      </div>

      <div class="hero-stats-row">
        <div class="hero-stat-card">
          <div class="hero-stat-num" style="color: #A3E635;">140+ Shots</div>
          <div class="hero-stat-label">VFX Coordinated • Feature Film</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num" style="color: var(--accent-cyan);">2 Pitch Decks</div>
          <div class="hero-stat-label">Theatrical & 3D Short Film</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num" style="color: #FFFFFF;">Sub-Pixel</div>
          <div class="hero-stat-label">0.34px Syntheyes 3D Solves</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num" style="color: var(--accent-purple);">4-Year BFA</div>
          <div class="hero-stat-label">Fine Arts in Animation • JNAFAU</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 1: PITCH DECKS -->
  <section class="section" id="pitch-decks">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Theatrical & Animation Decks</span>
        <h2 class="section-title">Executive Technical Pitch Decks</h2>
        <p class="section-desc">
          High-impact executive slide decks presenting complex cinematic workflows, matchmoving mathematics, Unreal Engine 5 virtual production pipelines, and character world-building.
        </p>
      </div>

      <div class="deck-grid">
        <!-- DECK 1: TAKSHAKA -->
        <div class="deck-card">
          <div class="deck-preview-carousel">
            <div class="carousel-track">
              <div class="slide-thumb" onclick="openModal('assets/images/slide_01_cover.png', 'Takshaka: Executive Title Slide', 'Opening title slide establishing visual narrative, cinematic mood, and production hierarchy.')">
                <img src="assets/images/slide_01_cover.png" alt="Takshaka Slide 1">
              </div>
              <div class="slide-thumb" onclick="openModal('assets/images/slide_02_camera_log.png', 'Takshaka: On-Set Camera Metadata Ingest', 'Technical breakdown of Arri/RED raw camera log intake, lens focal calibration, and Macbeth chart extraction.')">
                <img src="assets/images/slide_02_camera_log.png" alt="Takshaka Slide 2">
              </div>
              <div class="slide-thumb" onclick="openModal('assets/images/slide_04_3d_matchmove.png', 'Takshaka: Syntheyes 3D Matchmove & Camera Recovery', 'Demonstration of sub-pixel 3D camera tracking solving nodal rotation and translation for Unreal/Maya handoff.')">
                <img src="assets/images/slide_04_3d_matchmove.png" alt="Takshaka Slide 4">
              </div>
            </div>
          </div>
          <div class="deck-body">
            <div class="deck-tag-row">
              <span class="deck-tag primary">FEATURE FILM DEFENSE DECK</span>
              <span class="deck-tag">14 SLIDES</span>
              <span class="deck-tag">ON-SET METRIC PROOF</span>
            </div>
            <h3 class="deck-title">Takshaka: Feature Film Technical Defense Deck</h3>
            <p class="deck-summary">
              Comprehensive technical presentation defending on-set camera data logging, 3D Syntheyes camera recovery, Unreal Engine 5 virtual set extension, and high-fidelity live plate reconstruction across 140+ feature film VFX shots.
            </p>
            <div class="deck-footer">
              <span class="deck-meta">14 SLIDES • 1920x1080 MASTER PDF</span>
              <a href="assets/decks/Takshaka_VFX_Master_Pitch_Deck.pdf" target="_blank" class="btn btn-matte" style="padding: 6px 14px; font-size: 0.78rem;">
                <span>View Full PDF ↗</span>
              </a>
            </div>
          </div>
        </div>

        <!-- DECK 2: CRUCIBLE -->
        <div class="deck-card">
          <div class="deck-preview-carousel">
            <div class="carousel-track">
              <div class="slide-thumb" onclick="openModal('assets/images/crucible_slide_01.png', 'Crucible: 3D Cinematic Short Film Pitch Deck', 'Title presentation introducing the animated universe, dark luxury aesthetic, and thematic lore.')">
                <img src="assets/images/crucible_slide_01.png" alt="Crucible Slide 1">
              </div>
              <div class="slide-thumb" onclick="openModal('assets/images/crucible_slide_05.png', 'Crucible: Character Design & Silhouette Breakdown', 'Architectural character silhouettes, anatomy reference, and Unreal Engine 5 Substrate shading specs.')">
                <img src="assets/images/crucible_slide_05.png" alt="Crucible Slide 5">
              </div>
              <div class="slide-thumb" onclick="openModal('assets/images/crucible_slide_12.png', 'Crucible: Real-Time Environment Previs & Lighting', 'Unreal Engine 5 Lumen lighting pass, volumetric fog density, and virtual production set extensions.')">
                <img src="assets/images/crucible_slide_12.png" alt="Crucible Slide 12">
              </div>
            </div>
          </div>
          <div class="deck-body">
            <div class="deck-tag-row">
              <span class="deck-tag primary">3D ANIMATED SHORT FILM</span>
              <span class="deck-tag">20 SLIDES</span>
              <span class="deck-tag">UE5 REAL-TIME PREVIS</span>
            </div>
            <h3 class="deck-title">Crucible: 3D Cinematic Pitch Deck</h3>
            <p class="deck-summary">
              20-page master cinematic pitch deck for an animated short film. Details character world-building, high-stress facial silhouette design, Unreal Engine 5 Lumen lighting setup, and real-time virtual camera previs.
            </p>
            <div class="deck-footer">
              <span class="deck-meta">20 SLIDES • 1920x1080 MASTER PDF</span>
              <a href="assets/decks/Crucible_3D_Cinematic_Pitch_Deck.pdf" target="_blank" class="btn btn-matte" style="padding: 6px 14px; font-size: 0.78rem;">
                <span>View Full PDF ↗</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: INTERFACE & EXPERIENCE DESIGN (IMPROVED, ACCESSIBLE, TACTILE) -->
  <section class="section" id="interface-design">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Interface & Experience Design</span>
        <h2 class="section-title">Design System Architecture & Interactive UI</h2>
        <p class="section-desc">
          Designing scalable, accessible digital interfaces with high data density. Test the interactive modules below to verify hierarchy control, tactile button states, and live telemetry synchronization.
        </p>
      </div>

      <div class="interactive-ui-showcase">
        <!-- Top Tab Bar -->
        <div class="ui-showcase-bar">
          <div class="ui-tabs-selector">
            <button class="ui-tab-btn active" onclick="switchUIStage('telemetry', this)">
              <span class="tab-indicator"></span>
              <span>1. Live Telemetry HUD</span>
            </button>
            <button class="ui-tab-btn" onclick="switchUIStage('tokens', this)">
              <span class="tab-indicator"></span>
              <span>2. Design System Tokens</span>
            </button>
            <button class="ui-tab-btn" onclick="switchUIStage('vfx-stream', this)">
              <span class="tab-indicator"></span>
              <span>3. VFX Production Ingest</span>
            </button>
          </div>

          <div class="ui-demo-prompt-pill">
            <span>● PROTOTYPE WORKSTATION</span>
            <span style="color: var(--text-muted);">|</span>
            <span>CLICK TABS TO INSPECT</span>
          </div>
        </div>

        <!-- Canvas Body Area -->
        <div class="ui-stage-canvas" id="uiStageCanvas">
          <!-- Populated dynamically via JS -->
        </div>

        <!-- Bottom Bar -->
        <div style="padding: 14px 24px; background: var(--bg-surface-elevated); border-top: 1px solid var(--border-matte); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">
            WCAG AAA High Contrast • 8px Grid Spacing • Zero State Collisions
          </span>
          <span style="font-size: 0.78rem; color: #A3E635; font-family: var(--font-mono); font-weight: 600;">
            DESIGN SYSTEM v2.5 ACTIVE
          </span>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: MOTION GRAPHICS (HONEST, ACCURATE ARCHITECTURE & CLEAN AUDIO) -->
  <section class="section" id="motion-graphics">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Programmatic Motion & Creative Tech</span>
        <h2 class="section-title">Broadcast Motion Graphics & Kinetic Typography</h2>
        <p class="section-desc">
          High-velocity typography, dark luxury UI motion, and real-time audio-reactive rendering engineered programmatically at 1080x1920 60fps.
        </p>
      </div>

      <!-- Honest Tooling Disclosure -->
      <div class="disclosure-banner">
        <h4>Technical Production Pipeline & Tooling Disclosure</h4>
        <p>
          These motion sequences were engineered using <strong>Google Antigravity</strong> (agentic code development) coupled with <strong>reverse-engineered clean-room creative engines (EffectCraft & headless rendering pipelines)</strong> alongside <strong>Adobe After Effects</strong>. By translating typography hierarchies, spring easing mathematics, and design tokens directly into code-driven composition graphs, we eliminated manual keyframing and rendered broadcast-grade 1080x1920 60fps video at machine speed.
        </p>
      </div>

      <div class="motion-grid">
        <!-- REEL 1: APEX MOTION (CLEAN SINGLE-VOICE AUDIO) -->
        <div class="motion-card">
          <div class="video-viewport">
            <video controls poster="assets/images/thumb_apex_motion.jpg" preload="metadata">
              <source src="assets/videos/apex_motion_reel.mp4" type="video/mp4">
              Your browser does not support HTML5 video.
            </video>
          </div>
          <div class="motion-body">
            <span class="motion-badge">Apex Grand Motion System • Clean Broadcast Master</span>
            <h3 class="motion-title">Apex Grand Motion System (SYS-035)</h3>
            <p class="motion-desc">
              High-contrast luxury dark UI motion with expanding radial rings, fluid typographic reveals, and sub-millisecond code execution telemetry. Mastered audio with clean Christopher neural voiceover and EBU R128 loudness normalization.
            </p>
            <div class="motion-stack-box">
              <strong>Pipeline:</strong> Antigravity Agentic Code • Headless EffectCraft Engine • 1080x1920 60fps
            </div>
          </div>
        </div>

        <!-- REEL 2: KINETIC TYPOGRAPHY -->
        <div class="motion-card">
          <div class="video-viewport">
            <video controls poster="assets/images/thumb_kinetic_typography.jpg" preload="metadata">
              <source src="assets/videos/kinetic_typography_reel.mp4" type="video/mp4">
              Your browser does not support HTML5 video.
            </video>
          </div>
          <div class="motion-body">
            <span class="motion-badge">High-Velocity Typography • Spring Easing</span>
            <h3 class="motion-title">Kinetic Typographic Identity System</h3>
            <p class="motion-desc">
              Dynamic kinetic typography highlighting typographic scale, negative tracking, and spring momentum easing for broadcast and executive social distribution.
            </p>
            <div class="motion-stack-box">
              <strong>Pipeline:</strong> Reverse-Engineered EffectCraft Core • Spring Physics • 1080x1920 60fps
            </div>
          </div>
        </div>

        <!-- REEL 3: TITANIUM METERING -->
        <div class="motion-card">
          <div class="video-viewport">
            <video controls poster="assets/images/thumb_titanium_metering.jpg" preload="metadata">
              <source src="assets/videos/titanium_metering_reel.mp4" type="video/mp4">
              Your browser does not support HTML5 video.
            </video>
          </div>
          <div class="motion-body">
            <span class="motion-badge">Telemetry HUD • Dynamic Data Streams</span>
            <h3 class="motion-title">Titanium Metering & Telemetry HUD</h3>
            <p class="motion-desc">
              Precision technical data visualization showcasing live counters, audio waveform reactive meters, and real-time pipeline status cards in a dark titanium aesthetic.
            </p>
            <div class="motion-stack-box">
              <strong>Pipeline:</strong> Procedural Math Shaders • Headless Clean-Room Render Engine
            </div>
          </div>
        </div>

        <!-- REEL 4: FLUID SWISS -->
        <div class="motion-card">
          <div class="video-viewport">
            <video controls poster="assets/images/thumb_fluid_swiss.jpg" preload="metadata">
              <source src="assets/videos/fluid_swiss_reel.mp4" type="video/mp4">
              Your browser does not support HTML5 video.
            </video>
          </div>
          <div class="motion-body">
            <span class="motion-badge">Swiss Grotesque • Editorial Layout</span>
            <h3 class="motion-title">Swiss Monolith Editorial Motion</h3>
            <p class="motion-desc">
              Editorial-style motion graphics implementing Swiss International Typographic Style principles: strict mathematical grid alignment, high-contrast black/white geometry, and fluid mask wipe transitions.
            </p>
            <div class="motion-stack-box">
              <strong>Pipeline:</strong> Antigravity Code Orchestrator • Adobe After Effects Comp Graph
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: 3D ENVIRONMENTS & VIRTUAL SETS (INSTAGRAM PRIMITIVE-BASED RENDERS) -->
  <section class="section" id="virtual-sets">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Real-Time 3D & Virtual Production</span>
        <h2 class="section-title">3D Environments, Virtual Sets & Camera Tracking</h2>
        <p class="section-desc">
          High-resolution 3D environments, virtual background plates, and theatrical camera tracking authored in Unreal Engine 5, Autodesk Maya, and Syntheyes. High-resolution captures from the primitive-based project archives.
        </p>
      </div>

      <div class="spatial-grid">
        <!-- ENV 1: INSTAGRAM FEATURED RIVER GORGE & WATER SHADERS -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_instagram_river_gorge.jpg', 'Unreal Engine 5: Mountain River Gorge & Water Shaders', 'Cinematic high-resolution mountain river gorge featuring real-time translucent water shaders, mossy riverbed displacement, and lush pine forest canopy. Featured on Instagram (@primitive-based project archive).')">
            <img src="assets/images/env_instagram_river_gorge.jpg" alt="UE5 Mountain River Gorge">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Unreal Engine 5 • Instagram Featured (@primitive)</span>
            <h3 class="motion-title">Mountain River Gorge & Water Shaders</h3>
            <p class="motion-desc">
              Real-time translucent water shading, dynamic riverbed moss displacement, and procedural foliage scattering authored in Unreal Engine 5. Rendered at 6.6K master fidelity.
            </p>
          </div>
        </div>

        <!-- ENV 2: NIGHT SANCTUARY (INSTAGRAM FEATURED) -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_night_sanctuary_moonlight.jpg', 'Unreal Engine 5: Ancient Sanctuary & Overgrown Ruins (Night)', 'Real-time Unreal Engine 5 cinematic night environment featuring dynamic Lumen moonlight, volumetric mist, and Nanite moss/foliage overgrowth across classical ruin geometry. As featured on Instagram (@primitive-based project archive).')">
            <img src="assets/images/env_night_sanctuary_moonlight.jpg" alt="UE5 Night Sanctuary">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Unreal Engine 5 • Lumen Moonlight</span>
            <h3 class="motion-title">Ancient Sanctuary & Overgrowth (Night)</h3>
            <p class="motion-desc">
              Real-time atmospheric night lighting with dynamic Lumen bounce, volumetric moonlight shafts, and Nanite foliage integration. Featured on Instagram (@primitive archive).
            </p>
          </div>
        </div>

        <!-- ENV 3: DAY TEMPLE COLONNADE -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_day_temple_arch.jpg', 'Unreal Engine 5: Grand Temple Colonnade (Daylight)', 'Expansive daylight architectural set extension with sun-angled cast shadows, physical stone displacement, and aerial perspective depth.')">
            <img src="assets/images/env_day_temple_arch.jpg" alt="UE5 Day Temple Arch">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Unreal Engine 5 • Daylight Illumination</span>
            <h3 class="motion-title">Grand Temple Colonnade (Daylight)</h3>
            <p class="motion-desc">
              Monumental architectural environment built with Nanite geometry, real-time sun illumination, and calibrated camera focal depth.
            </p>
          </div>
        </div>

        <!-- ENV 4: CATHEDRAL VAULT RUINS -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_night_cathedral_ruins.jpg', 'Unreal Engine 5: Subterranean Cathedral Vault', 'High-vaulted structural hall with directional god-rays, physical materials, and camera depth-of-field calibration.')">
            <img src="assets/images/env_night_cathedral_ruins.jpg" alt="UE5 Cathedral Ruins">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Atmospheric Volumetrics • Shading</span>
            <h3 class="motion-title">Subterranean Cathedral Vault</h3>
            <p class="motion-desc">
              Cathedral-scale interior environment testing dramatic upward focal perspectives, roughness variation, and high-dynamic-range illumination.
            </p>
          </div>
        </div>

        <!-- ENV 5: DAWN COURTYARD VISTA -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_dawn_atmospheric_courtyard.jpg', 'Unreal Engine 5: Dawn Atmospheric Courtyard', 'Golden hour exterior architectural lighting study showcasing low-angle directional sunlight, atmospheric hazing, and stone wear details.')">
            <img src="assets/images/env_dawn_atmospheric_courtyard.jpg" alt="UE5 Dawn Courtyard">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Lighting Study • Golden Hour</span>
            <h3 class="motion-title">Dawn Atmospheric Courtyard</h3>
            <p class="motion-desc">
              Golden hour exterior architectural lighting study showcasing low-angle directional sunlight, atmospheric hazing, and stone wear details.
            </p>
          </div>
        </div>

        <!-- ENV 6: WORLDBREAKER GAME LEVEL -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_worldbreaker_cinematic.jpg', 'Unreal Engine 5: Worldbreaker Game Level & Terrain', 'High-scale real-time environment built for gameplay traversal, Nanite geometry streaming, and cinematic camera choreography in Worldbreaker.')">
            <img src="assets/images/env_worldbreaker_cinematic.jpg" alt="Worldbreaker Environment">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Level Design • World Partition</span>
            <h3 class="motion-title">Worldbreaker Game Level & Terrain</h3>
            <p class="motion-desc">
              Expansive real-time level built in Unreal Engine for Worldbreaker, engineered for seamless camera traversal and multi-layered atmospheric lighting.
            </p>
          </div>
        </div>

        <!-- ENV 7: NIGHT FOREST BIOME -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/env_night_forest_overgrowth.jpg', 'Unreal Engine 5: Night Forest Overgrowth & Biome', 'High-density procedural pine and undergrowth biome with nocturnal ambient lighting, wet ground roughness mapping, and deep forest volumetrics.')">
            <img src="assets/images/env_night_forest_overgrowth.jpg" alt="UE5 Night Forest">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Biome Scattering • Procedural Foliage</span>
            <h3 class="motion-title">Night Forest Overgrowth & Biome</h3>
            <p class="motion-desc">
              High-density procedural pine and undergrowth biome with nocturnal ambient lighting, wet ground roughness mapping, and deep forest volumetrics.
            </p>
          </div>
        </div>

        <!-- ENV 8: SYNTHEYES CAMERA TRACKING -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/test_syntheyes_track.png', 'Syntheyes 3D Camera Tracking & Solve', 'Solving real-world optical distortion, sensor dimensions, and nodal camera rotations from theatrical rushes with sub-pixel precision (0.34px).')">
            <img src="assets/images/test_syntheyes_track.png" alt="Syntheyes 3D Tracking">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Matchmoving & Spatial Survey</span>
            <h3 class="motion-title">Syntheyes 3D Camera Matchmove</h3>
            <p class="motion-desc">
              Solving real-world optical distortion, sensor dimensions, and nodal camera rotations from theatrical rushes with sub-pixel precision (<0.5px).
            </p>
          </div>
        </div>

        <!-- ENV 9: FEATURE FILM PLATE PREP -->
        <div class="spatial-card">
          <div class="spatial-img-box" onclick="openModal('assets/images/shot_150s_clean.png', 'Theatrical Plate Extraction & Matte Cleanup', 'Digital clean-plate generation, rig extraction, and background extension preparation ensuring seamless CGI integration.')">
            <img src="assets/images/shot_150s_clean.png" alt="Theatrical Plate Extraction">
          </div>
          <div class="spatial-body">
            <span class="motion-badge">Feature Film VFX • 140+ Shots</span>
            <h3 class="motion-title">Theatrical Plate Prep & Wire Removal</h3>
            <p class="motion-desc">
              On-set Macbeth chart extraction, dynamic rig/wire extraction, and high-fidelity clean plate reconstruction for VFX compositor handoff.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: PRODUCTION DOSSIER & CREDENTIALS (HUMAN, CLEAN, UNIQUE, AESTHETIC) -->
  <section class="section" id="credentials">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Verified Track Record</span>
        <h2 class="section-title">Production Records & Enterprise Credentials</h2>
        <p class="section-desc">
          Concrete studio production deliveries across feature film VFX pipelines, real-time 3D previs, and scalable design system engineering.
        </p>
      </div>

      <!-- 3 Production Cards -->
      <div class="dossier-grid">
        <!-- CARD 1: TAKSHAKA -->
        <div class="dossier-card">
          <span class="dossier-card-tag">FEATURE FILM • LEAD VFX COORDINATOR</span>
          <h3 class="dossier-card-title">Takshaka: On-Set VFX & Theatrical Coordination</h3>
          <p class="dossier-card-desc">
            Directed on-set data acquisition across principal photography: Macbeth color chart registration, 360° HDRI lighting brackets, and Arri/RED raw camera metadata logging. Managed 140+ VFX shots through Syntheyes 3D matchmoving, wire removal, and final supervisor review.
          </p>
          <div class="dossier-pills-row">
            <span class="dossier-pill">140+ Shots</span>
            <span class="dossier-pill">Syntheyes 3D</span>
            <span class="dossier-pill">Macbeth HDRI</span>
            <span class="dossier-pill">Arri/RED Conform</span>
          </div>
        </div>

        <!-- CARD 2: CRUCIBLE & UE5 -->
        <div class="dossier-card">
          <span class="dossier-card-tag">ANIMATED SHORT FILM • 3D TECHNICAL ARTIST</span>
          <h3 class="dossier-card-title">Crucible: Real-Time Previs & Virtual Production</h3>
          <p class="dossier-card-desc">
            Authored complete 20-page technical defense pitch deck for Unreal Engine 5 animated short film production. Engineered real-time virtual camera rigs, Nanite mesh optimization, and Lumen dynamic lighting passes for immediate executive previsualization.
          </p>
          <div class="dossier-pills-row">
            <span class="dossier-pill">20-Page Pitch Deck</span>
            <span class="dossier-pill">Unreal Engine 5</span>
            <span class="dossier-pill">Lumen Lighting</span>
            <span class="dossier-pill">Nanite Geometry</span>
          </div>
        </div>

        <!-- CARD 3: DESIGN SYSTEMS -->
        <div class="dossier-card">
          <span class="dossier-card-tag">INTERFACE ARCHITECTURE • MOTION SYSTEMS</span>
          <h3 class="dossier-card-title">Enterprise Design Systems & Programmatic Motion</h3>
          <p class="dossier-card-desc">
            Architected scalable digital interfaces with strict typographic balance, 8px layout grids, and WCAG AAA accessibility. Pioneered code-driven motion graphics combining agentic code, reverse-engineered clean-room engines, and After Effects for 60fps renders.
          </p>
          <div class="dossier-pills-row">
            <span class="dossier-pill">Design Tokens</span>
            <span class="dossier-pill">Adobe Photoshop</span>
            <span class="dossier-pill">After Effects</span>
            <span class="dossier-pill">60fps Motion</span>
          </div>
        </div>
      </div>

      <!-- DUAL EDUCATION & AVAILABILITY ROW -->
      <div class="dual-credentials-row">
        <!-- Academic Qualifications -->
        <div class="credential-box">
          <h4 class="credential-box-title">
            <svg width="18" height="18" fill="none" stroke="var(--deloitte-green)" stroke-width="2" viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            <span>Academic Qualifications</span>
          </h4>

          <div class="edu-item">
            <div class="edu-deg">Bachelor of Fine Arts (BFA) in Digital Animation</div>
            <div class="edu-inst">JNAFAU (Jawaharlal Nehru Architecture & Fine Arts University) • Hyderabad</div>
            <div class="edu-note">
              4-Year comprehensive university degree covering classical art anatomy, 3D CGI modeling, cinematography, and spatial digital painting.
            </div>
          </div>

          <div class="edu-item">
            <div class="edu-deg">Advanced Diploma in 3D Animation & VFX</div>
            <div class="edu-inst">Arena Animation • Hyderabad, India</div>
            <div class="edu-note">
              Intensive studio training in 3D pipeline asset authoring, dynamic lighting setups, and digital compositing.
            </div>
          </div>
        </div>

        <!-- Professional Availability -->
        <div class="credential-box">
          <h4 class="credential-box-title">
            <svg width="18" height="18" fill="none" stroke="#A3E635" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span>Professional Availability & Location</span>
          </h4>

          <div class="avail-row">
            <span class="avail-label">Current Location:</span>
            <span class="avail-val">Hyderabad, Telangana, India</span>
          </div>
          <div class="avail-row">
            <span class="avail-label">Office Proximity:</span>
            <span class="avail-val">Immediate Begumpet & HITEC City Transit</span>
          </div>
          <div class="avail-row">
            <span class="avail-label">Shift Readiness:</span>
            <span class="avail-val" style="color: #A3E635;">100% Rotational Shifts (11 AM – 8 PM / Flexible)</span>
          </div>
          <div class="avail-row">
            <span class="avail-label">Notice Period:</span>
            <span class="avail-val" style="color: var(--accent-cyan);">Immediate Joining (Zero Day Notice)</span>
          </div>
          <div class="avail-row">
            <span class="avail-label">Primary Workstation:</span>
            <span class="avail-val">Dual-Monitor High-Compute Rig + Full Studio Setup</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LIGHTBOX MODAL -->
  <div class="modal-overlay" id="imageModal" onclick="closeModal(event)">
    <div class="modal-container" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 class="modal-title" id="modalTitle">Preview</h3>
        <button class="modal-close" onclick="closeModal(event)">&times;</button>
      </div>
      <div class="modal-body">
        <img id="modalImg" src="" alt="Enlarged Preview">
        <p class="modal-desc" id="modalDesc"></p>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-info">
        <strong style="color: var(--text-pure);">Benny Joel Lakamana</strong> • Visual Designer & Technical Director • Hyderabad, India
      </div>
      <div class="footer-links">
        <a href="assets/docs/Benny_Joel_Lakamana_Resume_Deloitte.pdf" target="_blank" class="nav-link">Resume (PDF)</a>
        <a href="assets/decks/Takshaka_VFX_Master_Pitch_Deck.pdf" target="_blank" class="nav-link">Takshaka Deck</a>
        <a href="assets/decks/Crucible_3D_Cinematic_Pitch_Deck.pdf" target="_blank" class="nav-link">Crucible Deck</a>
        <a href="https://github.com/bennyjoel/portfolio" target="_blank" class="nav-link">GitHub</a>
      </div>
    </div>
  </footer>

  <!-- INTERACTIVE WORKSTATION JAVASCRIPT -->
  <script>
    const stageData = {
      'telemetry': `
        <div class="hud-grid">
          <div class="hud-metrics-column">
            <div class="hud-metric-card">
              <div class="hud-metric-label">Global Pipeline Health</div>
              <div class="hud-metric-value" style="color: #A3E635;">99.98%</div>
            </div>
            <div class="hud-metric-card">
              <div class="hud-metric-label">Render Dispatch Latency</div>
              <div class="hud-metric-value" style="color: var(--accent-cyan);">&lt; 14 ms</div>
            </div>
            <div class="hud-metric-card">
              <div class="hud-metric-label">WCAG Contrast Ratio</div>
              <div class="hud-metric-value" style="color: #FFFFFF;">18.4 : 1</div>
            </div>
          </div>

          <div class="hud-console-panel">
            <div class="hud-console-header">
              <span class="hud-console-title">Real-Time Production Feed & Node Verification</span>
              <span class="font-mono" style="font-size: 0.72rem; color: #A3E635;">● SYNCHRONIZED</span>
            </div>

            <div class="hud-log-row">
              <span><strong style="color: var(--text-pure);">[INGEST-01]</strong> Arri RAW 4K Conform & Color Space Hash Verification</span>
              <span class="font-mono" style="color: #A3E635; font-size: 0.72rem;">PASS (0.00ms)</span>
            </div>
            <div class="hud-log-row">
              <span><strong style="color: var(--text-pure);">[MATCHMOVE]</strong> Syntheyes Feature Tracking Marker Grid Solved</span>
              <span class="font-mono" style="color: var(--accent-cyan); font-size: 0.72rem;">0.34px RESIDUAL</span>
            </div>
            <div class="hud-log-row">
              <span><strong style="color: var(--text-pure);">[UE5-PREVIS]</strong> Nanite Colonnade Mesh Virtual Extension Buffer</span>
              <span class="font-mono" style="color: #A3E635; font-size: 0.72rem;">STREAMING (60 FPS)</span>
            </div>
            <div class="hud-log-row">
              <span><strong style="color: var(--text-pure);">[MOTION-AE]</strong> Headless EffectCraft 1080x1920 60fps MP4 Master</span>
              <span class="font-mono" style="color: var(--accent-purple); font-size: 0.72rem;">COMPLETED (15.0s)</span>
            </div>
          </div>
        </div>
      `,
      'tokens': `
        <div class="tokens-grid">
          <div class="token-card">
            <div class="token-title">Color Palette Tokens</div>
            <div class="color-swatch-row">
              <div class="swatch-box" style="background: #090B0E;"></div>
              <span><strong>--bg-canvas:</strong> #090B0E</span>
            </div>
            <div class="color-swatch-row">
              <div class="swatch-box" style="background: #161A22;"></div>
              <span><strong>--bg-elevated:</strong> #161A22</span>
            </div>
            <div class="color-swatch-row">
              <div class="swatch-box" style="background: #86BC25;"></div>
              <span><strong>--deloitte-green:</strong> #86BC25</span>
            </div>
            <div class="color-swatch-row">
              <div class="swatch-box" style="background: #00E5FF;"></div>
              <span><strong>--accent-cyan:</strong> #00E5FF</span>
            </div>
          </div>

          <div class="token-card">
            <div class="token-title">Typography & Grid</div>
            <div style="font-size: 0.8rem; color: var(--text-secondary); line-height: 1.8;">
              <div><strong>Display:</strong> Inter 800 (-0.035em tracking)</div>
              <div><strong>Body:</strong> Inter 400 (15px / 1.6 line-height)</div>
              <div><strong>Mono:</strong> JetBrains Mono (Code/Metrics)</div>
              <div><strong>Layout Rhythm:</strong> Strict 8px Multiples</div>
            </div>
          </div>

          <div class="token-card">
            <div class="token-title">Tactile Button States</div>
            <div class="interactive-btn-previewer">
              <button class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 0.78rem;">Active State Preview</button>
              <button class="btn btn-matte" style="width: 100%; justify-content: center; font-size: 0.78rem;">Surface Inset State</button>
              <button class="btn btn-emerald" style="width: 100%; justify-content: center; font-size: 0.78rem;">Feedback Pulse State</button>
            </div>
          </div>
        </div>
      `,
      'vfx-stream': `
        <table class="vfx-table">
          <thead>
            <tr>
              <th>Shot Identifier</th>
              <th>Task Scope</th>
              <th>Capture Standard</th>
              <th>Tracking Error</th>
              <th>Quality Gate</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="font-mono" style="color: var(--text-pure); font-weight: 600;">TAK_VFX_0150</td>
              <td>Wire Removal & Live Plate Clean</td>
              <td>Arri Alexa Mini LF 4.5K</td>
              <td class="font-mono">0.31 px</td>
              <td><span class="status-badge pass">SUPERVISOR APPROVED</span></td>
            </tr>
            <tr>
              <td class="font-mono" style="color: var(--text-pure); font-weight: 600;">TAK_VFX_0210</td>
              <td>3D Camera Matchmove & Sensor Solve</td>
              <td>RED V-Raptor 8K VV</td>
              <td class="font-mono">0.34 px</td>
              <td><span class="status-badge subpixel">SUB-PIXEL LOCK</span></td>
            </tr>
            <tr>
              <td class="font-mono" style="color: var(--text-pure); font-weight: 600;">TAK_VFX_0340</td>
              <td>Unreal Engine 5 Colonnade Virtual Set</td>
              <td>ACEScg / Nanite Geometry</td>
              <td class="font-mono">0.28 px</td>
              <td><span class="status-badge pass">SUPERVISOR APPROVED</span></td>
            </tr>
            <tr>
              <td class="font-mono" style="color: var(--text-pure); font-weight: 600;">TAK_VFX_0420</td>
              <td>Subterranean Vault Shading & Fog</td>
              <td>Dynamic Lumen Volumetrics</td>
              <td class="font-mono">0.36 px</td>
              <td><span class="status-badge pass">SUPERVISOR APPROVED</span></td>
            </tr>
          </tbody>
        </table>
      `
    };

    function switchUIStage(stageKey, btn) {
      document.querySelectorAll('.ui-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('uiStageCanvas').innerHTML = stageData[stageKey];
    }

    // Initialize with Telemetry HUD
    document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('uiStageCanvas').innerHTML = stageData['telemetry'];
    });

    // Lightbox modal
    function openModal(imgSrc, title, desc) {
      document.getElementById('modalImg').src = imgSrc;
      document.getElementById('modalTitle').textContent = title;
      document.getElementById('modalDesc').textContent = desc;
      document.getElementById('imageModal').classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeModal(event) {
      document.getElementById('imageModal').classList.remove('active');
      document.body.style.overflow = '';
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });
  </script>

</body>
</html>
"""

target_path = r"E:\Antigravity\Portfolio\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"SUCCESS: Written {len(html_code)} bytes to {target_path}")
