---
title: Structured output
description: Getting tables, checklists and JSON you can reliably feed into other tools.
sidebar: { order: 3 }
---

As soon as AI output feeds something else (a spreadsheet, a ticket, a script, another prompt), **structure beats prose**.

## Levels of structure

1. **Formatted prose:** headings, bullets, a table. Ask for it explicitly: "Use a table with columns X, Y, Z."
2. **Templates:** give the exact skeleton to fill in.
3. **Machine-readable output:** JSON, CSV or YAML that follows a schema.

## Use the platform's structured-output feature when you can

Most major model APIs support **structured outputs** (also called JSON mode, JSON schema output or response format), where you supply a JSON Schema and the API constrains the output to match it. Many no-code automation platforms expose the same thing as "output parser" or "structured output" steps. This is far more reliable than asking nicely for JSON.

A schema for extracting invoice data might look like:

```json
{
  "type": "object",
  "properties": {
    "vendor": { "type": "string" },
    "invoice_number": { "type": "string" },
    "total": { "type": "number" },
    "currency": { "type": "string", "enum": ["EUR", "USD", "GBP", "INR"] },
    "due_date": { "type": "string", "description": "ISO 8601 date" },
    "confidence": { "type": "string", "enum": ["high", "medium", "low"] }
  },
  "required": ["vendor", "total", "currency", "confidence"]
}
```

## Design tips

- **Include an escape hatch.** Fields like `confidence`, `notes` or `"unknown"` values stop the model from inventing data to fill required fields.
- **Use enums** for categories, so you never get "Bug", "bug" and "Defect" as three values.
- **Keep reasoning separate.** If you want the model to explain itself, add a `reasoning` field *before* the answer field, or ask for reasoning outside the structured block.
- **Validate anyway.** Check the output in code or with a spreadsheet rule; constrained output guarantees shape, not truth.

## Team practice

When an AI output is used by more than one person or tool, agree a **template or schema** and put it in the prompt library. Consistent structure is what makes automation (M7) and evaluation (M8) possible.
