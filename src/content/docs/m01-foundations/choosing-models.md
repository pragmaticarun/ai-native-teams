---
title: Choosing a model
description: A practical decision process using quality, cost, latency, context, and data constraints.
sidebar: { order: 4 }
---

Benchmarks and leaderboards tell you how a model does on *someone else's* tasks. What matters is how it does on **yours**.

## The five questions

1. **Quality: does it do *this* task well enough?** Test on 10–30 real examples from your work, not on demos.
2. **Cost: what does a task cost at your volume?** Cost per task = (input tokens × input price) + (output tokens × output price). Reasoning models also bill their thinking tokens as output.
3. **Latency: how fast must it be?** A chat assistant, a background batch job and a voice agent have very different needs.
4. **Context and modality: what goes in?** Long documents, images, audio, code repositories?
5. **Data and compliance: where can this data go?** Check your data classification and the provider's terms (training use, retention, region). This can rule models out before quality matters ([M10](/ai-native-teams/m10-governance/vendors-and-data/)).

## A simple routing pattern

Many AI-native teams use **more than one model**:

- A **capable default** for interactive work.
- A **reasoning / frontier tier** for hard problems, used deliberately.
- A **small, fast tier** for high-volume classification, extraction and routing.
- An **approved private option** (enterprise tenant, private deployment or open-weight model) for sensitive data.

## Comparing fairly

- Use the **same prompt and the same inputs** for each model.
- Run each input **at least 2–3 times**; look at variance, not just the best answer.
- **Blind the comparison** if you can: label outputs A/B/C so reviewers don't know which model wrote what.
- Score against a **rubric** you agreed beforehand (accuracy, completeness, format, tone).
- Record cost and time alongside quality.

## Don't over-index on today's ranking

Model rankings change every few months. Build the habit (and an eval set, [M8](/ai-native-teams/m08-evals/)) so switching models is a quick, evidence-based decision rather than a big debate.

## Team practice

Record your choice and the evidence in your playbook as a short decision record: *task, models tried, scores, cost, decision, review date.*
