#!/usr/bin/env python3
"""
Convert a Medium export (the "posts" folder of HTML files) into Jekyll posts.

Usage:
    pip install beautifulsoup4 markdownify requests
    python tools/medium_to_jekyll.py medium-export/posts --out _posts --images assets/img

Options:
    --no-download   keep Medium-hosted image URLs instead of downloading them
    --include-drafts  also convert files starting with "draft_"
"""
import argparse, re, sys
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

try:
    import requests
except ImportError:
    requests = None


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-") or "post"


class MediumConverter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags=None, **kwargs):
        code = el.get_text()
        return f"\n\n```\n{code.strip()}\n```\n\n"

    def convert_figure(self, el, text, parent_tags=None, **kwargs):
        return f"\n\n{text.strip()}\n\n"

    def convert_figcaption(self, el, text, parent_tags=None, **kwargs):
        return f"*{text.strip()}*\n\n" if text.strip() else ""


def download_image(url, img_dir, slug, idx):
    if requests is None:
        return None
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"    ! could not download {url}: {e}", file=sys.stderr)
        return None
    ctype = r.headers.get("content-type", "")
    ext = ".png"
    if "jpeg" in ctype or "jpg" in ctype: ext = ".jpg"
    elif "gif" in ctype: ext = ".gif"
    elif "webp" in ctype: ext = ".webp"
    elif "svg" in ctype: ext = ".svg"
    else:
        suffix = Path(urlparse(url).path).suffix
        if suffix: ext = suffix
    folder = img_dir / slug
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{idx}{ext}"
    (folder / name).write_bytes(r.content)
    return "/" + (folder / name).as_posix().lstrip("/")


def convert_file(path, out_dir, img_dir, download):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    title_el = soup.select_one("h1.p-name") or soup.find("h1") or soup.find("title")
    title = title_el.get_text(strip=True) if title_el else path.stem
    time_el = soup.select_one("time.dt-published")
    date = (time_el.get("datetime") if time_el else "")[:10] or path.stem[:10]
    subtitle_el = soup.select_one("section[data-field=subtitle]")
    subtitle = subtitle_el.get_text(strip=True) if subtitle_el else ""
    canon_el = soup.select_one("a.p-canonical")
    canonical = canon_el.get("href", "") if canon_el else ""

    body = soup.select_one("section[data-field=body]") or soup.body
    # drop the duplicated title/subtitle inside the body
    for sel in ("h1.p-name", "section[data-field=subtitle]", "hr.section-divider"):
        for el in body.select(sel):
            el.decompose()

    slug = slugify(title)
    # images
    first_image = None
    for i, img in enumerate(body.find_all("img"), 1):
        src = img.get("src", "")
        if not src:
            continue
        new = download_image(src, img_dir, f"{date}-{slug}", i) if download else None
        if new:
            img["src"] = new
        if first_image is None:
            first_image = img["src"]

    md = MediumConverter(heading_style="ATX", bullets="-", code_language="").convert_soup(body)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"

    safe_title = title.replace('"', '\\"')
    fm = ["---", "layout: post", f'title: "{safe_title}"', f"date: {date}"]
    if subtitle:
        fm.append(f'description: "{subtitle.replace(chr(34), chr(92) + chr(34))}"')
    if first_image:
        fm.append(f"image: {first_image}")
    if canonical:
        fm.append(f"medium_url: {canonical}")
    fm.append("---\n")

    out = out_dir / f"{date}-{slug}.md"
    out.write_text("\n".join(fm) + "\n" + md, encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("posts_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("_posts"))
    ap.add_argument("--images", type=Path, default=Path("assets/img"))
    ap.add_argument("--no-download", action="store_true")
    ap.add_argument("--include-drafts", action="store_true")
    a = ap.parse_args()

    a.out.mkdir(parents=True, exist_ok=True)
    files = sorted(a.posts_dir.glob("*.html"))
    n = 0
    for f in files:
        if f.name.startswith("draft_") and not a.include_drafts:
            continue
        print(f"Converting {f.name}")
        print("  ->", convert_file(f, a.out, a.images, not a.no_download))
        n += 1
    print(f"\nDone: {n} posts converted into {a.out}/")


if __name__ == "__main__":
    main()
