#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper Master 项目管理工具

功能：
- 初始化新论文项目
- 验证项目结构
- 查看项目信息

用法：
    python project_manager.py init <项目名称>
    python project_manager.py validate <项目路径>
    python project_manager.py info <项目路径>
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


# 项目根目录
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

# 项目结构模板
PROJECT_STRUCTURE = {
    "dirs": [
        "content",
        "output"
    ],
    "files": {
        "格式规范.md": """# 格式规范

> 此文件由 Format_Analyst 角色生成

## 基本信息
- 论文类型：
- 字数要求：
- 参考文献格式：GB/T 7714

## 页面设置
- 纸张大小：A4
- 页边距：上 2.5cm / 下 2.5cm / 左 2.5cm / 右 2.5cm

## 字体规范

| 元素 | 中文字体 | 英文字体 | 字号 |
|------|----------|----------|------|
| 论文标题 | 黑体 | Times New Roman | 二号 |
| 一级标题 | 黑体 | Times New Roman | 三号 |
| 二级标题 | 黑体 | Times New Roman | 四号 |
| 正文 | 宋体 | Times New Roman | 小四 |

## 段落格式
- 行距：1.5 倍
- 段首缩进：2 字符
""",
        "论文大纲.md": """# 论文大纲

> 此文件由 Outline_Architect 角色生成

## 基本信息
- **论文题目**：
- **总字数要求**：

---

## 正文结构

### 1. 引言（约 X 字）
- 1.1 研究背景
- 1.2 研究意义
- 1.3 研究内容与方法

### 2. [章节名称]（约 X 字）
- 2.1 
- 2.2 

### 3. 结论（约 X 字）
- 3.1 主要结论
- 3.2 研究展望

---

## 参考文献

""",
        "资料汇编.md": """# 资料汇编

> 此文件由 Research_Collector 角色生成

## 论文主题


## 关键词


---

## 一、核心概念

## 二、相关理论

## 三、研究现状

## 四、数据资料

## 五、案例资料

## 六、关键观点摘录

""",
        "参考文献.md": """# 参考文献

> 按 GB/T 7714 格式整理

## 期刊论文
[1] 

## 专著
[2] 

## 网络文献
[3] 

""",
        "README.md": """# 论文项目

## 项目信息
- 创建时间：{date}
- 论文主题：

## 文件说明
- `格式规范.md` - 格式规范文档
- `论文大纲.md` - 论文结构大纲
- `资料汇编.md` - 资料整理
- `参考文献.md` - 参考文献列表
- `content/` - 各章节内容
- `output/` - HTML 输出

## 工作流程
1. Format_Analyst → 格式规范
2. Research_Collector → 资料汇编
3. Outline_Architect → 论文大纲
4. Content_Writer → 各章节内容
5. HTML_Formatter → HTML 输出
"""
    }
}


def init_project(name: str) -> None:
    """初始化新论文项目"""
    # 生成项目目录名（带日期）
    date_str = datetime.now().strftime("%Y%m%d")
    project_name = f"{name}_{date_str}"
    project_path = PROJECT_ROOT / "projects" / project_name
    
    # 检查是否已存在
    if project_path.exists():
        print(f"❌ 项目已存在：{project_path}")
        return
    
    # 创建项目目录
    project_path.mkdir(parents=True, exist_ok=True)
    print(f"📁 创建项目目录：{project_path}")
    
    # 创建子目录
    for dir_name in PROJECT_STRUCTURE["dirs"]:
        dir_path = project_path / dir_name
        dir_path.mkdir(exist_ok=True)
        print(f"  📂 {dir_name}/")
    
    # 创建文件
    for file_name, content in PROJECT_STRUCTURE["files"].items():
        file_path = project_path / file_name
        # 替换模板变量
        content = content.replace("{date}", datetime.now().strftime("%Y-%m-%d"))
        file_path.write_text(content, encoding="utf-8")
        print(f"  📄 {file_name}")
    
    print(f"\n✅ 项目初始化完成：{project_path}")
    print("\n下一步：")
    print("1. 将格式要求文档放入 templates/user/ 目录")
    print("2. 在 AI 编辑器中打开项目")
    print("3. 开始与 AI 对话，创建论文")


