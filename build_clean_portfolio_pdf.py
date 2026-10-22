# -*- coding: utf-8 -*-
"""
BUILD MASTER PORTFOLIO PDF (EXACT PORTFOLIO WEBSITE UI)
Renders the exact portfolio website into a pixel-perfect, recruiter-ready PDF:
- Zero chopped cards or broken page breaks (break-inside: avoid)
- Prominent interactive portfolio banner at the start linking to https://bennyjoel.github.io/portfolio/
- Video players replaced with high-res crisp posters and direct 'Watch 60fps Reel Online ↗' badges
- 100% identical styling, typography, colors, and layout as index.html
- Assembles recruiter ZIP with Benny_Joel_Lakamana_Resume.pdf
"""

import os
import re
import zipfile
import subprocess
import shutil
from pathlib import Path
import pymupdf
import pypdf

PORTFOLIO_DIR = Path(r"E:\Antigravity\Portfolio")
RESUME_DIR = Path(r"E:\Resume")
BRAIN_DIR = Path(r"C:\Users\benny\.gemini\antigravity\brain\4bbb26d0-87f5-4216-910e-08a27fbcd0d9")
AUDIT_DIR = BRAIN_DIR / "portfolio_audit_pages"

SOURCE_HTML = PORTFOLIO_DIR / "index.html"
PRINT_HTML = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio_Print.html"
OUTPUT_PDF = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio.pdf"
RESUME_PDF = RESUME_DIR / "Benny_Joel_Lakamana_Deloitte_Associate_Design.pdf"
ZIP_OUTPUT = RESUME_DIR / "Benny_Joel_Lakamana_Portfolio_Package.zip"
ZIP_MIRROR = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio_Package.zip"

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def build_print_html():
    print("Step 1: Reading original index.html...")
    content = SOURCE_HTML.read_text(encoding="utf-8")

    # 1. Inject Print Optimization CSS
    print_css = """
    /* ==========================================================================
       PRINT INTEGRITY & ACCESSIBILITY STYLES (EXACT PORTFOLIO UI)
       ========================================================================== */
    @media print {
      @page {
        size: A4 portrait;
        margin: 12mm 12mm 12mm 12mm;
      }

      body {
        background-color: #080A0E !important;
        color: #F8FAFC !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      /* Full fidelity for matte background and colors */
      * {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      /* Fix Chromium Skia text clipping rectangle bug on gradient text */
      .hero-name {
        background: none !important;
        -webkit-background-clip: initial !important;
        -webkit-text-fill-color: #FFFFFF !important;
        color: #FFFFFF !important;
        font-size: 3.4rem !important;
        margin-bottom: 12px !important;
      }

      .hero-section {
        padding: 8px 0 16px 0 !important;
        border-bottom: none !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }

      .hero-bio {
        margin-bottom: 18px !important;
      }

      .hero-actions {
        margin-bottom: 20px !important;
      }

      .portfolio-experience-banner {
        margin: 6px auto 14px auto !important;
        padding: 10px 16px !important;
      }

      /* Eliminate sticky header in print so it stays neatly at the top of page 1 */
      .site-nav {
        position: static !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
        margin-bottom: 16px !important;
        background: #0E121A !important;
      }

      /* Enforce clean page breaks at major structural sections */
      #pitch-decks {
        page-break-before: always !important;
        break-before: page !important;
      }

      #product-ui {
        page-break-before: always !important;
        break-before: page !important;
      }

      #motion {
        page-break-before: always !important;
        break-before: page !important;
      }

      #3d-sets {
        page-break-before: always !important;
        break-before: page !important;
      }

      #credentials {
        page-break-before: always !important;
        break-before: page !important;
      }

      /* Bind section headers so they never separate from content */
      .section-header {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        margin-bottom: 24px !important;
      }

      .section-eyebrow,
      .section-title,
      .section-desc {
        page-break-after: avoid !important;
        break-after: avoid !important;
      }

      /* Prevent any card, section, or grid item from being sliced across page breaks */
      .deck-card,
      .ui-case-card,
      .motion-card,
      .spatial-card,
      .dossier-card,
      .edu-card,
      .hero-stat,
      .hero-stats-grid,
      .hero-section,
      .disclosure-banner,
      .portfolio-experience-banner,
      .live-banner,
      .academic-showcase-box,
      .site-footer {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }

      /* Motion Grid Flex Layout for Zero Chromium Blank Pages */
      .motion-grid {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 20px !important;
      }

      .motion-card {
        width: calc(50% - 10px) !important;
        max-width: calc(50% - 10px) !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
        overflow: visible !important;
        margin-bottom: 16px !important;
      }

      /* Spatial Grid Flex Layout for 3D Sets */
      .spatial-grid {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 16px !important;
      }

      .spatial-card {
        width: calc(33.333% - 11px) !important;
        max-width: calc(33.333% - 11px) !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
        overflow: visible !important;
        margin-bottom: 16px !important;
      }

      .spatial-img-box {
        height: 160px !important;
        max-height: 160px !important;
      }

      /* Dossier Grid Flex Layout for Credentials */
      .dossier-grid {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 16px !important;
      }

      .dossier-card {
        width: calc(33.333% - 11px) !important;
        max-width: calc(33.333% - 11px) !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
        margin-bottom: 16px !important;
      }

      /* Academic Cards Flex Layout */
      .academic-cards-grid {
        display: flex !important;
        gap: 20px !important;
      }

      .academic-cards-grid .edu-card {
        flex: 1 !important;
        break-inside: avoid !important;
        page-break-inside: avoid !important;
      }

      /* Ensure images scale nicely and never overflow page margins */
      img {
        max-width: 100% !important;
        height: auto !important;
        page-break-inside: avoid !important;
      }

      /* Hide interactive lightbox modal from print output */
      .modal-overlay {
        display: none !important;
      }
    }

    /* EXPERIENCE BANNER STYLES */
    .portfolio-experience-banner {
      background: linear-gradient(135deg, rgba(14, 18, 26, 0.98) 0%, rgba(19, 24, 34, 0.98) 100%);
      border: 1.5px solid rgba(134, 188, 37, 0.6);
      border-radius: 12px;
      padding: 16px 20px;
      margin: 16px auto 28px auto;
      max-width: 1200px;
      box-shadow: 0 10px 30px -10px rgba(134, 188, 37, 0.25);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .banner-info {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .banner-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: #86BC25;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .banner-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #86BC25;
      box-shadow: 0 0 10px #86BC25;
    }

    .banner-title {
      font-size: 13.5px;
      font-weight: 600;
      color: #F8FAFC;
      line-height: 1.4;
    }

    .banner-link-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #86BC25;
      color: #080A0E;
      text-decoration: none;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      padding: 10px 18px;
      border-radius: 8px;
      white-space: nowrap;
      box-shadow: 0 4px 16px rgba(134, 188, 37, 0.35);
    }

    /* PRINT POSTER & VIDEO PLAY OVERLAY */
    .print-video-wrap {
      position: relative;
      width: 100%;
      height: 280px;
      background: #000;
      overflow: hidden;
      border-radius: 8px 8px 0 0;
    }

    .print-video-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
    }

    .print-video-badge {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(14, 18, 26, 0.92);
      border: 1px solid rgba(255, 255, 255, 0.25);
      backdrop-filter: blur(8px);
      padding: 6px 12px;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: #FFFFFF;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 600;
      text-decoration: none;
    }

    .print-video-badge .triangle {
      color: #86BC25;
      font-size: 10px;
    }
    """

    content = content.replace("</style>", f"{print_css}\n  </style>")

    # 2. Inject Experience Banner right after site-nav
    banner_html = """
  <!-- RECRUITER PORTFOLIO ACCESS BANNER -->
  <div class="container" style="padding-top: 6px;">
    <div class="portfolio-experience-banner">
      <div class="banner-info">
        <div class="banner-pill">
          <span class="banner-pulse"></span>
          LIVE INTERACTIVE PORTFOLIO & REEL PLAYER
        </div>
        <div class="banner-title">
          To experience the full interactive portfolio with 60fps broadcast video playback, real-time 3D viewports, and live recruiter workstations:
        </div>
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #94A3B8;">
          Live Link: <strong style="color: #86BC25; text-decoration: underline;">https://bennyjoel.github.io/portfolio/</strong>
        </div>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/" target="_blank" class="banner-link-btn">
        <span>Open Live Portfolio</span>
        <span>↗</span>
      </a>
    </div>
  </div>
"""

    if "</nav>" in content:
        content = content.replace("</nav>", "</nav>\n" + banner_html, 1)
        print("[OK] Injected Live Portfolio Experience Banner after </nav>")
    else:
        print("[WARNING] Could not find </nav> tag to inject banner!")

    # 3. Replace all <video> tags in motion-grid with crisp print posters + play badge
    # Reel 1: Apex Grand Motion System
    reel1_old = re.search(r'<div class="video-viewport">\s*<video[^>]*thumb_apex_motion\.jpg[^>]*>.*?</video>\s*</div>', content, re.DOTALL)
    if reel1_old:
        reel1_new = """<div class="print-video-wrap">
            <img src="assets/images/thumb_apex_motion.jpg" class="print-video-img" alt="Apex Grand Motion System">
            <a href="https://bennyjoel.github.io/portfolio/#motion" class="print-video-badge" target="_blank">
              <span class="triangle">▶</span>
              <span>Watch 60fps Reel Online ↗</span>
            </a>
          </div>"""
        content = content.replace(reel1_old.group(0), reel1_new)

    # Reel 2: Kinetic Typography
    reel2_old = re.search(r'<div class="video-viewport">\s*<video[^>]*thumb_kinetic_typography\.jpg[^>]*>.*?</video>\s*</div>', content, re.DOTALL)
    if reel2_old:
        reel2_new = """<div class="print-video-wrap">
            <img src="assets/images/thumb_kinetic_typography.jpg" class="print-video-img" alt="Kinetic Typography & Dynamic Editorial">
            <a href="https://bennyjoel.github.io/portfolio/#motion" class="print-video-badge" target="_blank">
              <span class="triangle">▶</span>
              <span>Watch 60fps Reel Online ↗</span>
            </a>
          </div>"""
        content = content.replace(reel2_old.group(0), reel2_new)

    # Reel 3: Titanium Metering
    reel3_old = re.search(r'<div class="video-viewport">\s*<video[^>]*thumb_titanium_metering\.jpg[^>]*>.*?</video>\s*</div>', content, re.DOTALL)
    if reel3_old:
        reel3_new = """<div class="print-video-wrap">
            <img src="assets/images/thumb_titanium_metering.jpg" class="print-video-img" alt="Titanium Performance Metering">
            <a href="https://bennyjoel.github.io/portfolio/#motion" class="print-video-badge" target="_blank">
              <span class="triangle">▶</span>
              <span>Watch 60fps Reel Online ↗</span>
            </a>
          </div>"""
        content = content.replace(reel3_old.group(0), reel3_new)

    # Reel 4: Fluid Swiss
    reel4_old = re.search(r'<div class="video-viewport">\s*<video[^>]*thumb_fluid_swiss\.jpg[^>]*>.*?</video>\s*</div>', content, re.DOTALL)
    if reel4_old:
        reel4_new = """<div class="print-video-wrap">
            <img src="assets/images/thumb_fluid_swiss.jpg" class="print-video-img" alt="Fluid Swiss Interface Motion">
            <a href="https://bennyjoel.github.io/portfolio/#motion" class="print-video-badge" target="_blank">
              <span class="triangle">▶</span>
              <span>Watch 60fps Reel Online ↗</span>
            </a>
          </div>"""
        content = content.replace(reel4_old.group(0), reel4_new)

    PRINT_HTML.write_text(content, encoding="utf-8")
    print(f"[OK] Print-ready HTML saved: {PRINT_HTML} ({PRINT_HTML.stat().st_size:,} bytes)")
    return PRINT_HTML

