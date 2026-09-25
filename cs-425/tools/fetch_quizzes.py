#!/usr/bin/env python3
"""
Export the quizzes/assignments of a Coursera course you're enrolled in, with your submitted
answers and Coursera's grading feedback, as markdown in each week's folder.

Uses the same GraphQL query the Coursera quiz results page issues (AssignmentFeedback), which
returns only feedback for attempts you have already submitted. It never starts or submits an attempt.

Usage:
    COURSERA_CAUTH='<cookie>' python3 fetch_quizzes.py cs-425 [--item ID] [--out DIR]
"""
import argparse
import html
import json
import os
import random
import string
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_course as fc  # noqa: E402

DOCS = json.load(open(Path(__file__).resolve().parent / "graphql_docs.json"))
QUIZ_TYPES = {"staffGraded", "ungradedAssignment", "quiz", "exam"}


def csrf_token() -> str:
    rnd = "".join(random.choices(string.ascii_letters + string.digits, k=20))
    return f"{int(time.time())}.{rnd}"


def graphql(opname: str, variables: dict, cauth: str) -> dict:
    url = f"{fc.BASE}/graphql-gateway?opname={opname}"
    tok = csrf_token()
    body = json.dumps([{"operationName": opname, "variables": variables, "query": DOCS[opname]}]).encode()
    headers = {
        "User-Agent": fc.UA, "Accept": "application/json", "Content-Type": "application/json",
        "Origin": fc.BASE, "Referer": f"{fc.BASE}/",
        "X-Coursera-Application": "ondemand", "apollographql-client-name": "ondemand",
        "X-CSRF3-Token": tok, "Cookie": f"CAUTH={cauth}; CSRF3-Token={tok}",
    }
    for attempt in range(4):
        try:
            time.sleep(fc.REQUEST_DELAY)
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=90) as r:
                data = json.load(r)
            return data[0] if isinstance(data, list) else data
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {e.read()[:300]!r}")


# ----------------------------------------------------------------------------- rendering helpers

class _Text(HTMLParser):
    BLOCK = {"p", "div", "li", "br", "tr", "h1", "h2", "h3", "h4", "pre", "ul", "ol", "table"}

    def __init__(self):
        super().__init__()
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.out.append("\n- ")
        elif tag in self.BLOCK:
            self.out.append("\n")
        elif tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.out.append(f" [image: {src}] ")

    def handle_endtag(self, tag):
        if tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        self.out.append(data)


def content_text(c) -> str:
    """Render a Submission_*Content object (CML or HTML) as plain text."""
    if not c:
        return ""
    h = None
    if isinstance(c, dict):
        h = (c.get("htmlWithMetadata") or {}).get("html") or c.get("value") or c.get("cmlValue")
    else:
        h = str(c)
    if not h:
        return ""
    p = _Text()
    p.feed(h)
    txt = html.unescape("".join(p.out))
    lines = [ln.rstrip() for ln in txt.splitlines()]
    out, blank = [], False
    for ln in lines:
        if ln.strip():
            out.append(ln)
            blank = False
        elif not blank:
            out.append("")
            blank = True
    return "\n".join(out).strip()


