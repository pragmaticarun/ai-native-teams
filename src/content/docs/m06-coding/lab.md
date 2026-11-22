---
title: "Lab 6 · Ship a change with a coding agent"
description: Take a real change from spec to merged PR with a coding agent, measuring the before and after of making your repo agent-friendly.
sidebar: { order: 6 }
---

<ul class="lab-meta"><li>⏱ 2 hours</li><li>👥 Pairs (engineer + PM or engineer + engineer)</li><li>🧰 An approved coding agent, a real repository, CI</li></ul>

## Goal

Ship a real, small change using a spec → plan → tests → code → review flow, and improve the repo so the next one is easier.

## Steps

1. **Pick a task** (10 min). A real backlog item you'd estimate at a few hours: a small feature, a bug with a reproduction, a refactor with good test coverage.
2. **Write the spec** (20 min). PM and engineer together, using the [spec template](/ai-native-teams/m06-coding/spec-driven/#a-good-spec). Acceptance criteria must be testable.
3. **Plan with the agent** (15 min). Ask it to read the relevant code and propose a plan. Don't let it edit yet. Correct the plan.
4. **Tests first** (20 min). Agent writes failing tests from the acceptance criteria. You review them.
5. **Implement** (25 min). Agent makes the tests pass and runs the full verify command. Note every time you had to intervene and why.
6. **Review** (15 min). Use the [reviewer's checklist](/ai-native-teams/m06-coding/review-and-testing/#the-reviewers-checklist-for-ai-written-code). Open the PR through your normal process.
7. **Improve the repo** (15 min). For each intervention in step 5, ask: would an `AGENTS.md` line, a script or a skill have prevented it? Add it.

## Deliverable

- A PR (merged or in review).
- An intervention log: *what went wrong → root cause (spec / context / verification / model) → fix*.
- An updated `AGENTS.md` or new skill in the repo.

## Debrief

- What level ([lesson 1](/ai-native-teams/m06-coding/levels/)) did you work at? What would it take to do this task one level higher?
- How long did review take compared with writing the code?
