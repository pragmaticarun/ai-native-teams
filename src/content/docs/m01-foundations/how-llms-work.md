---
title: How LLMs work, without the maths
description: Tokens, next-token prediction, training stages, context windows and sampling, explained for everyone.
sidebar: { order: 1 }
---

## The one-sentence version

A large language model (LLM) is a program that, given some text, **predicts what text should come next**, one small piece at a time. Everything else (chat, coding, tool use, "reasoning") is built on that.

## Tokens: the unit of everything

Models don't read words; they read **tokens**, chunks of text that are often a word, part of a word, or a punctuation mark. In English, a token is roughly ¾ of a word on average, but code, numbers and non-English languages often use more tokens per word.

Tokens matter because they are the unit of:

- **Cost.** Providers charge per input token and per output token (output usually costs several times more).
- **Limits.** The *context window* is measured in tokens.
- **Speed.** Output is generated token by token, so long answers take longer.
- **Weird failures.** Counting letters in a word or doing exact arithmetic is hard partly because the model sees tokens, not characters or digits.

## How a model is made (three stages)

1. **Pre-training.** The model reads an enormous amount of text and code and learns to predict the next token. This is where it picks up language, facts, styles and patterns. It is expensive and happens rarely, which is why models have a **knowledge cutoff**.
2. **Post-training (instruction tuning and preference training).** The raw predictor is trained on examples of helpful conversations and on human or AI feedback about which answers are better. This is what turns "autocomplete" into an assistant that follows instructions and refuses harmful requests.
3. **Reasoning training (for reasoning models).** Many current models are further trained with reinforcement learning on tasks with checkable answers (maths, code, puzzles), which teaches them to "think" at length before answering. See [the next lesson](/ai-native-teams/m01-foundations/model-types/).

## The context window: the model's working memory

Everything the model "knows" about your conversation is in its **context window**: the system instructions, the conversation so far, any documents or tool results, and its own previous replies. Important consequences:

- **The model has no memory between conversations** unless a product feature (like "memory" or project files) puts information back into the context.
- **Context is finite.** Current frontier models accept hundreds of thousands of tokens, some a million or more, but quality on details can drop as the context fills up. More context is not automatically better. [Module 3](/ai-native-teams/m03-context/) is about choosing what goes in.
- **What's in the context steers the output.** Paste a sloppy example and you'll get sloppy output; paste your style guide and you'll get your style.

## Sampling: why answers vary

At each step the model produces a probability for every possible next token. The product then **samples** one. Settings like **temperature** control how adventurous that choice is: low temperature gives more predictable output, high temperature more varied output. That's why the same prompt can give different answers, and why you should **test a prompt several times** before trusting it.

## A useful analogy

Think of an LLM as **an extremely well-read new colleague with no memory of yesterday, who never says "I don't know" unless trained to, and who does their best work when you hand them a clear brief and the right documents.** Most good AI practice follows from that sentence.

## Common misconceptions

| Misconception | Reality |
|---|---|
| "It looks things up in a database." | By default it generates from patterns learned in training. It only "looks things up" if a tool (search, retrieval) is connected. |
| "It remembers our last chat." | Only if a memory feature re-inserts that information. |
| "If it sounds confident, it's right." | Fluency and correctness are separate. Confident errors are normal. |
| "It's learning from my corrections right now." | Not within a normal chat. Your corrections only affect the current context. (Whether your data is used for future *training* depends on the product's terms; see [M10](/ai-native-teams/m10-governance/).) |

## Team practice

- Agree on vocabulary: *token*, *context window*, *system prompt*, *temperature*, *hallucination*. Use the [glossary](/ai-native-teams/reference/glossary/).
- When someone reports "AI is useless for X", ask first: *what was in the context?*
