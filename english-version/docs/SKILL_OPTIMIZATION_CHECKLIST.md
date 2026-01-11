# Agent Skills Optimization Checklist

> Complete checklist based on best practices
> Version: 1.0.0
> Update Date: 2026-01-11

---

## I. Frontmatter Checklist

### 1.1 Required Fields

- [ ] **name**:
  - Only lowercase letters, numbers, hyphens
  - Length 1-64 characters
  - Format: `category-function` or `function-name`

- [ ] **description**:
  - Clearly states function (what) + use cases (when)
  - Length 1-1024 characters
  - Use imperative language
  - Format: `[Function description]. For [scenario 1], [scenario 2], [scenario 3]`

### 1.2 Recommended Fields

- [ ] **category**: Correct category added
- [ ] **version**: Use semantic versioning (e.g., 2.0.0)
- [ ] **last_updated**: Date format correct (YYYY-MM-DD)
- [ ] **license**: Added (recommend MIT)
- [ ] **compatibility**: Added (if applicable)
- [ ] **changelog**: Complete structure, contains all historical versions

### 1.3 Optional Fields (Add as Needed)

- [ ] **author**: Author information (if needed)
- [ ] **source**: Source information (if needed)
- [ ] **allowed-tools**: Tool list (if specific tools needed)
- [ ] **model**: Model specification (if specific model capabilities needed)
- [ ] **disable-model-invocation**: Whether to disable model invocation (if applicable)
- [ ] **mode**: Operation mode (autonomous/interactive, if applicable)

---

## II. Main Content Checklist

### 2.1 Structural Completeness

- [ ] **Title**: Clear Chinese title, reflects skill functionality
- [ ] **Function**: 1-2 sentences clearly describe core functionality, use imperative language
- [ ] **Use Cases**: At least 3 specific use cases
- [ ] **Core Steps/Workflow**: Clear step-by-step instructions, use imperative language
- [ ] **Input Requirements**: Clear input format, type, requirements
- [ ] **Output Format**: Use code block to display output template
- [ ] **Constraints/Requirements**: Clear usage constraints and notes
- [ ] **Examples**: At least 2 complete input/output examples
- [ ] **Version History**: Complete version history table

### 2.2 Language Style

- [ ] Use imperative language (avoid "should", "suggest", "can", etc.)
- [ ] Avoid redundant polite language ("please", "trouble you", etc.)
- [ ] Use standard verbs ("分析" not "进行分析")
- [ ] Description clear and concise, avoid lengthy sentences

### 2.3 Content Quality

- [ ] Main SKILL.md controlled within 5000 words (~3000 Chinese characters)
- [ ] Function description accurate, not exaggerated
- [ ] Use cases specific and clear, avoid generalization
- [ ] Examples real and effective, directly usable
- [ ] Constraints clear, no ambiguity

### 2.4 Paths and References

- [ ] All paths use variable `{baseDir}` instead of hardcoded paths
- [ ] Correct path format when referencing other documents
- [ ] references directory reference format correct

---

## III. References Checklist

### 3.1 Directory Structure

- [ ] `references/` directory created (if needed)
- [ ] `references/examples.md` contains detailed examples (recommended)
- [ ] Other detailed documents moved to references/ (if needed)

### 3.2 Content Organization

- [ ] Main file references references/ directory
- [ ] references/ document structure clear
- [ ] Detailed content moved from main file to references/ (if main file over 4000 words)

---

## IV. Best Practices Checklist

### 4.1 Discoverability

- [ ] description clearly states function and scenarios, easy to search
- [ ] category correct, easy to categorize and find
- [ ] Keywords accurate, match user search habits

### 4.2 Usability

- [ ] Examples complete, can directly copy and use
- [ ] Input/Output formats clear, no ambiguity
- [ ] Constraints clear, avoid misuse

### 4.3 Maintainability

- [ ] Version history complete, easy to track changes
- [ ] changelog detailed, explains change reasons
- [ ] Document structure clear, easy to update

---

## V. Category Checklist

### 5.1 Story Analysis Class (story-analysis)

- [ ] Analysis steps clear, rigorous logic
- [ ] Output format standardized, easy for subsequent processing
- [ ] Examples cover main story types

**Checked Skills**:
- [ ] drama-analyzer
- [ ] plot-keypoints
- [ ] detailed-plot-analyzer
- [ ] plot-points-analyzer
- [ ] story-type-analyzer
- [ ] story-summarizer
- [ ] story-outliner
- [ ] story-five-elements

### 5.2 Character Analysis Class (character-analysis)

- [ ] Character analysis dimensions complete
- [ ] Output format clear, structured information
- [ ] Examples cover different character types

**Checked Skills**:
- [ ] character-profile
- [ ] character-relationships

### 5.3 Evaluation Screening Class (evaluation)

- [ ] Evaluation dimensions clear, scoring standards explicit
- [ ] Output report structure complete
- [ ] Optimization recommendations specific and actionable

**Checked Skills**:
- [ ] ip-evaluator
- [ ] script-evaluator
- [ ] drama-evaluator
- [ ] story-outline-evaluator

