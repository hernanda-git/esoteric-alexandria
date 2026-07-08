#!/usr/bin/env python3
"""
continuous-enrich.py — NON-STOP sequential enrichment driver for Esoteric Alexandria.

Each "worker" is a one-shot autonomous `hermes -z` agent that authors ONE enrichment
doc (per gap in state/evolve.db), registers it in the category README, and marks the
gap filled. This driver pulls the next gap from the queue, dispatches a worker, waits
for it to finish, then IMMEDIATELY pulls the next — no idle gap between workers.

When the DB gap queue empties, the worker self-directs: it picks the thinnest category
and generates the next high-value uncovered topic, so enrichment never stops.

Stop conditions:
  - Create state/enrich-loop.stop  (clean shutdown after current worker finishes)
  - Kill the process (PID printed on start)

Usage:
  python3 scripts/continuous-enrich.py                 # run forever until stopped
  python3 scripts/continuous-enrich.py --max 5         # run 5 worker batches then exit
  python3 scripts/continuous-enrich.py --batch 3       # docs per worker run (default 3)
  python3 scripts/continuous-enrich.py --dry-run       # print plan, dispatch nothing

State:
  - state/enrich-loop.log      full transcript of every batch
  - state/enrich-loop.stop     presence => graceful stop
"""

import argparse
import os
import re
import shutil
import subprocess
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "state"
DB = STATE / "evolve.db"
STOP = STATE / "enrich-loop.stop"
LOG = STATE / "enrich-loop.log"
MODEL = "tencent/hy3:free"

slug_re = re.compile(r"[^a-zA-Z0-9]+")


def slug(topic: str) -> str:
    s = slug_re.sub("-", topic.lower()).strip("-")
    # trim to something filename-friendly
    s = "-".join(w for w in s.split("-") if w)[:60]
    return s or "topic"


