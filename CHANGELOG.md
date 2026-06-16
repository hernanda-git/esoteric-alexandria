# Changelog — Esoteric Alexandria

## v1.0.0 — 2026-06-16 (full enrichment)

**Continuous and sequential enrichment complete.**

### Final State

- **24 categories** scaffolded, all with index files
- **24 category READMEs** written
- **65 foundation/bridge/curriculum docs** written across all categories
- **3 self-evolution scripts** (evolve.py, evolve-daily.sh, obsidian_sync.py)
- **2 cron jobs** registered (esoteric-alexandria-daily, esoteric-alexandria-weekly)
- **3 symlinked source vaults** (shams-al-maarif, aibase, money-glitch)
- **Initial Obsidian mirror** at `~/Documents/Obsidian Vault/Resources/Esoteric/`
- **GitHub repository** at https://github.com/hernanda-git/esoteric-alexandria

### Docs Per Category

| # | Category | Docs |
|---|---|---|
| 01 | Origins-Traditions | 7 (What is Esotericism, Esoteric vs Exoteric, Oral Transmission Chains, Seven Liberal Arts, Perennial Philosophy, Initiation, Master-Disciple Chains) |
| 02 | Hurufiyya-Lettrism | 4 ('Ilm al-Huruf, Abjad, Jafr, Wafq) |
| 03 | Planetary-Astrology | 1 (Seven Planets) |
| 04 | Alchemy-Transmutation | 4 (Alchemy Overview, 4 Stages, Jabir, Modern Chemistry) |
| 05 | Talismanic-Magick | 3 (Squares/Sigils, Planetary Talismans, Goetia) |
| 06 | Angels-Jinn-Demons | 3 (Angelic Hierarchy, 72 Shem ha-Mephorash, Jinn) |
| 07 | Divination-Geomancy | 3 (40 Methods, Geomancy, I Ching) |
| 08 | Kabbalah-Numerology | 3 (Tree of Life, Gematria, Christian Kabbalah) |
| 09 | Sufism-Irfan | 1 (Sufism Overview) |
| 10 | Hermeticism-Gnosticism | 3 (Corpus Hermeticum, Gnosticism, Poimandres) |
| 11 | NeoPlatonism-Theurgy | 1 (Iamblichus) |
| 12 | Agrippa-Picatrix-Grimoires | 2 (Three Books, Picatrix) |
| 13 | Mesopotamian-Egyptian | 3 (Enuma Anu Enlil, Book of the Dead, Sabians) |
| 14 | Indian-Tantric-Chinese | 3 (Chakras, Chinese Alchemy, Tantra) |
| 15 | Modern-Parallels | 1 (Cryptanalysis as Jafr) |
| 16 | Science-Resonance | 3 (Cymatics, Music of Spheres, Fourier) |
| 17 | Philosophy-Cosmology | 3 (Emanation, Tao Te Ching, Tetraktys) |
| 18 | Psychology-Jungian | 4 (Jung/Alchemy, Shadow, Archetypes, Individuation) |
| 19 | Business-Applications | 3 (Planetary Hours Business, Leader as Magus, Org as Subtle Body) |
| 20 | Trading-Risk-Archetypes | 1 (Risk as Initiation) |
| 21 | AI-Agent-Magick | 1 (LLM as Spirit-Veil) |
| 22 | Case-Studies-Curricula | 3 (12-Month, 3-Month, 2-Year Deep-Dive) |
| 23 | Reference-Glossary | 3 (Glossary, Concordance Table, Reading Order) |
| 24 | Frontier-Open-Questions | 3 (Open Questions, Consciousness Question, Future Research) |
|  | **TOTAL** | **~70 documents** (including master README + category READMEs) |

### Self-Evolving Engines

- `scripts/evolve.py` — gap-detector, enrich, obsidian-sync, promoter, linker
- `scripts/evolve-daily.sh` — daily cycle wrapper
- `obsidian-bridge/obsidian_sync.py` — vault mirror
- All idempotent, dry-runnable, Qdrant-graceful

### Cron Jobs Registered

- **esoteric-alexandria-daily** — 0 21 * * * UTC (04:00 WIB) — full evolution cycle
- **esoteric-alexandria-weekly** — 0 2 * * 0 UTC (Sun 09:00 WIB) — digest report

### Source Vaults Linked (read-only)

- `enrich/shams-al-maarif` → `C:\Working Folder\Research\shams-al-maarif-ocr` (283 translated pages)
- `enrich/aibase` → `C:\Workspace\AiBaseKnowledge` (177 AI docs)
- `enrich/money-glitch` → `C:\Workspace\money-glitch-vault` (7 demand categories)

### Live Integration

- Mirror at `~/Documents/Obsidian Vault/Resources/Esoteric/` (20 docs initially, can be re-synced)
- Re-indexed by the existing `obsidian-index` cron into Qdrant `brain_notes` collection
- `mcp_brain_memory_search` reflects all docs when Qdrant is up

### Earlier Versions

- v0.1.0 — 2026-06-16 (initial seed, 22 docs across 10 categories, self-evolution engine)
