from pathlib import Path
r=Path(__file__).resolve().parents[1]
p=r/'src/maps.mjs';s=p.read_text()
s=s.replace("import {mapMediaManifest} from './map_media_manifest.mjs';","import {mapMediaManifest} from './map_media_manifest.mjs';\nimport {conceptMapManifest} from './concept_map_manifest.mjs';")
a=s.index('export function mapShots(entry,angle=0){');b=s.index('export function mapRound(entry)',a)
s=s[:a]+'''export function mapShots(entry,angle=0){
 if(!entry)return [];
 const manifest=(mapMediaManifest[entry.id]||[]).filter(safeLocalName)
   .map(filename=>`./assets/maps/${filename}`);
 const concept=(conceptMapManifest[entry.id]||[]).filter(safeLocalName)
   .map(filename=>`./assets/maps/${filename}`);
 const local=['webp','png','jpg','jpeg'].map(ext=>mapLocalPath(entry,ext));
 // User-approved captures always override the original concept artwork.
 if(manifest.length){
   const start=((Math.trunc(Number(angle)||0)%manifest.length)+manifest.length)%manifest.length;
   return [...manifest.slice(start),...manifest.slice(0,start),...concept];
 }
 const start=((Math.trunc(Number(angle)||0)%concept.length)+concept.length)%concept.length;
 return [...local,...concept.slice(start),...concept.slice(0,start)];
}
''' + s[b:]
p.write_text(s)
p=r/'src/app.mjs';s=p.read_text()
start=s.index("  if(mode==='quote')return ")
end=s.index("  if(mode==='ability')",start)
s=s[:start]+'''  if(mode==='quote')return `<div class="clue-visual gtp2-quote-rework"><div class="gtp2-quote-lines" aria-hidden="true"></div><div class="gtp2-quote-head"><span>◈ DECRYPTED / TEXT ONLY</span><span>CHANNEL 0${MODES.indexOf(active)+1}</span></div><div class="gtp2-quote-mark" aria-hidden="true">“</div><blockquote>“${esc(target.quote)}”</blockquote><div class="gtp2-quote-status"><span class="gtp2-live-dot"></span> ENCRYPTED SIGNAL · IDENTIFY THE SPEAKER</div></div>`;
''' + s[end:]
s=s.replace('alt="An actual Apex Legends location screenshot when a valid source is available"','alt="A stylized original scene reconstruction of an unknown location"')
s=s.replace("<div class=\"map-credit\">Multiple local angles supported · Only media cleared for redistribution</div>","<div class=\"map-credit\">ORIGINAL STYLIZED RECONSTRUCTIONS · NOT APEX SCREENSHOTS · TWO CAMERA ANGLES PER LOCATION</div>")
s=s.replace('Recognize the landscape, then pinpoint the POI.', 'Study the illustrated environment, then pinpoint the sector.')
s=s.replace('This sector has no licensed local capture yet. Play using the text clue, or add a permitted screenshot with Media Studio.','Visual reconstruction unavailable. The written location clue is still playable.')
s=s.replace('<a class="map-media-link" target="_blank" rel="noopener" href="./MEDIA_STUDIO.html">OPEN MEDIA STUDIO ↗</a>','')
# Add mode classes to main to power backgrounds
s=s.replace('return `<main class="wrap game map-game">','return `<main class="wrap game map-game gtp2-game-scene gtp2-scene-map">')
s=s.replace('return `<main class="wrap game" style="--tile:${classOf(active)}">','return `<main class="wrap game gtp2-game-scene gtp2-scene-${active}" style="--tile:${classOf(active)}">')
s=s.replace('PINKSHIFT RELOADED · UNOFFICIAL TRIVIA','NEON PHANTOM · ORIGINAL ART EDITION')
s=s.replace('6 MAPS · 36 SECTORS · MULTIPLE ANGLES','6 ARENAS · 36 ILLUSTRATED SECTORS · 72 VIEWS')
# Fix portrait loader source selection for portrait picker - prefer 3D full body cutouts if available; regular remote fallback remains
s=s.replace("const candidates=artCatalog[image.dataset.portrait]||[];let index=0;", "const candidates=[`./assets/legends/${image.dataset.portrait}.webp`,`./assets/legends/${image.dataset.portrait}.png`,...(artCatalog[image.dataset.portrait]||[])];let index=0;")
# add class to picker root and cards
s=s.replace('<div class="picker" role="dialog"','<div class="picker gtp2-picker" role="dialog"')
s=s.replace('<button class="picker-legend" data-action="guess"','<button class="picker-legend gtp2-legend-card" data-action="guess"')
s=s.replace('${portrait(l.slug,{alt:l.name,cls:\'balanced\'})}<strong>${esc(l.name)}</strong><small>${esc(l.role)}</small></button>`).join(\'\'):','${portrait(l.slug,{alt:l.name,cls:\'balanced\'})}<strong>${esc(l.name)}</strong><small>${esc(l.role)}</small></button>`).join(\'\'):')
# no-op but harmless
p.write_text(s)
p=r/'index.html';s=p.read_text().replace('pinkshift.css?v=2.1.0','pinkshift.css?v=2.2.0').replace('styles.css?v=2.1.0','styles.css?v=2.2.0').replace('src/app.mjs?v=2.1.0','src/app.mjs?v=2.2.0').replace('Pinkshift Reloaded','Neon Phantom — Pinkshift 2.0');p.write_text(s)
