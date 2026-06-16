---
title: 'Position Sizing — The Real Mathematics of Trading'
category: 20-Trading-Risk-Archetypes
tradition: Modern / Quantitative Trading
era: 20th-21st century
author: Van K. Tharp (b. 1946) — the founder of position-sizing theory in modern trading
tags: [position-sizing, van-tharp, r-multiple, fixed-fractional, kelly-criterion, vol-targeting, fmlm]
status: foundation-doc
core_source: 'Van K. Tharp, Trade Your Way to Financial Freedom (1998, 2nd ed. 2006) and The Definitive Guide to Position Sizing (2008, the dedicated text). The position-sizing theory is grounded in Ralph Vince''s earlier work (The Mathematics of Money Management, 1992) and the original Kelly (1956).'
related:
  - '"[[01-Trading-And-The-Asketikos]]"'
  - '"[[19-Business-Applications/02-Leader-Work-Without-The-Overclaim]]"'
sources:
  - 'Van K. Tharp, \"Trade Your Way to Financial Freedom\" (1998, 2nd ed. 2006)'
  - 'Van K. Tharp, \"The Definitive Guide to Position Sizing\" (2008, the dedicated text)'
  - 'Ralph Vince, \"The Mathematics of Money Management\" (1992)'
  - 'Larry Williams, \"Long-Term Secrets to Short-Term Trading\" (1999)'
  - 'John L. Kelly, \"A New Interpretation of Information Rate\" (1956, the original Kelly paper in the Bell System Technical Journal)'
  - 'Ed Thorp, \"The Mathematics of Gambling\" (1984)'
---

# Position Sizing — The Real Mathematics of Trading

## The Claim

Position sizing is the **single most important** determinant of trading returns. The position size — not the entry, not the exit, not the indicator, not the strategy — is the **primary** driver of the **long-term** returns. The trader who masters position sizing survives; the trader who does not master position sizing blows up.

This is **not** an esoteric claim. This is the **quantitative** consensus of the modern trading literature (Tharp, Vince, Thorp, Williams, and the academic literature on the Kelly criterion). The position sizing is the **mathematics** of the trading; the rest is the **craft**.

## The Mathematics — The Real Numbers

### The R-Multiple

