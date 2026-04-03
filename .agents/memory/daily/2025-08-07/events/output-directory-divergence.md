---
id: output-directory-divergence-2025-08-07
type: decision_candidate
timestamp: 2025-08-07T08:04:31Z
bootstrapped_at: 2026-04-03T00:00:00Z
decision_candidate: false
promoted_to_adr: "0004"
tags: [output, instapic, instareel, convention]
title: Output directories differ intentionally — ~/Downloads for images, ./downloads for reels
---

## Decision

The two scripts write to different default output locations:

- `instapic.py` — always writes to `~/Downloads/instapic-YYYY-MM-DD.<ext>`. Hardcoded, non-configurable.
- `instareel.py` — defaults to `./downloads/{uploader}_{YYYY-MM-DD}_{id}.mp4` relative to the working directory. Configurable via the third positional CLI argument.

## Rationale

The design doc distinguishes the mental model behind each output location: saving an image "feels like a user-initiated download" (belongs in the OS downloads folder), while saving a reel "feels like a project/batch asset" (belongs near the working directory). These are different interaction modes and warrant different defaults. Making instapic's output configurable was explicitly deferred as a future decision (design doc §Extension Points, item 2).

## Consequences

- Do not unify the two output locations without a new ADR.
- Do not add `--outdir` to `instapic.py` without revisiting this decision.
- instareel's output directory can be overridden at the CLI; instapic's cannot.

## Evidence

- `docs/technical-design.md` §`instapic.py` "Output directory": "hardcoded and non-configurable; individual image saves feel like user-initiated downloads, not project assets"
- `docs/technical-design.md` §`instareel.py` "Output directory": "differs from instapic.py intentionally — reels feel like project/batch assets"
- `docs/technical-design.md` §Output Conventions table
- `docs/technical-design.md` §Extension Points item 2: configurable output path for instapic is explicitly deferred
- Commit ab399e9 (2025-08-07): "instareel - save an mp4 from an instagram reel url" — established ./downloads default
