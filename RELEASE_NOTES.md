# Guess the Predator 2 — V2.2 NEON PHANTOM / PINKSHIFT 2.0

## New in this release

- Borderless single-art hero maintained. Pinkshift 2.0 refinements: smaller neon arcade cards, translucent controls, more balanced colors, improved keyboard outlines.
- Rebuilt gameplay presentation. Six **distinct illuminated backgrounds** for Classic, Pixel, Quote, Ability, Emoji and Map. Actual DOM controls remain clickable; background imagery contains no baked-in buttons.
- **Map mode no longer shows blank imagery:** 36 recognizable *themes* across 6 maps (including interior environments), **72 original stylized concept illustrations included physically in `assets/maps/`**. Two camera variants per location. Image assets are not screenshots and do not replicate Apex locations precisely. A descriptive field report makes the puzzles fairer despite impressionistic artwork.
- New Map loader prefers specifically imported, rights-approved local captures from Media Studio above its built-in concept illustrations. Map falls back to the bundled artwork if imported files go missing.
- All 28 Legend picker slots now have a packaged **transparent, original, role-inspired figurine illustration** in `assets/legends/` to avoid `PORTRAIT OFFLINE`. Uniform figure size, card proportions, hover transitions. **These are stylized 2D/2.5D stand-ins, NOT actual 3D renders of EA characters or accurate likenesses.**
- **Quote mode is TEXT ONLY**: no faux playback controls, no missing voice messages, revised transmission artwork.
- **20 locally authored WAV sounds**: six hover accents, six new mode-opening stingers and eight gameplay UI effects. No official Apex music, voicelines or impersonations.
- Original generated art files and regeneration scripts included with source for auditing.
- Updated media diagnostic: distinguishes original illustrations from user-installed photos. Updated repo validation and new Playwright tests.

## Still not solved / publication warnings

- **0 licensed actual Apex Map screenshots**, because the included 72 illustrations are original reinterpretations, not real captured locations.
- **0 human character voicelines**, intentionally: Quote now works solely on text.
- **8 earlier Ability icon image crops** remain. Those older EA-related assets have not been legally cleared. Ability mode intentionally uses only its installed icon subset.
- Game-specific names, references, overall trivia/game concept, earlier ability crops and the recognizable Halloween centerpiece remain **at potential risk under EA's content policy**. The project is NOT rights-cleared for public release. Read `RIGHTS_AND_GITHUB_AUDIT.md`.
- Transparent figures are original stylistic stand-ins, *not* accurate EA Legend 3D models. If authorized full-body 3D art becomes available, it can replace `assets/legends/<slug>.webp` without code changes.

## Preservation and deployment

- Same GTP2 local save key as 2.1, preserving Daily / Free Play progress.
- Works as GitHub Pages static site; no bundler, npm or runtime server dependency. All newly bundled map, figure and sound assets use relative paths.
- Start with `START_HERE.md`. For a safer public release, resolve the outstanding EA / character and icon rights questions first.
