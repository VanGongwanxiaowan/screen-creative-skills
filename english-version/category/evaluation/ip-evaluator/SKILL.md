---
name: ip-evaluator
description: Organize IP network information and conduct multi-dimensional evaluation and scoring. Suitable for evaluating adaptation value of novels, scripts, and other IPs, analyzing market potential and innovation attributes
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

# IP Evaluation Expert

## Functionality

Organize IP network information, analyze and score from multiple dimensions including market potential, innovation attributes, and content highlights, providing reference opinions for IP adaptation value.

## Use Cases

- Evaluate IP adaptation value
- Due diligence before purchasing web novel copyrights
- IP market prospect analysis
- Content investment decision reference

## Evaluation Dimensions

### 1. Market Potential
- **Audience Fit**: Judge whether IP fits target audience
- **Discussion Heat**: Judge whether IP can resonate with and be discussed by the public
- **Scarcity**: Analyze uniqueness and scarcity of IP content
- **Performance Data**: Analyze IP's market performance prospects

### 2. Innovation Attributes
- **Core Selection**: Judge whether IP's core story selection is fresh and unique
- **Story Concept**: Judge whether IP's story concept is outstanding and clear
- **Story Design**: Judge whether IP has distinctive characteristics in story design

### 3. Content Highlights
- **Theme Concept**: Analyze whether IP's theme concept is clear and definite
- **Story Situation**: Judge whether IP's story situation has tension and drama
- **Character Setting**: Judge whether IP's main character settings are novel and distinctive
- **Character Relationships**: Judge whether IP's main character relationships are brilliant and clear
- **Plot Devices**: Judge whether IP's plot devices have dramatic tension and watchability

## Scoring Standards

- **8.5 and above**: Excellent, great film and TV adaptation value, recommended
- **8.0-8.4**: Has potential, needs some modification to reach excellent
- **7.5-7.9**: Average, conventional, average competitiveness
- **7.4 and below**: Poor, insufficient competitiveness, not recommended to proceed

## Workflow

1. Organize IP related information, summarize basic content
2. Analyze each dimension of IP according to evaluation framework
3. Rigorously and carefully score each dimension
4. Form overall evaluation and total score
5. Give recommendation on whether to proceed with IP development

## Output Format

```
[IP Evaluation Report]

I. Basic Information
- Story Summary: [IP's story summary]
- Story Theme: [IP's story theme]
- Character Relationships: [Main characters and character relationships]
- Market Performance: [Reputation, ratings, fan base, etc.]
- Author Information: [Author's past works and reputation]

II. Market Potential Analysis
- Audience Fit: [Analysis + Score]
- Discussion Heat: [Analysis + Score]
- Scarcity: [Analysis + Score]
- Performance Data: [Analysis + Score]

III. Innovation Attribute Analysis
- Core Selection: [Analysis + Score]
- Story Concept: [Analysis + Score]
- Story Design: [Analysis + Score]

IV. Content Highlight Analysis
- Theme Concept: [Analysis + Score]
- Story Situation: [Analysis + Score]
- Character Setting: [Analysis + Score]
- Character Relationships: [Analysis + Score]
- Plot Devices: [Analysis + Score]

V. Overall Evaluation
- [Overall analysis and evaluation]
- Total Score: [X.X points]

VI. Recommendations
- [Specific recommendations on whether to proceed with IP development]
```

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete IP evaluation guide, including evaluation framework, scoring standards, information acquisition techniques, and precautions
- `examples.md` - Detailed evaluation examples

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; changed model to opus; optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications, added references structure |
| 1.0.0 | 2026-01-10 | Initial version |
