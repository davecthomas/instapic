---
adr: "0005"
title: Authentication model — no auth for images, cookie-file passthrough for reels
status: Accepted
date: 2026-04-03
tags: [authentication, instapic, instareel, security]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

The two scripts use distinct, minimal authentication strategies:

- **instapic.py** — no authentication. Full-resolution `src` URLs from public posts are fetched directly via `requests.get` without any session or credential.
- **instareel.py** — optional Netscape-format cookie file passed to yt-dlp via `--cookiefile`. Used for private or age-gated content. No OAuth, no session management, and no credentials are stored by the script itself.

## Rationale

Images from public posts do not require auth; adding session handling would be unnecessary complexity. For reels, Instagram's session-scoped media URLs are resolved internally by yt-dlp; the script only needs to supply a cookie file for access-gated content. Browser-exported cookies are the least-invasive mechanism that does not require the script to manage credentials.

## Consequences

- Do not add login flows, token storage, or OAuth to either script.
- Cookie file support is the ceiling of supported auth complexity.
- If content requires auth, the user must supply a cookie file; there is no fallback.
