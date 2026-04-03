# Instapic — Technical Design

## Overview

Instapic is a personal command-line utility for saving Instagram media locally. It is composed of two independent scripts: one for saving full-resolution images (`instapic.py`) and one for saving video Reels as MP4 files (`instareel.py`). There is no shared runtime, no server, and no database.

---

## Goals

- Save the full-resolution version of an Instagram image to disk with a single command.
- Save an Instagram Reel as an MP4 with a single command.
- Keep dependencies minimal and the scripts independently runnable.

## Non-Goals

- Bulk downloading or archiving accounts.
- Story or carousel support.
- Any server-side component, API, or web UI.
- Authentication beyond cookie file passthrough.

---

## Components

### `instapic.py` — Image Downloader

**Input:** A raw HTML `<img>` tag string, copy-pasted from the browser's DevTools Elements panel.

**Why this input model:** Instagram's full-resolution `src` URL is embedded in the `<img>` tag but is not easily bookmarkable or copy-linkable from the UI. Accepting the raw tag lets the user copy the entire element without having to manually extract the URL.

**Processing:**
1. `BeautifulSoup` parses the tag and extracts the `src` attribute.
2. The image URL is opened in the default browser (preview).
3. The file extension is inferred from the URL path; defaults to `jpg` if unrecognized.
4. The file is saved to `~/Downloads/instapic-YYYY-MM-DD.<ext>`.

**Output directory:** Always `~/Downloads`. This is hardcoded and non-configurable; individual image saves feel like user-initiated downloads, not project assets.

**Dependencies:** `requests`, `beautifulsoup4`

**Known limitations:**
- No timeout on the HTTP download request.
- Filename uses only the date, causing silent overwrite if run more than once per day.
- No error handling for network failures (raises unhandled exception).

---

### `instareel.py` — Reel Downloader

**Input:** A direct Instagram Reel URL (e.g. `https://www.instagram.com/reel/ABC123/`). Optionally, a Netscape-format cookies file path and an output directory.

**Why URL-based input:** Reel URLs are directly shareable and stable enough to use as input. No HTML parsing is needed because yt-dlp's Instagram extractor handles session-scoped media URL resolution internally.

**Processing:**
1. `yt-dlp` extracts media info and selects the best video+audio format (`bv*+ba/b`).
2. Fragments are downloaded concurrently (4 workers) and merged into a single `.mp4` via `merge_output_format`.
3. Output filename is `{uploader}_{upload_date}_{id}.mp4` under the output directory.

**Output directory:** Defaults to `./downloads` (relative to working directory). Configurable via positional CLI argument. This differs from `instapic.py` intentionally — reels feel like project/batch assets, not one-off user downloads.

**Authentication:** Cookie file passthrough via `yt-dlp`'s `--cookiefile` option. No OAuth or session management is implemented in this script.

**Dependencies:** `yt-dlp`

**Known limitations:**
- `prepare_filename` path reconstruction (stripping extension, appending `.mp4`) may diverge from the actual merged output path in edge cases.
- Argument parsing uses raw `sys.argv` rather than `argparse`; usage string still references the original script name `download_instagram_reel.py`.
- No URL validation before passing to yt-dlp.

---

## Dependency Model

| Script | Key Dependencies | Rationale |
|---|---|---|
| `instapic.py` | `requests`, `beautifulsoup4` | Lightweight; no need for a full browser or video stack |
| `instareel.py` | `yt-dlp` | Handles Instagram's rotating session-scoped media URLs; actively maintained |

Both scripts run inside a single `venv`. Dependencies are pinned in `requirements.txt`.

---

## Authentication Model

- **Images:** No authentication. Full-res `src` URLs from public posts are directly fetchable with a plain `requests.get`.
- **Reels:** Optional cookie file. For private or age-gated content, the user exports cookies from their browser (e.g. via a browser extension) and passes the path as the second CLI argument. No credentials are stored by the scripts themselves.

---

## Output Conventions

| Script | Default Output Location | Filename Pattern | Configurable |
|---|---|---|---|
| `instapic.py` | `~/Downloads/` | `instapic-YYYY-MM-DD.<ext>` | No |
| `instareel.py` | `./downloads/` | `{uploader}_{YYYY-MM-DD}_{id}.mp4` | Yes (3rd arg) |

---

## Extension Points and Future Decisions Pending

The following are open questions that have not yet been decided. They are candidates for future ADRs:

1. **Unified entry point vs. separate scripts** — Should a future `instagram.py` dispatcher wrap both tools under subcommands (`image`, `reel`)? ADR-0001 currently favors separation; revisit if a third media type is added.

2. **Configurable output path for instapic** — Currently hardcoded to `~/Downloads`. If the script is used in automation or CI-like contexts, a `--outdir` flag would be needed.

3. **Filename collision strategy for instapic** — The date-only filename is a known bug. Options: append seconds to the timestamp, append a counter, or hash the URL. No decision made.

4. **Argument parsing consistency** — `instapic.py` uses `argparse`; `instareel.py` uses raw `sys.argv`. Standardizing on `argparse` across both would be a minor but reviewable change.

5. **Carousel/multi-image support** — Not currently supported. Would require iterating over multiple `<img>` tags or using yt-dlp's playlist support.
