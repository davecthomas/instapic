---
id: two-tool-split-2024-08-10
type: decision_candidate
timestamp: 2024-08-10T15:42:29Z
bootstrapped_at: 2026-04-03T00:00:00Z
decision_candidate: false
promoted_to_adr: "0001"
tags: [architecture, tools, scope]
title: Two-tool split — images via instapic, video via instareel
---

## Decision

Instagram media downloading is split into two independent scripts rather than a single unified tool:

- `instapic.py` — downloads full-resolution images; accepts a raw HTML `<img>` tag as input
- `instareel.py` — downloads Reels as MP4; accepts a direct Reel URL as input

The two scripts share a venv but have no shared runtime, no shared entry point, and no shared code.

## Rationale

Images and video require fundamentally different download mechanisms. Images are fetched directly with `requests` after parsing the img tag; video requires `yt-dlp` to resolve Instagram's session-scoped media URLs and merge fragments. Combining both into one tool would couple a simple HTTP download workflow to a full video-pipeline dependency. Keeping them separate makes each independently runnable and independently maintainable.

The design doc notes this split should be revisited only if a third media type (e.g. Stories) is added.

## Consequences

- Do not add a unified `instagram.py` dispatcher without a new ADR.
- Each script is individually executable; no shared imports between them.
- If a third media type is added, revisit ADR-0001 before deciding architecture.

## Evidence

- `docs/technical-design.md` §Overview and §Components
- Commit 62eeaf4 (2024-08-10): "download a full res image from instagram" — established instapic.py as standalone image tool
- Commit ab399e9 (2025-08-07): "instareel - save an mp4 from an instagram reel url" — established instareel.py as standalone video tool
