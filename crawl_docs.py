#!/usr/bin/env python3
"""
爬取东方财富量化终端帮助文档，保存为 markdown 文件。
使用 emt.18.cn 的 API 端点直接获取 HTML 内容，然后转换为 markdown。
"""

import os
import re
import time
import urllib.request
import urllib.error
from html.parser import HTMLParser

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

# 文档页面列表：(文件名, URL)
DOC_PAGES = [
    # 终端指引
    ("00_终端指引.md", "https://emt.18.cn/api/quant-help/guide/guide.html"),
    ("01_策略指引.md", "https://emt.18.cn/api/quant-help/guide/559.html"),
    # Python SDK
    ("10_Python快速开始.md", "https://emt.18.cn/api/quant-help/python/quickstart.html"),
    ("11_Python策略架构.md", "https://emt.18.cn/api/quant-help/python/python_frame.html"),
    ("12_Python变量约定.md", "https://emt.18.cn/api/quant-help/python/python_concept.html"),
    ("13_Python数据结构_数据类.md", "https://emt.18.cn/api/quant-help/python/python_object_data.html"),
    ("14_Python数据结构_交易类.md", "https://emt.18.cn/api/quant-help/python/python_object_trade.html"),
    ("15_Python基础函数.md", "https://emt.18.cn/api/quant-help/python/python_basic.html"),
    ("16_Python数据订阅.md", "https://emt.18.cn/api/quant-help/python/python_subscribe.html"),
    ("17_Python数据事件.md", "https://emt.18.cn/api/quant-help/python/python_data_event.html"),
    ("18_Python行情数据查询.md", "https://emt.18.cn/api/quant-help/python/python_select_api_history.html"),
    ("19_Python通用数据函数.md", "https://emt.18.cn/api/quant-help/python/python_select_api_generic.html"),
    ("20_Python股票财务数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_stock.html"),
    ("21_Python股票增值数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_stock_vip.html"),
    ("22_Python期货基础数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_future.html"),
    ("23_Python期货增值数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_future_vip.html"),
    ("24_Python基金增值数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_fund_vip.html"),
    ("25_Python可转债数据.md", "https://emt.18.cn/api/quant-help/python/python_select_api_bond_vip.html"),
    ("26_Python交易函数.md", "https://emt.18.cn/api/quant-help/python/python_trade_api.html"),
    ("27_Python交易查询函数.md", "https://emt.18.cn/api/quant-help/python/trade_data.html"),
    ("28_Python两融交易函数.md", "https://emt.18.cn/api/quant-help/python/python-credit-trade-api.html"),
    ("29_Python_ETF交易函数.md", "https://emt.18.cn/api/quant-help/python/python_etf_trade_api.html"),
    ("30_Python算法交易函数.md", "https://emt.18.cn/api/quant-help/python/python_algo_trade.html"),
    ("31_Python交易事件.md", "https://emt.18.cn/api/quant-help/python/python_trade_event.html"),
    ("32_Python动态参数.md", "https://emt.18.cn/api/quant-help/python/python_parameter.html"),
    ("33_Python其他函数.md", "https://emt.18.cn/api/quant-help/python/python_other_api.html"),
    ("34_Python其他事件.md", "https://emt.18.cn/api/quant-help/python/python_other_event.html"),
    ("35_Python枚举常量.md", "https://emt.18.cn/api/quant-help/python/python_enum_constant.html"),
    ("36_Python错误码.md", "https://emt.18.cn/api/quant-help/python/python_err_code.html"),
    # 智能策略
    ("40_智能策略.md", "https://emt.18.cn/api/quant-help/smart/smart.html"),
    # 数据文档
    ("50_数据文档.md", "https://emt.18.cn/api/quant-help/data/data.html"),
    # 常见问题
    ("60_常见问题.md", "https://emt.18.cn/api/quant-help/faq/faq.html"),
]


