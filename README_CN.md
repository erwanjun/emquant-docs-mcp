# emquant-docs-mcp

[English](./README.md) | **中文**

[![npm version](https://img.shields.io/npm/v/emquant-docs-mcp.svg)](https://www.npmjs.com/package/emquant-docs-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**东方财富量化终端（掘金量化）帮助文档 MCP 服务器**

基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 构建，让 AI 助手能直接查询东方财富量化终端的完整 SDK 文档，包括 Python 和 C# 两套 API。

## 功能特点

- 📚 **60 篇文档**：覆盖入门指南、Python SDK、C# SDK、数据文档、常见问题
- 🔍 **全文搜索**：跨所有文档的关键词搜索，支持多关键词取交集
- 🎯 **API 搜索**：按函数名精确查找 API 定义，优先展示函数签名和参数说明
- 📖 **智能分页**：大文档自动分页（每页约 2 万字符），附带目录导航
- 🏷️ **分类浏览**：按 8 大类别（入门/Python 基础/Python 数据/Python 交易/C# 入门/C# 函数/C# 数据/数据文档等）分组展示
- ⚡ **快速指引**：内置常见任务（行情、下单、回测、仿真等）的快速入门步骤
- 🖼️ **离线图片**：76 张文档截图已下载到本地，无需联网即可查看

## 文档覆盖

| 分类 | 数量 | 说明 |
|------|------|------|
| 入门指南 | 2 篇 | 终端使用、策略开发入门 |
| Python SDK | 27 篇 | 策略架构、数据结构、基础函数、行情查询、交易函数、事件、枚举、错误码 |
| C# SDK | 23 篇 | 快速开始、典型场景、策略基类、成员函数、数据查询、数据结构、枚举、错误码 |
| 数据文档 | 6 篇 | 股票、基金、期货、指数、可转债、板块的字段定义 |
| 智能策略 | 1 篇 | 智能策略功能说明 |
| 常见问题 | 1 篇 | FAQ |

## 提供的工具

| 工具 | 说明 |
|------|------|
| `list_topics` | 按类别列出所有可用文档 |
| `search_docs` | 全文关键词搜索（多词空格分隔取交集） |
| `search_api` | 搜索 API 函数定义（同时搜索 Python 和 C# 文档） |
| `get_document` | 获取完整文档（大文件自动分页） |
| `get_section` | 获取文档中指定章节（含子章节） |
| `get_enum_constants` | 获取枚举常量（支持 `language` 参数选择 Python/C#） |
| `get_error_codes` | 获取错误码（支持 `language` 参数选择 Python/C#） |
| `get_faq` | 获取常见问题（无参数返回目录，指定 topic 返回内容） |
| `get_quickstart` | 获取常见任务快速指引（行情/下单/回测/仿真/财务/选股/持仓） |

## 安装与使用

### 前置要求

- **Python 3.10+**
- **MCP SDK**：`pip install mcp`

### 方式一：通过 npx（推荐）

无需安装，直接在 MCP 客户端配置中使用：

```json
{
  "mcpServers": {
    "emquant-docs": {
      "command": "npx",
      "args": ["-y", "emquant-docs-mcp"]
    }
  }
}
```

### 方式二：全局安装

```bash
npm install -g emquant-docs-mcp
```

然后在配置中使用：

```json
{
  "mcpServers": {
    "emquant-docs": {
      "command": "emquant-docs-mcp"
    }
  }
}
```

### 方式三：从源码运行

```bash
git clone https://github.com/erwanjun/emquant-docs-mcp.git
cd emquant-docs-mcp
pip install mcp
python server.py
```

## 客户端配置

### VS Code (GitHub Copilot)

在 `.vscode/mcp.json` 或用户 `settings.json` 中添加：

```json
{
  "mcp": {
    "servers": {
      "emquant-docs": {
        "command": "npx",
        "args": ["-y", "emquant-docs-mcp"]
      }
    }
  }
}
```

### Claude Desktop

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`（macOS）或 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）：

```json
{
  "mcpServers": {
    "emquant-docs": {
      "command": "npx",
      "args": ["-y", "emquant-docs-mcp"]
    }
  }
}
```

### Cursor

在 Cursor 设置 → MCP Servers 中添加，配置同上。

## 使用示例

接入 MCP 服务后，你可以向 AI 助手提问：

- *"帮我查一下 order_volume 函数的参数"*
- *"如何用 Python 获取历史 K 线数据？"*
- *"C# SDK 怎么订阅行情？"*
- *"列出所有可用的枚举常量"*
- *"回测模式怎么配置？"*
- *"查一下错误码 1003 是什么意思"*

## 推荐调用流程

1. **定位文档**：先调 `list_topics` 浏览文档目录
2. **关键词搜索**：用 `search_docs` 跨所有文档搜索
3. **查看函数**：用 `search_api` 搜索函数名
4. **深入阅读**：用 `get_document` 或 `get_section` 查看详细内容
5. **快速查引**：用 `get_quickstart` 获取常见任务步骤
6. **辅助查询**：`get_enum_constants` / `get_error_codes` / `get_faq`

## 开发

```bash
# 克隆仓库
git clone https://github.com/erwanjun/emquant-docs-mcp.git
cd emquant-docs-mcp

# 安装依赖
pip install mcp

# 运行服务器
python server.py

# 运行测试
python test_changes.py
```

## 许可证

[MIT](LICENSE)
