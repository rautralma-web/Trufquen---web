#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera las 5 páginas de línea de Trufquén desde UNA plantilla.
Garantiza header, footer, paleta y estructura idénticos en todas.
Ejecutar:  python3 _build.py
"""
import io, os
from PIL import Image

_SITE_DIR = os.path.dirname(os.path.abspath(__file__))
_size_cache = {}
def img_size(rel_path):
    if rel_path not in _size_cache:
        with Image.open(os.path.join(_SITE_DIR, rel_path)) as im:
            _size_cache[rel_path] = im.size
    return _size_cache[rel_path]

# ---------------------------------------------------------------- plantilla
TPL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Trufquén</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="https://trufquen.studio/{canonical_slug}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="img/brand/favicon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="img/brand/favicon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0A0908">
<meta property="og:title" content="{title} — Trufquén">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://trufquen.studio/{canonical_slug}">
<meta property="og:image" content="https://trufquen.studio/{og_image}">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="720">
<meta property="og:image:alt" content="{h1_es}">
<meta property="og:locale" content="es_CL">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Trufquén">
<meta name="twitter:description" content="{meta}">
<meta name="twitter:image" content="https://trufquen.studio/{og_image}">
<meta name="twitter:image:alt" content="{h1_es}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type":"ListItem","position":1,"name":"Trufquén","item":"https://trufquen.studio/"}},
    {{"@type":"ListItem","position":2,"name":"{title}","item":"https://trufquen.studio/{canonical_slug}"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "{title}",
  "description": "{meta}",
  "url": "https://trufquen.studio/{canonical_slug}",
  "image": "https://trufquen.studio/{og_image}",
  "creator": {{"@type":"Organization","name":"Trufquén","url":"https://trufquen.studio/"}}
}}
</script>
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
h1,h2,h3,.pull,.sheet a,.proj-nav-name{{font-family:'Archivo','Lato',sans-serif;font-stretch:125%}}
body{{font-family:'Lato',sans-serif;font-weight:300;background:var(--fondo);color:var(--mineral);line-height:1.75;-webkit-font-smoothing:antialiased}}
body.locked{{overflow:hidden}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
img{{display:block;max-width:100%}}
picture{{display:block}}
a{{color:inherit;text-decoration:none}}
.lang [data-en]{{display:none}}
.lang.en [data-es]{{display:none}}
.lang.en [data-en]{{display:inline}}
.lang.en [data-en].block{{display:block}}
.js-btn{{display:block;width:100%;border:0;padding:0;margin:0;background:none;font:inherit;text-align:inherit;color:inherit;-webkit-appearance:none;appearance:none}}
.js-btn:focus-visible{{outline:2px solid var(--cobre);outline-offset:2px}}
.video-toggle{{position:absolute;z-index:3;background:rgba(10,9,8,.55);backdrop-filter:blur(6px);border:1px solid rgba(240,235,227,.3);color:var(--mineral);width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:opacity .2s,background .2s}}
.video-toggle:hover{{background:rgba(10,9,8,.8)}}
.video-toggle svg{{width:16px;height:16px;fill:currentColor}}
.hero .video-toggle{{right:clamp(1.2rem,4vw,3rem);bottom:clamp(2.5rem,7vh,5rem)}}
.plate{{position:relative}}
.plate .video-toggle{{right:1.2rem;bottom:1.2rem}}

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

.rombo{{background:#000;text-align:center;padding:clamp(3rem,7vh,5rem) 0}}
.rombo img{{width:min(420px,70%);margin:0 auto;display:block}}
.rombo p{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.14em;color:var(--humo);text-transform:uppercase;margin-top:1.4rem;line-height:1.8}}
.gal{{padding:clamp(4rem,9vh,6rem) 0}}
.car{{display:flex;gap:2px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:0 clamp(1.4rem,5vw,3.5rem);cursor:grab}}
.car::-webkit-scrollbar{{display:none}}
.car.drag{{cursor:grabbing;scroll-snap-type:none}}
.car figure{{flex:0 0 {car_w};scroll-snap-align:center;margin:0;position:relative;overflow:hidden;background:var(--grafito)}}
.car img{{width:100%;aspect-ratio:{car_ar};object-fit:cover;transition:opacity .5s,transform 1s cubic-bezier(.2,.6,.2,1);opacity:.42}}
.car .ph{{width:100%;aspect-ratio:{car_ar};background:linear-gradient(155deg,#2a2018,#12100c 60%,#0c0a08);display:flex;align-items:center;justify-content:center;opacity:.42;transition:opacity .5s}}
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

.proj-nav{{border-top:1px solid var(--linea)}}
.proj-nav .wrap{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:1.5rem clamp(1rem,4vw,3rem);padding:clamp(2.5rem,6vh,4rem) clamp(1.4rem,5vw,3.5rem)}}
.proj-nav-link{{display:flex;flex-direction:column;gap:0.35rem}}
.proj-nav-prev{{align-items:flex-start;text-align:left}}
.proj-nav-next{{align-items:flex-end;text-align:right;order:3}}
.proj-nav-label{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:0.14em;text-transform:uppercase;color:var(--humo)}}
.proj-nav-name{{font-size:var(--fs-h3);font-weight:200;letter-spacing:0.02em;color:var(--mineral);transition:color .2s}}
.proj-nav-link:hover .proj-nav-name{{color:var(--cobre)}}
.proj-nav-all{{order:2;font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:0.14em;text-transform:uppercase;color:var(--cobre);border:1px solid var(--cobre);padding:0.85rem 1.6rem;min-height:44px;display:inline-flex;align-items:center;transition:all .25s}}
.proj-nav-all:hover{{background:var(--cobre);color:var(--grafito)}}
@media(max-width:640px){{.proj-nav .wrap{{flex-direction:column;text-align:center}}.proj-nav-prev{{order:1}}.proj-nav-all{{order:2}}.proj-nav-next{{order:3;align-items:center;text-align:center}}}}
footer{{position:relative;background:var(--grafito);color:var(--humo);padding:clamp(3rem,7vw,4.5rem) 0;text-align:center}}
footer::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(192,126,69,.65) 22%,rgba(192,126,69,.65) 78%,transparent)}}
footer .fbrand{{display:inline-flex;flex-direction:column;align-items:center;gap:.6rem;margin-bottom:1.5rem}}
footer .fbrand img{{height:44px}}
footer .fbrand span{{font-weight:200;letter-spacing:.42em;text-indent:.42em;text-transform:uppercase;color:var(--mineral);font-size:1.1rem}}
footer .social{{display:flex;justify-content:center;gap:1.2rem;margin-bottom:1.4rem}}
footer .social a{{color:var(--humo);transition:color .2s;display:inline-flex;min-width:44px;min-height:44px;align-items:center;justify-content:center}}
footer .social a:hover{{color:var(--cobre)}}
footer .social svg{{width:19px;height:19px}}
footer a{{font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:.14em;color:var(--humo);text-transform:uppercase;margin:0 .7rem;line-height:2.4}}
.fcontact{{margin-top:.4rem}}
.contact-dropdown{{display:inline-block}}
.contact-dropdown summary{{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:0.6rem;min-height:44px;padding:0.85rem 1.6rem;border:1px solid var(--cobre);color:var(--cobre);font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:0.14em;text-transform:uppercase;transition:all .25s}}
.contact-dropdown summary::-webkit-details-marker{{display:none}}
.contact-dropdown summary::after{{content:"+";font-size:1.1rem;line-height:1;transition:transform .25s}}
.contact-dropdown:hover summary,.contact-dropdown[open] summary{{background:var(--cobre);color:var(--grafito)}}
.contact-dropdown[open] summary::after{{transform:rotate(45deg)}}
.contact-dropdown-list{{display:flex;flex-direction:column;margin-top:0.6rem;border:1px solid var(--linea)}}
.contact-dropdown-list a{{display:flex;align-items:center;justify-content:center;min-height:44px;padding:0.9rem 1.4rem;font-family:'Space Mono',monospace;font-size:var(--fs-ui);letter-spacing:0.1em;text-transform:uppercase;color:var(--ceniza);border-top:1px solid var(--linea);transition:color .2s,background .2s}}
.contact-dropdown-list a:first-child{{border-top:none}}
.contact-dropdown-list a:hover{{color:var(--cobre);background:rgba(192,126,69,.08)}}
footer a:hover{{color:var(--cobre)}}
.legal{{font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:.08em;color:rgba(160,150,140,.85);line-height:1.9;text-transform:uppercase;margin-top:2rem;max-width:44rem;margin-left:auto;margin-right:auto;padding:0 1.5rem}}
.back-top{{position:absolute;top:clamp(1.5rem,4vw,2.5rem);right:clamp(1.2rem,4vw,3rem);display:inline-flex;align-items:center;gap:0.4rem;min-height:44px;font-family:'Space Mono',monospace;font-size:var(--fs-micro);letter-spacing:0.14em;text-transform:uppercase;color:var(--humo);transition:color .2s}}
.back-top:hover{{color:var(--cobre)}}

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
<body class="lang" id="top">
<a href="#contenido" class="skip"><span data-es>Saltar al contenido</span><span data-en>Skip to content</span></a>

<nav class="top" id="nav">
  <button class="menubtn" id="menuBtn" aria-expanded="false" aria-controls="sheet"><span data-es>Menú</span><span data-en>Menu</span></button>
  <a href="/" class="brand"><img src="img/brand/icon-blanco.png" width="300" height="130" alt=""><span class="word">Trufquén</span></a>
  <button class="langbtn" id="langBtn" aria-label="Cambiar idioma / Switch language">EN/ES</button>
</nav>

<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-label="Menú de navegación" data-label-es="Menú de navegación" data-label-en="Navigation menu" aria-hidden="true" inert>
  <button class="close" id="sheetClose"><span data-es>Cerrar</span><span data-en>Close</span></button>
  <nav>
    <a href="/"><span data-es>Inicio</span><span data-en>Home</span></a>
    <a href="ahumador-trufquen"><span data-es>Ahumador</span><span data-en>Smoking vessel</span></a>
    <a href="probetas-trufquen"><span data-es>Probetas</span><span data-en>Test pieces</span></a>
    <a href="engarce-trufquen">Engarce</a>
    <a href="luminarias-trufquen"><span data-es>Luminarias</span><span data-en>Lighting</span></a>
    <a href="tralma-trufquen">Tralma</a>
    <a href="/#contacto"><span data-es>Contacto</span><span data-en>Contact</span></a>
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
{rombo_section}
{plate_media}

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
        <button class="car-btn" id="btnPrev" aria-controls="car" aria-label="Pieza anterior" data-label-es="Pieza anterior" data-label-en="Previous piece">‹</button>
        <button class="car-btn" id="btnNext" aria-controls="car" aria-label="Pieza siguiente" data-label-es="Pieza siguiente" data-label-en="Next piece">›</button>
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

<section class="proj-nav">
  <div class="wrap">
    <a href="{prev_slug}" class="proj-nav-link proj-nav-prev" data-track="project_prev">
      <span class="proj-nav-label"><span data-es>← Proyecto anterior</span><span data-en>← Previous project</span></span>
      <span class="proj-nav-name"><span data-es>{prev_es}</span><span data-en>{prev_en}</span></span>
    </a>
    <a href="/#piezas" class="proj-nav-all"><span data-es>Volver a piezas</span><span data-en>Back to pieces</span></a>
    <a href="{next_slug}" class="proj-nav-link proj-nav-next" data-track="project_next">
      <span class="proj-nav-label"><span data-es>Proyecto siguiente →</span><span data-en>Next project →</span></span>
      <span class="proj-nav-name"><span data-es>{next_es}</span><span data-en>{next_en}</span></span>
    </a>
  </div>
</section>
</main>

<footer>
  <a href="#top" class="back-top"><span data-es>Volver arriba</span><span data-en>Back to top</span> ↑</a>
  <div class="fbrand"><img src="img/brand/icon-blanco.png" width="300" height="130" alt=""><span>Trufquén</span></div>
  <div class="social">
    <a href="https://instagram.com/trufquen" target="_blank" rel="noopener" aria-label="Instagram" data-track="social_instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg></a>
    <a href="https://facebook.com/Trufquen" target="_blank" rel="noopener" aria-label="Facebook" data-track="social_facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M13.6 21v-7.2h2.2l.3-2.6h-2.5v-1.6c0-.75.2-1.27 1.28-1.27h1.38V5.98c-.24-.03-1.06-.1-2-.1-2 0-3.36 1.22-3.36 3.46v1.93H8.6v2.6h2.32V21" fill="currentColor" stroke="none"/></svg></a>
  </div>
  <div>
    <a href="/"><span data-es>Inicio</span><span data-en>Home</span></a>
    <a href="https://trufquen.studio">trufquen.studio</a>
    <a href="https://instagram.com/trufquen">@trufquen</a>
  </div>
  <details class="contact-dropdown fcontact">
    <summary><span data-es>Escríbenos</span><span data-en>Write to us</span></summary>
    <div class="contact-dropdown-list">
      <a href="mailto:contacto@trufquen.studio?subject=Exposici%C3%B3n%20%E2%80%94%20Trufqu%C3%A9n" data-track="mailto_exposicion"><span data-es>Exposición</span><span data-en>Exhibition</span></a>
      <a href="mailto:contacto@trufquen.studio?subject=Colaboraci%C3%B3n%20%E2%80%94%20Trufqu%C3%A9n" data-track="mailto_colaboracion"><span data-es>Colaboración</span><span data-en>Collaboration</span></a>
      <a href="mailto:contacto@trufquen.studio?subject=Prensa%20%E2%80%94%20Trufqu%C3%A9n" data-track="mailto_prensa"><span data-es>Prensa</span><span data-en>Press</span></a>
      <a href="mailto:contacto@trufquen.studio?subject=Encargo%20o%20adquisici%C3%B3n%20%E2%80%94%20Trufqu%C3%A9n" data-track="mailto_encargo"><span data-es>Encargo o adquisición</span><span data-en>Commission or acquisition</span></a>
    </div>
  </details>
  <p class="legal"><span data-es>© 2026 Trufquén · Marca registrada INAPI N° 1391981 · Patente de invención INAPI N° 2015-01441 · Santiago de Chile</span><span data-en class="block">© 2026 Trufquén · Registered trademark INAPI No. 1391981 · INAPI invention patent No. 2015-01441 · Santiago, Chile</span></p>
</footer>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Vista ampliada de imagen" data-label-es="Vista ampliada de imagen" data-label-en="Enlarged image view" aria-hidden="true" inert>
  <button class="lb-x" id="lbX" aria-label="Cerrar" data-label-es="Cerrar" data-label-en="Close">✕</button>
  <button class="lb-nav lb-prev" id="lbPrev" aria-label="Imagen anterior" data-label-es="Imagen anterior" data-label-en="Previous image">‹</button>
  <img id="lbImg" alt="">
  <button class="lb-nav lb-next" id="lbNext" aria-label="Imagen siguiente" data-label-es="Imagen siguiente" data-label-en="Next image">›</button>
  <div class="lb-count" id="lbCount"></div>
  <div class="lb-cap" id="lbCap"></div>
  <div class="sr-only" id="lbAnnounce" aria-live="polite" aria-atomic="true"></div>
</div>

<script>
function ariaLang(){{var en=document.body.classList.contains('en');
  document.querySelectorAll('[data-label-es]').forEach(function(el){{el.setAttribute('aria-label',en?el.getAttribute('data-label-en'):el.getAttribute('data-label-es'))}});
  figs.forEach(function(f,i){{f.setAttribute('aria-label',('0'+(i+1)).slice(-2)+(en?' of ':' de ')+figs.length)}})}}
function toggleLang(){{var b=document.body;b.classList.toggle('en');document.documentElement.lang=b.classList.contains('en')?'en':'es';carPaint(carAt);ariaLang()}}
/* trampa de foco genérica para diálogos (menú y visor) */
function focusablesIn(container){{
  return [].slice.call(container.querySelectorAll('a[href],button:not([disabled]),[tabindex]:not([tabindex="-1"])'));
}}
function trapTab(container,e){{
  if(e.key!=='Tab')return;
  var f=focusablesIn(container); if(!f.length)return;
  var i=f.indexOf(document.activeElement);
  if(e.shiftKey && i<=0){{e.preventDefault();f[f.length-1].focus()}}
  else if(!e.shiftKey && i===f.length-1){{e.preventDefault();f[0].focus()}}
}}

var sheetEl=document.getElementById('sheet'), menuBtn=document.getElementById('menuBtn'), sheetPrevFocus=null;
function openSheet(){{
  sheetPrevFocus=document.activeElement;
  sheetEl.classList.add('open');sheetEl.removeAttribute('inert');sheetEl.setAttribute('aria-hidden','false');
  document.body.classList.add('locked');
  menuBtn.setAttribute('aria-expanded','true');document.getElementById('sheetClose').focus();
}}
function closeSheet(){{
  sheetEl.classList.remove('open');sheetEl.setAttribute('inert','');sheetEl.setAttribute('aria-hidden','true');
  document.body.classList.remove('locked');
  menuBtn.setAttribute('aria-expanded','false');if(sheetPrevFocus)sheetPrevFocus.focus();
}}
sheetEl.addEventListener('keydown',function(e){{trapTab(sheetEl,e)}});
menuBtn.addEventListener('click',openSheet);
document.getElementById('sheetClose').addEventListener('click',closeSheet);
document.getElementById('langBtn').addEventListener('click',toggleLang);
sheetEl.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',closeSheet)}});
(function(){{var n=document.getElementById('nav'),h=document.querySelector('.hero');
  new IntersectionObserver(function(e){{n.classList.toggle('solid',!e[0].isIntersecting)}},{{rootMargin:'-88% 0px 0px 0px'}}).observe(h)}})();

var car=document.getElementById('car'), figs=[].slice.call(car.querySelectorAll('figure')), carAt=0, snapping=false;
function slideW(){{return figs[0].getBoundingClientRect().width+2}}
function nearestIdx(){{
  var max=car.scrollWidth-car.clientWidth;
  if(car.scrollLeft<=1) return 0;
  if(car.scrollLeft>=max-1) return figs.length-1;
  var cr=car.getBoundingClientRect(), mid=cr.left+cr.width/2, best=0, bd=Infinity;
  figs.forEach(function(f,i){{var fr=f.getBoundingClientRect();var d=Math.abs((fr.left+fr.width/2)-mid);if(d<bd){{bd=d;best=i}}}});
  return best;
}}
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
var snapT=null;
function snapFree(){{snapping=false;var i=nearestIdx();if(i!==carAt){{carAt=i;carPaint(i)}}}}
function carTo(i,smooth){{carAt=i;snapping=true;clearTimeout(snapT);snapT=setTimeout(snapFree,600);car.scrollTo({{left:snapLeft(i),behavior:smooth===false?'auto':'smooth'}});carPaint(i)}}
function carGo(d){{carTo((carAt+d+figs.length)%figs.length)}}
car.addEventListener('scroll',function(){{
  if(snapping){{clearTimeout(snapT);snapT=setTimeout(snapFree,150);return}}
  var i=nearestIdx();
  if(i!==carAt){{carAt=i;carPaint(i)}}
}});
(function(){{
  var down=false,x0=0,s0=0,moved=0;
  car.addEventListener('mousedown',function(e){{down=true;moved=0;x0=e.pageX;s0=car.scrollLeft;car.classList.add('drag')}});
  window.addEventListener('mouseup',function(){{if(!down)return;down=false;car.classList.remove('drag');
    carTo(nearestIdx())}});
  car.addEventListener('mousemove',function(e){{if(!down)return;e.preventDefault();moved=Math.abs(e.pageX-x0);car.scrollLeft=s0-(e.pageX-x0)}});
  car.addEventListener('click',function(e){{if(moved>6){{e.preventDefault();e.stopPropagation()}}}},true);
}})();
window.addEventListener('resize',function(){{carTo(carAt,false)}});
document.getElementById('btnPrev').addEventListener('click',function(){{carGo(-1)}});
document.getElementById('btnNext').addEventListener('click',function(){{carGo(1)}});
carPaint(0);
ariaLang();

var lbSet=[],lbAt=0,lb=document.getElementById('lb'),lbImg=document.getElementById('lbImg'),lbPrevFocus=null,
    lbAnnounce=document.getElementById('lbAnnounce'),
    lbBg=[document.getElementById('nav'),document.getElementById('contenido'),document.querySelector('footer')];
function lbOpen(img){{
  lbPrevFocus=document.activeElement;
  lbSet=[].slice.call(document.querySelectorAll('.js-btn img'));lbAt=lbSet.indexOf(img);lbRender();
  lb.classList.add('open');lb.removeAttribute('inert');lb.setAttribute('aria-hidden','false');
  document.body.classList.add('locked');
  lbBg.forEach(function(el){{if(el)el.setAttribute('inert','')}});
  document.getElementById('lbX').focus();
}}
function lbRender(){{var im=lbSet[lbAt];if(!im)return;lbImg.src=im.currentSrc||im.src;lbImg.alt=im.alt||'';
  var cap=im.dataset.cap||im.alt||'';
  document.getElementById('lbCap').textContent=cap;
  document.getElementById('lbCount').textContent=(lbAt+1)+' / '+lbSet.length;
  var en=document.body.classList.contains('en');
  lbAnnounce.textContent=(lbAt+1)+(en?' of ':' de ')+lbSet.length+': '+cap;
}}
function lbGo(d){{lbAt=(lbAt+d+lbSet.length)%lbSet.length;lbRender()}}
function lbClose(){{
  lb.classList.remove('open');lb.setAttribute('inert','');lb.setAttribute('aria-hidden','true');
  document.body.classList.remove('locked');
  lbBg.forEach(function(el){{if(el)el.removeAttribute('inert')}});
  if(lbPrevFocus)lbPrevFocus.focus();
}}
document.getElementById('lbX').addEventListener('click',lbClose);
document.getElementById('lbPrev').addEventListener('click',function(){{lbGo(-1)}});
document.getElementById('lbNext').addEventListener('click',function(){{lbGo(1)}});
lb.addEventListener('keydown',function(e){{trapTab(lb,e)}});
document.addEventListener('click',function(e){{
  var t=e.target.closest('.js-btn');
  if(t){{var im=t.querySelector('img');if(im){{lbOpen(im)}}}}
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

/* control de pausa/reproducción + pausa automática fuera de pantalla */
var userPausedVideos=new WeakSet();
document.querySelectorAll('[data-video-toggle]').forEach(function(btn){{
  var vid=btn.parentElement.querySelector('video[data-motion]');
  if(!vid) return;
  function sync(){{
    var playing=!vid.paused;
    var ip=btn.querySelector('[data-icon-pause]'), ir=btn.querySelector('[data-icon-play]');
    if(ip)ip.style.display=playing?'block':'none';
    if(ir)ir.style.display=playing?'none':'block';
    var en=document.body.classList.contains('en');
    btn.setAttribute('aria-label',playing?(en?'Pause video':'Pausar video'):(en?'Play video':'Reproducir video'));
  }}
  btn.addEventListener('click',function(){{
    if(vid.paused){{vid.play();userPausedVideos.delete(vid)}}else{{vid.pause();userPausedVideos.add(vid)}}
  }});
  vid.addEventListener('play',sync); vid.addEventListener('pause',sync);
  sync();
}});
if('IntersectionObserver' in window){{
  var videoIO=new IntersectionObserver(function(entries){{
    entries.forEach(function(en){{
      var v=en.target;
      if(en.isIntersecting){{ if(!userPausedVideos.has(v)) v.play(); }}
      else {{ v.pause(); }}
    }});
  }},{{threshold:.25}});
  document.querySelectorAll('video[data-motion]').forEach(function(v){{videoIO.observe(v)}});
}}

if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches){{
  document.querySelectorAll('video[data-motion]').forEach(function(v){{v.pause();v.removeAttribute('autoplay');userPausedVideos.add(v)}});
}}

/* eventos de interacción (Zaraz) */
document.addEventListener('click', function(e){{
  var t = e.target.closest('[data-track]');
  if(t && window.zaraz) zaraz.track(t.dataset.track);
}});
</script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "af92bff511b04c5eb85a580f2dfcf333"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""

def pic(src, img_attrs, sizes=None):
    base, ext = src.rsplit('.', 1)
    w, h = img_size(src)
    small = w > 640 and os.path.exists(os.path.join(_SITE_DIR, base + '-640.' + ext))
    if small:
        sz = sizes or '100vw'
        avif_src = '%s-640.avif 640w, %s.avif %dw' % (base, base, w)
        webp_src = '%s-640.webp 640w, %s.webp %dw' % (base, base, w)
        img_src = '%s-640.%s 640w, %s %dw' % (base, ext, src, w)
        return ('<picture><source srcset="%s" sizes="%s" type="image/avif">'
                '<source srcset="%s" sizes="%s" type="image/webp">'
                '<img src="%s" srcset="%s" sizes="%s" width="%d" height="%d" %s></picture>'
                % (avif_src, sz, webp_src, sz, src, img_src, sz, w, h, img_attrs))
    return ('<picture><source srcset="%s.avif" type="image/avif"><source srcset="%s.webp" type="image/webp">'
            '<img src="%s" width="%d" height="%d" %s></picture>' % (base, base, src, w, h, img_attrs))

def slide(n, img, t_es, t_en, s_es, s_en, d_es, d_en, cap, fig_class=''):
    inner = ('<button type="button" class="js-btn" aria-label="Ampliar imagen: %s" data-label-es="Ampliar imagen: %s" data-label-en="Enlarge image: %s">%s</button>'
              % (t_es, t_es, t_en, pic(img, 'alt="%s" data-cap="%s" loading="lazy"' % (t_es, cap), sizes='(max-width:760px) 100vw, 60vw'))) if img else \
            '<div class="ph"><span>Imagen pendiente</span></div>'
    cls = (' class="%s"' % fig_class) if fig_class else ''
    return ('    <figure%s role="group" aria-roledescription="slide" aria-label="%s de 6" data-n="%s" data-t-es="%s" data-t-en="%s" data-s-es="%s" data-s-en="%s" data-d-es="%s" data-d-en="%s">\n      %s\n    </figure>\n'
            % (cls, n, n, t_es, t_en, s_es, s_en, d_es, d_en, inner))

def ficha(rows):
    return ''.join('        <div><dt><span data-es>%s</span><span data-en>%s</span></dt><dd><span data-es>%s</span><span data-en>%s</span></dd></div>\n'
                   % r for r in rows)

# ---------------------------------------------------------------- datos
LINE_ORDER = [
    ('ahumador-trufquen', 'Ahumador', 'Smoking vessel'),
    ('probetas-trufquen', 'Probetas', 'Test pieces'),
    ('engarce-trufquen', 'Engarce', 'Engarce'),
    ('luminarias-trufquen', 'Luminarias', 'Lighting'),
    ('tralma-trufquen', 'Tralma', 'Tralma'),
]

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
 quote_es='Sabemos dónde y cuándo el vidrio incandescente puede expandirse contra la arcilla sin quebrarla. Ese punto no está en un manual: lo aprendimos probándolo pieza por pieza, durante años, hasta poder repetirlo.',
 quote_en="We know where and when incandescent glass can expand against the clay without cracking it. That point isn't in a manual: we learned it testing it piece by piece, over years, until we could repeat it.",
 meta='Engarce: once piezas únicas de greda de Pomaire y cristal soplado a boca. La unión es mecánica, no fusión.',
 hero='img/engarce/engarce-hero-poster.jpg', hero_video='img/engarce/engarce-hero.mp4', hero_poster='img/engarce/engarce-hero-poster.jpg', heropos='center 55%',
 car_ar='2 / 3', car_w='clamp(240px,42vw,440px)',
 h1_es='Engarce', h1_en='Engarce',
 hp_es='El cristal se expande contra la greda y queda retenido por forma. La unión es mecánica, <span class="em">no una fusión.</span>',
 hp_en='Glass expands against the clay and is held by form. The union is mechanical, <span class="em">not a fusion.</span>',
 idx_es='2018 — 11 piezas únicas', idx_en='2018 — 11 unique pieces',
 t_es='En joyería, engarzar es sujetar<br>una piedra <span class="em">sin fundirla.</span>',
 t_en='In jewelry, to set a stone is to hold it<br><span class="em">without melting it.</span>',
 l_es='El nombre no es metáfora: es la descripción técnica exacta. El cristal ancla por perforación, relieve o anillo. Donde la greda es lisa, se desprende.',
 l_en="The name isn't a metaphor: it's the exact technical description. The glass anchors by perforation, relief or ring. Where the clay is smooth, it detaches.",
 plate='img/engarce/plate-material.jpg', plate_alt='La serie Engarce completa sobre banco de taller', plate_alt_en='The complete Engarce series on the workshop bench', plate_cap='Once piezas · la serie completa',
 g_es='Once piezas, una misma tesis', g_en='Eleven pieces, one thesis',
 slides=(
  slide('01','img/engarce/serie-01.jpg',u'Horqueta','Fork',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Una horqueta de greda muerde la base del cristal. El vidrio se expandió contra ella y quedó retenido por la forma.',
        'A clay fork bites the base of the crystal. The glass expanded against it and was held by form.',u'01 · horqueta')+
  slide('02','img/engarce/serie-02.jpg',u'Balance','Balance',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'El cuerpo de vidrio descansa sobre una barra de greda. El punto de apoyo es también el punto de anclaje.',
        'The glass body rests on a clay bar. The support point is also the anchor point.',u'02 · balance')+
  slide('03','img/engarce/serie-03.jpg',u'Abrazo','Embrace',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Un brazo de greda envuelve el cristal por el costado. La curva sigue la pared de vidrio sin tocar su boca.',
        'A clay arm wraps the crystal from the side. The curve follows the glass wall without touching its mouth.',u'03 · abrazo')+
  slide('04','img/engarce/serie-04.jpg',u'Disco','Disc',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Un disco macizo de greda corona el cristal. El vidrio se estrecha bajo su peso y lo sostiene desde abajo.',
        'A solid clay disc crowns the crystal. The glass narrows under its weight and holds it from below.',u'04 · disco')+
  slide('05','img/engarce/serie-05.jpg',u'Gancho','Hook',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Un gancho de greda entra por la base y ancla al interior. La unión es mecánica, sin adhesión química.',
        'A clay hook enters through the base and anchors inside. The union is mechanical, with no chemical adhesion.',u'05 · gancho')+
  slide('06','img/engarce/serie-06.jpg',u'Óvalo','Oval',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Un óvalo de greda se hunde en el flanco del cristal. El vidrio se cerró sobre él en caliente y lo dejó preso.',
        'A clay oval sinks into the crystal flank. The glass closed over it while hot and trapped it.',u'06 · óvalo')+
  slide('07','img/engarce/serie-07.jpg',u'Envolvente','Wrap',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'La greda recorre el cristal en diagonal. Donde la pared es lisa el contacto es firme; donde no, se desprendería.',
        'The clay runs across the crystal diagonally. Where the wall is smooth the contact holds; where not, it would detach.',u'07 · envolvente')+
  slide('08','img/engarce/serie-08.jpg',u'Trípode','Tripod',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Tres puntos de greda sostienen el cuerpo esférico. El equilibrio nace del reparto del peso, no de un pegamento.',
        'Three clay points support the spherical body. Balance comes from weight distribution, not from glue.',u'08 · trípode')+
  slide('09','img/engarce/serie-09.jpg',u'Flecha','Arrow',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Una flecha de greda atraviesa el cristal de lado a lado. El calado retiene la pieza por ambas paredes.',
        'A clay arrow crosses the crystal side to side. The perforation retains the piece through both walls.',u'09 · flecha')+
  slide('10','img/engarce/serie-10.jpg',u'Disco texturado','Textured disc',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'Un disco de greda con textura envuelve el cristal por el centro. La rugosidad aumenta la superficie de agarre.',
        'A textured clay disc wraps the crystal at the center. The roughness increases the grip surface.',u'10 · disco texturado')+
  slide('11','img/engarce/serie-11.jpg',u'Perforación','Perforation',u'Greda de Pomaire + cristal soplado','Pomaire clay + blown crystal',
        u'El cristal atraviesa una placa calada que lo envuelve y ancla al otro lado. La greda no se rompe: la abertura es menor que su masa.',
        "The glass crosses a perforated plate that wraps it and anchors on the far side. The clay doesn't break: the opening is smaller than its mass.",u'11 · perforación')),
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
 l2_es='Lo que en 2019 se planteó como una vinculación estable entre alfarería de Pomaire y soplado a boca, en 2020 se resolvió como investigación de contingencia. CristalArt era la última empresa del país capaz de soplar a escala de proyecto. Su cierre nos dejó sin el oficio que sostenía la técnica, y obligó a rediseñar el proceso sin abandonar la tesis.',
 l2_en="What in 2019 was proposed as a stable link between Pomaire pottery and mouth-blowing was resolved in 2020 as contingency research. CristalArt was the country's last company able to blow at project scale. Its closure left us without the craft that sustained the technique, and forced a redesign of the process without abandoning the thesis.",
 c_idx_es='Alcance',
 c_idx_en='Scope',
 c_t_es='Un resultado logrado<br>bajo presión real',
 c_t_en='A result achieved<br>under real pressure',
 c_a_es='Tralma entregó lo que se propuso —piezas de uso que unen greda y vidrio soplado a boca— reconstruyendo su base productiva a mitad de camino. Producción 100% a mano, pieza a pieza. La complejidad del contexto no rebajó el resultado: lo volvió más difícil de replicar.',
 c_a_en="Tralma delivered what it set out to do —usable pieces uniting clay and mouth-blown glass— while rebuilding its production base halfway through. 100% handmade, piece by piece. The context's complexity didn't lower the result: it made it harder to replicate.",
 c_b_es='Demostró que la técnica no depende de un único vidrio ni de un único proveedor. Esa versatilidad amplía el trabajo futuro y es, en la práctica, una barrera para quien intente copiar el resultado sin el proceso detrás.',
 c_b_en="It proved the technique doesn't depend on a single glass or a single supplier. That versatility broadens future work and is, in practice, a barrier for anyone trying to copy the result without the process behind it.",
 quote_es='Sabemos hacer esto; y sabemos rehacerlo cuando el terreno se mueve. Esa capacidad —no una copa en particular— es lo que la línea deja instalado.',
 quote_en='We know how to do this; and we know how to redo it when the ground shifts. That capacity —not any one cup— is what the line leaves in place.',
 meta='Tralma: greda colada y vidrio borosilicato soplado a boca. La línea que sobrevivió al cierre de la última cristalería del país.',
 hero='img/tralma/tralma-hero-poster.jpg', hero_video='img/tralma/tralma-fabricacion.mp4', hero_poster='img/tralma/tralma-hero-poster.jpg', heropos='center 45%',
 h1_es='Tralma', h1_en='Tralma',
 hp_es='Apellido materno del diseñador. Greda colada y borosilicato soplado a boca: la línea que <span class="em">sobrevivió a la desaparición de un oficio.</span>',
 hp_en="The designer's maternal surname. Cast clay and mouth-blown borosilicate: the line that <span class=\"em\">survived a craft's disappearance.</span>",
 idx_es='2020 — Cristalería', idx_en='2020 — Glassware',
 t_es='A mitad de camino cerró<br>la última cristalería <span class="em">del país.</span>',
 t_en='Halfway through, the country\'s<br>last glassworks <span class="em">closed.</span>',
 l_es='En vez de abandonar la hipótesis, le buscamos un sustrato nuevo: borosilicato en lugar de cristal sonoro. La distancia entre lo postulado y lo ejecutado es, en sí misma, el hallazgo. Sobre ese sustrato controlamos también la superficie: piezas lisas y piezas con textura, impresa en el molde, no por condensación.',
 l_en='Instead of abandoning the hypothesis, we found a new substrate for it: borosilicate instead of sonorous crystal. The distance between what was proposed and what was executed is, in itself, the finding. On that substrate we also control the surface: smooth pieces and textured ones, printed by the mould, not by condensation.',
 plate='img/tralma/copa-giro-poster.jpg', plate_video='img/tralma/copa-giro.mp4', plate_alt='Copa Tralma girando: borosilicato sobre base de greda colada', plate_alt_en='Tralma cup turning: borosilicate over a cast clay base', plate_cap='La copa terminada',
 g_es='Producción real, no render', g_en='Real production, not a render',
 slides=(
  slide('01','img/tralma/tralma-01-soplado.jpg',u'Soplado a la llama',u'Flame-blown',u'Borosilicato en formación','Borosilicate in the making',
        u'El maestro trabaja el borosilicato al soplete. La copa se forma en caliente, punto por punto, sin molde que la guíe.',
        u'The master works the borosilicate at the torch. The cup is formed hot, point by point, with no mould to guide it.',u'01 · soplado a la llama')+
  slide('02','img/tralma/tralma-02-copa.jpg',u'La copa',u'The cup',u'Borosilicato + greda colada','Borosilicate + cast clay',
        u'El cuerpo de vidrio se sopla contra la greda ya colada. La base no es un añadido: es la matriz que le dio forma.',
        u'The glass body is blown against the already-cast clay. The base is not an addition: it is the matrix that shaped it.',u'02 · la copa')+
  slide('03','img/tralma/tralma-03-vino.jpg',u'Con vino',u'With wine',u'La pieza en uso','The piece in use',
        u'Llena, la copa se lee entera: el vino ocupa el vidrio y la greda lo sostiene desde abajo. El peso equilibra la mano.',
        u'Filled, the cup reads whole: the wine occupies the glass and the clay holds it from below. The weight balances the hand.',u'03 · con vino')+
  slide('04','img/tralma/tralma-04-textura.jpg',u'Textura en el vidrio',u'Texture in the glass',u'Borosilicato + greda colada','Borosilicate + cast clay',
        u'Logramos imprimir textura en el borosilicato sin perder transparencia. No es condensación: es la textura impresa en el molde. La base es greda, no metal.',
        u"We achieved texture on the borosilicate without losing transparency. It isn't condensation: it's texture printed by the mould. The base is clay, not metal.",u'04 · textura en el vidrio')+
  slide('05','img/tralma/tralma-05-liso-textura.jpg',u'Lisas y con textura',u'Smooth and textured',u'Misma línea, dos terminaciones','Same line, two finishes',
        u'La misma copa admite dos terminaciones de superficie: lisa o texturada. Controlamos ambas sobre la misma base de greda colada.',
        u'The same cup admits two surface finishes: smooth or textured. We control both on the same cast clay base.',u'05 · lisas y con textura')+
  slide('06','img/tralma/tralma-06-uso.jpg',u'Condensación',u'Condensation',u'Superficie fría','Cold surface',
        u'El vidrio se escarcha y la greda no. Dos materiales, dos comportamientos térmicos, un mismo cuerpo en la mano.',
        u'The glass frosts over and the clay does not. Two materials, two thermal behaviors, one body in the hand.',u'06 · condensación')),
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
 c_a_es='Esta línea fijó también una particularidad del estudio: unir en un mismo objeto distintas materialidades que el territorio chileno dispone —greda, cobre, vidrio—. Entender cuánta luz atraviesa un espesor de arcilla es lo que después permitió leer la frontera greda–vidrio en las otras líneas.',
 c_a_en='This line also fixed a particularity of the studio: joining in a single object different materialities available in Chilean territory —clay, copper, glass. Understanding how much light passes through a thickness of clay is what later made it possible to read the clay–glass border in the other lines.',
 c_b_es='Es también la línea más doméstica. No exige pedestal ni vitrina: se cuelga sobre una mesa y se enciende todos los días. La prueba de que el sistema resiste el uso cotidiano, no solo la exhibición.',
 c_b_en="It's also the most domestic line. It demands no pedestal or vitrine: it hangs over a table and is switched on every day. Proof that the system withstands daily use, not just exhibition.",
 quote_es='La greda apagada es tierra: mate, porosa, fría. Encendida se vuelve un cuerpo cálido que retiene la luz en su espesor antes de soltarla.',
 quote_en='Unlit, the clay is earth: matte, porous, cold. Lit, it becomes a warm body that holds light in its thickness before releasing it.',
 meta='Luminarias Trufquén: piezas de iluminación donde la greda deja de contener la luz y pasa a filtrarla.',
 hero='img/luminarias/luminarias-hero-poster.jpg', hero_video='img/luminarias/luminarias-hero.mp4', hero_poster='img/luminarias/luminarias-hero-poster.jpg', heropos='center 50%',
 h1_es='Luminarias', h1_en='Lighting',
 hp_es='La greda es la protagonista: torneada, calada, colada. Aquí, además, <span class="em">deja de contener la luz y pasa a filtrarla.</span>',
 hp_en='Clay is the protagonist: turned, perforated, cast. Here, it also <span class="em">stops containing light and starts filtering it.</span>',
 idx_es='2018 — Serie', idx_en='2018 — Series',
 t_es='Lo que define la pieza<br>no es la greda que está:<br><span class="em">es la que se quitó.</span>',
 t_en="What defines the piece<br>isn't the clay that's there:<br><span class=\"em\">it's the clay removed.</span>",
 l_es='Un calado demasiado abierto encandila; uno demasiado cerrado no ilumina. Entre esos dos fracasos hay un rango angosto que no se calcula: se prueba encendiendo la pieza.',
 l_en="A perforation too open glares; one too closed lights nothing. Between those two failures lies a narrow range that isn't calculated: it's tested by switching the piece on.",
 plate='img/luminarias/plate-calada.jpg', plate_alt='Luminaria esférica encendida', plate_alt_en='Lit spherical lamp', plate_cap='Cuerpo de greda · collar de cobre',
 g_es='Una familia, varias escalas', g_en='One family, several scales',
 slides=(
  slide('01','img/luminarias/lum-01-mesa.jpg',u'En el taller',u'In the workshop',u'Torno · greda cruda','Wheel · raw clay',
        u'La esfera aún en el taller, junto a la greda cruda que la origina. El contexto del torno importa tanto como la pieza.',
        u'The sphere still in the workshop, next to the raw clay that originates it. The context of the wheel matters as much as the piece.',u'01 · en el taller')+
  slide('02','img/luminarias/lum-02-racimo.jpg',u'Racimo',u'Cluster',u'Colgantes · remate de cobre','Pendants · copper collar',
        u'Tres cuerpos suspendidos a distinta altura. El cobre remata la boca superior y sostiene el cable textil.',
        u'Three bodies suspended at different heights. Copper finishes the upper mouth and holds the textile cable.',u'02 · racimo')+
  slide('03','img/luminarias/lum-03-calada.jpg',u'Calada',u'Openwork',u'Greda calada + vidrio','Perforated clay + glass',
        u'Cada calado aloja una pieza de vidrio soplado. Apagada se lee como relieve; encendida, cada abertura proyecta su forma.',
        u'Each opening holds a piece of blown glass. Off, it reads as relief; lit, each opening projects its shape.',u'03 · calada')+
  slide('04','img/luminarias/lum-04-calada-encendida.jpg',u'Calada, encendida',u'Openwork, lit',u'Misma pieza en luz','Same piece in light',
        u'La misma pieza de la lámina anterior, encendida: el calado deja de ser relieve y pasa a proyectar su propio dibujo de luz.',
        u'The same piece from the previous plate, lit: the openwork stops being relief and starts projecting its own pattern of light.',u'04 · calada encendida')+
  slide('05','img/luminarias/lum-05-ovalo.jpg',u'Óvalo',u'Oval',u'Volumen cerrado','Closed volume',
        u'Un solo cuerpo lenticular con la boca desplazada. La greda se lee como piedra: densa, mate, sin brillo añadido.',
        u'A single lenticular body with the mouth offset. The clay reads as stone: dense, matte, with no added gloss.',u'05 · óvalo')+
  slide('06','img/luminarias/lum-06-detalle.jpg',u'El calado encendido',u'The openwork lit',u'Detalle en uso','Lit detail',
        u'Encendida, la pieza deja de contener la luz y pasa a filtrarla. El vidrio de cada abertura la concentra antes de soltarla.',
        u'Lit, the piece stops containing light and starts filtering it. The glass in each opening concentrates it before releasing it.',u'06 · el calado encendido')),
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
 c_b_es='Y la greda funciona como matriz: es molde y estructura a la vez. Esa doble función es lo que permitió, después, soplar más de un tipo de vidrio contra ella. Todo lo que vino después está construido sobre estas tres frases. Sabemos qué espesores, qué temperaturas y qué puntos de cocción y templado hacen que esto funcione pieza a pieza. Ese conocimiento es nuestro, se acumuló probeta por probeta, y no se transfiere con mirar una fotografía.',
 c_b_en="And clay works as a matrix: mold and structure at once. That double function is what later made it possible to blow more than one type of glass against it. Everything that came after is built on these three sentences. We know what thicknesses, what temperatures, and what firing and tempering points make this work piece by piece. That knowledge is ours, built up test piece by test piece, and it doesn't transfer by looking at a photograph.",
 quote_es='Sin las probetas no hay sistema: hay suerte. El archivo no es un recuerdo, es el procedimiento — cada material nuevo vuelve a pasar por aquí antes de convertirse en pieza.',
 quote_en="Without the test pieces there is no system: there is luck. The archive isn't a memory, it's the procedure — every new material passes through here again before becoming a piece.",
 meta='Probetas Trufquén: el archivo de ensayo que probó que la cohesión greda–vidrio es posible. Fondart Nacional, folio 406861.',
 hero='img/probetas/probeta-hero-poster.jpg', hero_video='img/probetas/probeta-hero.mp4', hero_poster='img/probetas/probeta-hero-poster.jpg', heropos='center 50%',
 h1_es='Probetas', h1_en='Test pieces',
 hp_es='El año en que dejamos de suponer. Esto no es una colección: <span class="em">es la evidencia.</span>',
 hp_en="The year we stopped assuming. This isn't a collection: <span class=\"em\">it's the evidence.</span>",
 idx_es='2017 — Fondart · Folio 406861', idx_en='2017 — Fondart · Folio 406861',
 t_es='Muchas fallaron.<br>Las que fallaron entregaron<br><span class="em">tanta información como las que resistieron.</span>',
 t_en='Many failed.<br>The ones that failed gave<br><span class="em">as much information as the ones that held.</span>',
 l_es='Cada probeta es una variable movida a propósito: espesor de pared, geometría del calado, tamaño de la abertura, momento térmico del vidrio. La única forma de saberlo era hacerlo y mirar.',
 l_en="Each test piece is one variable moved on purpose: wall thickness, perforation geometry, opening size, the glass's thermal moment. The only way to know was to do it and look.",
 plate='img/probetas/plate-variables.jpg', plate_alt='Vidrio incandescente soplado dentro de la greda calada', plate_alt_en='Incandescent glass blown inside the perforated clay', plate_cap='El ensayo en curso',
 g_es='Ocho ensayos del conjunto', g_en='Eight trials from the set',
 slides=(
  slide('01','img/probetas/pr-01-quiebre.jpg',u'Quiebre por temperatura',u'Thermal break',u'Ensayo fallido','Failed trial',
        u'El vidrio se contrajo más rápido que la greda y abrió la pared. Este quiebre fijó el límite que había que respetar.',
        u'The glass contracted faster than the clay and split the wall. This break set the limit we had to respect.',u'PR·01 · quiebre')+
  slide('02','img/probetas/pr-02-quiebre-detalle.jpg',u'Quiebre, detalle',u'Thermal break, detail',u'Vidrio fracturado','Fractured glass',
        u'El borde de vidrio quedó dentado dentro del cuerpo de greda. El registro del fallo es tan útil como el de un ensayo exitoso.',
        u'The glass edge was left jagged inside the clay body. The record of a failure is as useful as that of a successful trial.',u'PR·02 · quiebre, detalle')+
  slide('03','img/probetas/pr-03-macro.jpg',u'La frontera',u'The border',u'Macro del contacto','Contact macro',
        u'El detalle que lo probó todo: greda y vidrio comparten un borde nítido. No hay masa única — la unión es mecánica.',
        u'The detail that proved everything: clay and glass share a sharp edge. There is no single mass — the union is mechanical.',u'PR·03 · la frontera')+
  slide('04','img/probetas/pr-04-grieta.jpg',u'Grieta controlada',u'Controlled crack',u'Vidrio ámbar alojado','Amber glass lodged inside',
        u'La grieta deja ver el vidrio ámbar alojado dentro. Lo que en otra pieza sería falla, aquí quedó documentado como dato.',
        u'The crack reveals the amber glass lodged inside. What would be a defect elsewhere was documented here as data.',u'PR·04 · grieta controlada')+
  slide('05','img/probetas/pr-05-mano.jpg',u'Prueba en mano',u'Trial in hand',u'Verificación directa','Direct verification',
        u'Cada probeta se revisa también en la mano, no solo en el banco. El peso y el calce se confirman con el cuerpo, no solo con la vista.',
        u'Each test piece is also checked by hand, not only on the bench. Weight and fit are confirmed with the body, not just by sight.',u'PR·05 · prueba en mano')+
  slide('06','img/probetas/pr-06-individualidad.jpg',u'Grieta que individualiza',u'Individualizing crack',u'Vidrio ámbar visible','Amber glass visible',
        u'La misma grieta controlada, en un cuerpo más alto: cada probeta se agrieta distinto y esa diferencia pasó a leerse como identidad, no como defecto.',
        u'The same controlled crack, in a taller body: each test piece cracks differently, and that difference came to read as identity, not defect.',u'PR·06 · grieta que individualiza')+
  slide('07','img/probetas/pr-07-fallida.jpg',u'Probeta fallida',u'Failed test piece',u'Vidrio fracturado en banco','Glass shattered on the bench',
        u'El vidrio se fracturó por completo al separarse de la greda. Un fallo total también delimita el rango que sí funciona.',
        u'The glass shattered completely when it separated from the clay. A total failure also delimits the range that does work.',u'PR·07 · probeta fallida')+
  slide('08','img/probetas/pr-08-calce.jpg',u'Fuente por calce',u'Vessel by fit',u'Vidrio alojado en el calado','Glass set in the perforation',
        u'El vidrio se aloja en el calado de la fuente sin adhesión química. El calado no es ornamento: es el sistema de anclaje de toda la pieza.',
        u'The glass sits in the vessel\'s openwork with no chemical adhesion. The openwork is not ornament: it is the anchoring system of the whole piece.',u'PR·08 · fuente por calce')),
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
 rombo_section=('''<section class="rombo">
  <div class="wrap narrow">
    %s
    <p><span data-es>Rombo Pichikemenküe · iconografía mapuche · su proyección horizontal define la sección constructiva del Ahumador</span><span data-en>Pichikemenküe rhombus · Mapuche iconography · its horizontal projection defines the smoking vessel's constructive section</span></p>
  </div>
</section>''' % pic('img/ahumador/pichikemenkue-blanco.png', 'alt="Rombo Pichikemenküe, iconografía mapuche" loading="lazy"', sizes='(max-width:700px) 100vw, 38rem')),
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
 meta='Ahumador Trufquén: el artefacto de greda de Pomaire que origina el estudio. Cocción y ahumado en un solo objeto. Patente de invención registrada en INAPI.',
 hero='img/ahumador/ahumador-hero-poster.jpg', hero_video='img/ahumador/ahumador-hero.mp4', hero_poster='img/ahumador/ahumador-hero-poster.jpg', heropos='center 50%',
 h1_es='Ahumador', h1_en='Smoking vessel',
 hp_es='Cocina y ahúma en un solo cuerpo de greda, sobre la llama de una cocina convencional. <span class="em">La invención que origina el estudio.</span>',
 hp_en='Cooks and smokes in a single clay body, over a conventional stove flame. <span class="em">The invention that originates the studio.</span>',
 idx_es='2014 — Patente de invención INAPI', idx_en='2014 — INAPI invention patent',
 t_es='Ahumar dentro de la cocina,<br><span class="em">no fuera de ella.</span>',
 t_en='Smoking inside the kitchen,<br><span class="em">not outside it.</span>',
 l_es='Hasta este artefacto, ahumar exigía cámaras externas o esencias artificiales. El control vuelve al cocinero: intensidad, color y punto se regulan en el mismo objeto.',
 l_en='Until this device, smoking required external chambers or artificial essences. Control returns to the cook: intensity, color and doneness are regulated in the same object.',
 plate='img/ahumador/plate-torno.jpg', plate_alt='Greda levantada al torno en el taller alfarero', plate_alt_en='Clay raised on the wheel in the pottery workshop', plate_cap='La greda se levanta al torno · taller alfarero',
 g_es='La misma greda, dos estados', g_en='The same clay, two states',
 slides=(
  slide('01','img/ahumador/ahu-01-esmaltado.jpg',u'Terminación esmaltada',u'Glazed finish',u'Set completo · esmalte negro','Complete set · black glaze',
        u'El conjunto terminado en esmalte cerámico negro: ahumador, base y fuente de corte comparten la misma familia de formas.',
        u'The set finished in black ceramic glaze: smoking vessel, base and cutting vessel share the same family of forms.',u'01 · terminación esmaltada')+
  slide('02','img/ahumador/ahu-02-greda-cruda.jpg',u'Greda cruda',u'Raw clay',u'Fuente de corte · recién levantada','Cutting vessel · just raised',
        u'La fuente de corte recién levantada al torno, todavía húmeda. En este estado la greda admite corte y textura; después del fuego ya no.',
        u'The cutting vessel just raised on the wheel, still damp. In this state the clay accepts cutting and texture; after the fire it no longer does.',u'02 · greda cruda')+
  slide('03','img/ahumador/ahu-03-natural-taller.jpg',u'En el taller',u'In the workshop',u'Terminación natural, sin esmaltar','Natural finish, unglazed',
        u'El conjunto sin esmaltar, secándose al aire libre sobre troncos del taller. El color es el de la greda, no un recubrimiento.',
        u'The unglazed set, drying outdoors on workshop logs. The color is the clay\'s own, not a coating.',u'03 · en el taller')+
  slide('04','img/ahumador/ahu-04-corte.jpg',u'El corte',u'The cut',u'Trabajo en verde','Green-state work',
        u'El perfil de la fuente se define a mano sobre la pieza en verde. Cada corte decide cómo calzará el conjunto.',
        u'The vessel\'s profile is defined by hand on the green piece. Each cut decides how the set will fit together.',u'04 · el corte')+
  slide('05','img/ahumador/ahu-05-kultrun.jpg',u'Fuente de corte',u'Cutting vessel',u'Geometría del conjunto','Set geometry',
        u'Vista superior de la fuente, aún en greda cruda. Repite la sección del ahumador a otra escala: el sistema comparte una sola familia de formas.',
        u"Top view of the vessel, still raw clay. It repeats the smoking vessel's section at another scale: the whole system shares a single family of forms.",u'05 · fuente de corte')+
  slide('06','img/ahumador/ahu-06-producto.jpg',u'Greda natural',u'Natural clay',u'Sin esmaltar · foto de producto','Unglazed · product photo',
        u'Terminación natural: la greda queda a la vista, sellada por bruñido. El color es el del material, no un recubrimiento.',
        u"Natural finish: the clay stays exposed, sealed by burnishing. The color is the material's own, not a coating.",u'06 · greda natural')),
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
VIDEO_TOGGLE = ('<button type="button" class="video-toggle" data-video-toggle aria-label="Pausar video">'
                 '<svg viewBox="0 0 24 24" data-icon-pause><rect x="6" y="5" width="4" height="14"/><rect x="14" y="5" width="4" height="14"/></svg>'
                 '<svg viewBox="0 0 24 24" data-icon-play style="display:none"><path d="M7 5l12 7-12 7z"/></svg>'
                 '</button>')

def hero_media(p):
    if p.get('hero_video'):
        poster = p.get('hero_poster', p['hero'])
        return ('<video src="%s" poster="%s" autoplay muted loop playsinline preload="auto" aria-label="%s" data-label-es="%s" data-label-en="%s" data-motion></video>%s'
                % (p['hero_video'], poster, p['h1_es'], p['h1_es'], p['h1_en'], VIDEO_TOGGLE))
    return pic(p['hero'], 'alt="%s"' % p['h1_es'], sizes='100vw')

def plate_media(p):
    alt_en = p.get('plate_alt_en', p['plate_alt'])
    if p.get('plate_video'):
        return ('<div class="plate"><video src="%s" poster="%s" autoplay muted loop playsinline preload="metadata" aria-label="%s" data-label-es="%s" data-label-en="%s" data-motion></video>%s</div>'
                % (p['plate_video'], p['plate'], p['plate_alt'], p['plate_alt'], alt_en, VIDEO_TOGGLE))
    return ('<button type="button" class="plate js-btn" aria-label="Ampliar imagen: %s" data-label-es="Ampliar imagen: %s" data-label-en="Enlarge image: %s">%s</button>'
            % (p['plate_alt'], p['plate_alt'], alt_en, pic(p['plate'], 'alt="%s" data-cap="%s" loading="lazy"' % (p['plate_alt'], p['plate_cap']), sizes='100vw')))

for p in P:
    p.setdefault('car_ar', '3 / 2')
    p.setdefault('car_w', 'clamp(320px,60vw,760px)')
    p.setdefault('rombo_section', '')
    p['canonical_slug'] = p['slug'][:-5]  # sin ".html"
    p['og_image'] = p.get('hero_poster', p['hero'])
    _slugs = [x[0] for x in LINE_ORDER]
    _i = _slugs.index(p['canonical_slug'])
    p['prev_slug'], p['prev_es'], p['prev_en'] = LINE_ORDER[(_i - 1) % len(LINE_ORDER)]
    p['next_slug'], p['next_es'], p['next_en'] = LINE_ORDER[(_i + 1) % len(LINE_ORDER)]
    p['hero_media'] = hero_media(p)
    p['plate_media'] = plate_media(p)
    html = TPL.format(**p)
    # total de slides dinámico (Engarce tiene 11; el resto 6)
    n_slides = html.count('aria-roledescription="slide"')
    html = html.replace(' de 6" data-n=', ' de %d" data-n=' % n_slides)
    html = html.replace('<span class="car-count" id="count">01 / 06</span>',
                        '<span class="car-count" id="count">01 / %02d</span>' % n_slides)
    with io.open(p['slug'], 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK  ' + p['slug'])
print('\n%d paginas generadas desde la misma plantilla.' % len(P))
