---
title: Why evals
description: Why AI systems need systematic evaluation, and how evals differ from traditional tests.
sidebar: { order: 1 }
---

## AI breaks differently

Traditional software is deterministic: the same input gives the same output, so a test that passes keeps passing. AI systems are:

- **Non-deterministic:** the same input can give different outputs.
- **Sensitive to change:** a reworded prompt, a new model version, a new document in the index, or a new tool can change behaviour in ways nobody predicted.
- **Graded on a spectrum:** answers are better or worse, not just right or wrong.

So you need tests that run **many examples**, score them, and report **rates** ("94% of answers grounded in sources") rather than pass/fail on one case.

## What evals let you do

- **Decide** whether something is good enough to launch, with evidence.
- **Compare** prompts, models and designs fairly.
- **Catch regressions** when anything changes, including the provider updating a model.
- **Make quality a shared, concrete conversation** ("we're at 82% on hard cases; launch threshold is 90%") instead of anecdotes.

## Evals as product requirements

For AI features, the eval set *is* the specification of good behaviour. Product managers should own (with engineering and domain experts) what the eval checks and what threshold is acceptable. This is the AI-native version of acceptance criteria.

## Kinds of evals

| Kind | Question | Example |
|---|---|---|
| **Capability** | Can it do the task at all? | Extracts invoice totals correctly |
| **Regression** | Did a change break something that worked? | Re-run the full set when the prompt changes |
| **Safety / adversarial** | Does it resist misuse? | Prompt-injection attempts, requests for restricted data ([M9](/ai-native-teams/m09-safety/)) |
| **Trajectory (agents)** | Did the agent take sensible steps? | Used the right tools, didn't loop, asked for approval when required |
| **Online** | How does it do with real users? | Thumbs up/down, edit rates, escalation rates |

## How much is enough?

Start small and real: **20–50 examples** you understand deeply beat 5,000 synthetic ones you don't. Grow the set every time you find a failure in the wild.
