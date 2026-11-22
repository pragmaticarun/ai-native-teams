---
title: Tools landscape (November 2026)
description: A dated, vendor-neutral map of AI tools by category, with versions checked in November 2026.
sidebar: { order: 1 }
---

AI tools change monthly. This page lists **representative** tools by category so you can find them; inclusion isn't an endorsement and the lists aren't exhaustive. Always use what your organisation has approved.

**Last reviewed: 22 November 2026.** Versions marked with a date were checked against their package registries or GitHub releases on that date.

## Assistants and models

| Category | Examples |
|---|---|
| General assistants (business tiers) | ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Microsoft 365 Copilot, Mistral Le Chat, Perplexity |
| Model families via API | OpenAI GPT and reasoning models, Anthropic Claude (Opus, Sonnet, Haiku tiers), Google Gemini (Pro, Flash tiers), Mistral, Cohere, xAI Grok |
| Open-weight models | Llama (Meta), Gemma (Google), Mistral and Qwen families, DeepSeek, and others; run via cloud platforms or tools such as llama.cpp, Ollama, vLLM |
| Cloud model platforms | Amazon Bedrock, Google Vertex AI, Microsoft Azure AI Foundry |

## Coding agents

CLI versions from npm, 13 November 2026:

| Tool | Notes |
|---|---|
| Claude Code (`@anthropic-ai/claude-code` 2.1.323) | Terminal, IDE and web; skills, MCP, hooks ([docs](https://docs.claude.com/en/docs/claude-code/overview)) |
| OpenAI Codex CLI (`@openai/codex` 0.169.0) and Codex cloud | ([Codex cloud](https://developers.openai.com/codex/cloud)) |
| GitHub Copilot (IDE, CLI `@github/copilot` 1.0.111, coding agent) | Assign an issue, get a PR ([coding agent docs](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)) |
| Gemini CLI (`@google/gemini-cli` 0.68.0) | |
| Cursor | IDE agent, background agents; reads `AGENTS.md` and `.cursor/rules` ([rules docs](https://cursor.com/docs/rules)) |
| Others | Windsurf, Devin, Kiro (spec-driven IDE, [docs](https://kiro.dev/docs/specs/)), JetBrains AI, Amazon Q Developer |

Spec-driven development: **GitHub Spec Kit** v1.4.0 (10 Nov 2026), [github/spec-kit](https://github.com/github/spec-kit).

## Agent frameworks and SDKs

Versions from PyPI/npm, 13–17 November 2026:

| Framework | Python | TypeScript |
|---|---|---|
| LangGraph | `langgraph` 1.2.22 | `@langchain/langgraph` 1.7.4 |
| OpenAI Agents SDK | `openai-agents` 0.24.0 | `@openai/agents` 0.22.0 |
| Claude Agent SDK | `claude-agent-sdk` 0.2.182 | `@anthropic-ai/claude-agent-sdk` 0.3.325 |
| Pydantic AI | `pydantic-ai` 2.68.0 | |
| Vercel AI SDK | | `ai` 7.0.173 |
| Mastra | | `@mastra/core` 1.83.0 |

Durable execution for long-running agents: Temporal, DBOS, Restate, Inngest.

## MCP

- Spec revision **2026-07-28** ([changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)); next targeted for 30 March 2027.
- Official SDKs: Python `mcp` 2.3.0; TypeScript `@modelcontextprotocol/server` and `@modelcontextprotocol/client` 2.4.0; plus other languages.
- Debugging: MCP Inspector.
- Many vendors publish official MCP servers for their products. Check the publisher before installing ([M5](/ai-native-teams/m05-agents/mcp/#choosing-and-approving-mcp-servers)).

## Knowledge, RAG and search

| Category | Examples |
|---|---|
| Vector search | pgvector (Postgres), Pinecone, Weaviate, Qdrant, Milvus, Elasticsearch/OpenSearch, and vector features in cloud databases |
| Rerankers & embeddings | Embedding and reranking models from Cohere, Voyage AI, OpenAI, Google, Jina and open-weight options |
| Document parsing | Unstructured, LlamaParse, Docling, and multimodal models reading page images |
| Frameworks | LlamaIndex, LangChain, Haystack |
| Workplace search / enterprise assistants | Built-in connectors in enterprise assistants and workplace search products |

## Evals and observability

Versions from PyPI/npm, 13–17 November 2026: `inspect-ai` 0.3.290 ([Inspect](https://inspect.aisi.org.uk/)), `promptfoo` 0.125.1 ([docs](https://www.promptfoo.dev/docs/intro/)), `deepeval` 4.3.4, `ragas` 0.4.3, `braintrust` 0.50.0, `langsmith` 0.14.17, `arize-phoenix` 21.0.0, `logfire` 5.6.0. Also Langfuse and Weights & Biases Weave. OpenTelemetry [GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).

## Automation and agent builders

Zapier, Make, n8n, Microsoft Power Automate and Copilot Studio, plus agent builders and workflow features from AI vendors and many SaaS platforms.

## Security and governance

OWASP GenAI Security Project ([genai.owasp.org](https://genai.owasp.org/)), MITRE ATLAS, NIST AI RMF and AI 600-1, ISO/IEC 42001; guardrail tools and AI security platforms from many vendors and open-source projects.

## Sources

Versions for frameworks, coding agents, MCP SDKs and eval tools come from the verified tooling snapshot in the companion course's [syllabus](https://github.com/pragmaticarun/ai-native-course/blob/main/SYLLABUS.md) (checked 13 Nov 2026, pins re-checked 17 Nov 2026).
