---
title: Levels of AI-assisted engineering
description: A practical ladder from autocomplete to spec-driven agents, and what each level requires.
sidebar: { order: 1 }
---

## A practitioner's ladder

Dan Shapiro's widely discussed "five levels" (January 2026) models AI-assisted coding on the driving-automation levels. It's an opinion piece rather than research, but it's a useful shared vocabulary ([original post](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/), [discussion](https://simonwillison.net/2026/jan/28/the-five-levels/)):

| Level | What it looks like |
|---|---|
| **L0 Manual** | AI as search, occasional tab-complete |
| **L1 Offload discrete tasks** | "Write a unit test for this function" |
| **L2 Pair in flow** | Working with an AI-native tool continuously, as a pair |
| **L3 Manage and review** | You review the agent's diffs; the agent writes most code. Shapiro notes that most people top out here |
| **L4 Specs and skills** | You write specs and skills, review plans, leave, and check that tests pass |
| **L5 "Dark factory"** | A black box that turns specs into software |

## What moves a team up

The levels are about **the human's job**, and each step up needs better infrastructure, not just a better tool. DORA's research identifies seven capabilities that amplify the benefits of AI in software teams ([DORA AI Capabilities Model](https://dora.dev/ai/capabilities-model/report/)):

1. A clear and communicated AI stance
2. Healthy data ecosystems
3. AI-accessible internal data
4. Strong version control practices
5. Working in small batches
6. A user-centric focus
7. Quality internal platforms

In practice, moving from L2 to L3 needs **fast, trustworthy tests and CI** (or you can't review agent output efficiently). Moving from L3 to L4 needs **specs, written conventions and skills** (or the agent can't work unsupervised), plus **review policies** that scale.

## Different work, different levels

A healthy team doesn't run everything at one level:

- **L4** for well-specified, well-tested changes: dependency upgrades, adding endpoints that follow a pattern, test coverage, migrations with good verification.
- **L2–L3** for design-heavy or ambiguous work.
- **L0–L1** for security-critical code paths where you want maximum human understanding, at least until your verification is strong.

## Team practice

Map your last 20 merged changes: what level was each done at? What stopped the ones at L1–L2 from being done at L3–L4? The answers are your engineering improvement backlog.
