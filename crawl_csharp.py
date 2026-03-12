#!/usr/bin/env python3
"""爬取 C# SDK 帮助文档，保存为 markdown 文件。"""

import os
import re
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
BASE_URL = "https://emt.18.cn/api/quant-help/csharp"

# C# 文档页面：(文件名, HTML页面)
CS_PAGES = [
    ("70_CSharp快速开始.md", "cs-guide.html"),
    ("71_CSharp典型场景.md", "cs-typical-scene.html"),
    ("72_CSharp重要概念.md", "cs-important-concepts.html"),
    ("73_CSharp策略基类.md", "cs-base-class-proto.html"),
    ("74_CSharp基本成员函数.md", "cs-basic-member-func.html"),
    ("75_CSharp行情成员函数.md", "cs-quotation-member-func.html"),
    ("76_CSharp交易成员函数.md", "cs-trade-member-func.html"),
    ("77_CSharp动态参数成员函数.md", "cs-dynamic-params-member-func.html"),
    ("78_CSharp事件成员函数.md", "cs-event-member-func.html"),
    ("79_CSharp行情数据查询.md", "cs-data-search-func-history.html"),
    ("80_CSharp通用数据函数.md", "cs-data-search-func-generic.html"),
    ("81_CSharp股票财务数据.md", "cs-data-search-func-stock.html"),
    ("82_CSharp股票增值数据.md", "cs-data-search-func-stock-vip.html"),
    ("83_CSharp期货基础数据.md", "cs-data-search-func-future.html"),
    ("84_CSharp期货增值数据.md", "cs-data-search-func-future-vip.html"),
    ("85_CSharp基金增值数据.md", "cs-data-search-func-fund.html"),
    ("86_CSharp可转债数据.md", "cs-data-search-func-bond.html"),
    ("87_CSharp结果集合类.md", "cs-gm-data-list.html"),
    ("88_CSharp_GMData.md", "cs-gm-data.html"),
    ("89_CSharp数据结构.md", "cs-cxx_object_data.html"),
    ("90_CSharp交易类.md", "cs-cxx_object_trade.html"),
    ("91_CSharp枚举常量.md", "cs-enum-const.html"),
    ("92_CSharp错误码.md", "cs-error-code.html"),
]


