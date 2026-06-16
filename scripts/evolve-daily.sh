#!/usr/bin/env bash
# evolve-daily.sh — Daily self-evolution cycle for the Esoteric Alexandria library.
# Designed to be called from Hermes cron.
#
# Usage:
#   bash scripts/evolve-daily.sh                  # dry-run
#   bash scripts/evolve-daily.sh --apply          # actually write
#   bash scripts/evolve-daily.sh --apply --mode full
#
# Output: state/evolve-YYYY-MM-DD.log + state/gap-report-YYYY-MM-DD.md

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$REPO_ROOT"

APPLY=""
MODE="light"
for arg in "$@"; do
    case "$arg" in
        --apply) APPLY="--apply" ;;
        --mode=*) MODE="${arg#--mode=}" ;;
    esac
done

LOG_DIR="$REPO_ROOT/state"
mkdir -p "$LOG_DIR"
TODAY="$(date -u +%Y-%m-%d)"
LOG_FILE="$LOG_DIR/evolve-${TODAY}.log"

echo "[$(date -u +%H:%M:%S)] daily evolution: mode=$MODE apply=${APPLY:-dry-run}" | tee -a "$LOG_FILE"

# Step 1: gap detector (always)
python3 scripts/evolve.py --engine gap-detector $APPLY --mode "$MODE" 2>&1 | tee -a "$LOG_FILE"

# Step 2: enrich engine (link incoming source material)
python3 scripts/evolve.py --engine enrich $APPLY --mode "$MODE" 2>&1 | tee -a "$LOG_FILE"

# Step 3: obsidian sync (mirror to vault)
python3 scripts/evolve.py --engine obsidian-sync $APPLY --mode "$MODE" 2>&1 | tee -a "$LOG_FILE"

# Step 4: promoter (only if qdrant is up — best-effort, no-op otherwise)
python3 scripts/evolve.py --engine promoter $APPLY --mode "$MODE" 2>&1 | tee -a "$LOG_FILE"

# Step 5: linker (best-effort, no-op without qdrant)
python3 scripts/evolve.py --engine linker $APPLY --mode "$MODE" 2>&1 | tee -a "$LOG_FILE"

echo "[$(date -u +%H:%M:%S)] daily evolution complete" | tee -a "$LOG_FILE"
