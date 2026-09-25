# tools

Scripts that built this folder. Python 3 standard library only; `extract_slides.py` needs poppler's `pdftotext` (`brew install poppler`).

Network scripts need your Coursera session cookie in `COURSERA_CAUTH` (Chrome DevTools > Application > Cookies > coursera.org > `CAUTH`). The cookie is sent only to coursera.org and never written to disk. It expires; grab a fresh one if you get HTTP 403. Locked (timed-release) items are skipped and listed in each week's `index.md`; rerun after Coursera unlocks them.

Full refresh, in order:

```
cd cs-425/tools
export COURSERA_CAUTH='...'
python3 fetch_course.py cs-425      # lecture slides + transcripts (resumable)
python3 fetch_readings.py cs-425    # reading pages as markdown, plus attachments
python3 fetch_quizzes.py cs-425     # quizzes/assignments with your answers and feedback
python3 extract_slides.py           # PDF -> .pdf.txt next to every slide deck
python3 build_study_pack.py         # per-week transcripts.md + study_pack.md, course README
```

Notes:

- `fetch_quizzes.py` replays the read-only GraphQL query (`AssignmentFeedback`, text in `graphql_docs.json`) that Coursera's quiz results page issues. It never starts or submits an attempt, so quizzes you haven't submitted come back empty.
- `fetch_readings.py` converts Coursera CML markup to markdown and downloads any attached files it references.
- `UIUC Course Site/` was pulled by hand from the public course website (courses.grainger.illinois.edu/cs425/fa2026): FA26 lecture PDFs, HW/MP specs, and the lecture schedule.
