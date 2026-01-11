# Skills 版本管理规范

> 文档版本：1.0
> 更新日期：2026-01-10

---

## 一、版本号规则

### 1.1 语义化版本

采用 `major.minor.patch` 格式：

- **major (主版本号)**: 重大功能变更或不兼容的修改
- **minor (次版本号)**: 新增功能或向后兼容的修改
- **patch (修订号)**: 问题修复或小的改进

示例：
- `1.0.0` - 初始版本
- `1.1.0` - 新增示例
- `1.1.1` - 修复描述错误
- `2.0.0` - 重构核心内容

### 1.2 版本信息位置

在每个 SKILL.md 的 frontmatter 中添加：

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
    changes: 初始版本
---
```

---

## 二、变更记录模板

### 2.1 变更类型

| 类型 | 说明 | 标识 |
|------|------|------|
| 新增 | 新增功能或内容 | `added` |
| 优化 | 优化现有内容 | `improved` |
| 修复 | 修复问题 | `fixed` |
| 移除 | 移除功能或内容 | `removed` |
| 重大 | 重大变更 | `breaking` |

### 2.2 变更记录格式

```markdown
## 版本历史

| 版本 | 日期 | 变更类型 | 变更说明 |
|------|------|----------|----------|
| 1.1.0 | 2026-01-15 | added | 新增3个使用示例 |
| 1.0.1 | 2026-01-12 | fixed | 修复输出格式错误 |
| 1.0.0 | 2026-01-10 | - | 初始版本 |
```

---

## 三、更新流程

### 3.1 更新前的检查

- [ ] 确认修改的性质（新增/优化/修复）
- [ ] 确定版本号的变化
- [ ] 准备变更说明
- [ ] 测试修改后的内容

### 3.2 更新步骤

1. 更新 frontmatter 中的 `version` 和 `last_updated`
2. 在 `changelog` 数组开头添加新的变更记录
3. 在文档末尾更新版本历史表格
4. 提交变更

---

## 四、版本管理示例

### 示例 1：新增示例

```yaml
---
name: drama-analyzer
description: 深入分析故事文本，提炼主要情节点并分析戏剧功能
category: story-analysis
version: 1.1.0
last_updated: 2026-01-15
changelog:
  - version: 1.1.0
    date: 2026-01-15
    changes:
      - type: added
        content: 新增都市情感剧本分析示例
      - type: added
        content: 新增悬疑剧分析示例
      - type: improved
        content: 优化输出格式说明
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: 初始版本
---
```

### 示例 2：修复问题

```yaml
---
name: plot-keypoints
description: 梳理故事主要脉络，提炼主要情节点
category: story-analysis
version: 1.0.1
last_updated: 2026-01-12
changelog:
  - version: 1.0.1
    date: 2026-01-12
    changes:
      - type: fixed
        content: 修复输出格式示例中的错误
  - version: 1.0.0
    date: 2026-01-10
    changes:
      - type: added
        content: 初始版本
---
```

---

## 五、当前所有 Skills 版本状态

| Skill ID | 当前版本 | 最后更新 | 状态 |
|----------|----------|----------|------|
| story-analysis 类 | 1.0.0 | 2026-01-10 | 稳定 |
| character-analysis 类 | 1.0.0 | 2026-01-10 | 稳定 |
| evaluation 类 | 1.0.0 | 2026-01-10 | 稳定 |
| creation 类 | 1.0.0 | 2026-01-10 | 稳定 |
| series-analysis 类 | 1.0.0 | 2026-01-10 | 稳定 |
| workflow 类 | 1.0.0 | 2026-01-10 | 稳定 |
| result-processing 类 | 1.0.0 | 2026-01-10 | 稳定 |
| tools 类 | 1.0.0 | 2026-01-10 | 稳定 |
| knowledge-research 类 | 1.0.0 | 2026-01-10 | 稳定 |
| novel-screening 类 | 1.0.0 | 2026-01-10 | 稳定 |

---

## 六、版本发布计划

### 即将发布
- 无计划中的版本更新

### 讨论中
- 为所有 skills 添加更多真实场景示例
- 优化部分冗长的输出格式说明
- 添加技能组合使用的快捷指令

---

## 七、更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-01-10 | 初始版本，建立版本管理规范 |
