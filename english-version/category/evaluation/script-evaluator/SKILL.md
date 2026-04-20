---
name: script-evaluator
description: "Evaluate film and TV scripts across ideological, artistic, and entertainment value dimensions, producing structured scoring reports with follow-up recommendations. Use when assessing script development quality, determining modification direction, reviewing scripts before project approval, or benchmarking screenwriter capabilities."
allowed-tools: "Read, Write"
license: MIT
compatibility: Claude Code 1.0+
metadata:
  category: evaluation
  version: 2.1.0
  last_updated: 2026-01-11
  maintainer: Gong Fan
  model: opus
---

# Film and TV Script Evaluation Expert

## Functionality

Deeply read film and TV scripts, conduct professional evaluation and scoring from three dimensions: ideological, artistic, and entertainment value.

## Evaluation Dimensions

### 1. Ideological Value (Positive / Neutral / Negative)

| Sub-dimension | Criteria |
|---------------|----------|
| Values | Does the script promote a constructive value orientation? |
| Social Significance | Does the story reflect meaningful social reality? |

### 2. Artistic Value (Excellent / Acceptable / Lacking)

| Sub-dimension | Criteria |
|---------------|----------|
| Detail Portrayal | Specificity and vividness of scenes, actions, and objects |
| Creativity | Originality of premise, structure, or storytelling device |
| Narrative Logic | Cause-and-effect consistency across plot events |
| Narrative Techniques | Effective use of foreshadowing, flashback, parallel storylines |
| Narrative Rhythm | Pacing balance — tension build-up vs. release across acts |
| Dialogue Expression | Character voice distinctiveness, subtext, and economy of words |

### 3. Entertainment Value (scored 1.0–10.0)

| Sub-dimension | Criteria |
|---------------|----------|
| Audience Base | Alignment with target demographic expectations and genre conventions |
| Topicality | Relevance to current cultural trends or evergreen themes |
| Genre Style | Consistency and effective use of genre tropes |
| Character Shaping | Depth, arc, and memorability of characters |
| Character Relationships | Dynamic tension and evolution of interpersonal bonds |
| Plot Devices | Effectiveness of hooks, reversals, and climax construction |

## Scoring Standards

- **8.5 and above**: Excellent, has strong competitiveness and film and TV development value.
- **8.0-8.4**: Good, has strong competitiveness and film and TV development value.
- **7.5-7.9**: Qualified, average competitiveness.
- **7.4 and below**: Poor, almost no competitiveness.

## Workflow

1. **Read** the full script; note genre, target audience, and stated creative intent.
2. **Score Ideological Value** — classify as positive/neutral/negative with evidence from the text.
3. **Score Artistic Value** — rate each of the six sub-dimensions (1.0–10.0) with one-sentence justification per score.
4. **Score Entertainment Value** — rate each of the six sub-dimensions (1.0–10.0) with one-sentence justification per score.
5. **Validate consistency** — confirm sub-dimension scores align with the overall assessment; flag contradictions.
6. **Produce Overall Score and Recommendations** — weighted average of artistic and entertainment scores; provide specific, actionable next steps (proceed / revise with targeted notes).

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

