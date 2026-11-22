---
title: "Lab 8 · Build an eval set for a real AI use"
description: Turn one of your AI uses into a measured system with an eval set, graders and a threshold.
sidebar: { order: 5 }
---

<ul class="lab-meta"><li>⏱ 2 hours</li><li>👥 Groups of 3–4 (include a domain expert)</li><li>🧰 A spreadsheet; optionally an eval tool such as promptfoo or Inspect</li></ul>

## Goal

Produce an eval set, graders and a launch threshold for one real AI use (a prompt-library entry, the Lab 4 knowledge assistant, or the Lab 7 automation).

## Steps

1. **Pick the system and define "good"** (15 min). Write 3–5 criteria. For each: code-checkable, rubric, or must-include?
2. **Build the set** (35 min). 30 examples: ~20 typical, ~5 hard, ~3 should-abstain, ~2 adversarial. Reuse the Lab 1/4 test cases. Record the reason each example was added.
3. **Human baseline** (20 min). Run the system on all 30. Two people grade independently against the criteria. Compare and resolve disagreements; sharpen any criterion people disagreed on.
4. **Build an LLM judge** (25 min) for your hardest open-ended criterion using the [judge guidelines](/ai-native-teams/m08-evals/llm-judges/#writing-a-good-judge-prompt). Run it on the same 30. Compute agreement with the human labels.
5. **Make a change and re-run** (15 min). Change one thing (prompt, model or context). Re-run everything. Better or worse, and on which slices?
6. **Set the threshold** (10 min). What score per criterion is good enough to use this for real, given the stakes?

## Deliverable

The eval sheet (examples, criteria, human labels, judge labels, before/after scores), judge-human agreement, and the agreed threshold. Schedule when it will be re-run.

## Stretch: automate it

Put the set into an eval tool so it runs with one command or on a schedule. promptfoo ([docs](https://www.promptfoo.dev/docs/intro/)) uses a YAML config of prompts, providers and assertions; Inspect ([docs](https://inspect.aisi.org.uk/)) is a Python framework from the UK AI Security Institute.
