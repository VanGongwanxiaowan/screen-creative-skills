# Agent Skills Optimization Guide

> Optimization guide based on official Agent Skills specification
> Document Version: 1.0
> Update Date: 2026-01-11

---

## I. Agent Skills Official Specification Essentials

### 1.1 Frontmatter Specification

**Required Fields** (Only 2):
```yaml
---
name: skill-name              # Required, 1-64 characters, lowercase letters, numbers, hyphens only
description: Clear description # Required, 1-1024 characters, describe function + use cases
---
```

**Optional Fields**:
```yaml
---
license: Apache-2.0                    # License
compatibility: Claude Code 1.0+        # Compatibility info
metadata:                              # Additional metadata (recommend keeping lean)
  author: Author Name
  source: Original Source
allowed-tools:                         # List of allowed tools
  - Read
  - Write
model: sonnet                          # Specify model to use
disable-model-invocation: false        # Whether to disable model invocation
mode: autonomous                       # Operation mode
---
```

### 1.2 Description Best Practices

**Good Descriptions**:
- Clearly state "what" (function)
- Clearly state "when to use" (use cases)
- Keep concise, 1-1024 characters
- Use action-oriented language

**Example Comparison**:

| Type | Example | Evaluation |
|------|---------|------------|
| Poor | `This skill is used to analyze scripts` | Missing use cases |
| Medium | `Analyze story text, extract plot points and analyze dramatic functions` | Has function but scenarios unclear |
| Excellent | `Deeply analyze story text, extract main plot points and analyze dramatic function of each plot point. For analyzing novels, script outlines, story summaries, etc., identify key turning points and emotional nodes` | Function + scenarios clear |

### 1.3 Content Length Optimization

**Recommended Practices**:
- Control main SKILL.md file within **5000 words**
- Use "Progressive Disclosure"
  1. **Frontmatter**: ~100 tokens, for skill discovery
  2. **Main Content**: ~<5000 words, contains core instructions
  3. **External References**: Detailed documentation in `references/` subdirectory

**External Reference Format**:
```markdown
## Detailed Documentation

See `references/` directory:
- `detailed-guide.md` - Complete usage guide
- `examples.md` - More examples
- `troubleshooting.md` - Troubleshooting
```

### 1.4 Language Style - Imperative

**Use Imperative Language**:

| Avoid (Wrong) | Use (Correct) |
|----------------|--------------|
| You should first analyze... | First analyze... |
| We need... | Analyze... |
| Suggest user... | Let user... |
| Can consider... | Consider... |

**Standard Verbs**:
- `分析` (Analyze) not `进行分析` (Conduct analysis)
- `提取` (Extract) not `进行提取` (Conduct extraction)
- `生成` (Generate) not `进行生成` (Conduct generation)
- `评估` (Evaluate) not `进行评估` (Conduct evaluation)

### 1.5 Path Variable Specification

**Must use path variables**, prohibit hardcoded paths:

| Wrong (Hardcoded) | Correct (Variable) |
|-------------------|-------------------|
| `/Users/gongfan/juben/skills/...` | `{baseDir}/...` |
| `C:\Users\Name\project\...` | `{baseDir}/...` |
| `./references/guide.md` | `{baseDir}/references/guide.md` |

**Available Path Variables**:
- `{baseDir}` - Skill root directory
- `{cwd}` - Current working directory

---

## II. Optimization Checklist

### 2.1 Frontmatter Check

- [ ] `name` field contains only lowercase letters, numbers, hyphens
- [ ] `name` length 1-64 characters
- [ ] `description` clearly states function and use cases
- [ ] `description` length 1-1024 characters
- [ ] Add `category` field for categorization
- [ ] Add `version` field for version management
- [ ] Consider adding `license` and `compatibility`

### 2.2 Content Optimization Check

- [ ] Main SKILL.md controlled within 5000 words
- [ ] Use imperative language
- [ ] Remove redundant "please", "can", etc. polite language
- [ ] Move detailed documentation to `references/` directory
- [ ] Use path variables instead of hardcoded paths
- [ ] Keep structure clear, use progressive information disclosure

### 2.3 Version Management Check

- [ ] Add `version` field
- [ ] Add `last_updated` field
- [ ] Add `changelog` array recording change history
- [ ] Add version history table at end of document

---

## III. Optimization Template

### 3.1 Concise SKILL.md Template

```yaml
---
name: skill-name
description: Concisely describe function and use cases, 1-2 sentences clearly, control within 100-150 characters
category: category-name
version: 1.0.0
last_updated: 2026-01-11
changelog:
  - version: 1.0.0
    date: 2026-01-11
    changes:
      - type: added
        content: Initial version
---

# Skill Name

## Function

[1-2 sentences describing core function]

## Use Cases

- [Scenario 1]
- [Scenario 2]

## Core Steps

1. **Step Name**: [Imperative description]
2. **Step Name**: [Imperative description]
3. **Step Name**: [Imperative description]

## Input Requirements

- [Input 1]
- [Input 2]

## Output Format

```
[Output format template]
```

## Examples

### Example 1: [Scenario Name]

**Input**: [Example input]

**Output**:
```
[Example output]
```

## Detailed Documentation

See `{baseDir}/references/` directory for more documentation:
- `guide.md` - Complete usage guide
- `examples.md` - More examples
- `changelog.md` - Change history

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-11 | Initial version |
```

