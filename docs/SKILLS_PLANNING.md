# 剧本创作 Skills 整理规划文档

> 项目：竖屏短剧策划系统
> 文档版本：1.0
> 创建日期：2026-01-10

---

## 一、项目概述

本规划文档旨在将竖屏短剧策划系统中的所有 Agent Prompts 系统化地整理成 Claude Skills，以便在 Claude Code/Claude.ai 中复用这些专业能力。

### 1.1 目标

- 将所有 29 个 Agent Prompts 转换为标准 Claude Skills
- 建立 Skills 分类体系
- 提供清晰的 Skills 使用指南

### 1.2 范围

覆盖 `prompts/` 文件夹下的所有系统提示词，包括：
- TXT 格式提示词文件（27个）
- Python 格式提示词配置（1个包含多个子提示词）

---

## 二、现有 Agent Prompts 清单

### 2.1 故事分析类 (Story Analysis)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 1 | `drama_analysis_system.txt` | 剧本分析专家 | 深入分析故事文本，总结情节点并分析戏剧功能 |
| 2 | `major_plot_points_system.txt` | 大情节点分析专家 | 梳理故事主要脉络，总结主要情节点 |
| 3 | `detailed_plot_points_system.txt` | 详细情节点分析专家 | 对大情节点进行深入分析和扩展 |
| 4 | `plot_points_analyzer_system.txt` | 情节点分析专家 | 分析故事中的情节点，识别关键情节和转折点 |
| 5 | `story_type_analyzer_system.txt` | 题材类型与创意提炼专家 | 分析故事题材类型，提炼创意元素 |
| 6 | `story_summary_generator_system.txt` | 故事梗概生成专家 | 基于故事文本内容提炼主要情节和要点 |
| 7 | `story_summary_system.txt` | 故事大纲生成专家 | 总结故事人物、人物关系、情节，整理成故事大纲 |
| 8 | `story_five_elements_system.txt` | 故事五元素分析专家 | 分析故事的题材类型、故事梗概、人物小传、人物关系、大情节点 |

### 2.2 人物分析类 (Character Analysis)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 9 | `character_profile_generator_system.txt` | 人物小传生成专家 | 基于故事文本分析人物特征，生成详细的人物小传 |
| 10 | `character_relationship_analyzer_system.txt` | 人物关系分析专家 | 分析故事中人物之间的关系，识别人物关系的类型和特点 |

### 2.3 评估与筛选类 (Evaluation & Screening)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 11 | `ip_evaluation_agent_system.txt` | IP评估专家 | 对IP内容进行网络信息梳理，从多维度进行分析、打分 |
| 12 | `script_evaluation_agent_system.txt` | 影视剧本评估专家 | 对影视剧本从思想性、艺术性、观赏性三个维度进行评估打分 |
| 13 | `short_drama_evaluation_system.txt` | 竖屏短剧评估专家 | 依据竖屏短剧评估标准，从核心爽点、故事类型等维度评估打分 |
| 14 | `story_outline_evaluation_system.txt`* | 故事大纲评估专家 | 对故事大纲进行专业评估和分析 |

> 注：story_outline_evaluation 在 novel_screening_prompts.py 中

### 2.4 创作与策划类 (Creation & Planning)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 15 | `short_drama_creater_system.txt` | 竖屏短剧剧本创作大师 | 创作竖屏短剧剧本，包括宏观建构、剧本创作、精准优化、创意发想 |
| 16 | `short_drama_planner_system.txt` | 竖屏短剧策划师 | 提供情绪价值分析、黄金三秒钩子设计、三幕式结构规划等专业策划方案 |

### 2.5 剧集分析类 (Series Analysis)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 17 | `series_analysis_system.txt` | 已播剧集分析与拉片专家 | 分析已播剧集的各个方面，包括剧集信息获取、拉片分析、故事五元素分析 |

### 2.6 工作流编排类 (Workflow Orchestration)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 18 | `drama_workflow_system.txt` | 情节点戏剧功能分析工作流编排器 | 协调整个情节点分析流程 |
| 19 | `plot_points_workflow_system.txt` | 大情节点与详细情节点工作流编排专家 | 负责大情节点与详细情节点一键生成工作流的编排和协调 |