def render_part(idx: int, p: dict) -> list:
    """Render one feedback part (question or text block) to markdown lines."""
    lines = []
    if "title" in p and "body" in p:  # TextBlock
        lines.append(f"**{p.get('title') or 'Note'}**")
        lines.append(content_text(p.get("body")))
        return lines

    schema = p.get("questionSchema") or {}
    fb = p.get("feedback") or {}
    correctness = fb.get("correctness")
    outcome = fb.get("autoGradedFeedbackOutcome") or fb.get("manuallyGradedFeedbackOutcome") or {}
    score = ""
    if outcome:
        score = f" ({outcome.get('score')}/{outcome.get('maxScore')} pts)"
    mark = {"CORRECT": "✅ correct", "INCORRECT": "❌ incorrect", "PARTIALLY_CORRECT": "🟡 partially correct"}.get(
        correctness, correctness or "")
    lines.append(f"### Q{idx}{score} {mark}".rstrip())
    lines.append("")
    lines.append(content_text(schema.get("prompt")))
    lines.append("")

    # ---- multiple choice (single answer)
    if "multipleChoiceResponse" in p or "multipleChoiceReflectResponse" in p:
        resp = p.get("multipleChoiceResponse") or p.get("multipleChoiceReflectResponse") or {}
        chosen = resp.get("chosen")
        for o in schema.get("options", []):
            oid = o.get("optionId")
            tag = "(x)" if oid == chosen else "( )"
            note = ""
            if oid == chosen:
                note = "  ← your answer, CORRECT" if correctness == "CORRECT" else (
                    "  ← your answer, incorrect" if correctness == "INCORRECT" else "  ← your answer")
            lines.append(f"- {tag} {content_text(o.get('display'))}{note}")
        if correctness != "CORRECT":
            lines.append("")
            lines.append("_Correct option not revealed for this attempt._")
    # ---- checkbox (multiple answers)
    elif "checkboxResponse" in p or "checkboxReflectResponse" in p:
        resp = p.get("checkboxResponse") or p.get("checkboxReflectResponse") or {}
        chosen = set(resp.get("chosen") or [])
        for o in schema.get("options", []):
            oid = o.get("optionId")
            was = oid in chosen
            ca = o.get("correctlyAnswered")
            # correctlyAnswered means your choice for this option (checked or not) was right.
            should = was if ca else (not was) if ca is not None else None
            tag = "[x]" if was else "[ ]"
            if should is None:
                verdict = ""
            elif should:
                verdict = "  ✅ correct answer" + ("" if was else " (you missed it)")
            else:
                verdict = "  (not a correct answer)" + (" ← you selected it" if was else "")
            lines.append(f"- {tag} {content_text(o.get('display'))}{verdict}")
            ofb = content_text(o.get("feedback"))
            if ofb:
                lines.append(f"    - feedback: {ofb}")
    # ---- exact text / numeric / regex / math
    elif "textExactMatchResponse" in p:
        lines.append(f"- Your answer: `{(p['textExactMatchResponse'] or {}).get('answer')}`")
        ca = [a.get("answer") for a in schema.get("correctAnswers", [])]
        if ca:
            lines.append(f"- Correct answer(s): {', '.join(f'`{a}`' for a in ca)}")
    elif "numericResponse" in p or "regexResponse" in p or "mathResponse" in p or "textReflectResponse" in p:
        resp = p.get("numericResponse") or p.get("regexResponse") or p.get("mathResponse") or p.get("textReflectResponse") or {}
        lines.append(f"- Your answer: `{resp.get('answer')}`" + ("  ✅ (correct)" if correctness == "CORRECT" else ""))
    # ---- fillable blanks
    elif "multipleFillableBlanksResponse" in p:
        chosen = {r.get("responseId"): r.get("optionId")
                  for r in (p["multipleFillableBlanksResponse"] or {}).get("responses", [])}
        for bi, b in enumerate(schema.get("fillableBlanks", []), 1):
            sel = chosen.get(b.get("fillableBlankId"))
            lines.append(f"- Blank {bi}: {'✅' if b.get('isCorrect') else '❌'}")
            for o in b.get("answerOptions", []):
                tag = "(x)" if o.get("optionId") == sel else "( )"
                lines.append(f"    - {tag} {content_text(o.get('display'))}")
    # ---- free text / rich text / upload (manually graded)
    elif "plainTextResponse" in p:
        lines.append("Your answer:")
        lines.append("")
        lines.append(content_text((p["plainTextResponse"] or {}).get("plainText")))
    elif "richTextResponse" in p:
        lines.append("Your answer:")
        lines.append("")
        lines.append(content_text(((p["richTextResponse"] or {}).get("richText"))))
    elif "fileUploadResponse" in p:
        r = p["fileUploadResponse"] or {}
        lines.append(f"- Uploaded: {r.get('title')} {r.get('fileUrl')}")
    elif "urlResponse" in p:
        r = p["urlResponse"] or {}
        lines.append(f"- URL submitted: {r.get('url')}")
    else:
        lines.append("```json")
        lines.append(json.dumps({k: v for k, v in p.items() if k != "questionSchema"}, indent=1)[:2000])
        lines.append("```")

    # question-level feedback text
    qfb = content_text(fb.get("feedback"))
    if qfb:
        lines.append("")
        lines.append(f"> Feedback: {qfb}")
    # rubric feedback (manually graded)
    for rb in fb.get("rubrics") or []:
        lines.append("")
        lines.append(f"> Rubric: {content_text(rb.get('prompt'))}")
        for o in rb.get("options") or []:
            lines.append(f">   - {'(x)' if o.get('selected') else '( )'} {content_text(o.get('display'))} [{o.get('points')} pts]")
        if rb.get("score") is not None:
            lines.append(f">   score {rb.get('score')}/{rb.get('maxScore')}")
    lines.append("")
    return lines


