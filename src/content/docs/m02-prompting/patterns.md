---
title: Core prompt patterns
description: Few-shot examples, decomposition, interview-me, critique-and-revise, role prompts and more.
sidebar: { order: 2 }
---

These patterns work across models and tools. Learn them as moves you can combine.

## 1. Few-shot examples

Show 1–5 examples of input → desired output. Best for consistent format, tone or classification.

```text
Classify each feedback item as BUG, FEATURE_REQUEST, PRAISE or OTHER.

"Export to CSV crashes on large files" → BUG
"Would love dark mode" → FEATURE_REQUEST
"Your support team was great today" → PRAISE

Now classify:
"Can't log in since the update"
"Please add SSO for Okta"
```

Tip: vary your examples so the model learns the *pattern*, not surface details. Include a tricky edge case.

## 2. Interview me first

When you're not sure what you need, let the model ask.

```text
I need to write a hiring plan for two data engineers. Before drafting anything,
ask me up to 8 questions that would most change the plan. Ask them all at once.
```

## 3. Decompose the task

Break big jobs into steps, either in one prompt or as a sequence of prompts (a "chain").

```text
Step 1: List the main claims in this report.
Step 2: For each claim, quote the sentence in the data appendix that supports it,
or write "NOT SUPPORTED".
Step 3: Summarise which claims are weakly supported.
```

Chaining across separate prompts gives you a chance to check each step, and is the seed of a workflow ([M7](/ai-native-teams/m07-workflows/)).

## 4. Critique, then revise

Ask for a critique against explicit criteria, then a revision. Fight sycophancy by asking for problems specifically.

```text
Review this proposal as a sceptical CFO. List the 5 weakest points, most serious
first, with a one-line fix for each. Don't comment on strengths.
```

Better still, do the critique in a **fresh conversation** or with a different model, so it doesn't defend its own draft.

## 5. Perspectives and roles

"Act as a security reviewer", "explain this to a new hire", "respond as our most demanding customer". Roles focus the model's attention. They don't add knowledge it doesn't have.

## 6. Generate options, then choose

```text
Give me 5 genuinely different approaches to reducing onboarding time, from cheap
to ambitious. For each: one-line idea, effort (S/M/L), main risk. Then recommend one
and say why.
```

## 7. Ground in sources

```text
Answer using only the attached documents. After each claim, cite the document and
section in brackets. If the documents don't answer the question, say so.
```

## 8. Reverse prompting

Paste a great example of finished work and ask: "Write the prompt that would produce this." Useful for building library entries.

## 9. Meta-prompting

Ask the model to improve your prompt: "Here's a prompt I use for X. It sometimes produces Y. Rewrite it to fix that, and explain your changes." Then **test** the new version; don't assume it's better.

## Anti-patterns

- **Kitchen-sink prompts:** pages of rules accumulated over months that contradict each other. Prune.
- **Magic words:** "you are a world-class expert" adds little on modern models. Specific context adds a lot.
- **One-shot trust:** evaluating a prompt on one run. Outputs vary; test several times.
