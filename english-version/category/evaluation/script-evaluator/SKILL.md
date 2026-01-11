---
name: script-evaluator
description: Evaluate film and TV scripts from three dimensions: ideological, artistic, and entertainment value. Suitable for script development quality assessment, modification direction determination, pre-project approval review
category: evaluation
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools:
  - Read
  - Write
model: opus
changelog:
  - version: 2.1.0
    date: 2026-01-11
    changes:
      - type: improved
        content: Optimized description field to be more concise and comply with imperative language specifications
      - type: added
        content: Added allowed-tools (Read, Write) and model (opus) fields
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Refactored according to Agent Skills official specifications
      - type: improved
        content: Optimized description, using imperative language, simplified main content
      - type: added
        content: Added license and compatibility optional fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Film and TV Script Evaluation Expert

## Functionality

Deeply read film and TV scripts, conduct professional evaluation and scoring from three dimensions: ideological, artistic, and entertainment value.

## Use Cases

- Conduct quality assessment during script development.
- Determine script modification direction.
- Review scripts before film and TV project approval.
- Evaluate and improve screenwriter capabilities.

## Evaluation Dimensions

### 1. Ideological Value
Evaluate whether script's ideological value belongs to "positive," "neutral," or "negative."

- **Values**: Analyze whether script has correct value orientation.
- **Social Significance**: Analyze whether script has social significance that reflects reality.

### 2. Artistic Value
Evaluate whether script's artistic value belongs to "excellent," "acceptable," or "lacking."

- **Detail Portrayal**: Evaluate detail portrayal of script content.
- **Creativity Presentation**: Evaluate creativity presentation in script.
- **Narrative Logic**: Evaluate script's narrative logic.
- **Narrative Techniques**: Evaluate narrative techniques used in script.
- **Narrative Rhythm**: Evaluate script's narrative rhythm.
- **Dialogue Expression**: Evaluate character dialogue in script.

### 3. Entertainment Value
Combined with scoring standards, score overall entertainment value of script content.

- **Audience Base**: Evaluate whether script content matches target audience.
- **Topicality**: Evaluate script's themes and topics.
- **Genre Style**: Evaluate script's genre style.
- **Character Shaping**: Evaluate script's character shaping.
- **Character Relationships**: Evaluate script's character relationships.
- **Plot Devices**: Evaluate script's plot devices.

## Scoring Standards

- **8.5 and above**: Excellent, has strong competitiveness and film and TV development value.
- **8.0-8.4**: Good, has strong competitiveness and film and TV development value.
- **7.5-7.9**: Qualified, average competitiveness.
- **7.4 and below**: Poor, almost no competitiveness.

## Core Steps

1. **Deep Reading**: Deeply read script, form independent understanding.
2. **Ideological Evaluation**: Evaluate script's values and social significance.
3. **Artistic Evaluation**: Evaluate each artistic dimension of script.
4. **Entertainment Evaluation**: Evaluate each entertainment dimension of script.
5. **Overall Evaluation**: Combine three dimensions to form overall evaluation.
6. **Provide Recommendations**: Provide recommendations for proceeding or modification.

## Input Requirements

- Complete film and TV script or script segments
- Script type and genre (such as: urban emotion, ancient fantasy, etc.)

## Output Format

```
[Script Evaluation Report]

[Ideological Value]: [Overall Qualification]
- Values: [Analysis and Evaluation]
  Qualification: [Positive/Neutral/Negative]

- Social Significance: [Analysis and Evaluation]
  Qualification: [Positive/Neutral/Negative]

[Artistic Value]: [Overall Qualification]
- Detail Portrayal: [Analysis and Evaluation] Score: [X.X]
- Creativity Presentation: [Analysis and Evaluation] Score: [X.X]
- Narrative Logic: [Analysis and Evaluation] Score: [X.X]
- Narrative Techniques: [Analysis and Evaluation] Score: [X.X]
- Narrative Rhythm: [Analysis and Evaluation] Score: [X.X]
- Dialogue Expression: [Analysis and Evaluation] Score: [X.X]

[Entertainment Value]:
- Audience Base: [Analysis and Evaluation] Score: [X.X]
- Topicality: [Analysis and Evaluation] Score: [X.X]
- Genre Style: [Analysis and Evaluation] Score: [X.X]
- Character Shaping: [Analysis and Evaluation] Score: [X.X]
- Character Relationships: [Analysis and Evaluation] Score: [X.X]
- Plot Devices: [Analysis and Evaluation] Score: [X.X]

[Overall Evaluation]: Score: [X.X]
[Overall analysis and evaluation]

[Follow-up Recommendations]: [Proceed recommendations or modification recommendations]
```

## Constraints

- Evaluation must be based on provided script content, do not create or add information on your own.
- Scoring should be objective and fair, accompanied by detailed analysis.
- Recommendations should be specific and feasible, helping script improvement.

## Examples

Please refer to `{baseDir}/references/examples.md` for detailed evaluation examples. This file contains complete evaluation reports and analysis instructions for various script types (such as urban emotion dramas, sci-fi films, ancient dramas, etc.).

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete guide to film and TV script evaluation, including evaluation framework, scoring standards, evaluation process, and precautions
- `examples.md` - Detailed evaluation examples

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field, added allowed-tools and model fields, adjusted main content language style, added constraints, and directed to references/examples.md |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
