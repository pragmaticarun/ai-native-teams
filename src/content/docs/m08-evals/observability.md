---
title: Observability, cost and latency
description: Tracing AI systems, monitoring quality in production, and managing cost and speed.
sidebar: { order: 4 }
---

## Trace everything

For any AI system in production, record a **trace** per request: inputs, retrieved context, prompts, model and version, tool calls and results, outputs, tokens, latency and cost. Without traces, debugging "why did it say that?" is guesswork.

Most AI observability tools (LangSmith, Langfuse, Arize Phoenix, Braintrust, Logfire, Weights & Biases Weave and others) capture traces, and OpenTelemetry has semantic conventions for generative AI so traces can flow into standard observability stacks ([OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)).

**Privacy:** traces contain user data. Apply the same data policies as anywhere else: retention limits, access control, redaction.

## Monitor quality online

- **Explicit feedback:** thumbs up/down, "report a problem".
- **Implicit signals:** edits before sending, regenerations, escalations to humans, abandonment.
- **Sampled review:** a weekly sample of real interactions reviewed by people or calibrated judges.
- **Drift:** watch for changes in input types, topics and quality scores over time.

Feed interesting failures back into the eval set.

## Cost

Cost per task = tokens × price, multiplied by volume and by the number of model calls per task (agents make many).

Levers, roughly in order of ease:
1. **Right-size the model:** small models for simple steps ([M1](/ai-native-teams/m01-foundations/choosing-models/)).
2. **Trim context:** fewer, better retrieved chunks; concise tool outputs.
3. **Prompt caching:** most major providers discount repeated prompt prefixes (system prompts, long documents); structure prompts so the stable part comes first.
4. **Batch APIs** for work that doesn't need an immediate answer, often at a significant discount.
5. **Limit agent steps** and set budgets.
6. **Reasoning effort:** use lower effort settings where quality allows.

## Latency

- **Stream** responses so users see output immediately.
- **Parallelise** independent steps (e.g. retrieval from several sources).
- **Use smaller models** for steps on the critical path.
- **Cache** answers to frequent identical requests where appropriate.

## Team practice

Every AI system in production gets a small **dashboard**: volume, quality signal, cost per task, latency (p50/p95), and error/escalation rate. Review it in the same ritual where you review other service health.
