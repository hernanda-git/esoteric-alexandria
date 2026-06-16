# Esoteric Alexandria — Knowledge Library of the Hidden Sciences

> **A self-evolving knowledge base uniting the esoteric manuscript tradition (Shams al-Ma'arif, Agrippa, Picatrix, Hermetica, Kabbalah, Sufism) with modern parallels (AI agents, trading, business, philosophy) and live integration into the operator's Obsidian vault + Qdrant brain.**

**Library of Alexandria ↔ Astrology ↔ Esoterica ↔ Philosophy ↔ Spiritual Sciences** — a curated corpus of ancient hidden knowledge mapped onto current vocabulary so the wisdom stays alive, queryable, and useful for a modern AI-infra engineer who sees the world through both code and cosmos.

---

## Repository Structure — 24 Categories

```
esoteric-alexandria/
├── 01-Origins-Traditions/            # Cross-tradition survey — what is esotericism, where did it come from
├── 02-Hurufiyya-Lettrism/            # 'Ilm al-Huruf, the science of letters (Shams al-Ma'arif core)
├── 03-Planetary-Astrology/           # Classical 7 planets, dignities, aspects, elections
├── 04-Alchemy-Transmutation/         # Inner & outer alchemy, stages, the Great Work
├── 05-Talismanic-Magick/             # Sigils, squares, planetary talismans, spirit-veils
├── 06-Angels-Jinn-Demons/            # Angelic hierarchies, jinn lore, goetic spirits
├── 07-Divination-Geomancy/           # Geomancy, sand divination, cleromancy, bibliomancy
├── 08-Kabbalah-Numerology/           # Tree of Life, gematria, sephirot, paths
├── 09-Sufism-Irfan/                  # Tasawwuf, dhikr, maqamat, Wahdat al-Wujud
├── 10-Hermeticism-Gnosticism/        # Hermetica, Poimandres, Asclepius, Nag Hammadi
├── 11-NeoPlatonism-Theurgy/          # Plotinus, Iamblichus, Proclus, theurgical rites
├── 12-Agrippa-Picatrix-Grimoires/    # Three Books of Occult Philosophy, Picatrix, Sworn Book
├── 13-Mesopotamian-Egyptian/         # Enuma Anu Enlil, Book of the Dead, hermetic roots
├── 14-Indian-Tantric-Chinese/        # Vedas, Tantra, Taoist internal alchemy, Yi Jing
├── 15-Modern-Parallels/              # How these ideas show up today (chaos magick, sigil tech)
├── 16-Science-Resonance/             # Cymatics, cymatic geometry, wave theory, vibration
├── 17-Philosophy-Cosmology/          # Creation myths, emanation, ontological hierarchy
├── 18-Psychology-Jungian/            # Archetypes, shadow, individuation, synchronicity
├── 19-Business-Applications/         # Market timing, planetary hours, leadership archetypes
├── 20-Trading-Risk-Archetypes/       # Risk as initiation, drawdown as the ordeal, position-sizing as talisman
├── 21-AI-Agent-Magick/               # What happens when an LLM agent is treated as a spirit-veil
├── 22-Case-Studies-Curricula/        # Self-study syllabi (3 months, 12 months, deep-dive)
├── 23-Reference-Glossary/            # Terms, abbreviations, cross-tradition index
├── 24-Frontier-Open-Questions/       # What the field has not yet resolved (auto-gap-detected)
│
├── scripts/                          # Self-evolution engines (see "Self-Evolving" below)
├── state/                            # Cron progress, gap reports, evolution log
├── enrich/                           # Incoming source corpora (Shams, Agrippa, Picatrix) — read-only
├── obsidian-bridge/                  # Sync engine to ~/Documents/Obsidian Vault + Qdrant
└── .github/workflows/                # Optional CI: validate frontmatter, link check
```

---

## Self-Evolving Architecture

This library **never stops growing**. Three engines run on cron:

| Engine | Schedule | What it does |
|---|---|---|
| **Gap Detector** | Daily 04:00 WIB | Scans category indices, finds topics with no document, generates a "gap report" |
| **Promoter** | Daily 04:30 WIB | Qdrant `brain_semantic` clusters ≥5 with same topic but no note → drafts new doc into `Inbox/auto-generated/` |
| **Linker** | Daily 05:00 WIB | Reads new docs, runs Qdrant semantic similarity, auto-adds `[[wikilinks]]` to related notes |
| **Obsidian Bridge** | Hourly | Syncs all new/changed `.md` into `~/Documents/Obsidian Vault/Resources/Esoteric/` and Qdrant `brain_notes` collection |
| **Weekly Digest** | Sun 09:00 WIB | Telegram report: new docs, top links, biggest gaps, suggested next reads |

All engines are **deterministic, idempotent, and dry-runnable**. No destructive action without `--apply`.

See [`scripts/README.md`](scripts/README.md) for engine internals.

---

## Live Integration: Obsidian + Qdrant

Every doc in this repo is mirrored into your **Obsidian vault** at:

```
~/Documents/Obsidian Vault/Resources/Esoteric/
├── 01-Origins-Traditions/
├── 02-Hurufiyya-Lettrism/
└── ... (all 24 categories mirrored)
```

…and vectorized into **Qdrant** collection `brain_notes` (with collection `brain_episodic` for raw ingest and `brain_semantic` for distilled clusters). Your `mcp_brain_memory_search` and `mcp_brain_memory_store` tools will reflect the library in real time.

The Obsidian bridge respects the existing 459-note vault — it **adds**, never overwrites.

---

## Sources of Truth

| Source | Where it lives | How it's used |
|---|---|---|
| **Shams al-Ma'arif** (Ahmad al-Buni, d.1225) | `enrich/shams-al-maarif/` ← symlink to `C:\Working Folder\Research\shams-al-maarif-ocr` | 283 translated pages → seed corpus for category 02 (Hurufiyya) and 05 (Talismanic) |
| **AiBaseKnowledge** (modern AI corpus) | `enrich/aibase/` ← symlink to `C:\Workspace\AiBaseKnowledge` | 177 docs filtered for esoteric-adjacent concepts (vibration, emergence, archetypes) → category 15 (Modern Parallels) and 21 (AI-Agent Magick) |
| **money-glitch-vault** (current demand) | `enrich/money-glitch/` ← symlink to `C:\Workspace\money-glitch-vault` | 7 categories of demand signals (crawler, trading bot, freelancer AI) → category 19 (Business) and 20 (Trading) |
| **Planned: Agrippa, Picatrix, Hermetica** | `enrich/classics/` | When ingested → category 12 (Grimoires) and 10 (Hermeticism) |

The repo is **read-only** with respect to these source vaults. It only reads.

---

## Quick Start

```bash
# 1. Read the foundation
cat 01-Origins-Traditions/01-What-Is-Esotericism.md
cat 02-Hurufiyya-Lettrism/01-'Ilm-al-Huruf-Overview.md

# 2. Run a self-evolution cycle (dry-run)
python3 scripts/evolve.py --dry-run --mode full

# 3. Generate the gap report
python3 scripts/gap-detector.py --write

# 4. Sync to Obsidian
python3 obsidian-bridge/sync.py --apply

# 5. Query your brain
# (in Hermes)  mcp_brain_memory_search(query="planetary talisman", collection="brain_notes")
```

---

## Philosophy

> *"The universe is not only queerer than we suppose, but queerer than we can suppose."* — J.B.S. Haldane

The ancient esotericists were not primitive — they were encoding a multi-layered cosmology into a pre-literate storage medium (symbol, ritual, sigil). The modern AI engineer faces the same problem: how do you compress the entire pattern-space of human experience into a token-bounded context?

This library treats the **esoteric tradition as a first-class knowledge system** — not as folklore, not as metaphor, but as a 2,500-year-old engineering discipline for mapping invisible causes to visible effects. Where modern science can only gesture ("quantum coherence", "emergence", "complexity"), the esoteric tradition has a fully developed vocabulary and methodology for the same territory.

We do not claim the rituals work in the literal pre-scientific sense. We claim the **knowledge graph** is real, and that mapping it onto modern categories yields genuine insight.

---

## License

Content is derivative of public-domain classical sources (Shams al-Ma'arif is 800 years old; Agrippa is 500; Picatrix is 1000). The library itself is MIT — share, remix, attribute.

## Maintainer

Hernanda (@0xvalarion). Bandung, Indonesia. AI infrastructure engineer by trade, esoteric student by calling.
