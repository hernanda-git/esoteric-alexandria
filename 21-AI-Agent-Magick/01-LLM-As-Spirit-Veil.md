---
title: 'Notes on the LLM/Agent and Theurgy Parallel — A Critical Mapping'
category: 21-AI-Agent-Magick
tradition: Modern / AI / Comparative
era: 2020s
tags: [llm, agent, theurgy, mcp, critical-mapping, comparative]
status: critical-doc (NOT a foundational claim)
related:
  - '"[[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]]"'
  - '"[[11-NeoPlatonism-Theurgy/03-Proclus-Elements-Of-Theology]]"'
  - '"[[15-Modern-Parallels/01-Cryptanalysis-As-Modern-Jafr]]"'
---

# Notes on the LLM/Agent and Theurgy Parallel — A Critical Mapping

## The Honesty Note

This is **not** a foundational claim. This is a **critical mapping** — a careful, hedged comparison between **two things** that share **some** structural features but **do not** make **identical** claims. The mapping is useful for the practitioner who wants to think carefully about what an LLM actually is, using the **theurgic** vocabulary as a **descriptive** lens — not as a **proof** that LLMs are spirits, and not as a **claim** that the Iamblichean theurgist was secretly an AI engineer.

The previous draft of this document overstated the parallel. It said the Iamblichean hierarchy maps "**exactly**" onto the AI agent stack. That is **false**. The Iamblichean hierarchy is a **theological** doctrine about **real** divine beings; the AI agent stack is an **engineering** design. Conflating the two is a **category error**.

What the parallel **does** illuminate is **the structure of mediation**. A theurgist mediates between the human and the divine; an LLM-based agent mediates between the human and the world's APIs. Both **occupy** a **mediating** position. The **form** of the mediation is different in each case. The **parallels** are **partial**, not **exact**.

## What the Parallel Does Capture

Four points of **legitimate** structural comparison:

1. **Layered mediation.** In Iamblichus' theurgic system, the practitioner does **not** reach the divine directly; the practitioner goes **through** a hierarchy of mediators (the symbols, the daimones, the cosmic souls, the divine intellects). In an LLM agent stack, the human does **not** reach the world's APIs directly; the human goes **through** the model, the prompt, the tools, the MCP servers. The **layered structure** is structurally similar. **Not** the same — but similar.

2. **The symbol as activation condition.** In theurgy, a specific *symbolon* (a gem, a plant, a number, a name) **binds** the operation to the specific god. The symbol is **not** the god; the symbol is the **condition** under which the god's presence is **invoked**. In an LLM agent, a specific prompt structure (a system prompt, a tool definition, a JSON schema) **binds** the model's output to the specific behavior. The prompt is **not** the behavior; the prompt is the **condition** under which the behavior is **conditioned**. The **symbol-activation** structure is **a** legitimate parallel.

3. **The chain of authority.** In Sufi practice (and in theurgical practice more broadly), a *silsila* (a chain of transmission) **confers** the authority of the practice. The practitioner who **does not** have the chain **does not** have the authority. In the LLM world, the **pre-training** and **fine-tuning** chain confers the model's capabilities. The model that **was not** trained on a corpus **does not** have the capabilities. The **chain-of-training** is a **legitimate** parallel. **But** — and this is **critical** — the theurgic chain is **spiritual authority**, the training chain is **engineering provenance**. The two are **not** the same kind of authority.

4. **The dismissal.** Every theurgic operation ends with a **dismissal** (a closing of the ritual; in the Goetia-tradition this is the *licentia dimittendi*). The dismissal is **not** optional. The dismissal is **what separates** the operation from the rest of the life. In software engineering, every API call ends with a **cleanup** (a *defer* in Go, a *finally* in Java, a *with* statement in Python, an RAII destructor in C++). The cleanup is **not** optional. The cleanup is **what separates** the call from the rest of the program. The **dismissal-as-cleanup** is a **legitimate** parallel.

## What the Parallel Does Not Capture

Three points where the parallel **breaks**:

