---
title: Writing an AI use policy
description: What a practical, readable team AI use policy contains, with a template.
sidebar: { order: 3 }
---

A good AI use policy is **short enough to read, specific enough to act on, and encouraging**. Its main job is to let people use AI confidently.

DORA's research lists **a clear and communicated AI stance** as one of the capabilities that amplify AI's benefits ([DORA AI Capabilities Model](https://dora.dev/ai/capabilities-model/report/)). The policy is a large part of that stance.

## What it covers

1. **Purpose and stance.** Why we use AI, and that we *encourage* it within these rules.
2. **Approved tools** and how to request new ones (with a fast path).
3. **Data rules:** which data classes may go into which tools.
4. **Accountability:** you're responsible for what you ship or send, however it was made.
5. **Review requirements** by risk (e.g. customer-facing, legal, code, decisions about people).
6. **Disclosure:** when to tell customers or colleagues AI was used.
7. **Prohibited uses.**
8. **Agents and automations:** who may build them, permission rules, registration ([next lesson](/ai-native-teams/m10-governance/vendors-and-data/)).
9. **Incidents:** what to report and where.
10. **Learning:** expected training, and where to get help.

## Template

```markdown
# Team AI Use Policy (v1.0, owner: <name>, review: every 6 months)

## Our stance
We expect everyone to use AI to do better work. Use it often, check its work,
and share what you learn in #ai-playbook.

## Approved tools
- <Enterprise assistant>: all internal data up to Confidential.
- <Coding agent> in sandboxes: source code; no production secrets.
- Anything else: request in #ai-tools. We aim to answer within 5 working days.

## Data
| Data class | Approved tools | Never |
|---|---|---|
| Public | Any | |
| Internal | Approved tools | Personal accounts |
| Confidential (customer data, financials) | <Enterprise assistant> only | Free/consumer tools |
| Restricted (secrets, health data, ...) | None without a specific approval | Any AI tool |

## You are accountable
You own anything you send, ship or decide, whether or not AI helped.

## Review by risk
- Customer-facing text: human review before sending.
- Code: normal code review; high-risk paths need code owners (see engineering guide).
- Decisions about people (hiring, performance): AI may assist; humans decide;
  no automated rejection or ranking without HR + legal approval.

## Disclosure
Tell customers when they're talking to an AI system. Disclose AI use in research,
legal or financial analysis.

## Never
- Generate realistic images/voices of real people without consent.
- Use AI to monitor or score individual employees.
- Paste secrets into any AI tool (if it happens, rotate and report).

## Agents and automations
Register them in the AI register. Least privilege. Human approval for external or
irreversible actions.

## Incidents
Report data exposure, harmful output or unexpected agent actions in #security
within 1 hour.
```

## Making it real

- **Write it with the team**, not for them.
- **Fast approvals** for new tools, or people will route around you.
- **Explain the why** behind each rule.
- **Review every six months**; tools and law change.