def compile_pdf():
    print("\nStep 2: Compiling PDF via Headless Microsoft Edge...")
    cmd_pdf = [
        EDGE_EXE,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={str(OUTPUT_PDF)}",
        str(PRINT_HTML.resolve().as_uri())
    ]
    res = subprocess.run(cmd_pdf, capture_output=True, text=True)
    if not OUTPUT_PDF.exists():
        raise RuntimeError(f"Edge failed to generate PDF! stderr: {res.stderr}")
    print(f"[OK] Master PDF generated: {OUTPUT_PDF} ({OUTPUT_PDF.stat().st_size:,} bytes)")
    return OUTPUT_PDF

def audit_pdf():
    print("\nStep 3: Auditing generated PDF with PyMuPDF...")
    # Clean previous audit images
    if AUDIT_DIR.exists():
        for f in AUDIT_DIR.glob("audit_page_*.png"):
            try:
                f.unlink()
            except Exception:
                pass
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(str(OUTPUT_PDF))
    total_pages = len(doc)
    print(f"Total Pages: {total_pages}")

    for idx, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        page_img_path = AUDIT_DIR / f"audit_page_{idx+1:02d}.png"
        pix.save(str(page_img_path))
        print(f"  [Page {idx+1:02d}/{total_pages:02d}] {pix.width}x{pix.height} -> {page_img_path.name}")
    doc.close()
    return total_pages

