# ADR index

| ADR | Title | Status | Date | Tags | Must Read | Supersedes | Superseded By |
|---|---|---|---|---|---|---|---|
| [0001](0001-two-tool-split.md) | Two-tool split — images via instapic, video via instareel | Accepted | 2026-04-03 | architecture, tools, scope | yes | — | — |
| [0002](0002-yt-dlp-video-backend.md) | yt-dlp is the canonical video download backend | Accepted | 2026-04-03 | instareel, dependencies, video | no | — | — |
| [0003](0003-instapic-html-tag-input.md) | instapic accepts a raw HTML img tag as input, not a bare URL | Accepted | 2026-04-03 | instapic, input, ux | no | — | — |
| [0004](0004-output-directory-divergence.md) | Output directories differ intentionally — ~/Downloads for images, ./downloads for reels | Accepted | 2026-04-03 | output, instapic, instareel, convention | no | — | — |
| [0005](0005-authentication-model.md) | Authentication model — no auth for images, cookie-file passthrough for reels | Accepted | 2026-04-03 | authentication, instapic, instareel, security | no | — | — |
| [0006](0006-scope-non-goals.md) | Explicit scope boundary — personal single-item utility, no bulk/server/carousel | Accepted | 2026-04-03 | scope, non-goals, architecture | no | — | — |
| [0007](0007-single-venv-pinned-deps.md) | Both scripts share a single venv with pinned dependencies in requirements.txt | Accepted | 2026-04-03 | dependencies, venv, instapic, instareel | no | — | — |
