---
title: Reasoning models, multimodal and small models
description: The main kinds of models in 2026 and what each is good for.
sidebar: { order: 2 }
---

"The model" is no longer one thing. Most providers offer a family of models, and picking the right kind matters more than picking the right brand.

## Reasoning models

Reasoning ("thinking") models spend extra tokens working through a problem before they answer: breaking it down, trying approaches, checking their work. Most frontier models now have this built in, often with a setting for **how much** to think (an "effort" or "thinking budget" setting).

**Good for:** multi-step analysis, maths, planning, debugging, code changes, tricky judgment calls, agentic work.
**Trade-offs:** slower and more expensive per answer; overkill for simple lookups, rewriting or classification.

Practical tips:
- Give reasoning models the **goal and constraints**; you rarely need to spell out every step ("think step by step" mattered more for older models).
- Use low effort for routine tasks and raise it when quality matters. Measure, don't guess (see [M8](/ai-native-teams/m08-evals/)).

## Multimodal models

Most frontier models accept **images, PDFs and screenshots**, and many handle **audio** and some **video**. Separate models generate images, audio, speech and video.

**Good for:** reading charts and scanned documents, describing UI screenshots, turning a whiteboard photo into a plan, transcribing and summarising meetings, accessibility checks.
**Watch out for:** small text in images, exact numbers read from charts, and counting objects. Verify anything that matters.

## Small, open-weight and on-device models

Not every task needs the biggest model.

| Kind | Examples of use | Why choose it |
|---|---|---|
| **Small hosted models** (the "mini/flash/haiku" tier of each provider) | Classification, extraction, routing, summarising, high-volume work | Much cheaper and faster; often good enough |
| **Open-weight models** you can run yourself | Data that can't leave your environment, customisation, cost control at scale | Control over data and deployment; you own the operations |
| **On-device models** (on laptops and phones) | Offline features, privacy-sensitive features, low latency | Data never leaves the device; limited capability |

## Embedding models

A different kind of model that turns text (or images) into **vectors**, lists of numbers where similar meanings are close together. They power semantic search and RAG ([M4](/ai-native-teams/m04-rag/)). They don't generate text.

## Specialised and fine-tuned models

You can adapt a model to your domain by **fine-tuning** on your examples. In practice most teams should try, in this order: better prompts → better context (instructions, examples, retrieval) → a different model → fine-tuning. Fine-tuning helps most with consistent format/style at high volume or a narrow specialised task, and least with adding new facts (retrieval is better for that).

## Team practice

Maintain a short **"which model for what"** table in your playbook, for example: *default assistant*, *deep analysis / hard coding*, *bulk classification*, *sensitive data*. Review it quarterly, because the right answer changes.
