---
title: Agent-friendly repositories
description: Instructions files, one-command verification, conventions and structure that make agents effective.
sidebar: { order: 4 }
---

An agent-friendly repository is also a **human-friendly** one: a newcomer (human or AI) can find out how to build, test and change it in minutes.

## The checklist

1. **An `AGENTS.md` at the root** (and nested ones for sub-projects) with: what the project is, how to set up, how to verify, conventions, and things not to do ([agents.md](https://agents.md/)).
2. **One command to verify everything**, such as `make check`, `./verify.sh` or `npm test`, that runs lint, type-check and tests, and is fast enough to run often.
3. **Fast, deterministic tests.** Flaky tests teach agents (and people) to ignore failures.
4. **Consistent conventions** that are written down or enforced by linters and formatters, rather than tribal.
5. **Clear structure and naming** so search finds the right place.
6. **Skills for recurring procedures**: release, migration, adding an endpoint ([M3](/ai-native-teams/m03-context/skills/)).
7. **CI that runs on agent PRs** exactly as on human PRs.
8. **A PR template** that asks for what reviewers need: what changed, why, how it was verified, risks.

## Example `AGENTS.md`

```markdown
# Billing service

Handles invoices and payment webhooks. Python 3.13, FastAPI, Postgres.

## Setup and verify
- Setup: `make setup`
- Verify (run before every commit): `make check` (ruff, mypy, pytest; ~40 s)

## Conventions
- Money is always `Decimal` in minor units. Never float.
- New endpoints: copy the pattern in `app/routes/invoices.py`, add tests in `tests/routes/`.
- Database changes need an Alembic migration and a rollback.

## Don't
- Don't edit `app/generated/`. It's generated from the OpenAPI spec (`make gen`).
- Don't call payment providers in tests. Use `tests/fakes/`.

## Ask a human before
- Changing anything in `app/payments/` (PCI scope).
```

## Measure it

Give an agent 5 realistic tasks before and after improving the repo. Track: did it succeed, how many attempts, how much rework did review need. This is the most convincing argument for investing in developer experience.
