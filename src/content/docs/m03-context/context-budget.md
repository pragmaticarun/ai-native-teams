---
title: Context is a budget
description: The layers of context, and why both too little and too much hurt results.
sidebar: { order: 1 }
---

## What goes into the context window

On every turn, the model sees a single block of tokens assembled from several layers:

| Layer | Who controls it | Examples |
|---|---|---|
| **System / developer instructions** | The product or your team | Role, rules, tone, safety constraints |
| **Persistent instructions** | You or your team | Custom instructions, project instructions, `AGENTS.md`, rules files |
| **Knowledge** | You, or retrieval | Attached files, project knowledge, search or RAG results |
| **Tool definitions and results** | The agent setup | Available tools and what they returned |
| **Memory** | The product | Facts saved from earlier conversations |
| **Conversation history** | Everyone | Your messages and the model's replies so far |
| **The current request** | You | The prompt |

Context engineering means **choosing what goes into each layer**, so the model has what it needs for *this* step, and not much else.

## Too little context

The model fills the gaps with plausible guesses: generic advice, invented conventions, made-up facts. Symptoms: "technically right but useless for us", "it doesn't know how we do things".

## Too much context

Bigger context windows don't mean you should fill them.

- **Distraction.** Irrelevant material competes for attention; models can follow the wrong document or an outdated instruction.
- **Context rot.** Quality on details tends to drop as context gets very long. Research on long-context models has shown that information in the middle of long inputs can be used less reliably than information at the start or end ([Liu et al., "Lost in the Middle", 2023](https://arxiv.org/abs/2307.03172)).
- **Cost and speed.** Every token is paid for and processed on every turn (prompt caching reduces this for repeated prefixes).
- **Contradictions.** Old decisions and new decisions in the same context confuse the model, just as they confuse people.

## Principles

1. **Relevant over complete.** Include what this task needs. Link to or retrieve the rest.
2. **Stable on top, specific below.** Put long-lived rules in persistent instructions; put task details in the request.
3. **Fresh beats long.** When a conversation drifts, start a new one with a short summary of decisions so far.
4. **Examples are context.** A good example often beats a page of rules.
5. **Name the source of truth.** If two documents disagree, say which wins.
6. **Write for a smart newcomer.** Context should read like an excellent onboarding doc: terse, specific, current.

## Team practice

When an AI result disappoints, run a **context check** before rewriting the prompt:
- What did it *not* know that a teammate would have known?
- What did it see that was irrelevant, outdated or contradictory?
