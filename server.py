#!/usr/bin/env python3
"""
东方财富量化终端文档 MCP 服务器
提供文档搜索、章节查看、目录列表等工具
"""

import os
import re
from mcp.server.fastmcp import FastMCP

# 文档目录
DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

# 初始化 MCP 服务器
mcp = FastMCP("emquant-docs", instructions="""\
东方财富量化终端（掘金量化）帮助文档查询服务。

## 推荐调用流程
1. **定位文档**: 先调 `list_topics` 按分组浏览文档目录，确定目标文件名
2. **关键词搜索**: 用 `search_docs` 跨所有文档搜索关键词（多词空格分隔取交集）
3. **查看函数定义**: 用 `search_api` 直接搜索函数名（如 history、order_volume），优先返回 API 定义章节
4. **深入阅读**: 用 `get_document` 查看整个文档（大文件自动分页），或 `get_section` 定位特定章节
5. **快速查引**: 用 `get_quickstart` 获取常见任务（下单、获取行情、回测等）的快速指引
6. **辅助查询**: `get_enum_constants` 查枚举、`get_error_codes` 查错误码、`get_faq` 查常见问题

## 文档覆盖范围
- 入门指南（终端使用、策略开发入门）
- Python SDK 完整 API（数据函数、交易函数、事件、枚举常量、错误码）
- C# SDK 完整 API（策略基类、成员函数、数据查询、交易、数据结构、枚举常量）
- 数据文档（股票/基金/期货/指数/可转债/板块的字段说明和数据指标）
- 常见问题 FAQ

## 注意事项
- 大文档（>2万字符）会自动分页，返回提示中有 next_offset 翻页参数
- `get_section` 会包含目标章节的所有子章节内容
- 数据文档中引用的函数名可用 `search_api` 进一步查看详细定义（同时搜索 Python 和 C# 文档）
""")


