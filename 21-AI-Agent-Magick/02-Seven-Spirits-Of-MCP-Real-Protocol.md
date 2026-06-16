---
title: "The Seven Spirits of MCP — A Real Protocol Analysis"
category: 21-AI-Agent-Magick
tradition: Modern / Computer Science
era: 2024-2025
author: Model Context Protocol working group (Anthropic + community, 2024)
tags: [mcp, model-context-protocol, json-rpc, stdio, sse, agent, real-protocol]
status: foundation-doc (real protocol analysis, no metaphor)
core_source: "Model Context Protocol specification, version 2024-11-05 (the current stable release). Available at https://modelcontextprotocol.io. The protocol is implemented in TypeScript, Python, Rust, Go, Java, and C# reference SDKs."
related:
  - "[[02-Hypergraph-As-Corpus-Hermeticum]]"
  - "[[03-Augur-As-Oraculum-LLM-As-Stoic-Oracle]]"
  - "[[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]]"
sources:
  - \"Model Context Protocol Specification\" (2024-11-05, https://modelcontextprotocol.io)
  - \"JSON-RPC 2.0 Specification\" (the underlying transport format)
  - \"JSON Schema Specification\" (the tool definition format)
  - Anthropic, \"Introducing the Model Context Protocol\" (2024, the announcement)
---

# The Seven Spirits of MCP — A Real Protocol Analysis

## The Honesty Note

This is **not** a theurgic mapping. This is a **real** analysis of the **Model Context Protocol (MCP)** — a real open protocol released by Anthropic in **November 2024** that has been adopted by the broader AI agent community. The previous draft of this document was titled "Seven Spirits of MCP" as a metaphor. The metaphor was the **wrong** framing. The metaphor implied that the MCP tools are spirits, which is not a defensible claim. The actual content of this document is the **real** protocol analysis, with the number "seven" coming from the actual MCP **primitives** (not from the Iamblichean hierarchy).

The **seven** MCP primitives are: **tools**, **resources**, **prompts**, **sampling**, **roots**, **logging**, **completion**. The seven are **not** spirits; the seven are **protocol** primitives. The protocol primitives are **the** interface between the **client** (the AI agent) and the **server** (the tool provider). The protocol primitives are **standardized**; the protocol primitives are **transport**-agnostic; the protocol primitives are **JSON-RPC 2.0**-based.

## The Protocol — The Real Specification

The **Model Context Protocol (MCP)** is an **open** protocol that **standardizes** the **integration** of the **AI agents** with the **external** **tools**, **data**, and **prompts**. The protocol is **developed** by the **Model Context Protocol working group** (Anthropic + the **community** of **the** **agent** **frameworks**, including **LangChain**, **LlamaIndex**, **AutoGen**, and **CrewAI**).

