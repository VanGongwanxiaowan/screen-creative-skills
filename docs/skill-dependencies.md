# Skills 依赖关系文档

> 文档版本：1.0
> 更新日期：2026-01-10

---

## 概述

本文档描述了所有 Skills 之间的依赖关系、调用关系，以及推荐的组合使用方式。

---

## 一、依赖关系图

### 1.1 核心依赖链

```
story-five-elements (故事五元素分析)
    ├── story-type-analyzer (题材分析)
    ├── story-summarizer (故事梗概)
    ├── character-profile (人物小传)
    │   └── story-outliner (需要故事大纲作为输入)
    ├── character-relationships (人物关系)
    │   └── character-profile (需要人物信息)
    ├── plot-keypoints (大情节点)
    └── mind-map-generator (思维导图生成)
            └── plot-keypoints (需要情节点数据)

drama-workflow (戏剧分析工作流)
    ├── text-truncator (文本截断)
    ├── text-splitter (文本分割)
    ├── drama-analyzer (剧本分析)
    │   └── plot-keypoints (需要情节点定义)
    └── result-integrator (结果整合)
            └── drama-analyzer (需要分析结果)

plot-workflow (情节工作流)
    ├── plot-keypoints (大情节点)
    ├── detailed-plot-analyzer (详细情节点)
    │   └── plot-keypoints (需要大情节点)
    └── output-formatter (输出格式化)
            └── detailed-plot-analyzer (需要分析结果)

series-analyzer (剧集分析)
    ├── story-five-elements (五元素分析)
    ├── drama-analyzer (拉片分析)
    ├── web-search (联网搜索)
    └── result-integrator (结果整合)
```

### 1.2 评估链依赖

```
评估决策流程：
    ↓
ip-evaluator (IP评估)
    ↓ (通过)
story-outline-evaluator (大纲评估)
    ↓ (通过)
drama-evaluator (短剧评估)
    ↓ (通过)
script-evaluator (剧本评估)
```

### 1.3 创作链依赖

```
drama-planner (短剧策划)
    ↓
drama-creator (剧本创作)
    ↓
script-evaluator (剧本评估)
    ↓ (根据评估结果)
drama-creator (剧本优化)
```

---

## 二、Skill 调用关系表

### 2.1 被 调用最多的 Skills

| Skill Name | 被以下 Skills 调用 |
|------------|-------------------|
| `story-outliner` | story-five-elements, character-profile, character-relationships |
| `plot-keypoints` | story-five-elements, drama-analyzer, detailed-plot-analyzer |
| `character-profile` | story-five-elements, character-relationships |
| `drama-analyzer` | drama-workflow, series-analyzer |
| `result-integrator` | drama-workflow, plot-workflow, series-analyzer |

### 2.2 输入依赖关系

| Skill Name | 需要的输入 | 推荐的前置 Skill |
|------------|-----------|-----------------|
| `character-profile` | 故事文本 | story-outliner, story-summarizer |
| `character-relationships` | 人物信息 | character-profile |
| `plot-keypoints` | 故事文本 | story-outliner |
| `detailed-plot-analyzer` | 大情节点 | plot-keypoints |
| `mind-map-generator` | 情节点数据 | plot-keypoints, detailed-plot-analyzer |
| `script-evaluator` | 剧本内容 | drama-creator |
| `result-integrator` | 多个分析结果 | drama-analyzer, plot-points-analyzer |

---

## 三、推荐的组合使用模式

### 3.1 完整故事分析流程

```
用户请求：深度分析这个故事

推荐组合：
1. story-outliner → 生成故事大纲
2. story-type-analyzer → 分析题材类型
3. plot-keypoints → 提取大情节点
4. character-profile → 生成人物小传
5. character-relationships → 分析人物关系
6. mind-map-generator → 生成思维导图

一键替代：story-five-elements
```

### 3.2 IP 评估决策流程

```
用户请求：评估这个 IP 是否值得开发

推荐组合：
1. ip-evaluator → IP 初步评估
   ↓ (评分 >= 8.0)
2. story-outline-evaluator → 大纲详细评估
   ↓ (评分 >= 8.0)
3. drama-evaluator → 短剧改编潜力评估
   ↓ (评分 >= 8.0)
4. 给出最终建议
```

### 3.3 剧本创作流程

```
用户请求：帮我创作一个短剧剧本

推荐组合：
1. drama-planner → 制定策划方案
   ↓
2. drama-creator → 创作剧本
   ↓
3. script-evaluator → 评估剧本质量
   ↓ (根据评估结果)
4. drama-creator → 优化剧本
```

