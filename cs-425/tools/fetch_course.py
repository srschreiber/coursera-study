#!/usr/bin/env python3
"""
Download lecture slides and transcripts for a Coursera course you are enrolled in,
organized week by week.

Usage:
    COURSERA_CAUTH='<cookie value>' python3 fetch_course.py cs-425 [--out DIR] [--list] [--debug]

Auth: the CAUTH cookie from a logged-in coursera.org browser session. It is sent only
as a request header to Coursera-controlled hosts and never written to disk or printed.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://www.coursera.org"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
# Hosts we are willing to send the session cookie to / download from.
ALLOWED_HOST_SUFFIXES = (
    "coursera.org", "coursera-course-assets.s3.amazonaws.com",
    "cloudfront.net", "amazonaws.com", "coursera-university-assets.s3.amazonaws.com",
)
REQUEST_DELAY = 0.4
DEBUG_DIR = None


def host_allowed(url: str) -> bool:
    host = urllib.parse.urlparse(url).hostname or ""
    return any(host == s or host.endswith("." + s) for s in ALLOWED_HOST_SUFFIXES)


def is_coursera(url: str) -> bool:
    host = urllib.parse.urlparse(url).hostname or ""
    return host == "coursera.org" or host.endswith(".coursera.org")


def http_get(url: str, cauth: str, accept: str = "*/*", retries: int = 4):
    if not host_allowed(url):
        raise RuntimeError(f"refusing to fetch non-Coursera host: {url}")
    headers = {"User-Agent": UA, "Accept": accept}
    # Only the coursera.org API needs the session cookie; asset CDNs use signed URLs.
    if is_coursera(url):
        headers["Cookie"] = f"CAUTH={cauth}"
    last_err = None
    for attempt in range(retries):
        try:
            time.sleep(REQUEST_DELAY)
            req = urllib.request.Request(url, headers=headers)
            return urllib.request.urlopen(req, timeout=90)
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise last_err


def api_get(path: str, cauth: str, debug_name: str = None) -> dict:
    url = path if path.startswith("http") else BASE + path
    with http_get(url, cauth, accept="application/json") as r:
        data = json.load(r)
    if DEBUG_DIR and debug_name:
        (DEBUG_DIR / f"{debug_name}.json").write_text(json.dumps(data, indent=1))
    return data


def safe_name(s: str, limit: int = 110) -> str:
    s = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    return s[:limit] or "untitled"


def download(url: str, dest: Path, cauth: str) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    try:
        with http_get(url, cauth) as r, open(tmp, "wb") as f:
            while True:
                chunk = r.read(1 << 16)
                if not chunk:
                    break
                f.write(chunk)
        os.replace(tmp, dest)
        return True
    except Exception as e:  # noqa: BLE001
        if tmp.exists():
            tmp.unlink()
        print(f"      ! failed {dest.name}: {e}", file=sys.stderr)
        return False


# ----------------------------------------------------------------------------- course structure

def get_course(slug: str, cauth: str) -> dict:
    fields = (
        "moduleIds,"
        "onDemandCourseMaterialModules.v1(name,slug,description,lessonIds,optional),"
        "onDemandCourseMaterialLessons.v1(name,slug,elementIds,optional),"
        "onDemandCourseMaterialItems.v2(name,slug,contentSummary,isLocked,itemLockedReasonCode)"
    )
    q = urllib.parse.urlencode({
        "q": "slug", "slug": slug, "includes": "modules,lessons,items",
        "fields": fields, "showLockedItems": "true",
    })
    data = api_get(f"/api/onDemandCourseMaterials.v2/?{q}", cauth, "course")
    course = data["elements"][0]
    linked = data["linked"]
    modules = {m["id"]: m for m in linked["onDemandCourseMaterialModules.v1"]}
    lessons = {l["id"]: l for l in linked["onDemandCourseMaterialLessons.v1"]}
    items = {i["id"]: i for i in linked["onDemandCourseMaterialItems.v2"]}
    ordered = []
    for mid in course.get("moduleIds", list(modules)):
        m = modules[mid]
        m_items = []
        for lid in m.get("lessonIds", []):
            l = lessons.get(lid)
            if not l:
                continue
            for iid in l.get("itemIds") or [e.split("~", 1)[-1] for e in l.get("elementIds", [])]:
                if iid in items:
                    m_items.append((l, items[iid]))
        ordered.append((m, m_items))
    return course["id"], ordered


# ----------------------------------------------------------------------------- lecture assets

def lecture_slide_urls(course_id: str, item_id: str, cauth: str) -> list:
    """Return [(filename, url)] for files attached to a lecture (slides, notes)."""
    out = []
    try:
        data = api_get(
            f"/api/onDemandLectureAssets.v1/{course_id}~{item_id}/?includes=openCourseAssets",
            cauth, f"assets_{item_id}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return out
        raise
    oca = data.get("linked", {}).get("openCourseAssets.v1", [])
    asset_ids, direct = [], []
    for a in oca:
        t = a.get("typeName")
        d = a.get("definition", {})
        if t == "asset" and d.get("assetId"):
            asset_ids.append(d["assetId"])
        elif t == "url" and d.get("url"):
            direct.append((d.get("name") or a.get("name") or "link", d["url"]))
    if asset_ids:
        ids = ",".join(asset_ids)
        adata = api_get(f"/api/assets.v1/{ids}?fields=name,fileExtension,url,typeName",
                        cauth, f"assetfiles_{item_id}")
        for el in adata.get("elements", []):
            url = el.get("url", {})
            url = url.get("url") if isinstance(url, dict) else url
            if not url:
                continue
            name = el.get("name") or "file"
            ext = el.get("fileExtension")
            if ext and not name.lower().endswith("." + ext.lower()):
                name = f"{name}.{ext}"
            out.append((name, url))
    # External links (e.g. Google Drive) can't be fetched; record them in index instead.
    for name, url in direct:
        out.append((name, url))
    return out


def lecture_transcript_urls(course_id: str, item_id: str, cauth: str) -> dict:
    """Return {'txt': url, 'vtt': url, 'srt': url} for the English transcript when present."""
    fields = "onDemandVideos.v1(subtitles,subtitlesVtt,subtitlesTxt)"
    try:
        data = api_get(
            f"/api/onDemandLectureVideos.v1/{course_id}~{item_id}?includes=video&fields={fields}",
            cauth, f"video_{item_id}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}
        raise
    vids = data.get("linked", {}).get("onDemandVideos.v1", [])
    if not vids:
        return {}
    v = vids[0]
    out = {}
    for key, kind in (("subtitlesTxt", "txt"), ("subtitlesVtt", "vtt"), ("subtitles", "srt")):
        subs = v.get(key) or {}
        lang = "en" if "en" in subs else (next(iter(subs), None))
        if lang:
            path = subs[lang]
            out[kind] = path if path.startswith("http") else BASE + path
    return out


# ----------------------------------------------------------------------------- main

def main():
    global DEBUG_DIR, REQUEST_DELAY
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="course slug, e.g. cs-425")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--cauth", default=os.environ.get("COURSERA_CAUTH"))
    ap.add_argument("--list", action="store_true", help="only print the course outline")
    ap.add_argument("--debug", action="store_true", help="save raw API JSON under <out>/<slug>/_debug")
    ap.add_argument("--delay", type=float, default=REQUEST_DELAY)
    ap.add_argument("--week", type=int, help="only process this week number (1-based)")
    args = ap.parse_args()
    REQUEST_DELAY = args.delay

    if not args.cauth:
        sys.exit("Missing CAUTH cookie: set COURSERA_CAUTH or pass --cauth")
    cauth = args.cauth.strip().strip('"').strip("'")

    root = Path(args.out) / args.slug
    if args.debug:
        DEBUG_DIR = root / "_debug"
        DEBUG_DIR.mkdir(parents=True, exist_ok=True)

    try:
        course_id, modules = get_course(args.slug, cauth)
    except urllib.error.HTTPError as e:
        sys.exit(f"Course lookup failed: HTTP {e.code}. If 403, the CAUTH cookie is missing/expired.")

    print(f"Course {args.slug} ({course_id}): {len(modules)} weeks")
    summary = []
    for wi, (mod, entries) in enumerate(modules, 1):
        if args.week and wi != args.week:
            continue
        week_dir = root / safe_name(f"Week {wi:02d} - {mod['name']}")
        lectures = [(l, it) for l, it in entries if it["contentSummary"]["typeName"] == "lecture"]
        print(f"\nWeek {wi:02d}: {mod['name']}  ({len(lectures)} lectures, {len(entries)} items)")
        index_lines = [f"# Week {wi}: {mod['name']}", ""]
        if mod.get("description"):
            index_lines += [mod["description"].strip(), ""]
        for li, (lesson, item) in enumerate(lectures, 1):
            title = item["name"]
            print(f"  {li:02d}. {title}")
            index_lines.append(f"## {li:02d}. {title}")
            index_lines.append(f"- Lesson: {lesson['name']}")
            index_lines.append(f"- URL: {BASE}/learn/{args.slug}/lecture/{item['slug']}")
            if args.list:
                index_lines.append("")
                continue
            if item.get("isLocked"):
                print("      locked:", item.get("itemLockedReasonCode"))
                index_lines += [f"- LOCKED ({item.get('itemLockedReasonCode')})", ""]
                continue
            lec_dir = week_dir / safe_name(f"{li:02d} - {title}")
            got_slides = got_txt = False
            # slides / notes
            try:
                for name, url in lecture_slide_urls(course_id, item["id"], cauth):
                    if not host_allowed(url):
                        index_lines.append(f"- External link: {name}: {url}")
                        continue
                    dest = lec_dir / safe_name(name)
                    ok = download(url, dest, cauth)
                    got_slides |= ok
                    print(f"      {'✓' if ok else '✗'} {dest.name}")
                    index_lines.append(f"- {'Slides' if ok else 'FAILED slides'}: {dest.name}")
            except Exception as e:  # noqa: BLE001
                print(f"      ! slide lookup failed: {e}", file=sys.stderr)
                index_lines.append(f"- slide lookup error: {e}")
            # transcript
            try:
                subs = lecture_transcript_urls(course_id, item["id"], cauth)
                for kind in ("txt", "vtt", "srt"):
                    if kind in subs:
                        dest = lec_dir / safe_name(f"{title}.transcript.{kind}")
                        ok = download(subs[kind], dest, cauth)
                        got_txt |= ok
                        print(f"      {'✓' if ok else '✗'} {dest.name}")
                        index_lines.append(f"- Transcript ({kind}): {dest.name}")
                        if ok and kind == "txt":
                            break  # plain text is enough; skip vtt/srt duplicates
                if not subs:
                    index_lines.append("- No transcript available")
            except Exception as e:  # noqa: BLE001
                print(f"      ! transcript lookup failed: {e}", file=sys.stderr)
                index_lines.append(f"- transcript lookup error: {e}")
            if not got_slides:
                index_lines.append("- No slides attached to this lecture")
            index_lines.append("")
            summary.append((wi, title, got_slides, got_txt))
        week_dir.mkdir(parents=True, exist_ok=True)
        (week_dir / "index.md").write_text("\n".join(index_lines))

    if not args.list:
        n = len(summary)
        print(f"\nDone. {n} lectures; slides for {sum(s for _, _, s, _ in summary)}, "
              f"transcripts for {sum(t for _, _, _, t in summary)}. Output: {root}")


if __name__ == "__main__":
    main()
