# tools

Scripts that built this folder. Python 3 standard library only.

All network scripts need your Coursera session cookie in `COURSERA_CAUTH` (DevTools > Application > Cookies > coursera.org > `CAUTH`). The cookie is sent only to coursera.org and is never written to disk. It expires after a while; grab a fresh one if you get HTTP 403.

```
# lecture slides + transcripts (resumable; only downloads what's missing)
COURSERA_CAUTH='...' python3 fetch_course.py cs-425 --out ..

# quizzes/assignments with your submitted answers and Coursera's feedback
COURSERA_CAUTH='...' python3 fetch_quizzes.py cs-425 --out ..

# rebuild per-week transcripts.md and the course README (local only)
python3 build_study_pack.py ../cs-425
```

`fetch_quizzes.py` uses the same GraphQL query (`AssignmentFeedback`) that Coursera's quiz results page issues; the query text lives in `graphql_docs.json`. It never starts or submits an attempt, so it only returns questions for quizzes you've already submitted.

Locked items (timed-release content) are skipped and listed in each week's `index.md`; rerun after Coursera unlocks them.
