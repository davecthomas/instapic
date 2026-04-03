---
id: instapic-html-tag-input-2024-08-10
type: decision_candidate
timestamp: 2024-08-10T15:42:29Z
bootstrapped_at: 2026-04-03T00:00:00Z
decision_candidate: false
promoted_to_adr: "0003"
tags: [instapic, input, ux]
title: instapic accepts a raw HTML img tag as input, not a bare URL
---

## Decision

`instapic.py` takes a raw HTML `<img>` tag string as its CLI argument. It uses `BeautifulSoup` to extract the `src` attribute, then downloads from that URL. It does not accept a bare URL directly.

## Rationale

Instagram's full-resolution `src` URL is embedded in the `<img>` tag in the browser's DevTools Elements panel. The URL is not directly copy-linkable from Instagram's UI — copying the link gives a lower-resolution version. Accepting the entire `<img>` element lets the user copy it without manually extracting the URL, and `BeautifulSoup` handles any attribute-quoting or ordering variation.

## Consequences

- The CLI argument must be a valid HTML fragment containing an `<img>` tag with a `src` attribute.
- Do not add a mode that accepts bare URLs — the HTML tag input is intentional UX.
- If Instagram changes how it exposes full-res URLs, the parsing strategy may need updating but the input contract (HTML tag) should stay stable.

## Evidence

- `docs/technical-design.md` §`instapic.py` — Image Downloader, "Input" and "Why this input model"
- `instapic.py`: `extract_image_url()` uses `BeautifulSoup.find('img')` and returns `img_tag['src']`
- Commit 62eeaf4 (2024-08-10): "download a full res image from instagram"
