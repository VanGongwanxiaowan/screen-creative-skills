# Skills Version Management Specification

> Document Version: 1.0
> Update Date: 2026-01-10

---

## I. Version Number Rules

### 1.1 Semantic Versioning

Adopt `major.minor.patch` format:

- **major (Major Version)**: Significant functional changes or incompatible modifications
- **minor (Minor Version)**: New features or backward-compatible modifications
- **patch (Patch Version)**: Bug fixes or minor improvements

Examples:
- `1.0.0` - Initial version
- `1.1.0` - Add new examples
- `1.1.1` - Fix description errors
- `2.0.0` - Restructure core content

### 1.2 Version Information Location

Add in frontmatter of each SKILL.md:

```yaml
---
name: skill-name
description: skill description
category: category
version: 1.0.0
last_updated: 2026-01-10
changelog:
  - version: 1.0.0
    date: 2026-01-10
    changes: Initial version
---
```

---

## II. Change Record Template

### 2.1 Change Types

| Type | Description | Identifier |
|------|-------------|------------|
| Added | Add new features or content | `added` |
| Improved | Optimize existing content | `improved` |
| Fixed | Fix issues | `fixed` |
| Removed | Remove features or content | `removed` |
| Breaking | Major changes | `breaking` |

### 2.2 Change Record Format

```markdown
## Version History

| Version | Date | Change Type | Change Description |
|---------|------|-------------|-------------------|
| 1.1.0 | 2026-01-15 | added | Add 3 usage examples |
| 1.0.1 | 2026-01-12 | fixed | Fix output format error |
| 1.0.0 | 2026-01-10 | - | Initial version |
```

---

## III. Update Process

### 3.1 Pre-Update Checks

- [ ] Confirm nature of modification (added/improved/fixed)
- [ ] Determine version number change
- [ ] Prepare change description
- [ ] Test modified content

### 3.2 Update Steps

1. Update `version` and `last_updated` in frontmatter
2. Add new change record at beginning of `changelog` array
3. Update version history table at end of document
4. Submit changes

---

## IV. Version Management Examples

### Example 1: Add Examples

```yaml
---
name: drama-analyzer
description: Deeply analyze story text, extract main plot points and analyze dramatic functions
category: story-analysis
version: 1.1.0
last_updated: 2026-01-15
changelog:
  - version: 1.1.0
    date: 2026-01-15
    changes:
      - type: added
        content: Add urban emotional script analysis example
      - type: added
        content: Add suspense drama analysis example
      - type: improved
        content: Optimize output format description
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---
```

### Example 2: Fix Issues

```yaml
---
name: plot-keypoints
description: Outline story main structure, extract main plot points
category: story-analysis
version: 1.0.1
last_updated: 2026-01-12
changelog:
  - version: 1.0.1
    date: 2026-01-12
    changes:
      - type: fixed
        content: Fix error in output format example
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: Initial version
---
```

---

## V. Current All Skills Version Status

| Skill ID | Current Version | Last Update | Status |
|----------|----------------|-------------|--------|
| story-analysis class | 1.0.0 | 2026-01-10 | Stable |
| character-analysis class | 1.0.0 | 2026-01-10 | Stable |
| evaluation class | 1.0.0 | 2026-01-10 | Stable |
| creation class | 1.0.0 | 2026-01-10 | Stable |
| series-analysis class | 1.0.0 | 2026-01-10 | Stable |
| workflow class | 1.0.0 | 2026-01-10 | Stable |
| result-processing class | 1.0.0 | 2026-01-10 | Stable |
| tools class | 1.0.0 | 2026-01-10 | Stable |
| knowledge-research class | 1.0.0 | 2026-01-10 | Stable |
| novel-screening class | 1.0.0 | 2026-01-10 | Stable |

---

## VI. Version Release Plan

### Upcoming Releases
- No planned version updates

### In Discussion
- Add more real-scenario examples for all skills
- Optimize some lengthy output format descriptions
- Add shortcut commands for skill combination usage

---

## VII. Update Log

| Version | Date | Update Content |
|---------|------|---------------|
| 1.0 | 2026-01-10 | Initial version, establish version management specification |
