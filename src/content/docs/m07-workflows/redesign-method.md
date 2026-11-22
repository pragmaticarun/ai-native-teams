---
title: A method for workflow redesign
description: Map, score, redesign, pilot and scale, a five-step method for AI-native workflows.
sidebar: { order: 1 }
---

## Step 1 · Map the current workflow

Pick a workflow with a clear start and end (e.g. "customer reports a bug → fix shipped and customer told"). Map every step: who does it, what they read, what they produce, how long it takes, and **where work waits**. Waiting and hand-offs are usually where most of the elapsed time goes.

## Step 2 · Score each step

For every step, ask:

| Question | High score means |
|---|---|
| Is it mostly reading, writing, summarising, classifying, transforming or searching? | AI can probably do or draft it |
| Is the input information available digitally? | Feasible to automate |
| How costly is an error? | Higher cost → more human review |
| Is it a hand-off or a wait? | Candidate for elimination |
| Does it need judgment, relationships or accountability? | Keep a human in charge |

## Step 3 · Redesign, don't just accelerate

Three moves, in order of impact:

1. **Eliminate.** Does the step still need to exist? (Status reports that an agent can generate on demand; hand-offs that exist because one person couldn't do both parts before AI.)
2. **Collapse.** Can one person, with AI, do what used to need three hand-offs? (A PM who prototypes directly; a support agent who resolves instead of escalating.)
3. **Automate with checkpoints.** For what remains, let AI do the work and put humans at the decision points.

Then redraw the workflow. Name the **human checkpoints** explicitly.

## Step 4 · Pilot with measurement

- Choose 2–4 **outcome metrics** before starting (cycle time, quality, customer satisfaction, error rate), and record the **baseline** ([M12](/ai-native-teams/m12-value/)).
- Run the new workflow for 2–4 weeks with a small group.
- Log failures and fix them (instructions, tools, checkpoints).

## Step 5 · Scale and maintain

Document the workflow in the playbook: steps, prompts/skills/automations, owners, checkpoints, metrics. Assign an owner who reviews it when tools or models change.

## The "would we design it this way today?" test

For any workflow, ask: *if we were starting this team today, with today's AI, would we design the process like this?* If the answer is no, it's a redesign candidate.
