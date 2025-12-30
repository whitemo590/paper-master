# 工具集

本目录包含 Paper Master 的实用工具脚本。

## 工具列表

### project_manager.py — 项目管理工具

项目初始化、验证和管理的一站式工具。

**功能**：
- 初始化新论文项目（创建标准目录结构）
- 验证项目完整性
- 查看项目信息

**用法**：

```bash
# 初始化新项目
python tools/project_manager.py init <项目名称>

# 验证项目结构
python tools/project_manager.py validate <项目路径>

# 查看项目信息
python tools/project_manager.py info <项目路径>
```

**示例**：

```bash
# 创建一个新的论文项目
python tools/project_manager.py init 大数据应急管理

# 验证项目
python tools/project_manager.py validate projects/大数据应急管理_20251230

# 查看项目信息
python tools/project_manager.py info projects/大数据应急管理_20251230
```

---

## 相关文档

- [主 README](../README.md)
- [工作流指南](../docs/workflow_guide.md)
