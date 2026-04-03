---
id: auth-model-2025-08-07
type: decision_candidate
timestamp: 2025-08-07T00:00:00Z
bootstrapped_at: 2026-04-03T21:15:06Z
decision_candidate: true
tags: [authentication, instapic, instareel, security]
title: Authentication model — no auth for images, cookie-file passthrough for reels
---

## Decision

The two scripts use distinct, minimal authentication strategies:

- **instapic.py** — no authentication. Full-resolution `src` URLs from public posts are fetched directly via `requests.get` without any session or credential.
- **instareel.py** — optional Netscape-format cookie file passed to yt-dlp via `--cookiefile`. Used for private or age-gated content. No OAuth, no session management, and no credentials are stored by the script itself.

## Rationale

Images from public posts do not require auth; adding session handling would be unnecessary complexity. For reels, Instagram's session-scoped media URLs are handled internally by yt-dlp; the script only needs to supply a cookie file for access-gated content. Browser-exported cookies are the least-invasive mechanism that does not require the script to manage credentials.

## Consequences

- Do not add login flows, token storage, or OAuth to either script.
- Cookie file support is the ceiling of supported auth complexity.
- If content requires auth, the user must supply a cookie file; there is no fallback.

## Evidence

- `docs/technical-design.md` §Authentication Model
- Commit ab399e9 (2025-08-07): "instareel - save an mp4 from an instagram reel url" — introduced yt-dlp with cookiefile support
