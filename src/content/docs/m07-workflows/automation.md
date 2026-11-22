---
title: Automation platforms and building blocks
description: No-code and low-code tools for AI workflows, the common building blocks, and how to put checkpoints in them.
sidebar: { order: 5 }
---

## Options

| Option | Examples | Good for |
|---|---|---|
| **Assistant-native features** | Custom assistants/GPTs, projects, scheduled tasks, connectors, and agent features in enterprise assistants and office suites | Personal and team workflows inside one tool |
| **No-code automation platforms** | Zapier, Make, n8n, Microsoft Power Automate, and workflow builders in many SaaS tools | Connecting SaaS apps with AI steps; event-driven workflows |
| **Agent builders** | Visual agent builders from AI vendors and automation platforms | Agents with tools, without code |
| **Code** | Agent SDKs and frameworks ([tools landscape](/ai-native-teams/reference/tools-landscape/)) | Custom logic, scale, testing, integration with your product |

Use whatever your organisation has approved. Check data handling for every connector ([M10](/ai-native-teams/m10-governance/vendors-and-data/)).

## The building blocks

Almost every AI workflow is assembled from the same blocks:

1. **Trigger:** a new email, ticket, form, file, schedule or webhook.
2. **Gather context:** fetch the record, related history, knowledge articles.
3. **AI step:** classify, extract (structured output), summarise, draft, decide among options.
4. **Validate:** schema checks, rules ("amount under 500", "category in list"), confidence thresholds.
5. **Route:** auto-complete, send to a human for approval, or escalate.
6. **Act:** update a system, send a message, create a task.
7. **Log:** record inputs, outputs and decisions for audit and evaluation.

## Putting humans in the right place

- **Confidence-based routing:** auto-handle high-confidence, low-risk cases; send the rest to a person.
- **Approval steps** before anything external or irreversible.
- **Sampling:** review a random 5–10% of auto-handled cases weekly.
- **Kill switch:** a way to pause the automation instantly.

## Production checklist for team automations

- [ ] An owner and a backup owner
- [ ] Inputs and outputs logged (without storing more personal data than needed)
- [ ] Failure alerts go to a person
- [ ] A test set of 20+ real examples, re-run when prompts or models change ([M8](/ai-native-teams/m08-evals/))
- [ ] Approved tools and connectors only; least-privilege credentials
- [ ] Documented in the playbook
