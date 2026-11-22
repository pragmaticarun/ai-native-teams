---
title: Anatomy of a good prompt
description: The five parts of a clear brief, with before-and-after examples.
sidebar: { order: 1 }
---

## The five parts

| Part | Question it answers | Example |
|---|---|---|
| **Situation / role** | Who is this for, and what's going on? | "I'm a PM at a B2B payroll company preparing for a customer advisory board." |
| **Task** | What exactly should be produced? | "Draft a 1-page pre-read summarising Q3 feature launches." |
| **Context** | What does it need to know? | Release notes, customer feedback themes, the audience's concerns (pasted or attached) |
| **Constraints** | What must or mustn't happen? | "Plain language, no roadmap promises, under 400 words, flag anything uncertain." |
| **Output format** | What shape should the answer take? | "Headline, 3 sections with bullets, a 'questions for the board' list." |

You won't always need all five, but **missing context** and **missing output format** cause most disappointing results.

## Before and after

**Before**
```text
Write an email to a customer about the outage.
```

**After**
```text
I'm a support lead at a SaaS analytics company. Yesterday from 14:05 to 15:20 UTC,
dashboards failed to load for about 30% of EU customers because of a database
failover problem. Data was not lost. We've added monitoring and will publish a
post-incident review by Friday.

Draft an email to affected enterprise customers.
- Tone: accountable, calm, specific. No marketing language. No blaming vendors.
- Include: what happened, impact, what we've done, what's next, how to reach us.
- Under 200 words. Subject line plus body.
- If anything above seems missing for a customer to understand the impact, list it
  after the draft under "Gaps".
```

The second prompt is longer, but it takes one round instead of five, and it surfaces gaps instead of inventing details.

## Principles that matter more than wording

- **Be explicit about what "good" means.** The model can't read your mind about length, tone, audience or depth.
- **Give the "why".** "Keep it short *because it's read on mobile between meetings*" lets the model make better judgment calls than "keep it short".
- **Show, don't just tell.** One example of the output you want is often worth a paragraph of description.
- **Say what to do, not only what to avoid.** "Write in plain sentences" works better than a long list of "don't"s.
- **Allow uncertainty.** "If you're not sure, say so and explain what you'd need" reduces made-up answers.
- **Separate instructions from data.** Put pasted material in clearly marked blocks (e.g. between `<document>` tags or under a heading) so the model doesn't confuse your instructions with the content.

## Prompting modern models

Current models follow instructions closely, more literally than earlier ones. Practical consequences:

- If you want it to *do* something (edit the file, make the change), say so; "can you suggest…" may get suggestions only.
- Ask for the level of effort and thoroughness you want ("be comprehensive", "include edge cases").
- Avoid shouting (ALL CAPS, "CRITICAL!!!"). It can make models over-apply a rule. Calm, clear explanation works better.

## Team practice

Adopt a short **prompt template** in your playbook for common work (see [templates](/ai-native-teams/reference/templates/)). The goal is a shared habit, not bureaucracy.
