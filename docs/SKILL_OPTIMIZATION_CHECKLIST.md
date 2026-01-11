# Agent Skills 优化检查清单

> 基于最佳实践的完整检查清单
> 版本：1.0.0
> 更新日期：2026-01-11

---

## 一、Frontmatter 检查清单

### 1.1 必需字段

- [ ] **name**: 
  - 仅含小写字母、数字、连字符
  - 长度在 1-64 字符
  - 格式：`category-function` 或 `function-name`
  
- [ ] **description**: 
  - 清楚说明功能（what）+ 使用场景（when）
  - 长度在 1-1024 字符
  - 使用命令式语言
  - 格式：`[功能描述]。适用于 [场景1]、[场景2]、[场景3]`

### 1.2 推荐字段

- [ ] **category**: 已添加正确的分类
- [ ] **version**: 使用语义化版本号（如 2.0.0）
- [ ] **last_updated**: 日期格式正确（YYYY-MM-DD）
- [ ] **license**: 已添加（推荐 MIT）
- [ ] **compatibility**: 已添加（如适用）
- [ ] **changelog**: 结构完整，包含所有历史版本

### 1.3 可选字段（按需添加）

- [ ] **author**: 作者信息（如需要）
- [ ] **source**: 来源信息（如需要）
- [ ] **allowed-tools**: 工具列表（如需要特定工具）
- [ ] **model**: 模型指定（如需要特定模型能力）
- [ ] **disable-model-invocation**: 是否禁用模型调用（如适用）
- [ ] **mode**: 运行模式（autonomous/interactive，如适用）

---

## 二、主内容检查清单

### 2.1 结构完整性

- [ ] **标题**: 清晰的中文标题，反映技能功能
- [ ] **功能**: 1-2句话清晰描述核心功能，使用命令式语言
- [ ] **使用场景**: 至少3个具体使用场景
- [ ] **核心步骤/工作流程**: 清晰的分步说明，使用命令式语言
- [ ] **输入要求**: 明确的输入格式、类型、要求
- [ ] **输出格式**: 使用代码块展示输出模板
- [ ] **约束条件/要求**: 清晰的使用约束和注意事项
- [ ] **示例**: 至少2个完整的输入输出示例
- [ ] **版本历史**: 完整的版本历史表格

### 2.2 语言风格

- [ ] 使用命令式语言（避免"应该"、"建议"、"可以"等）
- [ ] 避免冗余的礼貌用语（"请"、"麻烦"等）
- [ ] 使用标准动词（"分析"而非"进行分析"）
- [ ] 描述清晰简洁，避免冗长句式

### 2.3 内容质量

- [ ] 主 SKILL.md 控制在 5000 词以内（约 3000 中文字）
- [ ] 功能描述准确，不夸大
- [ ] 使用场景具体明确，避免泛化
- [ ] 示例真实有效，可直接使用
- [ ] 约束条件清晰，无歧义

### 2.4 路径和引用

- [ ] 所有路径使用变量 `{baseDir}` 代替硬编码路径
- [ ] 引用其他文档时使用正确的路径格式
- [ ] references 目录引用格式正确

---

## 三、References 检查清单

### 3.1 目录结构

- [ ] `references/` 目录已创建（如需要）
- [ ] `references/examples.md` 包含详细示例（推荐）
- [ ] 其他详细文档已移至 references/（如需要）

### 3.2 内容组织

- [ ] 主文件引用 references/ 目录
- [ ] references/ 中的文档结构清晰
- [ ] 详细内容从主文件移至 references/（如主文件超过4000词）

---

## 四、最佳实践检查

### 4.1 可发现性

- [ ] description 清楚说明功能和场景，便于搜索
- [ ] category 正确，便于分类查找
- [ ] 关键词准确，符合用户搜索习惯

### 4.2 可用性

- [ ] 示例完整，可直接复制使用
- [ ] 输入输出格式明确，无歧义
- [ ] 约束条件清晰，避免误用

### 4.3 可维护性

- [ ] 版本历史完整，便于追踪变更
- [ ] changelog 详细，说明变更原因
- [ ] 文档结构清晰，便于更新

---

## 五、分类检查清单

### 5.1 故事分析类 (story-analysis)

- [ ] 分析步骤清晰，逻辑严密
- [ ] 输出格式标准化，便于后续处理
- [ ] 示例覆盖主要故事类型

**已检查 Skills**:
- [ ] drama-analyzer
- [ ] plot-keypoints
- [ ] detailed-plot-analyzer
- [ ] plot-points-analyzer
- [ ] story-type-analyzer
- [ ] story-summarizer
- [ ] story-outliner
- [ ] story-five-elements

### 5.2 人物分析类 (character-analysis)

- [ ] 人物分析维度完整
- [ ] 输出格式清晰，信息结构化
- [ ] 示例覆盖不同类型人物

**已检查 Skills**:
- [ ] character-profile
- [ ] character-relationships

### 5.3 评估筛选类 (evaluation)

- [ ] 评估维度清晰，评分标准明确
- [ ] 输出报告结构完整
- [ ] 优化建议具体可落地

