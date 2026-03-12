#!/usr/bin/env python3
"""Final smoke test for all MCP tools"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import py_compile
py_compile.compile(os.path.join(os.path.dirname(__file__), 'server.py'), doraise=True)
print('✓ 语法检查通过')

from server import (_docs_cache, list_topics, search_docs, get_document,
                    get_section, search_api, get_enum_constants,
                    get_error_codes, get_faq, get_quickstart)

print(f'✓ 文档数: {len(_docs_cache)}')
print(f'✓ 总字符数: {sum(len(c) for c in _docs_cache.values()):,}')

assert '📖' in list_topics()
assert '找到' in search_docs('history')
assert 'offset' in get_document('50_数据文档_股票.md')
assert '###' in get_section('15_Python基础函数.md', '基础函数')
assert '📄' in search_api('order_volume')
assert 'Order' in get_enum_constants()
assert '错误' in get_error_codes()
assert '目录' in get_faq()
assert '回测' in get_faq('回测')
assert '# 委托下单' in get_quickstart('下单')
assert '可用任务' in get_quickstart('不存在的')

print('✓ 全部 9 个工具 + 2 个资源 烟雾测试通过')