### 3.4 已播剧集学习流程

```
用户请求：分析这部已播剧集

推荐组合：
series-analyzer (一站式完成)
  - 自动调用：story-five-elements
  - 自动调用：drama-analyzer
  - 自动调用：web-search
  - 自动调用：result-integrator
```

### 3.5 长文本深度分析流程

```
用户请求：深度分析这个长文本故事

推荐组合：
drama-workflow (自动编排)
  - text-truncator → 截断长文本
  - text-splitter → 分割文本块
  - drama-analyzer → 并行分析
  - result-integrator → 整合结果
```

---

## 四、Skill 功能矩阵

### 4.1 按功能分类

| 功能类别 | 可用的 Skills |
|----------|--------------|
| **文本理解** | story-outliner, story-summarizer, story-type-analyzer, drama-analyzer |
| **情节分析** | plot-keypoints, detailed-plot-analyzer, plot-points-analyzer |
| **人物分析** | character-profile, character-relationships |
| **质量评估** | ip-evaluator, script-evaluator, drama-evaluator, story-outline-evaluator |
| **内容创作** | drama-creator, drama-planner |
| **工具支持** | text-truncator, text-splitter, file-reference, mind-map-generator |
| **信息检索** | knowledge-query, web-search |
| **结果整合** | result-integrator, output-formatter |

### 4.2 按使用场景分类

| 使用场景 | 推荐的 Skills |
|----------|--------------|
| **快速了解故事** | story-outliner, story-summarizer |
| **深度故事分析** | story-five-elements, drama-workflow |
| **人物开发** | character-profile → character-relationships |
| **情节设计** | plot-keypoints → detailed-plot-analyzer |
| **IP 决策** | ip-evaluator → story-outline-evaluator → drama-evaluator |
| **剧本创作** | drama-planner → drama-creator → script-evaluator |
| **学习优秀作品** | series-analyzer |
| **长文本处理** | drama-workflow (自动编排) |

---

## 五、Skill 能力对比

### 5.1 相似 Skill 对比

| 功能 | Skill A | Skill B | 区别 |
|------|---------|---------|------|
| 故事总结 | story-outliner | story-summarizer | outliner: 300-500字<br>summarizer: 提炼要点 |
| 情节点分析 | plot-keypoints | detailed-plot-analyzer | keypoints: 梳理主要脉络<br>detailed: 深入扩展分析 |
| 情节点分析 | drama-analyzer | plot-points-analyzer | drama: 分析戏剧功能<br>plot-points: 识别转折点 |
| 评估 | ip-evaluator | story-outline-evaluator | IP: 网络信息梳理<br>outline: 大纲质量评估 |
| 评估 | drama-evaluator | script-evaluator | drama: 短剧改编潜力<br>script: 剧本三维度评估 |

### 5.2 选择建议

```
Q: 需要生成故事大纲？
A: 文本较短 → story-outliner (300-500字)
   文本较长 → story-summarizer (提炼要点)
   完整分析 → story-five-elements (包含大纲)

Q: 需要分析情节点？
A: 快速梳理 → plot-keypoints
   深度分析 → detailed-plot-analyzer
   戏剧功能 → drama-analyzer
   转折分析 → plot-points-analyzer

Q: 需要评估质量？
A: IP 改编决策 → ip-evaluator
   大纲质量 → story-outline-evaluator
   短剧潜力 → drama-evaluator
   剧本质量 → script-evaluator
```

---

## 六、使用建议

### 6.1 单个 Skill 使用

适合场景：
- 需要完成单一、明确的任务
- 已经知道具体需要什么能力
- 快速获取特定信息

示例：
```
用户：用 story-outliner 给我生成一个故事大纲
用户：用 character-profile 分析这个人物
```

### 6.2 组合 Skill 使用

适合场景：
- 需要完成复杂的多步骤任务
- 需要全面的分析或创作
- 不确定具体使用哪些 skills

示例：
```
用户：深度分析这个故事
    → 自动使用 story-five-elements

用户：评估这个 IP 是否值得开发
    → 自动使用评估决策流程

用户：帮我创作一个短剧
    → 自动使用创作流程
```

### 6.3 工作流 Skill 使用

适合场景：
- 处理复杂的长文本
- 需要多步骤的自动化流程
- 需要整合多个分析结果

示例：
```
用户：分析这个长篇小说
    → 自动使用 drama-workflow

用户：分析这部电视剧
    → 自动使用 series-analyzer
```

---

## 七、更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-01-10 | 初始版本，建立依赖关系文档 |
