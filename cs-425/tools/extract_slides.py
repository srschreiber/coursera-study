#!/usr/bin/env python3
"""Extract text from every PDF under the course folder into a sibling <name>.pdf.txt file,
so slides can be pasted into an LLM as plain text. Local only; uses poppler's pdftotext.

Usage: python3 extract_slides.py [course_dir]
"""
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
tool = shutil.which("pdftotext")
if not tool:
    sys.exit("pdftotext not found (brew install poppler)")

done = skipped = failed = 0
for pdf in sorted(root.rglob("*.pdf")):
    if "_debug" in pdf.parts or not pdf.resolve().is_relative_to(root):
        continue
    dest = pdf.with_name(pdf.name + ".txt")
    if dest.exists() and dest.stat().st_mtime >= pdf.stat().st_mtime:
        skipped += 1
        continue
    try:
        subprocess.run([tool, "-layout", "-enc", "UTF-8", str(pdf), str(dest)],
                       check=True, timeout=120, capture_output=True)
        # squeeze runs of blank lines
        lines = dest.read_text(errors="replace").splitlines()
        out, blank = [], 0
        for ln in lines:
            ln = ln.rstrip()
            blank = blank + 1 if not ln else 0
            if blank <= 1:
                out.append(ln)
        dest.write_text("\n".join(out).strip() + "\n")
        done += 1
    except Exception as e:  # noqa: BLE001
        print(f"! {pdf.relative_to(root)}: {e}", file=sys.stderr)
        failed += 1
print(f"extracted {done}, up-to-date {skipped}, failed {failed}")
