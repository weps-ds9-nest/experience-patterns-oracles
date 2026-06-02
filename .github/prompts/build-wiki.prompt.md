---
description: "Promote raw/ scraped files into wiki/ — clean boilerplate, write concise summaries, and add [[wiki-links]] to build the knowledge graph."
name: "Build Wiki"
agent: "agent"
---

You are building the UX Pattern Oracle wiki from scraped source files.

Before starting, list all slugs already present in `wiki/` (filenames without `.md`).
Work through every `.md` file in `raw/` (skip `.gitkeep`) **that does not already have a
corresponding file in `wiki/`** — i.e. skip any raw file whose slug already exists in wiki/.
Process remaining files in batches of 10. After each batch confirm the files written, then continue.

---

## For each file, do all three steps in order:

### Step 1 — Clean

Strip all of the following boilerplate that Jina/smry.ai inserts at the top:

- Lines starting with `Title:`, `URL Source:`, `Published Time:`, `Warning:`
- The literal text `Markdown Content:` and the blank line after it
- Any smry.ai navigation chrome:
  - Lines containing `smry.ai`, `Get Pro`, `favicon`, `Annotations`, `No highlights yet`, `Select text in the article`

Keep everything that is actual article content.

### Step 2 — Summarise & rewrite

Rewrite the cleaned content into a compact wiki entry:

- **Heading**: `# <Article Title>` (infer from content if missing)
- **One-paragraph summary** (~80 words) capturing the core argument
- **Key patterns or concepts** — bullet list of the named patterns, principles, or frameworks the article introduces (3–8 bullets, each ≤ 15 words)
- **Full article body** — keep the cleaned original text after the bullets, lightly edited for clarity (remove filler phrases, fix obvious OCR/scrape artefacts)

### Step 3 — Add wiki-links

Append a `## Related` section at the very end with `[[wiki-links]]` to other files
**that already exist in `wiki/`** at the time you write this file.

Rules:
- 3–6 links per file
- Only link to files that exist — never invent slugs
- Use the destination file's slug without the `.md` extension: `[[progressive-disclosure]]`
- Group links by relevance, not alphabetically

---

## Output path

Save each processed file to `wiki/<slug>.md` where `<slug>` is a short,
lowercase, hyphen-separated name derived from the article title
(e.g. `progressive-disclosure-in-ai.md`, `conversational-ai-patterns.md`).

Do **not** modify any file in `raw/`.
Do **not** create a changelog, summary file, or any file other than the wiki entries.

---

## Batch protocol

After every 10 files, output a one-line status:
`Batch N complete: [list of wiki/ filenames written]`
Then immediately start the next batch without waiting.
