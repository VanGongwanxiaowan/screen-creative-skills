# Script Creation Skills Organization Planning Document

> Project: Vertical Screen Drama Planning System
> Document Version: 1.0
> Creation Date: 2026-01-10

---

## I. Project Overview

This planning document aims to systematically organize all Agent Prompts in the vertical screen drama planning system into standard Claude Skills for reuse in Claude Code/Claude.ai.

### 1.1 Goals

- Convert all 29 Agent Prompts to standard Claude Skills
- Establish Skills classification system
- Provide clear Skills usage guide

### 1.2 Scope

Cover all system prompts under the `prompts/` folder, including:
- TXT format prompt files (27 files)
- Python format prompt configuration (1 file containing multiple sub-prompts)

---

## II. Existing Agent Prompts Inventory

### 2.1 Story Analysis Class (Story Analysis)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 1 | `drama_analysis_system.txt` | Script Analysis Expert | Deeply analyze story text, summarize plot points and analyze dramatic functions |
| 2 | `major_plot_points_system.txt` | Major Plot Points Analysis Expert | Outline story main structure, summarize major plot points |
| 3 | `detailed_plot_points_system.txt` | Detailed Plot Points Analysis Expert | Conduct in-depth analysis and expansion of major plot points |
| 4 | `plot_points_analyzer_system.txt` | Plot Point Analysis Expert | Analyze plot points in story, identify key plots and turning points |
| 5 | `story_type_analyzer_system.txt` | Genre Type and Creative Extraction Expert | Analyze story genre type, extract creative elements |
| 6 | `story_summary_generator_system.txt` | Story Summary Generation Expert | Extract main plots and key points based on story text content |
| 7 | `story_summary_system.txt` | Story Outline Generation Expert | Summarize story characters, character relationships, plots, organize into story outline |
| 8 | `story_five_elements_system.txt` | Story Five Elements Analysis Expert | Analyze story genre type, story summary, character biographies, character relationships, major plot points |

### 2.2 Character Analysis Class (Character Analysis)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 9 | `character_profile_generator_system.txt` | Character Biography Generation Expert | Analyze character characteristics based on story text, generate detailed character biographies |
| 10 | `character_relationship_analyzer_system.txt` | Character Relationship Analysis Expert | Analyze relationships between characters in story, identify relationship types and characteristics |

### 2.3 Evaluation & Screening Class (Evaluation & Screening)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 11 | `ip_evaluation_agent_system.txt` | IP Evaluation Expert | Conduct network information organization on IP content, multi-dimensional analysis and scoring |
| 12 | `script_evaluation_agent_system.txt` | Film & TV Script Evaluation Expert | Evaluate and score film & TV scripts from three dimensions: ideological, artistic, and viewing |
| 13 | `short_drama_evaluation_system.txt` | Vertical Screen Drama Evaluation Expert | Evaluate and score according to vertical screen drama evaluation standards, from core satisfaction points, story types, etc. |
| 14 | `story_outline_evaluation_system.txt`* | Story Outline Evaluation Expert | Conduct professional evaluation and analysis of story outlines |

> Note: story_outline_evaluation in novel_screening_prompts.py

### 2.4 Creation & Planning Class (Creation & Planning)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 15 | `short_drama_creater_system.txt` | Vertical Screen Drama Script Creation Master | Create vertical screen drama scripts, including macro construction, script creation, precision optimization, creative ideation |
| 16 | `short_drama_planner_system.txt` | Vertical Screen Drama Planner | Provide professional planning proposals including emotional value analysis, golden three seconds hook design, three-act structure planning |

### 2.5 Series Analysis Class (Series Analysis)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 17 | `series_analysis_system.txt` | Aired Series Analysis and Breakdown Expert | Analyze all aspects of aired series, including series info acquisition, breakdown analysis, story five elements analysis |

### 2.6 Workflow Orchestration Class (Workflow Orchestration)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 18 | `drama_workflow_system.txt` | Plot Point Dramatic Function Analysis Workflow Orchestrator | Coordinate entire plot point analysis process |
| 19 | `plot_points_workflow_system.txt` | Major Plot Points and Detailed Plot Points Workflow Orchestrator | Responsible for orchestration and coordination of major plot points and detailed plot points one-click generation workflow |

