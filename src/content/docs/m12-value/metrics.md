---
title: Choosing metrics
description: Outcome, quality, adoption and experience metrics, plus the vanity metrics to avoid.
sidebar: { order: 1 }
---

## Four families of metrics

| Family | Examples | Why |
|---|---|---|
| **Outcomes** | Cycle/lead time for a workflow, customer resolution time, time-to-first-prototype, throughput of *completed* work, revenue or cost per unit | The point of the exercise |
| **Quality** | Error and rework rates, change failure rate, defect escape rate, eval scores, customer satisfaction, escalation rate | Speed without quality is debt |
| **Adoption** | Weekly active users of approved tools, share of workflows redesigned, playbook contributions | Leading indicators, *not* value |
| **Experience** | Developer/employee experience surveys, time spent on toil vs meaningful work, confidence using AI | Sustainability and retention |

For software teams, the **DORA metrics** (deployment frequency, lead time for changes, change failure rate, failed deployment recovery time, and rework rate) remain the standard delivery measures; DORA's research is also where "AI is an amplifier" comes from ([DORA 2025 report](https://dora.dev/research/2025/dora-report/)). Frameworks like **SPACE** (satisfaction, performance, activity, communication, efficiency) remind you to measure more than activity.

## Metrics to avoid as targets

- **Lines of code / words generated.** More output isn't more value, and it's easily inflated.
- **AI suggestion acceptance rate** as a productivity measure. Useful for tuning a tool, misleading as a value metric.
- **Number of AI tools or licences.**
- **Individual usage rankings** ([M11](/ai-native-teams/m11-change/leading-change/#make-it-safe-to-experiment-and-to-fail)).
- **Self-reported time saved, alone.** Useful signal, but people's estimates of their own time savings can be well off. Pair it with measured outcomes.

## Pick few, pick together

For each redesigned workflow, choose **one outcome, one quality and one experience metric**. For the team overall, add a handful of adoption indicators. Agree them with the sponsor *before* the change.

## Watch for the bottleneck moving

When AI speeds up one step, the constraint moves elsewhere (often review, integration, decisions or downstream teams). If a local metric improves but the end-to-end outcome doesn't, look for the new bottleneck rather than declaring success.