def render_quiz(title: str, item: dict, state: dict, status: dict, url: str) -> str:
    lines = [f"# {title}", "", f"- Coursera: {url}", f"- Item type: {item['contentSummary']['typeName']}"]
    if status:
        eg = (status.get("outcome") or {}).get("earnedGrade")
        lines.append(f"- Grading status: {status.get('gradingStatus')}" + (f", earned grade {eg}" if eg is not None else ""))
    fb = state.get("feedback") or {}
    oc = fb.get("outcome") or {}
    if oc:
        lines.append(f"- Score: latest {oc.get('latestScore')}, highest {oc.get('highestScore')}, max {oc.get('maxScore')}")
    lines.append("")
    instr = fb.get("instructions") or {}
    ov = content_text(instr.get("overview"))
    if ov:
        lines += ["## Instructions", "", ov, ""]
    parts = fb.get("parts") or []
    qn = 0
    lines.append("## Questions")
    lines.append("")
    for p in parts:
        if not ("title" in p and "body" in p):
            qn += 1
        lines += render_part(qn, p)
    if not parts:
        lines.append("_No submitted attempt found, so Coursera returned no questions or feedback._")
    return "\n".join(lines)


# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--cauth", default=os.environ.get("COURSERA_CAUTH"))
    ap.add_argument("--item", help="only this item id")
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()
    if not args.cauth:
        sys.exit("Missing CAUTH cookie: set COURSERA_CAUTH or pass --cauth")
    cauth = args.cauth.strip()
    root = Path(args.out) / args.slug
    dbg = root / "_debug"
    dbg.mkdir(parents=True, exist_ok=True)

    course_id, modules = fc.get_course(args.slug, cauth)
    done = skipped = failed = 0
    for wi, (mod, entries) in enumerate(modules, 1):
        quizzes = [(l, it) for l, it in entries if it["contentSummary"]["typeName"] in QUIZ_TYPES]
        if args.item:
            quizzes = [(l, it) for l, it in quizzes if it["id"] == args.item]
        if not quizzes:
            continue
        week_dir = root / fc.safe_name(f"Week {wi:02d} - {mod['name']}")
        print(f"\nWeek {wi:02d}: {mod['name']}")
        for lesson, item in quizzes:
            title = item["name"]
            url = f"{fc.BASE}/learn/{args.slug}/assignment-submission/{item['id']}/{item['slug']}"
            if item.get("isLocked"):
                print(f"  - {title}: locked ({item.get('itemLockedReasonCode')})")
                skipped += 1
                continue
            try:
                vars_ = {"courseId": course_id, "itemId": item["id"]}
                fbres = graphql("AssignmentFeedback", vars_, cauth)
                stres = graphql("AssignmentGradingStatus", vars_, cauth)
                if args.debug:
                    (dbg / f"quiz_{item['id']}.json").write_text(json.dumps({"feedback": fbres, "status": stres}, indent=1))
                if fbres.get("errors"):
                    raise RuntimeError(f"GraphQL errors: {fbres['errors']}")
                state = ((fbres.get("data") or {}).get("SubmissionState") or {}).get("queryState") or {}
                status = ((stres.get("data") or {}).get("SubmissionState") or {}).get("queryState") or {}
                if "errors" in state and "feedback" not in state:
                    raise RuntimeError(f"queryState failure: {state['errors']}")
                md = render_quiz(title, item, state, status, url)
                dest = week_dir / "Quizzes" / (fc.safe_name(title) + ".md")
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(md)
                nq = sum(1 for p in (state.get("feedback") or {}).get("parts") or [] if not ("title" in p and "body" in p))
                oc = (state.get("feedback") or {}).get("outcome") or {}
                print(f"  ✓ {title}: {nq} questions, highest {oc.get('highestScore')}/{oc.get('maxScore')} -> {dest.relative_to(root)}")
                done += 1
            except Exception as e:  # noqa: BLE001
                print(f"  ✗ {title}: {e}", file=sys.stderr)
                failed += 1
    print(f"\nDone. exported {done}, locked/skipped {skipped}, failed {failed}")


if __name__ == "__main__":
    main()