### 5.4 Creation Planning Class (creation)

- [ ] Creation methodology clear
- [ ] Output format meets industry standards
- [ ] Examples demonstrate different creation tasks

**Checked Skills**:
- [ ] drama-creator
- [ ] drama-planner

### 5.5 Workflow Orchestration Class (workflow)

- [ ] Workflow steps clear
- [ ] Agent collaboration mechanism explicit
- [ ] Output includes execution status and results

**Checked Skills**:
- [ ] drama-workflow
- [ ] plot-workflow

### 5.6 Tools Utilities Class (tools)

- [ ] Tool function clear, parameters clear
- [ ] Output format standardized
- [ ] Error handling description complete

**Checked Skills**:
- [ ] file-reference
- [ ] text-truncator
- [ ] text-splitter
- [ ] mind-map-generator

### 5.7 Other Categories

**Checked Skills**:
- [ ] series-analyzer (Series Analysis)
- [ ] result-integrator (Result Processing)
- [ ] output-formatter (Result Processing)
- [ ] knowledge-query (Knowledge Research)
- [ ] web-search (Knowledge Research)
- [ ] novel-summarizer (Novel Screening)
- [ ] novel-evaluator (Novel Screening)
- [ ] score-analyzer (Novel Screening)
- [ ] novel-truncator (Novel Screening)

---

## VI. Optimization Priority

### High Priority (Core Skills, Optimized)

1. ✅ drama-analyzer - Script Analysis Expert
2. ✅ story-five-elements - Story Five Elements Analysis Expert
3. ✅ character-profile - Character Biography Generation Expert
4. ✅ drama-evaluator - Vertical Screen Drama Evaluation Expert
5. ✅ drama-creator - Vertical Screen Drama Script Creation Master
6. ✅ ip-evaluator - IP Evaluation Expert

### Medium Priority (Important Skills, Pending Optimization)

7. [ ] plot-keypoints - Major Plot Points Analysis Expert
8. [ ] detailed-plot-analyzer - Detailed Plot Points Analysis Expert
9. [ ] drama-planner - Vertical Screen Drama Planner
10. [ ] script-evaluator - Film & TV Script Evaluation Expert
11. [ ] drama-workflow - Plot Point Dramatic Function Analysis Workflow Orchestrator
12. [ ] plot-workflow - Major Plot Points and Detailed Plot Points Workflow Orchestrator

### Standard Priority (Other Skills, Optimize as Needed)

13. [ ] Remaining 19 Skills

---

## VII. Quick Check Scripts

Use following commands to quickly check Frontmatter of all Skills:

```bash
# Check Frontmatter of all SKILL.md files
find skills/category -name "SKILL.md" -exec grep -l "^---" {} \;

# Check description field
find skills/category -name "SKILL.md" -exec grep "^description:" {} \;

# Check version field
find skills/category -name "SKILL.md" -exec grep "^version:" {} \;
```

---

## VIII. Optimization Recommendations

### 8.1 Batch Optimization Steps

1. **Step 1**: Check Frontmatter completeness of all Skills
2. **Step 2**: Optimize description field, ensure compliance with specifications
3. **Step 3**: Uniformly add recommended fields (license, compatibility, etc.)
4. **Step 4**: Optimize main content, use imperative language
5. **Step 5**: Add detailed examples (at least 2)
6. **Step 6**: Create references/ directory (if needed)
7. **Step 7**: Update version number and changelog

### 8.2 Common Problem Fixes

**Problem 1**: Description too simple
- **Fix**: Add use cases, use "For..." format

**Problem 2**: Use non-imperative language
- **Fix**: Change "应该分析" to "分析", "建议使用" to "使用"

**Problem 3**: Missing examples
- **Fix**: Add at least 2 complete input/output examples

**Problem 4**: Main file too long
- **Fix**: Move detailed content to `references/examples.md`

**Problem 5**: Hardcoded paths
- **Fix**: Use `{baseDir}` variable instead of hardcoded paths

---

## IX. Completion Statistics

### Overall Progress

- **Total Skills**: 31
- **Optimized**: 6 (19%)
- **Pending**: 25 (81%)

### Category Progress

| Category | Total | Optimized | Pending | Completion |
|----------|-------|-----------|---------|------------|
| Story Analysis | 8 | 2 | 6 | 25% |
| Character Analysis | 2 | 1 | 1 | 50% |
| Evaluation Screening | 4 | 2 | 2 | 50% |
| Creation Planning | 2 | 1 | 1 | 50% |
| Workflow Orchestration | 2 | 0 | 2 | 0% |
| Tools Utilities | 4 | 0 | 4 | 0% |
| Other Categories | 9 | 0 | 9 | 0% |

---

## X. Next Actions

1. ✅ Create perfect template and optimization guide
2. ✅ Optimize 6 core Skills
3. ✅ Optimize remaining 25 Skills (by priority)
4. ✅ Create missing references/ directories and documents
5. [ ] Update README.md and planning documents
6. [ ] Conduct comprehensive checking and testing

---

**Last Update**: 2026-01-11
**Maintainer**: juben project team
