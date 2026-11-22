---
title: "Coding agents: kinds and when to use each"
description: IDE agents, terminal agents, cloud/background agents and AI code review, with how to work with them well.
sidebar: { order: 2 }
---

## The kinds

| Kind | Examples (Nov 2026) | Best for |
|---|---|---|
| **IDE agents** | Cursor, GitHub Copilot in VS Code and JetBrains, Windsurf, and agent modes in other IDEs | Interactive work where you watch and steer |
| **Terminal / CLI agents** | Claude Code, OpenAI Codex CLI, GitHub Copilot CLI, Gemini CLI | Multi-file changes, running tests and tools, scripting agents into workflows |
| **Cloud / background agents** | GitHub Copilot coding agent (assign an issue, get a PR), Codex cloud, Cursor background agents, Claude Code on the web, Devin | Well-specified tasks you hand off and review later; parallel work |
| **AI code review** | Review bots and agent review features on pull requests | A first-pass review on every PR; catching obvious issues before humans look |

Tool names and capabilities change quickly. See the dated [tools landscape](/ai-native-teams/reference/tools-landscape/). The patterns below are stable.

## Working well with a coding agent

1. **Explore, plan, then code.** Ask the agent to read the relevant code and propose a plan *before* editing. Review the plan; it's much cheaper to fix than the code.
2. **Give it a way to verify.** Tests, a type-checker, a linter, a script that reproduces the bug, a screenshot to match. Agents do dramatically better when they can check their own work.
3. **Keep tasks small.** One concern per session or PR. Small batches are easier to review, and DORA lists working in small batches as one of its AI capabilities.
4. **Course-correct early.** Interrupt as soon as it heads the wrong way; don't wait for a 40-file diff.
5. **Clear context between tasks.** Start fresh sessions for unrelated work.
6. **Use it to understand, not just write.** "Explain how auth works in this repo", "find every place we compute tax" are some of the highest-value uses, especially for onboarding.

## Background agents and parallel work

Cloud agents let one engineer run several tasks at once. This shifts the bottleneck to **review**. Teams that adopt them successfully:

- Write issues as **specs** with acceptance criteria ([next lesson](/ai-native-teams/m06-coding/spec-driven/)).
- Have **CI that the agent must pass** before a human looks.
- Limit how many agent PRs a person has in flight.
- Track **rework**: how often agent PRs need significant changes or get abandoned.

## Non-engineers and code

PMs, designers and analysts increasingly use coding agents and "vibe coding" tools to build prototypes, internal tools and data scripts. Encourage this for **prototypes and personal tools**, with a clear line: anything that touches production, customer data or shared systems goes through normal engineering review.