def _load_docs() -> dict[str, str]:
    """加载所有 markdown 文档到内存"""
    docs = {}
    if not os.path.isdir(DOCS_DIR):
        return docs
    for fname in sorted(os.listdir(DOCS_DIR)):
        if fname.endswith(".md"):
            path = os.path.join(DOCS_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                docs[fname] = f.read()
    return docs


# 启动时加载文档
_docs_cache = _load_docs()


# ── MCP Resources ─────────────────────────────────────────
@mcp.resource(
    "emquant://docs/{filename}",
    name="emquant_doc",
    title="EMQuant 文档",
    description="获取指定 EMQuant 文档的完整内容。filename 为文档文件名，如 10_Python介绍.md",
    mime_type="text/markdown",
)
def doc_resource(filename: str) -> str:
    content = _docs_cache.get(filename)
    if content:
        return content
    for fname in _docs_cache:
        if filename.lower() in fname.lower():
            return _docs_cache[fname]
    return f"未找到文档 '{filename}'"


@mcp.resource(
    "emquant://docs",
    name="emquant_doc_index",
    title="EMQuant 文档索引",
    description="获取所有可用文档的列表及其大小",
    mime_type="text/plain",
)
def doc_index_resource() -> str:
    lines = []
    for fname in sorted(_docs_cache.keys()):
        title = _get_topic_title(fname)
        size = len(_docs_cache[fname])
        lines.append(f"{fname}: {title} ({size} 字符)")
    return "\n".join(lines)


# ── Helper functions ──────────────────────────────────────

def _get_topic_title(filename: str) -> str:
    """从文件名提取主题标题"""
    name = filename.replace(".md", "")
    # 去掉序号前缀 (如 "10_")
    name = re.sub(r"^\d+_", "", name)
    return name


@mcp.tool()
def list_topics() -> str:
    """列出所有可用的文档主题，按类别分组。返回文件名和主题，可用于 get_document / get_section 查看内容。"""
    categories = [
        ("📖 入门指南", lambda f: f.startswith("0")),
        ("🐍 Python SDK — 基础与架构", lambda f: re.match(r"^1[0-4]_", f)),
        ("🐍 Python SDK — 数据函数", lambda f: re.match(r"^1[5-9]_|^2[0-5]_", f)),
        ("🐍 Python SDK — 交易函数", lambda f: re.match(r"^2[6-9]_|^3[0-1]_", f)),
        ("🐍 Python SDK — 其他", lambda f: re.match(r"^3[2-6]_", f)),
        ("🤖 智能策略", lambda f: f.startswith("4")),
        ("📊 数据文档（按品种）", lambda f: f.startswith("5")),
        ("❓ 常见问题", lambda f: f.startswith("6")),
        ("🔷 C# SDK — 入门与架构", lambda f: re.match(r"^7[0-3]_", f)),
        ("🔷 C# SDK — 成员函数", lambda f: re.match(r"^7[4-8]_", f)),
        ("🔷 C# SDK — 数据查询", lambda f: re.match(r"^[89][0-9]_.*CSharp", f) and "数据" in f or re.match(r"^7[9]_|^8[0-6]_", f)),
        ("🔷 C# SDK — 数据结构与其他", lambda f: re.match(r"^8[7-9]_|^9[0-2]_", f)),
    ]
    lines = []
    categorized = set()
    for label, pred in categories:
        items = [(f, _get_topic_title(f), len(_docs_cache[f]))
                 for f in sorted(_docs_cache) if pred(f)]
        if items:
            lines.append(f"\n**{label}**")
            for fname, title, size in items:
                lines.append(f"  - {fname}: {title} ({size:,} 字符)")
                categorized.add(fname)
    # 未分类
    uncategorized = [f for f in sorted(_docs_cache) if f not in categorized]
    if uncategorized:
        lines.append("\n**📄 其他**")
        for fname in uncategorized:
            lines.append(f"  - {fname}: {_get_topic_title(fname)} ({len(_docs_cache[fname]):,} 字符)")
    return "\n".join(lines).strip() if lines else "未找到文档文件"


@mcp.tool()
def search_docs(query: str, max_results: int = 10) -> str:
    """在所有文档中搜索关键词。支持多个关键词（空格分隔，取交集）。

    Args:
        query: 搜索关键词，多个关键词用空格分隔
        max_results: 最大返回结果数，默认10
    """
    keywords = query.lower().split()
    if not keywords:
        return "请提供搜索关键词"

    results = []
    for fname, content in _docs_cache.items():
        content_lower = content.lower()
        # 所有关键词都必须匹配
        if not all(kw in content_lower for kw in keywords):
            continue

        # 找到包含关键词的段落
        paragraphs = re.split(r"\n#{1,6}\s", content)
        headers = re.findall(r"^(#{1,6}\s.+)$", content, re.MULTILINE)

        matched_sections = []
        for i, para in enumerate(paragraphs):
            para_lower = para.lower()
            if any(kw in para_lower for kw in keywords):
                # 找最近的标题
                header = ""
                header_candidates = re.findall(r"^(#{1,6}\s.+)$", para, re.MULTILINE)
                if header_candidates:
                    header = header_candidates[0].strip()
                
                # 截取包含关键词的上下文
                lines = para.split("\n")
                for j, line in enumerate(lines):
                    if any(kw in line.lower() for kw in keywords):
                        start = max(0, j - 2)
                        end = min(len(lines), j + 5)
                        snippet = "\n".join(lines[start:end]).strip()
                        if len(snippet) > 500:
                            snippet = snippet[:500] + "..."
                        matched_sections.append({
                            "header": header,
                            "snippet": snippet
                        })
                        break

        if matched_sections:
            title = _get_topic_title(fname)
            for sec in matched_sections[:3]:  # 每个文件最多3个匹配
                entry = f"📄 **{title}** ({fname})"
                if sec["header"]:
                    entry += f"\n   {sec['header']}"
                entry += f"\n```\n{sec['snippet']}\n```"
                results.append(entry)

    results = results[:max_results]
    if not results:
        return f"未找到包含 '{query}' 的文档内容"

    return f"找到 {len(results)} 条结果：\n\n" + "\n\n---\n\n".join(results)


def _extract_toc(content: str) -> str:
    """从文档内容提取目录（所有标题行）"""
    headers = re.findall(r"^(#{1,6}\s.+)$", content, re.MULTILINE)
    if not headers:
        return "(无目录)"
    return "\n".join(headers)


def _find_doc(filename: str) -> tuple[str, str] | tuple[None, None]:
    """按精确名或模糊匹配查找文档，返回 (filename, content)"""
    if filename in _docs_cache:
        return filename, _docs_cache[filename]
    for fname in _docs_cache:
        if filename.lower() in fname.lower() or fname.lower() in filename.lower():
            return fname, _docs_cache[fname]
    return None, None


MAX_DOC_CHARS = 20000  # 约 5000 tokens


@mcp.tool()
def get_document(filename: str, offset: int = 0) -> str:
    """获取指定文档的内容。大文件自动分页，每次返回约 20000 字符。

    Args:
        filename: 文档文件名，如 "15_Python基础函数.md"。支持模糊匹配。
        offset: 起始字符偏移量，默认0。大文件需多次调用，依次传入返回的 next_offset。
    """
    fname, content = _find_doc(filename)
    if content is None:
        return f"未找到文档 '{filename}'。请使用 list_topics 查看可用文档。"

    total = len(content)
    prefix = f"（匹配到: {fname}）\n\n" if fname != filename else ""

    if total <= MAX_DOC_CHARS and offset == 0:
        return prefix + content

    # 分页模式
    chunk = content[offset:offset + MAX_DOC_CHARS]
    end = offset + len(chunk)
    has_more = end < total

    header = f"📄 {fname} [{offset+1}-{end}/{total} 字符]"
    if offset == 0:
        # 首页附带目录
        toc = _extract_toc(content)
        header += f"\n\n**目录：**\n{toc}\n\n---\n"

    footer = ""
    if has_more:
        footer = f"\n\n---\n⏩ 还有 {total - end} 字符未显示。调用 get_document('{fname}', offset={end}) 获取下一页。"

    return prefix + header + "\n\n" + chunk + footer


@mcp.tool()
def get_section(filename: str, section_title: str) -> str:
    """获取指定文档中某个章节的内容。

    Args:
        filename: 文档文件名
        section_title: 章节标题关键词
    """
    content = _docs_cache.get(filename)
    if not content:
        # 模糊匹配文件名
        for fname in _docs_cache:
            if filename.lower() in fname.lower():
                content = _docs_cache[fname]
                filename = fname
                break
    if not content:
        return f"未找到文档 '{filename}'"

    # 按标题分割，保留标题行
    sections = re.split(r"(^#{1,6}\s.+$)", content, flags=re.MULTILINE)

    matched = []
    search_lower = section_title.lower()
    i = 0
    while i < len(sections):
        m = re.match(r"^(#{1,6})\s", sections[i])
        if m and search_lower in sections[i].lower():
            header_level = len(m.group(1))  # 匹配标题的级别
            parts = [sections[i]]
            if i + 1 < len(sections):
                parts.append(sections[i + 1])
            # 向后收集子标题（级别更深的标题及其内容）
            j = i + 2
            while j < len(sections):
                sub_m = re.match(r"^(#{1,6})\s", sections[j])
                if sub_m:
                    if len(sub_m.group(1)) <= header_level:
                        break  # 遇到同级或更高级标题，停止
                    parts.append(sections[j])  # 子标题
                    if j + 1 < len(sections):
                        parts.append(sections[j + 1])  # 子标题的内容
                    j += 2
                else:
                    j += 1
            result_text = "\n".join(p.strip() for p in parts if p.strip())
            if len(result_text) > MAX_DOC_CHARS:
                result_text = result_text[:MAX_DOC_CHARS] + "\n\n... (内容过长已截断)"
            matched.append(result_text)
        i += 1

    if not matched:
        return f"在 {filename} 中未找到包含 '{section_title}' 的章节"

    return "\n\n---\n\n".join(matched)


@mcp.tool()
def search_api(function_name: str) -> str:
    """搜索特定 API 函数的文档。适合查找函数签名、参数、返回值等。
    优先返回标题中包含函数名的章节（即正式 API 定义），其次返回正文提及的内容。

    Args:
        function_name: 函数名称，如 "history", "order_volume", "get_position"
    """
    fn_lower = function_name.lower().replace("-", "_")
    # (priority, text) — priority 越小越靠前
    scored_results: list[tuple[int, str]] = []

    # 优先搜索 Python API 文档（15_~36_）和 C# API 文档（74_~92_），然后是其他文档
    api_files = sorted(
        _docs_cache.keys(),
        key=lambda f: (0 if re.match(r"^(1[5-9]|2\d|3[0-6])_", f) else
                       0 if re.match(r"^(7[4-9]|8\d|9[0-2])_", f) else 1, f)
    )

    for fname in api_files:
        content = _docs_cache[fname]
        if fn_lower not in content.lower():
            continue

        sections = re.split(r"(^#{1,6}\s.+$)", content, flags=re.MULTILINE)
        title = _get_topic_title(fname)
        is_api_file = bool(re.match(r"^(1[5-9]|2\d|3[0-6]|7[4-9]|8\d|9[0-2])_", fname))

        i = 0
        while i < len(sections):
            section_text = sections[i]

            if re.match(r"^#{1,6}\s", section_text) and fn_lower in section_text.lower():
                # 标题直接包含函数名 — 最高优先
                header = section_text
                body = sections[i + 1] if i + 1 < len(sections) else ""
                if len(body) > 3000:
                    body = body[:3000] + "\n\n... (内容过长已截断，使用 get_section 获取完整内容)"
                priority = 0 if is_api_file else 2
                scored_results.append((priority, f"📄 **{title}** ({fname})\n\n{header}\n{body.strip()}"))
            elif not re.match(r"^#{1,6}\s", section_text) and fn_lower in section_text.lower():
                # 正文提及函数名 — 低优先
                lines = section_text.split("\n")
                for j, line in enumerate(lines):
                    if fn_lower in line.lower():
                        start = max(0, j - 3)
                        end = min(len(lines), j + 10)
                        snippet = "\n".join(lines[start:end]).strip()
                        if len(snippet) > 2000:
                            snippet = snippet[:2000] + "..."
                        prev_header = sections[i - 1] if i > 0 and re.match(r"^#{1,6}\s", sections[i - 1]) else ""
                        priority = 1 if is_api_file else 3
                        scored_results.append((priority, f"📄 **{title}** ({fname})\n\n{prev_header}\n{snippet}"))
                        break
            i += 1

    if not scored_results:
        return f"未找到函数 '{function_name}' 的文档。请检查函数名拼写。"

    # 按优先级排序，取前5
    scored_results.sort(key=lambda x: x[0])
    return "\n\n---\n\n".join(r[1] for r in scored_results[:5])


@mcp.tool()
def get_enum_constants(language: str = "python") -> str:
    """获取枚举常量文档，包括订单类型、持仓方向、市场代码等。

    Args:
        language: 编程语言，可选 "python"（默认）或 "csharp"
    """
    target = "CSharp" if language.lower() in ("csharp", "c#", "cs") else "Python"
    for fname in sorted(_docs_cache.keys()):
        if "枚举常量" in fname and target in fname:
            return _docs_cache[fname]
    # fallback: 返回任意一个
    for fname, content in _docs_cache.items():
        if "枚举常量" in fname:
            return content
    return "未找到枚举常量文档"


@mcp.tool()
def get_error_codes(language: str = "python") -> str:
    """获取错误码文档，用于排查 API 调用错误。

    Args:
        language: 编程语言，可选 "python"（默认）或 "csharp"
    """
    target = "CSharp" if language.lower() in ("csharp", "c#", "cs") else "Python"
    for fname in sorted(_docs_cache.keys()):
        if "错误码" in fname and target in fname:
            return _docs_cache[fname]
    for fname, content in _docs_cache.items():
        if "错误码" in fname:
            return content
    return "未找到错误码文档"


@mcp.tool()
def get_faq(topic: str = "") -> str:
    """获取常见问题解答。可选指定主题筛选。不指定 topic 时返回问题目录列表。

    Args:
        topic: 筛选关键词，如 "回测", "仿真", "数据", "SDK", "安装"。留空则返回目录。
    """
    for fname, content in _docs_cache.items():
        if "常见问题" in fname:
            if not topic:
                # 返回 FAQ 目录而非全文
                toc = _extract_toc(content)
                return f"## 常见问题目录\n\n{toc}\n\n💡 请使用 `get_faq(topic='关键词')` 查看具体问题，如 get_faq(topic='回测')"
            # 按主题筛选
            sections = re.split(r"(^#{1,4}\s.+$)", content, flags=re.MULTILINE)
            matched = []
            topic_lower = topic.lower()
            i = 0
            while i < len(sections):
                if i + 1 < len(sections) and re.match(r"^#{1,4}\s", sections[i]):
                    full = sections[i] + sections[i + 1]
                    if topic_lower in full.lower():
                        if len(full) > MAX_DOC_CHARS:
                            full = full[:MAX_DOC_CHARS] + "\n\n... (内容过长已截断)"
                        matched.append(full.strip())
                i += 1
            if matched:
                result = "\n\n---\n\n".join(matched)
                if len(result) > MAX_DOC_CHARS:
                    result = result[:MAX_DOC_CHARS] + "\n\n... (结果过长已截断，请缩小搜索范围)"
                return result
            return f"未找到与 '{topic}' 相关的常见问题"
    return "未找到常见问题文档"


# ── 常见任务快速指引 ──────────────────────────────────────
_QUICKSTART_GUIDES = {
    "行情": {
        "title": "获取行情数据",
        "steps": [
            "1. 实时快照: `current(symbols)` — 查询最新 Tick（免费）",
            "2. 历史K线: `history(symbol, frequency, start_time, end_time, fields)` — 日/分钟线",
            "3. 最新N条: `history_n(symbol, frequency, count, fields)` — 最新 N 根 K 线",
            "4. 数据订阅: 在 `init` 中调用 `subscribe(symbols, frequency)`, 在 `on_bar`/`on_tick` 中接收推送",
        ],
        "docs": ["18_Python行情数据查询.md", "16_Python数据订阅.md", "17_Python数据事件.md"],
    },
    "下单": {
        "title": "委托下单",
        "steps": [
            "1. 按量下单: `order_volume(symbol, volume, side, order_type, position_effect, price)`",
            "2. 按金额下单: `order_value(symbol, value, side, order_type, position_effect, price)`",
            "3. 目标持仓: `order_target_volume(symbol, volume, position_side, order_type)`",
            "4. 撤单: `order_cancel(wait_cancel_orders)` 或 `order_cancel_all()`",
            "5. 必须参数: side=OrderSide_Buy/Sell, order_type=OrderType_Limit/Market, position_effect=PositionEffect_Open/Close",
        ],
        "docs": ["26_Python交易函数.md", "35_Python枚举常量.md"],
    },
    "回测": {
        "title": "策略回测",
        "steps": [
            "1. `init` 中设置: `subscribe(symbols, '1d')` 订阅数据",
            "2. `on_bar` 中编写交易逻辑",
            "3. `run(filename, strategy_id, token, mode=MODE_BACKTEST, backtest_start_time, backtest_end_time, backtest_initial_cash)`",
            "4. 回测结果包含: 收益率、夏普比率、最大回撤等绩效指标",
        ],
        "docs": ["15_Python基础函数.md", "10_Python快速开始.md", "01_策略指引.md"],
    },
    "仿真": {
        "title": "仿真交易",
        "steps": [
            "1. 在掘金终端创建仿真交易账户",
            "2. `run(filename, strategy_id, token, mode=MODE_LIVE, account=account_id)`",
            "3. 策略运行后可在终端监控持仓、委托、成交",
        ],
        "docs": ["15_Python基础函数.md", "01_策略指引.md", "00_终端指引.md"],
    },
    "财务": {
        "title": "获取财务数据",
        "steps": [
            "1. 基础财务: `get_fundamentals(table, symbols, start_date, end_date, fields)`",
            "2. 单季/累计: `get_fundamentals_n(table, symbols, count, fields)`",
            "3. 可用表: trading_derivative_indicator（交易衍生）, balance_sheet（资产负债）, income_statement（利润表）等",
        ],
        "docs": ["20_Python股票财务数据.md", "19_Python通用数据函数.md"],
    },
    "选股": {
        "title": "条件选股",
        "steps": [
            "1. 标的查询: `get_symbol_infos(sec_type, exchanges)` — 获取标的列表",
            "2. 筛选数据: `get_fundamentals` 获取财务指标 + `history` 获取行情",
            "3. 组合筛选: 在 Python 中对 DataFrame 做条件过滤",
        ],
        "docs": ["19_Python通用数据函数.md", "20_Python股票财务数据.md"],
    },
    "持仓": {
        "title": "查询持仓和账户",
        "steps": [
            "1. 查持仓: `get_position()` — 返回所有持仓",
            "2. 查资金: `get_cash()` — 账户资金信息",
            "3. 查委托: `get_orders()` — 当日所有委托",
            "4. 查成交: `get_execution_reports()` — 成交回报",
        ],
        "docs": ["27_Python交易查询函数.md", "14_Python数据结构_交易类.md"],
    },
}


@mcp.tool()
def get_quickstart(task: str) -> str:
    """获取常见量化任务的快速入门指引。

    Args:
        task: 任务名称，可选值: 行情, 下单, 回测, 仿真, 财务, 选股, 持仓。也支持模糊匹配。
    """
    task_lower = task.lower()

    # 精确匹配
    if task_lower in _QUICKSTART_GUIDES:
        guide = _QUICKSTART_GUIDES[task_lower]
    else:
        # 模糊匹配
        matched = [(k, v) for k, v in _QUICKSTART_GUIDES.items()
                    if k in task_lower or task_lower in k or task_lower in v["title"]]
        if not matched:
            available = ", ".join(_QUICKSTART_GUIDES.keys())
            return f"未找到 '{task}' 的快速指引。可用任务: {available}"
        guide = matched[0][1]

    lines = [f"# {guide['title']}\n"]
    for step in guide["steps"]:
        lines.append(step)
    lines.append(f"\n📚 **相关文档**: {', '.join(guide['docs'])}")
    lines.append("💡 使用 `search_api` 可查看上述函数的完整参数说明")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
