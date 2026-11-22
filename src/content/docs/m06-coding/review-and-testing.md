---
title: Testing, review and security with agents
description: Tests-first with agents, risk-based review policies, and guardrails for agents that run code.
sidebar: { order: 5 }
---

## Tests first, with agents

Test-driven development works especially well with agents:

1. Agree on the behaviour (from the spec's acceptance criteria).
2. Ask the agent to **write the tests first** and confirm they fail.
3. Review the tests (they're the contract; this is where your attention matters).
4. Ask the agent to make them pass **without changing the tests**.
5. Run the full suite.

Watch for agents "solving" failing tests by weakening or deleting them, or special-casing test inputs. Review policy should flag any change to existing tests.

## Risk-based review

Review effort should match risk, not lines of code.

| Risk tier | Examples | Review |
|---|---|---|
| Low | Docs, tests, internal tools, copy | AI review + one quick human look, or auto-merge with green CI if your policy allows |
| Medium | Typical product changes | AI first pass + one human reviewer who reads the spec and the diff |
| High | Auth, payments, data deletion, infrastructure, security-sensitive code | Two humans, including a code owner; extra testing; staged rollout |

Use `CODEOWNERS` (or equivalent) to route high-risk paths automatically.

## The reviewer's checklist for AI-written code

- Does it do what the **spec** says, and nothing extra?
- Are there **tests** for the acceptance criteria? Were any existing tests weakened?
- Any **invented APIs, packages or config**? (Check that new dependencies exist and are the real package, not a look-alike.)
- **Security:** input validation, authz checks, secrets, injection, logging of sensitive data.
- **Duplication:** agents often re-implement something that already exists in the codebase.
- Would you be able to **maintain** this code?

## Guardrails for agents that run code

Coding agents execute commands. Configure them so mistakes are contained:

- **Sandboxing:** run agents in containers, VMs or cloud sandboxes, not on machines with production credentials. Thoughtworks' Technology Radar (Vol. 35, Nov 2026) places agent sandboxing in its Adopt ring ([agent sandboxing](https://www.thoughtworks.com/en-us/radar/techniques/agent-sandboxing)).
- **Permission modes:** allow safe commands (tests, lint, read) automatically; require approval for network access, installs, deletes, pushes and deploys.
- **No production secrets** in the agent's environment. Use scoped, short-lived tokens.
- **Branch protection:** agents open PRs; they don't push to main.
- **Audit logs** of what agents ran.

See [M9 · Agent permissions](/ai-native-teams/m09-safety/agent-permissions/) for the general model.
