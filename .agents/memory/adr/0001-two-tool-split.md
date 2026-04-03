---
adr: "0001"
title: Two-tool split — images via instapic, video via instareel
status: Accepted
date: 2026-04-03
tags: [architecture, tools, scope]
must_read: true
supersedes: ~
superseded_by: ~
---

## Decision

The project is implemented as two independent CLI scripts rather than one unified tool:

- **instapic.py** — downloads a single full-resolution image; input is a raw HTML `<img>` tag pasted from browser DevTools.
- **instareel.py** — downloads an MP4 from a Reel URL; input is a direct Instagram URL.

## Rationale

The input model, library stack, and output destination differ enough between images and video that a unified entry point would add complexity (subcommand routing, shared arg parsing) without meaningful benefit for a personal utility.

## Consequences

- New capabilities should be added as separate scripts (or as arguments to the relevant existing script) rather than merged into a single dispatcher.
- Each script can evolve its dependencies independently.
