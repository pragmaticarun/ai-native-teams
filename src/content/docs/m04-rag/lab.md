---
title: "Lab 4 · A knowledge assistant over your docs"
description: Build and evaluate a grounded Q&A assistant, with a no-code track and a code track.
sidebar: { order: 5 }
---

<ul class="lab-meta"><li>⏱ 2 hours</li><li>👥 Teams of 3–4</li><li>🧰 No-code: an approved assistant with project files or connectors · Code: Python 3.10+</li></ul>

## Goal

Build a knowledge assistant over 10–30 of your team's documents, measure it on real questions, and decide whether it's good enough to use.

## Part A · Prepare (20 min)

1. Choose a **non-confidential** document set your team asks about often: onboarding docs, runbooks, product FAQs, policies.
2. Write **20 test questions** with expected answers and source documents. Include 3 that the docs *can't* answer.

## Part B · Build (40 min)

**No-code track.** Create a project or custom assistant in your approved tool, upload the documents (or connect the source), and add instructions: *answer only from the documents, cite the document name, say "I don't know" if not covered.*

**Code track.** Clone the course repo and try the retrieval demo:

```bash
git clone https://github.com/pragmaticarun/ai-native-teams
cd ai-native-teams/labs/m04
python3 mini_rag.py docs "How many weeks of parental leave?"
```

Point it at a folder of your own Markdown files, look at which chunks it retrieves, then paste the printed prompt into your approved model. Stretch: replace BM25 with hybrid search using an embedding model your organisation approves.

## Part C · Evaluate (40 min)

Run all 20 questions. For each, record:

| # | Right source retrieved/cited? | Answer correct? | Faithful (no unsupported claims)? | Abstained correctly? |
|---|---|---|---|---|

Then classify each failure using the [diagnosis table](/ai-native-teams/m04-rag/evaluating/#diagnose-by-stage).

## Part D · Decide (20 min)

- What's the accuracy? Is it good enough for **this** use, given the stakes?
- Which failures came from **the documents themselves** (missing, outdated, contradictory)?
- What would you change first?

## Deliverable

Your 20-question test set (keep it, it's an eval set for M8), your score table, and a one-paragraph go/no-go recommendation.
