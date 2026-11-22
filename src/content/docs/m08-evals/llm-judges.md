---
title: Graders and LLM-as-judge
description: Code graders, human review, and using models to grade models, calibrated against people.
sidebar: { order: 3 }
---

## Three kinds of graders

| Grader | Strengths | Weaknesses | Use for |
|---|---|---|---|
| **Code** | Fast, cheap, deterministic | Only for checkable properties | Format, exact values, schema validity, forbidden words, tool calls made |
| **Human** | Best judgment, domain knowledge | Slow, expensive, inconsistent between people | Gold-standard labels, calibration, high-stakes review |
| **LLM-as-judge** | Scales open-ended grading | Can be biased or wrong; needs calibration | Rubric scoring of faithfulness, tone, completeness |

Use code wherever you can, LLM judges where you must, and humans to keep both honest.

## Writing a good judge prompt

- **One criterion per judge.** "Is every claim supported by the sources? Answer PASS or FAIL, then give the unsupported claim if any." Not "rate overall quality 1–10".
- **Binary or small scales** (pass/fail, 1–3) are more reliable than 1–10.
- **Give the judge what it needs:** the input, the sources, the output, the reference answer if any.
- **Ask for reasoning before the verdict**, so you can audit judgments.
- **Use a strong model** for judging, and preferably not the exact same setup that produced the output.

## Calibrate against humans

A judge is only useful if it agrees with your experts.

1. Have 1–2 experts label 50–100 outputs.
2. Run the judge on the same outputs.
3. Measure agreement. Look especially at cases where the judge passes something humans failed.
4. Improve the judge prompt; repeat until agreement is good enough for the stakes.
5. Re-check periodically, and whenever you change the judge model.

## Known judge biases

LLM judges have been shown to favour **longer answers**, answers in **certain positions** (first or second in a comparison), and sometimes **outputs from their own model family**. Mitigate with clear criteria, swapping the order in pairwise comparisons, and human calibration.

## Grading agents

For agents, grade the **outcome** (was the task actually done? check the final state, not the agent's claim) and the **trajectory** (sensible tools, no forbidden actions, approvals requested, within budget). Outcome checks by code ("the ticket is closed and the customer was emailed") are the most trustworthy.
