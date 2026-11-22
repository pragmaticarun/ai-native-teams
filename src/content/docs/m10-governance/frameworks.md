---
title: Frameworks and standards
description: NIST AI RMF and its Generative AI Profile, ISO/IEC 42001, and how teams can use them without drowning in paperwork.
sidebar: { order: 2 }
---

## NIST AI Risk Management Framework (AI RMF 1.0)

Published by the US National Institute of Standards and Technology in January 2023, the AI RMF is voluntary and widely used internationally ([NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)). It organises AI risk management into four functions:

| Function | What it means for a team |
|---|---|
| **Govern** | Policies, roles, accountability and culture for AI risk |
| **Map** | Understand context: what the system is for, who's affected, what could go wrong |
| **Measure** | Assess and track risks (evals, testing, monitoring) |
| **Manage** | Prioritise and act on risks; respond to incidents |

NIST also published a **Generative AI Profile** (NIST AI 600-1, July 2024) that applies the framework to risks specific to generative AI, such as confabulation, information integrity, data privacy and information security ([NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1)).

## ISO/IEC 42001:2023

The first international **management system standard** for AI: requirements for establishing, running and improving an AI management system (AIMS), in the same family style as ISO/IEC 27001 for information security. Organisations can be **certified** against it ([ISO/IEC 42001](https://www.iso.org/standard/42001)). Related: ISO/IEC 23894 gives guidance on AI risk management.

## Others worth knowing

- **OWASP GenAI Security Project** for security risks ([M9](/ai-native-teams/m09-safety/threat-model/)).
- **MITRE ATLAS**, a knowledge base of adversary tactics against AI systems ([atlas.mitre.org](https://atlas.mitre.org/)).
- **OECD AI Principles**, high-level principles adopted by many governments ([oecd.ai](https://oecd.ai/en/ai-principles)).

## Using frameworks at team scale

Frameworks are written for organisations. A team can map its everyday practices to them:

| Team practice from this course | NIST AI RMF function |
|---|---|
| AI use policy, owners, champions (M10, M11) | Govern |
| Agent briefs, threat models, AI register (M5, M9, M10) | Map |
| Eval sets, red-teaming, monitoring dashboards (M8, M9) | Measure |
| Approvals, kill switches, incident response, fixes from evals (M5, M7, M9) | Manage |

When your organisation's governance team asks "how do you manage AI risk?", that table is your answer, with the artefacts as evidence.
