# Agent Skills Perfect Template

> Best practice-based Agent Skills writing template
> Version: 3.0.0
> Update Date: 2026-01-11

---

## I. Frontmatter Best Practices

### 1.1 Complete Frontmatter Template

```yaml
---
name: skill-name                    # Required, 1-64 characters, lowercase letters, numbers, hyphens only
description: Clear description of functionality and use cases. Use "Function. For..." format, 1-1024 characters
category: category-name             # Recommended, for categorization
version: 2.0.0                      # Recommended, semantic versioning
last_updated: 2026-01-11            # Recommended, last update date
license: MIT                        # Optional, recommend MIT
compatibility: Claude Code 1.0+     # Optional, compatibility info
author: Author Name                 # Optional, author info
source: Original Source             # Optional, source info
allowed-tools:                      # Optional, list of allowed tools
  - Read                            # File reading tool
  - Write                           # File writing tool
  - Search                          # Search tool (if needed)
model: sonnet                       # Optional, specify model to use (sonnet/opus/haiku)
disable-model-invocation: false     # Optional, whether to disable model invocation
mode: autonomous                    # Optional, operation mode (autonomous/interactive)
changelog:                          # Recommended, change history
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking              # breaking/added/improved/deprecated/fixed
        content: Restructure according to Agent Skills official specification
      - type: improved
        content: Optimize description, use imperative language, streamline main content
      - type: added
        content: Add license, compatibility optional fields
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---
```

### 1.2 Description Writing Rules

**Format Template**:
```
[Action verb] + [object] + [core functionality description]. For [scenario 1], [scenario 2], [scenario 3]
```

**Good Description Examples**:
- ✅ `Analyze story text, extract main plot points and analyze dramatic functions. For analyzing novels, script outlines, story summaries, etc., identify key turning points and emotional nodes`
- ✅ `Intelligently truncate text, maintaining content completeness and semantic coherence. For long text preprocessing, ensure text doesn't exceed specified length limits`
- ✅ `Analyze IP network information and conduct multi-dimensional evaluation scoring. For evaluating adaptation value of novels, scripts, etc., analyze market potential and innovative attributes`

**Bad Description Examples**:
- ❌ `This skill is used to analyze scripts` (Missing use cases)
- ❌ `Analyze story text` (Too simple, missing scenarios)
- ❌ `This is a very powerful tool that can help users perform various complex analysis tasks` (Too vague, lacks specific functionality)

### 1.3 Imperative Language Specification

| Wrong (Passive/Descriptive) | Correct (Imperative) |
|---------------------------|------------------|
| Should first analyze... | First analyze... |
| Need to extract... | Extract... |
| Suggest user... | Let user... |
| Can consider... | Consider... |
| You can... | ... |
| Should... | ... |

**Standard Verb List**:
- `分析` (Analyze) not `进行分析` (Conduct analysis)
- `提取` (Extract) not `进行提取` (Conduct extraction)
- `生成` (Generate) not `进行生成` (Conduct generation)
- `评估` (Evaluate) not `进行评估` (Conduct evaluation)
- `创作` (Create) not `进行创作` (Conduct creation)
- `优化` (Optimize) not `进行优化` (Conduct optimization)

---

## II. Main Content Structure Template

### 2.1 Standard Structure

```markdown
# Skill Name

## Function

[1-2 sentences clearly describing core functionality, use imperative language]

## Use Cases

- [Scenario 1: Specific description]
- [Scenario 2: Specific description]
- [Scenario 3: Specific description]

## Core Steps / Workflow

1. **Step Name**: [Imperative description, clearly explain operation]
2. **Step Name**: [Imperative description]
3. **Step Name**: [Imperative description]

## Input Requirements

- [Input 1: Specific format, type, requirements]
- [Input 2: Optional input description]
- [Input 3: Parameter description]

## Output Format

```
[Output format template, use code block to display]
```

## Constraints / Requirements

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Examples

### Example 1: [Scenario Name]

**Input**:
```
[Example input content]
```

**Output**:
```
[Example output content]
```

### Example 2: [Another Scenario]

**Input**:
```
[Example input]
```

**Output**:
```
[Example output]
```

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete usage guide
- `examples.md` - More examples
- `troubleshooting.md` - Troubleshooting

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-01-11 | Restructure according to official specification, optimize structure |
| 1.0.0 | 2026-01-10 | Initial version |
```

