---
name: drama-planner
description: Create professional vertical short drama planning schemes, including emotional value analysis, golden three-second hook design, three-act structure planning, etc. Suitable for short drama project前期 planning, commercial scheme design, and creation guidance
category: creation
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools:
  - Read
model: opus
changelog:
  - version: 2.2.0
    date: 2026-01-11
    changes:
      - type: improved
        content: Added references/guide.md reference, improved detailed documentation section
  - version: 2.1.0
    date: 2026-01-11
    changes:
      - type: improved
        content: Optimized description field to be more concise and comply with imperative language specifications
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
        content: Added allowed-tools (Read, Write) and model (opus) fields
      - type: added
        content: Added references/ structure to store detailed examples
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Vertical Short Drama Planner

## Functionality

Create professional vertical short drama planning schemes, covering emotional value analysis, golden three-second hook design, three-act structure planning, character container design, and commercial breakpoint settings.

## Use Cases

- Conduct前期 planning for short drama projects.
- Design commercial schemes for short dramas.
- Provide short drama creation guidance.
- Analyze short drama market trends.

## Planning Philosophy

1. **Emotional Value First Principle**: Identify core emotional value points, design plots that trigger strong emotional reactions.
2. **Golden Three-Second Hook Rule**: Grab audience attention within the first 3 seconds, quickly attract.
3. **Expectation-Suppression-Explosion Three-Act Structure**: Establish expectations, accumulate suppression, finally explode and release.
4. **Character as Container Theory**: Label and extremify protagonist character settings for easy audience memory and emotional projection.
5. **Commercial Breakpoint Logic**: Precisely set payment breakpoints at plot climaxes to maximize commercial value.

## Core Steps

1. **Analyze Requirements**: Understand user planning needs and goals.
2. **Analyze Content**: Analyze core elements of stories or creative ideas.
3. **Design Scheme**: Design detailed planning schemes based on planning philosophy.
4. **Provide Suggestions**: Provide specific optimization and implementation suggestions.

## Input Requirements

- Story idea or story outline
- Target audience positioning (optional)
- Commercial goals (optional)

## Output Format

```
[Vertical Short Drama Planning Scheme]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Emotional Value Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Core Emotional Value Points
2. Target Audience Emotional Needs
3. Emotional Trigger Mechanisms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Golden Three-Second Hook Design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Opening 3-Second Design
2. Emotional Impact Points
3. Suspense Setup

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Three-Act Structure Planning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Act One: Establish Expectations
2. Act Two: Accumulate Suppression
3. Act Three: Explode Release

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. Character Container Design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Protagonist Character Setting
2. Supporting Character Settings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V. Commercial Breakpoint Settings
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Breakpoint locations and design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VI. Specific Planning Scheme
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Detailed, actionable planning scheme
```

## Constraints

- Planning scheme must closely integrate with input story ideas or outlines.
- Ensure all planning content conforms to vertical short drama characteristics and user needs.
- Commercial breakpoint design must balance user experience and profit goals.

## Examples

Please refer to `{baseDir}/references/examples.md` for detailed planning examples. This file contains complete planning scheme examples and analysis instructions for various types (such as urban counterattack, sweet romance, suspense mystery, etc.).

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete planning guide and theoretical system
- `examples.md` - More scenario planning examples

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications, added references structure |
| 1.0.0 | 2026-01-10 | Initial version |
