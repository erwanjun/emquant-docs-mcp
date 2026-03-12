#!/usr/bin/env python3
"""下载缺失的文档页面"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl_docs import HTMLToMarkdown, DOCS_DIR
import urllib.request

MISSING = [
    ("50_数据文档_股票.md", "https://emt.18.cn/api/quant-help/data/stock.html"),
    ("60_常见问题.md", "https://emt.18.cn/api/quant-help/faq/583.html"),
]

for fname, url in MISSING:
    print(f"Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=30)
    html = resp.read().decode("utf-8", errors="replace")
    
    parser = HTMLToMarkdown()
    parser.feed(html)
    md = parser.get_markdown()
    
    path = os.path.join(DOCS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  Saved {fname} ({len(md)} chars)")

print("Done!")
