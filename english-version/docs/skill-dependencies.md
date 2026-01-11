# Skills Dependency Documentation

> Document Version: 1.0
> Update Date: 2026-01-10

---

## Overview

This document describes dependencies, calling relationships between all Skills, and recommended combination usage patterns.

---

## I. Dependency Graph

### 1.1 Core Dependency Chain

```
story-five-elements (Story Five Elements Analysis)
    ├── story-type-analyzer (Genre Analysis)
    ├── story-summarizer (Story Summary)
    ├── character-profile (Character Biography)
    │   └── story-outliner (needs story outline as input)
    ├── character-relationships (Character Relationships)
    │   └── character-profile (needs character info)
    ├── plot-keypoints (Major Plot Points)
    └── mind-map-generator (Mind Map Generator)
            └── plot-keypoints (needs plot point data)

drama-workflow (Drama Analysis Workflow)
    ├── text-truncator (Text Truncation)
    ├── text-splitter (Text Splitting)
    ├── drama-analyzer (Script Analysis)
    │   └── plot-keypoints (needs plot point definitions)
    └── result-integrator (Result Integration)
            └── drama-analyzer (needs analysis results)

plot-workflow (Plot Workflow)
    ├── plot-keypoints (Major Plot Points)
    ├── detailed-plot-analyzer (Detailed Plot Points)
    │   └── plot-keypoints (needs major plot points)
    └── output-formatter (Output Formatting)
            └── detailed-plot-analyzer (needs analysis results)

series-analyzer (Series Analysis)
    ├── story-five-elements (Five Elements Analysis)
    ├── drama-analyzer (Breakdown Analysis)
    ├── web-search (Web Search)
    └── result-integrator (Result Integration)
```

### 1.2 Evaluation Chain Dependencies

```
Evaluation Decision Flow:
    ↓
ip-evaluator (IP Evaluation)
    ↓ (pass)
story-outline-evaluator (Outline Evaluation)
    ↓ (pass)
drama-evaluator (Short Drama Evaluation)
    ↓ (pass)
script-evaluator (Script Evaluation)
```

### 1.3 Creation Chain Dependencies

```
drama-planner (Short Drama Planning)
    ↓
drama-creator (Script Creation)
    ↓
script-evaluator (Script Evaluation)
    ↓ (based on evaluation results)
drama-creator (Script Optimization)
```

---

## II. Skill Call Relationship Table

### 2.1 Most Called Skills

| Skill Name | Called by Following Skills |
|------------|---------------------------|
| `story-outliner` | story-five-elements, character-profile, character-relationships |
| `plot-keypoints` | story-five-elements, drama-analyzer, detailed-plot-analyzer |
| `character-profile` | story-five-elements, character-relationships |
| `drama-analyzer` | drama-workflow, series-analyzer |
| `result-integrator` | drama-workflow, plot-workflow, series-analyzer |

### 2.2 Input Dependency Relationships

| Skill Name | Required Input | Recommended Preceding Skill |
|------------|---------------|---------------------------|
| `character-profile` | Story text | story-outliner, story-summarizer |
| `character-relationships` | Character info | character-profile |
| `plot-keypoints` | Story text | story-outliner |
| `detailed-plot-analyzer` | Major plot points | plot-keypoints |
| `mind-map-generator` | Plot point data | plot-keypoints, detailed-plot-analyzer |
| `script-evaluator` | Script content | drama-creator |
| `result-integrator` | Multiple analysis results | drama-analyzer, plot-points-analyzer |

---

## III. Recommended Combination Usage Patterns

### 3.1 Complete Story Analysis Workflow

```
User Request: Deeply analyze this story

Recommended Combination:
1. story-outliner → Generate story outline
2. story-type-analyzer → Analyze genre type
3. plot-keypoints → Extract major plot points
4. character-profile → Generate character biographies
5. character-relationships → Analyze character relationships
6. mind-map-generator → Generate mind map

One-click Alternative: story-five-elements
```

### 3.2 IP Evaluation Decision Workflow

```
User Request: Evaluate whether this IP is worth developing

Recommended Combination:
1. ip-evaluator → Initial IP evaluation
   ↓ (score >= 8.0)
2. story-outline-evaluator → Detailed outline evaluation
   ↓ (score >= 8.0)
3. drama-evaluator → Short drama adaptation potential evaluation
   ↓ (score >= 8.0)
4. Provide final recommendation
```

### 3.3 Script Creation Workflow

```
User Request: Help me create a short drama script

Recommended Combination:
1. drama-planner → Create planning proposal
   ↓
2. drama-creator → Create script
   ↓
3. script-evaluator → Evaluate script quality
   ↓ (based on evaluation results)
4. drama-creator → Optimize script
```

