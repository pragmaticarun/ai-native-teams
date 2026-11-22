---
title: Skills and progressive disclosure
description: Packaging reusable know-how so agents load it only when it's relevant.
sidebar: { order: 4 }
---

## The problem

Your team has dozens of procedures: how to write a release note, run the month-end check, triage a security report, format a board pack. Putting all of them in the instructions file makes it huge and distracting. Leaving them out means the AI doesn't know them.

## Progressive disclosure

The answer is **progressive disclosure**: the model sees a *short description* of each piece of know-how up front, and loads the full details only when a task needs them. This is how good documentation works for humans too: a table of contents, then the chapter you need.

## Agent Skills

**Agent Skills** are an open format for this. A skill is a folder with a `SKILL.md` file whose YAML frontmatter has a `name` and a `description`, plus optional scripts, templates and reference files. The agent sees only names and descriptions until a task matches, then reads the full skill ([specification](https://agentskills.io/specification)). The format was started by Anthropic and donated to the Agentic AI Foundation as an open standard ([announcement](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)), and several agent tools now support it.

```markdown
---
name: release-notes
description: Write customer-facing release notes from merged PRs and tickets. Use when
  asked to draft release notes, a changelog entry or a "what's new" post.
---

# Release notes

1. Collect merged PRs since the last tag (`scripts/list-prs.sh`).
2. Group by: New, Improved, Fixed. Skip internal-only changes (label `internal`).
3. Write for admins, not developers: lead with the benefit, then the detail.
4. Use `template.md`. Max 8 bullets per group.
5. Flag anything touching billing or permissions for PM review.
```

## Writing good skills

- **The description is the trigger.** Say *what it does* and *when to use it*, with the words people actually use ("release notes", "changelog", "what's new").
- **One job per skill.** Small, composable skills beat one giant "how we work" skill.
- **Include scripts for deterministic steps.** Let code do what code is good at (listing files, validating format) and let the model do judgment.
- **Reference files instead of inline walls of text.** The skill can point to `template.md`, `examples/`, `checklist.md`.
- **Test it.** Run three realistic requests: does the skill trigger? Does it produce the right result? Does it *not* trigger on unrelated requests?

## Equivalents in other tools

Even where "skills" aren't supported, the same pattern applies: custom assistants or GPTs per procedure, saved prompts with short descriptions, a docs index the agent can search, or tools exposed via MCP ([M5](/ai-native-teams/m05-agents/mcp/)).

## Team practice

When a prompt-library entry ([M2](/ai-native-teams/m02-prompting/prompt-library/)) is used weekly and has stabilised, **promote it to a skill** (or custom assistant). Keep skills in version control or a shared space, with an owner.