class HTMLToMarkdown(HTMLParser):
    """简易 HTML -> Markdown 转换器（复用 crawl_docs.py 逻辑）"""

    def __init__(self):
        super().__init__()
        self.output = []
        self.current_tag = None
        self.tag_stack = []
        self.in_pre = False
        self.in_code = False
        self.in_table = False
        self.table_row = []
        self.table_rows = []
        self.in_td = False
        self.td_content = ""
        self.list_depth = 0
        self.ordered_list = False
        self.list_counter = 0
        self.skip_tags = {"script", "style", "nav", "footer", "header"}
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag in self.skip_tags:
            self.skip_depth += 1
            return
        if self.skip_depth > 0:
            return

        self.tag_stack.append(tag)
        self.current_tag = tag

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self.output.append("\n" + "#" * level + " ")
        elif tag == "p":
            self.output.append("\n\n")
        elif tag == "br":
            self.output.append("\n")
        elif tag == "strong" or tag == "b":
            self.output.append("**")
        elif tag == "em" or tag == "i":
            self.output.append("*")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.output.append("`")
        elif tag == "pre":
            self.in_pre = True
            self.output.append("\n```\n")
        elif tag == "a":
            href = attrs_dict.get("href", "")
            self.output.append("[")
            self._current_href = href
        elif tag == "img":
            alt = attrs_dict.get("alt", "")
            src = attrs_dict.get("src", "")
            self.output.append(f"![{alt}]({src})")
        elif tag == "ul":
            self.list_depth += 1
            self.ordered_list = False
        elif tag == "ol":
            self.list_depth += 1
            self.ordered_list = True
            self.list_counter = 0
        elif tag == "li":
            indent = "  " * (self.list_depth - 1)
            if self.ordered_list:
                self.list_counter += 1
                self.output.append(f"\n{indent}{self.list_counter}. ")
            else:
                self.output.append(f"\n{indent}- ")
        elif tag == "table":
            self.in_table = True
            self.table_rows = []
        elif tag == "tr":
            self.table_row = []
        elif tag in ("td", "th"):
            self.in_td = True
            self.td_content = ""
        elif tag == "blockquote":
            self.output.append("\n> ")
        elif tag == "hr":
            self.output.append("\n---\n")

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip_depth -= 1
            return
        if self.skip_depth > 0:
            return

        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.output.append("\n")
        elif tag == "strong" or tag == "b":
            self.output.append("**")
        elif tag == "em" or tag == "i":
            self.output.append("*")
        elif tag == "code" and not self.in_pre:
            self.in_code = False
            self.output.append("`")
        elif tag == "pre":
            self.in_pre = False
            self.output.append("\n```\n")
        elif tag == "a":
            href = getattr(self, "_current_href", "")
            self.output.append(f"]({href})")
        elif tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            if self.list_depth == 0:
                self.output.append("\n")
        elif tag in ("td", "th"):
            self.in_td = False
            self.table_row.append(self.td_content.strip())
        elif tag == "tr":
            if self.table_row:
                self.table_rows.append(self.table_row)
        elif tag == "table":
            self.in_table = False
            if self.table_rows:
                self._render_table()
        elif tag == "p":
            self.output.append("\n")

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        if self.in_td:
            self.td_content += data
        elif self.in_pre:
            self.output.append(data)
        else:
            text = data
            if not self.in_code:
                text = re.sub(r'\n\s+', ' ', text)
            self.output.append(text)

    def _render_table(self):
        if not self.table_rows:
            return
        cols = max(len(r) for r in self.table_rows)
        for row in self.table_rows:
            while len(row) < cols:
                row.append("")
        self.output.append("\n\n")
        header = self.table_rows[0]
        self.output.append("| " + " | ".join(header) + " |\n")
        self.output.append("| " + " | ".join(["---"] * cols) + " |\n")
        for row in self.table_rows[1:]:
            self.output.append("| " + " | ".join(row) + " |\n")
        self.output.append("\n")

    def get_markdown(self):
        text = "".join(self.output)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def fetch_page(url):
    """获取页面 HTML 内容"""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            # 提取 <body> 内容
            body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
            if body_match:
                return body_match.group(1)
            # 有些页面没有完整body，直接解析全文
            return html
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  ✗ 获取失败: {e}")
        return None


def html_to_markdown(html):
    """将 HTML 转换为 Markdown"""
    parser = HTMLToMarkdown()
    parser.feed(html)
    return parser.get_markdown()


def clean_markdown(text):
    """清理转换后的 markdown"""
    # 移除导航面包屑
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        # 跳过面包屑导航
        if re.match(r'^(快速开始|Python|C\+\+|C#|Matlab|智能策略|数据文档|常见问题)\s*$', line.strip()):
            continue
        if line.strip() == '量化终端帮助中心':
            continue
        # 跳过空链接
        if re.match(r'^\[?\]?\(#?\)?\s*$', line.strip()):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)

    total = len(CS_PAGES)
    success = 0
    failed = 0

    for i, (filename, page) in enumerate(CS_PAGES, 1):
        filepath = os.path.join(DOCS_DIR, filename)
        url = f"{BASE_URL}/{page}"
        print(f"[{i}/{total}] {filename}")
        print(f"  URL: {url}")

        html = fetch_page(url)
        if html is None:
            failed += 1
            continue

        markdown = html_to_markdown(html)
        markdown = clean_markdown(markdown)

        if len(markdown) < 50:
            print(f"  ✗ 内容过少 ({len(markdown)} chars)")
            failed += 1
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"  ✓ 成功: {len(markdown):,} chars")
        success += 1
        time.sleep(0.5)

    print(f"\n爬取完成: {success}/{total} 成功, {failed} 失败")


if __name__ == "__main__":
    main()
