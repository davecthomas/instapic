---
date: 2025-08-07
generated_at: 2026-04-03T21:15:06Z
bootstrapped: true
---

# Summary — 2025-08-07

## Decision candidates

- **yt-dlp-video-backend** — yt-dlp is the canonical video backend for instareel; handles Instagram's rotating session-scoped URLs, concurrent fragment download, and mp4 merging. Promoted → ADR-0002. See `events/yt-dlp-video-backend.md`.
- **output-directory-divergence** — Output directories differ intentionally: ~/Downloads (hardcoded) for images (feels like a one-off download), ./downloads (configurable) for reels (feels like a project asset). Promoted → ADR-0004. See `events/output-directory-divergence.md`.
- **auth-model** — Authentication model established: no auth for images (plain requests.get), optional cookie-file passthrough for reels via yt-dlp. No OAuth or credential storage. Promoted → ADR-0005. See `events/auth-model.md`.

## Commits

- ab399e9 — "instareel - save an mp4 from an instagram reel url": introduced instareel.py with yt-dlp backend, cookie file support, and concurrent fragment download.