def log(msg: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def db_conn():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def next_gaps(batch: int):
    """Return up to `batch` unfilled gaps, skipping any whose doc file already exists."""
    conn = db_conn()
    rows = conn.execute(
        "SELECT id, category, topic FROM gaps WHERE filled_at IS NULL ORDER BY id ASC"
    ).fetchall()
    conn.close()
    out = []
    seen = set()
    for gid, cat, topic in rows:
        key = (cat, topic)
        if key in seen:
            continue
        seen.add(key)
        fname = f"{slug(topic)}.md"
        if (REPO / cat / fname).exists():
            # already written — mark filled so we don't loop on it
            c2 = db_conn()
            c2.execute(
                "UPDATE gaps SET filled_at=? WHERE id=? AND filled_at IS NULL",
                (datetime.now(timezone.utc).isoformat(), gid),
            )
            c2.commit()
            c2.close()
            continue
        out.append((gid, cat, fname, topic))
        if len(out) >= batch:
            break
    return out


def build_deterministic_prompt(targets):
    lines = []
    lines.append(
        "You are an enrichment worker for the Esoteric Alexandria knowledge library "
        f"at {REPO}."
    )
    lines.append("")
    lines.append(
        "Author the following doc(s). For EACH target, follow these steps EXACTLY:"
    )
    lines.append("")
    lines.append("TARGETS (gap_id | category | filename | topic):")
    for gid, cat, fname, topic in targets:
        lines.append(f"  {gid} | {cat} | {fname} | {topic}")
    lines.append("")
    lines.append("PER-TARGET STEPS:")
    lines.append(
        "1. Read the target category's README.md and ONE existing sibling .md to learn the "
        "exact YAML frontmatter format and prose style. MATCH IT PRECISELY — including the "
        "frontmatter fields (title, category, tradition, era, tags, status, related "
        "[[wikilinks]], sources) and the structured body with citations + a 'See Also' "
        "section."
    )
    lines.append(
        f"2. Check whether {REPO}/<category>/<filename> already exists. If it exists, SKIP "
        "writing but still perform step 5 (mark the gap). Never overwrite an existing doc."
    )
    lines.append(
        "3. Author the doc: substantive, accurate, well-cited (50-90 lines). Use REAL "
        "academic or primary sources. This is a serious esoteric knowledge base, not filler. "
        "Map the tradition onto modern categories (AI, complexity, psychology, business, "
        "systems theory) where relevant, in the house style."
    )
    lines.append("4. Write the file with the write_file tool to the absolute path.")
    lines.append(
        "5. Register it: append a numbered row to the category README.md documents table "
        "(read it first, find the '## Documents' table, add a row with the next sequential "
        "number, the title as a link to the filename, plus Era and Tradition columns matching "
        "the existing header)."
    )
    lines.append(
        "6. Mark the gap filled by running this in the terminal tool:"
    )
    lines.append(
        '     python3 -c "import sqlite3,datetime; '
        "c=sqlite3.connect('" + str(DB) + "'); "
        "[c.execute(\\\"UPDATE gaps SET filled_at=? WHERE id=? AND filled_at IS NULL\\\", "
        "(datetime.datetime.now(datetime.timezone.utc).isoformat(), GID)) for GID in "
        "[IDLIST]]; c.commit()\""
    )
    lines.append("   (replace IDLIST with the gap_id(s) you completed this run)")
    lines.append("")
    lines.append(
        "When all targets are done, write a one-line summary listing the files created."
    )
    lines.append(
        "Do NOT create duplicate docs. Do NOT modify unrelated files. Stay within the repo."
    )
    return "\n".join(lines).replace("IDLIST", ",".join(str(t[0]) for t in targets))


def build_selfdirected_prompt(batch: int):
    return (
        "You are an enrichment worker for the Esoteric Alexandria knowledge library "
        f"at {REPO}.\n\n"
        "The gap queue (state/evolve.db) is EMPTY. Self-direct: generate up to "
        f"{batch} NEW high-value enrichment docs for the THINNEST categories (those with "
        "the fewest .md docs excluding README.md), choosing topics NOT yet covered.\n\n"
        "PER DOC, follow EXACTLY:\n"
        "1. Read that category's README.md and one existing sibling .md to copy the exact "
        "YAML frontmatter format and prose style (title, category, tradition, era, tags, "
        "status, related [[wikilinks]], sources; structured body with citations; 'See Also').\n"
        "2. Pick a specific, uncovered, high-value topic. Do NOT duplicate existing docs "
        "(list the category dir first).\n"
        "3. Author a substantive, accurate, well-cited doc (50-90 lines) in the house style, "
        "mapping tradition onto modern categories where relevant.\n"
        "4. Write it with the write_file tool to the absolute path.\n"
        "5. Append a numbered row to the category README.md documents table (match header).\n"
        "6. Record provenance by running in terminal:\n"
        '     python3 -c "import sqlite3,datetime; c=sqlite3.connect(\''
        + str(DB)
        + '\'); now=datetime.datetime.now(datetime.timezone.utc).isoformat(); '
        "c.execute(\\\"INSERT INTO gaps (category,topic,severity,detected_at,filled_at) "
        "VALUES (?,?,'high',?,?)\\\", ('CAT','TOPIC',now,now)); c.commit()\"\n"
        "   (substitute CAT and TOPIC for each doc).\n\n"
        "Write a one-line summary of the files created. Do not modify unrelated files."
    )


def dispatch(prompt: str, batch_label: str) -> bool:
    """Run one hermes -z worker. Returns True if it completed successfully."""
    hermes = shutil.which("hermes") or "/home/it26/.local/bin/hermes"
    usage = STATE / f"enrich-usage-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    cmd = [
        hermes, "-z", prompt,
        "--yolo",
        "--model", MODEL,
        "--usage-file", str(usage),
    ]
    log(f"--- DISPATCH {batch_label} (model={MODEL}) ---")
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(REPO),
            capture_output=True,
            text=True,
            timeout=20 * 60,  # hard cap 20 min per worker
        )
    except subprocess.TimeoutExpired:
        log(f"WORKER TIMEOUT after 20m — marking {batch_label} failed")
        return False
    out = (proc.stdout or "") + (proc.stderr or "")
    # log a trimmed transcript
    for line in out.splitlines()[-40:]:
        log("    " + line[:300])
    ok = proc.returncode == 0
    log(f"WORKER exit={proc.returncode} -> {'OK' if ok else 'FAILED'}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=0, help="max worker batches (0=forever)")
    ap.add_argument("--batch", type=int, default=3, help="docs per worker run")
    ap.add_argument("--dry-run", action="store_true", help="plan only, dispatch nothing")
    args = ap.parse_args()

    if STOP.exists():
        STOP.unlink()

    log("=" * 70)
    log(f"CONTINUOUS ENRICHMENT STARTED  pid={os.getpid()}  batch={args.batch}  "
        f"max={args.max or 'forever'}  model={MODEL}")
    log(f"Repo: {REPO}")
    log(f"Stop file: {STOP}  |  kill -TERM {os.getpid()} to stop")
    log("=" * 70)

    batches = 0
    backoff = 0
    while True:
        if STOP.exists():
            log("STOP FILE PRESENT — graceful shutdown.")
            break
        if args.max and batches >= args.max:
            log(f"REACHED --max {args.max} batches — exiting.")
            break

        targets = next_gaps(args.batch)
        if targets:
            prompt = build_deterministic_prompt(targets)
            label = "batch#%d gaps=%s" % (batches + 1, ",".join(str(t[0]) for t in targets))
        else:
            prompt = build_selfdirected_prompt(args.batch)
            label = f"batch#{batches + 1} self-directed"

        if args.dry_run:
            log(f"[DRY-RUN] would dispatch {label}")
            log(prompt[:600])
            break

        ok = dispatch(prompt, label)
        batches += 1

        if not ok:
            backoff = min(backoff + 30, 300)
            log(f"backing off {backoff}s before next worker")
            # honor stop during backoff
            for _ in range(backoff // 5):
                if STOP.exists():
                    log("STOP FILE PRESENT during backoff — shutdown.")
                    return
                time.sleep(5)
            continue
        else:
            backoff = 0

    log("CONTINUOUS ENRICHMENT ENDED.")


if __name__ == "__main__":
    main()