### 2.7 Result Processing Class (Result Processing)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 20 | `result_integrator_system.txt` | Result Integration Tool | Integrate multiple plot point analysis results into comprehensive report |
| 21 | `output_formatter_system.txt` | Output Formatting Expert | Integrate output results of various agents into structured final output |

### 2.8 Tools & Utilities Class (Tools & Utilities)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 22 | `file_reference_system.txt` | File Reference Parsing Expert | Process and analyze file references uploaded by users |
| 23 | `text_truncator_system.txt` | Text Truncation Tool | Intelligently truncate text, maintaining content completeness |
| 24 | `text_splitter_system.txt` | Text Splitting Tool | Split text into specified size chunks |
| 25 | `mind_map_system.txt` | Mind Map Generation Expert | Call generateTreeMind tool to create visual mind maps |

### 2.9 Knowledge & Research Class (Knowledge & Research)

| No. | Filename | Agent Name | Function Description |
|-----|----------|------------|---------------------|
| 26 | `knowledge_system.txt` | Vertical Screen Drama Knowledge Base Query Expert | Focus on knowledge base queries and information retrieval |
| 27 | `websearch_system.txt` | Vertical Screen Drama Web Search Expert | Use Zhipu AI for precise web search |

### 2.10 Novel Screening Class (Novel Screening - Python Config)

| No. | Config Key | Agent Name | Function Description |
|-----|------------|------------|---------------------|
| 28 | `story_summary` | Story Outline Generation Expert | Read and understand story text, summarize into fluent story outline |
| 29 | `story_evaluation` | Senior Story Evaluation Expert | Judge and score stories from various dimensions according to evaluation priorities of genre and type |
| 30 | `score_analyzer` | Score Analysis Agent | Analyze score data in multiple evaluation results, statistics of various scoring indicators |
| 31 | `text_truncator` | Text Truncation Tool Agent | Receive text content and max length limit, intelligently truncate text |

---

## III. Skills Classification System Design

### 3.1 Primary Classification

Divide Skills into following categories based on Agent functional domains:

| Category Code | Category Name | English Name | Skills Count |
|---------------|--------------|--------------|-------------|
| SA | Story Analysis | Story Analysis | 8 |
| CA | Character Analysis | Character Analysis | 2 |
| EV | Evaluation Screening | Evaluation | 4 |
| CR | Creation Planning | Creation & Planning | 2 |
| SS | Series Analysis | Series Analysis | 1 |
| WF | Workflow Orchestration | Workflow | 2 |
| RP | Result Processing | Result Processing | 2 |
| TL | Tools Utilities | Tools & Utilities | 4 |
| KR | Knowledge Research | Knowledge & Research | 2 |
| NS | Novel Screening | Novel Screening | 4 |

### 3.2 Skills Naming Convention

Follow Claude Skills naming convention:
- Use lowercase letters
- Use hyphens to separate words
- Format: `{category}-{function-name}`

Examples:
- `story-plot-analyzer` - Plot point analysis
- `character-profile-generator` - Character biography generation
- `drama-evaluator` - Script evaluation

---

## IV. Skills Directory Structure

