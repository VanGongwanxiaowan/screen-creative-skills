# Agent Skills 优化指南

> 基于官方 Agent Skills 规范的优化指南
> 文档版本：1.0
> 更新日期：2026-01-11

---

## 一、Agent Skills 官方规范要点

### 1.1 Frontmatter 规范

**必需字段** (仅2个):
```yaml
---
name: skill-name              # 必需，1-64字符，仅小写字母、数字、连字符
description: Clear description # 必需，1-1024字符，描述功能+使用场景
---
```

**可选字段**:
```yaml
---
license: Apache-2.0                    # 许可证
compatibility: Claude Code 1.0+        # 兼容性说明
metadata:                              # 额外元数据 (建议保持精简)
  author: Author Name
  source: Original Source
allowed-tools:                         # 允许使用的工具列表
  - Read
  - Write
model: sonnet                          # 指定使用的模型
disable-model-invocation: false        # 是否禁用模型调用
mode: autonomous                       # 运行模式
---
```

### 1.2 Description 最佳实践

**好的描述**:
- 清楚说明"做什么" (what)
- 明确说明"何时使用" (when to use)
- 保持简洁，1-1024 字符
- 使用动作导向的语言

**示例对比**:

| 类型 | 示例 | 评价 |
|------|------|------|
| 差 | `这个技能是用来分析剧本的` | 缺少使用场景 |
| 中 | `分析故事文本，提炼情节点并分析戏剧功能` | 有功能但场景不明确 |
| 优 | `深入分析故事文本，提炼主要情节点并分析每个情节点的戏剧功能。适用于分析小说、剧本大纲、故事梗概等文本，识别关键转折点和情感节点` | 功能+场景明确 |

### 1.3 内容长度优化

**推荐做法**:
- 主 SKILL.md 文件控制在 **5000 词以内**
- 使用"渐进式信息披露" (Progressive Disclosure)
  1. **Frontmatter**: 约 100 tokens，用于技能发现
  2. **主内容**: 约 <5000 词，包含核心指令
  3. **外部引用**: 详细文档放在 `references/` 子目录

**外部引用格式**:
```markdown
## 详细文档

参见 `references/` 目录:
- `detailed-guide.md` - 完整使用指南
- `examples.md` - 更多示例
- `troubleshooting.md` - 故障排除
```

### 1.4 语言风格 - 命令式

**使用命令式语言** (Imperative Language):

| 避免 (错误) | 使用 (正确) |
|-----------|-----------|
| 你应该先分析... | 先分析... |
| 我们需要... | 分析... |
| 建议用户... | 让用户... |
| 可以考虑... | 考虑... |

**标准动词**:
- `分析` 而非 `进行分析`
- `提取` 而非 `进行提取`
- `生成` 而非 `进行生成`
- `评估` 而非 `进行评估`

### 1.5 路径变量规范

**必须使用路径变量**，禁止硬编码路径:

| 错误 (硬编码) | 正确 (变量) |
|-------------|------------|
| `/Users/gongfan/juben/skills/...` | `{baseDir}/...` |
| `C:\Users\Name\project\...` | `{baseDir}/...` |
| `./references/guide.md` | `{baseDir}/references/guide.md` |

**可用路径变量**:
- `{baseDir}` - skill 根目录
- `{cwd}` - 当前工作目录

---

## 二、优化检查清单

### 2.1 Frontmatter 检查

- [ ] `name` 字段仅含小写字母、数字、连字符
- [ ] `name` 长度在 1-64 字符
- [ ] `description` 清楚说明功能和使用场景
- [ ] `description` 长度在 1-1024 字符
- [ ] 添加 `category` 字段用于分类
- [ ] 添加 `version` 字段用于版本管理
- [ ] 考虑添加 `license` 和 `compatibility`

### 2.2 内容优化检查

- [ ] 主 SKILL.md 控制在 5000 词以内
- [ ] 使用命令式语言
- [ ] 移除冗余的"请"、"可以"等礼貌用语
- [ ] 将详细文档移至 `references/` 目录
- [ ] 使用路径变量代替硬编码路径
- [ ] 保持结构清晰，使用渐进式信息披露

### 2.3 版本管理检查

- [ ] 添加 `version` 字段
- [ ] 添加 `last_updated` 字段
- [ ] 添加 `changelog` 数组记录变更历史
- [ ] 在文档末尾添加版本历史表格

---

## 三、优化模板

### 3.1 简洁版 SKILL.md 模板

```yaml
---
name: skill-name
description: 简洁描述功能和使用场景，1-2句话说明清楚，控制在100-150字
category: category-name
version: 1.0.0
last_updated: 2026-01-11
changelog:
  - version: 1.0.0
    date: 2026-01-11
    changes:
      - type: added
        content: 初始版本
---

# Skill 名称

## 功能

[1-2句话描述核心功能]

## 使用场景

- [场景1]
- [场景2]

## 核心步骤

1. **步骤名称**: [命令式描述]
2. **步骤名称**: [命令式描述]
3. **步骤名称**: [命令式描述]

## 输入要求

- [输入1]
- [输入2]

## 输出格式

```
[输出格式模板]
```

## 示例

### 示例 1: [场景名称]

**输入**: [示例输入]

**输出**:
```
[示例输出]
```

## 详细文档

参见 `{baseDir}/references/` 目录获取更多文档:
- `guide.md` - 完整使用指南
- `examples.md` - 更多示例
- `changelog.md` - 变更历史

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0.0 | 2026-01-11 | 初始版本 |
```

### 3.2 Description 写作模板

```
[动作] + [对象] + [目的/结果]。适用于/用于 [使用场景1]、[使用场景2]、[使用场景3]
```