def build_recruiter_zip():
    print("\nStep 4: Syncing and Packaging ZIP for Recruiter...")
    if not RESUME_PDF.exists():
        raise FileNotFoundError(f"Resume PDF not found: {RESUME_PDF}")

    resume_name_in_zip = "Benny_Joel_Lakamana_Resume.pdf"
    portfolio_name_in_zip = "Benny_Joel_Lakamana_Portfolio.pdf"

    # Also sync PDF directly to Resume folder
    target_portfolio_pdf = RESUME_DIR / portfolio_name_in_zip
    shutil.copy2(OUTPUT_PDF, target_portfolio_pdf)
    print(f"[OK] Synced to: {target_portfolio_pdf}")

    # Build primary ZIP at E:\Resume\Benny_Joel_Lakamana_Portfolio_Package.zip
    with zipfile.ZipFile(ZIP_OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(RESUME_PDF, arcname=resume_name_in_zip)
        zf.write(OUTPUT_PDF, arcname=portfolio_name_in_zip)
    print(f"[OK] Created ZIP: {ZIP_OUTPUT} ({ZIP_OUTPUT.stat().st_size:,} bytes)")

    # Mirror ZIP to Portfolio directory
    shutil.copy2(ZIP_OUTPUT, ZIP_MIRROR)
    print(f"[OK] Created ZIP: {ZIP_MIRROR} ({ZIP_MIRROR.stat().st_size:,} bytes)")

    # Copy to Desktop for immediate access
    desktop_dirs = [
        Path(r"C:\Users\benny\Desktop"),
        Path(r"C:\Users\benny\OneDrive\Desktop"),
    ]
    for desk in desktop_dirs:
        if desk.exists():
            desk_zip = desk / "Benny_Joel_Lakamana_Portfolio_Package.zip"
            shutil.copy2(ZIP_OUTPUT, desk_zip)
            print(f"[OK] Copied ZIP to Desktop: {desk_zip}")

    # Also copy to assets/docs in Portfolio directory for web hosting
    docs_dir = PORTFOLIO_DIR / "assets" / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUTPUT_PDF, docs_dir / portfolio_name_in_zip)
    shutil.copy2(ZIP_OUTPUT, docs_dir / "Benny_Joel_Lakamana_Portfolio_Package.zip")
    print(f"[OK] Synced to web assets: {portfolio_name_in_zip}, Benny_Joel_Lakamana_Portfolio_Package.zip")

if __name__ == "__main__":
    build_print_html()
    compile_pdf()
    audit_pdf()
    build_recruiter_zip()
    print("\n=== SUCCESS: MASTER PORTFOLIO PDF & RECRUITER ZIP ASSEMBLED ===")