def validate_project(path: str) -> bool:
    """验证项目结构"""
    project_path = Path(path)
    
    if not project_path.exists():
        print(f"❌ 项目路径不存在：{path}")
        return False
    
    print(f"🔍 验证项目：{project_path.name}")
    print("=" * 50)
    
    errors = []
    warnings = []
    
    # 检查必需目录
    for dir_name in PROJECT_STRUCTURE["dirs"]:
        dir_path = project_path / dir_name
        if not dir_path.exists():
            warnings.append(f"缺少目录：{dir_name}/")
    
    # 检查必需文件
    required_files = ["格式规范.md", "论文大纲.md"]
    for file_name in required_files:
        file_path = project_path / file_name
        if not file_path.exists():
            warnings.append(f"缺少文件：{file_name}")
    
    # 检查 content 目录是否有内容
    content_path = project_path / "content"
    if content_path.exists():
        content_files = list(content_path.glob("*.md"))
        if len(content_files) == 0:
            warnings.append("content/ 目录为空，尚未撰写内容")
        else:
            print(f"✅ 已撰写 {len(content_files)} 个章节")
    
    # 检查 output 目录
    output_path = project_path / "output"
    if output_path.exists():
        html_files = list(output_path.glob("*.html"))
        if len(html_files) > 0:
            print(f"✅ 已生成 HTML 文件")
        else:
            warnings.append("output/ 目录为空，尚未生成 HTML")
    
    # 输出结果
    if errors:
        print("\n❌ 错误：")
        for err in errors:
            print(f"  - {err}")
    
    if warnings:
        print("\n⚠️ 警告：")
        for warn in warnings:
            print(f"  - {warn}")
    
    if not errors and not warnings:
        print("\n✅ 项目结构完整")
    
    return len(errors) == 0


def show_info(path: str) -> None:
    """显示项目信息"""
    project_path = Path(path)
    
    if not project_path.exists():
        print(f"❌ 项目路径不存在：{path}")
        return
    
    print(f"📋 项目信息：{project_path.name}")
    print("=" * 50)
    
    # 统计文件
    md_files = list(project_path.glob("*.md"))
    content_files = list((project_path / "content").glob("*.md")) if (project_path / "content").exists() else []
    html_files = list((project_path / "output").glob("*.html")) if (project_path / "output").exists() else []
    
    print(f"📁 项目路径：{project_path}")
    print(f"📄 规范文档：{len(md_files)} 个")
    print(f"📝 章节内容：{len(content_files)} 个")
    print(f"🌐 HTML 输出：{len(html_files)} 个")
    
    # 列出内容文件
    if content_files:
        print("\n📝 已撰写章节：")
        for f in sorted(content_files):
            print(f"  - {f.name}")


def main():
    parser = argparse.ArgumentParser(
        description="Paper Master 项目管理工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python project_manager.py init 我的论文
  python project_manager.py validate projects/我的论文_20251230
  python project_manager.py info projects/我的论文_20251230
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # init 子命令
    init_parser = subparsers.add_parser("init", help="初始化新论文项目")
    init_parser.add_argument("name", help="项目名称")
    
    # validate 子命令
    validate_parser = subparsers.add_parser("validate", help="验证项目结构")
    validate_parser.add_argument("path", help="项目路径")
    
    # info 子命令
    info_parser = subparsers.add_parser("info", help="查看项目信息")
    info_parser.add_argument("path", help="项目路径")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_project(args.name)
    elif args.command == "validate":
        validate_project(args.path)
    elif args.command == "info":
        show_info(args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
