## IMPORTANT CLEAN DEPLOY

If you are replacing an older GTP2 repository, delete these stale files before copying the new build: `src/concept_map_manifest.mjs`, any `assets/maps/*-concept-*.webp`, the folder `assets/legends/`, and any `assets/sfx/enter-*.wav`. Keep `.git`.

> For V2.2.1 rollback and safe repo cleanup, read `ROLLBACK_README.md` first.

# Guess The Predator 2 — Pinkshift Reloaded

**PUBLICATION CAUTION:** Read `RIGHTS_AND_GITHUB_AUDIT.md` first. The site's game-specific content has not been fully cleared. EA's published content policy restricts fan games, so this package is intended for local review/development until permissions or appropriate legal review are completed.

## Preview / local development

No npm required. From the project root, run `python -m http.server 8000`, then open `http://localhost:8000/` in your browser. Opening index.html via `file://` may block ES Modules.

## If authorized to publish on GitHub Pages

1. Create a brand-new repository (e.g. `guess-the-predator-2`).
2. Extract the ZIP. Copy **all contents of the ZIP** directly to repository root (`index.html`, `pinkshift.css`, `styles.css`, `src`, `assets`, `.github`). Do not wrap them inside an extra folder.
3. Commit and Push via GitHub Desktop to the main branch.
4. GitHub → Settings → Pages → Build and deployment → Source: **GitHub Actions**. Wait for workflow to turn green.
5. Clear cache or press Ctrl+F5 if the old theme still appears.

## Media Studio workflow

- Open `MEDIA_STUDIO.html` on the site. Each map/POI accepts **up to eight** distinct local images. Imports are not uploaded automatically.
- Use only media with public distribution permission. Confirm rights checkbox; export media pack ZIP; extract it over repo root and push.
- Install genuine permitted character recordings through Studio if available. They will work with the existing playback control; synthetic impersonations are not included.
- `MEDIA_DIAGNOSTIC.html` shows actual files found by the browser.

## Status

- 36 configured Map sectors, including interiors; **0 actual licensed Map screenshots** supplied.
- 8 local Ability crops; 20 need authorized artwork.
- **14 original UI audio clips installed and playable** after user interaction.
- 0 character voices bundled (human recordings require appropriate permission).
- Remote portrait hotlinks currently remain an unresolved rights/reliability concern.
