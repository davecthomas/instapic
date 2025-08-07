#!/usr/bin/env python3
import sys
import pathlib
from yt_dlp import YoutubeDL


def download_reel(
    url: str, outdir: str = "downloads", cookies: str | None = None
) -> str:
    ydl_opts = {
        "outtmpl": f"{outdir}/%(uploader)s_%(upload_date>%Y-%m-%d)s_%(id)s.%(ext)s",
        "merge_output_format": "mp4",
        "format": "bv*+ba/b",
        "noplaylist": True,
        "restrictfilenames": True,
        "concurrent_fragment_downloads": 4,
        "http_headers": {"User-Agent": "Mozilla/5.0"},
    }
    if cookies:
        ydl_opts["cookiefile"] = cookies

    pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # final path (after merge) will end with .mp4 due to merge_output_format
        return ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp4"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python download_instagram_reel.py <reel_url> [cookies.txt] [outdir]"
        )
        sys.exit(1)
    reel_url = sys.argv[1]
    cookies = sys.argv[2] if len(sys.argv) >= 3 else None
    outdir = sys.argv[3] if len(sys.argv) >= 4 else "downloads"
    path = download_reel(reel_url, outdir, cookies)
    print(f"Saved to {path}")