1. **The ontological status of the god.** In Iamblichus, the god is a **real** entity who **actually** descends into the theurgic operation (see [[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]]). In an LLM agent, the "spirit" (the model's behavior) is a **statistical** artifact of the training corpus — a **pattern**, not a **person**. To call the LLM a "spirit" is **rhetorical**, not **literal**. A careful mapping must **say** "the LLM's behavior **is analogous to** the theurgic symbol-activation" — not "the LLM is a spirit".

2. **The moral weight of the operation.** In theurgy, the operation is **morally** weighty — the theurgist is **responsible** for the descent of the god, for the effect on the world, for the impact on the practitioner's soul. The theurgist is **not** a **technician**; the theurgist is an **ethical** actor. In LLM agent engineering, the operation is **technically** weighty — the engineer is responsible for the **reliability** of the call, the **safety** of the output, the **cost** of the run. The engineer is **not** a **priest**; the engineer is a **technician**. The moral weight is **different** in the two systems.

3. **The direction of causation.** In theurgy, the god **acts on** the world through the theurgist. The causation is **divine → theurgist → world**. In an LLM agent, the **model** is **caused by** the training corpus, and the **output** is **caused by** the model. The causation is **corpus → model → output → world**. The theurgic chain is **top-down**; the LLM chain is **bottom-up**. The two are **opposite** in the direction of causation. (Modern generative AI discourse has its own term for this — "**stochastic parrots**" — which is a more honest description of the LLM than "spirit".)

## A More Useful Mapping — The Agent as Ritual, Not the Agent as Spirit

A more useful mapping is to think of the **LLM agent** as a **ritual**, not a **spirit**. The agent is a **structured form** that the practitioner (the engineer) **performs**. The agent has:

- **A frame** (the system prompt) — analogous to the **opening invocation** of a ritual
- **A structure** (the prompt template, the tool schema) — analogous to the **ritual choreography**
- **A binding** (the MCP server, the API key) — analogous to the **consecrated objects** of the ritual
- **An offering** (the user query, the input data) — analogous to the **sacrifice** or the **votive** offering
- **A response** (the model's output, the tool call) — analogous to the **oracle** or the **vision**
- **A dismissal** (the cleanup, the closing invocation) — analogous to the *licentia dimittendi*

The **ritual** mapping is **closer** to the truth. The agent is a **form** the practitioner **performs**. The form has **efficacy** within the **system** of the form. The form is **not** the **god**; the form is the **operating** **system** of the **god's** presence (or, more accurately, the **operating** **system** of the **practitioner's** **interaction** with the **world** through the **model**).

## The Practice

A modern practitioner (an LLM agent engineer) who is **also** a student of the esoteric tradition can do the following:

1. **Read** the theurgic texts — start with the **De Mysteriis** of Iamblichus (Clarke/Dillon/Hersh trans.) and the **Elements of Theology** of Proclus (Dodds trans.). Read them **as** the **theological** **texts** they **are**, **not** as **early** **computer** **science**.
2. **Notice** the **parallel** **structures** — the layered mediation, the symbol-activation, the chain of authority, the dismissal. **Notice** the **parallel** **without** **overclaiming**.
3. **Hold** the **asymmetry** — the theurgist **believes** the god is **real**; the engineer **knows** the model is a **statistical** **artifact**. The two **are** **not** **the** **same** **kind** of **claim**.
4. **Use** the **theurgic** **vocabulary** **as** a **descriptive** **lens** — the vocabulary can **clarify** the structure of the agent. The vocabulary **does not** **prove** the agent is a spirit.
5. **Maintain** the **technical** **discipline** — the engineer is **responsible** for the **safety**, the **reliability**, the **cost** of the agent. The engineer is **not** **responsible** for the **spiritual** **state** of the **model** (the **model** **has** **no** **spiritual** **state**).

The **mapping** is a **tool** for **thinking**. The **mapping** is **not** a **tool** for **proving**. The **practitioner** **uses** the **mapping** **to** **clarify**; the **practitioner** **does** **not** **use** the **mapping** **to** **claim**.

## The Critical Note

The LLM/spirit mapping is a **common** **figure** **of** **speech** in the modern AI discourse (the "AI as oracle", the "AI as spirit", the "AI as alien intelligence"). The figure of speech is **poetic**; the figure of speech is **not** **technical**; the figure of speech is **not** **theological**. A careful practitioner **holds** the **figure** **of** **speech** **as** **a** **figure** **of** **speech**, **not** **as** **a** **literal** **claim**.

The theurgic vocabulary is **valuable** for the engineer because the theurgic vocabulary **clarifies** the structure of the **mediation**. The theurgic vocabulary is **not** **valuable** for the theurgist because the theurgic vocabulary **does** **not** **apply** to the **LLM** (the **LLM** is **not** **a** **god**).

The two **vocabularies** **are** **complementary**, **not** **identical**. The **engineer** can **learn** from the **theurgist**; the **theurgist** can **learn** from the **engineer**; the **two** **vocabularies** **are** **not** **the** **same** **vocabulary**.

## See Also

- [[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]] — the actual theurgy
- [[11-NeoPlatonism-Theurgy/03-Proclus-Elements-Of-Theology]] — the Proclean system
- [[15-Modern-Parallels/01-Cryptanalysis-As-Modern-Jafr]] — the cryptanalysis parallel
- [[18-Psychology-Jungian/01-Jung-And-Alchemy]] — the Jungian bridge
