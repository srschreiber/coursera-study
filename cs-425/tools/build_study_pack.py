#!/usr/bin/env python3
"""Combine downloaded transcripts into one markdown file per week (plus a course README)
so the material is easy to hand to an LLM. Purely local; no network."""
import re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path.home() / "Documents/Coursera/cs-425")
readme = [f"# {root.name} study pack", "", "Per-week folders contain one subfolder per lecture with the slide PDF and a plain-text transcript.",
          "Each week also has `transcripts.md` (all lecture transcripts for that week, in order) and `index.md` (what was found).",
          "Weeks with quizzes have a `Quizzes/` folder: one markdown file per quiz with the questions, my submitted answers, correctness, and Coursera's feedback.", ""]
for week in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("Week ")):
    lectures = sorted(p for p in week.iterdir() if p.is_dir())
    out = [f"# {week.name}", ""]
    n_tx = n_slides = 0
    for lec in lectures:
        title = re.sub(r"^\d+ - ", "", lec.name)
        out += [f"## {lec.name}", ""]
        slides = sorted(x.name for x in lec.iterdir() if x.suffix.lower() in (".pdf", ".pptx", ".ppt"))
        if slides:
            n_slides += 1
            out += ["Slides: " + ", ".join(slides), ""]
        tx = sorted(lec.glob("*.transcript.txt"))
        if tx:
            n_tx += 1
            text = tx[0].read_text(errors="replace").strip()
            out += ["### Transcript", "", text, ""]
        else:
            out += ["_No transcript available._", ""]
    (week / "transcripts.md").write_text("\n".join(out))
    readme.append(f"- **{week.name}** — {len(lectures)} lectures, {n_tx} transcripts, {n_slides} with slides")
    print(f"{week.name}: {len(lectures)} lectures, {n_tx} transcripts, {n_slides} slide decks")
(root / "README.md").write_text("\n".join(readme) + "\n")