### 2.2 Content Length Control

**Best Practices**:
- Main SKILL.md file controlled within **5000 words**
- Move detailed content to `references/` directory
- Use progressive information disclosure

**Content Distribution Recommendations**:
- Frontmatter: ~200 tokens
- Function description: ~300 tokens
- Use cases: ~200 tokens
- Core steps: ~500 tokens
- Input/Output: ~400 tokens
- Examples: ~2000 tokens (2-3 examples)
- Other: ~400 tokens

**Total**: ~4000 tokens (approximately 3000 Chinese characters)

---

## III. references/ Directory Structure

### 3.1 Recommended Files

```
references/
├── guide.md              # Complete usage guide (optional)
├── examples.md           # Detailed example collection (recommended)
├── troubleshooting.md    # Troubleshooting guide (optional)
├── api-reference.md      # API reference (if needed)
└── changelog.md          # Detailed change log (optional)
```

### 3.2 references/examples.md Template

```markdown
# [Skill Name] Detailed Examples

## Example 1: [Scenario Name]

### Scenario Description
[Detailed description of use case]

### Input
```
[Complete input example]
```

### Output
```
[Complete output example]
```

### Analysis Notes
[Explain why output this way, key points]

---

## Example 2: [Another Scenario]
[Similar structure]

---

## Common Usage Patterns

### Pattern 1: [Usage Pattern Name]
[Description]

### Pattern 2: [Usage Pattern Name]
[Description]
```

---

## IV. Complete Example: drama-analyzer

```yaml
---
name: drama-analyzer
description: Analyze story text, extract main plot points and analyze dramatic functions. For analyzing novels, script outlines, story summaries, etc., identify key turning points and emotional nodes
category: story-analysis
version: 2.0.0
last_updated: 2026-01-11
license: MIT
compatibility: Claude Code 1.0+
changelog:
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Restructure according to Agent Skills official specification
      - type: improved
        content: Optimize description, use imperative language, streamline main content
      - type: added
        content: Add license, compatibility optional fields
      - type: added
        content: Create references/ directory for detailed examples
  - version: 1.1.0
    date: 2026-01-10
    changes:
      - type: added
        content: Add multi-scenario examples
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---

# Script Analysis Expert

## Function

Analyze story text, extract main plot points and analyze dramatic function of each plot point.

## Use Cases

- Analyze core plot structure of novels or story texts
- Identify key turning points and emotional nodes in stories
- Evaluate dramatic function and driving force of each plot point
- Provide plot analysis foundation for script adaptation

## Core Steps

1. **Deep Reading**: Fully read and understand story text content
2. **Plot Point Extraction**: Summarize main plot points in story based on plot point definition
3. **Dramatic Function Analysis**: Analyze dramatic function of each plot point
4. **Structured Output**: Output analysis results in specified format

## Input Requirements

- Complete story text (novel, script outline, story summary, etc.)
- Recommended text length: 500+ words
- Support multiple text formats: plain text, Markdown, etc.

## Output Format

```
[Plot Point]: <Single plot point description>
[Dramatic Function]: <Dramatic function analysis of this plot point>

[Plot Point]: <Single plot point description>
[Dramatic Function]: <Dramatic function analysis of this plot point>
...
```

## Constraints

- Each plot point description not exceeding 100 words
- Extract at least 5 plot points
- Strictly summarize according to original story text meaning, do not create or adapt
- Do not use Arabic numerals to number plot points
- Avoid hallucinations, do not bring words from prompt into generated answers

## Examples

### Example 1: Suspense Novel Plot Analysis

**Input**:
```
Protagonist Li Ming is a senior reporter who one day receives a mysterious letter claiming to know the truth about his father's accidental death twenty years ago. The letter provides an address and time, requiring him to go alone.

