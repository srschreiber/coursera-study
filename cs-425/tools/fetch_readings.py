#!/usr/bin/env python3
"""
Download the reading/supplement pages of a Coursera course you're enrolled in (syllabus,
week overviews, homework solutions, ...) as markdown, plus any attached files (PDFs etc).

Usage:
    COURSERA_CAUTH='<cookie>' python3 fetch_readings.py cs-425 [--out DIR] [--debug]
"""
import argparse
import html
import json
import os
import re
import sys
import urllib.error
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_course as fc  # noqa: E402


class CmlToMarkdown(HTMLParser):
    """Very small converter for Coursera CML (an XML dialect close to HTML)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.assets = []       # asset ids referenced by <asset .../>
        self.list_stack = []
        self.in_code = False
        self.href = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "heading":
            lvl = int(a.get("level", "2") or 2)
            self.out.append("\n\n" + "#" * min(max(lvl, 1), 6) + " ")
        elif tag == "text":
            self.out.append("\n\n")
        elif tag == "list":
            self.list_stack.append(a.get("bulletType", "bullets"))
            self.out.append("\n")
        elif tag == "li":
            bullet = "1." if self.list_stack and self.list_stack[-1] == "numbers" else "-"
            self.out.append("\n" + "  " * (len(self.list_stack) - 1) + bullet + " ")
        elif tag == "asset":
            if a.get("id"):
                self.assets.append(a["id"])
            self.out.append(f"\n\n[Attachment: {a.get('name', '')}.{a.get('extension', '')}]\n\n")
        elif tag == "img":
            self.out.append(f" [image: {a.get('src', '')}] ")
        elif tag == "a":
            self.href = a.get("href")
            self.out.append("[")
        elif tag == "code":
            self.in_code = True
            self.out.append("\n\n```\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "table":
            self.out.append("\n\n")
        elif tag == "tr":
            self.out.append("\n| ")
        elif tag in ("td", "th"):
            pass

    def handle_endtag(self, tag):
        if tag == "list":
            if self.list_stack:
                self.list_stack.pop()
            self.out.append("\n")
        elif tag == "a":
            self.out.append(f"]({self.href or ''})")
            self.href = None
        elif tag == "code":
            self.in_code = False
            self.out.append("\n```\n\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag in ("td", "th"):
            self.out.append(" | ")

    def handle_data(self, data):
        if self.in_code:
            self.out.append(data)
        else:
            self.out.append(re.sub(r"\s+", " ", data))

    def markdown(self) -> str:
        txt = html.unescape("".join(self.out))
        txt = re.sub(r"[ \t]+\n", "\n", txt)
        txt = re.sub(r"\n{3,}", "\n\n", txt)
        return txt.strip()


def fetch_supplement(course_id: str, item_id: str, cauth: str, debug_name=None):
    """Return (markdown, [(filename, url)]) for a supplement item."""
    q = ("includes=asset&fields=openCourseAssets.v1(typeName),openCourseAssets.v1(definition)")
    data = fc.api_get(f"/api/onDemandSupplements.v1/{course_id}~{item_id}?{q}", cauth, debug_name)
    assets = data.get("linked", {}).get("openCourseAssets.v1", [])
    md_parts, asset_ids, files = [], [], []
    for a in assets:
        t = a.get("typeName")
        d = a.get("definition") or {}
        if t == "cml":
            conv = CmlToMarkdown()
            conv.feed(d.get("value") or "")
            md_parts.append(conv.markdown())
            asset_ids += conv.assets
        elif t == "asset" and d.get("assetId"):
            asset_ids.append(d["assetId"])
        elif t == "url" and d.get("url"):
            md_parts.append(f"[{d.get('name') or d['url']}]({d['url']})")
    # resolve attachments
    seen = set()
    ids = [i for i in asset_ids if not (i in seen or seen.add(i))]
    if ids:
        adata = fc.api_get(f"/api/assets.v1/{','.join(ids)}?fields=name,fileExtension,url", cauth,
                           (debug_name + "_assets") if debug_name else None)
        for el in adata.get("elements", []):
            url = el.get("url", {})
            url = url.get("url") if isinstance(url, dict) else url
            if not url:
                continue
            name = el.get("name") or "file"
            ext = el.get("fileExtension")
            if ext and not name.lower().endswith("." + ext.lower()):
                name = f"{name}.{ext}"
            files.append((name, url))
    return "\n\n".join(p for p in md_parts if p), files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--cauth", default=os.environ.get("COURSERA_CAUTH"))
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()
    if not args.cauth:
        sys.exit("Missing CAUTH cookie: set COURSERA_CAUTH or pass --cauth")
    cauth = args.cauth.strip()
    root = Path(args.out) / args.slug
    if args.debug:
        fc.DEBUG_DIR = root / "_debug"
        fc.DEBUG_DIR.mkdir(parents=True, exist_ok=True)

    course_id, modules = fc.get_course(args.slug, cauth)
    done = skipped = failed = 0
    for wi, (mod, entries) in enumerate(modules, 1):
        readings = [(l, it) for l, it in entries if it["contentSummary"]["typeName"] == "supplement"]
        if not readings:
            continue
        week_dir = root / fc.safe_name(f"Week {wi:02d} - {mod['name']}")
        print(f"\nWeek {wi:02d}: {mod['name']}")
        for ri, (lesson, item) in enumerate(readings, 1):
            title = item["name"]
            if item.get("isLocked"):
                print(f"  - {title}: locked")
                skipped += 1
                continue
            try:
                md, files = fetch_supplement(course_id, item["id"], cauth,
                                             f"supp_{item['id']}" if args.debug else None)
                rdir = week_dir / "Readings"
                rdir.mkdir(parents=True, exist_ok=True)
                url = f"{fc.BASE}/learn/{args.slug}/supplement/{item['id']}/{item['slug']}"
                body = [f"# {title}", "", f"- Coursera: {url}", f"- Lesson: {lesson['name']}", ""]
                got = []
                for name, furl in files:
                    if not fc.host_allowed(furl):
                        body.append(f"- External link: {name}: {furl}")
                        continue
                    dest = rdir / fc.safe_name(f"{ri:02d} - {name}")
                    if fc.download(furl, dest, cauth):
                        got.append(dest.name)
                if got:
                    body.append("Attachments: " + ", ".join(f"`{g}`" for g in got))
                    body.append("")
                body.append(md or "_(empty page)_")
                (rdir / fc.safe_name(f"{ri:02d} - {title}.md")).write_text("\n".join(body) + "\n")
                print(f"  ✓ {title}" + (f"  [+{len(got)} file(s): {', '.join(got)}]" if got else ""))
                done += 1
            except Exception as e:  # noqa: BLE001
                print(f"  ✗ {title}: {e}", file=sys.stderr)
                failed += 1
    print(f"\nDone. readings {done}, locked {skipped}, failed {failed}")


if __name__ == "__main__":
    main()
