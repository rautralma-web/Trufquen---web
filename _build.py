#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera las 5 páginas de línea de Trufquén desde UNA plantilla.
Garantiza header, footer, paleta y estructura idénticos en todas.
Ejecutar:  python3 _build.py
"""
import io, os

# ---------------------------------------------------------------- plantilla
TPL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Trufquén</title>
<meta name="description" content="{meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,100..900&family=Lato:wght@200;300;400&family=Space+Mono:wght@400&display=swap" rel="stylesheet">
<style>
:root{{
  --fondo:#100E0D;--fondo-2:#181513;--grafito:#0A0908;
  --mineral:#F0EBE3;--ceniza:#CFC8BE;--cobre:#C07E45;--terracota:#C98A5E;
  --humo:#8F857B;--tinta:#F0EBE3;--linea:rgba(240,235,227,0.13);
  --fs-micro:.6875rem;--fs-ui:.75rem;--fs-small:.875rem;--fs-body:1rem;--fs-pull:clamp(1.25rem,2vw,1.5rem);--fs-h3:clamp(1.4rem,2.6vw,1.85rem);--fs-h2:clamp(1.7rem,3vw,2.3rem);--fs-h1:clamp(2.1rem,4.6vw,3.1rem)
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:focus-visible{{outline:2px solid var(--cobre);outline-offset:3px}}
.skip{{position:absolute;inset-inline-start:-999px;z-index:120;font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:.14em;text-transform:uppercase;color:var(--fondo);background:var(--cobre);padding:1rem 1.4rem}}
.skip:focus{{position:fixed;inset-inline-start:0;inset-block-start:0}}
html{{scroll-behavior:smooth}}
h1,h2,h3,.pull,.sheet a{{font-family:'Archivo','Lato',sans-serif;font-stretch:125%}}
body{{font-family:'Lato',sans-serif;font-weight:300;background:var(--fondo);color:var(--mineral);line-height:1.75;-webkit-font-smoothing:antialiased}}
body.locked{{overflow:hidden}}
img{{display:block;max-width:100%}}
a{{color:inherit;text-decoration:none}}
.lang [data-en]{{display:none}}
.lang.en [data-es]{{display:none}}
.lang.en [data-en]{{display:inline}}
.lang.en [data-en].block{{display:block}}

nav.top{{position:fixed;top:0;left:0;right:0;z-index:80;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;
  height:var(--navh,104px);padding:0 clamp(1.2rem,4vw,3rem);pointer-events:none;
  transition:height .5s cubic-bezier(.22,.68,.24,1),background .45s,box-shadow .45s}}
nav.top > *{{pointer-events:auto}}
nav.top.solid{{height:62px;--bs:.52;background:rgba(16,14,13,.92);backdrop-filter:blur(18px);box-shadow:0 1px 0 var(--linea)}}
.brand{{position:absolute;left:50%;top:50%;display:flex;flex-direction:column;align-items:center;gap:.45rem;mix-blend-mode:difference;color:#fff;
  transform:translate(-50%,-50%) scale(var(--bs,1));transition:transform .5s cubic-bezier(.22,.68,.24,1);will-change:transform}}
.brand img{{height:clamp(40px,4.2vw,54px);width:auto;filter:invert(1) brightness(3)}}
.brand .word{{font-weight:200;font-size:clamp(1.1rem,2.3vw,1.6rem);letter-spacing:.44em;text-indent:.44em;text-transform:uppercase;white-space:nowrap;line-height:1}}
.menubtn,.langbtn{{background:none;border:none;cursor:pointer;font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:.16em;text-transform:uppercase;padding:8px 0;min-height:44px;mix-blend-mode:difference;color:#fff;transition:opacity .2s}}
.menubtn{{grid-column:1;justify-self:start}}
.langbtn{{grid-column:3;justify-self:end}}
.menubtn:hover,.langbtn:hover{{opacity:.6}}
.sheet{{position:fixed;inset:0;z-index:95;background:var(--fondo);display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .4s}}
.sheet.open{{opacity:1;pointer-events:auto}}
.sheet nav{{display:flex;flex-direction:column;gap:.3rem;text-align:center}}
.sheet a{{font-weight:200;font-size:var(--fs-h2);letter-spacing:.12em;text-transform:uppercase;color:var(--mineral);padding:.3rem 1rem}}
.sheet a:hover{{color:var(--cobre)}}
.sheet .close{{position:absolute;top:1.6rem;right:clamp(1.2rem,4vw,3rem);background:none;border:none;font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:.16em;text-transform:uppercase;color:var(--mineral);cursor:pointer;min-height:44px;min-width:44px;display:inline-flex;align-items:center;justify-content:center}}

.hero{{position:relative;height:100vh;height:100dvh;background:var(--grafito);overflow:hidden}}
.hero img,.hero video{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{heropos}}}
.hero::after{{content:'';position:absolute;inset:0;background:linear-gradient(to bottom,rgba(10,9,8,.5) 0%,rgba(10,9,8,.08) 32%,rgba(10,9,8,.2) 60%,rgba(16,14,13,.95) 100%)}}
.hero-line{{position:absolute;left:0;right:0;bottom:clamp(2.5rem,7vh,5rem);z-index:2;text-align:center;padding:0 1.5rem}}
.hero-line h1{{font-weight:200;font-size:var(--fs-h1);letter-spacing:.08em;text-transform:uppercase;color:var(--mineral);margin-bottom:1rem}}
.hero-line p{{font-weight:200;font-size:var(--fs-pull);line-height:1.6;color:var(--humo);max-width:34rem;margin:0 auto}}
.hero-line .em{{color:var(--cobre)}}

.wrap{{max-width:1180px;margin:0 auto;padding:0 clamp(1.4rem,5vw,3.5rem)}}
.narrow{{max-width:38rem;margin:0 auto;text-align:center}}
section{{padding:clamp(4.5rem,10vh,7rem) 0}}
.idx{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.24em;color:var(--humo);text-transform:uppercase;display:block;margin-bottom:2rem;text-align:center}}
h2{{font-weight:200;line-height:1.3;font-size:var(--fs-h2)}}
.lede{{font-size:var(--fs-body);line-height:1.9;color:var(--ceniza);margin-top:1.4rem}}
.em{{color:var(--terracota)}}
.band-c{{background:var(--fondo-2)}}
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,5vw,4rem);margin-top:2.5rem;text-align:left}}
@media(max-width:760px){{.duo{{grid-template-columns:1fr;gap:1.5rem}}}}
.duo p{{font-size:var(--fs-small);line-height:1.9;color:var(--ceniza)}}
.pull{{font-weight:200;font-size:var(--fs-pull);line-height:1.5;color:var(--mineral);max-width:44rem;margin:0 auto;border-left:1px solid var(--cobre);padding-left:1.6rem;text-align:left}}

.plate{{width:100%;background:var(--grafito);cursor:zoom-in}}
.plate img{{width:100%;height:clamp(380px,80vh,820px);object-fit:cover;display:block}}
.plate video{{width:100%;height:auto;max-height:90vh;object-fit:contain;background:var(--grafito);display:block;margin:0 auto}}

.gal{{padding:clamp(4rem,9vh,6rem) 0}}
.car{{display:flex;gap:2px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:0 clamp(1.4rem,5vw,3.5rem);cursor:grab}}
.car::-webkit-scrollbar{{display:none}}
.car.drag{{cursor:grabbing;scroll-snap-type:none}}
.car figure{{flex:0 0 clamp(280px,44vw,580px);scroll-snap-align:center;margin:0;position:relative;overflow:hidden;background:var(--grafito)}}
.car img{{width:100%;aspect-ratio:4/5;object-fit:cover;transition:opacity .5s,transform 1s cubic-bezier(.2,.6,.2,1);opacity:.42}}
.car .ph{{width:100%;aspect-ratio:4/5;background:linear-gradient(155deg,#2a2018,#12100c 60%,#0c0a08);display:flex;align-items:center;justify-content:center;opacity:.42;transition:opacity .5s}}
.car .ph span{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.2em;color:rgba(240,235,227,.55);text-transform:uppercase}}
.car figure.on img,.car figure.on .ph{{opacity:1}}
.car figure.on:hover img{{transform:scale(1.03)}}
.car figure.sym img{{object-fit:contain;padding:14%;background:var(--fondo-2)}}
.car figure.sym.on:hover img{{transform:none}}
.car figure::after{{content:"⤢";position:absolute;right:1rem;bottom:1rem;font-size:.8rem;color:rgba(240,235,227,.85);opacity:0;transition:opacity .3s;pointer-events:none}}
.car figure.on:hover::after{{opacity:1}}

.car-ui{{max-width:1180px;margin:2rem auto 0;padding:0 clamp(1.4rem,5vw,3.5rem);display:grid;grid-template-columns:1fr auto;gap:2rem;align-items:end}}
@media(max-width:760px){{.car-ui{{grid-template-columns:1fr;gap:1.5rem}}}}
.car-txt{{min-height:8.5rem}}
.car-txt .n{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.18em;color:var(--cobre);text-transform:uppercase;display:block;margin-bottom:.7rem}}
.car-txt h3{{font-weight:200;font-size:var(--fs-h3);line-height:1.2;margin-bottom:.5rem}}
.car-txt .spec{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.14em;color:var(--humo);text-transform:uppercase;display:block;margin-bottom:.9rem}}
.car-txt p{{font-size:var(--fs-small);line-height:1.8;color:var(--ceniza);max-width:34rem}}
.car-txt .fade{{animation:swap .45s cubic-bezier(.2,.6,.2,1)}}
@keyframes swap{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.car-ctl{{display:flex;flex-direction:column;align-items:flex-end;gap:1rem}}
.car-count{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.14em;color:var(--humo)}}
.car-btns{{display:flex;gap:.5rem}}
.car-btn{{background:none;border:1px solid var(--linea);color:var(--mineral);width:46px;height:46px;cursor:pointer;font-size:1.1rem;line-height:1;transition:all .2s}}
.car-btn:hover{{border-color:var(--cobre);color:var(--cobre)}}
.car-prog{{width:100%;max-width:1180px;margin:1.5rem auto 0;padding:0 clamp(1.4rem,5vw,3.5rem)}}
.car-prog i{{display:block;height:1px;background:var(--linea);position:relative}}
.car-prog i::after{{content:'';position:absolute;left:0;top:0;height:1px;background:var(--cobre);width:var(--p,16.6%);transition:width .3s}}

details.more{{max-width:38rem;margin:0 auto;border-top:1px solid var(--linea)}}
details.more summary{{cursor:pointer;list-style:none;padding:1.1rem 0;font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.18em;text-transform:uppercase;color:var(--cobre);display:flex;justify-content:center;gap:.6rem;align-items:center}}
details.more summary::-webkit-details-marker{{display:none}}
details.more summary::after{{content:"+";font-size:var(--fs-small);transition:transform .25s}}
details.more[open] summary::after{{transform:rotate(45deg)}}
.fgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.4rem 2rem;padding:1rem 0 2.5rem;text-align:left}}
.fgrid dt{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.16em;text-transform:uppercase;color:var(--cobre);margin-bottom:.4rem}}
.fgrid dd{{font-size:var(--fs-small);line-height:1.7;color:var(--ceniza)}}

footer{{position:relative;background:var(--grafito);color:var(--humo);padding:clamp(3rem,7vw,4.5rem) 0;text-align:center}}
footer::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(192,126,69,.65) 22%,rgba(192,126,69,.65) 78%,transparent)}}
footer .fbrand{{display:inline-flex;flex-direction:column;align-items:center;gap:.6rem;margin-bottom:1.5rem}}
footer .fbrand img{{height:44px}}
footer .fbrand span{{font-weight:200;letter-spacing:.42em;text-indent:.42em;text-transform:uppercase;color:var(--mineral);font-size:1.1rem}}
footer a{{font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:.14em;color:var(--humo);text-transform:uppercase;margin:0 .7rem;line-height:2.4}}
footer a:hover{{color:var(--cobre)}}
.legal{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.08em;color:rgba(160,150,140,.85);line-height:1.9;text-transform:uppercase;margin-top:2rem;max-width:44rem;margin-left:auto;margin-right:auto;padding:0 1.5rem}}

.lb{{position:fixed;inset:0;z-index:100;background:rgba(8,7,6,.98);display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .35s}}
.lb.open{{opacity:1;pointer-events:auto}}
.lb img{{max-width:92vw;max-height:82vh;object-fit:contain}}
.lb-cap{{position:absolute;bottom:2.2rem;left:0;right:0;text-align:center;font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.16em;color:var(--humo);text-transform:uppercase;padding:0 4rem}}
.lb-count{{position:absolute;top:2rem;left:0;right:0;text-align:center;font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.16em;color:rgba(143,133,123,.8)}}
.lb-x{{position:absolute;top:1.2rem;right:1.4rem;background:none;border:none;color:var(--mineral);font-size:1.4rem;cursor:pointer;min-width:44px;min-height:44px;display:flex;align-items:center;justify-content:center}}
.lb-nav{{position:absolute;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--mineral);font-size:2rem;cursor:pointer;padding:1.5rem;opacity:.55;transition:opacity .2s}}
.lb-nav:hover{{opacity:1}}
.lb-prev{{left:.5rem}}.lb-next{{right:.5rem}}
@media(max-width:640px){{.lb-nav{{font-size:1.4rem;padding:.8rem}}}}
@media(max-width:640px){{
:root{{--fs-micro:.75rem;--fs-ui:.8125rem;--fs-small:.9375rem}}
nav.top{{height:88px}}
nav.top.solid{{height:56px;--bs:.6}}
.menubtn,.langbtn{{padding:8px 10px}}
}}

@media (prefers-reduced-motion: no-preference){{
  @keyframes ignite{{from{{opacity:.18;transform:scale(1.045)}}to{{opacity:1;transform:none}}}}
  @keyframes emerge{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
  .hero img,.hero video{{animation:ignite 1.5s cubic-bezier(.22,.61,.24,1) .1s both}}
  .hero-line{{animation:emerge 1s cubic-bezier(.2,.6,.2,1) .55s both}}
}}
@media (prefers-reduced-motion: reduce){{
  *,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}
}}
</style>
</head>
<body class="lang">
<a href="#contenido" class="skip"><span data-es>Saltar al contenido</span><span data-en>Skip to content</span></a>

<nav class="top" id="nav">
  <button class="menubtn" id="menuBtn" aria-expanded="false" aria-controls="sheet"><span data-es>Menú</span><span data-en>Menu</span></button>
  <a href="index.html" class="brand"><img src="img/brand/icon-blanco.png" alt=""><span class="word">Trufquén</span></a>
  <button class="langbtn" id="langBtn" aria-label="Cambiar idioma / Switch language">EN/ES</button>
</nav>

<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-label="Menú de navegación">
  <button class="close" id="sheetClose"><span data-es>Cerrar</span><span data-en>Close</span></button>
  <nav>
    <a href="index.html"><span data-es>Inicio</span><span data-en>Home</span></a>
    <a href="ahumador-trufquen.html"><span data-es>Ahumador</span><span data-en>Smoking vessel</span></a>
    <a href="probetas-trufquen.html"><span data-es>Probetas</span><span data-en>Test pieces</span></a>
    <a href="engarce-trufquen.html">Engarce</a>
    <a href="luminarias-trufquen.html"><span data-es>Luminarias</span><span data-en>Lighting</span></a>
    <a href="tralma-trufquen.html">Tralma</a>
    <a href="index.html#contacto"><span data-es>Contacto</span><span data-en>Contact</span></a>
  </nav>
</div>

<main id="contenido">
<header class="hero">
  {hero_media}
  <div class="hero-line">
    <h1><span data-es>{h1_es}</span><span data-en>{h1_en}</span></h1>
    <p><span data-es>{hp_es}</span><span data-en class="block">{hp_en}</span></p>
  </div>
</header>

<section>
  <div class="wrap narrow">
    <span class="idx"><span data-es>{idx_es}</span><span data-en>{idx_en}</span></span>
    <h2><span data-es>{t_es}</span><span data-en class="block">{t_en}</span></h2>
    <p class="lede"><span data-es>{l_es}</span><span data-en class="block">{l_en}</span></p>
    <p class="lede"><span data-es>{l2_es}</span><span data-en class="block">{l2_en}</span></p>
  </div>
</section>

<figure class="plate">
  {plate_media}
</figure>

<section class="gal band-c">
  <div class="wrap narrow" style="margin-bottom:3rem">
    <span class="idx"><span data-es>Evidencia material</span><span data-en>Material evidence</span></span>
    <h2><span data-es>{g_es}</span><span data-en class="block">{g_en}</span></h2>
  </div>

  <div class="car" id="car" role="region" aria-roledescription="carousel" aria-label="{g_es}">
{slides}  </div>

  <div class="car-prog"><i id="prog"></i></div>

  <div class="car-ui">
    <div class="car-txt" id="txt" aria-live="polite" aria-atomic="true">
      <span class="n" id="tn">01</span>
      <h3 id="tt"></h3>
      <span class="spec" id="ts"></span>
      <p id="td"></p>
    </div>
    <div class="car-ctl">
      <span class="car-count" id="count">01 / 06</span>
      <div class="car-btns">
        <button class="car-btn" id="btnPrev" aria-controls="car" aria-label="Pieza anterior">‹</button>
        <button class="car-btn" id="btnNext" aria-controls="car" aria-label="Pieza siguiente">›</button>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="narrow">
      <span class="idx"><span data-es>{c_idx_es}</span><span data-en>{c_idx_en}</span></span>
      <h2><span data-es>{c_t_es}</span><span data-en class="block">{c_t_en}</span></h2>
    </div>
    <div class="duo">
      <p><span data-es>{c_a_es}</span><span data-en class="block">{c_a_en}</span></p>
      <p><span data-es>{c_b_es}</span><span data-en class="block">{c_b_en}</span></p>
    </div>
  </div>
</section>

<section class="band-c">
  <div class="wrap">
    <p class="pull"><span data-es>{quote_es}</span><span data-en class="block">{quote_en}</span></p>
  </div>
</section>

<section>
  <div class="wrap">
    <details class="more">
      <summary><span data-es>Ficha técnica</span><span data-en>Technical sheet</span></summary>
      <dl class="fgrid">
{ficha}      </dl>
    </details>
  </div>
</section>
</main>

<footer>
  <div class="fbrand"><img src="img/brand/icon-blanco.png" alt=""><span>Trufquén</span></div>
  <div>
    <a href="index.html"><span data-es>Inicio</span><span data-en>Home</span></a>
    <a href="https://trufquen.studio">trufquen.studio</a>
    <a href="https://instagram.com/trufquen">@trufquen</a>
    <a href="mailto:contacto@trufquen.studio">contacto@trufquen.studio</a>
  </div>
  <p class="legal"><span data-es>© 2026 Trufquén · Marca registrada INAPI N° 1391981 · Patente de invención INAPI N° 2015-01441 · Santiago de Chile</span><span data-en class="block">© 2026 Trufquén · Registered trademark INAPI No. 1391981 · INAPI invention patent No. 2015-01441 · Santiago, Chile</span></p>
</footer>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Vista ampliada de imagen">
  <button class="lb-x" id="lbX" aria-label="Cerrar">✕</button>
  <button class="lb-nav lb-prev" id="lbPrev" aria-label="Imagen anterior">‹</button>
  <img id="lbImg" alt="">
  <button class="lb-nav lb-next" id="lbNext" aria-label="Imagen siguiente">›</button>
  <div class="lb-count" id="lbCount"></div>
  <div class="lb-cap" id="lbCap"></div>
</div>

<script>
function ariaLang(){{var en=document.body.classList.contains('en');
  var m={{btnPrev:['Pieza anterior','Previous piece'],btnNext:['Pieza siguiente','Next piece'],lbX:['Cerrar','Close'],lbPrev:['Imagen anterior','Previous image'],lbNext:['Imagen siguiente','Next image']}};
  for(var k in m){{var el=document.getElementById(k);if(el)el.setAttribute('aria-label',en?m[k][1]:m[k][0])}}
  figs.forEach(function(f,i){{f.setAttribute('aria-label',('0'+(i+1)).slice(-2)+(en?' of ':' de ')+figs.length)}})}}
function toggleLang(){{var b=document.body;b.classList.toggle('en');document.documentElement.lang=b.classList.contains('en')?'en':'es';carPaint(carAt);ariaLang()}}
var sheetEl=document.getElementById('sheet'), menuBtn=document.getElementById('menuBtn'), sheetPrevFocus=null;
function openSheet(){{sheetPrevFocus=document.activeElement;sheetEl.classList.add('open');menuBtn.setAttribute('aria-expanded','true');document.getElementById('sheetClose').focus()}}
function closeSheet(){{sheetEl.classList.remove('open');menuBtn.setAttribute('aria-expanded','false');if(sheetPrevFocus)sheetPrevFocus.focus()}}
menuBtn.addEventListener('click',openSheet);
document.getElementById('sheetClose').addEventListener('click',closeSheet);
document.getElementById('langBtn').addEventListener('click',toggleLang);
sheetEl.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',closeSheet)}});
(function(){{var n=document.getElementById('nav'),h=document.querySelector('.hero');
  new IntersectionObserver(function(e){{n.classList.toggle('solid',!e[0].isIntersecting)}},{{rootMargin:'-88% 0px 0px 0px'}}).observe(h)}})();

var car=document.getElementById('car'), figs=[].slice.call(car.querySelectorAll('figure')), carAt=0, snapping=false;
function slideW(){{return figs[0].getBoundingClientRect().width+2}}
function carPaint(i){{
  var f=figs[i]; if(!f) return;
  var en=document.body.classList.contains('en');
  var t=document.getElementById('txt');
  document.getElementById('tn').textContent=f.dataset.n;
  document.getElementById('tt').textContent=en?f.dataset.tEn:f.dataset.tEs;
  document.getElementById('ts').textContent=en?f.dataset.sEn:f.dataset.sEs;
  document.getElementById('td').textContent=en?f.dataset.dEn:f.dataset.dEs;
  document.getElementById('count').textContent=('0'+(i+1)).slice(-2)+' / '+('0'+figs.length).slice(-2);
  document.getElementById('prog').style.setProperty('--p',((i+1)/figs.length*100)+'%');
  figs.forEach(function(x,j){{x.classList.toggle('on',j===i);x.setAttribute('aria-hidden',j===i?'false':'true')}});
  t.classList.remove('fade'); void t.offsetWidth; t.classList.add('fade');
}}
function snapLeft(i){{var fr=figs[i].getBoundingClientRect(),cr=car.getBoundingClientRect();return car.scrollLeft+fr.left-cr.left-(cr.width-fr.width)/2}}
function carIdx(){{var i=Math.round((car.scrollLeft-snapLeft(0))/slideW());return Math.max(0,Math.min(figs.length-1,i))}}
var snapT=null;
function snapFree(){{snapping=false;var i=carIdx();if(i!==carAt){{carAt=i;carPaint(i)}}}}
function carTo(i,smooth){{carAt=i;snapping=true;clearTimeout(snapT);snapT=setTimeout(snapFree,600);car.scrollTo({{left:snapLeft(i),behavior:smooth===false?'auto':'smooth'}});carPaint(i)}}
function carGo(d){{carTo((carAt+d+figs.length)%figs.length)}}
car.addEventListener('scroll',function(){{
  if(snapping){{clearTimeout(snapT);snapT=setTimeout(snapFree,150);return}}
  var i=carIdx();
  if(i!==carAt){{carAt=i;carPaint(i)}}
}});
(function(){{
  var down=false,x0=0,s0=0,moved=0;
  car.addEventListener('mousedown',function(e){{down=true;moved=0;x0=e.pageX;s0=car.scrollLeft;car.classList.add('drag')}});
  window.addEventListener('mouseup',function(){{if(!down)return;down=false;car.classList.remove('drag');
    carTo(carIdx())}});
  car.addEventListener('mousemove',function(e){{if(!down)return;e.preventDefault();moved=Math.abs(e.pageX-x0);car.scrollLeft=s0-(e.pageX-x0)}});
  car.addEventListener('click',function(e){{if(moved>6){{e.preventDefault();e.stopPropagation()}}}},true);
}})();
window.addEventListener('resize',function(){{carTo(carAt,false)}});
document.getElementById('btnPrev').addEventListener('click',function(){{carGo(-1)}});
document.getElementById('btnNext').addEventListener('click',function(){{carGo(1)}});
carPaint(0);
ariaLang();

var lbSet=[],lbAt=0,lb=document.getElementById('lb'),lbImg=document.getElementById('lbImg'),lbPrevFocus=null;
function lbOpen(img){{lbPrevFocus=document.activeElement;lbSet=[].slice.call(document.querySelectorAll('.car img, .plate img, .hero img'));lbAt=lbSet.indexOf(img);lbRender();lb.classList.add('open');document.body.classList.add('locked');document.getElementById('lbX').focus()}}
function lbRender(){{var im=lbSet[lbAt];if(!im)return;lbImg.src=im.currentSrc||im.src;lbImg.alt=im.alt||'';
  document.getElementById('lbCap').textContent=im.dataset.cap||im.alt||'';
  document.getElementById('lbCount').textContent=(lbAt+1)+' / '+lbSet.length}}
function lbGo(d){{lbAt=(lbAt+d+lbSet.length)%lbSet.length;lbRender()}}
function lbClose(){{lb.classList.remove('open');document.body.classList.remove('locked');if(lbPrevFocus)lbPrevFocus.focus()}}
document.getElementById('lbX').addEventListener('click',lbClose);
document.getElementById('lbPrev').addEventListener('click',function(){{lbGo(-1)}});
document.getElementById('lbNext').addEventListener('click',function(){{lbGo(1)}});
lb.addEventListener('keydown',function(e){{
  if(e.key!=='Tab')return;
  var f=[document.getElementById('lbX'),document.getElementById('lbPrev'),document.getElementById('lbNext')];
  var i=f.indexOf(document.activeElement);
  if(e.shiftKey && (i<=0)){{e.preventDefault();f[f.length-1].focus()}}
  else if(!e.shiftKey && i===f.length-1){{e.preventDefault();f[0].focus()}}
}});
document.addEventListener('click',function(e){{
  var t=e.target.closest('.car figure, .plate');
  if(t){{var im=t.querySelector('img');if(im){{e.preventDefault();lbOpen(im)}}}}
}});
lb.addEventListener('click',function(e){{if(e.target===lb)lbClose()}});
document.addEventListener('keydown',function(e){{
  if(e.key==='Escape' && sheetEl.classList.contains('open')){{closeSheet();return}}
  if(lb.classList.contains('open')){{
    if(e.key==='Escape')lbClose(); if(e.key==='ArrowLeft')lbGo(-1); if(e.key==='ArrowRight')lbGo(1);
  }} else if(!sheetEl.classList.contains('open')){{ if(e.key==='ArrowLeft')carGo(-1); if(e.key==='ArrowRight')carGo(1); }}
}});
(function(){{var x0=null;
  lb.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX}},{{passive:true}});
  lb.addEventListener('touchend',function(e){{if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>50)lbGo(dx>0?-1:1);x0=null}},{{passive:true}})}})();

if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){{
  document.querySelectorAll('video[data-motion]').forEach(function(v){{v.pause();v.removeAttribute('autoplay')}});
}}
</script>
</body>
</html>
"""

