---
name: drama-workflow
description: "Orchestrate the full plot-point dramatic function analysis pipeline — text preprocessing, parallel segment analysis, result integration, and report generation — for long-form story content. Use when analyzing plot points and dramatic functions in long texts, producing structured dramatic analysis reports, or coordinating multi-step story analysis workflows."
allowed-tools: "Read"
license: MIT
compatibility: Claude Code 1.0+
metadata:
  category: workflow
  version: 2.1.0
  last_updated: 2026-01-11
  maintainer: Gong Fan
  model: opus
---

# Plot Point Dramatic Function Analysis Workflow Orchestrator

## Workflow

### Step 1: Text Preprocessing
- Split input text at natural scene or chapter boundaries.
- Target segment size: 2,000–4,000 words with ~200-word overlap between adjacent segments to preserve context continuity.
- **Checkpoint**: verify every paragraph is covered by at least one segment (no gaps).

### Step 2: Parallel Segment Analysis
For each segment, identify:
- **Plot points** — actions or events that change the direction of the story (turning points, revelations, confrontations).
- **Dramatic function** of each plot point — classify as: exposition, rising action, climax, falling action, or resolution.
- Quote or paraphrase the specific text passage supporting each identification.

### Step 3: Result Integration
- Merge plot points from all segments in chronological order.
- Deduplicate plot points that span segment boundaries (same event appearing in overlapping regions).
- **Checkpoint**: confirm the merged list covers the full story arc from opening to ending.

### Step 4: Dramatic Structure Analysis
- Map the merged plot points onto a dramatic arc (tension curve).
- Identify structural patterns: three-act structure, rising/falling tension, parallel storylines.
- Note any structural weaknesses (missing climax, unresolved threads, pacing imbalances).

### Step 5: Report Generation
Assemble findings into the output format below. Include professional insights from a screenwriter perspective.

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

- Minimum input length: text must be long enough to meaningfully split (typically >4,000 words).
- Each plot point must cite or paraphrase supporting text — no unsupported claims.
- Final report must cover the complete story arc with no gaps between segments.

## References

See `{baseDir}/references/examples.md` for worked examples of plot-point dramatic function analysis reports across different text types (long novels, scripts).
