# -*- coding: utf-8 -*-
"""
BUILD MASTER PORTFOLIO PDF MONOGRAPH & RECRUITER ZIP PACKAGE
Compiles a luxury 7-page A4 landscape portfolio dossier for Benny Joel Lakamana:
- Page 1: Cover & Executive Overview
- Page 2: Unreal Engine 5 Spatial Previs (Feature Trilogy)
- Page 3: Epic Scale, Atmospherics & Theatrical Matchmove
- Page 4: Broadcast Motion Graphics & Kinetic Typography
- Page 5: Product Design & Interactive Systems Architecture
- Page 6: Executive Pitch Decks & Production Dossiers
- Page 7: Academic Rigor, Production Toolkit & Direct Access
"""

import os
import zipfile
import subprocess
import shutil
from pathlib import Path
import pymupdf
import pypdf

PORTFOLIO_DIR = Path(r"E:\Antigravity\Portfolio")
RESUME_DIR = Path(r"E:\Resume")
BRAIN_DIR = Path(r"C:\Users\benny\.gemini\antigravity\brain\4bbb26d0-87f5-4216-910e-08a27fbcd0d9")

HTML_PATH = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio.html"
PDF_PATH = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio.pdf"
RESUME_PDF_PATH = RESUME_DIR / "Benny_Joel_Lakamana_Deloitte_Associate_Design.pdf"
ZIP_RESUME_PATH = RESUME_DIR / "Benny_Joel_Lakamana_Portfolio_Package.zip"
ZIP_PORTFOLIO_PATH = PORTFOLIO_DIR / "Benny_Joel_Lakamana_Portfolio_Package.zip"

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Benny Joel Lakamana — Master Portfolio & Production Dossier</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

  @page {
    size: 297mm 210mm;
    margin: 0;
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    background-color: #07090E;
    color: #F8FAFC;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    overflow-x: hidden;
  }

  /* PAGE CONTAINER */
  .page {
    width: 297mm;
    height: 210mm;
    max-height: 210mm;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    position: relative;
    padding: 12mm 16mm 10mm 16mm;
    background: #07090E radial-gradient(circle at 80% 10%, rgba(59, 130, 246, 0.08) 0%, transparent 60%);
    display: flex;
    flex-direction: column;
    justifyContent: space-between;
  }

  /* TOP HEADER (Pages 2-7) */
  .page-header {
    display: flex;
    justifyContent: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 3mm;
    margin-bottom: 4mm;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .header-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    font-weight: 700;
    color: #3B82F6;
    letter-spacing: 0.15em;
    background: rgba(59, 130, 246, 0.12);
    padding: 3px 8px;
    border-radius: 4px;
    border: 1px solid rgba(59, 130, 246, 0.3);
  }

  .header-name {
    font-size: 9pt;
    font-weight: 600;
    color: #94A3B8;
    letter-spacing: 0.05em;
  }

  .header-link-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    font-weight: 600;
    color: #E2E8F0;
    text-decoration: none;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 4px 12px;
    border-radius: 20px;
    transition: all 0.2s;
  }

  .pulse-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10B981;
    box-shadow: 0 0 8px #10B981;
  }

  /* SECTION TITLE BLOCK */
  .section-intro {
    margin-bottom: 3.5mm;
  }

  .section-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 700;
    color: #3B82F6;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 2px;
  }

  .section-title {
    font-size: 15pt;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #FFFFFF;
    line-height: 1.15;
  }

  .section-desc {
    font-size: 8.5pt;
    color: #94A3B8;
    margin-top: 2px;
    line-height: 1.35;
  }

  /* FOOTER */
  .page-footer {
    display: flex;
    justifyContent: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    padding-top: 2.5mm;
    margin-top: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: #64748B;
  }

  .footer-link {
    color: #94A3B8;
    text-decoration: none;
    font-weight: 600;
  }

  .footer-link:hover {
    color: #3B82F6;
  }

  /* CARDS & GRIDS */
  .grid-3col {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4mm;
    flex: 1;
  }

  .grid-2x2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 3.5mm;
    flex: 1;
  }

  .card {
    background: rgba(18, 22, 31, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  }

  .card-img-wrap {
    width: 100%;
    position: relative;
    overflow: hidden;
    background: #0B0E17;
  }

  .card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .card-badge {
    position: absolute;
    top: 8px;
    left: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.5pt;
    font-weight: 700;
    color: #FFFFFF;
    background: rgba(0, 0, 0, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(8px);
    padding: 3px 8px;
    border-radius: 4px;
    letter-spacing: 0.05em;
  }

  .card-body {
    padding: 3.5mm 4mm;
    display: flex;
    flex-direction: column;
    justifyContent: space-between;
    flex: 1;
  }

  .card-title {
    font-size: 10pt;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: -0.02em;
    margin-bottom: 2px;
  }

  .card-desc {
    font-size: 7.5pt;
    color: #94A3B8;
    line-height: 1.35;
    margin-bottom: 3mm;
  }

  .card-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: auto;
  }

  .card-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.5pt;
    font-weight: 600;
    color: #CBD5E1;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 2px 6px;
    border-radius: 3px;
  }

  .card-pill.highlight {
    color: #60A5FA;
    background: rgba(59, 130, 246, 0.1);
    border-color: rgba(59, 130, 246, 0.3);
  }

  /* ============================================================== */
  /* PAGE 1: COVER LAYOUT */
  /* ============================================================== */
  .cover-layout {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 8mm;
    flex: 1;
    align-items: center;
    margin-top: 2mm;
    margin-bottom: 2mm;
  }

  .cover-left {
    display: flex;
    flex-direction: column;
    gap: 4mm;
  }

  .eyebrow-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59, 130, 246, 0.1);
    border: 1px solid rgba(59, 130, 246, 0.3);
    padding: 4px 12px;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    font-weight: 700;
    color: #60A5FA;
    letter-spacing: 0.15em;
    width: fit-content;
  }

  .cover-name {
    font-size: 28pt;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.04em;
    line-height: 1.05;
  }

  .cover-role {
    font-size: 13pt;
    font-weight: 600;
    color: #CBD5E1;
    letter-spacing: -0.02em;
    line-height: 1.3;
  }

  .cover-contacts {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    color: #94A3B8;
  }

  .cover-cta-box {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid rgba(59, 130, 246, 0.4);
    border-radius: 10px;
    padding: 4.5mm 5mm;
    box-shadow: 0 10px 30px -10px rgba(59, 130, 246, 0.2);
  }

  .cover-cta-title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 2mm;
  }

  .cover-cta-desc {
    font-size: 8pt;
    color: #94A3B8;
    line-height: 1.4;
    margin-bottom: 3.5mm;
  }

  .cover-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #3B82F6;
    color: #FFFFFF;
    text-decoration: none;
    font-weight: 700;
    font-size: 8.5pt;
    padding: 6px 16px;
    border-radius: 6px;
    box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
  }

  .cover-right {
    display: flex;
    flex-direction: column;
    gap: 4mm;
  }

  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3mm;
  }

  .kpi-card {
    background: rgba(18, 22, 31, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 3.5mm 4mm;
  }

  .kpi-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16pt;
    font-weight: 800;
    color: #38BDF8;
    line-height: 1.1;
  }

  .kpi-label {
    font-size: 8pt;
    font-weight: 700;
    color: #FFFFFF;
    margin-top: 1px;
    letter-spacing: -0.01em;
  }

  .kpi-sub {
    font-size: 7pt;
    color: #64748B;
    margin-top: 2px;
    line-height: 1.3;
  }

  .cover-hero-img-wrap {
    width: 100%;
    height: 48mm;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.12);
  }

  /* ============================================================== */
  /* PAGE 5: UI ARCHITECTURE SPLIT */
  /* ============================================================== */
  .ui-layout {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 5mm;
    flex: 1;
  }

  .ui-preview-col {
    display: flex;
    flex-direction: column;
    gap: 3.5mm;
  }

  .ui-spec-col {
    display: flex;
    flex-direction: column;
    justifyContent: space-between;
    background: rgba(18, 22, 31, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 4mm 5mm;
  }

  /* ============================================================== */
  /* PAGE 6: DECK TRILOGY */
  /* ============================================================== */
  .deck-featured {
    background: rgba(18, 22, 31, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 3.5mm;
    margin-bottom: 3.5mm;
  }

  .deck-thumbs-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 3mm;
    margin-top: 2.5mm;
  }

  .deck-2col {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 4mm;
    flex: 1;
  }

  /* ============================================================== */
  /* PAGE 7: CREDENTIALS & TOOLKIT */
  /* ============================================================== */
  .creds-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6mm;
    flex: 1;
  }

  .edu-box {
    background: rgba(18, 22, 31, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 4mm 5mm;
    margin-bottom: 3mm;
  }

  .toolkit-group {
    margin-bottom: 3mm;
  }

  .toolkit-heading {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 700;
    color: #38BDF8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 2mm;
  }
</style>
</head>
<body>

  <!-- =================================================================== -->
  <!-- PAGE 1: COVER & EXECUTIVE OVERVIEW -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header" style="border: none; margin-bottom: 0;">
      <div class="header-left">
        <span class="header-tag">PRODUCTION DOSSIER</span>
        <span class="header-name">BENNY JOEL LAKAMANA // VISUAL & ASSOCIATE DESIGNER</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio
      </a>
    </div>

    <div class="cover-layout">
      <div class="cover-left">
        <div class="eyebrow-badge">4-YEAR BFA DEGREE • REAL-TIME 3D PREVIS • 140+ VFX SHOTS</div>
        <h1 class="cover-name">Benny Joel<br>Lakamana</h1>
        <div class="cover-role">Visual & Associate Designer • 3D Generalist<br>Broadcast Motion Graphics Specialist</div>
        
        <div class="cover-contacts">
          <span>📍 Hyderabad, India</span>
          <span>✉ bennyofficial19@gmail.com</span>
          <span>📞 +91 79951 86695</span>
        </div>

        <div class="cover-cta-box">
          <div class="cover-cta-title">
            <svg width="18" height="18" fill="none" stroke="#38BDF8" stroke-width="2" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Interactive Web Portfolio & Reel Player
          </div>
          <p class="cover-cta-desc">
            Experience all 60fps broadcast video masters, interactive UI architecture sandboxes, zoomable 3D viewport plates, and production pitch decks on the live deployment.
          </p>
          <a href="https://bennyjoel.github.io/portfolio/" class="cover-btn">
            Open Interactive Web Portfolio →
          </a>
        </div>
      </div>

      <div class="cover-right">
        <div class="kpi-grid">
          <div class="kpi-card">
            <div class="kpi-num">140+</div>
            <div class="kpi-label">Feature Film VFX Shots</div>
            <div class="kpi-sub">Takshaka, on-set Macbeth charts, 3D matchmoving & plate reconstruction.</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-num">Real-Time</div>
            <div class="kpi-label">Unreal Engine 5 Previs</div>
            <div class="kpi-sub">Lumen GI, Nanite virtual geometry, RVT landscape blending, ACEScg.</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-num">60 FPS</div>
            <div class="kpi-label">Broadcast Motion Design</div>
            <div class="kpi-sub">Antigravity Agentic Code, clean-room EffectCraft engine, After Effects.</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-num">4-Year BFA</div>
            <div class="kpi-label">Animation & VFX Degree</div>
            <div class="kpi-sub">JNAFAU studio rigor + Arena Animation VFX Prime 3-year course.</div>
          </div>
        </div>

        <div class="cover-hero-img-wrap">
          <img src="assets/images/env_instagram_river_gorge.jpg" class="card-img" alt="Unreal Engine 5 Showcase">
          <div class="card-badge">FEATURED: UNREAL ENGINE 5.5 LUMEN & NANITE PREVIS</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • MASTER PORTFOLIO & PRODUCTION DOSSIER</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/" class="footer-link">https://bennyjoel.github.io/portfolio/</a></span>
      <span class="footer-right">PAGE 01 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 2: 3D SPATIAL PREVIS & REAL-TIME ENVIRONMENTS -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">01 // 3D SPATIAL PREVIS</span>
        <span class="header-name">UNREAL ENGINE 5.5 REAL-TIME PRODUCTION ENVIRONMENTS</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/#environments" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio/#environments
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 01 // PRODUCTION 3D ENVIRONMENTS</div>
      <h2 class="section-title">Photoreal Cinematic Lighting, Volumetrics & Nanite Geometry</h2>
      <p class="section-desc">Real-time virtual set extensions, procedural river gorge topologies, and physical exposure calibration engineered in Unreal Engine 5.5.</p>
    </div>

    <div class="grid-3col">
      <!-- Card 1 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 68mm;">
          <img src="assets/images/env_instagram_river_gorge.jpg" class="card-img" alt="Mountain River Gorge">
          <div class="card-badge">INSTAGRAM FEATURED</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Mountain River Gorge</h3>
          <p class="card-desc">
            High-fidelity Lumen real-time riverbed with Nanite rocky cliff faces, atmospheric mist, and contact normal blending via Runtime Virtual Textures (RVT).
          </p>
          <div class="card-pills">
            <span class="card-pill highlight">Unreal Engine 5.5</span>
            <span class="card-pill">Lumen GI</span>
            <span class="card-pill">Nanite</span>
            <span class="card-pill">RVT Blending</span>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 68mm;">
          <img src="assets/images/env_night_sanctuary_moonlight.jpg" class="card-img" alt="Ancient Sanctuary">
          <div class="card-badge">NIGHT VOLUMETRICS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Ancient Sanctuary Moonlight</h3>
          <p class="card-desc">
            Sub-surface stone lookdev, cold moonlight key with warm interior secondary bounce, volumetric dust shafts, and high-dynamic-range night lighting.
          </p>
          <div class="card-pills">
            <span class="card-pill highlight">Lumen Reflections</span>
            <span class="card-pill">Substrate PBR</span>
            <span class="card-pill">Volumetric Fog</span>
            <span class="card-pill">Night Previs</span>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 68mm;">
          <img src="assets/images/env_day_colonnade_vista.jpg" class="card-img" alt="Grand Temple Colonnade">
          <div class="card-badge">DAYLIGHT PHYSICAL SKY</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Grand Temple Colonnade</h3>
          <p class="card-desc">
            Physical sun simulation, high-contrast daylight exposure, historical architectural symmetry, and camera focal length staging for cinematic framing.
          </p>
          <div class="card-pills">
            <span class="card-pill highlight">Physical Sky</span>
            <span class="card-pill">Exposure Calibration</span>
            <span class="card-pill">Nanite Meshes</span>
            <span class="card-pill">Camera Staging</span>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • UNREAL ENGINE 5.5 PREVIS ENVIRONMENTS</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/#environments" class="footer-link">Explore High-Res Plates: bennyjoel.github.io/portfolio/#environments</a></span>
      <span class="footer-right">PAGE 02 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 3: SCALE, VOLUMETRICS & THEATRICAL MATCHMOVE -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">02 // SCALE & MATCHMOVE</span>
        <span class="header-name">WORLD PARTITION, ARCHITECTURAL ATMOSPHERICS & PLATE TRACKING</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/#environments" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio/#environments
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 02 // SCALE, VOLUMETRICS & CAMERA LOG TRACKING</div>
      <h2 class="section-title">Large-Scale World Partition & Sub-Pixel Syntheyes Matchmoving</h2>
      <p class="section-desc">From subterranean vaulted cathedrals to multi-kilometer exterior sets and sub-0.5px camera matchmove solves for live-action plates.</p>
    </div>

    <div class="grid-2x2">
      <!-- Card 1 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 40mm;">
          <img src="assets/images/env_night_cathedral_ruins.jpg" class="card-img" alt="Cathedral Ruins">
          <div class="card-badge">INTERIOR ATMOSPHERICS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Subterranean Cathedral Vault</h3>
          <p class="card-desc">Gothic vaulted stone geometry with dense volumetric god-rays piercing clerestory apertures, wet floor specular reflections, and Lumen bounce.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Volumetric God-Rays</span>
            <span class="card-pill">Gothic Architecture</span>
            <span class="card-pill">Lumen Bounce</span>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 40mm;">
          <img src="assets/images/env_dawn_atmospheric_courtyard.jpg" class="card-img" alt="Dawn Courtyard">
          <div class="card-badge">GOLDEN HOUR HORIZON</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Dawn Courtyard Golden Hour</h3>
          <p class="card-desc">Horizon solar bloom with morning dew surface roughness lookdev, organic crawling ivy foliage, and delicate ambient light ratios.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Golden Hour Bloom</span>
            <span class="card-pill">Procedural Ivy</span>
            <span class="card-pill">Roughness LookDev</span>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 40mm;">
          <img src="assets/images/env_worldbreaker_cinematic.jpg" class="card-img" alt="Worldbreaker Level">
          <div class="card-badge">WORLD PARTITION EXTENSION</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Worldbreaker Level Previs</h3>
          <p class="card-desc">Multi-kilometer World Partition blockout, dynamic cloud shadow projection, atmospheric depth haze, and cinematic focal hierarchy.</p>
          <div class="card-pills">
            <span class="card-pill highlight">World Partition</span>
            <span class="card-pill">Multi-Kilometer Previs</span>
            <span class="card-pill">Cloud Shadows</span>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 40mm;">
          <img src="assets/images/test_syntheyes_track.png" class="card-img" alt="Syntheyes Matchmove">
          <div class="card-badge">THEATRICAL MATCHMOVE</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Syntheyes 3D Camera Matchmove (&lt;0.5px)</h3>
          <p class="card-desc">Sub-pixel feature tracking on Arri/RED raw plates, lens distortion calibration, ground plane alignment, and camera solve into Maya & Unreal Engine.</p>
          <div class="card-pills">
            <span class="card-pill highlight">&lt;0.5px Residual</span>
            <span class="card-pill">Syntheyes 3D</span>
            <span class="card-pill">Lens Calibration</span>
            <span class="card-pill">Maya/UE5 Solve</span>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • SCALE & PRODUCTION RIGOR</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/#environments" class="footer-link">Interactive 3D Grid: bennyjoel.github.io/portfolio/#environments</a></span>
      <span class="footer-right">PAGE 03 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 4: BROADCAST MOTION GRAPHICS & KINETIC TYPOGRAPHY -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">03 // MOTION GRAPHICS</span>
        <span class="header-name">BROADCAST 60FPS KINETIC TYPOGRAPHY & LUXURY DARK UI</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/#motion" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio/#motion
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 03 // 60FPS BROADCAST MOTION GRAPHICS</div>
      <h2 class="section-title">Code-Driven Layout Graphs, EffectCraft Engine & After Effects</h2>
      <p class="section-desc">Engineered using Google Antigravity and clean-room creative engines (EffectCraft) alongside Adobe After Effects for automated broadcast-grade video.</p>
    </div>

    <div class="grid-2x2">
      <!-- Card 1 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 38mm;">
          <img src="assets/images/thumb_apex_motion.jpg" class="card-img" alt="Apex Grand Motion">
          <div class="card-badge">MASTER REEL 01 • 1080x1920 60FPS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Apex Grand Motion System</h3>
          <p class="card-desc">High-contrast luxury dark UI motion with expanding radial rings, fluid typographic reveals, and clean single-voice neural voiceover mastering.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Clean Broadcast Mix</span>
            <span class="card-pill">EffectCraft Engine</span>
            <span class="card-pill">1080x1920 60fps</span>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 38mm;">
          <img src="assets/images/thumb_kinetic_typography.jpg" class="card-img" alt="Kinetic Typography">
          <div class="card-badge">MASTER REEL 02 • 1080x1920 60FPS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Kinetic Typography & Editorial</h3>
          <p class="card-desc">High-velocity typographic spring transitions, Swiss-editorial layout grids, dynamic kerning, and synchronized multi-track audio foley.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Spring Dampening</span>
            <span class="card-pill">Swiss Grid</span>
            <span class="card-pill">Foley Design</span>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 38mm;">
          <img src="assets/images/thumb_titanium_metering.jpg" class="card-img" alt="Titanium Metering">
          <div class="card-badge">MASTER REEL 03 • 1080x1920 60FPS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Titanium Performance Metering</h3>
          <p class="card-desc">Real-time speedometer counters, floating glass telemetry panels, and sub-millisecond latency benchmarks with crisp hardware renders.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Telemetry Counters</span>
            <span class="card-pill">Glass Morphism</span>
            <span class="card-pill">Latency Meters</span>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="card">
        <div class="card-img-wrap" style="height: 38mm;">
          <img src="assets/images/thumb_fluid_swiss.jpg" class="card-img" alt="Fluid Swiss Motion">
          <div class="card-badge">MASTER REEL 04 • 1080x1920 60FPS</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">Fluid Swiss Interface Motion</h3>
          <p class="card-desc">Minimalist monochrome luxury design tokens, subtle ambient glow, high-frequency spring dampening, and elegant editorial pacing.</p>
          <div class="card-pills">
            <span class="card-pill highlight">Monochrome Design</span>
            <span class="card-pill">Ambient Glow</span>
            <span class="card-pill">Editorial Timing</span>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • BROADCAST MOTION GRAPHICS</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/#motion" class="footer-link">Watch All Video Reels: bennyjoel.github.io/portfolio/#motion</a></span>
      <span class="footer-right">PAGE 04 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 5: PRODUCT DESIGN & INTERACTIVE ARCHITECTURE -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">04 // PRODUCT DESIGN</span>
        <span class="header-name">DOMINATOR SYSTEMS ENTERPRISE GATEWAY & INTERACTIVE SANDBOX</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/#ui-sandbox" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio/#ui-sandbox
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 04 // PRODUCT DESIGN & UI WORKSTATION ARCHITECTURE</div>
      <h2 class="section-title">Design System Tokens, WCAG AAA Compliance & Recruiter Sandbox</h2>
      <p class="section-desc">Interactive product architecture engineered with strict accessibility, high-contrast dark luxury tokens, and live simulated telemetry.</p>
    </div>

    <div class="ui-layout">
      <div class="ui-preview-col">
        <div class="card" style="flex: 1;">
          <div class="card-img-wrap" style="height: 48mm;">
            <img src="assets/images/ui_dominator_desktop.png" class="card-img" alt="Dominator Systems Desktop">
            <div class="card-badge">DESKTOP SYSTEM INTERFACE</div>
          </div>
          <div class="card-body" style="padding: 2.5mm 3.5mm;">
            <h3 class="card-title">Dominator Systems Enterprise Gateway</h3>
            <p class="card-desc">High-density administrative workstation with interactive tab switching, live telemetry HUD, and real-time bash terminal benchmark simulation.</p>
          </div>
        </div>

        <div class="card" style="flex: 1;">
          <div class="card-img-wrap" style="height: 40mm;">
            <img src="assets/images/ui_enterprise_dashboard.png" class="card-img" alt="Enterprise Dashboard">
            <div class="card-badge">TELEMETRY CONSOLE</div>
          </div>
          <div class="card-body" style="padding: 2.5mm 3.5mm;">
            <h3 class="card-title">Real-Time Telemetry & Token Metrics</h3>
            <p class="card-desc">Multi-agent system monitoring console tracking sub-millisecond execution times, zero-trust token authentication, and cluster status.</p>
          </div>
        </div>
      </div>

      <div class="ui-spec-col">
        <div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 8pt; font-weight: 700; color: #38BDF8; margin-bottom: 2mm;">
            DESIGN SYSTEM & ACCESSIBILITY SPECIFICATIONS
          </div>

          <div style="margin-bottom: 3.5mm;">
            <h4 style="font-size: 9pt; color: #FFFFFF; font-weight: 700; margin-bottom: 1mm;">WCAG AAA Dark Luxury Tokens</h4>
            <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35;">
              Engineered with 14:1 contrast ratios on obsidian backgrounds (<code style="color:#60A5FA;">#07090E</code> and <code style="color:#60A5FA;">#0B0E17</code>), eliminating recruiter eye fatigue during prolonged reviews.
            </p>
          </div>

          <div style="margin-bottom: 3.5mm;">
            <h4 style="font-size: 9pt; color: #FFFFFF; font-weight: 700; margin-bottom: 1mm;">Interactive 3-Stage Workstation</h4>
            <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35;">
              The live website includes an interactive sandbox allowing recruiters to toggle between Live Telemetry HUD, Design System Tokens, and VFX Ingest pipelines with real DOM state transitions.
            </p>
          </div>

          <div style="margin-bottom: 3.5mm;">
            <h4 style="font-size: 9pt; color: #FFFFFF; font-weight: 700; margin-bottom: 1mm;">Technical Implementation Stack</h4>
            <div class="card-pills" style="margin-top: 1.5mm;">
              <span class="card-pill highlight">Next.js 15</span>
              <span class="card-pill highlight">Tailwind CSS</span>
              <span class="card-pill">TypeScript</span>
              <span class="card-pill">FastAPI Microservices</span>
              <span class="card-pill">Figma Tokens</span>
            </div>
          </div>
        </div>

        <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 6px; padding: 3mm; margin-top: auto;">
          <div style="font-size: 7.5pt; font-weight: 700; color: #FFFFFF; margin-bottom: 1mm;">Test The Live Recruiter Sandbox</div>
          <p style="font-size: 7pt; color: #94A3B8; line-height: 1.3; margin-bottom: 2mm;">
            Interact with live buttons, switch tabs, and run terminal simulations directly in your browser.
          </p>
          <a href="https://bennyjoel.github.io/portfolio/#ui-sandbox" class="cover-btn" style="padding: 4px 10px; font-size: 7.5pt;">
            Open Live Sandbox →
          </a>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • PRODUCT DESIGN & UI WORKSTATION</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/#ui-sandbox" class="footer-link">Interactive Sandbox: bennyjoel.github.io/portfolio/#ui-sandbox</a></span>
      <span class="footer-right">PAGE 05 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 6: EXECUTIVE PITCH DECKS & PRODUCTION DOSSIERS -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">05 // PITCH DECKS</span>
        <span class="header-name">FEATURE FILM DEFENSE DECKS & VISUAL STORYTELLING</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/#decks" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio/#decks
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 05 // EXECUTIVE PITCH DECKS & PRODUCTION SLATES</div>
      <h2 class="section-title">Theatrical Defense Presentations & Multi-Platform Commercial Decks</h2>
      <p class="section-desc">Extensive pitch decks detailing matchmove camera residual logs, virtual set extension pipelines, and lighting lookdev bibles.</p>
    </div>

    <div style="display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
      <!-- Deck 1 Featured -->
      <div class="deck-featured">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5mm;">
          <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 7pt; font-weight: 700; color: #38BDF8; letter-spacing: 0.1em;">FEATURE FILM PRODUCTION • 14 SLIDES</span>
            <h3 style="font-size: 11pt; font-weight: 700; color: #FFFFFF; margin-top: 1px;">Takshaka Feature Film Technical Defense Deck</h3>
          </div>
          <span style="font-family: 'JetBrains Mono', monospace; font-size: 7pt; color: #94A3B8;">Arri Alexa Raw • Syntheyes • Maya • UE5</span>
        </div>
        <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35;">
          Technical presentation deck defending matchmove precision, plate reconstruction, optical lens calibration, and Unreal Engine 5 virtual set extension across 140+ theatrical shots.
        </p>
        <div class="deck-thumbs-strip">
          <img src="assets/images/slide_01_cover.png" style="width: 100%; height: 32mm; object-fit: cover; border-radius: 4px; border: 1px solid rgba(255,255,255,0.1);" alt="Takshaka Slide 1">
          <img src="assets/images/slide_04_3d_matchmove.png" style="width: 100%; height: 32mm; object-fit: cover; border-radius: 4px; border: 1px solid rgba(255,255,255,0.1);" alt="Takshaka Slide 4">
          <img src="assets/images/slide_05_level_design.png" style="width: 100%; height: 32mm; object-fit: cover; border-radius: 4px; border: 1px solid rgba(255,255,255,0.1);" alt="Takshaka Slide 5">
        </div>
      </div>

      <!-- Deck 2 & 3 Split -->
      <div class="deck-2col">
        <!-- Crucible -->
        <div class="card" style="padding: 3mm;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5mm;">
            <h4 style="font-size: 9.5pt; font-weight: 700; color: #FFFFFF;">Crucible 3D Short Film Pitch Deck</h4>
            <span class="card-pill">20 Slides</span>
          </div>
          <p style="font-size: 7pt; color: #94A3B8; line-height: 1.3; margin-bottom: 2mm;">
            Comprehensive visual development deck covering worldbuilding, moodboards, character lookdev, lighting bible, and Unreal Engine 5 timeline.
          </p>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2mm;">
            <img src="assets/images/crucible_slide_01.png" style="width: 100%; height: 20mm; object-fit: cover; border-radius: 4px;" alt="Crucible 1">
            <img src="assets/images/crucible_slide_05.png" style="width: 100%; height: 20mm; object-fit: cover; border-radius: 4px;" alt="Crucible 5">
            <img src="assets/images/crucible_slide_15.png" style="width: 100%; height: 20mm; object-fit: cover; border-radius: 4px;" alt="Crucible 15">
          </div>
        </div>

        <!-- Aarav -->
        <div class="card" style="padding: 3mm;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5mm;">
            <h4 style="font-size: 9.5pt; font-weight: 700; color: #FFFFFF;">Aarav Commercial Production Deck</h4>
            <span class="card-pill">Campaign</span>
          </div>
          <p style="font-size: 7pt; color: #94A3B8; line-height: 1.3; margin-bottom: 2mm;">
            Multi-platform commercial campaign deck outlining framing guides, color treatment, aspect ratio variations (16:9, 9:16, 1:1), and delivery specs.
          </p>
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2mm;">
            <img src="assets/images/aarav_slide_01.png" style="width: 100%; height: 20mm; object-fit: cover; border-radius: 4px;" alt="Aarav 1">
            <img src="assets/images/aarav_slide_02.png" style="width: 100%; height: 20mm; object-fit: cover; border-radius: 4px;" alt="Aarav 2">
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • PITCH DECKS & PRESENTATION SYSTEMS</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/#decks" class="footer-link">Inspect All Decks: bennyjoel.github.io/portfolio/#decks</a></span>
      <span class="footer-right">PAGE 06 / 07</span>
    </div>
  </div>

  <!-- =================================================================== -->
  <!-- PAGE 7: CREDENTIALS, TOOLKIT & DIRECT ACCESS -->
  <!-- =================================================================== -->
  <div class="page">
    <div class="page-header">
      <div class="header-left">
        <span class="header-tag">06 // CREDENTIALS</span>
        <span class="header-name">ACADEMIC RIGOR, PRODUCTION TOOLKIT & VERIFICATION</span>
      </div>
      <a href="https://bennyjoel.github.io/portfolio/" class="header-link-pill">
        <div class="pulse-dot"></div>
        bennyjoel.github.io/portfolio
      </a>
    </div>

    <div class="section-intro">
      <div class="section-num">SECTION 06 // ACADEMIC QUALIFICATIONS & PRODUCTION TOOLKIT</div>
      <h2 class="section-title">Studio Rigor, Enterprise Toolkit & Direct Portfolio Access</h2>
      <p class="section-desc">Formal university fine arts education combined with rigorous 3D studio training and modern code-driven creative pipelines.</p>
    </div>

    <div class="creds-layout">
      <!-- Left Column: Education -->
      <div>
        <div class="edu-box">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5mm;">
            <span class="card-pill highlight" style="font-size: 7pt;">4-YEAR UNIVERSITY DEGREE</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #64748B;">Hyderabad, India</span>
          </div>
          <h3 style="font-size: 11pt; font-weight: 700; color: #FFFFFF; margin-bottom: 1mm;">
            Bachelor of Fine Arts (BFA) in Animation and VFX
          </h3>
          <div style="font-size: 8pt; font-weight: 600; color: #38BDF8; margin-bottom: 2mm;">
            JNAFAU (Jawaharlal Nehru Architecture & Fine Arts University)
          </div>
          <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35; margin-bottom: 2.5mm;">
            Four years of full-time academic studio rigor covering classical human anatomy, 3D CGI modeling, spatial cinematography, lighting physics, and narrative previsualization.
          </p>
          <div class="card-pills">
            <span class="card-pill">Classical Anatomy</span>
            <span class="card-pill">3D Modeling</span>
            <span class="card-pill">Cinematography Theory</span>
            <span class="card-pill">Previs Sequences</span>
          </div>
        </div>

        <div class="edu-box">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5mm;">
            <span class="card-pill highlight" style="font-size: 7pt;">3-YEAR INTENSIVE COURSE</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #64748B;">Hyderabad, India</span>
          </div>
          <h3 style="font-size: 11pt; font-weight: 700; color: #FFFFFF; margin-bottom: 1mm;">
            Animation VFX Prime
          </h3>
          <div style="font-size: 8pt; font-weight: 600; color: #38BDF8; margin-bottom: 2mm;">
            Arena Animation
          </div>
          <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35; margin-bottom: 2.5mm;">
            Three years of comprehensive hands-on studio training in end-to-end 3D production pipelines, dynamic character rigging, lighting integration, and digital multi-pass compositing.
          </p>
          <div class="card-pills">
            <span class="card-pill">3D Pipeline Production</span>
            <span class="card-pill">Lighting & Shading</span>
            <span class="card-pill">Digital Compositing</span>
            <span class="card-pill">VFX LookDev</span>
          </div>
        </div>
      </div>

      <!-- Right Column: Toolkit & Action -->
      <div style="display: flex; flex-direction: column; justify-content: space-between;">
        <div style="background: rgba(18, 22, 31, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 4mm 5mm;">
          <div class="toolkit-group">
            <div class="toolkit-heading">Real-Time & 3D Spatial Previs</div>
            <div class="card-pills">
              <span class="card-pill highlight">Unreal Engine 5.5</span>
              <span class="card-pill">Lumen GI</span>
              <span class="card-pill">Nanite</span>
              <span class="card-pill">World Partition</span>
              <span class="card-pill">Sequencer</span>
              <span class="card-pill">Autodesk Maya</span>
              <span class="card-pill">Houdini VEX</span>
              <span class="card-pill">Syntheyes 3D</span>
            </div>
          </div>

          <div class="toolkit-group">
            <div class="toolkit-heading">Broadcast Motion Graphics & Visual Design</div>
            <div class="card-pills">
              <span class="card-pill highlight">Adobe After Effects</span>
              <span class="card-pill">Adobe Photoshop</span>
              <span class="card-pill">EffectCraft Engine</span>
              <span class="card-pill">Figma Design Systems</span>
              <span class="card-pill">Kinetic Typography</span>
            </div>
          </div>

          <div class="toolkit-group" style="margin-bottom: 0;">
            <div class="toolkit-heading">Systems & Automated Pipelines</div>
            <div class="card-pills">
              <span class="card-pill highlight">Google Antigravity</span>
              <span class="card-pill">TypeScript</span>
              <span class="card-pill">Next.js 15</span>
              <span class="card-pill">Python</span>
              <span class="card-pill">FFmpeg Mastering</span>
              <span class="card-pill">Git CI/CD</span>
            </div>
          </div>
        </div>

        <div class="cover-cta-box" style="margin-top: 3mm;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2mm;">
            <div style="font-size: 10pt; font-weight: 700; color: #FFFFFF;">
              Direct Recruiter Access & Submission Notes
            </div>
            <div class="pulse-dot"></div>
          </div>
          <p style="font-size: 7.5pt; color: #94A3B8; line-height: 1.35; margin-bottom: 3mm;">
            This portfolio document is accompanied by Benny Joel's official 1-page resume (<code style="color: #60A5FA;">Benny_Joel_Lakamana_Resume.pdf</code>) in the recruiter submission package.
          </p>
          <div style="display: flex; gap: 8px;">
            <a href="https://bennyjoel.github.io/portfolio/" class="cover-btn" style="flex: 1; justify-content: center; font-size: 8pt; padding: 5px 12px;">
              Launch Live Portfolio →
            </a>
            <a href="mailto:bennyofficial19@gmail.com" class="cover-btn" style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); box-shadow: none; font-size: 8pt; padding: 5px 12px;">
              Email Benny Joel
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span class="footer-left">BENNY JOEL LAKAMANA • VERIFIED ACADEMIC & PRODUCTION CREDENTIALS</span>
      <span class="footer-center"><a href="https://bennyjoel.github.io/portfolio/" class="footer-link">Portfolio Website: https://bennyjoel.github.io/portfolio/</a></span>
      <span class="footer-right">PAGE 07 / 07</span>
    </div>
  </div>

</body>
</html>
"""

def generate_pdf_and_package():
    print("Step 1: Writing master HTML document...")
    HTML_PATH.write_text(HTML_TEMPLATE, encoding="utf-8")
    print(f"[OK] HTML written: {HTML_PATH} ({HTML_PATH.stat().st_size:,} bytes)")

    print("\nStep 2: Compiling PDF via Headless Microsoft Edge...")
    cmd_pdf = [
        EDGE_EXE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}", HTML_PATH.as_uri()
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"[OK] PDF generated: {PDF_PATH} ({PDF_PATH.stat().st_size:,} bytes)")

    print("\nStep 3: Verifying PDF with PyMuPDF & PyPDF...")
    reader = pypdf.PdfReader(str(PDF_PATH))
    num_pages = len(reader.pages)
    print(f"Total Pages: {num_pages}")
    assert num_pages == 7, f"Expected exactly 7 pages, got {num_pages}!"

    # Render PNG previews of Page 1 and Page 2 for visual audit
    doc = pymupdf.open(str(PDF_PATH))
    for i in range(min(num_pages, 3)):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        preview_png = BRAIN_DIR / f"portfolio_doc_page_{i+1}.png"
        pix.save(str(preview_png))
        print(f"[OK] Rendered preview: {preview_png.name} ({pix.width}x{pix.height}, {preview_png.stat().st_size:,} bytes)")
    doc.close()

    print("\nStep 4: Copying portfolio PDF to E:\\Resume\\...")
    dst_portfolio_pdf = RESUME_DIR / "Benny_Joel_Lakamana_Portfolio.pdf"
    shutil.copy2(str(PDF_PATH), str(dst_portfolio_pdf))
    print(f"[OK] Synced to: {dst_portfolio_pdf}")

    print("\nStep 5: Verifying resume source PDF...")
    assert RESUME_PDF_PATH.exists(), f"Missing resume: {RESUME_PDF_PATH}"
    print(f"[OK] Verified resume: {RESUME_PDF_PATH} ({RESUME_PDF_PATH.stat().st_size:,} bytes)")

    print("\nStep 6: Creating Recruiter ZIP Package...")
    # The ZIP should contain:
    # 1. Benny_Joel_Lakamana_Resume.pdf
    # 2. Benny_Joel_Lakamana_Portfolio.pdf
    
    for zip_target in [ZIP_RESUME_PATH, ZIP_PORTFOLIO_PATH]:
        with zipfile.ZipFile(str(zip_target), "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(str(RESUME_PDF_PATH), arcname="Benny_Joel_Lakamana_Resume.pdf")
            zf.write(str(PDF_PATH), arcname="Benny_Joel_Lakamana_Portfolio.pdf")
        print(f"[OK] Created ZIP package: {zip_target} ({zip_target.stat().st_size:,} bytes)")

    # Inspect ZIP entries
    with zipfile.ZipFile(str(ZIP_RESUME_PATH), "r") as zf:
        print("\nZIP Contents:")
        for info in zf.infolist():
            print(f"  - {info.filename} ({info.file_size:,} bytes)")

    print("\n=== ALL DELIVERABLES GENERATED & VERIFIED SUCCESSFULLY ===")

if __name__ == "__main__":
    generate_pdf_and_package()
