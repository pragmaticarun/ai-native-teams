---
title: Baselines and fair comparisons
description: How to establish a baseline and compare before and after without fooling yourself.
sidebar: { order: 2 }
---

## Baseline first

You can't show improvement without a starting point. Before changing a workflow:

1. Define the metric precisely ("median days from ticket created to resolved, P2 tickets, excluding waiting-on-customer time").
2. Pull **historical data** for the last 2–3 months if it exists. If not, measure for 2–4 weeks before the change.
3. Note anything unusual in the period (holidays, launches, incidents, reorganisations).

## Ways to compare, weakest to strongest

| Method | How | Watch out for |
|---|---|---|
| **Anecdote** | "It feels faster" | Useful for hypotheses only |
| **Before/after** | Same team, metric before vs after | Other changes happened at the same time |
| **Before/after with a comparison group** | A similar team or workflow that didn't change | Groups may differ |
| **Staggered rollout** | Roll out to groups at different times; compare each group to itself and to not-yet-started groups | Takes longer, much more convincing |
| **Randomised experiment** | Randomly assign tasks or people to with/without AI | Not always practical; the strongest evidence |

## Common traps

- **Novelty effect:** early enthusiasm fades; measure for long enough (often 6–12 weeks).
- **Selection bias:** pilot volunteers are often your strongest people.
- **Moving goalposts:** changing the metric definition mid-way.
- **Quality blind spot:** faster, with more rework a month later. Always pair speed with quality.
- **Measuring the wrong unit:** task-level speed-ups that don't change end-to-end outcomes.

## Qualitative evidence matters

Combine numbers with **structured stories**: short write-ups of specific cases (before, after, what changed, what it enabled). Interview a few users. Qualitative evidence explains *why* the numbers moved, and catches problems numbers miss.
