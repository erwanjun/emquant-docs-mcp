#!/usr/bin/env python3
"""清理 C# 文档：修复垃圾头部、下载图片、修复链接。"""

import os
import re
import time
import urllib.request
import urllib.error
import urllib.parse

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
IMAGES_DIR = os.path.join(DOCS_DIR, "images")
BASE_URL = "https://emt.18.cn/api/quant-help/csharp"


def download_image(url, local_path):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 100:
                return False
            with open(local_path, "wb") as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"  ✗ 下载失败: {e}")
        return False


def clean_csharp_docs():
    """清理所有 C# 文档"""
    fixes = {"headers": 0, "images_downloaded": 0, "images_replaced": 0, "empty_links": 0, "breadcrumbs": 0}
    img_pattern = re.compile(r'!\[([^\]]*)\]\((uploads/[^)]+)\)')

    for fname in sorted(os.listdir(DOCS_DIR)):
        if not fname.endswith(".md"):
            continue
        if not (fname.startswith("7") or fname.startswith("8") or fname.startswith("9")):
            continue
        if not "CSharp" in fname and not "CS" in fname:
            continue

        fpath = os.path.join(DOCS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        # 1. 修复垃圾头部: `#  ** [快速开始](.) ` → 移除
        content = re.sub(r'^#\s+\*\*\s*\[.*?\]\(\.\)\s*\n', '', content)
        # 也有 `#  ** [交易成员函数](.) ` 格式
        content = re.sub(r'#\s+\*\*\s*\[.*?\]\(\.\)\s*\n', '', content)
        if content != original:
            fixes["headers"] += 1

        # 2. 移除面包屑导航行
        lines = content.split("\n")
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            if re.match(r'^(快速开始|Python|C\+\+|C#|Matlab|智能策略|数据文档|常见问题)\s*$', stripped):
                fixes["breadcrumbs"] += 1
                continue
            if stripped == '量化终端帮助中心':
                fixes["breadcrumbs"] += 1
                continue
            # 空链接
            if re.match(r'^\[?\s*\]?\s*\(\s*#?\s*\)\s*$', stripped):
                fixes["empty_links"] += 1
                continue
            cleaned_lines.append(line)
        content = "\n".join(cleaned_lines)

        # 3. 修复 broken relative links like [xxx](cs-xxx.html#...)
        content = re.sub(r'\[([^\]]+)\]\(cs-[^)]+\.html[^)]*\)', r'**\1**', content)

        # 4. 下载并替换图片引用
        matches = img_pattern.findall(content)
        for alt, rel_path in matches:
            img_name = os.path.basename(rel_path)
            local_path = os.path.join(IMAGES_DIR, img_name)

            if not os.path.exists(local_path):
                url = f"{BASE_URL}/{urllib.parse.quote(rel_path)}"
                print(f"  下载C#图片: {url}")
                if download_image(url, local_path):
                    size = os.path.getsize(local_path)
                    print(f"  ✓ 成功: {img_name} ({size:,} bytes)")
                    fixes["images_downloaded"] += 1
                else:
                    print(f"  ✗ 失败: {img_name}")
                time.sleep(0.3)

            if os.path.exists(local_path):
                old = f"![{alt}]({rel_path})"
                new = f"![{alt}](images/{img_name})"
                if old in content:
                    content = content.replace(old, new)
                    fixes["images_replaced"] += 1

        # 5. 清理多余空行
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = content.strip() + "\n"

        if content != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ 已清理: {fname}")

    print(f"\n清理统计:")
    print(f"  垃圾头部: {fixes['headers']}")
    print(f"  面包屑: {fixes['breadcrumbs']}")
    print(f"  空链接: {fixes['empty_links']}")
    print(f"  图片下载: {fixes['images_downloaded']}")
    print(f"  图片引用修复: {fixes['images_replaced']}")


if __name__ == "__main__":
    clean_csharp_docs()