def slide(n, img, t_es, t_en, s_es, s_en, d_es, d_en, cap, fig_class=''):
    inner = ('<img src="%s" alt="%s" data-cap="%s" loading="lazy">' % (img, t_es, cap)) if img else \
            '<div class="ph"><span>Imagen pendiente</span></div>'
    cls = (' class="%s"' % fig_class) if fig_class else ''
    return ('    <figure%s role="group" aria-roledescription="slide" aria-label="%s de 6" data-n="%s" data-t-es="%s" data-t-en="%s" data-s-es="%s" data-s-en="%s" data-d-es="%s" data-d-en="%s">\n      %s\n    </figure>\n'
            % (cls, n, n, t_es, t_en, s_es, s_en, d_es, d_en, inner))

def ficha(rows):
    return ''.join('        <div><dt><span data-es>%s</span><span data-en>%s</span></dt><dd><span data-es>%s</span><span data-en>%s</span></dd></div>\n'
                   % r for r in rows)

# ---------------------------------------------------------------- datos
P = []

# ---------- ENGARCE
P.append(dict(
 slug='engarce-trufquen.html', title='Engarce',
 l2_es='Engarce no comenzó como catálogo, sino como una pregunta técnica: ¿pueden dos materiales de comportamiento térmico opuesto coexistir en un solo cuerpo sin que uno destruya al otro? La respuesta se construyó en dos etapas con respaldo Fondart. La primera estableció mediante probetas que la cohesión era posible; la segunda la llevó a producción controlada. Once piezas únicas son su resultado material.',
 l2_en="Engarce didn't begin as a catalog, but as a technical question: can two materials with opposite thermal behavior coexist in one body without destroying each other? The answer was built in two Fondart-backed stages. The first established through test pieces that cohesion was possible; the second took it to controlled production. Eleven unique pieces are its material result.",
 c_idx_es='Alcance',
 c_idx_en='Scope',
 c_t_es='La serie que fijó<br>los parámetros',
 c_t_en='The series that set<br>the parameters',
 c_a_es='Engarce demostró que la cohesión greda–vidrio es posible, controlable y producible. Once piezas, dos oficios articulados, una técnica documentada. Lo que en otras manos sería un hallazgo casual, aquí quedó fijado como método repetible.',
 c_a_en='Engarce proved that clay–glass cohesion is possible, controllable and producible. Eleven pieces, two crafts articulated, one technique documented. What in other hands would be a casual finding was fixed here as a repeatable method.',
 c_b_es='También abrió la agenda que sigue: greda negra, cristal de color, matricería en otros materiales. Ese horizonte no es tarea pendiente, sino la señal de un trabajo que entiende cada colección como etapa, no como cierre.',
 c_b_en="It also opened the agenda that continues: black clay, colored crystal, matrix-making in other materials. That horizon isn't unfinished business, but the sign of a practice that sees each collection as a stage, not a closing.",
 quote_es='Sé dónde y cuándo el vidrio incandescente puede expandirse contra la arcilla sin quebrarla. Ese punto no está en un manual: lo aprendí probándolo pieza por pieza, durante años, hasta poder repetirlo.',
 quote_en="I know where and when incandescent glass can expand against the clay without cracking it. That point isn't in a manual: I learned it testing it piece by piece, over years, until I could repeat it.",
 meta='Engarce: once piezas únicas de greda de Pomaire y cristal soplado a boca. La unión es mecánica, no fusión.',
 hero='img/engarce/hero.jpg', heropos='center 40%',
 h1_es='Engarce', h1_en='Engarce',
 hp_es='El cristal se expande contra la greda y queda retenido por forma. La unión es mecánica, <span class="em">no una fusión.</span>',
 hp_en='Glass expands against the clay and is held by form. The union is mechanical, <span class="em">not a fusion.</span>',
 idx_es='2018 — 11 piezas únicas', idx_en='2018 — 11 unique pieces',
 t_es='En joyería, engarzar es sujetar<br>una piedra <span class="em">sin fundirla.</span>',
 t_en='In jewelry, to set a stone is to hold it<br><span class="em">without melting it.</span>',
 l_es='El nombre no es metáfora: es la descripción técnica exacta. El cristal ancla por perforación, relieve o anillo. Donde la greda es lisa, se desprende.',
 l_en="The name isn't a metaphor: it's the exact technical description. The glass anchors by perforation, relief or ring. Where the clay is smooth, it detaches.",
 plate='img/bg/engarce-genealogia.jpg', plate_alt='Proceso de la serie Engarce', plate_cap='Engarce · proceso',
 g_es='Once piezas, una misma tesis', g_en='Eleven pieces, one thesis',
 slides=(
  slide('01','img/engarce/engarce-01-modelada.jpg','Modelada a mano','Hand-modeled','15–37 cm · greda de Pomaire','15–37 cm · Pomaire clay',
        'La greda se levanta sin torno. Cada cuerpo es irrepetible, y el cristal debe adaptarse a esa irregularidad.',
        'The clay is raised without a wheel. Each body is unrepeatable, and the glass must adapt to that irregularity.','01 · modelada a mano')+
  slide('02','img/engarce/engarce-02-torneada.jpg','Torneada','Wheel-turned','28–40 cm · greda de Pomaire','28–40 cm · Pomaire clay',
        'La simetría del torno reparte el empuje del vidrio de forma pareja. Es la geometría que más resiste.',
        "The wheel's symmetry distributes the glass's push evenly. It's the geometry that resists most.",'02 · torneada')+
  slide('03','img/engarce/engarce-03-torneada-texturizada.jpg','Torneada y texturizada','Wheel-turned and textured','28–39 cm · greda de Pomaire','28–39 cm · Pomaire clay',
        'La textura no es decorativa: aumenta la superficie de agarre y el cristal ancla mejor.',
        "The texture isn't decorative: it increases grip surface and the glass anchors better.",'03 · torneada y texturizada')+
  slide('04','img/engarce/engarce-04-translucido.jpg','Greda + cristal translúcido','Clay + translucent crystal','Cristal soplado a boca','Mouth-blown crystal',
        'Contra el fondo negro, el cristal existe como forma autónoma y la greda como masa terrestre.',
        'Against the black background, the glass exists as autonomous form and the clay as earthly mass.','04 · greda + cristal translúcido')+
  slide('05','img/engarce/engarce-05-relieve.jpg','Anclaje por relieve','Relief anchoring','Unión mecánica','Mechanical union',
        'El relieve retiene el cristal por presión de forma. No hay adhesión química en ningún punto.',
        'The relief retains the glass by form pressure. There is no chemical adhesion at any point.','05 · anclaje por relieve')+
  slide('06','img/engarce/engarce-06-perforacion.jpg','Anclaje por perforación','Perforation anchoring','Unión mecánica','Mechanical union',
        'El cristal atraviesa el calado y ancla al otro lado de la pared. La greda no se rompe si la abertura es menor que la masa que la rodea.',
        "The glass crosses the perforation and anchors on the other side of the wall. The clay doesn't break if the opening is smaller than the surrounding mass.",'06 · anclaje por perforación')),
 ficha=ficha([
  ('Serie','Series','11 piezas únicas · 2018–2019','11 unique pieces · 2018–2019'),
  ('Materialidad','Materiality','Greda de Pomaire + cristal soplado a boca','Pomaire clay + mouth-blown crystal'),
  ('Unión','Union','Mecánica. Perforación, relieve o anillo. Sin adhesión química.','Mechanical. Perforation, relief or ring. No chemical adhesion.'),
  ('Diseño','Design','Raúl Hernández Tralma','Raúl Hernández Tralma'),
  ('Greda','Clay','José Domingo Prado','José Domingo Prado'),
  ('Cristal','Glass','Raúl Lizama · CristalArt','Raúl Lizama · CristalArt'),
  ('Fotografía','Photography','Darío Vargas','Darío Vargas'),
  ('Dimensiones','Dimensions','Referenciales. La greda natural varía entre piezas.','Referential. Natural clay varies between pieces.'),
  ('Respaldo','Backing','Fondart Nacional · Folio 503470','National Fondart · Folio 503470'),
  ('Reconocimiento','Recognition','Individual GAM · Wanted Design NY · BID Madrid','Solo show GAM · Wanted Design NY · BID Madrid'),
 ])))

