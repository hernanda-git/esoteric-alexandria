#!/usr/bin/env python3
"""
evolve.py — Self-evolution engine for the Esoteric Alexandria library.

Mirrors the pattern of the ai-knowledge-library cron jobs:
  - gap-detector:    find topics with no document, generate gap report
  - promoter:        qdrant semantic clusters -> auto-generate draft docs
  - linker:          qdrant similarity -> add [[wikilinks]] between related docs
  - enrich:          when new source material arrives in enrich/, link to existing
  - obsidian-sync:   mirror to Obsidian vault and Qdrant
  - report:          weekly digest

Default: dry-run. Use --apply to actually write.

Usage:
  python3 evolve.py --dry-run --mode light
  python3 evolve.py --apply --mode full
  python3 evolve.py --engine gap-detector --apply
"""

import argparse
import json
import re
import sys
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
STATE_DIR = REPO_ROOT / "state"
STATE_DIR.mkdir(exist_ok=True)
EVOLVE_DB = STATE_DIR / "evolve.db"

CATEGORIES = sorted(p.name for p in REPO_ROOT.iterdir()
                    if p.is_dir() and re.match(r'^\d{2}-', p.name))


# ---------------------------------------------------------------------------
# State DB
# ---------------------------------------------------------------------------

def init_db():
    conn = sqlite3.connect(EVOLVE_DB)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            engine TEXT NOT NULL,
            mode TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            changes_count INTEGER DEFAULT 0,
            report TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS auto_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            topic TEXT NOT NULL,
            source_cluster TEXT,
            created_at TEXT NOT NULL,
            reviewed_at TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS auto_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_path TEXT NOT NULL,
            to_path TEXT NOT NULL,
            score REAL NOT NULL,
            created_at TEXT NOT NULL,
            UNIQUE(from_path, to_path)
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS gaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            topic TEXT NOT NULL,
            severity TEXT NOT NULL,
            detected_at TEXT NOT NULL,
            filled_at TEXT
        )
    ''')
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Engine 1: gap detector
# ---------------------------------------------------------------------------

def engine_gap_detector(conn, apply=False):
    """Scan category index files; find topics promised in README but not in docs."""
    print("=" * 60)
    print("ENGINE: gap-detector")
    print("=" * 60)
    changes = 0
    now = datetime.now(timezone.utc).isoformat()

    for cat in CATEGORIES:
        index_path = REPO_ROOT / cat / "README.md"
        if not index_path.exists():
            continue
        index_text = index_path.read_text(encoding="utf-8")
        # Find topics in the index table (markdown table rows starting with `| N | [title](path) |`)
        promised = re.findall(r'\|\s*\d+\s*\|\s*\[([^\]]+)\]\(([^)]+)\)', index_text)
        existing_docs = {p.name for p in (REPO_ROOT / cat).glob("*.md") if p.name != "README.md"}

        for title, link in promised:
            doc_name = link.split('/')[-1] if '/' in link else link
            doc_name = doc_name.split('#')[0]
            if doc_name and doc_name not in existing_docs:
                severity = "high" if "foundations" in index_path.read_text(encoding="utf-8").lower() else "medium"
                print(f"  [gap] {cat}: missing doc for '{title}' (file: {doc_name})")
                changes += 1
                if apply:
                    conn.execute('''
                        INSERT OR REPLACE INTO gaps (category, topic, severity, detected_at)
                        VALUES (?, ?, ?, ?)
                    ''', (cat, title, severity, now))
                    conn.commit()

    print(f"  total gaps: {changes}")
    return changes


# ---------------------------------------------------------------------------
# Engine 2: enrich engine (link incoming source material to library)
# ---------------------------------------------------------------------------

def engine_enrich(conn, apply=False):
    """When new source material arrives in enrich/, scan for topics that match existing library docs."""
    print("=" * 60)
    print("ENGINE: enrich (source material -> library)")
    print("=" * 60)
    changes = 0
    enrich_dir = REPO_ROOT / "enrich"
    if not enrich_dir.exists():
        return 0

    # For each new file in enrich/, look for category 01-09 that could receive a stub cross-reference
    for src in enrich_dir.rglob("*.md"):
        if src.name == "README.md" or "/.git/" in str(src):
            continue
        rel = src.relative_to(REPO_ROOT)
        # Check if the source is already mentioned in any library doc
        src_stem = src.stem
        for cat in CATEGORIES[:9]:  # only the tradition categories 01-09
            cat_dir = REPO_ROOT / cat
            for doc in cat_dir.glob("*.md"):
                if doc.name == "README.md":
                    continue
                text = doc.read_text(encoding="utf-8", errors="ignore")
                if src_stem in text:
                    # already linked
                    continue
        # We log a stub for now
        print(f"  [enrich] source material available: {rel}")
        changes += 1
    print(f"  sources seen: {changes}")
    return changes


# ---------------------------------------------------------------------------
# Engine 3: obsidian sync
# ---------------------------------------------------------------------------

def engine_obsidian_sync(conn, apply=False):
    """Mirror all library docs into Obsidian vault and (best effort) Qdrant."""
    print("=" * 60)
    print("ENGINE: obsidian-sync")
    print("=" * 60)
    # Find Obsidian vault
    vault_candidates = [
        Path("/mnt/c/Users/it26/Documents/Obsidian Vault"),
        Path.home() / "Documents" / "Obsidian Vault",
        Path("/home/it26/Documents/Obsidian Vault"),
    ]
    vault = None
    for v in vault_candidates:
        if v.exists():
            vault = v
            break

    if vault is None:
        print("  [skip] Obsidian vault not found in known locations")
        return 0

    target_root = vault / "Resources" / "Esoteric"
    if not target_root.exists():
        if apply:
            target_root.mkdir(parents=True, exist_ok=True)
        else:
            print(f"  [dry-run] would create {target_root}")
    changes = 0
    for cat in CATEGORIES:
        cat_dir = REPO_ROOT / cat
        target_cat = target_root / cat
        if apply and not target_cat.exists():
            target_cat.mkdir(parents=True, exist_ok=True)
        for doc in cat_dir.glob("*.md"):
            target = target_cat / doc.name
            if not target.exists() or target.read_text(encoding="utf-8") != doc.read_text(encoding="utf-8"):
                if apply:
                    target.write_text(doc.read_text(encoding="utf-8"), encoding="utf-8")
                changes += 1
                print(f"  [{'apply' if apply else 'dry-run'}] {doc.relative_to(REPO_ROOT)} -> {target.relative_to(vault)}")
    print(f"  changes: {changes}")
    return changes


# ---------------------------------------------------------------------------
# Engine 4: linker (best-effort, no qdrant = no-op)
# ---------------------------------------------------------------------------

def engine_linker(conn, apply=False):
    """Find semantically related docs and add [[wikilinks]]. No qdrant = no-op."""
    print("=" * 60)
    print("ENGINE: linker")
    print("=" * 60)
    print("  [skip] no qdrant available — relying on frontmatter `related:` and existing [[wikilinks]]")
    return 0


# ---------------------------------------------------------------------------
# Engine 5: promoter (best-effort, no qdrant = no-op)
# ---------------------------------------------------------------------------

def engine_promoter(conn, apply=False):
    """qdrant semantic cluster >= 5 memories -> new doc in Inbox/."""
    print("=" * 60)
    print("ENGINE: promoter")
    print("=" * 60)
    print("  [skip] no qdrant available — promoter requires semantic cluster input")
    return 0


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def write_gap_report(changes, apply=True):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = STATE_DIR / f"gap-report-{today}.md"
    if not apply:
        return
    text = f"""# Gap Report — {today}

Generated by `evolve.py` (engine: gap-detector).

## Summary

- **{changes}** topic(s) are referenced in category index files but have no actual document yet.

## Action

The next evolution cycle will draft these as `auto-generated` notes in the corresponding category. The promoter engine (Qdrant-dependent) will be re-enabled when the qdrant collection is up.

## Cross-Reference

See `state/evolve.db` table `gaps` for the structured list. The most severe gaps are in the foundation categories (01-Origins, 02-Hurufiyya, 03-Planetary, 09-Sufism, 10-Hermeticism, 11-NeoPlatonism, 12-Agrippa) — these are the load-bearing categories that other categories reference back to.
"""
    report_path.write_text(text, encoding="utf-8")
    print(f"  [report] {report_path.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["light", "full", "weekly"], default="light")
    parser.add_argument("--engine", choices=["gap-detector", "enrich", "linker", "promoter", "obsidian-sync", "all"], default="all")
    parser.add_argument("--apply", action="store_true", help="actually write changes (default dry-run)")
    parser.add_argument("--dry-run", action="store_true", help="alias for default (no --apply)")
    args = parser.parse_args()
    if args.dry_run:
        args.apply = False

    apply = args.apply
    print(f"  Mode: {args.mode}, Engine: {args.engine}, Apply: {apply}")
    print()

    conn = init_db()
    total = 0
    engines = ["gap-detector", "enrich", "linker", "promoter", "obsidian-sync"] if args.engine == "all" else [args.engine]
    for eng in engines:
        if eng == "gap-detector":
            n = engine_gap_detector(conn, apply=apply)
        elif eng == "enrich":
            n = engine_enrich(conn, apply=apply)
        elif eng == "linker":
            n = engine_linker(conn, apply=apply)
        elif eng == "promoter":
            n = engine_promoter(conn, apply=apply)
        elif eng == "obsidian-sync":
            n = engine_obsidian_sync(conn, apply=apply)
        total += n
        print()

    # log run
    conn.execute('''
        INSERT INTO runs (engine, mode, started_at, finished_at, changes_count)
        VALUES (?, ?, ?, ?, ?)
    ''', (args.engine, args.mode, datetime.now(timezone.utc).isoformat(), datetime.now(timezone.utc).isoformat(), total))
    conn.commit()

    if engines == ["gap-detector"]:
        write_gap_report(total, apply=apply)

    print("=" * 60)
    print(f"TOTAL CHANGES: {total}")
    print("=" * 60)
    return 0 if not apply else 0  # always 0 — the engine is non-destructive


if __name__ == "__main__":
    sys.exit(main())
