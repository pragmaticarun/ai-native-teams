---
title: The agent loop, and when you need one
description: How agents work, the spectrum from prompt to workflow to agent, and common failure modes.
sidebar: { order: 2 }
---

## The loop

```text
goal → [ model decides next step → call tool → observe result ] → repeat → done (or ask a human)
```

An agent is that loop plus: a goal, a set of tools, a context that accumulates results, and a **stopping rule** (goal reached, budget spent, or human needed). An agent loop is like an event loop whose scheduler is a language model.

## Prompt, workflow or agent?

| | Single prompt | Workflow (fixed steps) | Agent (model decides steps) |
|---|---|---|---|
| Example | Summarise this document | Every new ticket: classify → route → draft reply | "Investigate why signups dropped last week" |
| Predictability | High | High | Lower |
| Handles the unexpected | No | Only designed paths | Yes |
| Cost / latency | Low | Low–medium | Higher, variable |
| Testing | Easy | Moderate | Harder |

Anthropic's guide to building effective agents makes the same point: start with the simplest thing that works, and add agentic autonomy only when the task needs flexible, model-driven steps ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)). **Most business automation should be workflows with AI steps, not open-ended agents.** Agents shine where the path can't be known in advance: research, debugging, coding, investigation.

## Where you meet agents today

- **Coding agents** in the IDE, terminal or cloud ([M6](/ai-native-teams/m06-coding/)).
- **Research agents** ("deep research" modes) that search, read and write reports.
- **Assistant agents** in office suites and enterprise assistants that act across email, documents and calendars.
- **Custom agents** built with agent frameworks or SDKs (see the [tools landscape](/ai-native-teams/reference/tools-landscape/)).

## How agents fail

| Failure | Mitigation |
|---|---|
| Loops or wanders off-task | Step and cost budgets; clear stopping rule; progress notes |
| Declares success too early | Make it verify (run the tests, re-read the requirement); check results yourself |
| Picks the wrong tool | Better tool descriptions; fewer tools |
| Takes a harmful action | Least privilege; approvals for writes; sandboxing ([M9](/ai-native-teams/m09-safety/agent-permissions/)) |
| Gets hijacked by content it reads | Treat tool results as untrusted; limit data + action combinations ([M9](/ai-native-teams/m09-safety/prompt-injection/)) |
| Context fills with noise | Concise tool outputs; compaction; sub-agents ([M3](/ai-native-teams/m03-context/memory/)) |

## Team practice

Before building or enabling an agent, write a one-paragraph **agent brief**: goal, tools and their permissions, budget, stopping rule, what needs human approval, and how you'll know it worked.