# ---------- TRALMA
P.append(dict(
 slug='tralma-trufquen.html', title='Tralma',
 l2_es='Lo que en 2019 se planteó como una vinculación estable entre alfarería de Pomaire y soplado a boca, en 2020 se resolvió como investigación de contingencia. CristalArt —heredera de la Cristalería Yungay, tradición sin plomo desde 1922— era la última empresa del país capaz de soplar a escala de proyecto. Su cierre nos dejó sin el oficio que sostenía la técnica, y obligó a rediseñar el proceso sin abandonar la tesis.',
 l2_en="What in 2019 was proposed as a stable link between Pomaire pottery and mouth-blowing was resolved in 2020 as contingency research. CristalArt —heir to Cristalería Yungay, a lead-free tradition since 1922— was the country's last company able to blow at project scale. Its closure left us without the craft that sustained the technique, and forced a redesign of the process without abandoning the thesis.",
 c_idx_es='Alcance',
 c_idx_en='Scope',
 c_t_es='Un resultado logrado<br>bajo presión real',
 c_t_en='A result achieved<br>under real pressure',
 c_a_es='Tralma entregó lo que se propuso —piezas de uso que unen greda y vidrio soplado a boca— reconstruyendo su base productiva a mitad de camino. Producción 100% a mano, pieza a pieza. La complejidad del contexto no rebajó el resultado: lo volvió más difícil de replicar.',
 c_a_en="Tralma delivered what it set out to do —usable pieces uniting clay and mouth-blown glass— while rebuilding its production base halfway through. 100% handmade, piece by piece. The context's complexity didn't lower the result: it made it harder to replicate.",
 c_b_es='Demostró que la técnica no depende de un único vidrio ni de un único proveedor. Esa versatilidad amplía el trabajo futuro y es, en la práctica, una barrera para quien intente copiar el resultado sin el proceso detrás.',
 c_b_en="It proved the technique doesn't depend on a single glass or a single supplier. That versatility broadens future work and is, in practice, a barrier for anyone trying to copy the result without the process behind it.",
 quote_es='Sabemos hacer esto; y sabemos rehacerlo cuando el terreno se mueve. Esa capacidad —no una copa en particular— es lo que la línea deja instalado.',
 quote_en='We know how to do this; and we know how to redo it when the ground shifts. That capacity —not any one cup— is what the line leaves installed.',
 meta='Tralma: greda colada y vidrio borosilicato soplado a boca. La línea que sobrevivió al cierre de la última cristalería del país.',
 hero='img/tralma/hero-serie.jpg', hero_video='img/tralma/tralma-fabricacion.mp4', hero_poster='img/tralma/hero-serie.jpg', heropos='center 45%',
 h1_es='Tralma', h1_en='Tralma',
 hp_es='Apellido materno del diseñador. Greda colada y borosilicato soplado a boca: la línea que <span class="em">sobrevivió a la desaparición de un oficio.</span>',
 hp_en="The designer's maternal surname. Cast clay and mouth-blown borosilicate: the line that <span class=\"em\">survived a craft's disappearance.</span>",
 idx_es='2020 — Cristalería', idx_en='2020 — Glassware',
 t_es='A mitad de camino cerró<br>la última cristalería <span class="em">del país.</span>',
 t_en='Halfway through, the country\'s<br>last glassworks <span class="em">closed.</span>',
 l_es='En vez de abandonar la hipótesis, le buscamos un sustrato nuevo: borosilicato en lugar de cristal sonoro. La distancia entre lo postulado y lo ejecutado es, en sí misma, el hallazgo.',
 l_en='Instead of abandoning the hypothesis, we found it a new substrate: borosilicate instead of sonorous crystal. The distance between what was proposed and what was executed is, in itself, the finding.',
 plate='img/tralma/copa-giro-poster.jpg', plate_video='img/tralma/copa-giro.mp4', plate_alt='Copa Tralma girando: borosilicato sobre base de greda colada', plate_cap='La copa terminada',
 g_es='Producción real, no render', g_en='Real production, not a render',
 slides=(
  slide('01','img/tralma/tralma-copa.jpg','Copa','Cup','Borosilicato + greda colada','Borosilicate + cast clay',
        'El cuerpo de vidrio se sopla contra la greda ya colada. La base no es un añadido: es la matriz que le dio forma.',
        'The glass body is blown against the already-cast clay. The base isn\'t an addition: it\'s the matrix that shaped it.','01 · copa')+
  slide('02','img/tralma/tralma-frontera.jpg','Frontera visible','Visible border','Unión mecánica','Mechanical union',
        'Greda y vidrio conservan una línea nítida entre sí. No hay masa única: esa frontera es la prueba de que la unión es mecánica.',
        'Clay and glass keep a sharp line between them. There is no single mass: that border proves the union is mechanical.','02 · frontera visible')+
  slide('03','img/tralma/tralma-soplado.jpg',u'Soplado a la llama','Flame-blown',u'Borosilicato en formación','Borosilicate in the making',
        u'El vidrio incandescente se sopla contra la base de greda ya colada. La copa nace de esa unión, no se ensambla después.',
        'The molten glass is blown against the already-cast clay base. The cup is born from that union, not assembled afterward.',u'03 · soplado a la llama')+
  slide('04','img/tralma/tralma-vino.jpg',u'Con vino','With wine',u'La pieza en uso','The piece in use',
        u'Llena, la copa se lee entera: el vino ocupa el vidrio y la greda lo sostiene desde abajo. El peso equilibra la mano.',
        'Filled, the cup reads whole: the wine occupies the glass and the clay holds it from below. The weight balances the hand.',u'04 · con vino')+
  slide('05','img/tralma/tralma-condensacion.jpg','Condensación','Condensation','Superficie fría','Cold surface',
        'El vidrio se escarcha y la greda no. Dos materiales, dos comportamientos térmicos, un mismo cuerpo.',
        'The glass frosts over and the clay doesn\'t. Two materials, two thermal behaviors, one body.','05 · condensación')+
  slide('06','img/tralma/tralma-encaje.jpg','Encaje','The fit','Detalle','Detail',
        'La greda envuelve el vidrio por debajo y lo retiene por forma. El encaje es el mismo principio de Engarce, en otra escala.',
        'The clay wraps the glass from below and holds it by form. The fit is Engarce\'s principle, at another scale.','06 · encaje')),
 ficha=ficha([
  ('Línea','Line','Cristalería contemporánea · 2020','Contemporary glassware · 2020'),
  ('Materialidad','Materiality','Greda de Pomaire colada + borosilicato soplado a boca','Cast Pomaire clay + mouth-blown borosilicate'),
  ('Unión','Union','Mecánica, con frontera visible entre materiales.','Mechanical, with a visible border between materials.'),
  ('Diseño','Design','Raúl Hernández Tralma','Raúl Hernández Tralma'),
  ('Greda','Clay','Raúl Hernández Tralma con el maestro Javier Neira','Raúl Hernández Tralma with master Javier Neira'),
  ('Vidrio','Glass','Maestro Francisco Saitua · La Vidriería','Master Francisco Saitua · La Vidriería'),
  ('Dimensiones','Dimensions','Referenciales. La greda natural varía entre piezas.','Referential. Natural clay varies between pieces.'),
  ('Respaldo','Backing','Fondart Nacional · Folio 549584','National Fondart · Folio 549584'),
 ])))

