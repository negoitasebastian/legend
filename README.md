# Guess the Predator 2 — Neon Rebirth

Fresh repository-ready HTML / CSS / JavaScript fan-trivia project. No npm, bundler, React, CDN, or build step for the game itself. Entire interface is in English. The new site uses its **own** browser storage key and is independent of V16.

## Gameplay
- 6 game modes: Classic, Pixel, Quote, Ability, Emoji, Map.
- Daily and Free Play; One Signal = 6 tries, Full Scan = 5 tries; optional 180-second Rush.
- Legend of the Day, 28-legend Wheel, streaks, statistics, Forbidden Tip and Chest unlocked after six Daily modes (wins or losses).
- 36 Map location prompts across six maps. Some are **interior** locations; screenshots are not automatically bundled.
- Original neon menu hover sound effects (generated locally by Web Audio, not extracted game samples).

## Install to a brand-new GitHub repository
1. Create an **empty public GitHub repository**, e.g. `guess-the-predator-2`. Avoid generating starter README/license files on GitHub to keep upload simple.
2. Extract **GTP2 FULL PROJECT ZIP**. Copy all contents (including `.github`) to your new repository's root, not inside another folder.
3. Commit and push to `main` using GitHub Desktop.
4. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
5. Wait for the **GTP2 — Test and Deploy GitHub Pages** workflow to finish successfully. Open `https://YOUR-NAME.github.io/guess-the-predator-2/`.
6. Hard refresh once (Ctrl+Shift+R) if your browser keeps old assets.

## Real Map screenshots / human recordings
The **36 locations are game data**, but this archive has **0 real map screenshots** and **0 human voice recordings**. We did not scrape, fabricate or relabel copyrighted media. Until you provide and approve real gameplay captures, Map Mode presents an honest text clue when an image is unavailable. Similarly, Quote remains a playable written clue until a genuine human recording is installed.

Open `MEDIA_STUDIO.html` (also linked in the navigation) to import permitted gameplay screenshots and human voice recordings. Select each image from your computer; the tool checks dimensions and exports a separate ZIP with correctly named files. Extract that media ZIP over the **root** of your new repo and push again. Available recordings are then playable automatically. Map screenshot filenames correspond to `assets/map-catalog.json` IDs. More screenshots can be imported later without touching the game engine.

Human recordings should be independently authorized; in-game voice-actor recordings may have additional rights restrictions. The importer does not manufacture audio or hide missing files.

`MEDIA_DIAGNOSTIC.html` shows a **live check** for local Map images, Ability icons, and installed voice manifest entries.

## Other details
- The page is a standalone fan-trivia design, not a copy of the original game UI.
- Single 1672×941 local background image (WebP). No duplicated menu baked into the art.
- One cursor-tracking canvas; no extra emoji eyeballs. Honors FX OFF and reduced-motion preference.
- 8 local Ability icons tested. Only those verified icons enter Ability round selection; no broken or fake icon clues.
- No official Apex voice files or official UI sounds are included.
- No official EA / Respawn marks are used as the site's own brand.
- Site footer includes the EA non-affiliation disclaimer.
- For static QA: `node --test tests/*.test.mjs` and `python3 scripts/validate_release.py` (requires Pillow only for validation). GitHub workflow has Pillow preinstalled in current hosted runner environments, but may require an explicit install if changed.
