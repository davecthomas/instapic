---
adr: "0004"
title: Output directories differ intentionally — ~/Downloads for images, ./downloads for reels
status: Accepted
date: 2026-04-03
tags: [output, instapic, instareel, convention]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

- `instapic.py` saves to `~/Downloads/` — hardcoded, non-configurable.
- `instareel.py` saves to `./downloads/` relative to the working directory — configurable via the 3rd CLI argument.

## Rationale

Single images feel like user-initiated OS-level downloads; `~/Downloads` is the natural destination. Reels feel like batch/project assets that belong near the working directory. Unifying these defaults would degrade the UX of one or both tools.

## Consequences

- Do not add `--outdir` to `instapic.py` unless a concrete automation use case requires it.
- Do not change `instareel.py`'s default to `~/Downloads` — it would break scripts and pipelines that rely on output landing in the working directory.
- If a third media type is added, decide its output convention explicitly rather than inheriting from either existing script.
