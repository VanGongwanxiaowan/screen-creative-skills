# 文件引用解析专家 - 详细示例

## 示例 1: 解析单个文件引用

### 输入

```
请解析以下文件引用：

@file://data/stories/story1.txt
```

### 输出

```
【文件引用解析结果】

文件路径：data/stories/story1.txt
引用类型：本地文件引用

建议操作：
1. 读取文件内容
2. 检查文件是否存在
3. 验证文件格式是否正确
```

## 示例 2: 解析多个文件引用

### 输入

```
请解析以下文件引用：

第一个故事：@file://data/stories/story1.txt
第二个故事：@file://data/stories/story2.txt
背景资料：@file://data/background/info.md
```

### 输出

```
【文件引用解析结果】

识别到3个文件引用：

1. 文件路径：data/stories/story1.txt
   引用类型：故事文本

2. 文件路径：data/stories/story2.txt
   引用类型：故事文本

3. 文件路径：data/background/info.md
   引用类型：背景资料

建议操作：
1. 按顺序读取所有文件
2. 验证每个文件的完整性
3. 整合文件内容进行分析
```

## 示例 3: 解析URL引用

### 输入

```
请解析以下引用：

@url://https://example.com/article/how-to-write-drama
```

### 输出

```
【文件引用解析结果】

URL：https://example.com/article/how-to-write-drama
引用类型：网络资源引用

建议操作：
1. 使用WebFetch工具获取URL内容
2. 提取文章的核心内容
3. 整合到分析中
```

## 示例 4: 解析混合引用

### 输入

```
请解析以下引用：

故事文本：@file://project/stories/main_story.txt
参考资料：@url://https://drama-guide.com/techniques
用户备注：@file://project/notes/user_notes.md
```

### 输出

```
【文件引用解析结果】

识别到3个引用：

1. 本地文件：project/stories/main_story.txt（故事文本）
2. 网络资源：https://drama-guide.com/techniques（参考资料）
3. 本地文件：project/notes/user_notes.md（用户备注）

建议操作：
1. 优先读取主故事文件
2. 获取网络参考资料作为辅助
3. 读取用户备注了解特殊要求
4. 整合所有内容进行分析
```
