#!/usr/bin/env python3
"""下载文档中引用的所有图片到本地，并修复 markdown 中的引用路径。"""

import os
import re
import time
import urllib.request
import urllib.error
import urllib.parse

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
IMAGES_DIR = os.path.join(DOCS_DIR, "images")
BASE_URL = "https://emt.18.cn/api/quant-help"

# 文件名前缀 -> section 的映射
def get_section(filename):
    prefix = filename[:2]
    if prefix in ("00", "01"):
        return "guide"
    elif prefix >= "10" and prefix <= "36":
        return "python"
    elif prefix == "40":
        return "smart"
    elif prefix >= "50" and prefix <= "55":
        return "data"
    elif prefix == "60":
        return "faq"
    return "guide"  # fallback


def download_image(url, local_path):
    """下载图片，返回 True/False"""
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 100:  # 太小说明不是真图片
                return False
            with open(local_path, "wb") as f:
                f.write(data)
            return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"  ✗ 下载失败: {e}")
        return False


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    # 1. 扫描所有 md 文件找图片引用
    img_pattern = re.compile(r'!\[([^\]]*)\]\((uploads/[^)]+)\)')
    file_images = {}  # {filename: [(alt, rel_path), ...]}

    for fname in sorted(os.listdir(DOCS_DIR)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(DOCS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        matches = img_pattern.findall(content)
        if matches:
            file_images[fname] = matches

    # 2. 收集所有唯一图片及其 section
    all_images = {}  # {uploads/xxx: section}
    for fname, imgs in file_images.items():
        section = get_section(fname)
        for alt, rel_path in imgs:
            if rel_path not in all_images:
                all_images[rel_path] = section

    print(f"共找到 {len(all_images)} 张唯一图片，分布在 {len(file_images)} 个文件中\n")

    # 3. 下载所有图片
    success = 0
    failed = 0
    for rel_path, section in sorted(all_images.items()):
        # uploads/201812/attach_xxx.png -> images/attach_xxx.png
        img_name = os.path.basename(rel_path)
        local_path = os.path.join(IMAGES_DIR, img_name)

        if os.path.exists(local_path):
            print(f"  ✓ 已存在: {img_name}")
            success += 1
            continue

        url = f"{BASE_URL}/{section}/{urllib.parse.quote(rel_path)}"
        print(f"  下载: {url}")
        if download_image(url, local_path):
            size = os.path.getsize(local_path)
            print(f"  ✓ 成功: {img_name} ({size:,} bytes)")
            success += 1
        else:
            failed += 1
        time.sleep(0.3)

    print(f"\n下载完成: {success} 成功, {failed} 失败")

    # 4. 修复 markdown 中的引用路径
    print("\n修复 markdown 图片引用...")
    for fname, imgs in file_images.items():
        fpath = os.path.join(DOCS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False
        for alt, rel_path in imgs:
            img_name = os.path.basename(rel_path)
            local_path = os.path.join(IMAGES_DIR, img_name)
            if os.path.exists(local_path):
                old = f"![{alt}]({rel_path})"
                new = f"![{alt}](images/{img_name})"
                if old in content:
                    content = content.replace(old, new)
                    changed = True

        if changed:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ 已修复: {fname}")

    print("\n图片引用修复完成！")


if __name__ == "__main__":
    main()