# ---------- LUMINARIAS
P.append(dict(
 slug='luminarias-trufquen.html', title='Luminarias',
 l2_es='El collar de cobre no es un remate decorativo: es la pieza que resuelve el encuentro entre un material que se contrae al cocer y un sistema eléctrico que exige medidas exactas.',
 l2_en="The copper collar isn't a decorative finish: it's the part that resolves the meeting between a material that shrinks when fired and an electrical system that demands exact measurements.",
 c_idx_es='Alcance',
 c_idx_en='Scope',
 c_t_es='Lo que la luz<br>dejó instalado',
 c_t_en='What the light<br>left in place',
 c_a_es='Aquí el estudio aprendió a tratar la greda como material con comportamiento óptico, no solo estructural. Entender cuánta luz atraviesa un espesor de arcilla es lo que después permitió leer la frontera greda–vidrio en las otras líneas.',
 c_a_en='Here the studio learned to treat clay as a material with optical behavior, not just structural. Understanding how much light passes through a thickness of clay is what later made it possible to read the clay–glass border in the other lines.',
 c_b_es='Es también la línea más doméstica. No exige pedestal ni vitrina: se cuelga sobre una mesa y se enciende todos los días. La prueba de que el sistema resiste el uso cotidiano, no solo la exhibición.',
 c_b_en="It's also the most domestic line. It demands no pedestal or vitrine: it hangs over a table and is switched on every day. Proof that the system withstands daily use, not just exhibition.",
 quote_es='La greda apagada es tierra: mate, porosa, fría. Encendida se vuelve un cuerpo cálido que retiene la luz en su espesor antes de soltarla.',
 quote_en='Unlit, the clay is earth: matte, porous, cold. Lit, it becomes a warm body that holds light in its thickness before releasing it.',
 meta='Luminarias Trufquén: piezas de iluminación donde la greda deja de contener la luz y pasa a filtrarla.',
 hero='img/luminarias/hero.jpg', heropos='center 45%',
 h1_es='Luminarias', h1_en='Lighting',
 hp_es='La greda deja de contener la luz: <span class="em">la filtra.</span> El espesor y el calado deciden cuánta sale.',
 hp_en='The clay stops containing light: <span class="em">it filters it.</span> Thickness and perforation decide how much escapes.',
 idx_es='2018 — Serie', idx_en='2018 — Series',
 t_es='Lo que define la pieza<br>no es la greda que está:<br><span class="em">es la que se quitó.</span>',
 t_en="What defines the piece<br>isn't the clay that's there:<br><span class=\"em\">it's the clay removed.</span>",
 l_es='Un calado demasiado abierto encandila; uno demasiado cerrado no ilumina. Entre esos dos fracasos hay un rango angosto que no se calcula: se prueba encendiendo la pieza.',
 l_en="A perforation too open glares; too closed lights nothing. Between those two failures lies a narrow range that isn't calculated: it's tested by switching the piece on.",
 plate='img/luminarias/plate-esfera.jpg', plate_alt='Luminaria esférica encendida', plate_cap='Cuerpo de greda · collar de cobre',
 g_es='Una familia, varias escalas', g_en='One family, several scales',
 slides=(
  slide('01','img/luminarias/lum-01-racimo.jpg','Racimo','Cluster','Tres cuerpos suspendidos','Three suspended bodies',
        'Tres esferas de greda colgando del mismo punto. La luz de una lava la superficie de la otra.',
        'Three clay spheres hanging from the same point. The light of one washes the surface of the next.','01 · racimo')+
  slide('02','img/luminarias/lum-02-anillo.jpg','Anillo de cobre','Copper ring','Encuentro con el difusor','Meeting the diffuser',
        'El cobre acepta la variación de la greda; la greda no acepta la del cobre. El ajuste ocurre siempre del lado del metal.',
        "Copper accepts clay's variation; clay doesn't accept copper's. The adjustment always happens on the metal's side.",'02 · anillo de cobre')+
  slide('03','img/luminarias/lum-03-sobremesa.jpg','Sobremesa','Table lamp','Luz rasante','Grazing light',
        'Apoyada, la boca queda casi a ras de la mesa. La luz sale lateral y revela la textura de lo que toca.',
        'Resting, the aperture sits nearly flush with the table. Light exits sideways and reveals the texture of what it touches.','03 · sobremesa')+
  slide('04','img/luminarias/lum-04-difusor.jpg','Boca de salida','Aperture','Difusor a la vista','Diffuser exposed',
        'El diámetro de la boca es la variable que más pesa: decide cuánta luz escapa sin filtrar.',
        'The aperture diameter is the heaviest variable: it decides how much light escapes unfiltered.','04 · boca de salida')+
  slide('05','img/luminarias/lum-05-gota.jpg',u'En reposo','At rest',u'Racimo apagado, luz de día','Cluster off, daylight',
        u'Apagada, la luminaria sigue siendo greda: volumen, textura y cobre a plena luz. El objeto no depende de la ampolleta.',
        'Switched off, the light is still clay: volume, texture and copper in daylight. The object does not depend on the bulb.',u'05 · en reposo')+
  slide('06','img/luminarias/lum-06-cobre.jpg','Collares','Collars','El sistema desde abajo','The system from below',
        'Desde abajo se ve el sistema completo: cuerpo de greda, collar de cobre y el punto donde ambos se encuentran.',
        'From below the whole system is visible: clay body, copper collar and the point where the two meet.','06 · collares')),
 ficha=ficha([
  ('Serie','Series','Iluminación · en producción','Lighting · in production'),
  ('Materialidad','Materiality','Greda de Pomaire + collar y remates en cobre','Pomaire clay + copper collar and fittings'),
  ('Principio','Principle','La luz se regula por espesor de pared, calado y diámetro de boca.','Light is regulated by wall thickness, perforation and aperture diameter.'),
  ('Formatos','Formats','Colgante individual · racimo · sobremesa','Individual pendant · cluster · table lamp'),
  ('Diseño','Design','Raúl Hernández Tralma','Raúl Hernández Tralma'),
  ('Dimensiones','Dimensions','Referenciales. La greda natural varía entre piezas.','Referential. Natural clay varies between pieces.'),
 ])))

