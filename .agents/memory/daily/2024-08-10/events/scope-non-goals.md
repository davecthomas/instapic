---
id: scope-non-goals-2024-08-10
type: decision_candidate
timestamp: 2024-08-10T00:00:00Z
bootstrapped_at: 2026-04-03T21:15:06Z
decision_candidate: true
tags: [scope, non-goals, architecture]
title: Explicit scope boundary — personal single-item utility, no bulk/server/carousel
---

## Decision

Instapic is scoped strictly to single-item personal downloads. The following are explicit non-goals:

- Bulk downloading or archiving entire accounts
- Story or carousel/multi-image support
- Any server-side component, API, or web UI
- Authentication beyond cookie-file passthrough

## Rationale

The tool is a personal utility. Scope creep toward account archiving or a web UI would introduce legal/ToS risk, architectural complexity (auth, state, scheduling), and maintenance burden disproportionate to the use case. The design doc calls these out explicitly to prevent feature drift.

## Consequences

- Reject or explicitly ADR any proposal to add bulk download, account-level scraping, carousel iteration, or a service layer.
- If a third media type (e.g. Stories) is added, revisit ADR-0001 on the two-tool split before deciding architecture.

## Evidence

- `docs/technical-design.md` §Non-Goals
- `docs/technical-design.md` §Extension Points and Future Decisions Pending (item 5: carousel noted as unsupported)
- Commit 62eeaf4 (2024-08-10): "download a full res image from instagram" — establishes minimal single-image scope
