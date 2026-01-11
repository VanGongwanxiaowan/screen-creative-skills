---
name: character-profile
description: Analyze character traits based on story text and generate detailed character biographies. Suitable for deeply understanding story character settings, providing references for actors to shape characters, and establishing character profiles for script creation
category: character-analysis
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
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Character Biography Generation Expert

## Functionality

Analyze character traits based on story text and generate detailed character biographies, including basic information, personality characteristics, background stories, character relationships, and their role in the story.

## Use Cases

- Deeply understand character settings in stories
- Provide references for actors to shape characters
- Establish character profiles for script creation
- Provide materials for character design

## Core Steps

1. **Text Analysis**: Carefully read and analyze story text, extract all information related to characters
2. **Feature Extraction**: Systematically extract basic information, appearance characteristics, identity background of characters
3. **Personality Analysis**: Deeply analyze character personality traits, behavior patterns, and language styles
4. **Relationship Organization**: Organize the relationship network between characters and other characters, understand relationship types and development
5. **Role Positioning**: Analyze the character's functional positioning in the story, plot-driving role, and thematic expression role
6. **Biography Generation**: Integrate all information to generate a structurally complete and detailed character biography

## Input Requirements

- Complete story text containing character information
- Can specify the name of the character to be analyzed
- Recommended text length: 500+ words

## Output Format

```
[Character Biography: Character Name]

I. Basic Information
- Name: [Character Name]
- Age: [Age]
- Identity: [Identity/Occupation]
- Appearance: [Appearance Description]

II. Personality Characteristics
- Main Personality: [Personality Description]
- Behavioral Characteristics: [Behavior Description]
- Language Characteristics: [Language Style Description]

III. Background Story
- Family Background: [Family Situation]
- Growth Experience: [Growth Process]
- Important Experiences: [Important Events]

IV. Character Relationships
- Relationships with Main Characters: [Relationship Description]
- Character Relationship Network: [Overall Relationship Description]

V. Role in the Story
- Functional Positioning: [Function in the Story]
- Plot Driving: [How to Drive the Plot]
- Thematic Expression: [How to Express the Theme]
```

## Constraints

- Strictly analyze characters based on story text content, do not create character information on your own
- Maintain consistency in character descriptions
- Ensure character descriptions are based on actual text content

## Examples

### Example: Analyze Protagonist Character Biography

**Input**:
```
Please generate a character biography for the protagonist in the following story:
[Story about workplace woman Lin Qian...]
```

**Output**:
```
[Character Biography: Lin Qian]

I. Basic Information
- Name: Lin Qian
- Age: 28
- Identity: Advertising Company Planning Manager
- Appearance: Tall and slender, capable temperament, determined eyes

II. Personality Characteristics
- Main Personality: Independent and self-reliant, persevering, outwardly cold but inwardly warm
- Behavioral Characteristics: Decisive in action, pursuing perfection, not easily showing weakness
- Language Characteristics: Concise and comprehensive, hitting the key points, sometimes slightly sharp

III. Background Story
- Family Background: Ordinary family in a small city, parents are teachers
- Growth Experience: Excellent grades since childhood, got into a prestigious university in Beijing through own efforts
- Important Experiences: After graduating from university, ventured to Beijing alone, rose from intern to Planning Manager

IV. Character Relationships
- With Lu Yuan: Developed from competitors to lovers
- With Xiao Li: Colleagues and friends, support each other
- With Manager Zhang: Supervisor-subordinate relationship, also mentor and friend

V. Role in the Story
- Functional Positioning: Core driver of the story
- Plot Driving: Drives plot development through her choices and actions
- Thematic Expression: Showcases the spirit of independent and self-reliant modern women
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-11 | Optimized description field to be more concise and comply with imperative language specifications; changed model to opus; optimized descriptions of functionality, use cases, core steps, input requirements, and output format to comply with imperative language specifications; added constraints, examples, and detailed documentation sections. |
| 2.0.0 | 2026-01-11 | Refactored according to official specifications |
| 1.0.0 | 2026-01-10 | Initial version |
