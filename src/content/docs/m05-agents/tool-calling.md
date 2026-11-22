---
title: Tool calling
description: How models use tools, and how to design tools models use well.
sidebar: { order: 1 }
---

## How it works

1. You (or the product) describe the available **tools** to the model: a name, a description, and the parameters each takes (as a JSON Schema).
2. The model, instead of answering in text, can reply with a **tool call**: "call `get_weather` with `{"city": "Pune"}`".
3. Your application **runs the tool** and sends the result back.
4. The model uses the result to answer, or calls another tool.

The model never executes anything itself. **Your code or the product executes tools**, which is exactly where you put permissions, validation and approvals.

```json
{
  "name": "search_tickets",
  "description": "Search support tickets by keyword. Returns up to 10 tickets with id, title, status and customer. Use for questions about existing customer issues.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": { "type": "string", "description": "Keywords, e.g. 'SSO login error'" },
      "status": { "type": "string", "enum": ["open", "closed", "any"], "default": "any" }
    },
    "required": ["query"]
  }
}
```

## Designing tools models use well

Tool design is interface design for a new kind of user.

- **Descriptions are prompts.** Say what the tool does, when to use it, and what it returns. Ambiguous descriptions cause wrong tool choices.
- **Fewer, higher-level tools beat many low-level ones.** `create_invoice(customer, items)` is better than six tools the model must sequence correctly.
- **Return what's useful, concisely.** Return names and summaries, not 5,000-line raw dumps. Paginate. Truncate with a note.
- **Make errors instructive.** "No customer named 'Acme Ltd'. Did you mean 'ACME Limited' (id 4417)?" lets the model recover.
- **Separate reading from writing.** Read-only tools can be granted freely; write tools need tighter control and often approval.
- **Make dangerous actions explicit.** `delete_record` should require an id, not a search query, and should be behind confirmation.

## Built-in tools

Many assistants and APIs now offer built-in tools: web search, code execution, file reading, image generation, memory. Turning these on is often the fastest way to give a model capability, and the same governance questions apply: what data goes where, and what can it change?
