---
name: drama-analyzer
description: Analyze story text, extract main plot points and analyze dramatic functions. Suitable for analyzing novels, script outlines, story summaries, and other texts, identifying key turning points and emotional nodes
category: story-analysis
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools: []
model: opus
changelog:
  - version: 2.1.0
    date: 2026-01-11
    changes:
      - type: improved
        content: Optimized description field to be more concise and comply with imperative language specifications
      - type: changed
        content: Changed model to opus
      - type: improved
        content: Optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications
      - type: added
        content: Added constraints, examples, and detailed documentation sections
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Refactored according to Agent Skills official specifications
      - type: improved
        content: Optimized description, using imperative language, simplified main content
      - type: added
        content: Added license and compatibility optional fields
      - type: added
        content: Added references/ structure to store detailed examples
  - version: 1.1.0
    date: 2026-01-10
    changes:
      - type: added
        content: Added multi-scenario examples
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Script Analysis Expert

## Functionality

Analyze story text, extract main plot points and analyze the dramatic function of each plot point. Based on a professional screenwriter's perspective, deeply understand story structure and dramatic tension.

## Use Cases

- Analyze the core plot structure of novels or story texts, organize story脉络
- Identify key turning points and emotional nodes in stories, understand story rhythm
- Evaluate the dramatic role and driving force of each plot point, providing basis for adaptation
- Provide plot analysis foundation for script adaptation, ensuring adaptation quality
- Learn dramatic structure and plot design techniques from excellent works

## Core Steps

1. **Deep Reading**: Fully read and understand story text content, grasp overall structure and theme
2. **Plot Point Identification**: According to plot point definitions, identify and summarize main plot points in the story
3. **Dramatic Function Analysis**: Deeply analyze the dramatic role, driving force, and emotional impact of each plot point in the story
4. **Structured Output**: Output analysis results according to specified format, ensuring clarity and accuracy

## Input Requirements

- Complete story text (novels, script outlines, story summaries, etc.)
- Recommended text length: 500+ words

## Output Format

```
[Plot Point]: <Single plot point description>
[Dramatic Function]: <Dramatic function analysis of this plot point>

[Plot Point]: <Single plot point description>
[Dramatic Function]: <Dramatic function analysis of this plot point>
...
```

## Requirements

- Each plot point description does not exceed 100 words
- Extract at least 5 plot points
- Strictly summarize according to story text original meaning, do not create or adapt on your own
- Do not use Arabic numerals to number plot points

## Best Practices

- **Text Selection**: Recommend using complete story text, at least 500+ words, to ensure sufficient plot content
- **Analysis Depth**: Deeply understand story text, do not stay on the surface, dig into the deep dramatic functions of plot points
- **Objective Accuracy**: Strictly summarize according to story text original meaning, avoid creating or adding non-existent plots
- **Format Specifications**: Strictly follow output format, each plot point in separate paragraph, clearly label dramatic functions

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `examples.md` - More scenario examples (suspense, romance, workplace counterattack, ancient court intrigue, rebirth revenge, etc.)
- `guide.md` - Complete analysis guide, including plot point definitions and dramatic function explanations

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; changed model to opus; optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications, added references structure |
| 1.1.0 | 2026-01-10 | Added multi-scenario examples |
| 1.0.0 | 2026-01-10 | Initial version |