### 2.7 结果处理类 (Result Processing)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 20 | `result_integrator_system.txt` | 结果整合工具 | 将多个情节点分析结果整合成综合报告 |
| 21 | `output_formatter_system.txt` | 输出整理专家 | 将各个智能体的输出结果整合为结构化的最终输出 |

### 2.8 工具与辅助类 (Tools & Utilities)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 22 | `file_reference_system.txt` | 文件引用解析专家 | 处理和分析用户上传的文件引用 |
| 23 | `text_truncator_system.txt` | 文本截断工具 | 智能截断文本，保持内容的完整性 |
| 24 | `text_splitter_system.txt` | 文本分割工具 | 将文本分割成指定大小的块 |
| 25 | `mind_map_system.txt` | 思维导图生成专家 | 调用generateTreeMind工具创建可视化思维导图 |

### 2.9 知识与检索类 (Knowledge & Research)

| 序号 | 文件名 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 26 | `knowledge_system.txt` | 竖屏短剧知识库查询专家 | 专注于知识库查询和信息检索 |
| 27 | `websearch_system.txt` | 竖屏短剧网络检索专家 | 使用智谱AI进行精准的网络搜索 |

### 2.10 小说初筛类 (Novel Screening - Python配置)

| 序号 | 配置键 | Agent名称 | 功能描述 |
|------|--------|-----------|----------|
| 28 | `story_summary` | 故事大纲生成专家 | 对故事文本进行阅读与理解，总结成行文流畅的故事大纲 |
| 29 | `story_evaluation` | 资深的故事评估专家 | 根据题材与类型类故事的评估重点，从各个维度对故事进行判断、评分 |
| 30 | `score_analyzer` | 评分分析智能体 | 分析多轮评估结果中的评分数据，统计各项评分指标 |
| 31 | `text_truncator` | 文本截断工具智能体 | 接收文本内容和最大长度限制，智能截断文本 |

---

## 三、Skills 分类体系设计

### 3.1 一级分类

基于 Agent 的功能域，将 Skills 划分为以下类别：

| 类别代码 | 类别名称 | 英文名称 | Skills数量 |
|----------|----------|----------|------------|
| SA | 故事分析 | Story Analysis | 8 |
| CA | 人物分析 | Character Analysis | 2 |
| EV | 评估筛选 | Evaluation | 4 |
| CR | 创作策划 | Creation & Planning | 2 |
| SS | 剧集分析 | Series Analysis | 1 |
| WF | 工作流编排 | Workflow | 2 |
| RP | 结果处理 | Result Processing | 2 |
| TL | 工具辅助 | Tools & Utilities | 4 |
| KR | 知识检索 | Knowledge & Research | 2 |
| NS | 小说初筛 | Novel Screening | 4 |

### 3.2 Skills 命名规范

遵循 Claude Skills 命名约定：
- 使用小写字母
- 使用连字符分隔单词
- 格式：`{类别}-{功能名}`

示例：
- `story-plot-analyzer` - 情节点分析
- `character-profile-generator` - 人物小传生成
- `drama-evaluator` - 剧本评估

---

## 四、Skills 目录结构

