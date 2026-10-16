# Guess The Predator 2 — publication / IP audit (2026-10-16)

**Status: NOT RIGHTS-CLEARED for public publication as an Apex-derived interactive fan game.**
This document is a practical audit, not legal advice or a guarantee against notices or account action.

## Primary official sources
- EA Content Policy: https://help.ea.com/en/articles/security-and-rules/ea-content-policy/
- EA User Agreement: https://www.ea.com/legal/user-agreement
- GitHub DMCA process: https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy
- GitHub Trademark policy: https://docs.github.com/en/site-policy/content-removal-policies/submitting-content-removal-requests

## Important findings

1. **Fan games / spin-offs: HIGH RISK.** EA's current public policy permits some personal fan sites, but explicitly says it does not allow fan games, knockoffs or spin-offs based on its games. This is an interactive trivia site about EA game characters/locations. Styling it as an independent fan site, using original code and adding a disclaimer lowers confusion but **does not remove this policy conflict**. Obtain appropriate permission or qualified legal guidance before publishing.
2. **EA logos / trademark: reduced, not eliminated.** The visible site's branding uses a self-created `G` badge and *Guess The Predator*, rather than using official EA/Respawn/Apex logos as its own mark. References to Apex Legends and its character/location names are informational, but may still implicate intellectual-property rights. Keep the non-affiliation statement. Do not imply EA endorsement.
3. **Visuals: unresolved provenance.** `assets/decor/haunted-hero.webp` is a newly generated Halloween illustration of a character inspired by Mirage. It is not a screenshot of Apex, but recognizably references EA's character. Approval for distribution was not established. The eight local ability-icon crops came from earlier screenshots; rights were not independently verified. Their presence in this repository does **not** prove they are cleared for public distribution.
4. **Portraits: HIGH / unresolved.** `src/art.mjs` still contains remote character-portrait references on external sites, including fan sites and wikis. Their licenses, reuse rights and hotlink policies were not verified. Some images may fail to load or attract takedown complaints. Replace with genuinely permitted local images and remove unapproved external dependencies before posting to the public. Never infer reuse permission merely because an image is reachable in a browser.
5. **Map photos: 0 included.** `assets/maps/` contains no actual POI screenshots. The game now uses **only local paths**, not wiki hotlinks. `MEDIA_STUDIO.html` prepares up to eight files per location, but the owner must clear and provide each file. Self-recorded gameplay may still be subject to EA's policy, especially the fan-game restriction.
6. **Audio: reduced risk.** `assets/sfx/*.wav` contains 14 original sounds synthesized for this website (no extracted soundtrack or Apex audio). `assets/voices/` contains zero character recordings. Use voice lines only if distribution permission covers them; EA notes that talent/voices/music may involve third-party rights. No AI-generated impersonations are bundled.
7. **GitHub: account risk remains.** GitHub may disable repositories subject to compliant copyright notices. In appropriate circumstances, repeat IP infringement can affect an account. A README disclaimer or a private/unlisted link is not a substitute for permission.
8. **Software: lower-risk areas.** Core interface/source code, logic, procedural SFX and original file naming are independent new work; no game executable, anti-cheat bypass, extracted proprietary code or in-game source files were detected in the newly authored patch. A full legal determination of earlier code/art provenance has not been made.

## Publication decision table

| Type | In archive | Provenance | Publication clearance |
|---|---:|---|---|
| Original HTML/CSS/JS | Yes | Project-authored | No third-party source code identified in the patch; broader project still needs review |
| Original synthesized UI WAV sounds | 14 | Project-authored | No known third-party samples used |
| Halloween hero / recognizable character | 1 | Newly generated fan illustration | EA character rights unresolved |
| Eight genuine Ability icon crops | 8 | Previous screenshot-derived assets | NOT VERIFIED |
| 28 remote Legend portrait references | Yes (URLs only) | Third-party hotlinks | NOT VERIFIED |
| Genuine Map location captures | 0 | None bundled | Not applicable until imported |
| Actual character voice clips | 0 | None bundled | Not applicable until imported |
| Fan game / trivia concept | Present | Apex-inspired experience | **EA policy risk; approval not established** |

## Suggested safest next move

Do not publish this Apex-specific build as "officially safe". Before making it public, obtain permission for the fan-game use and all external or game-derived art/audio, or substantially rework the content into original IP with no EA characters, locations, logos or media. Avoid monetization without checking policy; even non-commercial activity doesn't create blanket permission. Keep source/license proof for every asset. If a rights-holder or GitHub contacts you, respond promptly using official channels.