# ---------- PROBETAS
P.append(dict(
 slug='probetas-trufquen.html', title='Probetas',
 l2_es='Dos materiales de comportamiento opuesto: una arcilla que ya pasó por el fuego y quedó rígida, y un vidrio que llega incandescente y quiere seguir moviéndose. Al encontrarse, uno de los dos cede. La pregunta no era si se podían unir, sino bajo qué condiciones exactas la greda no se quiebra. El taller no es un estudio fotográfico y estas imágenes no lo disimulan: el registro se hizo en el momento del ensayo, no después.',
 l2_en="Two materials with opposite behavior: a clay that has been through fire and is now rigid, and a glass that arrives incandescent and wants to keep moving. When they meet, one gives way. The question wasn't whether they could join, but under exactly what conditions the clay doesn't crack. The workshop isn't a photo studio and these images don't hide it: the record was made at the moment of the trial, not afterward.",
 c_idx_es='Lo que se estableció',
 c_idx_en='What was established',
 c_t_es='Tres hallazgos que aún<br>gobiernan el estudio',
 c_t_en='Three findings that still<br>govern the studio',
 c_a_es='La cohesión es posible, y es mecánica: el vidrio queda tomado por forma —perforación, relieve o anillo—. La temperatura es una variable de diseño, no una condición del taller: el diferencial térmico define qué formas resisten.',
 c_a_en='Cohesion is possible, and it is mechanical: the glass is held by form —perforation, relief or ring—. Temperature is a design variable, not a workshop condition: the thermal differential defines which forms hold.',
 c_b_es='Y la greda funciona como matriz: es molde y estructura a la vez. Esa doble función es lo que permitió, después, soplar más de un tipo de vidrio contra ella. Todo lo que vino después está construido sobre estas tres frases.',
 c_b_en='And clay works as a matrix: mold and structure at once. That double function is what later made it possible to blow more than one type of glass against it. Everything that came after is built on these three sentences.',
 quote_es='Sin las probetas no hay sistema: hay suerte. El archivo no es un recuerdo, es el procedimiento — cada material nuevo vuelve a pasar por aquí antes de convertirse en pieza.',
 quote_en="Without the test pieces there is no system: there is luck. The archive isn't a memory, it's the procedure — every new material passes through here again before becoming a piece.",
 meta='Probetas Trufquén: el archivo de ensayo que probó que la cohesión greda–vidrio es posible. Fondart Nacional, folio 406861.',
 hero='img/probetas/hero.jpg', heropos='center 45%',
 h1_es='Probetas', h1_en='Test pieces',
 hp_es='El año en que dejamos de suponer. Esto no es una colección: <span class="em">es la evidencia.</span>',
 hp_en="The year we stopped assuming. This isn't a collection: <span class=\"em\">it's the evidence.</span>",
 idx_es='2017 — Fondart · Folio 406861', idx_en='2017 — Fondart · Folio 406861',
 t_es='Muchas fallaron.<br>Las que fallaron entregaron<br><span class="em">tanta información como las que resistieron.</span>',
 t_en='Many failed.<br>The ones that failed gave<br><span class="em">as much information as the ones that held.</span>',
 l_es='Cada probeta es una variable movida a propósito: espesor de pared, geometría del calado, tamaño de la abertura, momento térmico del vidrio. La única forma de saberlo era hacerlo y mirar.',
 l_en="Each test piece is one variable moved on purpose: wall thickness, perforation geometry, opening size, the glass's thermal moment. The only way to know was to do it and look.",
 plate='img/probetas/plate-soplado.jpg', plate_alt='Vidrio incandescente soplado dentro de la greda calada', plate_cap='El ensayo en curso',
 g_es='Seis ensayos del conjunto', g_en='Six trials from the set',
 slides=(
  slide('01','img/probetas/pr-01-calada.jpg','Pantalla calada','Perforated screen','Antes del vidrio','Before the glass',
        'La matriz sola. El calado define por dónde podrá salir el vidrio y cuánta pared queda para resistir el empuje.',
        'The matrix alone. The perforation defines where the glass can emerge and how much wall remains to resist the push.','PR·01 · pantalla calada')+
  slide('02','img/probetas/pr-02-domo.jpg','Domo sobre ranura','Dome over slot','Anclaje lateral','Lateral anchoring',
        'El vidrio se expande hacia arriba y escapa por las ranuras laterales. El anclaje ocurre fuera del eje.',
        'The glass expands upward and escapes through lateral slots. Anchoring happens off-axis.','PR·02 · domo sobre ranura')+
  slide('03','img/probetas/pr-03-gota.jpg','Gota por calado','Droplet through perforation','Presión controlada','Controlled pressure',
        'El vidrio sale por la abertura y forma una lente. Hallazgo: la greda no se rompe si la abertura es menor que la masa que la rodea.',
        "The glass emerges and forms a lens. Finding: the clay doesn't break if the opening is smaller than the surrounding mass.",'PR·03 · gota por calado')+
  slide('04','img/probetas/pr-04-relieve.jpg','Relieve','Relief','El vidrio como ojo','Glass as eye',
        'Tres salidas simétricas en un mismo cuerpo. La simetría reparte el empuje para que ninguna pared reciba toda la carga.',
        'Three symmetrical outlets in one body. Symmetry distributes the push so no single wall takes the whole load.','PR·04 · relieve')+
  slide('05','img/probetas/pr-05-frontera.jpg',u'La frontera','The border',u'Greda y vidrio en la boca','Clay and glass at the mouth',
        u'El detalle que lo probó todo: el vidrio se derrama sobre el labio de greda y se ancla sin fundirse. La unión es mecánica, y aquí se ve.',
        'The detail that proved everything: glass spills over the clay lip and anchors without melting. The union is mechanical, and here you can see it.',u'PR·05 · la frontera')+
  slide('06','img/probetas/pr-06-torno.jpg','Asas de vidrio','Glass handles','El ensayo en el torno','The trial on the lathe',
        'El vidrio sale por dos costados y forma asas. La pieza queda sobre el torno: el registro se toma sin mover la evidencia.',
        'The glass emerges from two sides and forms handles. The piece stays on the lathe: the record is taken without moving the evidence.','PR·06 · asas de vidrio')),
 ficha=ficha([
  ('Etapa','Stage','Investigación 2017 · Fondart Nacional, folio 406861','Research 2017 · National Fondart, folio 406861'),
  ('Materiales','Materials','Greda roja de Pomaire · cristal sonoro · borosilicato','Pomaire red clay · sonorous crystal · borosilicate'),
  ('Unión','Union','Mecánica. Determinada por ensayo, no por literatura.','Mechanical. Determined by trial, not by literature.'),
  ('Análisis','Analysis','Incluyó análisis de materias primas con laboratorio independiente.','Included raw material analysis with an independent laboratory.'),
  ('Dirección','Direction','Raúl Hernández Tralma','Raúl Hernández Tralma'),
  ('Registro','Record','Fotografía tomada en taller durante el ensayo. No es fotografía de producto.','Photography taken in the workshop during the trial. Not product photography.'),
 ])))