```
skills/
├── README.md                    # Skills overview document
├── category/
│   ├── story-analysis/          # Story analysis class
│   │   ├── drama-analyzer/
│   │   │   └── SKILL.md
│   │   ├── plot-points-analyzer/
│   │   │   └── SKILL.md
│   │   ├── detailed-plot-analyzer/
│   │   │   └── SKILL.md
│   │   ├── plot-keypoints/
│   │   │   └── SKILL.md
│   │   ├── story-type-analyzer/
│   │   │   └── SKILL.md
│   │   ├── story-summarizer/
│   │   │   └── SKILL.md
│   │   ├── story-outliner/
│   │   │   └── SKILL.md
│   │   └── story-five-elements/
│   │       └── SKILL.md
│   ├── character-analysis/      # Character analysis class
│   │   ├── character-profile/
│   │   │   └── SKILL.md
│   │   └── character-relationships/
│   │       └── SKILL.md
│   ├── evaluation/              # Evaluation screening class
│   │   ├── ip-evaluator/
│   │   │   └── SKILL.md
│   │   ├── script-evaluator/
│   │   │   └── SKILL.md
│   │   ├── drama-evaluator/
│   │   │   └── SKILL.md
│   │   └── story-outline-evaluator/
│   │       └── SKILL.md
│   ├── creation/                # Creation planning class
│   │   ├── drama-creator/
│   │   │   └── SKILL.md
│   │   └── drama-planner/
│   │       └── SKILL.md
│   ├── series-analysis/         # Series analysis class
│   │   └── series-analyzer/
│   │       └── SKILL.md
│   ├── workflow/                # Workflow orchestration class
│   │   ├── drama-workflow/
│   │   │   └── SKILL.md
│   │   └── plot-workflow/
│   │       └── SKILL.md
│   ├── result-processing/       # Result processing class
│   │   ├── result-integrator/
│   │   │   └── SKILL.md
│   │   └── output-formatter/
│   │       └── SKILL.md
│   ├── tools/                   # Tools utilities class
│   │   ├── file-reference/
│   │   │   └── SKILL.md
│   │   ├── text-truncator/
│   │   │   └── SKILL.md
│   │   ├── text-splitter/
│   │   │   └── SKILL.md
│   │   └── mind-map-generator/
│   │       └── SKILL.md
│   ├── knowledge-research/      # Knowledge research class
│   │   ├── knowledge-query/
│   │   │   └── SKILL.md
│   │   └── web-search/
│   │       └── SKILL.md
│   └── novel-screening/         # Novel screening class
│       ├── novel-summarizer/
│       │   └── SKILL.md
│       ├── novel-evaluator/
│       │   └── SKILL.md
│       ├── score-analyzer/
│       │   └── SKILL.md
│       └── novel-truncator/
│           └── SKILL.md
```

---

## V. SKILL.md Template Design

### 5.1 Standard SKILL.md Structure

```markdown
---
name: skill-name
description: Clear description of this skill's functionality and use cases
category: category
version: 1.0
---

# Skill Name

## Function Description
Detailed description of this skill's functionality and purpose.

## Use Cases
- Scenario 1: Description
- Scenario 2: Description

## Core Capabilities
1. Capability 1: Description
2. Capability 2: Description

## Workflow
1. Step 1
2. Step 2
3. Step 3

## Input Requirements
- Input 1: Description
- Input 2: Description

## Output Format
Describe format and structure of output results.

## Usage Examples

### Example 1: Scenario Description
```
User Input: Example input
```

**Expected Output:**
```
Example output
```

## Notes
- Note 1
- Note 2
```

### 5.2 Prompt Conversion Mapping Table

| Original Prompt Field | SKILL.md Corresponding Field |
|----------------------|----------------------------|
| Profile → role | # Skill Name |
| Profile → description | Function Description |
| Goals | Core Capabilities + Use Cases |
| Constraints | Notes |
| Skills | Core Capabilities |
| Workflows | Workflow |
| OutputFormat | Output Format |

---

## VI. Implementation Plan

### 6.1 Phase Division

#### Phase 1: Infrastructure Setup (Day 1)
1. Create Skills directory structure
2. Create SKILL.md template file
3. Write Skills README.md overview document

#### Phase 2: Core Skills Conversion (Day 2-3)
Convert following core Skills by priority:
1. Story analysis class (8)
2. Character analysis class (2)
3. Evaluation screening class (4)

#### Phase 3: Creation & Tools Skills Conversion (Day 4)
1. Creation planning class (2)
2. Tools utilities class (4)
3. Knowledge research class (2)

#### Phase 4: Workflow & Result Processing (Day 5)
1. Workflow orchestration class (2)
2. Result processing class (2)
3. Series analysis class (1)
4. Novel screening class (4)

#### Phase 5: Testing & Optimization (Day 6)
1. Skills function testing
2. Cross Skills collaboration testing
3. Documentation improvement

### 6.2 Quality Standards

Each SKILL.md must meet following standards:
- [ ] Frontmatter complete (name, description)
- [ ] Function description clear and accurate
- [ ] Use cases specific and clear
- [ ] Workflow steps clear
- [ ] Input/Output formats clear
- [ ] Include usage examples
- [ ] Notes complete

---

## VII. Skills Usage Guide

### 7.1 Install Skills

Place skills folder in Claude Code supported location:
```
.claude/skills/
```

### 7.2 Call Skills

Mention skill name directly in conversation to activate:

```
User: Use story-plot-analyzer to analyze following story text...
```

### 7.3 Skills Combination Usage

Multiple skills can be combined to complete complex tasks:

```
User: First use story-summarizer to generate outline, then use character-profile to generate character biographies...
```

---

## VIII. Appendix

### 8.1 Complete Skills Mapping Table

