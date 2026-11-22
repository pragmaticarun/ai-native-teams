---
title: Multi-agent systems and human-in-the-loop
description: Orchestrator and sub-agent patterns, autonomy levels, and designing human oversight that's real.
sidebar: { order: 4 }
---

## Multi-agent patterns

| Pattern | How it works | Good for |
|---|---|---|
| **Orchestrator + sub-agents** | A lead agent splits work and delegates self-contained sub-tasks to sub-agents with fresh contexts | Broad research, parallel investigation, large code changes |
| **Pipeline / hand-off** | Specialist agents pass work along (intake → research → draft → review) | Structured processes |
| **Generator + critic** | One agent produces, another reviews against criteria | Quality-sensitive outputs |
| **Parallel attempts** | Several agents try independently; pick the best or combine | Hard problems with checkable answers |

Anthropic described its multi-agent research system, where a lead agent coordinates parallel sub-agents, as substantially better on broad research tasks, at the cost of using many more tokens than a single agent ([How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)).

**Rule of thumb:** use multiple agents when work is genuinely **parallel** or benefits from **separate contexts**. Don't build an "org chart of agents" for a task one agent with good tools can do.

## Autonomy is a design choice

One useful framework defines five levels of agent autonomy by **the user's role**: **Operator → Collaborator → Consultant → Approver → Observer** ([Feng, McDonald & Zhang, 2025](https://arxiv.org/abs/2506.12469)). The same agent can run at different levels for different tasks.

| Level (user's role) | What it looks like |
|---|---|
| L1 Operator | User drives; AI helps on request |
| L2 Collaborator | User and AI work together, both taking actions |
| L3 Consultant | AI leads; consults the user for expertise and preferences |
| L4 Approver | AI acts; the user approves at key points or risky actions |
| L5 Observer | AI acts fully; the user monitors and can intervene |

## Designing human-in-the-loop that's real

Human oversight only works if the human can actually catch problems.

- **Put approvals where they matter:** irreversible, external, financial or customer-visible actions. Not on every step.
- **Show what will happen, not just what was decided:** the exact email, the exact diff, the exact records to be changed.
- **Make "no" easy** and make the agent recover gracefully.
- **Watch for rubber-stamping.** If people approve 200 actions a day without reading, you have automation with extra steps, not oversight. Thoughtworks' Technology Radar warns against this kind of "human-in-the-loop theater" ([Radar](https://www.thoughtworks.com/radar)).
- **Sample and audit** low-risk automated actions instead of approving each one.

## Team practice

For each agent or automation, record its **autonomy level, approval points and audit method** in your playbook. Review them when the agent's tools or the stakes change.
