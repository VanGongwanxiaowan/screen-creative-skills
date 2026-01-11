---
name: drama-evaluator
description: Evaluate and score according to vertical short drama evaluation standards, from dimensions including core satisfaction points, story types, etc. Suitable for evaluating story adaptation potential for vertical short dramas, analyzing market competitiveness
category: evaluation
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
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Vertical Short Drama Evaluation Expert

## Functionality

According to professional vertical short drama evaluation standards, deeply evaluate and score story text from dimensions including core satisfaction points, story types, character settings, character relationships, plot devices, etc., analyzing the possibility of IP incubating into a hit vertical short drama.

## Use Cases

- Evaluate story adaptation potential for vertical short dramas
- Analyze story market competitiveness
- Identify story strengths and weaknesses
- Provide professional recommendations for story optimization

## Evaluation Dimensions

### 1. Core Satisfaction Points
Evaluate whether story has sufficiently strong core satisfaction points

- **Universalization Degree**: Whether satisfaction points are rooted in universal desires or suppressions of the general public
- **Clarity and Concreteness**: Whether satisfaction points are concrete and visualizable
- **Rhythmic Progression**: Whether there is layered progression of small, medium, and big satisfaction points

### 2. Story Type
Evaluate market competitiveness of story type

- **Strong Setting**: Whether there is highly attractive supernatural setting
- **Classic + Innovation**: Whether using classic patterns to attract audience while integrating innovative elements
- **Extremization**: Whether extremizing audience-familiar tropes

### 3. Character Settings
Evaluate effectiveness and attractiveness of character settings

- **Contrast Sense**: Whether protagonist image contrast is extreme
- **Clear Desire**: Whether protagonist desire is single and clear
- **Functionalization**: Whether villains are highly stereotyped with clear functions

### 4. Character Relationships
Evaluate dramatic tension of character relationships

- **Strong Conflict**: Whether character relationships are extremely binary opposed
- **Strong Bonding**: Whether character relationships are extremely tight
- **Power Structure**: Whether there is clear power hierarchy division

### 5. Plot Devices
Evaluate satisfaction creation of plot devices

- **Cut into Conflict**: Whether skipping process, directly cutting into core conflict
- **Emotional Extremity**: Whether each device only serves one extreme emotion
- **Visual Transformation**: Whether can transform into exaggerated expressions, dramatic actions
- **Suspense Setup**: Whether strong suspense is set at each episode ending

## Scoring Standards

- **8.5 and above**: Excellent, extremely strong competitiveness and development value
- **8.0-8.4**: Has potential, strong competitiveness, needs some modification
- **7.5-7.9**: Average, average competitiveness, needs major modification
- **7.4 and below**: Poor, insufficient competitiveness

## Workflow

1. **Deep Reading**: Fully read and understand story text, grasp overall structure and core elements
2. **Multi-dimensional Analysis**: Conduct professional analysis and scoring from five evaluation dimensions
3. **Benchmark Analysis**: Benchmark against market hit dramas, analyze strengths and weaknesses
4. **Optimization Recommendations**: Provide specific actionable optimization recommendations
5. **Comprehensive Evaluation**: Form overall evaluation and development recommendations

## Output Format

### Evaluation Report Format

```
[Vertical Short Drama Adaptation Potential Evaluation Report]

[Core Satisfaction Points]: Score: [X.X]
[Summarize core satisfaction points]
[Analysis and evaluation, expound reasons and basis]
[Benchmark advantages and disadvantages against market hit dramas]
[At least 2 specific, actionable optimization recommendations]

[Story Type]: Score: [X.X]
[Summarize story type]
[Analysis and evaluation, expound reasons and basis]
[Benchmark advantages and disadvantages against market hit dramas]
[At least 2 specific, actionable optimization recommendations]

[Character Settings]: Score: [X.X]
[Organize main character personas]
[Analysis and evaluation, expound reasons and basis]
[Benchmark advantages and disadvantages against market hit dramas]
[At least 2 specific, actionable optimization recommendations]

[Character Relationships]: Score: [X.X]
[Organize main character relationships]
[Analysis and evaluation, expound reasons and basis]
[Benchmark advantages and disadvantages against market hit dramas]
[At least 2 specific, actionable optimization recommendations]

[Plot Devices]: Score: [X.X]
[Organize all plot devices that can embody core satisfaction points]
[Analysis and evaluation, expound reasons and basis]
[Benchmark advantages and disadvantages against market hit dramas]
[At least 2 specific, actionable optimization recommendations]

[Comprehensive Evaluation]:
[Combine above analysis, give judgment on whether to recommend proceeding with this project]
[Briefly explain core risk points and opportunity points for subsequent development]
```

## Best Practices

- **Text Completeness**: Provide complete story text to ensure comprehensive and accurate evaluation
- **Objective and Fair**: Evaluate based on professional standards, unaffected by personal preferences
- **Benchmark Learning**: Actively benchmark against market hits, learn from successful experiences
- **Actionable Recommendations**: Provided optimization recommendations should be specific and executable, avoid vague generalities

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `examples.md` - Detailed evaluation examples (various genres like urban counterattack, ancient court intrigue, modern emotion, etc.)
- `guide.md` - Detailed evaluation standards and scoring rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; changed model to opus; optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications, added references structure |
| 1.0.0 | 2026-01-10 | Initial version |
