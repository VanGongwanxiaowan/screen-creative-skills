---
name: text-truncator
description: Intelligently truncate text while preserving content integrity and semantic coherence. Suitable for long text preprocessing, ensuring text does not exceed specified length limits
category: tools
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
        content: Optimized description field to be more concise and comply with imperative language standards
      - type: changed
        content: Changed model to opus
      - type: improved
        content: Optimized descriptions for functionality, core capabilities, input requirements, and output format to comply with imperative language standards
      - type: added
        content: Added usage scenarios, constraints, examples, and detailed documentation sections
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Restructured according to Agent Skills official specifications
      - type: improved
        content: Optimized description, used imperative language, streamlined main content
      - type: added
        content: Added license and compatibility optional fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Text Truncator Tool

## Functionality

Intelligently truncate text while maintaining content integrity and semantic coherence, limiting text to a specified length.

## Usage Scenarios

- Preprocess text that exceeds length limits to meet agent input requirements
- Extract key sections for text previews or summary generation to improve efficiency and readability
- Assist content creation by intelligently trimming generated long text to avoid redundancy

## Core Capabilities

- **Semantic-Priority Truncation**: Prioritize truncation at natural semantic boundaries (periods, question marks, exclamation points) to maximize sentence integrity
- **Paragraph Integrity**: When semantic boundaries are insufficient, prioritize truncation at paragraph ends or line breaks to avoid breaking paragraph structure
- **Precise Length Control**: Strictly adhere to user-specified maximum length limits, ensuring output text does not exceed limits
- **Truncation Marker Insertion** (optional): Automatically add custom truncation markers (such as "...") at the end of truncated text to indicate content omission

## Input Requirements

- **Text Content**: Original text to be truncated (string)
- **Maximum Length Limit**: Maximum length after text truncation (integer, such as character count or token count)
- **Truncation Marker** (optional): Custom truncation marker, such as "..." or "[content truncated]"

## Output Format

```
[Text Truncation Report]

- Original text length: [integer] words/tokens
- Truncated length: [integer] words/tokens
- Truncation position: [position description, such as "at end of sentence X"] or "not truncated"

### Truncated Text
[truncated text content]
```

## Constraints

- Truncated text length must strictly comply with maximum length limits
- Ensure truncated text remains as semantically coherent and complete as possible
- If text does not reach maximum length, do not truncate; return original text
- Output format must be structured, clearly displaying length information before and after truncation and truncated text content

## Examples

See `{baseDir}/references/examples.md` for more detailed examples:
- `examples.md` - Contains truncation examples for different lengths, different truncation markers, and complex text structures

## Detailed Documentation

See `{baseDir}/references/examples.md` for detailed guidance and cases on the text truncator tool.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field; changed model to opus; optimized descriptions for functionality, core capabilities, input requirements, and output format; added usage scenarios, constraints, examples, and detailed documentation sections |
| 2.0.0 | 2026-01-11 | Restructured according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
