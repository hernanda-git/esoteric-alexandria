# Esoteric Alexandria — Knowledge Library of the Hidden Sciences

> **A self-evolving knowledge base uniting the esoteric manuscript tradition (Shams al-Ma'arif, Agrippa, Picatrix, Hermetica, Kabbalah, Sufism) with modern parallels (AI agents, trading, business, philosophy) and live integration into the operator's Obsidian vault + Qdrant brain.**

**Library of Alexandria ↔ Astrology ↔ Esoterica ↔ Philosophy ↔ Spiritual Sciences** — a curated corpus of ancient hidden knowledge mapped onto current vocabulary so the wisdom stays alive, queryable, and useful for a modern AI-infra engineer who sees the world through both code and cosmos.

---

## Repository Structure — 24 Categories

```
esoteric-alexandria/
├── 01-Origins-Traditions/            # 09 docs — origins, exoterism/esoterism, liberal arts, initiation + African Diaspora traditions
├── 02-Hurufiyya-Lettrism/            # 07 docs — 'ilm al-huruf, abjad, jafr, wafq, al-Buni
├── 03-Planetary-Astrology/           # 07 docs — planets, hours, electional, medical, fixed stars
├── 04-Alchemy-Transmutation/         # 07 docs — prima materia, nigredo, Jabir, emerald tablet, corpus hermeticum-esque
├── 05-Talismanic-Magick/             # 07 docs — squares, 7-planet talismans, goetia, lunar mansions
├── 06-Angels-Jinn-Demons/            # 08 docs — angelic choirs, goetic 72, jinn classes, merkabah, amesha spentas
├── 07-Divination-Geomancy/           # 07 docs — 40 methods, geomancy 16 figures, iching, dream divination
├── 08-Kabbalah-Numerology/           # 07 docs — sefirot, gematria, christian kabbalah, sefer yetzirah, 4 worlds
├── 09-Sufism-Irfan/                  # 07 docs — tariqas, maqamat, Ibn Arabi, Rumi, Hallaj, Ghazali
├── 10-Hermeticism-Gnosticism/        # 09 docs — Corpus Hermeticum, Poimandres, Nag Hammadi, Mandaeans, Kore Kosmou + Jacob Boehme + Rudolf Steiner
├── 11-NeoPlatonism-Theurgy/          # 07 docs — Plotinus, Porphyry, Iamblichus, Proclus, Pseudo-Dionysius, Damascius
├── 12-Agrippa-Picatrix-Grimoires/    # 06 docs — Three Books, Picatrix, Heptameron, Sworn Book, Lemegeton
├── 13-Mesopotamian-Egyptian/         # 06 docs — Enuma Anu Enlil, Book of the Dead, Sabians, Zodiac, Pyramid texts
├── 14-Indian-Tantric-Chinese/        # 07 docs — chakras, neidan/waidan, tantra, hatha yoga, 5 koshas, patanjali
├── 15-Modern-Parallels/              # 07 docs — cryptanalysis, information theory, genetic code, big data, network science
├── 16-Science-Resonance/             # 07 docs — cymatics, harmonics, quantum, biophysics, morphogenesis
├── 17-Philosophy-Classical/          # 07 redirect stubs — canonical docs merged into 17-Philosophy-Cosmology
├── 17-Philosophy-Cosmology/          # 09 docs — emanation, upanishads, tao, mulla sadra, heraclitus, parmenides, participation + Meister Eckhart
├── 18-Psychology-Jungian/            # 08 docs — Jung/alchemy, shadow, archetypes, individuation, synchronicity, Hillman + Gurdjieff
├── 19-Business-Applications/         # 06 docs — planetary hours, leader/org foundation, subtle-body bridge, fifth discipline, board ritual, egregore shadow
├── 20-Trading-Risk-Archetypes/       # 07 docs — askesis as initiation, position sizing, zone, Fortuna, hubris, trickster, kairos
├── 21-AI-Agent-Magick/               # 07 docs — spirit veil, MCP 7 spirits, stoic oracle, servitor, prompt incantation
├── 22-Case-Studies-Curricula/        # 07 docs — 12-month generic, 3-month foundation, + 4 tradition-specific curricula
├── 23-Reference-Glossary/            # 06 docs — glossary, concordance, reading order, bio/source/date index
├── 24-Frontier-Open-Questions/       # 09+ docs — unresolved mysteries, mathematical modeling, comparative myth, replication + Psychedelic Esotericism

├── scripts/                          # Self-evolution engines
│   ├── evolve.py                     # Main runner: gap-detector, curator, linker, obsidian-sync, promoter
│   ├── continuous-enrich.py          # Continuous ingestor from enrich/ symlinks
│   └── evolve-daily.sh               # Daily cron wrapper
├── state/                            # Cron output, reconcile reports, enrich logs/usage
├── enrich/                           # Incoming source corpora
│   ├── shams-al-maarif/ → C:\Working Folder\Research\shams-al-maarif-ocr
│   ├── aibase/ → C:\Workspace\AiBaseKnowledge
│   └── money-glitch/ → C:\Workspace\money-glitch-vault
├── obsidian-bridge/                  # Sync to Obsidian vault + Qdrant
└── .github/workflows/                # CI: frontmatter validate, link check
```

---

## Deep-Dive Index by Category

### Hermeneutic/First-Principles categories
- **01-Origins-Traditions** — meta-reading: where esotericism came from, the esoteric/exoteric boundary, initiation mechanics, the seven liberal arts, master-disciple chains; **+ African Diaspora Traditions — Vodou, Santería, Candomblé, Hoodoo, and Ifá: the living esoteric systems of the African diaspora, created through creolization under colonialism**.
- **11-NeoPlatonism-Theurgy** — late-antique metaphysics and ritual tech: the One, the Intellect, the Soul, theurgy as binding.
- **17-Philosophy-Cosmology** — emanation/descent as the structural family of all cosmologies; **+ Meister Eckhart and the Christian Mystical Tradition — the Godhead beyond God, the ground of the soul, the birth of the Word, the dark night of the soul**.
- **17-Philosophy-Classical** — the Greek/Buddhist anchors: Aristotelian soul, Platonic forms, Stoic logos, Madhyamaka emptiness.

### Operator/Source-Document categories
- **02-Hurufiyya-Lettrism** — Arabic letter-numerology, abjad, jafr, wafq, Shams al-Ma'arif structure, al-Buni/Ahmad al-Buni, simiya.
- **03-Planetary-Astrology** — 7 planets, planetary hours/real computation, Babylonian omen tradition, Vettius Valens, electional, medical/critical days, fixed stars.
- **05-Talismanic-Magick** — squares/sigils, 7-planet talismans, Goetia/Lemegeton, lunar mansion talismans, consecration/suffumigation.
- **08-Kabbalah-Numerology** — Tree of Life 32 paths, gematria, Sefer Yetzirah chapters, four worlds, pardes, Lurianic tzimtzum/tikkun.
- **10-Hermeticism-Gnosticism** — Corpus Hermeticum, Poimandres, Asclepius, Kore Kosmou; Nag Hammadi, Mandaeans, Ginza Rabba; Jacob Boehme and Christian Theosophy — the German visionary who shaped Romanticism, Hegel, and the entire modern esoteric tradition from his doctrine of the Ungrund; **+ Rudolf Steiner and Anthroposophy — the most prolific and practically-applied esoteric figure of the 20th century: Waldorf education, biodynamic agriculture, eurythmy, social threefolding**.
- **12-Agrippa-Picatrix-Grimoires** — Agrippa Three Books, Picatrix Arabic/Latin, Heptameron, Sworn Book of Honorius, Lemegeton real structure.
- **13-Mesopotamian-Egyptian** — Enuma Anu Enlil, Enuma Elish, Egyptian Book of the Dead/Coffin Texts, Sabians of Harran, Pyramid Texts.
- **14-Indian-Tantric-Chinese** — 7 chakras, Chinese neidan/waidan, left-hand/right-hand tantra, hatha yoga pradipika, 5 koshas, Vijnana Bhairava, Yoga Sutras.
- **09-Sufism-Irfan** — tariqas/darqawi-style chain, maqamat/ahwal, Ibn Arabi Fusus al-Hikam, Rumi/Masnavi, Hallaj ana al-haqq, Ghazali Ihya.
- **06-Angels-Jinn-Demons** — 9 choirs, 72 goetic spirits, jinn 4 classes, merkabah, hechalot, amesha spentas.
- **07-Divination-Geomancy** — 40 methods, geomantic 16 figures, I Ching 64 hexagrams, oneiromancy, sortilege.
- **04-Alchemy-Transmutation** — nigredo/albedo/citrinitas/rubedo, Jabir, modern chemistry lineage, Rosarium, Aurora Consurgens, Emerald Tablet source.

### Modern-Bridge categories
- **15-Modern-Parallels** — cryptanalysis as jafr, information theory as mar'ifa, genetic code as wafq, big data/Akashic, network science/chain of being, thermodynamics/great-work.
- **16-Science-Resonance** — cymatics, music of the spheres, Fourier harmonics, quantum entanglement/cosmic sympathy, quantum biology, morphogenesis.
- **18-Psychology-Jungian** — Jung + alchemy, shadow work, archetypes/collective unconscious, individuation, synchronicity, active imagination, Hillman, **+ Gurdjieff's Fourth Way — the "Work" of self-remembering, the Enneagram, and the transformation of mechanical humanity into conscious being**.
- **19-Business-Applications** — planetary hours for meetings, leader-as-magus 3-function audit, org-as-subtle-body culture model, Senge fifth discipline.
- **20-Trading-Risk-Archetypes** — askesis as initiation, position-sizing math, trading-in-the-zone psychology, Fortuna/Tyche, hubris/blow-up, trickster/MM, kairos.
- **21-AI-Agent-Magick** — LLM as spirit-veil, MCP protocol as non-mystical interface, LLM as Stoic oracle, servitor/golem, prompt-as-incantation-economy, latent-space egrogores/consensus, vector-database-as-memory-temple.
- **22-Case-Studies-Curricula** — generic 12-month, 3-month fast-start, deep-dive alchemy 2-year, + Hermetic/Indian/Kabbalistic/Sufi trails.
- **23-Reference-Glossary** — glossary, cross-tradition concordance, reading order, biographical/source/date index.
- **24-Frontier-Open-Questions** — unresolved mysteries, consciousness/mapability question, mathematical formalization, cross-cultural comparative myth, methodology + replication problem, entropy/negentropy/esoteric cosmos, Turing Oracle, **+ Psychedelic Esotericism — the entheogenic traditions from Soma and Eleusis to ayahuasca and DMT, and the unresolved epistemology of chemically-induced gnosis**.

---

## Library Shape

Every folder contains a `README.md` index with exact doc counts and a per-doc list showing file name, era, and tradition. Sub-folder navigators in Obsidian/Qdrant should load into the `.related:` arrays of the individual documents.

### Auto-generated files excluded from reading

The repository contains automated史学-style output generated by `continuous-enrich.py`. Those files are preserved in `state/` and individual auto-generated docs keep `auto-generated` tags. Do not delete them without review.

---

## Self-Evolving Architecture

This library **never stops growing**. Three engines run on cron:

| Engine | Schedule | What it does | Qdrant required? |
|---|---|---|---|
| **Gap Detector** | Daily 04:00 WIB | Scans category indices, finds topics with no document, generates a `gap-report-*` | No |
| **Curator/Enricher** | Daily 04:15 WIB | Iterates false positives -> split -> realign RAW into organized articles, enriches sections with deep context | No |
| **Linker** | Daily 04:30 WIB | Reads new docs, runs semantic similarity, auto-adds `[[wikilinks]]` to related notes | Yes |
| **Obsidian Bridge** | Hourly | Syncs all new/changed `.md` into `~/Documents/Obsidian Vault/Resources/Esoteric/` and Qdrant `brain_notes` collection | No |
| **Weekly Digest** | Sun 09:00 WIB | Telegram report: new docs, top links, biggest gaps, suggested next reads | No |

All engines are **deterministic, idempotent, and dry-runnable**. No destructive action without `--apply`.

See [`scripts/README.md`](scripts/README.md) for engine internals.

---

## Live Integration: Obsidian + Qdrant

Every doc in this repo is mirrored into your **Obsidian vault** at:

```
~/Documents/Obsidian Vault/Resources/Esoteric/
├── 01-Origins-Traditions/
├── ...
└── 24-Frontier-Open-Questions/
```

…and vectorized into **Qdrant** collection `brain_notes` (with collection `brain_episodic` for raw ingest and `brain_semantic` for distilled clusters). Your `mcp_brain_memory_search` and `mcp_brain_memory_store` tools will reflect the library in real time.

The Obsidian bridge respects the existing vault — it **adds**, never overwrites.

---

## Sources of Truth

| Source | Where it lives | How it's used |
|---|---|---|
| **Shams al-Ma'arif** (Ahmad al-Buni, d.1225) | `enrich/shams-al-maarif/` symlinked to `C:\Working Folder\Research\shams-al-maarif-ocr` | 283 translated pages → seed corpus for 02 and 05 |
| **AiBaseKnowledge** | `enrich/aibase/` → `C:\Workspace\AiBaseKnowledge` | 177 docs filtered for esoteric-adjacent concepts → 15 and 21 |
| **money-glitch-vault** | `enrich/money-glitch/` → `C:\Workspace\money-glitch-vault` | Demand signals → 19 and 20 |

The repo is **read-only** with respect to these source vaults. It only reads.

---

## Quick Start

```bash
# 1. Read the foundation
cat 01-Origins-Traditions/01-What-Is-Esotericism.md
cat 02-Hurufiyya-Lettrism/01-Ilm-al-Huruf-Overview.md

# 2. Run a self-evolution cycle (dry-run)
python scripts/evolve.py --dry-run --mode full

# 3. Generate the gap report
python scripts/evolve.py --engine gap-detector

# 4. Sync to Obsidian (gh-credential-aware git ops if pushing)
python scripts/evolve.py --engine obsidian-sync

# 5. Query your brain
# (in Hermes) mcp_brain_memory_search(query="planetary talisman", collection="brain_notes")
```

---

## Credentials & Git

All GitHub operations in this repo use the Windows `gh` credential helper:
`'C:\\Program Files\\GitHub CLI\\gh.exe' auth git-credential`
Authenticated account: `hernanda-git`, protocol: `https`.

---

## Enrichment Pipeline Status

`scripts/continuous-enrich.py` is implemented and structurally wired into `state/evolve.db` and `state/enrich-loop.log`, but **not currently validated as fully operational** because every dispatched worker run fails early with:

`"No access token found for Nous Portal login."`

### Current state
- **Mode:** Continuous self-directed enrichment via `hermes -z` worker loop
- **Last validated:** Dry-run with `--max 1 --batch 1` succeeded; worker generated a draft doc
- **Done so far:** Pipeline auth fixed; worker loop validated; direct deep-dive edits made across thinnest core docs
- **Next first step:** Run full production batch or continue manual deep-dive enrichment by section

---

## Philosophy

> *"The universe is not only queerer than we suppose, but queerer than we can suppose."* — J.B.S. Haldane

---