```
skills/
├── README.md                    # Skills 总览文档
├── category/
│   ├── story-analysis/          # 故事分析类
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
│   ├── character-analysis/      # 人物分析类
│   │   ├── character-profile/
│   │   │   └── SKILL.md
│   │   └── character-relationships/
│   │       └── SKILL.md
│   ├── evaluation/              # 评估筛选类
│   │   ├── ip-evaluator/
│   │   │   └── SKILL.md
│   │   ├── script-evaluator/
│   │   │   └── SKILL.md
│   │   ├── drama-evaluator/
│   │   │   └── SKILL.md
│   │   └── story-outline-evaluator/
│   │       └── SKILL.md
│   ├── creation/                # 创作策划类
│   │   ├── drama-creator/
│   │   │   └── SKILL.md
│   │   └── drama-planner/
│   │       └── SKILL.md
│   ├── series-analysis/         # 剧集分析类
│   │   └── series-analyzer/
│   │       └── SKILL.md
│   ├── workflow/                # 工作流编排类
│   │   ├── drama-workflow/
│   │   │   └── SKILL.md
│   │   └── plot-workflow/
│   │       └── SKILL.md
│   ├── result-processing/       # 结果处理类
│   │   ├── result-integrator/
│   │   │   └── SKILL.md
│   │   └── output-formatter/
│   │       └── SKILL.md
│   ├── tools/                   # 工具辅助类
│   │   ├── file-reference/
│   │   │   └── SKILL.md
│   │   ├── text-truncator/
│   │   │   └── SKILL.md
│   │   ├── text-splitter/
│   │   │   └── SKILL.md
│   │   └── mind-map-generator/
│   │       └── SKILL.md
│   ├── knowledge-research/      # 知识检索类
│   │   ├── knowledge-query/
│   │   │   └── SKILL.md
│   │   └── web-search/
│   │       └── SKILL.md
│   └── novel-screening/         # 小说初筛类
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

## 五、SKILL.md 模板设计

### 5.1 标准 SKILL.md 结构

```markdown
---
name: skill-name
description: 清晰描述此 skill 的功能和使用场景
category: 类别
version: 1.0
---

# Skill 名称

## 功能描述
详细描述这个 skill 的功能和作用。

## 使用场景
- 场景1：描述
- 场景2：描述

## 核心能力
1. 能力1：描述
2. 能力2：描述

## 工作流程
1. 步骤1
2. 步骤2
3. 步骤3

## 输入要求
- 输入1：描述
- 输入2：描述

## 输出格式
描述输出结果的格式和结构。

## 使用示例

### 示例1：场景描述
```
用户输入：示例输入
```

**预期输出：**
```
示例输出
```

