---
title: Limits and failure modes
description: Hallucination, sycophancy, stale knowledge, context rot, brittleness, and the standard mitigation for each.
sidebar: { order: 3 }
---

Every team member should be able to name these failure modes and the matching mitigation. This is the foundation of using AI *safely* rather than just *often*.

| Failure mode | What it looks like | Mitigation |
|---|---|---|
| **Hallucination (confabulation)** | Invented facts, citations, APIs, quotes, numbers, delivered fluently | Ground the model in sources (retrieval, attached documents); ask for citations and check them; prefer tools for facts (search, database, calculator) |
| **Sycophancy** | Agrees with you, praises weak ideas, changes a correct answer when you push back | Ask for critique explicitly; ask it to argue the other side; don't reveal which answer you prefer; use a second model or fresh chat as reviewer |
| **Stale knowledge** | Unaware of recent events, prices, versions, laws | Give it current sources or a search tool; state today's date; check dates on anything time-sensitive |
| **Context rot / lost in the middle** | Ignores an instruction buried in a long conversation or document; quality drops in very long chats | Keep context focused; restate key constraints; start a fresh conversation with a summary; put critical instructions at the start or end |
| **Brittleness** | Small wording changes give very different results | Test prompts on several inputs and runs; use structured outputs; build evals ([M8](/ai-native-teams/m08-evals/)) |
| **Instruction injection** | Text inside a document, web page or email takes control ("ignore previous instructions…") | Treat all external content as untrusted data; limit what tools can do; human approval for risky actions ([M9](/ai-native-teams/m09-safety/)) |
| **Weak exact computation** | Arithmetic, counting, date maths, exact string operations go wrong | Have the model use a tool (code execution, spreadsheet, calculator) |
| **Bias** | Stereotyped or uneven treatment of groups; skewed defaults | Test with varied inputs; human review for decisions about people; see [responsible AI](/ai-native-teams/m09-safety/responsible-ai/) |
| **Overconfidence about itself** | Explains "how it got the answer" or "what it can see" inaccurately | Don't trust self-reports; verify behaviour directly |

## The verification habit

The single most important habit in this course: **match your verification effort to the cost of being wrong.**

- **Low stakes** (brainstorming, first drafts, personal notes): skim and use.
- **Medium stakes** (internal docs, code you'll test, customer-facing drafts a human sends): review carefully, check facts you'll rely on.
- **High stakes** (legal, medical, financial, security, decisions about people, production changes): independent verification, a second human, and an audit trail. Often, AI should only *assist* the human decision.

## Why "just tell it not to hallucinate" doesn't work

Instructions like "only use facts you're sure of" help a little, but the model can't reliably tell what it knows. What works is **changing the setup**: give sources, require citations to them, allow "I don't know", and check.

## Team practice

Start an **"AI fails" channel or doc**. Each post: what was asked, what went wrong, which failure mode, and what would have caught it. Review the patterns monthly; they become rules in your playbook.
