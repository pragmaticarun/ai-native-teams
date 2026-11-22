---
title: Spec-driven development
description: Writing specifications, plans and tasks that agents can execute, and humans can review.
sidebar: { order: 3 }
---

When agents write most of the code, the **specification becomes the main artefact humans author and review**. Spec-driven development (SDD) makes that explicit: requirements → design/plan → tasks → implementation, with each step reviewed.

## Tools that support it

- **GitHub Spec Kit**: an open-source toolkit and `specify` CLI that sets up a spec → plan → tasks workflow for many coding agents ([github/spec-kit](https://github.com/github/spec-kit)).
- **Kiro**: an AWS agentic IDE whose specs are `requirements.md` → `design.md` → `tasks.md` ([Kiro specs docs](https://kiro.dev/docs/specs/)).
- **Plain Markdown in the repo** works too. The discipline matters more than the tool.

## A good spec

```markdown
# Spec: CSV export for the reports page

## Problem
Admins copy report tables by hand into spreadsheets (14 support tickets last quarter).

## Users and scenarios
- As an admin, I can export the currently filtered report to CSV.
- Exports over 50,000 rows run in the background and arrive by email.

## Acceptance criteria
- [ ] Export respects the current filters and column order.
- [ ] Dates are ISO 8601; numbers have no thousands separators.
- [ ] Users without the "reports.export" permission don't see the button.
- [ ] An export of 49,999 rows completes in under 10 s on staging data.

## Out of scope
- Excel format. Scheduled exports.

## Constraints
- Use the existing jobs queue for background exports. No new dependencies.

## Open questions
- Should exports be audited? (Ask security.)
```

## Why it works

- **Acceptance criteria become tests.** The agent can write tests first, then code to pass them.
- **Out of scope and constraints** stop the agent from over-building.
- **Open questions** surface decisions humans must make, instead of the agent guessing.
- **Reviewing a one-page spec** is faster and more effective than reviewing a 1,000-line diff.

## For product managers

Spec-driven development is a direct opportunity for PMs: clear problems, scenarios and acceptance criteria are what agents need most. A PM who can write a spec an agent can execute is extremely effective in an AI-native team. AI can help draft specs too: give it the customer evidence and ask it to draft scenarios and criteria, then sharpen them.

## Pitfalls

- **Specs as bureaucracy.** Scale the spec to the change: a one-line fix needs a one-line issue.
- **Specs that rot.** Update the spec when decisions change, or delete it after merge. Stale specs mislead future agents.
