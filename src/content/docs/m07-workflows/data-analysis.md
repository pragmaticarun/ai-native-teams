---
title: Data analysis with AI
description: Getting trustworthy answers from data with code execution, semantic layers and verification.
sidebar: { order: 4 }
---

## The golden rule

**Let the model write and run code, not do maths in its head.** Use tools with code execution (data-analysis features in assistants, notebooks with AI, coding agents) so every number comes from a computation you can inspect.

## A trustworthy workflow

1. **Describe the data:** what each column means, units, known quirks ("refunds are negative amounts", "region was renamed in March").
2. **State the question precisely:** "weekly active users by plan, last 12 weeks, excluding internal accounts".
3. **Ask for the plan first:** which tables, filters and joins.
4. **Run and inspect:** look at the code or SQL, row counts, and a few raw rows.
5. **Sanity-check:** does the total match a known figure (a dashboard, finance's number)?
6. **Then interpret:** ask for explanations *and* alternative explanations.

## Text-to-SQL and semantic layers

Natural-language querying works best on top of a **semantic layer or curated views** with defined metrics ("active user", "revenue"), so the model doesn't invent its own definitions. Give it **read-only** access to approved datasets.

## Common traps

- **Plausible but wrong joins** that double-count.
- **Silent filters**: the model drops nulls or outliers without saying so.
- **Invented definitions** of business metrics.
- **Charts that look right** with mislabelled axes or units.
- **Confusing correlation and causation** in "insights".

## Team practice

For any AI-assisted analysis that informs a decision, keep the **code/SQL with the result**, and have someone who knows the data review it. Same standard as a human analyst's work.
