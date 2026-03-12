#!/usr/bin/env python3
"""测试所有改动是否正常工作"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import _docs_cache, list_topics, search_docs, search_api, get_document, get_enum_constants, get_error_codes

passed = 0
failed = 0

def check(name, condition):
    global passed, failed
    if condition:
        print(f"  ✓ {name}")
        passed += 1
    else:
        print(f"  ✗ {name}")
        failed += 1

# 1. 文档数量
print("=== 文档加载 ===")
check(f"文档总数 >= 60 (实际 {len(_docs_cache)})", len(_docs_cache) >= 60)
cs_docs = [f for f in _docs_cache if "CSharp" in f]
check(f"C# 文档 = 23 (实际 {len(cs_docs)})", len(cs_docs) == 23)

# 2. list_topics
print("\n=== list_topics ===")
topics = list_topics()
check("包含 C# SDK 分组", "C# SDK" in topics)
check("包含 Python SDK 分组", "Python SDK" in topics)
check("包含入门指南分组", "入门指南" in topics)

# 3. search_api
print("\n=== search_api ===")
result = search_api("OrderVolume")
check("搜索 OrderVolume 找到 C# 结果", "CSharp" in result or "orderVolume" in result)
result2 = search_api("order_volume")
check("搜索 order_volume 找到 Python 结果", "Python" in result2 or "order_volume" in result2)

# 4. get_enum_constants
print("\n=== get_enum_constants ===")
cs_enum = get_enum_constants("csharp")
check("C# 枚举返回内容", len(cs_enum) > 100)
py_enum = get_enum_constants("python")
check("Python 枚举返回内容", len(py_enum) > 100)
check("C# 和 Python 枚举不同", cs_enum != py_enum)

# 5. get_error_codes
print("\n=== get_error_codes ===")
cs_err = get_error_codes("csharp")
check("C# 错误码返回内容", len(cs_err) > 50)
py_err = get_error_codes("python")
check("Python 错误码返回内容", len(py_err) > 50)

# 6. get_document
print("\n=== get_document ===")
result = get_document("76_CSharp交易成员函数.md")
check("获取 C# 交易文档", "GetAccounts" in result or "orderVolume" in result)

# 7. 图片验证
print("\n=== 图片引用 ===")
images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "images")
img_count = len([f for f in os.listdir(images_dir) if f.endswith((".png", ".jpg"))])
check(f"本地图片 >= 76 (实际 {img_count})", img_count >= 76)

remaining = 0
for fname, content in _docs_cache.items():
    count = content.count("](uploads/")
    if count > 0:
        remaining += count
        print(f"    残留: {fname} ({count} 处)")
check(f"无残留 uploads/ 引用 (残留 {remaining})", remaining == 0)

# 8. 图片路径正确
img_refs = 0
for fname, content in _docs_cache.items():
    img_refs += content.count("](images/")
check(f"图片引用使用 images/ 路径 ({img_refs} 处)", img_refs > 0)

print(f"\n=== 结果: {passed} 通过, {failed} 失败 ===")
sys.exit(1 if failed else 0)
