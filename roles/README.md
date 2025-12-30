# AI 角色定义

本文件夹包含 Paper Master 系统的核心 AI 角色定义文档。

## 角色概览

| 角色 | 文件 | 职责 | 输入 | 输出 |
|------|------|------|------|------|
| **格式分析师** | [Format_Analyst.md](./Format_Analyst.md) | 分析论文格式要求 | 格式要求文档 | 《格式规范》 |
| **资料查询者** | [Research_Collector.md](./Research_Collector.md) | 网络查询相关资料 | 论文主题 | 《资料汇编》《参考文献》 |
| **大纲创作师** | [Outline_Architect.md](./Outline_Architect.md) | 创建论文大纲 | 格式规范、资料 | 《论文大纲》 |
| **内容填充者** | [Content_Writer.md](./Content_Writer.md) | 分部分撰写内容 | 大纲、资料 | 各章节 MD 文件 |
| **HTML 格式化专家** | [HTML_Formatter.md](./HTML_Formatter.md) | 生成 Word 兼容 HTML | 所有内容 | HTML 文件 |

## 工作流程

```
用户输入论文要求
    ↓
[Format_Analyst] 格式分析师
    ↓ 输出《格式规范》
[Research_Collector] 资料查询者
    ↓ 输出《资料汇编》《参考文献》
[Outline_Architect] 大纲创作师
    ↓ 输出《论文大纲》（用户确认）
[Content_Writer] 内容填充者
    ↓ 逐部分撰写，输出各章节 MD
    ↓ （可迭代修改）
[HTML_Formatter] HTML 格式化专家
    ↓ 输出 HTML 文件
浏览器打开 → 复制 → 粘贴到 Word
```

## 角色详解

### 1️⃣ Format_Analyst（格式分析师）

**何时使用**：项目开始时（首要步骤）

**核心能力**：
- 解析用户提供的格式要求文档
- 标准化格式规范输出
- 识别特殊要求（图表、公式、页眉页脚等）

**关键输出**：《格式规范》，包含字体、字号、行距、页边距、标题层级等

📄 [查看完整定义](./Format_Analyst.md)

---

### 2️⃣ Research_Collector（资料查询者）

**何时使用**：格式规范完成后

**核心能力**：
- 网络搜索相关学术资料
- 整理资料摘要
- 生成 GB/T 7714 格式参考文献

📄 [查看完整定义](./Research_Collector.md)

---

### 3️⃣ Outline_Architect（大纲创作师）

**何时使用**：资料汇编完成后

**核心能力**：
- 设计论文结构
- 分配各部分字数
- 规划论证逻辑

📄 [查看完整定义](./Outline_Architect.md)

---

### 4️⃣ Content_Writer（内容填充者）

**何时使用**：大纲确认后

**核心能力**：
- 学术写作风格
- 逐部分撰写
- 整合引用资料

**工作方式**：每次只写一个章节，支持迭代修改

📄 [查看完整定义](./Content_Writer.md)

---

### 5️⃣ HTML_Formatter（HTML 格式化专家）

**何时使用**：所有内容完成后

**核心能力**：
- 组合所有章节内容
- 生成 Word 兼容的 HTML
- 应用格式规范中的样式

📄 [查看完整定义](./HTML_Formatter.md)

---

## 使用建议

### 基本流程

1. 准备格式要求文档（放入 `templates/user/`）
2. 从 **Format_Analyst** 开始，完成格式确认
3. **Research_Collector** 查询资料
4. **Outline_Architect** 创建大纲并确认
5. **Content_Writer** 逐部分撰写
6. **HTML_Formatter** 生成最终 HTML

### 最佳实践

- ⭐ 格式分析师的「初次确认」是首要步骤
- ✅ 大纲完成后请用户确认再继续
- ✅ 内容逐部分撰写，每部分单独保存
- ✅ 最终 HTML 在浏览器中预览后再复制

---

## 相关文档

- [主 README](../README.md)
- [工作流指南](../docs/workflow_guide.md)
- [HTML 转 Word 指南](../docs/html_to_word_guide.md)
