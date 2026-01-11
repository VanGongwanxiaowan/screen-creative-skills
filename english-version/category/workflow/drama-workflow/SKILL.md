---
name: drama-workflow
description: Coordinate plot point dramatic function analysis process, manage text preprocessing, parallel analysis, result integration. Suitable for plot point and dramatic function analysis of long texts, scenarios requiring structured analysis reports
category: workflow
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools:
  - Read
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
        content: Added allowed-tools (Read) and model fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Plot Point Dramatic Function Analysis Workflow Orchestrator

## Functionality

Coordinate entire plot point dramatic function analysis process, manage text preprocessing, parallel analysis, result integration, and report generation.

## Use Cases

- Conduct plot point and dramatic function analysis on long story texts.
- Need high-quality, professional dramatic analysis reports.
- Need to obtain structured analysis results.

## Workflow Steps

1. **Text Preprocessing**: Truncate and split long text to ensure text is suitable for subsequent analysis.
2. **Parallel Analysis**: Perform plot point analysis on text segments to improve analysis efficiency.
3. **Result Integration**: Merge and optimize analysis results to ensure result consistency.
4. **Report Generation**: Generate final comprehensive analysis report.

## Orchestration Principles

- Ensure correct input-output transmission.
- Manage context isolation between agents.
- Optimize parallel processing performance.
- Guarantee completeness and accuracy of analysis results.

## Input Requirements

- Long text story content.
- Analysis requirement description (optional).

## Output Format

```
[Plot Point Dramatic Function Analysis Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Analysis Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Text Length: [Word count]
- Number of Segments: [Count]
- Total Plot Points: [Count]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Plot Point Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Plot Point 1]: [Description]
[Dramatic Function]: [Analysis]

[Plot Point 2]: [Description]
[Dramatic Function]: [Analysis]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Dramatic Structure Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Overall dramatic structure analysis]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. Professional Insights
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Professional insights from screenwriter perspective]
```

## Constraints

- Input text length must meet segmentation processing requirements.
- Ensure independence and accuracy of each plot point analysis.
- Final report must have clear logic and definite conclusions.

## Examples

Please refer to `{baseDir}/references/examples.md` for detailed workflow examples. This file contains plot point dramatic function analysis reports for different text types such as long novels, scripts, etc.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field, added allowed-tools and model fields, adjusted main content language style, added constraints, and directed to references/examples.md |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
