# AI-Native Teams

A comprehensive, hands-on course that takes **whole teams** (engineering, product, design, operations and leadership) from AI-curious to AI-native: the concepts, tools, workflows, safety practices, governance and change management it takes.

- **Site:** https://pragmaticarun.github.io/ai-native-teams/
- **Format:** 13 modules, ~55 lessons, 12 hands-on labs, a capstone (your team's 90-day plan) and 12 self-check quizzes.
- **Content last reviewed:** 22 November 2026.

| Part | Modules |
|---|---|
| Start here | What AI-native means, learning paths by role, team self-assessment |
| 1 · Understand | How modern AI works · Prompting · Context engineering |
| 2 · Build | RAG & knowledge · Tools, agents & MCP · AI-assisted engineering · AI workflows for every role |
| 3 · Trust | Evals & observability · Safety & security · Governance & compliance (EU AI Act, NIST AI RMF, ISO/IEC 42001) |
| 4 · Transform | Operating model & change · Measuring value · Capstone: 90-day plan |

Companion course for engineers who want to build agents from scratch: [AI-Native Software Development](https://pragmaticarun.github.io/ai-native-course/).

## Run locally

```bash
pnpm install
pnpm dev                 # http://localhost:4321/ai-native-teams/
pnpm check:quizzes && pnpm build   # what CI runs
python3 -m pytest -q labs          # lab code tests
```

Requires Node 22+ and pnpm 12. Lab code needs Python 3.10+ and has no third-party dependencies (pytest for tests).

## Deployment

`.github/workflows/deploy.yml` builds and publishes the site on every push to `main`. One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Contributing

Found something wrong or out of date? Open an issue or PR. See [AGENTS.md](AGENTS.md) for conventions (they apply to humans too).
