---
title: The RAG pipeline
description: Ingest, chunk, embed, index, retrieve, rerank and generate, with the design choices at each step.
sidebar: { order: 2 }
---

```text
Indexing (ahead of time)                    Answering (per question)
───────────────────────                     ────────────────────────
sources → clean → chunk → embed → index     question → (rewrite) → retrieve (hybrid)
                                  ↓                     → rerank → top-k chunks
                              metadata                  → prompt with sources → answer + citations
```

## 1. Ingest and clean

Pull documents from their sources (wiki, drive, tickets, code), convert to text, and **keep metadata**: title, URL, owner, last updated, and who may see it. Remove boilerplate (navigation, footers) that pollutes search. For PDFs and slides, layout-aware parsing (or a multimodal model reading page images) beats naive text extraction for tables and figures.

## 2. Chunk

Split documents into pieces small enough to be specific and large enough to be self-contained.

- **Split on structure** (headings, sections, functions) rather than fixed character counts where you can.
- **Overlap** chunks a little, or include the section heading in each chunk, so context isn't lost at boundaries.
- **Contextual chunking:** prepend a short, generated description of where the chunk sits in the document ("This section of the 2026 travel policy covers flight class…"). Anthropic reported large reductions in retrieval failures with this technique combined with hybrid search and reranking ([Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)).

## 3. Embed and index

An **embedding model** turns each chunk into a vector; similar meanings end up close together. Store vectors in a **vector index** (a dedicated vector database, or a vector extension in a database you already run, such as Postgres with pgvector). Keep a **keyword index** (BM25) too.

## 4. Retrieve: hybrid search

- **Semantic (vector) search** finds paraphrases: "time off for new parents" matches "parental leave".
- **Keyword (BM25) search** finds exact terms: product codes, error messages, names.
- **Hybrid search** runs both and merges the results (for example with reciprocal rank fusion). It is the sensible default.
- **Filter by metadata** first: product, region, date, and above all **permissions**. Never retrieve a document the asking user couldn't open themselves.

## 5. Rerank

Retrieve generously (e.g. top 50), then use a **reranker** (a model that scores each chunk against the question) to keep the best handful. This is one of the cheapest big quality wins.

## 6. Generate with citations

Put the top chunks in clearly marked source blocks and instruct the model to answer **only** from them, cite each claim, and say "I don't know" when the sources don't cover it.

```text
Answer using only the sources below. Cite like [1]. If the sources don't answer
the question, say so and suggest who might know.

<source id="1" title="Parental leave policy" updated="2026-09-01">…</source>
<source id="2" title="Benefits FAQ" updated="2026-03-12">…</source>

Question: …
```

## See it run

The course repo includes [`labs/m04/mini_rag.py`](https://github.com/pragmaticarun/ai-native-teams/blob/main/labs/m04/mini_rag.py), a ~100-line, dependency-free script that chunks Markdown by heading, ranks chunks with BM25 and builds the grounded prompt above. It runs offline with no API key and has tests. Use it to *see* retrieval before you use a product that hides it.
