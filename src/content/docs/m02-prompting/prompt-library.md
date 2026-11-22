---
title: Iterating and building a prompt library
description: A methodical loop for improving prompts, and how to share and maintain them as a team.
sidebar: { order: 4 }
---

## The iteration loop

1. **Start with a clear brief** (lesson 1).
2. **Run it on 3–5 varied, real inputs**, including an awkward one.
3. **Look at failures specifically.** Is it missing context? Misreading the task? Wrong format? Inventing facts?
4. **Change one thing** and re-run the same inputs.
5. **Stop when it's good enough** for the stakes. Perfection is rarely worth it.

Keep the inputs you tested with. They become your test set when you or a model update the prompt.

## When the prompt isn't the problem

If you've iterated three or four times without improvement, the issue is usually upstream:

- **Missing context** → give documents, examples, or retrieval ([M3](/ai-native-teams/m03-context/), [M4](/ai-native-teams/m04-rag/)).
- **Task too big** → decompose into steps or a workflow ([M7](/ai-native-teams/m07-workflows/)).
- **Needs facts or actions** → give it tools ([M5](/ai-native-teams/m05-agents/)).
- **Wrong model** → try a reasoning model or a different provider ([M1](/ai-native-teams/m01-foundations/choosing-models/)).

## A team prompt library

A prompt library is a shared, curated set of prompts for recurring work. It is the first artefact of shared AI practice.

**Each entry has:**

| Field | Example |
|---|---|
| Name | Customer incident email |
| Purpose & when to use | First draft of outage comms for enterprise customers |
| The prompt | With `[PLACEHOLDERS]` for what changes each time |
| Inputs needed | Timeline, impact, remediation, next update time |
| Recommended model/tool | Default assistant; no customer PII beyond names |
| Example output | A good past result |
| Known failure modes | Tends to over-apologise; check times and time zones |
| Owner & last tested | Priya, 2026-11-03 |

**Where to keep it:** wherever your team already works, such as a wiki page, a repo folder, or your AI tool's shared features (many enterprise assistants support shared projects, custom assistants or saved prompts). Tools change; the *content* is the asset.

**Keep it alive:**
- Every entry has an **owner** and a **last tested** date.
- Review quarterly; delete what nobody uses.
- When a prompt becomes heavily used and stable, promote it to a **custom assistant, skill or automation** ([M3](/ai-native-teams/m03-context/skills/), [M7](/ai-native-teams/m07-workflows/)).