**已检查 Skills**:
- [ ] ip-evaluator
- [ ] script-evaluator
- [ ] drama-evaluator
- [ ] story-outline-evaluator

### 5.4 创作策划类 (creation)

- [ ] 创作方法论清晰
- [ ] 输出格式符合行业标准
- [ ] 示例展示不同创作任务

**已检查 Skills**:
- [ ] drama-creator
- [ ] drama-planner

### 5.5 工作流编排类 (workflow)

- [ ] 工作流步骤清晰
- [ ] 智能体协作机制明确
- [ ] 输出包含执行状态和结果

**已检查 Skills**:
- [ ] drama-workflow
- [ ] plot-workflow

### 5.6 工具辅助类 (tools)

- [ ] 工具功能明确，参数清晰
- [ ] 输出格式标准化
- [ ] 错误处理说明完整

**已检查 Skills**:
- [ ] file-reference
- [ ] text-truncator
- [ ] text-splitter
- [ ] mind-map-generator

### 5.7 其他类别

**已检查 Skills**:
- [ ] series-analyzer (剧集分析)
- [ ] result-integrator (结果处理)
- [ ] output-formatter (结果处理)
- [ ] knowledge-query (知识检索)
- [ ] web-search (知识检索)
- [ ] novel-summarizer (小说初筛)
- [ ] novel-evaluator (小说初筛)
- [ ] score-analyzer (小说初筛)
- [ ] novel-truncator (小说初筛)

---

## 六、优化优先级

### 高优先级（核心 Skills，已优化）

1. ✅ drama-analyzer - 剧本分析专家
2. ✅ story-five-elements - 故事五元素分析专家
3. ✅ character-profile - 人物小传生成专家
4. ✅ drama-evaluator - 竖屏短剧评估专家
5. ✅ drama-creator - 竖屏短剧剧本创作大师
6. ✅ ip-evaluator - IP评估专家

### 中优先级（重要 Skills，待优化）

7. [ ] plot-keypoints - 大情节点分析专家
8. [ ] detailed-plot-analyzer - 详细情节点分析专家
9. [ ] drama-planner - 竖屏短剧策划师
10. [ ] script-evaluator - 影视剧本评估专家
11. [ ] drama-workflow - 情节点戏剧功能分析工作流编排器
12. [ ] plot-workflow - 大情节点与详细情节点工作流编排专家

### 标准优先级（其他 Skills，按需优化）

13. [ ] 剩余 19 个 Skills

---

## 七、快速检查脚本

使用以下命令快速检查所有 Skills 的 Frontmatter：

```bash
# 检查所有 SKILL.md 文件的 Frontmatter
find skills/category -name "SKILL.md" -exec grep -l "^---" {} \;

# 检查 description 字段
find skills/category -name "SKILL.md" -exec grep "^description:" {} \;

# 检查 version 字段
find skills/category -name "SKILL.md" -exec grep "^version:" {} \;
```

---

## 八、优化建议

### 8.1 批量优化步骤

1. **第一步**: 检查所有 Skills 的 Frontmatter 完整性
2. **第二步**: 优化 description 字段，确保符合规范
3. **第三步**: 统一添加推荐字段（license, compatibility 等）
4. **第四步**: 优化主内容，使用命令式语言
5. **第五步**: 添加详细示例（至少2个）
6. **第六步**: 创建 references/ 目录（如需要）
7. **第七步**: 更新版本号和 changelog

### 8.2 常见问题修复

**问题1**: description 过于简单
- **修复**: 添加使用场景，使用"适用于..."格式

**问题2**: 使用非命令式语言
- **修复**: 将"应该分析"改为"分析"，"建议使用"改为"使用"

**问题3**: 缺少示例
- **修复**: 添加至少2个完整的输入输出示例

**问题4**: 主文件过长
- **修复**: 将详细内容移至 `references/examples.md`

**问题5**: 路径硬编码
- **修复**: 使用 `{baseDir}` 变量代替硬编码路径

---

## 九、完成度统计

### 总体进度

- **总 Skills 数**: 31
- **已优化**: 6 (19%)
- **待优化**: 25 (81%)

### 分类进度

| 类别 | 总数 | 已优化 | 待优化 | 完成度 |
|------|------|--------|--------|--------|
| 故事分析类 | 8 | 2 | 6 | 25% |
| 人物分析类 | 2 | 1 | 1 | 50% |
| 评估筛选类 | 4 | 2 | 2 | 50% |
| 创作策划类 | 2 | 1 | 1 | 50% |
| 工作流编排类 | 2 | 0 | 2 | 0% |
| 工具辅助类 | 4 | 0 | 4 | 0% |
| 其他类别 | 9 | 0 | 9 | 0% |

---

## 十、下一步行动

1. ✅ 创建完美模板和优化指南
2. ✅ 优化 6 个核心 Skills
3. ✅ 优化剩余 25 个 Skills（按优先级）
4. ✅ 创建缺失的 references/ 目录和文档
5. [ ] 更新 README.md 和规划文档
6. [ ] 进行全面检查和测试

---

**最后更新**: 2026-01-11
**维护者**: juben 项目团队

