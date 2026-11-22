---
title: Memory, long sessions and compaction
description: How assistants and agents remember, and how to keep long work on track.
sidebar: { order: 3 }
---

## Three kinds of "memory"

| Kind | What it is | Examples |
|---|---|---|
| **Working memory** | The current context window | This conversation |
| **Session summaries / compaction** | The tool summarises older parts of a long conversation to free space | Long agent runs and coding sessions in many current tools |
| **Long-term memory** | Facts saved and re-inserted in later sessions | Assistant "memory" features, notes files an agent maintains, a team knowledge base |

All of them end up as **tokens in the context window**. Memory is just context that's been saved and brought back.

## Long conversations drift

Long chats accumulate abandoned ideas, superseded decisions and tangents. Signs of drift: the model reintroduces something you rejected, ignores a constraint from early on, or repeats itself.

**Fixes, in order:**
1. **Restate** the key constraints and current decision.
2. **Summarise and restart.** Ask: "Summarise our decisions, open questions and the current draft in under 300 words." Start a new conversation with that summary.
3. **Externalise state.** For multi-day work, keep a working document (plan, decisions log, progress checklist) and have the AI read and update it, rather than relying on chat history.

## How agents handle long tasks

Agents doing hours of work use the same ideas, automated:

- **Compaction:** summarising history when the window fills, keeping decisions and dropping noise.
- **Note-taking:** writing progress to a file (e.g. a `PROGRESS.md` or task list) and re-reading it.
- **Sub-agents:** delegating a self-contained sub-task to a fresh context and getting back only the result, so the main context stays clean (see [M5](/ai-native-teams/m05-agents/multi-agent-and-hitl/)).
- **Just-in-time retrieval:** searching for files or docs when needed instead of loading everything up front.

## Memory risks

- **Wrong memories persist.** Check and edit what your assistant has saved about you.
- **Privacy.** Memory may store personal or confidential details. Know your tool's settings and your policy ([M10](/ai-native-teams/m10-governance/)).
- **Memory poisoning.** Agents that save memories from untrusted content (web pages, emails) can be manipulated into "remembering" malicious instructions ([M9](/ai-native-teams/m09-safety/)).

## Team practice

For any piece of work that spans more than a day, keep a **shared working doc** (goal, decisions, open questions, next steps) that both humans and AI read. This doubles as a hand-off doc when someone is out.
