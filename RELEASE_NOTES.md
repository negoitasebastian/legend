# GTP2 — Pinkshift Reloaded / 2.1

## Visual changes
- Restored a brighter pink/violet/cyan **Pinkshift** palette with glass panels, mode-specific glow, and neon controls.
- Main-page hero remains a single edge-to-edge local artwork, **no border**, no menu painted into the image, no duplicate character image.
- Desktop and mobile layouts tuned; each mode remains a functional HTML button.
- Added prominent original UI sound Test control.

## Original audio shipped
- **14 actual WAV files** inside `assets/sfx/`: six different hover sounds plus nav, pick, clue, wrong, correct, win, lose and reveal.
- Sound preference is ON for brand-new users. Browsers may require a first click to authorize audio; use the TEST button. Saved user preferences are respected.
- No licensed Apex sound, soundtrack, synthetic character imitation or actual voice lines included.

## Media recovery / gameplay
- Map Mode supports **36 POIs** over six maps with interiors and exteriors.
- **Up to 8 screenshot angles per POI** with deterministic local-file rotation across rounds. Local media manifest avoids unreliable hotlinks. Default single-file names remain supported.
- **Media Studio 2.1** imports multiple screenshot files, additional real Ability icons and authorized human recordings. It exports an offline ZIP plus manifests and preserves prior manifests where possible.
- New Media Diagnostic checks genuine media files and all 14 WAVs on GitHub Pages.
- Legacy gameplay, 6 Daily modes, Wheel, Tip Chest, attempts and local save key preserved.

## Verified
- Node game unit tests, Chromium desktop 1600×900 and mobile 390×844 navigation / gaze / FX, ZIP media export of two images for the same POI.
- Release validation checks the generated SFX and required files.

## NOT complete / IMPORTANT
- 0/36 real licensed location screenshots included; 0 human Legend voice lines bundled. These are not fixed by adding an importer. Media needs to be supplied with permission.
- 8 local ability icons exist, while the other 20 require permitted artwork.
- External Legend portrait hotlinks still need a rights/performance review and local replacement.
- The EA content policy explicitly restricts fan games and spin-offs; no guarantee of GitHub compliance or continued hosting. See `RIGHTS_AND_GITHUB_AUDIT.md` **before publishing**.
