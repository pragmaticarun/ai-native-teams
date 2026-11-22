---
title: Threat modelling AI systems
description: The OWASP Top 10 for LLM applications, the agentic risks, and a simple threat-modelling routine.
sidebar: { order: 1 }
---

## OWASP Top 10 for LLM Applications (2026)

The OWASP GenAI Security Project's list is the most widely used shared vocabulary for LLM risks. The 2026 edition, released in August 2026, ranks ([OWASP GenAI](https://genai.owasp.org/), as summarised by [Invicti](https://www.invicti.com/blog/web-security/owasp-llm-top-10-2026-whats-new) and [Help Net Security](https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/)):

| ID | Risk | In plain words |
|---|---|---|
| LLM01 | **Prompt Injection** | Input or content the model reads hijacks its instructions |
| LLM02 | **Sensitive Information Disclosure** | The system reveals personal, confidential or secret data |
| LLM03 | **Excessive Agency** | The AI has more tools, permissions or autonomy than it needs |
| LLM04 | **Supply Chain** | Compromised models, packages, plugins, MCP servers or datasets |
| LLM05 | **Data and Model Poisoning** | Training, fine-tuning or retrieval data is manipulated |
| LLM06 | **Unbounded Consumption** | Runaway cost or resource use, including denial-of-wallet |
| LLM07 | **Misinformation** | Confident, wrong output that people rely on |
| LLM08 | **Hidden Context Exposure** | System prompts or hidden context leak (renamed from 2025's "System Prompt Leakage") |
| LLM09 | **Vector and Embedding Weaknesses** | Attacks on or leaks through RAG indexes |
| LLM10 | **Improper Output Handling** | Model output passed unchecked into code, queries, HTML or other systems |

The headline theme reported for the 2026 edition is that **the model will be fooled**: design systems that stay safe when it is. OWASP also publishes a separate **Top 10 for Agentic Applications** (first published December 2025) covering risks specific to autonomous agents ([OWASP agentic top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)). Read it before deploying agents with write access.

## A 30-minute threat-modelling routine

For any AI system, answer these questions as a team:

1. **What can it read?** (data sources, documents, the web, email, tickets)
2. **Who controls that content?** Anything written by outsiders (customers, websites, emails, shared docs) is **untrusted**.
3. **What can it do?** List every tool and action, and mark which are irreversible or external.
4. **What can it send out, and where?** Messages, web requests, files, images, links.
5. **Who uses it, with whose permissions?**
6. **What's the worst realistic outcome?** Data leak, wrong action, cost blow-up, reputational harm.
7. **What stops it?** For each worst case, name the control that is *not* "the model will behave".

## The design principle

**Assume the model can be manipulated and will sometimes be wrong.** Put security in the system around it (permissions, validation, isolation, approvals, monitoring), not in the prompt.
