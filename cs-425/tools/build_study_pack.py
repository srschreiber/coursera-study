#!/usr/bin/env python3
"""Build LLM-ready bundles from the downloaded course folder. Purely local; no network.

Per week:   Week NN/transcripts.md  - all lecture transcripts in order
            Week NN/study_pack.md   - readings + per-lecture slide text and transcript + quizzes
Course:     README.md               - what's here and what's missing

Usage: python3 build_study_pack.py [course_dir]
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()


def read(p: Path) -> str:
    return p.read_text(errors="replace").strip()


def strip_h1(md: str) -> str:
    """Drop a leading '# Title' line so it can be re-headed at a deeper level."""
    return re.sub(r"^# .*\n+", "", md, count=1)


readme = [f"# {root.name} study pack", "",
          "Everything Coursera had unlocked for this course as of the last run, organized week by week, plus the public FA26 materials from the UIUC course website.", "",
          "**Start here for an LLM:** upload `Week NN/study_pack.md` for each week you're studying. Each one bundles that week's reading pages, every lecture's slide text and transcript, and the quizzes with your graded answers.", "",
          "Per week folder:", "",
          "- `NN - <lecture>/` : slide PDF, extracted slide text (`.pdf.txt`), transcript (`.transcript.txt`)",
          "- `Readings/` : Coursera reading pages as markdown (overviews, instructions, solution links)",
          "- `Quizzes/` : one markdown file per quiz with questions, your answers, correctness, and feedback",
          "- `transcripts.md` : just the transcripts, concatenated",
          "- `study_pack.md` : everything above in one file",
          "- `index.md` : what was found or locked for that week", "",
          "`UIUC Course Site/` holds the FA26 in-class lecture PDFs (with extracted text), homework and MP specification PDFs, and the lecture schedule from courses.grainger.illinois.edu/cs425/fa2026.", "",
          "## Weeks", ""]

for week in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("Week ")):
    lectures = sorted(p for p in week.iterdir() if p.is_dir() and re.match(r"\d\d - ", p.name))
    readings = sorted((week / "Readings").glob("*.md")) if (week / "Readings").exists() else []
    quizzes = sorted((week / "Quizzes").glob("*.md")) if (week / "Quizzes").exists() else []
    n_tx = n_slides = 0

    tx_out = [f"# {week.name}", ""]
    pack = [f"# {week.name}", "",
            f"Contents: {len(readings)} readings, {len(lectures)} lectures, {len(quizzes)} quizzes/assignments.", ""]

    if readings:
        pack += ["## Readings", ""]
        for r in readings:
            pack += [f"### {r.stem[5:] if re.match(r'\d\d - ', r.stem) else r.stem}", "", strip_h1(read(r)), ""]

    if lectures:
        pack += ["## Lectures", ""]
    for lec in lectures:
        tx_out += [f"## {lec.name}", ""]
        pack += [f"### {lec.name}", ""]
        slides = sorted(x for x in lec.iterdir() if x.suffix.lower() in (".pdf", ".pptx", ".ppt"))
        slide_txt = sorted(lec.glob("*.pdf.txt"))
        tx = sorted(lec.glob("*.transcript.txt"))
        if slides:
            n_slides += 1
            pack += ["Slides: " + ", ".join(f"`{s.name}`" for s in slides), ""]
            tx_out += ["Slides: " + ", ".join(s.name for s in slides), ""]
        for st in slide_txt:
            pack += ["#### Slide text", "", "```", read(st), "```", ""]
        if tx:
            n_tx += 1
            body = read(tx[0])
            tx_out += ["### Transcript", "", body, ""]
            pack += ["#### Transcript", "", body, ""]
        else:
            tx_out += ["_No transcript available._", ""]
            pack += ["_No transcript available._", ""]

    if quizzes:
        pack += ["## Quizzes and assignments", ""]
        for q in quizzes:
            pack += [f"### {q.stem}", "", strip_h1(read(q)), ""]

    (week / "transcripts.md").write_text("\n".join(tx_out))
    (week / "study_pack.md").write_text("\n".join(pack))
    locked = 0
    if (week / "index.md").exists():
        locked = read(week / "index.md").count("LOCKED")
    note = f" ({locked} lectures still locked)" if locked else ""
    readme.append(f"- **{week.name}** — {len(lectures)} lectures ({n_tx} transcripts, {n_slides} with slides), "
                  f"{len(readings)} readings, {len(quizzes)} quizzes{note}")
    print(f"{week.name}: {len(lectures)} lectures, {len(readings)} readings, {len(quizzes)} quizzes{note}")

site = root / "UIUC Course Site"
if site.exists():
    pdfs = sorted(site.rglob("*.pdf"))
    readme += ["", "## UIUC Course Site", ""] + [f"- `{p.relative_to(root)}`" for p in pdfs]
    if (site / "lecture_schedule.md").exists():
        readme.append(f"- `{(site / 'lecture_schedule.md').relative_to(root)}`")

(root / "README.md").write_text("\n".join(readme) + "\n")
