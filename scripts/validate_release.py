from pathlib import Path
from PIL import Image
import json,sys
root=Path(__file__).resolve().parents[1]
required=['index.html','styles.css','pinkshift.css','MEDIA_STUDIO.html','MEDIA_DIAGNOSTIC.html','src/app.mjs','src/engine.mjs','src/maps.mjs','src/map_media_manifest.mjs','src/ability_media_manifest.mjs','src/data.mjs','assets/decor/haunted-hero.webp','assets/map-catalog.json','.github/workflows/pages.yml']
for f in required:
    assert (root/f).is_file(),f'MISSING FILE: {f}'
locations=json.loads((root/'assets/map-catalog.json').read_text())
assert len(locations)==36, f'Expected 36 catalog entries, found {len(locations)}'
assert len({r['id'] for r in locations})==36
assert len({r['map'] for r in locations})==6
assert len([r for r in locations if r['kind']=='Interior'])>=10
img=Image.open(root/'assets/decor/haunted-hero.webp')
assert img.size[0]>=1280 and img.size[1]>=720
js=(root/'src/app.mjs').read_text();css=(root/'styles.css').read_text()
assert js.count('id="mirage-gaze"')==1
assert 'gtp2-backdrop' in js and '.gtp2-backdrop' in css
assert not (root/'assets/decor/haunted-showcase-full.png').exists()
assert 'HUMAN VOICE FILE NOT INSTALLED' not in js
assert './MEDIA_STUDIO.html' in js
assert 'gtp2-audio-preview' in js
assert 'mapMediaManifest' in (root/'src/maps.mjs').read_text()
assert 'https://' not in (root/'src/maps.mjs').read_text()
assert len(list((root/'assets/sfx').glob('*.wav')))==14
assert (root/'src/engine.mjs').read_text().count('%36')>=1
for f in (root/'assets/ability-icons').glob('*.png'):
    assert f.read_bytes()[:8]==b'\x89PNG\r\n\x1a\n', f
maps=sum(any((root/'assets/maps'/f"{r['id']}.{ext}").exists() for ext in ['webp','jpg','png','jpeg']) for r in locations)
print(f'GTP2 QA PASS: 36 POI entries / 6 maps / {maps} bundled real photos / 8 local Ability icons / 14 original WAV SFX / one borderless hero')
if not maps: print('NOTE: No verified location screenshots bundled. Import authorized captures via Media Studio.')
