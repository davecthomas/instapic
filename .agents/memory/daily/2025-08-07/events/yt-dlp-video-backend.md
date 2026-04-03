---
id: yt-dlp-video-backend-2025-08-07
type: decision_candidate
timestamp: 2025-08-07T08:04:31Z
bootstrapped_at: 2026-04-03T00:00:00Z
decision_candidate: false
promoted_to_adr: "0002"
tags: [instareel, dependencies, video]
title: yt-dlp is the canonical video download backend
---

## Decision

`instareel.py` uses `yt-dlp` as its sole video download backend. Key configuration:

- Format: `bv*+ba/b` (best video + best audio, fallback to best combined)
- Merge output: `mp4` via `merge_output_format`
- Concurrent fragment downloads: 4 workers
- User-Agent spoofed to `Mozilla/5.0`
- Output filename: `{uploader}_{YYYY-MM-DD}_{id}.mp4`

## Rationale

Instagram uses session-scoped, rotating media URLs. `yt-dlp` has an actively maintained Instagram extractor that handles URL resolution internally, including fragment assembly and muxing. Implementing this directly with `requests` would require reverse-engineering Instagram's media API and maintaining that against Instagram's changes. `yt-dlp` also handles concurrent fragment downloads natively.

## Consequences

- Do not replace yt-dlp with a raw requests-based video fetcher.
- Pin yt-dlp in `requirements.txt` and update it explicitly when Instagram extraction breaks (not via floating version).
- Any cookie-file-based auth is passed through `yt-dlp`'s `--cookiefile` option, not managed independently.

## Evidence

- `docs/technical-design.md` §`instareel.py` — Reel Downloader, "Why URL-based input" and "Processing"
- `docs/technical-design.md` §Dependency Model: "Handles Instagram's rotating session-scoped media URLs; actively maintained"
- Commit ab399e9 (2025-08-07): "instareel - save an mp4 from an instagram reel url"
