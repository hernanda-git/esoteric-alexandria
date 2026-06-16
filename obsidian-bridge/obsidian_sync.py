#!/usr/bin/env python3
"""
obsidian_sync.py — Mirror the Esoteric Alexandria library into the Obsidian vault.

Writes all library docs (excluding auto-generated / drafts) into:
    ~/Documents/Obsidian Vault/Resources/Esoteric/

Designed to be idempotent — running multiple times per day is safe.

Usage:
    python3 obsidian_sync.py              # dry-run
    python3 obsidian_sync.py --apply      # actually write
"""

import argparse
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).parent.parent

VAULT_CANDIDATES = [
    Path("/mnt/c/Users/it26/Documents/Obsidian Vault"),
    Path.home() / "Documents" / "Obsidian Vault",
    Path("/home/it26/Documents/Obsidian Vault"),
]

EXCLUDE_DIRS = {"scripts", "state", "enrich", ".github", "obsidian-bridge", ".git"}
CATEGORY_RE = re.compile(r"^\d{2}-")


def find_vault():
    for v in VAULT_CANDIDATES:
        if v.exists():
            return v
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    apply = args.apply

    vault = find_vault()
    if not vault:
        print("ERROR: Obsidian vault not found in any known location")
        print("  tried:")
        for v in VAULT_CANDIDATES:
            print(f"    - {v}")
        return 1

    target_root = vault / "Resources" / "Esoteric"
    print(f"Vault:   {vault}")
    print(f"Target:  {target_root}")
    print(f"Mode:    {'APPLY' if apply else 'dry-run'}")
    print()

    if apply:
        target_root.mkdir(parents=True, exist_ok=True)

    synced = 0
    skipped = 0
    for cat_dir in sorted(REPO_ROOT.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name in EXCLUDE_DIRS:
            continue
        if not CATEGORY_RE.match(cat_dir.name):
            continue
        target_cat = target_root / cat_dir.name
        if apply and not target_cat.exists():
            target_cat.mkdir(parents=True, exist_ok=True)
        for doc in cat_dir.glob("*.md"):
            target = target_cat / doc.name
            if not apply:
                print(f"  [dry-run] {doc.relative_to(REPO_ROOT)} -> {target.relative_to(vault)}")
                synced += 1
            else:
                if target.exists() and target.read_text(encoding="utf-8") == doc.read_text(encoding="utf-8"):
                    skipped += 1
                else:
                    target.write_text(doc.read_text(encoding="utf-8"), encoding="utf-8")
                    print(f"  [synced] {doc.relative_to(REPO_ROOT)} -> {target.relative_to(vault)}")
                    synced += 1
    # Also write the master README to the root
    target_readme = target_root / "README.md"
    if apply:
        target_readme.write_text((REPO_ROOT / "README.md").read_text(encoding="utf-8"), encoding="utf-8")
        print(f"  [synced] README.md -> {target_readme.relative_to(vault)}")
    synced += 1

    print()
    print(f"Synced:   {synced}")
    print(f"Skipped:  {skipped} (unchanged)")

    # Write sync log
    log_path = REPO_ROOT / "state" / "obsidian-sync.log"
    log_path.parent.mkdir(exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()} | apply={apply} | synced={synced} | skipped={skipped}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
