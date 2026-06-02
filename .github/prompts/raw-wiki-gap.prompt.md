---
description: "Audit which raw/ files still need to be promoted to wiki/ and produce a prioritised work list."
name: "Raw → Wiki Gap Analysis"
agent: "agent"
---

You are auditing the UX Pattern Oracle content pipeline.

## Task

1. List every `.md` file in `raw/` (ignore `.gitkeep`). Extract slugs (filename without `.md`).
2. List every `.md` file in `wiki/` (ignore `.gitkeep`). Extract slugs.
3. Compute the difference: slugs in `raw/` that have **no** matching slug in `wiki/`.
4. Output a prioritised work list using the groupings below.

## Output format

Print a markdown table with three columns: **Slug**, **Raw file size (bytes)**, **Suggested wiki slug**.
Sort by descending file size (larger files are usually richer content).

Then group the table by topic tag (infer from the slug):

- `dashboard` — anything with dashboard, data-viz, metrics
- `ai-ux` — AI, GenAI, LLM, ML, chatbot, oracle, agent patterns  
- `drag-and-drop` — drag, drop, DnD, sortable
- `accessibility` — accessible, a11y, WCAG
- `enterprise-b2b` — enterprise, B2B, SaaS, admin
- `other` — everything else

After the table, print a one-line count:
`Gap: N files remain to be promoted (out of M total raw files).`

## Rules

- Do not create, edit, or delete any files.
- Do not start promoting files — this prompt is read-only analysis.
- If `raw/` is empty, print: `No raw files found.`
