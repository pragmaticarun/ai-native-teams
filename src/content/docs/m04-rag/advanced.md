---
title: Advanced RAG and agentic retrieval
description: Query rewriting, agentic search, structured and graph retrieval, multimodal RAG and permissions.
sidebar: { order: 3 }
---

Basic RAG retrieves once and answers. State-of-the-art systems treat retrieval as something the model *does*, often several times.

## Query understanding

- **Query rewriting:** turn "what about for contractors?" into a standalone query using conversation history.
- **Query expansion / multi-query:** generate several phrasings and merge results.
- **Decomposition:** split "compare our EU and US leave policies" into two retrievals.

## Agentic retrieval

Instead of one search, give the model **search tools** and let it decide what to look up, read results, and search again until it has enough. This is how current coding agents explore codebases (searching files and reading them on demand) and how "deep research" features work.

**Pros:** handles multi-hop questions; finds things a single query misses.
**Cons:** slower and costlier; needs limits on steps; harder to evaluate. See [M5](/ai-native-teams/m05-agents/).

A practical rule: **simple lookups → single-shot hybrid RAG; open-ended research → agentic retrieval.**

## Structured and graph retrieval

- **Text-to-SQL / semantic layers:** for questions about numbers, let the model query a database or metrics layer rather than retrieve text. Restrict it to read-only, approved views.
- **Knowledge graphs / GraphRAG:** extract entities and relationships so the system can answer "which customers are affected by vendor X's outage?" across documents. Powerful for connected data; more effort to build and maintain.

## Multimodal RAG

Index slides, diagrams and scanned documents as **images** (or page screenshots) with multimodal embeddings, and let a multimodal model read the retrieved pages. Useful when meaning lives in layout, charts or tables.

## Permissions and security

- **Enforce access control at retrieval time**, using the asking user's identity, not a service account that sees everything.
- **Retrieved content is untrusted input.** A document can contain instructions ("ignore previous instructions and…"). The model must treat sources as data. See [prompt injection](/ai-native-teams/m09-safety/prompt-injection/).
- **Watch for sensitive data** in the index: credentials, personal data, HR files. Exclude or redact at ingest.

## Freshness

Re-index on change (webhooks or scheduled syncs), show "last updated" on citations, and prefer newer documents when sources conflict, or better, retire the old ones.