## 注意事项
- 注意事项1
- 注意事项2
```

### 5.2 Prompt 转换映射表

| 原 Prompt 字段 | SKILL.md 对应字段 |
|----------------|------------------|
| Profile → role | # Skill 名称 |
| Profile → description | 功能描述 |
| Goals | 核心能力 + 使用场景 |
| Constrains | 注意事项 |
| Skills | 核心能力 |
| Workflows | 工作流程 |
| OutputFormat | 输出格式 |

---

## 六、实施计划

### 6.1 阶段划分

#### 阶段一：基础设施搭建（Day 1）
1. 创建 Skills 目录结构
2. 创建 SKILL.md 模板文件
3. 编写 Skills README.md 总览文档

#### 阶段二：核心 Skills 转换（Day 2-3）
按优先级转换以下核心 Skills：
1. 故事分析类（8个）
2. 人物分析类（2个）
3. 评估筛选类（4个）

#### 阶段三：创作与工具 Skills 转换（Day 4）
1. 创作策划类（2个）
2. 工具辅助类（4个）
3. 知识检索类（2个）

#### 阶段四：工作流与结果处理（Day 5）
1. 工作流编排类（2个）
2. 结果处理类（2个）
3. 剧集分析类（1个）
4. 小说初筛类（4个）

#### 阶段五：测试与优化（Day 6）
1. Skills 功能测试
2. 跨 Skills 协作测试
3. 文档完善

### 6.2 质量标准

每个 SKILL.md 必须满足以下标准：
- [ ] Frontmatter 完整（name, description）
- [ ] 功能描述清晰准确
- [ ] 使用场景具体明确
- [ ] 工作流程步骤清晰
- [ ] 输入输出格式明确
- [ ] 包含使用示例
- [ ] 注意事项完整

---

## 七、Skills 使用指南

### 7.1 安装 Skills

将 skills 文件夹放置在 Claude Code 支持的位置：
```
.claude/skills/
```

### 7.2 调用 Skills

在对话中直接提及 skill 名称即可激活：

```
用户：使用 story-plot-analyzer 分析以下故事文本...
```

### 7.3 Skills 组合使用

多个 skills 可以组合使用以完成复杂任务：

```
用户：先用 story-summarizer 生成大纲，然后用 character-profile 生成人物小传...
```

---

## 八、附录

### 8.1 完整 Skills 映射表

| 序号 | 原文件 | Skill ID | Skill 名称 | 类别 |
|------|--------|----------|------------|------|
| 1 | drama_analysis_system.txt | drama-analyzer | 剧本分析专家 | SA |
| 2 | major_plot_points_system.txt | plot-keypoints | 大情节点分析专家 | SA |
| 3 | detailed_plot_points_system.txt | detailed-plot-analyzer | 详细情节点分析专家 | SA |
| 4 | plot_points_analyzer_system.txt | plot-points-analyzer | 情节点分析专家 | SA |
| 5 | story_type_analyzer_system.txt | story-type-analyzer | 题材类型与创意提炼专家 | SA |
| 6 | story_summary_generator_system.txt | story-summarizer | 故事梗概生成专家 | SA |
| 7 | story_summary_system.txt | story-outliner | 故事大纲生成专家 | SA |
| 8 | story_five_elements_system.txt | story-five-elements | 故事五元素分析专家 | SA |
| 9 | character_profile_generator_system.txt | character-profile | 人物小传生成专家 | CA |
| 10 | character_relationship_analyzer_system.txt | character-relationships | 人物关系分析专家 | CA |
| 11 | ip_evaluation_agent_system.txt | ip-evaluator | IP评估专家 | EV |
| 12 | script_evaluation_agent_system.txt | script-evaluator | 影视剧本评估专家 | EV |
| 13 | short_drama_evaluation_system.txt | drama-evaluator | 竖屏短剧评估专家 | EV |
| 14 | novel_screening_prompts.py (story_evaluation) | story-outline-evaluator | 故事大纲评估专家 | EV |
| 15 | short_drama_creater_system.txt | drama-creator | 竖屏短剧剧本创作大师 | CR |
| 16 | short_drama_planner_system.txt | drama-planner | 竖屏短剧策划师 | CR |
| 17 | series_analysis_system.txt | series-analyzer | 已播剧集分析与拉片专家 | SS |
| 18 | drama_workflow_system.txt | drama-workflow | 情节点戏剧功能分析工作流编排器 | WF |
| 19 | plot_points_workflow_system.txt | plot-workflow | 大情节点与详细情节点工作流编排专家 | WF |
| 20 | result_integrator_system.txt | result-integrator | 结果整合工具 | RP |
| 21 | output_formatter_system.txt | output-formatter | 输出整理专家 | RP |
| 22 | file_reference_system.txt | file-reference | 文件引用解析专家 | TL |
| 23 | text_truncator_system.txt | text-truncator | 文本截断工具 | TL |
| 24 | text_splitter_system.txt | text-splitter | 文本分割工具 | TL |
| 25 | mind_map_system.txt | mind-map-generator | 思维导图生成专家 | TL |
| 26 | knowledge_system.txt | knowledge-query | 竖屏短剧知识库查询专家 | KR |
| 27 | websearch_system.txt | web-search | 竖屏短剧网络检索专家 | KR |
| 28 | novel_screening_prompts.py (story_summary) | novel-summarizer | 故事大纲生成专家 | NS |
| 29 | novel_screening_prompts.py (story_evaluation) | novel-evaluator | 资深的故事评估专家 | NS |
| 30 | novel_screening_prompts.py (score_analyzer) | score-analyzer | 评分分析智能体 | NS |
| 31 | novel_screening_prompts.py (text_truncator) | novel-truncator | 文本截断工具智能体 | NS |

### 8.2 技能依赖关系

```
story-five-elements (五元素分析)
    ├── story-type-analyzer (题材分析)
    ├── story-summarizer (故事梗概)
    ├── character-profile (人物小传)
    ├── character-relationships (人物关系)
    ├── plot-keypoints (大情节点)
    └── mind-map-generator (思维导图)

drama-workflow (戏剧分析工作流)
    ├── text-truncator (文本截断)
    ├── text-splitter (文本分割)
    ├── drama-analyzer (剧本分析)
    └── result-integrator (结果整合)
```

---

## 九、更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-01-10 | 初始版本，完成整体规划 |

---

**文档结束**
