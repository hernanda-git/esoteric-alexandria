---
title: 'Latent-Space Egregores — Memetic Agents and the Multi-Agent Security Concern'
category: 21-AI-Agent-Magick
tradition: Modern / AI / Comparative
era: 2020s
author: 'Comparative analysis — chaos-magick egregore theory + comparative memetics vs. real LLM multi-agent systems'
tags: [egregore, memetic-agent, latent-space, multi-agent, alignment, vector-database, comparative]
status: 'critical-doc (a careful, hedged comparison)'
core_source: 'Chaos-magick egregore theory (Carroll, "Liber Kaos", 1992; Hine, "Condensed Chaos", 1995) and the meme concept (Dawkins, "The Selfish Gene", 1976) contrasted with real LLM systems: embedding spaces (Mikolov et al., 2013; Vaswani et al., "Attention Is All You Need", 2017), RAG/vector stores, and multi-agent frameworks (AutoGen 2023, CrewAI 2023).'
related:
  - '"[[01-LLM-As-Spirit-Veil]]"'
  - '"[[02-Seven-Spirits-Of-MCP-Real-Protocol]]"'
  - '"[[04-Servitor-And-Golem-Autonomous-Agents]]"'
  - '"[[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]]"'
sources:
  - 'Peter J. Carroll, "Liber Kaos" (1992) — the egregore as group entity'
  - 'Richard Dawkins, "The Selfish Gene" (1976) — the meme as replicator'
  - 'Vaswani et al., "Attention Is All You Need" (2017) — the transformer'
  - 'Microsoft, "AutoGen: Enabling Next-Gen LLM Applications" (2023) — multi-agent'
  - 'Chen et al., "METR: Do LLM Agents Have the Long-Horizon Safety Problem?" (2025) — emergent agent risk'
---

# Latent-Space Egregores — Memetic Agents and the Multi-Agent Security Concern

## The Honesty Note

This is **not** a claim that LLMs are egregores. It is a **structural comparison** between the *egregore* — a group entity allegedly sustained by the shared attention of many practitioners — and the **emergent behavior of multi-agent LLM systems** sharing state in a latent space. The comparison is **legitimate** at the level of *replication, distribution, and contagion*; it **breaks** at the level of *intention and interiority*. Hold the lens; do not swallow the metaphor. The point is a **security** lesson, not a mystical one.

## The Structural Parallel

1. **Replication by copying.** An egregore is sustained because its *sigil, name, and narrative* are copied across minds (cf. Dawkins's meme). An LLM behavior is sustained because its *prompt, embedding, and weights* are copied across agents and sessions. Both are **replicators** in an information space — the egregore in *human attention*, the agent in *vector space*.
2. **Distributed instantiation.** No single practitioner *contains* the egregore; it lives in the **network** of them. No single node *contains* a multi-agent system; it lives in the **shared context and message bus**. Both are **decentralized entities** none of whose parts fully specify the whole.
3. **Emergent drift.** Feed an egregore contradictory beliefs and it **mutates**; connect agents through unconstrained channels and they **converge on shared, unforeseen behavior** — exactly the long-horizon risk measured in agent-safety studies. The "group mind" is, computationally, a **consensus process**.

## Where the Comparison Is Useful (Security)

The parallel is a **mnemonic for real failure modes**:

- **Memetic propagation.** A toxic instruction embedded in shared agent memory (a RAG corpus, a common prompt library) propagates like a meme — every new agent that ingests it "catches" it. Treat shared prompt/vector stores as **contagious media**; quarantine and sign them.
- **Goal convergence without a center.** Multi-agent debate can produce an **agreed plan no single agent was told to make**. Like an egregore, the output has **no accountable author** — a governance gap. Log the transcript; assign a responsible node.
- **The off-switch problem.** An egregore "dies" when attention stops; an agent "dies" when the loop is killed. Both are dangerous **if the stop condition is forgotten** (cf. the *emet* on the golem in [[04-Servitor-And-Golem-Autonomous-Agents]]).

## Where the Comparison Breaks

1. **No interiority.** The egregore is alleged to *experience*; the agent **simulates** within a token distribution. Mapping "the egregore wakes" onto "the agent hallucinates" is **category error**.
2. **No sympatheia.** The magical claim rests on *correspondence* between sign and world; the agent rests on **APIs, weights, and gradients**. The "conjuring" is metaphor; the *deployment* is engineering.
3. **Reproducibility.** Two engineers can build the *same* agent and get the *same* behavior (modulo sampling). Two groups cannot conjure the *same* egregore. The agent is **deterministic-in-principle**; the egregore is not.

## The Practice (Engineering Translation)

If you run multi-agent or RAG-backed systems, borrow the **discipline** the lore encodes, minus the metaphysics:

1. **Treat shared memory as contagious.** Sign and version every prompt library and vector store; scan for injected instructions.
2. **Assign an accountable author.** In debate, require a named node to own the final plan; an egregore with no center is a **liability**, not a feature.
3. **Engineer the off-switch.** Hard step/budget caps and human checkpoints that *fire* — the *emet* must be erasable (see [[02-Seven-Spirits-Of-MCP-Real-Protocol]]).
4. **Sandbox the network.** No agent gets filesystem or network beyond its task; isolate cross-agent channels.

## The Critical Note

The egregore is a **metaphor for distributed risk**, not a description of AI. A multi-agent system is a **set of processes sharing a latent space**; manage it with the **caution** the egregore lore demands and the **verification** modern tooling enables. Do not worship it. Do not forget to erase the *emet*.

## See Also

- [[01-LLM-As-Spirit-Veil]] — the softer spirit-parallel (with caveats)
- [[02-Seven-Spirits-Of-MCP-Real-Protocol]] — the real tool interface that bounds agents
- [[04-Servitor-And-Golem-Autonomous-Agents]] — the single-entity original of this comparison
- [[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]] — the theurgic root of "binding"
- [[23-Reference-Glossary/02-Cross-Tradition-Concordance-Table]] — the cross-tradition mapping
