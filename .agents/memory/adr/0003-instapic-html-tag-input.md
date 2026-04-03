---
adr: "0003"
title: instapic accepts a raw HTML img tag as input, not a bare URL
status: Accepted
date: 2026-04-03
tags: [instapic, input, ux]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

`instapic.py` accepts a raw HTML `<img>` tag string (copy-pasted from the browser's DevTools Elements panel) as its sole positional argument. `BeautifulSoup` extracts the `src` attribute to obtain the image URL.

## Rationale

Instagram's full-resolution `src` URL is embedded in the `<img>` tag but is not directly copy-linkable from the UI. Accepting the whole tag removes the need for the user to manually isolate the URL from inside it, making the workflow: right-click → Copy element → paste as CLI argument.

## Consequences

- Any future change to accept bare URLs as input requires replacing `extract_image_url` (`instapic.py:9-14`), not just the argument parser.
- The script cannot be piped a URL directly without a wrapper; this is acceptable for a manual-use personal tool.
