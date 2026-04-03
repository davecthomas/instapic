---
adr: "0002"
title: yt-dlp is the canonical video download backend
status: Accepted
date: 2026-04-03
tags: [instareel, dependencies, video]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

`instareel.py` delegates all video extraction and download to `yt-dlp` rather than implementing Instagram-specific HTTP scraping.

## Rationale

Instagram's media URLs are session-scoped and rotate frequently. Maintaining a custom extractor would require ongoing reverse-engineering. yt-dlp handles format selection, fragment merging to MP4, concurrent downloads, and cookie-based auth, and is actively maintained against Instagram's anti-scraping changes.

## Consequences

- Do not replace yt-dlp with custom downloader logic.
- Keep `yt-dlp` pinned in `requirements.txt` and update it when Instagram auth or format changes break downloads.
- Cookie file support (`--cookiefile`) is the supported auth mechanism for private/age-gated content.
