# Cron Schedule — Esoteric Alexandria Self-Evolution

The library runs on a daily + weekly + monthly cycle. All jobs are managed by Hermes cron.

## Daily (00:00 - 06:00 WIB)

| Time (WIB) | Job | Command | Engine |
|---|---|---|---|
| 04:00 | gap-detector | `bash scripts/evolve-daily.sh` | gap-detector |
| 04:15 | enrich | (continues in same script) | enrich |
| 04:30 | obsidian-sync | (continues) | obsidian-sync |
| 05:00 | promoter | (continues) | promoter (Qdrant-gated) |
| 05:30 | linker | (continues) | linker (Qdrant-gated) |

The whole cycle is wrapped in a single `scripts/evolve-daily.sh` invocation. The script runs all engines in sequence and writes a log to `state/evolve-YYYY-MM-DD.log`.

## Weekly (Sunday 09:00 WIB)

| Time | Job | Command |
|---|---|---|
| Sun 09:00 | weekly-digest | `python3 scripts/weekly-digest.py` — Telegram report: new docs, top gaps, suggested next reads |

## Monthly (1st of month, 10:00 WIB)

| Time | Job | Command |
|---|---|---|
| 1st 10:00 | monthly-summary | `python3 scripts/monthly-summary.py` — full state report + quality scoring |

## Cron Registration (Hermes)

```python
# Daily evolution
cronjob create --name esoteric-alexandria-daily \
    --schedule "0 21 * * *" \
    --prompt "Run the Esoteric Alexandria self-evolution cycle. Execute cd C:/Workspace/esoteric-alexandria && python3 scripts/evolve.py --apply --mode light 2>&1 | tail -30. Then python3 obsidian-bridge/obsidian_sync.py --apply. Report changes. If no changes, stay silent." \
    --workdir "C:/Workspace/esoteric-alexandria"

# Weekly digest
cronjob create --name esoteric-alexandria-weekly \
    --schedule "0 2 * * 0" \
    --prompt "Run the Esoteric Alexandria weekly digest. cd C:/Workspace/esoteric-alexandria && python3 scripts/weekly-digest.py --apply. Deliver the digest to telegram."
```

(Replace `0 21 * * *` with the local UTC equivalent. WIB is UTC+7, so 04:00 WIB = 21:00 UTC the previous day.)

## Qdrant Integration

The Qdrant collection `brain_notes` (in the existing unified-brain stack) is the **canonical store** for the library's vector representation. Every time a new doc is added to the library, the obsidian-sync script should trigger a re-index of the new doc into Qdrant.

For now, the existing `obsidian-index` (in the user's unified-brain) re-indexes the whole vault periodically. The Esoteric Alexandria library, once mirrored into the Obsidian vault at `Resources/Esoteric/`, is automatically picked up by the existing re-indexer.

## Graceful Degradation

If Qdrant is down:
- `promoter` and `linker` are no-ops (they are pure Qdrant consumers)
- `gap-detector`, `enrich`, and `obsidian-sync` keep working
- The library still evolves — the missing parts are *enrichment* (auto-generated docs from Qdrant clusters) and *cross-linking* (auto `[[wikilinks]]`)

If the Obsidian vault is missing:
- The engine logs a warning and skips
- The library is still in `C:\Workspace\esoteric-alexandria` and can be browsed there

If both are missing:
- The engine still works on the repo level — gap-detection and enrich-tracking run, results land in `state/`
