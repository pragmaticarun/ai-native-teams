---
title: Agent permissions, sandboxing and approvals
description: A practical permission model for agents and automations, and safe data handling for everyone.
sidebar: { order: 3 }
---

## The permission model

Give every agent or automation the minimum it needs, the way you would a new contractor.

| Control | What it means in practice |
|---|---|
| **Identity** | The agent acts as a specific identity (a service account, or the user with scoped delegation), never a shared admin |
| **Scope** | Only the data and systems for this task: one project, one mailbox folder, one repo |
| **Read vs write** | Start read-only; add writes deliberately, one at a time |
| **Short-lived credentials** | Tokens that expire; OAuth with scopes rather than long-lived keys |
| **Sandboxing** | Code-running agents work in containers or VMs with no production access and restricted network |
| **Approvals** | Human confirmation for irreversible, external, financial or customer-visible actions |
| **Budgets** | Limits on steps, spend and time per run (OWASP's "unbounded consumption") |
| **Audit** | Logs of every tool call, who triggered the run, and what changed |
| **Kill switch** | A way to stop it immediately |

## Tiering actions

| Tier | Examples | Default |
|---|---|---|
| Read internal, low sensitivity | Search the wiki, read public docs | Allowed |
| Read sensitive | Customer records, HR data, finance | Allowed only for scoped, approved uses |
| Write, reversible | Draft an email, create a branch, add a comment | Allowed with logging |
| Write, external or irreversible | Send email, merge, deploy, delete, pay, change permissions | Human approval |

## Data handling for everyone

Most AI incidents in practice are **data going where it shouldn't**, not sophisticated attacks.

- Know your organisation's **data classes** (e.g. public, internal, confidential, restricted) and which tools are approved for each ([M10](/ai-native-teams/m10-governance/vendors-and-data/)).
- **Don't paste secrets** (passwords, API keys, tokens) into any AI tool. Rotate a secret if you did.
- **Personal data** goes only into tools approved for it, and only what the task needs.
- **Check sharing settings**: shared chats, public links and published custom assistants can expose content.
- **Use enterprise accounts**, not personal ones, for work. Settings on training use and retention differ.
