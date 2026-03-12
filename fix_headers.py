#!/usr/bin/env python3
"""清除所有文档开头的 HTML 导航残留杂质行"""
import os, re

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

fixed = 0
for fname in sorted(os.listdir(DOCS_DIR)):
    if not fname.endswith(".md"):
        continue
    path = os.path.join(DOCS_DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 模式1: "#  ** [xxx](.) " — 导航面包屑残留
    content = re.sub(r'^#\s+\*\*\s*\[.*?\]\(\.\)\s*\n+', '', content)
    # 模式2: 开头的空白行
    content = content.lstrip('\n')

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        first_line = content.split('\n')[0][:60]
        print(f"  ✓ {fname}: {first_line}")
        fixed += 1

print(f"\n修复了 {fixed} 个文件")
