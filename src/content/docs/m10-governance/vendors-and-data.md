---
title: Vendors, data and the AI register
description: Evaluating AI tools and providers, matching data classes to tools, and keeping a lightweight register of AI systems.
sidebar: { order: 4 }
---

## Questions to ask any AI vendor

| Area | Questions |
|---|---|
| **Training use** | Is our data (prompts, files, outputs) used to train models? Is that off by default for business accounts? |
| **Retention** | How long are prompts, outputs and logs kept? Can we set it? Zero-retention options? |
| **Location** | Where is data processed and stored? Regional options? |
| **Sub-processors** | Which model providers and other parties see the data? |
| **Security** | Certifications (e.g. SOC 2, ISO/IEC 27001, ISO/IEC 42001), SSO, admin controls, audit logs |
| **Access control** | Does the tool respect our permissions (e.g. in connectors and enterprise search)? |
| **Connectors & agents** | What can integrations read and do? Can admins restrict them? |
| **Contract** | Data processing agreement, IP terms, indemnities for generated output |
| **Model changes** | How are model updates communicated? Can we pin versions (for API use)? |

Consumer and business versions of the same product often have **very different** terms. Make sure people use the business version.

## Matching data to tools

Combine your data classification with your approved tools in one matrix (see the [policy template](/ai-native-teams/m10-governance/policy/#template)). Keep it on one page, linked from everywhere people use AI.

## The AI register

A simple list of the AI systems your team runs (not every chat, but every **assistant, automation, agent or AI feature** that others rely on).

| Field | Example |
|---|---|
| Name & purpose | Support triage automation |
| Owner | Maria K. (backup: Dev S.) |
| Tools & models | Automation platform; small model for classification |
| Data used | Ticket text and customer name (Confidential) |
| Actions it can take | Set priority and queue; no customer-facing output |
| Autonomy & approvals | L5 observer with 10% weekly sampling ([M5](/ai-native-teams/m05-agents/multi-agent-and-hitl/#autonomy-is-a-design-choice)) |
| Risk tier | Low (internal, reversible) |
| Evals | 120-ticket set, 96% routing accuracy, re-run monthly |
| Regulatory notes | None (not customer-facing, no decisions about people) |
| Last reviewed | 2026-11-10 |

Review the register quarterly. It's also your evidence for governance frameworks and audits.

## Lightweight review process

| Risk | Example | Review |
|---|---|---|
| Low | Internal summarising, drafting, coding in sandboxes | Self-service within policy; register if shared |
| Medium | Customer-facing drafts with human send; internal agents with write access | Team lead + security checklist |
| High | Automated customer-facing output; decisions about people; regulated data | Formal review with legal, security, privacy; documented evals |
