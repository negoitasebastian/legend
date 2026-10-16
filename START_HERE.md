# Deploy — GTP2 V2.2 Neon Phantom

**Before a public release:** See `RIGHTS_AND_GITHUB_AUDIT.md`. Working code, homebrew art, and an unofficial disclaimer do not guarantee permission from EA; existing character, icon and fan-game restrictions remain.

1. Create or open a **new repository**, e.g. `guess-the-predator-2`, in GitHub Desktop.
2. Extract this FULL ZIP. **Copy all its contents** (`index.html`, `styles.css`, `pinkshift.css`, `.github/`, `src/`, `assets/`, etc.) straight into your repository root. No additional `GTP2_PINKSHIFT_20_BUILD/` folder.
3. Preserve the repository `.git` directory; do not copy a `.git` folder from elsewhere.
4. Commit and `Push origin` to the `main` branch.
5. GitHub → repository Settings → Pages → Build and deployment → Source **GitHub Actions**.
6. Wait for the Pages workflow to finish successfully, then refresh the published site with Ctrl+F5.
7. Test: Home (one borderless Mirage scene), all 6 modes, Map artwork, Browse Legends, Quote text-only, Sound ON + TEST, and `MEDIA_DIAGNOSTIC.html`.

## What is included and what is not

- 72 *stylized illustrations* of 36 sectors: **not** screenshots. Your approved images can replace them using Media Studio.
- 28 original local transparent *illustrative figurines*: **not** the actual 3D character models.
- 20 original interface WAVs (no official sound recordings).
- Original HTML/CSS/JS plus automated QA.
- No authenticated Apex voice tracks or genuine real-game location captures.

To replace figures later with permitted images, add transparent `assets/legends/<slug>.webp` (or PNG where supported). Images should show one full-body character on transparent background; the roster card size and alignment are consistent.

The site does not require npm, React or an API backend. Save progress remains in the GTP2 browser localStorage key.
