# Guess the Predator 2 — Neon Phantom / Pinkshift 2.0

A static, independent Apex-inspired trivia prototype. Written in plain HTML/CSS/JavaScript for GitHub Pages. **Not endorsed or affiliated with EA / Respawn. Not certified for public publishing.**

## Game features

Six modes: Classic, Pixel, Quote (text only), Ability, Emoji and Map. Daily & Free Play, One Signal / Full Scan, optional Rush 180s, streaks and local save progress, Wheel, Legend of the Day and Forbidden Tip/Chest.

### Actual bundled media

| Asset | Quantity | Reality |
|---|---:|---|
| Map sectors | 36 | 6 arenas, including 13 interiors |
| Map imagery | **72** | Original 2D illustrated concept scenes (two perspectives per sector), **not genuine Apex screenshots** |
| Local Legend figures | **28** | Transparent original stylized 2.5D sci-fi figurines; not game models or accurate Legend likenesses |
| Original UI sound effects | **20 WAV** | 6 hover, 6 entering modes, 8 interface / feedback effects |
| Game ability icons | **8** | Earlier screenshots; **rights not independently verified** |
| Authorized character voice clips | **0** | Quote is text-only by design |

No third-party map image hotlinks. Map imports from `MEDIA_STUDIO.html` override built-in concept paintings, and if they are unavailable, the painted fallback continues working. `MEDIA_DIAGNOSTIC.html` distinguishes source photos from original paintings.

## Play and test

- GitHub Pages: upload the ZIP **contents directly to repository root**; do not create an extra nested project folder.
- Local preview: `python -m http.server 8000` from this root, then `http://localhost:8000/`.
- Node tests: `node --test tests/*.test.mjs`.
- Release validation: `python3 scripts/validate_release.py` (Pillow required).
- Optional Chromium tests: `python3 tests/make_browser_harness.py` then `python3 tests/browser_qa.py`, `python3 tests/v22_visual_qa.py`, and `python3 tests/v22_audio_qa.py` (playwright/Chromium).

Read `START_HERE.md`, `RELEASE_NOTES.md` and especially `RIGHTS_AND_GITHUB_AUDIT.md` before publishing any Apex-related game.
