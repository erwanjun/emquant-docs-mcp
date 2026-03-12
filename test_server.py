#!/usr/bin/env python3
"""测试 MCP 服务器的各种边界情况"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from server import _docs_cache, search_docs, search_api, get_document, get_section, get_faq

# 1. 大文件问题
big = _docs_cache.get('21_Python股票增值数据.md', '')
print(f"[1] 最大文档长度: {len(big)} chars ≈ {len(big)//4} tokens")

# 2. search_docs 基本搜索
r = search_docs('subscribe')
print(f"\n[2] search_docs('subscribe') => {len(r)} chars, 结果数: {r.count('---') + 1}")

# 3. search_api 搜索 history (常见但出现在很多地方)
r = search_api('history')
print(f"\n[3] search_api('history') => {len(r)} chars, 匹配数: {r.count('---') + 1}")

# 4. search_api 搜索 order_volume (精确函数)
r = search_api('order_volume')
print(f"\n[4] search_api('order_volume') => {len(r)} chars")
print(r[:300])

# 5. get_section 测试
r = get_section('26_Python交易函数.md', 'order_volume')
print(f"\n[5] get_section(交易函数, order_volume) => {len(r)} chars")
print(r[:200])

# 6. 搜索中文关键词
r = search_docs('融资融券')
print(f"\n[6] search_docs('融资融券') => {len(r)} chars")

# 7. 文档开头质量检查
print("\n[7] 文档开头内容:")
for fname, content in list(_docs_cache.items())[:5]:
    first_lines = content.strip().split('\n')[:2]
    print(f"  {fname}: {first_lines}")

# 8. 缺失文件检查
needed = ['40_智能策略.md', '50_数据文档.md']
print("\n[8] 缺失文件:")
for f in needed:
    print(f"  {f}: {'存在' if f in _docs_cache else '不存在'}")

# 9. get_document 模糊匹配测试
r = get_document('交易函数')
print(f"\n[9] get_document('交易函数') => {'匹配成功' if '未找到' not in r else '未找到'}, {len(r)} chars")

# 10. get_faq 主题筛选
r = get_faq('安装')
print(f"\n[10] get_faq('安装') => {len(r)} chars, 包含'安装': {'安装' in r}")

# 11. 数据文档子页面检查
print("\n[11] 数据文档覆盖:")
data_topics = ['基金', '期货', '指数', '可转债', '板块']
for t in data_topics:
    found = any(t in fname for fname in _docs_cache)
    in_content = any(t in content for content in _docs_cache.values())
    print(f"  {t}: 独立文件={'有' if found else '无'}, 内容中={'有' if in_content else '无'}")
