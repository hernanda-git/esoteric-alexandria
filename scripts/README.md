# Self-Evolving Engines

Three engines run on cron to keep the library fresh.

## Quick Run

```bash
# Dry-run a full evolution cycle
python3 scripts/evolve.py --dry-run --mode full

# Apply changes
python3 scripts/evolve.py --apply --mode full

# Run a single engine
python3 scripts/evolve.py --engine gap-detector --apply
python3 scripts/evolve.py --engine obsidian-sync --apply
```

The wrapper script `evolve-daily.sh` runs all engines in sequence and writes a log to `state/evolve-YYYY-MM-DD.log`.

## Engines

| Engine | What it does | Qdrant required? | Schedule |
|---|---|---|---|
| **gap-detector** | Scan category indices, find promised-but-undocumented topics, log to `state/gap-report-YYYY-MM-DD.md` | No | Daily 04:00 WIB |
| **enrich** | Watch `enrich/` for new source material, link to existing library docs | No | Daily 04:15 WIB |
| **obsidian-sync** | Mirror all `.md` into Obsidian vault at `~/Documents/Obsidian Vault/Resources/Esoteric/` | No | Daily 04:30 WIB |
| **promoter** | Qdrant `brain_semantic` cluster ≥5 memories by topic → draft doc in `Inbox/auto-generated/` | **Yes** | Daily 05:00 WIB |
| **linker** | Qdrant semantic similarity → add `[[wikilinks]]` between related docs | **Yes** | Daily 05:30 WIB |

When Qdrant is down, `promoter` and `linker` are no-ops (graceful degradation). The library still self-evolves on the other three engines.

## State DB

All engines write to `state/evolve.db` (SQLite). Tables:

- `runs` — every engine invocation
- `gaps` — topics the gap-detector finds
- `auto_notes` — docs created by the promoter (tagged `auto-generated`)
- `auto_links` — links added by the linker

The DB is the **provenance chain** for everything the engines do.

## Cron Integration

The engines are designed to be called by Hermes cron jobs. See `state/cron-schedule.txt` for the recommended schedule.

## Idempotency

All engines are **idempotent**: running them multiple times does not duplicate work. The DB acts as the dedup layer.
