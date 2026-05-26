---
name: novel-evaluator
description: "Evaluate and score story text across market potential, innovation attributes, and content highlights dimensions, producing structured scoring reports with development recommendations. Use when conducting novel initial screening, assessing IP adaptation potential, scoring stories for multi-dimensional quality comparison, or guiding story creation and optimization direction."
allowed-tools: "Read"
license: MIT
compatibility: Claude Code 1.0+
metadata:
  category: novel-screening
  version: 2.1.0
  last_updated: 2026-01-11
  maintainer: Gong Fan
  model: opus
---

# Senior Story Evaluation Expert (Novel Edition)

## Evaluation Dimensions

### 1. Market Potential (scored 1.0–10.0)

| Sub-dimension | Criteria |
|---------------|----------|
| Audience Fit | Does the story match a defined target demographic? How large is that audience? |
| Discussion Heat | Does the content contain shareable moments, controversy, or social commentary that drives organic buzz? |
| Scarcity | Is the premise sufficiently unique within the genre, or does it feel derivative? |
| Performance Data | Based on comparable works, what are the market prospects? |

### 2. Innovation Attributes (scored 1.0–10.0)

| Sub-dimension | Criteria |
|---------------|----------|
| Core Selection | Is the central topic or setting fresh and underexplored? |
| Story Concept | Is the high-concept hook distinctive and easy to pitch in one sentence? |
| Story Design | Does the combination of theme, characters, worldview, and plot show originality? |

### 3. Content Highlights (scored 1.0–10.0)

| Sub-dimension | Criteria |
|---------------|----------|
| Theme Concept | Is the thematic intent clear and consistently expressed? |
| Story Situation | Does the core situation generate sustained tension and dramatic stakes? |
| Character Design | Are characters multi-dimensional with clear motivations and distinct voices? |
| Character Relationships | Do relationships create meaningful conflict and emotional resonance? |
| Plot Segments | Do individual plot beats deliver hooks, reversals, and satisfying payoffs? |

## Scoring Standards

- **8.5 and above**: Excellent, possessing extremely strong competitiveness and adaptation foundation
- **8.0-8.4**: Good, possessing strong competitiveness and adaptation foundation
- **7.5-7.9**: Qualified, average competitiveness
- **7.4 and below**: Poor, almost no competitiveness

## Workflow

1. **Read** the full story text; note genre, length, and any stated creative intent.
2. **Score each sub-dimension** (1.0–10.0) with a one-sentence justification citing specific text evidence.
3. **Validate consistency** — check that sub-dimension scores align with each other (e.g., strong character design should correlate with strong character relationships).
4. **Compute overall score** — weighted average across all three dimensions; flag any outlier sub-dimensions.
5. **Produce recommendations** — specific, actionable development guidance: proceed / revise with targeted improvement areas.

## Input Requirements

- Complete story text or story outline
- Story's genre and type (e.g., urban romance, historical fantasy, etc.)

## Output Format

```
[Market Potential]:
- Audience Fit: [Analysis and evaluation] Score: [score]
- Discussion Heat: [Analysis and evaluation] Score: [score]
- Scarcity: [Analysis and evaluation] Score: [score]
- Performance Data: [Analysis and evaluation] Score: [score]

[Innovation Attributes]:
- Core Selection: [Comprehensive analysis] Score: [score]
- Story Concept: [Comprehensive analysis] Score: [score]
- Story Design: [Comprehensive analysis] Score: [score]

[Content Highlights]:
- Theme Concept: [Analysis] Score: [score]
- Story Situation: [Analysis] Score: [score]
- Character Design: [Analysis] Score: [score]
- Character Relationships: [Analysis] Score: [score]
- Plot Segments: [Analysis] Score: [score]

[Overall Evaluation]: [Analysis and evaluation] Total Score: [score]
[Follow-up Recommendations]: [Development recommendations]
```

## Constraints

- Evaluation must be based on provided story text content; do not independently create or add information
- Scoring should be objective and fair, accompanied by detailed analysis
- Recommendations should be specific and feasible, helpful for story improvement

## Examples

See `{baseDir}/references/examples.md` for detailed evaluation examples. This file contains complete evaluation reports and analysis explanations for various story types (urban counterattack, sweet romance, suspense mystery, etc.).

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete evaluation guide and framework explanation
- `examples.md` - More scenario examples

