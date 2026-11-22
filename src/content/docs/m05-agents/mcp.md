---
title: "MCP: connecting agents to everything"
description: What the Model Context Protocol is, how it works, and how to adopt it safely.
sidebar: { order: 3 }
---

## The problem MCP solves

Every AI app wants to connect to every tool: drives, wikis, ticketing, CRMs, databases, design tools. Without a standard, that's a custom integration for every pair. The **Model Context Protocol (MCP)** is an open protocol that standardises how AI applications connect to tools and data, so one **MCP server** for a system can be used by any **MCP client** (assistant, IDE, agent). It's often compared to USB-C for AI.

MCP was introduced by Anthropic in November 2024 and has been contributed to the Linux Foundation's **Agentic AI Foundation**, with broad support across AI vendors and tools ([AAIF announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [spec](https://modelcontextprotocol.io/)).

## The parts

| Part | Role |
|---|---|
| **Host / client** | The AI application (desktop assistant, IDE, agent) that connects to servers |
| **Server** | Exposes capabilities from a system: **tools** (actions), **resources** (data to read) and **prompts** (templates) |
| **Transport** | Local (stdio, a process on your machine) or remote (HTTP, usually with OAuth sign-in) |

Most people use MCP without writing any code: they add a server (a "connector" or "integration") in their assistant's settings and sign in.

## Where the spec is (November 2026)

The current specification revision is **`2026-07-28`**. It made the protocol **stateless** (no initialisation handshake or protocol-level sessions; version and capabilities travel with each request), added server discovery, and deprecated some older features ([changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)). In November 2026 the maintainers announced a six-month release cycle, with the next revision targeted for 30 March 2027 ([release cycle post](https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/)). For non-builders the practical point is: **MCP is stable enough to standardise on, and it keeps evolving, so keep clients and servers updated.**

## Choosing and approving MCP servers

An MCP server runs with real access to real systems. Treat adding one like installing software with your credentials.

- **Who publishes it?** Prefer official servers from the system's vendor, or well-maintained open-source servers. Be wary of random packages with similar names.
- **What can it do?** List its tools. Are there write/delete tools? Can you disable them?
- **What credentials does it use?** Prefer OAuth with scoped, per-user access over a shared admin token.
- **Where does it run?** Local servers run code on your machine; remote servers see your data.
- **Is it pinned and reviewed?** For local servers, pin versions; tool descriptions can change between versions.

## MCP-specific risks

- **Tool poisoning:** malicious instructions hidden in tool descriptions or results.
- **Over-broad access:** one connector that can read all email *and* send email is an exfiltration path ([M9](/ai-native-teams/m09-safety/prompt-injection/)).
- **Confused deputy:** a server acting with more privilege than the user who asked.

## Building your own

Teams build MCP servers to expose internal systems (an internal API, a metrics store, a runbook database) to every AI tool at once. Official SDKs exist for TypeScript, Python, and other languages. Design the tools using the principles in [lesson 1](/ai-native-teams/m05-agents/tool-calling/#designing-tools-models-use-well). For an engineering deep dive, see the companion [AI-Native Software Development course](https://pragmaticarun.github.io/ai-native-course/).
