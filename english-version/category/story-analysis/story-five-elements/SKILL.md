---
name: story-five-elements
description: "Analyze five core story elements — genre type, story summary, character biographies, character relationships, and major plot points — producing a structured comprehensive report with optional mind map. Use when preparing for script adaptation, conducting deep story analysis, creating story development documentation, or evaluating overall story quality and market potential."
license: MIT
compatibility: Claude Code 1.0+
metadata:
  category: story-analysis
  version: 2.1.0
  last_updated: 2026-01-11
  maintainer: Gong Fan
  model: opus
---

# Story Five Elements Analysis Expert

## Five Core Elements

| Element | What to Produce |
|---------|----------------|
| **Genre & Creative Elements** | Primary/secondary genres, unique creative hooks, tone, and style markers |
| **Story Summary** | 300–500 word narrative covering setup, escalation, climax, and resolution |
| **Character Biographies** | For each major character: background, motivation, personality traits, arc |
| **Character Relationships** | Relationship types, power dynamics, evolution across the story |
| **Major Plot Points** | Key turning points mapped to three-act structure (setup, confrontation, resolution) |

## Workflow

1. **Preprocess** — if text exceeds context limits, split at chapter or scene boundaries with 200-word overlap to preserve continuity.
2. **Analyze each element** — for each of the five elements above, extract evidence directly from the text. Quote or paraphrase key passages as supporting evidence.
3. **Cross-reference** — verify character biographies align with relationship descriptions; confirm plot points match the story summary's narrative arc.
4. **Compile report** — assemble findings in the output format below.
5. **Generate mind map** (optional) — produce a text-based mind map linking the five elements.

## Input Requirements

- Complete story text (supports long text)
- Text length: No limit (system will automatically process long text)

## Output Format

```
[Story Five Elements Analysis Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Genre Type and Creative Element Extraction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Genre types, creative elements, story features, style characteristics]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Story Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Complete story summary, 300-500 words]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Character Biographies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Biographies generated for each main character]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. Character Relationships
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Character relationship types, relationship characteristics, relationship development process]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V. Major Plot Points
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Main plot points arranged by development stage]
```

## References

See `{baseDir}/references/` for detailed worked examples and analysis techniques:
- `examples.md` — full analysis examples across genres (urban emotion, court intrigue, suspense mystery)
- `guide.md` — complete five-elements analysis guide