| No. | Original File | Skill ID | Skill Name | Category |
|-----|--------------|----------|------------|----------|
| 1 | drama_analysis_system.txt | drama-analyzer | Script Analysis Expert | SA |
| 2 | major_plot_points_system.txt | plot-keypoints | Major Plot Points Analysis Expert | SA |
| 3 | detailed_plot_points_system.txt | detailed-plot-analyzer | Detailed Plot Points Analysis Expert | SA |
| 4 | plot_points_analyzer_system.txt | plot-points-analyzer | Plot Point Analysis Expert | SA |
| 5 | story_type_analyzer_system.txt | story-type-analyzer | Genre Type and Creative Extraction Expert | SA |
| 6 | story_summary_generator_system.txt | story-summarizer | Story Summary Generation Expert | SA |
| 7 | story_summary_system.txt | story-outliner | Story Outline Generation Expert | SA |
| 8 | story_five_elements_system.txt | story-five-elements | Story Five Elements Analysis Expert | SA |
| 9 | character_profile_generator_system.txt | character-profile | Character Biography Generation Expert | CA |
| 10 | character_relationship_analyzer_system.txt | character-relationships | Character Relationship Analysis Expert | CA |
| 11 | ip_evaluation_agent_system.txt | ip-evaluator | IP Evaluation Expert | EV |
| 12 | script_evaluation_agent_system.txt | script-evaluator | Film & TV Script Evaluation Expert | EV |
| 13 | short_drama_evaluation_system.txt | drama-evaluator | Vertical Screen Drama Evaluation Expert | EV |
| 14 | novel_screening_prompts.py (story_evaluation) | story-outline-evaluator | Story Outline Evaluation Expert | EV |
| 15 | short_drama_creater_system.txt | drama-creator | Vertical Screen Drama Script Creation Master | CR |
| 16 | short_drama_planner_system.txt | drama-planner | Vertical Screen Drama Planner | CR |
| 17 | series_analysis_system.txt | series-analyzer | Aired Series Analysis and Breakdown Expert | SS |
| 18 | drama_workflow_system.txt | drama-workflow | Plot Point Dramatic Function Analysis Workflow Orchestrator | WF |
| 19 | plot_points_workflow_system.txt | plot-workflow | Major Plot Points and Detailed Plot Points Workflow Orchestrator | WF |
| 20 | result_integrator_system.txt | result-integrator | Result Integration Tool | RP |
| 21 | output_formatter_system.txt | output-formatter | Output Formatting Expert | RP |
| 22 | file_reference_system.txt | file-reference | File Reference Parsing Expert | TL |
| 23 | text_truncator_system.txt | text-truncator | Text Truncation Tool | TL |
| 24 | text_splitter_system.txt | text-splitter | Text Splitting Tool | TL |
| 25 | mind_map_system.txt | mind-map-generator | Mind Map Generation Expert | TL |
| 26 | knowledge_system.txt | knowledge-query | Vertical Screen Drama Knowledge Base Query Expert | KR |
| 27 | websearch_system.txt | web-search | Vertical Screen Drama Web Search Expert | KR |
| 28 | novel_screening_prompts.py (story_summary) | novel-summarizer | Story Outline Generation Expert | NS |
| 29 | novel_screening_prompts.py (story_evaluation) | novel-evaluator | Senior Story Evaluation Expert | NS |
| 30 | novel_screening_prompts.py (score_analyzer) | score-analyzer | Score Analysis Agent | NS |
| 31 | novel_screening_prompts.py (text_truncator) | novel-truncator | Text Truncation Tool Agent | NS |

### 8.2 Skill Dependencies

```
story-five-elements (Five Elements Analysis)
    ├── story-type-analyzer (Genre Analysis)
    ├── story-summarizer (Story Summary)
    ├── character-profile (Character Biography)
    ├── character-relationships (Character Relationships)
    ├── plot-keypoints (Major Plot Points)
    └── mind-map-generator (Mind Map)

drama-workflow (Drama Analysis Workflow)
    ├── text-truncator (Text Truncation)
    ├── text-splitter (Text Splitting)
    ├── drama-analyzer (Script Analysis)
    └── result-integrator (Result Integration)
```

---

## IX. Update Log

| Version | Date | Update Content |
|---------|------|---------------|
| 1.0 | 2026-01-10 | Initial version, complete overall planning |

---

**End of Document**