class HTMLToMarkdown(HTMLParser):
    """简易 HTML -> Markdown 转换器"""

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
        elif tag == "pre":
            self.in_pre = True
            self.output.append("\n```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.output.append("`")
        elif tag == "strong" or tag == "b":
            self.output.append("**")
        elif tag == "em" or tag == "i":
            self.output.append("*")
        elif tag == "a":
            href = attrs_dict.get("href", "")
            self.output.append("[")
            self._href = href
        elif tag == "ul":
            self.list_depth += 1
            self.ordered_list = False
            self.output.append("\n")
        elif tag == "ol":
            self.list_depth += 1
            self.ordered_list = True
            self.list_counter = 0
            self.output.append("\n")
        elif tag == "li":
            indent = "  " * (self.list_depth - 1)
            if self.ordered_list:
                self.list_counter += 1
                self.output.append(f"{indent}{self.list_counter}. ")
            else:
                self.output.append(f"{indent}- ")
        elif tag == "table":
            self.in_table = True
            self.table_rows = []
        elif tag == "tr":
            self.table_row = []
        elif tag in ("td", "th"):
            self.in_td = True
            self.td_content = ""
        elif tag == "img":
            alt = attrs_dict.get("alt", "图片")
            src = attrs_dict.get("src", "")
            self.output.append(f"![{alt}]({src})")

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
        elif tag == "pre":
            self.in_pre = False
            self.output.append("\n```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = False
            self.output.append("`")
        elif tag == "strong" or tag == "b":
            self.output.append("**")
        elif tag == "em" or tag == "i":
            self.output.append("*")
        elif tag == "a":
            href = getattr(self, "_href", "")
            self.output.append(f"]({href})")
        elif tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            self.output.append("\n")
        elif tag == "li":
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
                text = re.sub(r"\n\s+", " ", text)
            self.output.append(text)

    def _render_table(self):
        if not self.table_rows:
            return
        # 计算列数
        max_cols = max(len(row) for row in self.table_rows)
        # 标准化行
        for row in self.table_rows:
            while len(row) < max_cols:
                row.append("")

        self.output.append("\n\n")
        # 表头
        header = self.table_rows[0]
        self.output.append("| " + " | ".join(header) + " |\n")
        self.output.append("| " + " | ".join(["---"] * max_cols) + " |\n")
        # 数据行
        for row in self.table_rows[1:]:
            self.output.append("| " + " | ".join(row) + " |\n")
        self.output.append("\n")

    def get_markdown(self):
        text = "".join(self.output)
        # 清理多余空行
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_markdown(html_content):
    """将 HTML 转换为 Markdown"""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    return parser.get_markdown()


def fetch_page(url):
    """获取页面内容"""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        print(f"  错误: {e}")
        return None


def crawl_all():
    """爬取所有文档页面"""
    os.makedirs(DOCS_DIR, exist_ok=True)

    for filename, url in DOC_PAGES:
        filepath = os.path.join(DOCS_DIR, filename)
        print(f"正在爬取: {filename}")
        print(f"  URL: {url}")

        html = fetch_page(url)
        if html is None:
            print(f"  跳过: 无法获取")
            continue

        # 尝试提取 body 或主要内容区域
        body_match = re.search(
            r"<body[^>]*>(.*)</body>", html, re.DOTALL | re.IGNORECASE
        )
        if body_match:
            html_content = body_match.group(1)
        else:
            html_content = html

        markdown = html_to_markdown(html_content)

        if len(markdown.strip()) < 50:
            print(f"  警告: 内容过少 ({len(markdown)} 字符)，可能是动态加载页面")
            # 保存原始 HTML 作为备份
            raw_path = filepath.replace(".md", "_raw.html")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(html)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"  已保存: {filepath} ({len(markdown)} 字符)")
        time.sleep(0.5)  # 避免请求过快

    print(f"\n完成! 文档已保存到: {DOCS_DIR}")


if __name__ == "__main__":
    crawl_all()
