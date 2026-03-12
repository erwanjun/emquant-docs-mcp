#!/usr/bin/env python3
"""文档清洗 v2: 清理数据文档头部 / 空链接 / 星号噪声"""
import os, re

DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")

stats = {"header": 0, "empty_link": 0, "stars": 0, "blank_runs": 0}


def clean_file(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    original = text

    # A. 清理数据文档/FAQ 的垃圾头部（页面标题行 + 面包屑）
    # 格式: "股票 · 数据文档 · 东财掘金帮助文档\n#  ** [股票](.)\n"
    m = re.match(r"^.+·.+·.+东财掘金帮助文档\s*\n", text)
    if m:
        text = text[m.end():]
        stats["header"] += 1
    m = re.match(r"^#\s+\*\*\s*\[.*?\]\(\.\)\s*\n", text)
    if m:
        text = text[m.end():]
        stats["header"] += 1

    # B. 空链接 [](xxx.html#anchor---中文) → 提取中文部分作为参考
    def replace_empty_link(m: re.Match) -> str:
        stats["empty_link"] += 1
        url = m.group(1)
        # 从 anchor 提取可读文本: "orderside---委托方向" → "委托方向"
        anchor = url.split("#")[-1] if "#" in url else ""
        # 取最后一个 --- 分隔的中文部分
        parts = anchor.split("---")
        readable = parts[-1] if parts else ""
        readable = readable.replace("%20", " ").replace("-", " ").strip()
        if readable:
            return f"（参见 {readable}）"
        return ""

    text = re.sub(r"\[\]\(([^)]+\.html[^)]*)\)", replace_empty_link, text)

    # 清理行首遗留的 `` `` 包裹（原 HTML 中空 <code> + 空链接的组合）
    text = re.sub(r"^``\s*``\s*（参见", "（参见", text, flags=re.MULTILINE)
    text = re.sub(r"^``\s*``\s*$", "", text, flags=re.MULTILINE)

    # D. 清理独立的 **** 噪声行
    count_before = len(re.findall(r"^\*{4}$", text, re.MULTILINE))
    text = re.sub(r"^\*{4}\s*$\n?", "", text, flags=re.MULTILINE)
    stats["stars"] += count_before

    # 收缩连续 3+ 空行为 2 空行
    before_blank = len(text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    if len(text) < before_blank:
        stats["blank_runs"] += 1

    # 去头尾空白
    text = text.strip() + "\n"

    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  ✓ {os.path.basename(path)}")


def main():
    for fname in sorted(os.listdir(DOCS_DIR)):
        if fname.endswith(".md"):
            clean_file(os.path.join(DOCS_DIR, fname))
    print(f"\n清洗完成: 头部 {stats['header']}处, 空链接 {stats['empty_link']}个, "
          f"星号行 {stats['stars']}处, 空行压缩 {stats['blank_runs']}处")


if __name__ == "__main__":
    main()
