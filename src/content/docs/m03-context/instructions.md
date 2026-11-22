---
title: Instructions files and project knowledge
description: Custom instructions, projects, AGENTS.md and rules files. Writing them well and keeping them current.
sidebar: { order: 2 }
---

Persistent instructions are the highest-leverage context you control: written once, applied to every conversation or agent run.

## Where persistent instructions live

| Tool type | Mechanism (names vary by product) |
|---|---|
| Chat assistants | Custom instructions, profile preferences, **projects** or **custom assistants** with instructions and knowledge files |
| Coding agents | **`AGENTS.md`**, an open Markdown format read by many coding agents ([agents.md](https://agents.md/)), and tool-specific files such as `CLAUDE.md` or Cursor's `.cursor/rules/` ([Cursor rules docs](https://cursor.com/docs/rules)) |
| Automations and agents you build | The system prompt in your workflow or agent configuration |

AGENTS.md is now stewarded by the Linux Foundation's Agentic AI Foundation, alongside MCP ([announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)).

## What to put in a team instructions file

A good file answers the questions a capable new teammate would ask in week one.

```markdown
# Team instructions: Customer Success, EMEA

## Who we are
We support ~400 mid-market customers of our HR platform. Most contacts are HR managers,
not technical users.

## How we write
- Plain English, short sentences, British spelling.
- Never promise dates for features. Say "we'll update you" and link the public roadmap.
- Sign off as the human sender, never as "the team".

## Facts to rely on
- Product names and tiers: see `product-tiers.md` (source of truth; overrides anything else).
- SLA: P1 response within 1 hour, 24/7. P2 within 4 business hours.

## Things that go wrong
- Customers confuse "Payroll Sync" (integration) with "Payroll" (module). Ask which they mean.
- Don't paste customer personal data into tools that aren't on the approved list.

## When unsure
Say what you don't know and suggest who to ask (#cs-escalations).
```

## Writing rules that work

- **Short and specific beats long and generic.** "Use British spelling" is useful; "write well" is not. Aim for something people will actually read; split by topic if it grows.
- **Explain non-obvious rules.** "No feature dates, *because legal requires roadmap disclaimers*."
- **Link instead of paste** for large reference material, if the tool can open links or files.
- **Point to the source of truth** for facts that change.
- **Don't duplicate what the model already does well.** You don't need "be helpful" or "write clearly".
- **Put commands and checks in, for coding agents.** How to build, test, lint and verify (see [M6](/ai-native-teams/m06-coding/agent-friendly-repos/)).

## Keeping it current

Stale instructions are worse than none: the model will confidently follow last year's process.

- Give the file an **owner** and review it monthly.
- **Every repeated correction is a missing instruction.** If you've told the AI the same thing three times, add it.
- Treat changes like code: small edits, a short reason, reviewed by a teammate.
- **Test after changes:** re-run 3–5 typical tasks and compare.