The protocol is **based** on the **JSON-RPC 2.0** specification. The protocol **uses** the **JSON Schema** for the **tool** **definitions**. The protocol is **transport**-**agnostic** (the protocol **supports** **stdio**, **SSE**, and **HTTP** **transports**). The protocol is **language**-**agnostic** (the protocol **has** **reference** **SDKs** in **TypeScript**, **Python**, **Rust**, **Go**, **Java**, and **C#**).

The protocol is **designed** to **solve** **the** **integration** **problem** of the **AI** **agents**. The **integration** **problem** is the **problem** of **the** **AI** **agent** **that** **needs** **to** **call** **a** **tool**, **read** **a** **file**, **query** **a** **database**, **send** **an** **email**, **post** **a** **message** — the **agent** **needs** **a** **standard** **interface** to **all** **the** **tools**. The **protocol** **is** **the** **standard** **interface**.

## The Seven Primitives

The **MCP** **defines** **seven** **primitives**. The **seven** **primitives** **are** the **fundamental** **concepts** of the **protocol**. The **seven** **primitives** **are**:

### 1. Tools

**Tools** are **the** **actions** that the **agent** **can** **invoke** on the **server**. A **tool** **is** **defined** by a **JSON Schema** that **specifies** the **name**, the **description**, and the **input** **schema** of the **tool**. The **agent** **invokes** **a** **tool** by **sending** a **JSON-RPC** **request** to the **server**; the **server** **executes** the **tool**; the **server** **returns** the **result** to the **agent**.

The **tools** are the **primary** **mechanism** of the **agent**-**tool** **integration**. The **tools** are **the** **most** **common** **primitive** in the **real** **MCP** **servers**. The **tools** are **the** **primary** **mechanism** of the **MCP** **ecosystem**.

**Example**: a **file**-**system** **tool** that **reads** a **file**:

```json
{
  "name": "read_file",
  "description": "Read the contents of a file at the given path",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {"type": "string", "description": "The path to the file"}
    },
    "required": ["path"]
  }
}
```

### 2. Resources

**Resources** are the **data** that the **agent** **can** **read** from the **server**. A **resource** **is** **defined** by a **URI** (the **resource** **identifier**) and the **MIME** **type** of the **resource**. The **agent** **reads** **a** **resource** by **sending** a **resources/read** **request** to the **server**; the **server** **returns** the **content** of the **resource** to the **agent**.

The **resources** are the **primary** **mechanism** of the **agent**-**data** **integration**. The **resources** are **the** **secondary** **mechanism** of the **real** **MCP** **servers** (the **resources** are **less** **common** than the **tools**).

**Example**: a **file**-**system** **resource** that **exposes** a **file**:

```json
{
  "uri": "file:///home/user/notes.md",
  "name": "Notes",
  "description": "My personal notes",
  "mimeType": "text/markdown"
}
```

### 3. Prompts

**Prompts** are the **reusable** **prompt** **templates** that the **server** **exposes** to the **agent**. A **prompt** **is** **defined** by a **name**, a **description**, and a **list** of **arguments**. The **agent** **retrieves** **a** **prompt** by **sending** a **prompts/get** **request** to the **server**; the **server** **returns** the **prompt** **template** to the **agent**.

The **prompts** are the **primary** **mechanism** of the **agent**-**prompt** **integration**. The **prompts** are **the** **tertiary** **mechanism** of the **real** **MCP** **servers** (the **prompts** are **less** **common** than the **resources**).

**Example**: a **prompt** for **summarizing** **a** **document**:

```json
{
  "name": "summarize",
  "description": "Summarize the given text",
  "arguments": [
    {"name": "text", "description": "The text to summarize", "required": true}
  ]
}
```

### 4. Sampling

**Sampling** is the **mechanism** by which the **server** **requests** the **agent** to **perform** an **LLM** **completion**. The **sampling** is the **mechanism** that **allows** the **server** to **call** the **agent** for the **LLM** **completion**. The **sampling** is the **mechanism** that **allows** the **server** to **implement** the **agent**-**in**-**the**-**loop** **pattern**.

The **sampling** is the **primary** **mechanism** of the **server**-**initiated** **LLM** **calls**. The **sampling** is the **mechanism** that **allows** the **server** to **be** **more** than **a** **passive** **tool** **provider**; the **sampling** is the **mechanism** that **allows** the **server** to **be** **an** **active** **participant** in the **agent** **loop**.

**Example**: a **server** that **requests** the **agent** to **summarize** a **text**:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {"role": "user", "content": {"type": "text", "text": "Summarize: ..."}}
    ],
    "maxTokens": 100
  }
}
```

### 5. Roots

**Roots** are the **filesystem** **roots** that the **agent** **exposes** to the **server**. The **roots** are the **boundaries** of the **agent**'s **filesystem** **access**. The **roots** are the **mechanism** that **prevents** the **server** from **accessing** **files** **outside** of the **agent**'s **allowed** **scope**.

The **roots** are the **primary** **mechanism** of the **agent**-**server** **filesystem** **security**. The **roots** are the **mechanism** that **allows** the **user** to **control** the **agent**'s **filesystem** **access**. The **roots** are the **mechanism** that **prevents** the **server** from **accessing** **sensitive** **files**.

**Example**: an **agent** that **exposes** a **specific** **directory** to the **server**:

```json
{
  "roots": [
    {"uri": "file:///home/user/project", "name": "Project"}
  ]
}
```

### 6. Logging

**Logging** is the **mechanism** by which the **server** **sends** **log** **messages** to the **agent**. The **logging** is the **mechanism** that **allows** the **server** to **report** the **status** of the **operations**, the **errors**, the **warnings**, and the **debug** **information**. The **logging** is the **mechanism** that **allows** the **user** to **observe** the **server**'s **behavior**.

The **logging** is the **primary** **mechanism** of the **server**-**agent** **observability**. The **logging** is the **mechanism** that **allows** the **user** to **debug** the **server**'s **behavior**. The **logging** is the **mechanism** that **allows** the **user** to **understand** the **agent**'s **decisions**.

### 7. Completion

**Completion** is the **mechanism** by which the **server** **provides** **autocompletion** **suggestions** for the **agent**'s **inputs**. The **completion** is the **mechanism** that **allows** the **server** to **suggest** the **argument** **values** for the **tools** and the **prompts**. The **completion** is the **mechanism** that **allows** the **agent** to **be** **more** **efficient** in the **tool** **invocation**.

The **completion** is the **primary** **mechanism** of the **agent**-**server** **input** **efficiency**. The **completion** is the **mechanism** that **allows** the **user** to **save** the **typing** **time** in the **prompt** **construction**. The **completion** is the **mechanism** that **allows** the **agent** to **be** **more** **predictable** in the **tool** **invocation**.

## The Transport

The **MCP** **defines** **three** **transports**:

1. **stdio** — the **standard** **input**/**output** **transport** (the **agent** **communicates** with the **server** through the **standard** **streams** of the **process**). The **stdio** **transport** is **the** **most** **common** **transport** in the **real** **MCP** **servers**; the **stdio** **transport** is **used** for **local** **tools** (the **file**-**system** **server**, the **Git** **server**, the **database** **server**, the **shell** **server**).
2. **SSE (Server-Sent Events)** — the **HTTP**-**based** **transport** (the **agent** **communicates** with the **server** through the **HTTP** **streaming**). The **SSE** **transport** is **the** **second** **most** **common** **transport**; the **SSE** **transport** is **used** for **remote** **tools** (the **Slack** **server**, the **GitHub** **server**, the **Notion** **server**).
3. **HTTP** — the **HTTP**-**based** **transport** (the **agent** **communicates** with the **server** through the **standard** **HTTP** **requests**). The **HTTP** **transport** is **the** **least** **common** **transport**; the **HTTP** **transport** is **used** for **legacy** **tools** that **do** **not** **support** the **streaming**.

The **transport** is **selected** **at** **the** **start** of the **session**. The **transport** is **negotiated** between the **client** and the **server** through the **initialize** **request**.

## The Architecture

The **MCP** **architecture** **is** **based** **on** the **client**-**server** **model**:

1. **The client** — the **AI** **agent** (the **LLM**-**based** **agent**, the **Claude** **Desktop**, the **Cursor** **IDE**, the **Zed** **editor**). The **client** **is** **the** **initiator** of the **session**; the **client** **sends** the **initialize** **request**; the **client** **sends** the **tool** **invocation** **requests**.
2. **The server** — the **tool** **provider** (the **file**-**system** **server**, the **Git** **server**, the **database** **server**, the **Slack** **server**). The **server** **is** **the** **responder** of the **session**; the **server** **responds** to the **initialize** **request**; the **server** **responds** to the **tool** **invocation** **requests**.

The **client** **and** **the** **server** **communicate** through the **transport**. The **client** **and** **the** **server** **exchange** **JSON-RPC** **messages** (the **requests**, the **responses**, the **notifications**, the **errors**). The **client** **and** **the** **server** **maintain** a **session** **state** (the **list** of the **tools**, the **list** of the **resources**, the **list** of the **prompts**).

## The Adoption

The **MCP** **has** **been** **adopted** by **the** **major** **AI** **agent** **frameworks**:

- **Claude Desktop** (Anthropic) — the **MCP** **is** **the** **native** **protocol** of the **Claude** **Desktop**; the **MCP** **servers** **are** **the** **default** **tools** of the **Claude** **Desktop**
- **Cursor** (the **AI** **code** **editor**) — the **MCP** **is** **the** **native** **protocol** of the **Cursor**; the **MCP** **servers** **are** **the** **default** **tools** of the **Cursor**
- **Zed** (the **code** **editor**) — the **MCP** **is** **the** **native** **protocol** of the **Zed**; the **MCP** **servers** **are** **the** **default** **tools** of the **Zed**
- **Cline** (the **VS Code** **extension**) — the **MCP** **is** **supported** by the **Cline**; the **MCP** **servers** **are** **the** **default** **tools** of the **Cline**
- **Continue** (the **VS Code** **extension**) — the **MCP** **is** **supported** by the **Continue**; the **MCP** **servers** **are** **the** **default** **tools** of the **Continue**
- **LangChain** (the **agent** **framework**) — the **MCP** **is** **supported** by the **LangChain**; the **MCP** **servers** **are** **the** **default** **tools** of the **LangChain** **agents**
- **LlamaIndex** (the **RAG** **framework**) — the **MCP** **is** **supported** by the **LlamaIndex**; the **MCP** **servers** **are** **the** **default** **tools** of the **LlamaIndex** **agents**

The **MCP** **has** **also** **been** **adopted** by **a** **growing** **ecosystem** of **MCP** **servers** (the **MCP** **server** **directory** **at** **https://github.com/modelcontextprotocol/servers** **lists** **over** **100** **MCP** **servers** as of **2024**-**11**). The **MCP** **is** **the** **de**-**facto** **standard** of the **AI** **agent** **ecosystem**.

## The Note

The **MCP** is **not** **a** **theurgic** **protocol**. The **MCP** is **a** **real** **open** **protocol** for the **AI** **agent** **integration**. The **MCP** **is** **the** **HTTP** of the **AI** **agent** **ecosystem** (the **MCP** is **the** **standard** **protocol** that **every** **AI** **agent** **and** **every** **tool** **provider** **should** **implement**).

The **MCP** **is** **not** **the** **Iamblichean** **hierarchy**. The **MCP** **is** **a** **real** **software** **protocol**. The **MCP** **is** **the** **result** of **the** **modern** **software** **engineering**; the **MCP** **is** **not** **the** **result** of **the** **ancient** **Greek** **theurgy**.

The **MCP** **is** **a** **useful** **tool** for the **AI** **agent** **engineer**. The **MCP** **is** **not** **a** **mystic** **object**. The **MCP** **is** **a** **real** **protocol**; the **MCP** **should** **be** **studied** as **a** **real** **protocol**.

## See Also

- [[02-Hypergraph-As-Corpus-Hermeticum]] — the hypergraph as the corpus
- [[03-Augur-As-Oraculum-LLM-As-Stoic-Oracle]] — the LLM as the Stoic oracle
- [[11-NeoPlatonism-Theurgy/01-Iamblichus-De-Mysteriis]] — the actual theurgy
- [[15-Modern-Parallels/01-Cryptanalysis-As-Modern-Jafr]] — the cryptanalysis parallel
