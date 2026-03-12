#!/usr/bin/env python3
"""补爬 5 个数据子页面：基金、期货、指数、可转债、板块"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl_docs import HTMLToMarkdown, DOCS_DIR
import urllib.request

PAGES = [
    ("51_数据文档_基金.md", "https://emt.18.cn/api/quant-help/data/fund.html"),
    ("52_数据文档_期货.md", "https://emt.18.cn/api/quant-help/data/future.html"),
    ("53_数据文档_指数.md", "https://emt.18.cn/api/quant-help/data/indices.html"),
    ("54_数据文档_可转债.md", "https://emt.18.cn/api/quant-help/data/bond.html"),
    ("55_数据文档_板块.md", "https://emt.18.cn/api/quant-help/data/sector.html"),
]

for fname, url in PAGES:
    print(f"Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=30)
    html = resp.read().decode("utf-8", errors="replace")

    parser = HTMLToMarkdown()
    parser.feed(html)
    md = parser.get_markdown()

    # 清除开头杂质
    md = re.sub(r'^#\s+\*\*\s*\[.*?\]\(\.\)\s*\n+', '', md)
    md = md.lstrip('\n')

    path = os.path.join(DOCS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  ✓ {fname} ({len(md)} chars)")

print("\nDone!")
