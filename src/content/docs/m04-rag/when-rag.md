---
title: When to use RAG (and when not to)
description: Choosing between RAG, long context, project files, fine-tuning and live tools.
sidebar: { order: 1 }
---

## The options

| Approach | How it works | Best when | Weak when |
|---|---|---|---|
| **Paste or attach** | Put the document in the conversation | One-off questions about a few documents | Many documents; repeated use |
| **Project files / knowledge** | Assistant keeps a set of files for every chat in a project | A stable, modest set of documents for a team | Large or fast-changing corpora |
| **Long context** | Load a big corpus into a very large window | Deep reasoning across a whole codebase or contract set, at modest volume | Cost per question; recall of details in huge inputs |
| **RAG** | Search a large corpus per question; insert the top results | Large, changing knowledge bases; citations needed; access control per document | Questions that need *all* documents at once (e.g. "count every contract with clause X") |
| **Tools / live queries** | The model calls an API, database or search | Live data (orders, tickets, metrics), exact numbers | Unstructured knowledge |
| **Fine-tuning** | Train the model on examples | Consistent style/format, narrow specialised tasks | Adding facts that change |

Most real systems **combine** these: RAG over docs, tools for live data, and instructions for style.

## Signs you need RAG

- People ask "where is the doc that says…?" many times a week.
- Answers must **cite** the policy, contract or runbook they came from.
- Knowledge changes weekly and must be current.
- Different people may see different documents (permissions).

## Signs you don't (yet)

- A dozen documents cover it → use project files.
- The knowledge isn't written down → write it first. RAG can't retrieve what doesn't exist.
- The documents contradict each other → clean up the sources of truth first. RAG will faithfully retrieve the contradiction.

## Buy, configure or build?

Many teams don't need to build RAG at all. Enterprise assistants, workplace search products and knowledge-base tools increasingly include connectors and retrieval over common sources (drives, wikis, ticketing systems). **Start with what your approved tools offer**, evaluate it ([lesson 4](/ai-native-teams/m04-rag/evaluating/)), and build only when you need control over quality, data or integration.
