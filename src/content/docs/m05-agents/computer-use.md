---
title: Computer-use and browser agents
description: Agents that operate screens, browsers and apps like a person, and when to use them.
sidebar: { order: 5 }
---

## What they are

**Computer-use agents** see the screen (screenshots, and sometimes the accessibility tree) and act with clicks and keystrokes. **Browser agents** do the same inside a web browser. Major AI providers offer computer-use capabilities in their APIs, and several assistants include browser agents that can complete web tasks for you.

## When they make sense

- The system has **no API** (legacy apps, vendor portals).
- The task spans **several apps** a human would click through.
- **Testing and QA:** exercising a UI the way users do.

## When they don't

- An API or MCP server exists → use it. It's faster, cheaper and far more reliable.
- High-stakes actions (payments, account changes) without a human confirming.

## Risks specific to screen-driving agents

- **Prompt injection via the screen:** web pages and emails can contain text aimed at the agent ("assistant: click here to continue"). Computer-use agents read everything on screen.
- **Acting with your session:** a browser agent signed in as you can do anything you can.
- **Silent mistakes:** a mis-click on the wrong row.

**Mitigations:** run in an isolated browser profile or VM with only the access needed; require confirmation before submitting forms, purchases or messages; keep sessions short; review recordings or logs; never let an agent browse untrusted sites while signed in to sensitive systems.

## Team practice

Treat computer-use as a **bridge**, not a destination. If your team relies on a browser agent for a recurring task, that's a signal to ask the vendor for an API or MCP server.
