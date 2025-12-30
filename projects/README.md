# 用户项目工作区

此目录用于存放用户的论文项目。

## 创建新项目

使用项目管理工具：

```bash
python tools/project_manager.py init <项目名称>
```

项目将自动创建在此目录下，命名格式为：`<项目名称>_<日期>`

## 目录结构

每个项目包含以下结构：

```
<项目名>_<日期>/
├── README.md           # 项目说明
├── 格式规范.md          # Format_Analyst 输出
├── 资料汇编.md          # Research_Collector 输出
├── 参考文献.md          # Research_Collector 输出
├── 论文大纲.md          # Outline_Architect 输出
├── content/            # Content_Writer 输出
│   ├── 00_摘要.md
│   ├── 01_引言.md
│   └── ...
└── output/             # HTML_Formatter 输出
    └── 论文.html
```
