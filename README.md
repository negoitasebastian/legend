# Guess The Predator 2 — Pinkshift Reloaded 2.1

Independent prototype of an Apex-inspired interactive fan trivia website, written as static HTML, CSS and JS modules. No npm/build dependencies. **Not endorsed by or affiliated with EA or its licensors.**

**Review `RIGHTS_AND_GITHUB_AUDIT.md` before any public GitHub deployment.** EA's public content policy does not permit fan games/spin-offs, and some earlier visual assets/hotlinks are not cleared for redistribution. Working code does not establish permission.

### Included features

- Borderless full-screen one-image homepage; vivid magenta/cyan Pinkshift design.
- Six challenge modes: Classic, Pixel, Quote, Ability, Emoji, Map. Daily and Unlimited; 6 guesses One Signal, 5 Full Scan, optional Rush 180 seconds.
- 36 configured POIs on 6 maps, including interiors; multiple independently imported captures per POI.
- Wheel, Legend of the Day, Forbidden Tip/Chest, streaks and local browser storage.
- **14 original local WAV UI sounds**: 6 hover sounds and 8 functional navigation/outcome effects. No third-party audio samples or character impersonations included.
- Media Studio for permitted map screenshots, Ability icons and human-recorded voice clips; Media Diagnostic for live asset health checks.

### Current media availability

| Category | Available |
|---|---|
| Map locations configured | 36 |
| Actual permitted location screenshots bundled | **0** |
| Genuine Ability crops in legacy project | 8 |
| Actual licensed character voice recordings | **0** |
| Original authored WAV effects | **14** |
| Remote Legend portraits | Links only, rights/reliability not verified |

Local preview: `python -m http.server 8000` then `http://localhost:8000/`.
Node smoke test: `node --test tests/*.test.mjs`; package check: `python3 scripts/validate_release.py`.

More details: `START_HERE.md`, `RELEASE_NOTES.md`, `RIGHTS_AND_GITHUB_AUDIT.md`.
