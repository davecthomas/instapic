---
date: 2024-08-10
generated_at: 2026-04-03T21:15:06Z
bootstrapped: true
---

# Summary — 2024-08-10

## Decision candidates

- **two-tool-split** — Two independent scripts (instapic for images, instareel for video) with no shared runtime; split because images and video require fundamentally different download mechanisms. Promoted → ADR-0001. See `events/two-tool-split.md`.
- **instapic-html-tag-input** — instapic accepts a raw HTML `<img>` tag (not a bare URL) because Instagram's full-res src is not directly copy-linkable from the UI. Promoted → ADR-0003. See `events/instapic-html-tag-input.md`.
- **scope-non-goals** — Explicit scope boundary defined: personal single-item utility only; no bulk downloading, carousel/story support, or server/API layer. Promoted → ADR-0006. See `events/scope-non-goals.md`.
- **single-venv-pinned-deps** — Both scripts share a single venv with all dependencies pinned in requirements.txt. Promoted → ADR-0007. See `events/single-venv-pinned-deps.md`.

## Commits

- 62eeaf4 — "download a full res image from instagram": established instapic.py with BeautifulSoup img-tag parsing, requests download, and ~/Downloads output.
- 4c23ca8 — "no changes": no substantive change.