### 3.4 Aired Series Learning Workflow

```
User Request: Analyze this aired series

Recommended Combination:
series-analyzer (One-stop completion)
  - Automatically calls: story-five-elements
  - Automatically calls: drama-analyzer
  - Automatically calls: web-search
  - Automatically calls: result-integrator
```

### 3.5 Long Text Deep Analysis Workflow

```
User Request: Deeply analyze this long text story

Recommended Combination:
drama-workflow (Automatic orchestration)
  - text-truncator → Truncate long text
  - text-splitter → Split text chunks
  - drama-analyzer → Parallel analysis
  - result-integrator → Integrate results
```

---

## IV. Skill Function Matrix

### 4.1 By Function Category

| Function Category | Available Skills |
|------------------|------------------|
| **Text Understanding** | story-outliner, story-summarizer, story-type-analyzer, drama-analyzer |
| **Plot Analysis** | plot-keypoints, detailed-plot-analyzer, plot-points-analyzer |
| **Character Analysis** | character-profile, character-relationships |
| **Quality Evaluation** | ip-evaluator, script-evaluator, drama-evaluator, story-outline-evaluator |
| **Content Creation** | drama-creator, drama-planner |
| **Tool Support** | text-truncator, text-splitter, file-reference, mind-map-generator |
| **Information Retrieval** | knowledge-query, web-search |
| **Result Integration** | result-integrator, output-formatter |

### 4.2 By Use Case Category

| Use Case | Recommended Skills |
|----------|-------------------|
| **Quick Story Understanding** | story-outliner, story-summarizer |
| **Deep Story Analysis** | story-five-elements, drama-workflow |
| **Character Development** | character-profile → character-relationships |
| **Plot Design** | plot-keypoints → detailed-plot-analyzer |
| **IP Decision** | ip-evaluator → story-outline-evaluator → drama-evaluator |
| **Script Creation** | drama-planner → drama-creator → script-evaluator |
| **Learn Excellent Works** | series-analyzer |
| **Long Text Processing** | drama-workflow (automatic orchestration) |

---

## V. Skill Capability Comparison

### 5.1 Similar Skill Comparison

| Function | Skill A | Skill B | Difference |
|----------|---------|---------|------------|
| Story Summary | story-outliner | story-summarizer | outliner: 300-500 words<br>summarizer: Extract key points |
| Plot Point Analysis | plot-keypoints | detailed-plot-analyzer | keypoints: Outline main structure<br>detailed: In-depth expansion analysis |
| Plot Point Analysis | drama-analyzer | plot-points-analyzer | drama: Analyze dramatic function<br>plot-points: Identify turning points |
| Evaluation | ip-evaluator | story-outline-evaluator | IP: Network info organization<br>outline: Outline quality evaluation |
| Evaluation | drama-evaluator | script-evaluator | drama: Short drama adaptation potential<br>script: Script three-dimension evaluation |

### 5.2 Selection Recommendations

```
Q: Need to generate story outline?
A: Shorter text → story-outliner (300-500 words)
   Longer text → story-summarizer (extract key points)
   Complete analysis → story-five-elements (includes outline)

Q: Need to analyze plot points?
A: Quick outline → plot-keypoints
   Deep analysis → detailed-plot-analyzer
   Dramatic function → drama-analyzer
   Turning point analysis → plot-points-analyzer

Q: Need to evaluate quality?
A: IP adaptation decision → ip-evaluator
   Outline quality → story-outline-evaluator
   Short drama potential → drama-evaluator
   Script quality → script-evaluator
```

---

## VI. Usage Recommendations

### 6.1 Single Skill Usage

Suitable scenarios:
- Need to complete single, clear task
- Already know exactly what capability is needed
- Quick access to specific information

Examples:
```
User: Use story-outliner to generate a story outline for me
User: Use character-profile to analyze this character
```

### 6.2 Combined Skill Usage

Suitable scenarios:
- Need to complete complex multi-step tasks
- Need comprehensive analysis or creation
- Not sure which specific skills to use

Examples:
```
User: Deeply analyze this story
    → Automatically use story-five-elements

User: Evaluate whether this IP is worth developing
    → Automatically use evaluation decision flow

User: Help me create a short drama
    → Automatically use creation flow
```

### 6.3 Workflow Skill Usage

Suitable scenarios:
- Processing complex long texts
- Need multi-step automated processes
- Need to integrate multiple analysis results

Examples:
```
User: Analyze this long novel
    → Automatically use drama-workflow

User: Analyze this TV series
    → Automatically use series-analyzer
```

---

## VII. Update Log

| Version | Date | Update Content |
|---------|------|---------------|
| 1.0 | 2026-01-10 | Initial version, establish dependency documentation |
