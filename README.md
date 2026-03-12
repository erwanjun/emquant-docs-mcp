# emquant-docs-mcp

**English** | [中文](./README_CN.md)

[![npm version](https://img.shields.io/npm/v/emquant-docs-mcp.svg)](https://www.npmjs.com/package/emquant-docs-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**MCP server for EMQuant (东方财富量化终端 / Goldminer Quant) documentation**

Built on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), this server lets AI assistants directly query the complete EMQuant SDK documentation, covering both Python and C# APIs.

## Features

- 📚 **60 Documents** — Covers getting started guides, Python SDK, C# SDK, data references, and FAQ
- 🔍 **Full-text Search** — Search across all docs with multi-keyword intersection support
- 🎯 **API Lookup** — Find function signatures, parameters, and return types by name
- 📖 **Smart Pagination** — Large documents auto-paginate (~20K chars/page) with table of contents
- 🏷️ **Categorized Browsing** — Documents organized into 8+ categories for easy discovery
- ⚡ **Quick Start Guides** — Built-in step-by-step guides for common tasks (quotes, trading, backtesting, etc.)
- 🖼️ **Offline Images** — 76 documentation screenshots bundled locally

## Documentation Coverage

| Category | Count | Description |
|----------|-------|-------------|
| Getting Started | 2 | Terminal setup, strategy development guide |
| Python SDK | 27 | Architecture, data structures, base functions, market data, trading, events, enums, error codes |
| C# SDK | 23 | Quick start, typical scenarios, base class, member functions, data queries, data structures, enums, error codes |
| Data Reference | 6 | Field definitions for stocks, funds, futures, indices, convertible bonds, sectors |
| Smart Strategy | 1 | Smart strategy features |
| FAQ | 1 | Frequently asked questions |

## Available Tools

| Tool | Description |
|------|-------------|
| `list_topics` | List all available documents grouped by category |
| `search_docs` | Full-text keyword search (space-separated keywords, intersection match) |
| `search_api` | Search API function definitions (searches both Python and C# docs) |
| `get_document` | Get full document content (auto-paginated for large files) |
| `get_section` | Get a specific section from a document (includes subsections) |
| `get_enum_constants` | Get enum constant definitions (supports `language` param: python/csharp) |
| `get_error_codes` | Get error codes (supports `language` param: python/csharp) |
| `get_faq` | Get FAQ (no args = TOC; specify `topic` for filtered results) |
| `get_quickstart` | Get quick start guides for common tasks (quotes/trading/backtesting/etc.) |

## Installation

### Prerequisites

- **Python 3.10+**
- **MCP SDK**: `pip install mcp`

### Option 1: Via npx (Recommended)

No installation needed — just configure your MCP client:

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

### Option 2: Global Install

```bash
npm install -g emquant-docs-mcp
```

Then use in your configuration:

```json
{
  "mcpServers": {
    "emquant-docs": {
      "command": "emquant-docs-mcp"
    }
  }
}
```

### Option 3: From Source

```bash
git clone https://github.com/erwanjun/emquant-docs-mcp.git
cd emquant-docs-mcp
pip install mcp
python server.py
```

## Client Configuration

### VS Code (GitHub Copilot)

Add to `.vscode/mcp.json` or user `settings.json`:

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

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

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

Add in Cursor Settings → MCP Servers with the same configuration as above.

## Usage Examples

After connecting the MCP server, you can ask your AI assistant:

- *"Show me the parameters for order_volume"*
- *"How to get historical K-line data with Python?"*
- *"How to subscribe to market data in C#?"*
- *"List all available enum constants"*
- *"How to configure backtesting mode?"*
- *"What does error code 1003 mean?"*

## Recommended Workflow

1. **Browse** — Call `list_topics` to discover available documents
2. **Search** — Use `search_docs` for keyword search across all docs
3. **API Lookup** — Use `search_api` to find function definitions
4. **Deep Read** — Use `get_document` or `get_section` for detailed content
5. **Quick Reference** — Use `get_quickstart` for common task step-by-step guides
6. **Helpers** — `get_enum_constants` / `get_error_codes` / `get_faq`

## Development

```bash
# Clone the repository
git clone https://github.com/erwanjun/emquant-docs-mcp.git
cd emquant-docs-mcp

# Install dependencies
pip install mcp

# Run the server
python server.py

# Run tests
python test_changes.py
```

## License

[MIT](LICENSE)
