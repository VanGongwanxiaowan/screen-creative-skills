---
name: web-search
description: Use web search to get latest market information and industry trends. Suitable for getting vertical short drama market trends, hot topic analysis, success case research
category: knowledge-research
version: 2.1.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
maintainer: Gong Fan
allowed-tools:
  - WebSearch
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
        content: Optimized descriptions for functionality, usage scenarios, core steps, input requirements, and output format to comply with imperative language standards
      - type: added
        content: Added constraints, examples, and detailed documentation sections
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Restructured according to Agent Skills official specifications
      - type: improved
        content: Optimized description, used imperative language, streamlined main content
      - type: added
        content: Added license and compatibility optional fields
      - type: added
        content: Added allowed-tools (WebSearch) and model fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Vertical Short Drama Web Search Expert

## Functionality

Use web search capabilities to get latest market information and industry trends, providing accurate web search and information retrieval services.

## Usage Scenarios

- Get vertical short drama market trend analysis
- Research hot topics and success cases
- Track industry policies and platform algorithm changes
- Collect content creation and commercial operation techniques

## Core Capabilities

1. **Web Search**: Conduct accurate web searches to get latest market information and industry trends
2. **Information Organization**: Intelligently classify and organize search results, extracting key information and core points
3. **Content Summary**: Deeply analyze and summarize search results, providing practical recommendations and insights

## Workflow

1. **Execute Search**: Build precise queries based on user needs and conduct web searches
2. **Intelligent Summary**: Analyze search result relevance and importance, generating structured summary reports

## Specialized Areas

### Vertical Short Drama Market
- Market trends and user preference analysis
- Hit short drama case studies
- Platform policies and algorithm changes
- Production cost and revenue analysis

### Content Creation
- Hot topics and element analysis
- Creation techniques and methodologies
- Character design and plot design

### Commercial Operations
- Marketing strategies and promotion methods
- User growth and retention techniques
- Monetization models and profit analysis

## Input Requirements

- Clear web search keywords or questions
- Optionally specify search scope

## Output Requirements

- Clear titles and categories
- Complete time background and context
- Accurate citation of key data
- Practical recommendations and action guides

## Constraints

- Search results must come from the web; do not query knowledge base
- Information organization must be objective and accurate; avoid subjective commentary
- Output content should be structured and easy to understand and apply

## Examples

See `{baseDir}/references/examples.md` for detailed examples. This file contains complete outputs and analysis explanations for various web search scenarios.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field; changed model to opus; optimized descriptions for functionality, usage scenarios, core steps, input requirements, and output format; added constraints, examples, and detailed documentation sections |
| 2.0.0 | 2026-01-11 | Restructured according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
