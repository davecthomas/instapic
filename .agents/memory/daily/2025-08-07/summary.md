---
date: 2025-08-07
generated_at: 2026-04-03T21:15:06Z
bootstrapped: true
---

# Summary — 2025-08-07

## Decision candidates

- **auth-model** — Authentication model established: no auth for images (plain requests.get), optional cookie-file passthrough for reels via yt-dlp. No OAuth or credential storage. See `events/auth-model.md`.

## Commits

- ab399e9 — "instareel - save an mp4 from an instagram reel url": introduced instareel.py with yt-dlp backend, cookie file support, and concurrent fragment download.
