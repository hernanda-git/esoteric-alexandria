---
title: 'Abjad Numerals — The Number-Letter System'
category: 02-Hurufiyya-Lettrism
tradition: Semitic / Islamic
era: Pre-Islamic to 8th century
tags: [numerology, gematria, abjad, calculation]
status: foundation-doc
related:
  - '"[[01-Ilm-al-Huruf-Overview]]"'
  - '"[[08-Kabbalah-Numerology/01-Gematria-Mapping]]"'
---

# Abjad Numerals — The Number-Letter System

## The System

The **abjad** is a Semitic numeral system in which the 28 letters of the Arabic alphabet are assigned fixed numerical values, in ascending order. The name itself is the first four letters (alif, ba', jim, dal = 1, 2, 3, 4) — a memorization acronym like "abacus" or "alphabet".

| Letter | Name | Value | Letter | Name | Value |
|---|---|---|---|---|---|
| ا | alif | 1 | ك | kaf | 20 |
| ب | ba' | 2 | ل | lam | 30 |
| ج | jim | 3 | م | mim | 40 |
| د | dal | 4 | ن | nun | 50 |
| ه | ha' | 5 | س | sin | 60 |
| و | waw | 6 | ع | 'ayn | 70 |
| ز | za'/zay | 7 | ف | fa' | 80 |
| ح | ha' | 8 | ص | sad | 90 |
| ط | ta' | 9 | ق | qaf | 100 |
| ي | ya' | 10 | ر | ra' | 200 |
| | | | ش | shin | 300 |
| | | | ت | ta' | 400 |
| | | | ث | tha' | 500 |
| | | | خ | kha' | 600 |
| | | | ذ | dhal | 700 |
| | | | ض | dad | 800 |
| | | | ظ | dha' | 900 |
| | | | غ | ghayn | 1000 |

## Why the Order Matters

The order is **not arbitrary**. Each letter's value encodes its **planetary** and **zodiacal** correspondence. The *'ilm al-huruf* practitioner needs the *order* to know which letter rules which planet.

For example, the first nine letters (ا to ط) are the "units" (1-9) and correspond to the first three zodiac triplicities:

- Aries: alif, ba', jim (1, 2, 3)
- Taurus: dal, ha', waw (4, 5, 6)
- Gemini: za', ha', ta' (7, 8, 9)

The "tens" (10-90) correspond to the next triplicities, and so on.

## The Reduction

The al-Buni tradition uses **digital root** (modulo 9, with 9 = 9 not 0):

```
abjad(word) = sum of letter values
reduce(word) = abjad(word) mod 9, with 0 → 9
```

This is the same operation as the **Hebrew gematria** tradition in the Kabbalah. The convergence is not coincidence — both traditions inherit from a common Semitic ancestor.

## A Quick Reference for the Library

| Word | Abjad | Reduced | Letter | Planet |
|---|---|---|---|---|
| الله (Allah) | 66 | 3 | jim (ج) | Mercury |
| محمد (Muhammad) | 92 | 2 | ba' (ب) | Moon / Venus (debated) |
| علي (Ali) | 110 | 2 | ba' (ب) | Moon |
| بسم (Bism) | 102 | 3 | jim (ج) | Mercury |
| الرحمن (al-Rahman) | 329 | 5 | ha' (ه) | Sun / Jupiter |
| الرحيم (al-Rahim) | 258 | 6 | waw (و) | Jupiter / Venus |

The "hidden" letter behind a name is the *buruz* — the letter of greatest power in the name, computed by reduction.

## Cross-Reference

- The Hebrew gematria of the Kabbalah ([[08-Kabbalah-Numerology/01-Gematria-Mapping]]) uses an essentially identical system
- The Greek isopsephy ([[01-Origins-Traditions/01-What-Is-Esotericism]]) predates both
- The Greek-Indian and Chinese character-number systems are siblings

This is one of the cleanest cases of **cross-tradition concordance** — the same general technique, independently developed in at least 4 traditions, with the same mathematical structure.