Li Ming goes to the designated location and finds it's an abandoned warehouse. In the warehouse, he finds a diary, the owner of which is his father's colleague before his death. The diary records a shocking secret: father's death was not an accident, but murder.

Just as Li Ming prepares to leave, he suddenly encounters unidentified persons following him. He quickly drives away, but on the way home, discovers his car has been tampered with and the brakes fail.
```

**Output**:
```
[Plot Point]: Protagonist receives mysterious letter claiming to know truth about father's death
[Dramatic Function]: Set suspense hook, trigger audience curiosity, drive protagonist to investigate, establish core driving force of story

[Plot Point]: Protagonist finds diary in abandoned warehouse, discovers truth about father's death
[Dramatic Function]: Reveal core secret, drive plot development, deepen suspense, foreshadow future conflicts

[Plot Point]: Protagonist encounters unidentified persons following, car tampered with
[Dramatic Function]: Create tense atmosphere, escalate conflict, imply secret organization behind, increase urgency and danger
```

### Example 2: Romance Story Plot Analysis

**Input**:
```
[Romance story fragment...]
```

**Output**:
```
[Analysis result...]
```

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `examples.md` - More scenario examples (urban emotional drama, workplace drama, costume drama, etc.)
- `guide.md` - Complete analysis guide and best practices

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-01-11 | Restructure according to official specification, optimize structure, add references directory |
| 1.1.0 | 2026-01-10 | Add multi-scenario examples |
| 1.0.0 | 2026-01-10 | Initial version |
```

---

## V. Checklist

### 5.1 Frontmatter Checklist

- [ ] `name` field contains only lowercase letters, numbers, hyphens, 1-64 characters
- [ ] `description` clearly states function and use cases, 1-1024 characters
- [ ] `description` uses imperative language
- [ ] `category` field added
- [ ] `version` uses semantic versioning
- [ ] `last_updated` date format correct
- [ ] `changelog` structure complete, contains all historical versions
- [ ] `license` added (recommend MIT)
- [ ] `compatibility` added (if applicable)
- [ ] `allowed-tools` added (if needed)
- [ ] `model` added (if needed)

### 5.2 Main Content Checklist

- [ ] Main SKILL.md controlled within 5000 words
- [ ] Use imperative language (avoid "should", "suggest", "can", etc.)
- [ ] Function description clear and concise
- [ ] Use cases specific and clear (at least 3)
- [ ] Core steps clear, use imperative language
- [ ] Input/Output formats clear
- [ ] Include at least 2 complete examples
- [ ] Constraints clear
- [ ] Use path variable `{baseDir}` instead of hardcoded paths
- [ ] Version history table complete

### 5.3 References Checklist

- [ ] `references/` directory created (if needed)
- [ ] `references/examples.md` contains detailed examples (recommended)
- [ ] All paths use `{baseDir}` variable
- [ ] Detailed content moved from main file to references

---

## VI. Common Questions

### Q1: When is the allowed-tools field needed?

**A**: Add when skill needs to call specific tools. For example:
- Need file read/write: `allowed-tools: [Read, Write]`
- Need web search: `allowed-tools: [Search]`
- Text-only processing: Can omit

### Q2: When is the model field needed?

**A**: Add when skill needs specific model capabilities. For example:
- Complex creation tasks: `model: sonnet` or `model: opus`
- Simple analysis tasks: Can omit (use default model)
- Fast processing tasks: `model: haiku`

### Q3: How to decide whether to create references/ directory?

**A**:
- Main SKILL.md over 4000 words: Create references/
- Need multiple detailed examples: Create `references/examples.md`
- Have complex usage guides: Create `references/guide.md`
- Simple skill (<3000 words): Can omit references/

---

## VII. Best Practices Summary

1. **Clarity**: description must clearly state functionality and scenarios
2. **Imperative**: All instructions use imperative language
3. **Conciseness**: Main file controlled within 5000 words
4. **Progressive**: Detailed content in references/
5. **Consistency**: Follow unified format and structure
6. **Maintainability**: Complete version history and changelog
7. **Discoverability**: Clear category and description
8. **Testability**: Include complete examples

---

**Last Update**: 2026-01-11
**Maintainer**: juben project team