A **R-multiple** (named by Van Tharp, after Vince's R) is the **profit** or **loss** of a trade measured in **units of risk**. A trade that risks $100 and makes $300 is a 3R trade. A trade that risks $100 and loses $100 is a 1R loss. A trade that risks $100 and breaks even is a 0R trade.

The **R-multiple** is the **right** way to **measure** the **outcome** of a trade. The R-multiple is the **standard** of the modern trading literature. The R-multiple is the **trader's** own measurement — the trader **defines** the **R** (the **amount** the trader **is** willing to **lose** on the **trade**), and the R-multiple is the **profit** or **loss** **relative** to the R.

The R-multiple is **independent** of the **size** of the **position** and of the **size** of the **account**. A 3R trade is a 3R trade **whether** the account is $10,000 or $10,000,000. The R-multiple is the **standardized** **measurement** that **allows** the trader to **compare** the **outcome** of **different** **trades** on **different** **instruments** on **different** **timeframes**.

### The System Expectancy

The **system expectancy** is the **average** R-multiple of a series of trades. The system expectancy is calculated as:

```
E = (Win% × AvgWinR) - (Loss% × AvgLossR)
```

The system expectancy is **positive** if the system is **profitable** on the **average**. The system expectancy is **negative** if the system is **unprofitable** on the **average**.

A system with **E = 0.3R** is **profitable** on the **average** of 0.3R per trade. A system with **E = -0.1R** is **unprofitable** on the **average** of 0.1R per trade. The system expectancy is the **single** **number** that **summarizes** the **edge** of the **trading** **system**.

### The Geometric Growth

The **geometric growth** is the **mathematical** **result** that the **compounded** return of a **series** of **trades** is the **geometric** **mean** of the **individual** **trade** **returns**, **not** the **arithmetic** **mean**. The geometric growth is the **mathematical** **reason** why the **position** **size** is **so** **important**.

The **arithmetic** **mean** of the **returns** is **larger** than the **geometric** **mean** of the **returns** (the **arithmetic** **mean** is **biased** **upward** by the **large** **positive** **returns**). The **difference** between the **arithmetic** **mean** and the **geometric** **mean** is **the** **volatility** **drag**. The **volatility** **drag** is the **amount** of the **return** that is **lost** to the **volatility** of the **returns**. The **volatility** **drag** is **larger** for **larger** **position** **sizes** and **for** **more** **volatile** **returns**.

The **position** **size** **controls** the **volatility** **drag**. The **smaller** the **position** **size**, the **smaller** the **volatility** **drag**. The **larger** the **position** **size**, the **larger** the **volatility** **drag**. The **position** **size** is the **balance** between the **return** and the **risk**.

## The Position Sizing Models

### The Fixed-Fractional Model

The **fixed-fractional** **model** is the **simplest** **position** **sizing** **model**. The **trader** **risks** a **fixed** **percentage** of the **account** on **each** **trade**. The **percentage** is **the** **fixed** **fraction**.

For example, a trader who **risks** 1% of the **account** on **each** **trade** **has** a **fixed** **fraction** of 1%. A trader who **risks** 2% of the **account** on **each** **trade** **has** a **fixed** **fraction** of 2%. The **fixed** **fraction** is **the** **same** for **every** **trade**.

The **fixed-fractional** **model** has the **advantage** of **simplicity** and the **disadvantage** of **not** **adapting** to **the** **volatility** of the **instrument** or to **the** **edge** of the **trader**. A trader who **uses** a **fixed** **fraction** of 1% on **a** **low-volatility** **instrument** (a **low** **ATR**) **is** **risking** **more** than a trader who **uses** the **same** **fixed** **fraction** of 1% on a **high-volatility** **instrument** (a **high** **ATR**).

The **fixed-fractional** **model** is **the** **default** in the **modern** **trading** **literature**. The **fixed-fractional** **model** is **the** **basis** of the **risk** **management** of the **institutional** **traders**.

### The Fixed-Ratio Model

The **fixed-ratio** **model** is the **position** **sizing** **model** **developed** by **Ryan Jones** (the **futures** **trader**, not the **musician**) in **the** **1990s**. The **fixed-ratio** **model** **increases** the **position** **size** by **a** **fixed** **delta** for **every** **fixed** **increment** of **the** **account** **growth**. The **fixed** **delta** is **the** **increase** of the **position** **size** for **every** **increment** of the **account** **growth**.

For example, a trader who **uses** a **fixed-ratio** of **$5,000** **per** **contract** **increases** the **position** **size** by **1** **contract** for **every** **$5,000** of the **account** **growth**. A trader who **uses** a **fixed-ratio** of **$10,000** **per** **contract** **increases** the **position** **size** by **1** **contract** for **every** **$10,000** of the **account** **growth**.

The **fixed-ratio** **model** has the **advantage** of **adapting** to the **growth** of the **account** and the **disadvantage** of **not** **adapting** to the **volatility** of the **instrument** or to the **edge** of the **trader**. The **fixed-ratio** **model** is **less** **common** than the **fixed-fractional** **model** in the **modern** **trading** **literature**.

### The Volatility-Targeting Model

The **volatility-targeting** **model** is the **position** **sizing** **model** that **targets** a **fixed** **percentage** of **volatility** of the **portfolio**. The **volatility** is **estimated** from the **recent** **returns** of the **instrument** (the **historical** **volatility** or the **implied** **volatility**). The **position** **size** is **calculated** to **produce** a **portfolio** **volatility** that **equals** the **target**.

For example, a trader who **targets** a **portfolio** **volatility** of 10% **per** **annum** **positions** the **size** of the **trade** so that the **trade** **contributes** 10% **volatility** to the **portfolio**. The **volatility-targeting** **model** has the **advantage** of **adapting** to the **volatility** of the **instrument** (the **higher** the **volatility** of the **instrument**, the **smaller** the **position** **size**). The **volatility-targeting** **model** is **the** **default** in the **modern** **quantitative** **trading** **literature** (the **model** is **used** by **AHL**, **Man Investments**, **Winton**, and the **majority** of **the** **quant** **funds**).

### The Kelly Criterion

The **Kelly** **criterion** is the **mathematical** **formula** for the **optimal** **bet** **size** on a **series** of **independent** **bets** with a **known** **edge**. The **Kelly** **criterion** is **derived** by **John L. Kelly** at **Bell Labs** in **1956** and was **first** **applied** to the **gambling** by **Edward Thorp** (in **the** **1960s**). The **Kelly** **criterion** **maximizes** the **long-term** **geometric** **growth** of the **bankroll**.

The **Kelly** **criterion** **formula** is:

```
f* = (bp - q) / b
```

where **f*** is the **optimal** **fraction** of the **bankroll** to **bet**, **b** is the **net** **odds** of the **bet** (the **gain** **per** **bet** **divided** by the **loss** **per** **bet**), **p** is the **probability** of **winning**, and **q** is the **probability** of **losing** (= 1 - p).

For example, a bet with **b = 2** (the gain is 2x the loss), **p = 0.6** (the win rate is 60%), and **q = 0.4** (the loss rate is 40%) has an **optimal** **fraction** of **f*** = (2 × 0.6 - 0.4) / 2 = **0.4** (40% of the bankroll).

The **Kelly** **criterion** is **optimal** for **the** **long-term** **geometric** **growth**; the **Kelly** **criterion** is **NOT** **optimal** for the **short-term** **survival**. The **Kelly** **criterion** **implies** a **substantial** **drawdown** (the **Kelly** **drawdown** is **approximately** **50%** for a **moderate** **edge**); the **Kelly** **drawdown** is **intolerable** for **most** **traders**. The **practical** **recommendation** is to **bet** **a** **fraction** of the **Kelly** (typically **1/4** to **1/2** Kelly) to **reduce** the **drawdown** to a **tolerable** **level**.

The **Kelly** **criterion** is **the** **mathematical** **basis** of the **modern** **position** **sizing** **literature**. The **Kelly** **criterion** is **the** **starting** **point** of the **modern** **position** **sizing** **theory**. The **Kelly** **criterion** is **not** **the** **complete** **theory**; the **Kelly** **criterion** is **the** **mathematical** **foundation** of the **theory**.

## The Drawdown — The Real Numbers

A **drawdown** is the **peak-to-trough** **decline** of the **account**. The **drawdown** is **measured** as the **percentage** of the **account** that is **lost** from the **peak** to the **trough**. A 50% drawdown is a **loss** of 50% of the **account**; a 30% drawdown is a **loss** of 30% of the **account**.

The **drawdown** is **the** **price** of the **position** **sizing**. The **larger** the **position** **size**, the **larger** the **drawdown**. The **drawdown** is **the** **inevitable** **cost** of the **position** **sizing**; the **drawdown** is **the** **price** of the **return**.

The **drawdown** is **not** a **mystic** **ordeal**; the **drawdown** is a **mathematical** **consequence** of the **position** **sizing**. The **drawdown** is **the** **statistical** **fact** of the **trading**. The **drawdown** is **the** **mathematical** **fact** that the **trader** **must** **accept** **to** **trade** **at** **size**.

The **drawdown** has **three** **components**:

1. **The volatility drawdown** — the **drawdown** that is **due** to the **volatility** of the **returns** (the **larger** the **position** **size**, the **larger** the **volatility** **drawdown**)
2. **The edge drawdown** — the **drawdown** that is **due** to the **edge** of the **trader** (the **smaller** the **edge**, the **larger** the **edge** **drawdown**)
3. **The streak drawdown** — the **drawdown** that is **due** to the **streaks** of **losses** (the **streak** **drawdown** is **independent** of the **edge** and the **volatility**; the **streak** **drawdown** is the **drawdown** that is **due** to the **random** **streak** of **losses**)

The **three** **components** are **additive**; the **total** **drawdown** is the **sum** of the **three** **components**. The **trader** **who** **understands** the **three** **components** **can** **control** the **drawdown** by **adjusting** the **position** **size** (which **adjusts** the **volatility** **drawdown**) and the **edge** (which **is** **the** **only** **component** **the** **trader** **can** **improve** over the **long** **term**).

## The Practice

A modern trader who **wants** the **discipline** of the **position** **sizing** **can**:

1. **Read** the **Tharp** (*Trade Your Way to Financial Freedom*) — the **foundation** of the **modern** **position** **sizing** **literature**
2. **Read** the **Vince** (*The Mathematics of Money Management*) — the **mathematical** **basis** of the **position** **sizing** **theory**
3. **Read** the **Thorp** (*The Mathematics of Gambling*) — the **Kelly** **criterion** **and** its **application** to the **gambling** and to the **trading**
4. **Calculate** the **R-multiple** of **every** **trade** — the **trader** **measures** the **outcome** in **R** rather than in **$**
5. **Calculate** the **system** **expectancy** — the **trader** **calculates** the **system** **expectancy** over the **recent** **trades** (the **last** **20**-**50** **trades**)
6. **Use** a **position** **sizing** **model** — the **trader** **uses** the **fixed-fractional** **model** (the **default**) or the **volatility-targeting** **model** (the **modern** **default**)
7. **Track** the **drawdown** — the **trader** **tracks** the **drawdown** **daily** and **adjusts** the **position** **size** if the **drawdown** **exceeds** the **target**
8. **Maintain** the **practice** **for** **years** — the **position** **sizing** **practice** is **lifelong**; the **practice** is **not** **a** **quick** **fix**

The **position** **sizing** **practice** is **not** **a** **mystic** **tradition**; the **position** **sizing** **practice** is **a** **specific** **modern** **mathematical** **discipline** with **specific** **methodology**, **specific** **measurement**, **specific** **outcomes**.

## The Note

The **position** **size** is **not** **a** **talisman** (the **previous** **draft** **of** the **trading** **doc** **used** the **talisman** **metaphor**; the **metaphor** is **misleading**). The **position** **size** is **a** **mathematical** **parameter** that **controls** the **volatility** **drag** of the **trading**. The **position** **size** is **a** **mathematical** **tool**, **not** a **mystic** **object**.

The **trader** who **understands** the **position** **size** as **a** **mathematical** **tool** is the **trader** who **trades** **at** **size**. The **trader** who **misunderstands** the **position** **size** as **a** **mystic** **object** is the **trader** who **blows** **up**.

## See Also

- [[01-Trading-And-The-Asketikos]] — the ascetical discipline
- [[19-Business-Applications/02-Leader-Work-Without-The-Overclaim]] — the leadership
- [[15-Modern-Parallels/01-Cryptanalysis-As-Modern-Jafr]] — the cryptanalysis bridge
- [[18-Psychology-Jungian/02-Shadow-Work-And-The-Dark-Self]] — the shadow work
