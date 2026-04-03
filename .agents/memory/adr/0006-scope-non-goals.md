---
adr: "0006"
title: Explicit scope boundary — personal single-item utility, no bulk/server/carousel
status: Accepted
date: 2026-04-03
tags: [scope, non-goals, architecture]
must_read: false
supersedes: ~
superseded_by: ~
---

## Decision

Instapic is scoped strictly to single-item personal downloads. The following are explicit non-goals:

- Bulk downloading or archiving entire accounts
- Story or carousel/multi-image support
- Any server-side component, API, or web UI
- Authentication beyond cookie-file passthrough

## Rationale

The tool is a personal utility. Scope creep toward account archiving or a web UI would introduce legal/ToS risk, architectural complexity (auth, state, scheduling), and maintenance burden disproportionate to the use case.

## Consequences

- Reject or explicitly ADR any proposal to add bulk download, account-level scraping, carousel iteration, or a service layer.
- If a third media type (e.g. Stories) is added, revisit ADR-0001 on the two-tool split before deciding architecture.
