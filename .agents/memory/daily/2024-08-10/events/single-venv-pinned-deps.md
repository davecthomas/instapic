---
id: single-venv-pinned-deps-2024-08-10
type: decision_candidate
timestamp: 2024-08-10T00:00:00Z
bootstrapped_at: 2026-04-03T21:15:06Z
decision_candidate: true
tags: [dependencies, venv, instapic, instareel]
title: Both scripts share a single venv with pinned dependencies in requirements.txt
---

## Decision

Both `instapic.py` and `instareel.py` run inside a single shared Python `venv`. All dependencies (`requests`, `beautifulsoup4`, `yt-dlp`) are pinned in `requirements.txt`.

## Rationale

Despite the scripts being independent executables, a single venv keeps setup simple for a personal tool — one `pip install -r requirements.txt` activates both. Pinning prevents silent breakage when yt-dlp releases a version that changes Instagram extraction behavior.

## Consequences

- Keep `yt-dlp` pinned and update it explicitly when Instagram changes break downloads (not via float/wildcard).
- Do not split into per-script venvs or introduce a package manager (Poetry, pipenv) unless the dependency graph becomes more complex.

## Evidence

- `docs/technical-design.md` §Dependency Model
- `README.md` install instructions: single `venv` + `requirements.txt`
- Commit 62eeaf4 (2024-08-10): "download a full res image from instagram" — established venv-based setup
