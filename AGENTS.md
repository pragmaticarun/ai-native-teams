# Instructions for agents working on this repo

AI-Native Teams: an Astro Starlight course site deployed to GitHub Pages.

## Setup and verify
- Setup: `pnpm install`
- Verify: `pnpm check:quizzes && pnpm build && python3 -m pytest -q labs`
- Preview: `pnpm dev`

## Layout
- Lessons: `src/content/docs/<module>/*.md` (plain Markdown; use `.mdx` only when a page needs a component).
- Each module has `index.md` (overview), numbered lessons via `sidebar.order`, `lab.md` and `quiz.mdx`.
- Quizzes: `src/quizzes/mXX.yaml`, rendered by `src/components/Quiz.astro`; `scripts/validate-quizzes.mjs` checks them.
- Lab code: `labs/`, each with tests that run in CI. Never add tests that need API keys.
- Sidebar: `astro.config.mjs`.

## Rules
- Internal links must start with `/ai-native-teams/`; the links validator fails the build otherwise.
- Never invent statistics, frameworks, versions or regulatory dates. Link a primary source; label anything unverified.
- Tool lists are dated. When you change versions or tools, update the "Last reviewed" date in `reference/tools-landscape.md`.
- Keep the course vendor-neutral: teach the pattern first, name tools as examples.
- Use British spelling and plain, short sentences.
