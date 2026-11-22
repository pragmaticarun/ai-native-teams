---
title: Glossary
description: Plain-language definitions of the terms used in this course.
sidebar: { order: 2 }
---

| Term | Meaning |
|---|---|
| **Agent** | A model that takes actions with tools in a loop until a goal is reached |
| **Agent Skills** | An open format for packaging know-how as folders with a `SKILL.md`, loaded only when relevant |
| **AGENTS.md** | An open Markdown file format for instructions to coding agents, placed in a repository |
| **AI-native** | Workflows designed assuming capable AI, with humans accountable and outcomes measured |
| **Autonomy level** | How much an agent does without a human; a design choice per task |
| **Chunking** | Splitting documents into pieces for retrieval |
| **Compaction** | Summarising older context so a long session can continue |
| **Context engineering** | Choosing what information a model sees, when, and in what form |
| **Context window** | The maximum amount of text (in tokens) a model can consider at once |
| **Embedding** | A vector of numbers representing meaning; similar meanings are close together |
| **Eval** | A systematic test of AI behaviour over many examples, scored against criteria |
| **Few-shot** | Giving examples of the desired output in the prompt |
| **Fine-tuning** | Further training a model on your examples |
| **Grounding** | Basing answers on provided sources, usually with citations |
| **Guardrail** | A check that blocks or modifies unsafe inputs or outputs |
| **Hallucination (confabulation)** | Fluent, confident output that is false |
| **Human-in-the-loop (HITL)** | A human reviews or approves at defined points |
| **Hybrid search** | Combining keyword (BM25) and semantic (vector) search |
| **LLM** | Large language model: predicts the next token given text so far |
| **LLM-as-judge** | Using a model to grade outputs against criteria, calibrated against humans |
| **MCP (Model Context Protocol)** | An open protocol connecting AI applications to tools and data through servers |
| **Multimodal** | Handling more than text: images, audio, video, documents |
| **Prompt caching** | Provider feature that discounts and speeds up repeated prompt prefixes |
| **Prompt injection** | Instructions hidden in input or content that hijack a model |
| **RAG** | Retrieval-augmented generation: retrieve relevant knowledge, add it to context, answer with citations |
| **Reasoning model** | A model trained to think through problems at length before answering |
| **Reranker** | A model that re-scores retrieved results for relevance |
| **Spec-driven development** | Requirements → design → tasks → code, with specs as the main human artefact |
| **Structured output** | Output constrained to a format or JSON Schema |
| **Sycophancy** | A model's tendency to agree with or flatter the user |
| **System prompt** | Instructions set by the product or developer that frame every conversation |
| **Temperature** | A setting controlling how random sampling is |
| **Token** | The unit models read and write; roughly ¾ of an English word on average |
| **Tool calling** | A model requesting that the application run a function with given arguments |
| **Trajectory** | The sequence of steps and tool calls an agent took |
| **Lethal trifecta** | Private data + untrusted content + external communication in one AI system: the conditions for data theft via injection |
