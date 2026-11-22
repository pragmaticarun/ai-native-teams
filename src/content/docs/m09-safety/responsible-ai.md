---
title: Responsible AI
description: Fairness, transparency, intellectual property, synthetic media, over-reliance and environmental impact.
sidebar: { order: 4 }
---

Security asks "can it be attacked?". Responsible AI asks "is it fair, honest and good for the people affected?". Both are part of being AI-native.

## Fairness and bias

Models learn patterns from human-generated data, including stereotypes and imbalances.

- **Highest risk:** decisions or recommendations about people, such as hiring, performance, lending, insurance, healthcare, education and access to services.
- **Test with variation:** run the same case with different names, genders, ages, languages or locations, and compare.
- **Keep humans deciding** about people, with AI as input, not verdict, and make sure those humans can disagree with it.
- **Document** what the system is for and not for.

## Transparency

- **Tell people when they're dealing with AI** (chatbots, AI-generated content). In the EU, the AI Act's transparency obligations require this in many cases ([M10](/ai-native-teams/m10-governance/regulation/)).
- **Be honest internally** about AI use in work products. Many teams adopt a simple norm: you're accountable for anything you send, however it was produced, and you disclose AI use where the audience would care (e.g. research findings, legal or financial analysis).

## Intellectual property and confidentiality

- **Inputs:** don't put others' confidential material (client documents under NDA, third-party code with restrictive licences) into tools not approved for it.
- **Outputs:** copyright and ownership of AI-generated content is unsettled law and differs by jurisdiction. Check with legal before relying on AI-generated material as a core asset (brand assets, product code in some contexts).
- **Code:** use features that filter or flag suggestions matching public code where available, and keep normal licence-compliance checks.

## Synthetic media

- Never generate realistic images, voices or video of **real people** without consent.
- **Label** AI-generated media where required or where people could be misled.
- Be alert to **deepfake fraud**: voice or video "from the CEO" asking for urgent payments or credentials. Verify through a second channel.

## Over-reliance and skills

- **Automation bias:** people tend to accept automated suggestions even when wrong. Design reviews that require active checking (e.g. reviewers note what they verified).
- **Skill atrophy:** if juniors never write a first draft or debug by hand, they may not develop the judgment to review AI work. Deliberately include learning tasks ([M11](/ai-native-teams/m11-change/enablement/)).

## Environmental impact

Large models use significant energy and water. Practical, proportionate steps: right-size models, avoid needless regeneration and huge contexts, and prefer providers that publish efficiency and sustainability data.