**示例**:
```
分析故事文本，提炼主要情节点并分析每个情节点的戏剧功能。适用于分析小说、剧本大纲、故事梗概等文本，识别故事中的关键转折点和情感节点
```

---

## 四、优化实施计划

### 4.1 第一阶段: Frontmatter 优化

1. 为所有 31 个 skills 优化 `description` 字段
2. 确保所有 `name` 符合命名规范
3. 添加标准化的 version 和 changelog

### 4.2 第二阶段: 内容精简

1. 将详细指南移至 `references/` 目录
2. 精简主 SKILL.md 内容
3. 使用命令式语言重写指令

### 4.3 第三阶段: 结构优化

1. 统一使用路径变量
2. 创建 references 目录结构
3. 更新文档引用

---

## 五、当前 Skills 状态分析

### 5.1 需要优化的项目

| 问题 | 影响范围 | 优先级 |
|------|---------|--------|
| Description 过于冗长 | 全部 31 个 | 高 |
| 使用非命令式语言 | 全部 31 个 | 高 |
| 缺少可选字段 | 全部 31 个 | 中 |
| 内容可能超过 5000 词 | 部分复杂 skills | 中 |
| 缺少 references 结构 | 全部 31 个 | 低 |

### 5.2 优化优先级

**第一批** (高优先级 - 核心分析类):
- drama-analyzer
- plot-keypoints
- story-type-analyzer
- story-five-elements

**第二批** (中优先级 - 评估和创作类):
- ip-evaluator
- drama-evaluator
- drama-creator
- drama-planner

**第三批** (标准优先级 - 其余 skills):
- 剩余 23 个 skills

---

## 六、优化示例

### 示例: 优化前 vs 优化后

#### 优化前 (drama-analyzer):

```yaml
---
name: drama-analyzer
description: 深入分析故事文本，提炼主要情节点并分析每个情节点的戏剧功能
category: story-analysis
version: 1.1.0
last_updated: 2026-01-10
changelog:
  - version: 1.1.0
    date: 2026-01-10
    changes:
      - type: added
        content: 添加都市情感剧、悬疑剧、职场剧等多场景示例
      - type: improved
        content: 完善使用示例和输出格式说明
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: 初始版本，从 agent prompt 转换为 skill
---

# 剧本分析专家

## 功能描述
基于资深编剧的专业视角，深入分析一段故事文本的内容...
[大量内容...]
```

#### 优化后:

```yaml
---
name: drama-analyzer
description: 分析故事文本，提炼主要情节点并分析戏剧功能。适用于分析小说、剧本大纲、故事梗概等文本，识别关键转折点和情感节点
category: story-analysis
version: 2.0.0
last_updated: 2026-01-11
changelog:
  - version: 2.0.0
    date: 2026-01-11
    changes:
      - type: breaking
        content: 按照 Agent Skills 官方规范重构
      - type: improved
        content: 优化 description，精简主内容，移动详细文档到 references/
  - version: 1.1.0
    date: 2026-01-10
    changes:
      - type: added
        content: 添加多场景示例
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: 初始版本
---

# 剧本分析专家

## 功能

分析故事文本，提炼主要情节点并分析每个情节点的戏剧功能。

## 使用场景

- 分析小说或故事文本的核心情节结构
- 识别故事中的关键转折点和情感节点
- 评估每个情节点的戏剧作用和推动力
- 为剧本改编提供情节分析基础

## 核心步骤

1. **深度阅读**: 充分阅读和理解故事文本内容
2. **情节点提炼**: 根据情节点定义，总结故事中的主要情节点
3. **戏剧功能分析**: 分析每个情节点的戏剧作用
4. **结构化输出**: 按照指定格式输出分析结果

## 输入要求

- 完整的故事文本（小说、剧本大纲、故事梗概等）
- 文本长度建议：500字以上

## 输出格式

```
【情节点】：<单个情节点描述>
【戏剧功能】：<该情节点的戏剧功能分析>
```

## 要求

- 每个情节点的表述不超过100字
- 至少提炼5个情节点
- 严格按照故事文本原文意思总结，不自行创作改编
- 不使用阿拉伯数字为情节点标号

## 示例

### 示例: 悬疑小说情节分析

**输入**:
```
[悬疑小说片段...]
```

**输出**:
```
【情节点】：主角收到神秘信件，声称知道其父亲死亡真相
【戏剧功能】：设置悬念钩子，引发观众好奇，推动主角展开调查

【情节点】：主角在调查过程中遭遇不明人士跟踪
【戏剧功能】：制造紧张氛围，暗示背后有秘密组织，升级冲突
```

## 详细文档

参见 `{baseDir}/references/` 获取更多文档:
- `guide.md` - 完整分析指南
- `examples.md` - 多场景示例
- `terminology.md` - 术语定义

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 2.0.0 | 2026-01-11 | 按官方规范重构，优化结构 |
| 1.1.0 | 2026-01-10 | 添加多场景示例 |
| 1.0.0 | 2026-01-10 | 初始版本 |
```

---

## 七、相关文档

- `PERFECT_SKILL_TEMPLATE.md` - 完美 SKILL.md 模板（包含完整示例）
- `SKILL_OPTIMIZATION_CHECKLIST.md` - 完整优化检查清单
- `README.md` - Skills 总览文档

## 八、参考资源

- [Agent Skills 官方规范](https://agentskills.io/specification)
- [Agent Skills GitHub](https://github.com/anthropics/skills)
- [Claude Agent Skills 深度解析](https://lih.substack.com/p/claude-agent-skills)

---

## 九、更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.1 | 2026-01-11 | 添加相关文档链接，完善优化指南 |
| 1.0 | 2026-01-11 | 初始版本，基于官方规范创建优化指南 |
