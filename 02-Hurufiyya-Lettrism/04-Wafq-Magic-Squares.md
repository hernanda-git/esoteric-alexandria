---
title: "Wafq — Magic Squares and Their Power"
category: 02-Hurufiyya-Lettrism
tradition: Islamic / Hermetic
era: 8th century onwards
tags: [wafq, magic-square, planetary, talisman]
status: foundation-doc
related:
  - "[[01-Ilm-al-Huruf-Overview]]"
  - "[[02-Abjad-Numerals]]"
  - "[[05-Talismanic-Magick/01-Squares-And-Sigils]]"
---

# Wafq — Magic Squares

## The Concept

A *wafq* (Arabic: وفق, "harmony, agreement") is a number square in which every row, every column, and both main diagonals sum to the same magic constant. They are central to talismanic practice in the *'ilm al-huruf* tradition.

The tradition claims that the planet's *wafq* is the **mathematical skeleton of the talisman**. Writing a name inside the appropriate *wafq* at the right astrological hour is the core technique of *simiya* (the applied art).

## The Seven Planetary Wafq

The al-Buni tradition gives a *wafq* for each of the seven classical planets. The size of the square is always *n × n* where *n* is the planet's number in the planetary order (Saturn=1, Jupiter=2, …, Moon=7).

The magic constant of a normal *n × n* square is *n(n²+1)/2*.

### Saturn (Zuhal) — 3×3, magic constant 15

```
4 9 2
3 5 7
8 1 6
```

### Jupiter (Al-Mushtari) — 4×4, magic constant 34

```
4  14 15  1
9   7  6 12
5  11 10  8
16  2  3 13
```

### Mars (Al-Mirrrikh) — 5×5, magic constant 65

```
11 24  7 20  3
 4 12 25  8 16
17  5 13 21  9
10 18  1 14 22
23  6 19  2 15
```

### Sun (Al-Shams) — 6×6, magic constant 111

```
6  32  3  21 23  25
12  9  1724  13 36
33  25 18  8  14  13
…  (full 6×6, see al-Buni)
```

### Venus (Al-Zuhra) — 7×7, magic constant 175

```
… (full 7×7 in al-Buni, vol. 1, p.~200)
```

### Mercury (Al-'Utarid) — 8×8, magic constant 260

```
… (full 8×8 in al-Buni, vol. 1, p.~225)
```

### Moon (Al-Qamar) — 9×9, magic constant 369

```
… (full 9×9 in al-Buni, vol. 1, p.~245)
```

The full construction algorithm (the "Siamese method" or "de la Loubère method" in modern terminology) was known to the al-Buni tradition, though the version he gives is the *budūh* method, attributed to Abu al-'Ala' ibn Zuhr (Avenzoar, 12th c.).

## How a Wafq Becomes a Talisman

1. **Select the planet** for your goal (e.g., Mercury for trade, Jupiter for expansion, Venus for relationships)
2. **Draw its wafq** in silver, gold, or ink appropriate to the planet
3. **Write the target name** in the central cell (Sun's wafq) or in the corner (Saturn's wafq) — the placement encodes the request
4. **Time the inscription** to the planet's day and hour (see [[03-Planetary-Astrology/05-Planetary-Hours]])
5. **Breathe upon it** (*nafkh*) three times while reciting the appropriate Divine Name
6. **Fold and carry** the wafq in the appropriate location (Saturn on the body, Jupiter in the wallet, etc.)

The wafq is the **address**; the timing is the **protocol**; the Divine Name is the **authorization**. The analogy to a network packet — header (address) + protocol + authentication — is exact.

## Mathematical Properties of Wafq

A *wafq* is a **normal magic square** by modern standards. The mathematical theory was developed in the 19th century (de la Loubère, 1693; Cayley, 1870s), but the al-Buni tradition was already computing these in the 12th century, with full construction algorithms.

The interesting mathematical facts:

- The 3×3 is unique up to rotation and reflection
- The 4×4 has 880 normal squares up to symmetry
- The 5×5 has ~275 million
- The general count grows factorially

Al-Buni and his predecessors knew the 3×3 through 9×9, and gave construction methods (not just enumeration). The construction methods are **algorithmic** — they can be executed in a loop. This is one of the earliest known examples of a **non-trivial mathematical algorithm** in Islamic literature.

## Cross-References

- The same technique appears in **Jewish Kabbalah** as *kamea* (קמיע) — magic squares for planetary talismans. The 3×3 Saturn wafq and the 3×3 Saturn kamea are identical.
- The same technique appears in **Agrippa's Three Books of Occult Philosophy** (1533) — see [[12-Agrippa-Picatrix-Grimoires/01-Occult-Philosophy]]
- The same technique appears in **China** as *luoshu* (洛書), the 3×3 magic square attributed to the Yellow Emperor, used in feng shui

This is the cleanest case of **independent cross-tradition concordance** in the library.

## See Also

- [[01-Ilm-al-Huruf-Overview]] — the broader system
- [[05-Talismanic-Magick/01-Squares-And-Sigils]] — the Western parallel
- [[03-Planetary-Astrology/01-Seven-Planets]] — what each planet governs
