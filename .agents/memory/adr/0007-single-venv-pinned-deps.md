---
adr: "0007"
title: Both scripts share a single venv with pinned dependencies in requirements.txt
status: Accepted
date: 2026-04-03
tags: [dependencies, venv, instapic, instareel]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

Both `instapic.py` and `instareel.py` run inside a single shared Python `venv`. All dependencies (`requests`, `beautifulsoup4`, `yt-dlp`) are pinned in `requirements.txt`.

## Rationale

A single venv keeps setup simple for a personal tool — one `pip install -r requirements.txt` activates both. Pinning prevents silent breakage when yt-dlp releases a version that changes Instagram extraction behavior.

## Consequences

- Keep `yt-dlp` pinned and update it explicitly when Instagram changes break downloads — do not use a floating version specifier.
- Do not split into per-script venvs or introduce a heavier package manager (Poetry, pipenv) unless the dependency graph grows substantially more complex.