### 3.2 Description Writing Template

```
[Action] + [Object] + [Purpose/Result]. For/Used in [Use Case 1], [Use Case 2], [Use Case 3]
```

**Example**:
```
Analyze story text, extract main plot points and analyze dramatic function of each plot point. For analyzing novels, script outlines, story summaries, etc., identify key turning points and emotional nodes in stories
```

---

## IV. Optimization Implementation Plan

### 4.1 Phase 1: Frontmatter Optimization

1. Optimize `description` field for all 31 skills
2. Ensure all `name` comply with naming specification
3. Add standardized version and changelog

### 4.2 Phase 2: Content Simplification

1. Move detailed guides to `references/` directory
2. Simplify main SKILL.md content
3. Rewrite instructions using imperative language

### 4.3 Phase 3: Structure Optimization

1. Uniformly use path variables
2. Create references directory structure
3. Update documentation references

---

## V. Current Skills Status Analysis

### 5.1 Items Needing Optimization

| Issue | Scope | Priority |
|-------|-------|----------|
| Description too verbose | All 31 | High |
| Use non-imperative language | All 31 | High |
| Missing optional fields | All 31 | Medium |
| Content may exceed 5000 words | Some complex skills | Medium |
| Missing references structure | All 31 | Low |

### 5.2 Optimization Priority

**Batch 1** (High Priority - Core Analysis Class):
- drama-analyzer
- plot-keypoints
- story-type-analyzer
- story-five-elements

**Batch 2** (Medium Priority - Evaluation and Creation Class):
- ip-evaluator
- drama-evaluator
- drama-creator
- drama-planner

**Batch 3** (Standard Priority - Remaining Skills):
- Remaining 23 skills

---

## VI. Optimization Examples

### Example: Before vs After Optimization

#### Before Optimization (drama-analyzer):

```yaml
---
name: drama-analyzer
description: Deeply analyze story text, extract main plot points and analyze dramatic function of each plot point
category: story-analysis
version: 1.1.0
last_updated: 2026-01-10
changelog:
  - version: 1.1.0
    date: 2026-01-10
    changes:
      - type: added
        content: Add urban emotional drama, suspense drama, workplace drama multi-scenario examples
      - type: improved
        content: Improve usage examples and output format description
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version, convert from agent prompt to skill
---

# Script Analysis Expert

## Function Description
Based on professional screenwriter's perspective, deeply analyze story text content...
[Lots of content...]
```

#### After Optimization:

```yaml
---
name: drama-analyzer
description: Analyze story text, extract main plot points and analyze dramatic functions. For analyzing novels, script outlines, story summaries, etc., identify key turning points and emotional nodes
category: story-analysis
version: 2.0.0
last_updated: 2026-01-11
changelog:
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: Restructure according to Agent Skills official specification
      - type: improved
        content: Optimize description, simplify main content, move detailed documentation to references/
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

## Output Format

```
[Plot Point]: <Single plot point description>
[Dramatic Function]: <Dramatic function analysis of this plot point>
```

## Requirements

- Each plot point description not exceeding 100 words
- Extract at least 5 plot points
- Strictly summarize according to original story text meaning, do not create or adapt
- Do not use Arabic numerals to number plot points

## Examples

### Example: Suspense Novel Plot Analysis

**Input**:
```
[Suspense novel fragment...]
```

**Output**:
```
[Plot Point]: Protagonist receives mysterious letter claiming to know truth about father's death
[Dramatic Function]: Set suspense hook, trigger audience curiosity, drive protagonist investigation

[Plot Point]: Protagonist encounters unidentified persons tracking during investigation
[Dramatic Function]: Create tense atmosphere, imply secret organization behind, escalate conflict
```

## Detailed Documentation

See `{baseDir}/references/` for more documentation:
- `guide.md` - Complete analysis guide
- `examples.md` - Multi-scenario examples
- `terminology.md` - Term definitions

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-01-11 | Restructure according to official specification, optimize structure |
| 1.1.0 | 2026-01-10 | Add multi-scenario examples |
| 1.0.0 | 2026-01-10 | Initial version |
```

---

## VII. Related Documentation

- `PERFECT_SKILL_TEMPLATE.md` - Complete SKILL.md template (includes complete examples)
- `SKILL_OPTIMIZATION_CHECKLIST.md` - Complete optimization checklist
- `README.md` - Skills overview document

## VIII. Reference Resources

- [Agent Skills Official Specification](https://agentskills.io/specification)
- [Agent Skills GitHub](https://github.com/anthropics/skills)
- [Claude Agent Skills Deep Dive](https://lih.substack.com/p/claude-agent-skills)

---

## IX. Update Log

| Version | Date | Update Content |
|---------|------|---------------|
| 1.1 | 2026-01-11 | Add related documentation links, improve optimization guide |
| 1.0 | 2026-01-11 | Initial version, create optimization guide based on official specification |