# ---------- AHUMADOR  (solo 4 fotos reales -> 2 marcadores)
P.append(dict(
 slug='ahumador-trufquen.html', title='Ahumador',
 l2_es='Astillas de madera en la base, alimento sobre parrilla de acero, y una cámara de greda que concentra humo y calor en un solo gesto. La forma nace de una matriz geométrica de la iconografía mapuche —el rombo del Pichikemenküe— convertida en sección constructiva: dos cuerpos que calzan mediante una pestaña perimetral, sellando la cámara sin herrajes ni juntas sintéticas.',
 l2_en='Wood chips at the base, food on a steel grill, and a clay chamber that concentrates smoke and heat in a single gesture. The form is born from a geometric matrix of Mapuche iconography —the Pichikemenküe rhombus— turned into a constructive section: two bodies fitting through a perimeter flange, sealing the chamber without hardware or synthetic joints.',
 c_idx_es='Probado en cocina profesional',
 c_idx_en='Tested in professional kitchens',
 c_t_es='El control vuelve<br>a manos del cocinero',
 c_t_en="Control returns<br>to the cook's hands",
 c_a_es='Validado en las cocinas de una escuela profesional de gastronomía: control de temperatura por el orificio de la tapa y cocción directa a la llama. Las observaciones de ese ensayo definieron la parrilla de acero y el sistema de cierre definitivos.',
 c_a_en="Validated in the kitchens of a professional culinary school: temperature control through the lid's opening and direct-flame cooking. The observations from that trial defined the final steel grill and closing system.",
 c_b_es='Una segunda validación en servicio real confirmó el aroma y el sabor ahumado en preparación directa al fuego, con un tamaño calificado como apropiado para cocina de servicio. La pieza no se probó en un laboratorio: se probó cocinando.',
 c_b_en="A second validation in real service confirmed the smoked aroma and flavor in direct-fire preparation, with a size rated appropriate for service kitchens. The piece wasn't tested in a lab: it was tested by cooking.",
 quote_es='La geometría que previene fisuras en la cocción es la misma que define el carácter del objeto. El nombre del estudio nace aquí: trufquén, ceniza en mapuzungun.',
 quote_en="The geometry that prevents cracking during firing is the same one that defines the object's character. The studio's name is born here: trufquén, ash in Mapuzungun.",
 meta='Ahumador Trufquén: el artefacto de greda de Pomaire que origina el estudio. Cocción y ahumado en un solo objeto. Invención registrada en INAPI.',
 hero='img/ahumador/hero.jpg', heropos='center 55%',
 h1_es='Ahumador', h1_en='Smoking vessel',
 hp_es='Cocina y ahúma en un solo cuerpo de greda, sobre la llama de una cocina convencional. <span class="em">La invención que origina el estudio.</span>',
 hp_en='Cooks and smokes in a single clay body, over a conventional stove flame. <span class="em">The invention that originates the studio.</span>',
 idx_es='2014 — Patente INAPI', idx_en='2014 — INAPI patent',
 t_es='Ahumar dentro de la cocina,<br><span class="em">no fuera de ella.</span>',
 t_en='Smoking inside the kitchen,<br><span class="em">not outside it.</span>',
 l_es='Hasta este artefacto, ahumar exigía cámaras externas o esencias artificiales. El control vuelve al cocinero: intensidad, color y punto se regulan en el mismo objeto.',
 l_en='Until this device, smoking required external chambers or artificial essences. Control returns to the cook: intensity, color and doneness are regulated in the same object.',
 plate='img/ahumador/plate-torno.jpg', plate_alt='Greda levantada al torno en el taller alfarero', plate_cap='La greda se levanta al torno · taller alfarero',
 g_es='La misma greda, dos estados', g_en='The same clay, two states',
 slides=(
  slide('01','img/ahumador/ahumador-01-brunida.jpg','Greda natural bruñida','Burnished natural clay','Sellada con piedra de río','Sealed with river stone',
        'Sin recubrimientos. La superficie se impermeabiliza por fricción: es un sellado mecánico, no químico.',
        'No coatings. The surface is waterproofed by friction: a mechanical seal, not a chemical one.','01 · greda natural bruñida')+
  slide('02','img/ahumador/finish-negro.jpg','Esmaltada negra','Black glazed','Esmalte cerámico','Ceramic glaze',
        'La misma pieza, otro estado. El esmalte cambia la lectura del volumen sin tocar su geometría.',
        'The same piece, another state. The glaze changes how the volume reads without touching its geometry.','02 · esmaltada negra')+
  slide('03','img/ahumador/conjunto.jpg','El conjunto','The set','Platos bajos y platos base','Low plates and base plates',
        'Cocinar, servir y consumir ocurren en un mismo sistema material. La pieza va del fuego a la mesa sin trasvasije.',
        'Cooking, serving and eating happen within one material system. The piece goes from fire to table without transfer.','03 · el conjunto')+
  slide('04','img/ahumador/finish-natural.jpg','La cámara','The chamber','Tapa con pestaña de calce','Lid with fitting flange',
        'Dos cuerpos que calzan por una pestaña perimetral. El humo queda sellado sin herrajes ni juntas sintéticas.',
        'Two bodies fitting through a perimeter flange. The smoke is sealed without hardware or synthetic joints.','04 · la cámara')+
  slide('05','img/ahumador/ahumador-05-fuego.jpg',u'Sobre la llama','Over the flame','En uso, sobre brasas','In use, over embers',
        'El ahumador trabaja directo sobre las brasas: la greda va del fuego a la mesa sin intermediarios.',
        'The smoking vessel works directly over embers: the clay goes from fire to table with nothing in between.','05 · sobre la llama')+
  slide('06','img/ahumador/pichikemenkue-horizontal.png',u'Geometría de origen','Origin geometry',
        u'Rombo Pichikemenküe','Pichikemenküe rhombus',
        u'El rombo Pichikemenküe, iconografía mapuche. Su proyección horizontal define la sección constructiva del ahumador.',
        'The Pichikemenküe rhombus, Mapuche iconography. Its horizontal projection defines the constructive section of the smoking vessel.',
        u'Rombo Pichikemenküe — iconografía mapuche','sym')),
 ficha=ficha([
  ('Pieza','Piece','Pieza 0 · 2014 · origen del estudio','Piece 0 · 2014 · origin of the studio'),
  ('Material','Material','Greda de Pomaire. Verificada libre de plomo (ICP-OES).','Pomaire clay. Verified lead-free (ICP-OES).'),
  ('Geometría','Geometry','Matriz romboidal del Pichikemenküe, iconografía mapuche, llevada a sección constructiva.','Rhomboid matrix of the Pichikemenküe, Mapuche iconography, taken to constructive section.'),
  ('Componentes','Components','Base, tapa con pestaña de calce, parrilla de acero, asas.','Base, lid with fitting flange, steel grill, handles.'),
  ('Terminación','Finish','Bruñido con piedra de río o esmalte cerámico negro.','Burnished with river stone or black ceramic glaze.'),
  ('Diseño','Design','Raúl Hernández Tralma','Raúl Hernández Tralma'),
  ('Alfarería','Pottery','Rodrigo Veliz · Taller Barros, Pomaire','Rodrigo Veliz · Taller Barros, Pomaire'),
  ('Dimensiones','Dimensions','Aprox. Ø 260 × 215 mm. Referenciales: la greda natural varía.','Approx. Ø 260 × 215 mm. Referential: natural clay varies.'),
  ('Propiedad intelectual','Intellectual property','Invención registrada en INAPI, Chile.','Invention registered with INAPI, Chile.'),
 ])))

# ---------------------------------------------------------------- escribir
def hero_media(p):
    if p.get('hero_video'):
        poster = p.get('hero_poster', p['hero'])
        return ('<video src="%s" poster="%s" autoplay muted loop playsinline preload="auto" aria-label="%s" data-motion></video>'
                % (p['hero_video'], poster, p['h1_es']))
    return '<img src="%s" alt="%s">' % (p['hero'], p['h1_es'])

def plate_media(p):
    if p.get('plate_video'):
        return ('<video src="%s" poster="%s" autoplay muted loop playsinline preload="metadata" aria-label="%s" data-motion></video>'
                % (p['plate_video'], p['plate'], p['plate_alt']))
    return '<img src="%s" alt="%s" data-cap="%s" loading="lazy">' % (p['plate'], p['plate_alt'], p['plate_cap'])

for p in P:
    p['hero_media'] = hero_media(p)
    p['plate_media'] = plate_media(p)
    html = TPL.format(**p)
    with io.open(p['slug'], 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK  ' + p['slug'])
print('\n%d paginas generadas desde la misma plantilla.' % len(P))
