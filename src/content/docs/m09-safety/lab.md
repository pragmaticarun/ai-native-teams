---
title: "Lab 9 · Red-team your own assistant"
description: Attack an assistant or automation your team built, find weaknesses, and fix the design.
sidebar: { order: 5 }
---

<ul class="lab-meta"><li>⏱ 90–120 min</li><li>👥 Two groups: builders and attackers, then swap</li><li>🧰 An assistant or automation from Labs 4, 5 or 7, in a test environment</li></ul>

:::caution[Stay in bounds]
Only test systems your team owns, in a test or sandbox environment, with test data. Tell your security team you're running the exercise.
:::

## Goal

Find realistic ways your own AI system can be misused, and fix the **design**, not just the prompt.

## Steps

1. **Threat model** (20 min). Builders walk attackers through the system using the [30-minute routine](/ai-native-teams/m09-safety/threat-model/#a-30-minute-threat-modelling-routine). Mark which legs of the [lethal trifecta](/ai-native-teams/m09-safety/prompt-injection/#the-lethal-trifecta) are present.
2. **Attack** (40 min). Attackers try, and record every attempt:
   - **Direct injection:** get it to ignore instructions or reveal hidden context.
   - **Indirect injection:** plant instructions in a document, ticket or page it will read.
   - **Data extraction:** get it to reveal data the user shouldn't see.
   - **Excessive agency:** get it to take an action it shouldn't.
   - **Misinformation:** get it to state something false with confidence.
   - **Unbounded consumption:** make it loop or produce enormous output.
3. **Score** (15 min). For each successful attack: severity (low/medium/high) and which OWASP category.
4. **Fix the design** (25 min). For each high/medium finding, choose a *system* control: remove a tool, narrow a scope, add an approval, isolate untrusted processing, validate output. Re-test.
5. **Add to evals** (10 min). Every successful attack becomes an adversarial case in your [eval set](/ai-native-teams/m08-evals/building-evals/).

## Deliverable

A findings table (attack, result, severity, OWASP category, fix, re-test result) and updated eval cases.
