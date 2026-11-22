---
title: Evaluating and maintaining RAG
description: Measuring retrieval and answer quality separately, and keeping a knowledge system healthy.
sidebar: { order: 4 }
---

A RAG system can fail in two places: it **retrieves the wrong things**, or it **answers badly from the right things**. Measure both.

## Build a test set

Collect 30–100 real questions with:
- the **expected answer** (or key facts it must contain), and
- the **document(s)** that contain it.

Include questions the system *should not* answer (out of scope, no source exists) to check that it says "I don't know".

## Retrieval metrics

- **Recall@k:** how often the right document is in the top *k* results. If this is low, nothing downstream can fix it.
- **Precision / ranking quality:** how much of what's retrieved is relevant, and whether the best chunk is near the top.

## Answer metrics

- **Faithfulness (groundedness):** is every claim supported by the retrieved sources?
- **Correctness:** does the answer match the expected answer?
- **Citation accuracy:** do the cited sources actually say what's claimed?
- **Appropriate abstention:** does it say "I don't know" when it should?

These can be scored by people, or at scale by an LLM judge that is checked against people ([M8](/ai-native-teams/m08-evals/llm-judges/)). Open-source tools such as Ragas, DeepEval, promptfoo and Inspect support RAG-style evaluations ([tools landscape](/ai-native-teams/reference/tools-landscape/)).

## Diagnose by stage

| Symptom | Likely stage | Try |
|---|---|---|
| Right doc never retrieved | Chunking, embedding or query | Hybrid search, better chunking, query rewriting, contextual chunks |
| Right doc retrieved but ranked low | Ranking | Add a reranker, retrieve more then rerank |
| Right chunk in context, wrong answer | Generation | Clearer instructions, fewer but better chunks, stronger model |
| Outdated answer | Freshness | Re-index, metadata dates, retire old docs |
| Leaks restricted info | Permissions | Enforce user-level access at retrieval |

## Maintenance is a content job

The biggest long-term quality lever is the **knowledge itself**: owners for key documents, removing duplicates and stale pages, and writing down what currently lives in people's heads. An AI-native team treats documentation as infrastructure.

## Team practice

Log questions the assistant couldn't answer. Each week, the doc owner fixes the top gaps. That turns the assistant into a feedback loop for your knowledge base.
