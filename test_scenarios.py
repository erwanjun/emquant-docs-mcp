#!/usr/bin/env python3
"""End-to-end scenario test"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from server import *

def test(name, result, checks):
    ok = all(c(result) for c in checks)
    status = "✅" if ok else "❌"
    print(f"{status} {name}: {len(result)} chars")
    if not ok:
        for c in checks:
            if not c(result):
                print(f"   FAIL: {c.__doc__}")
    return ok

results = []

# 场景1: 新手入门
r = get_quickstart("回测")
results.append(test("场景1: 快速指引-回测", r, [
    lambda r: "subscribe" in r,  # doc: 有subscribe
    lambda r: "on_bar" in r,  # doc: 有on_bar
    lambda r: "MODE_BACKTEST" in r,  # doc: 有回测模式
]))

# 场景2: 查函数用法
r = search_api("order_volume")
results.append(test("场景2: search_api order_volume", r, [
    lambda r: "order_volume" in r.lower(),  # doc: 含函数名
    lambda r: "symbol" in r,  # doc: 含参数
    lambda r: "Python交易函数" in r,  # doc: 来自正确文件
]))

# 场景3: 查行情函数
r = search_api("history")
results.append(test("场景3: search_api history", r, [
    lambda r: "history" in r.lower(),  # doc: 含函数名
    lambda r: "frequency" in r or "symbol" in r,  # doc: 含参数
]))

# 场景4: 财务函数
r = search_api("get_fundamentals")
results.append(test("场景4: search_api get_fundamentals", r, [
    lambda r: "fundamentals" in r.lower(),  # doc: 含函数名
    lambda r: "table" in r.lower() or "symbols" in r,  # doc: 含参数
]))

# 场景5: 枚举常量
r = get_enum_constants()
results.append(test("场景5: 枚举常量", r, [
    lambda r: "OrderType" in r or "ordertype" in r.lower(),  # doc: 含OrderType
    lambda r: "OrderSide" in r or "orderside" in r.lower(),  # doc: 含OrderSide
    lambda r: len(r) < 20000,  # doc: 不超长
]))

# 场景6: 大文件分页
r = get_document("50_数据文档_股票.md")
results.append(test("场景6: 大文件分页", r, [
    lambda r: "目录" in r or "offset" in r,  # doc: 触发分页
    lambda r: len(r) < 25000,  # doc: 在限制内
]))

# 场景7: 关键词搜索
r = search_docs("市盈率")
results.append(test("场景7: search_docs 市盈率", r, [
    lambda r: "市盈率" in r,  # doc: 含关键词
    lambda r: "找到" in r,  # doc: 有结果计数
]))

# 场景8: FAQ流程
r1 = get_faq()
r2 = get_faq("token")
results.append(test("场景8a: FAQ目录", r1, [
    lambda r: "目录" in r,  # doc: 是目录
    lambda r: len(r) < 5000,  # doc: 不是全文
]))
results.append(test("场景8b: FAQ筛选", r2, [
    lambda r: "token" in r.lower(),  # doc: 含关键词
]))

# 场景9: list_topics分组
r = list_topics()
results.append(test("场景9: list_topics分组", r, [
    lambda r: "📖" in r,  # doc: 有入门分组
    lambda r: "🐍" in r,  # doc: 有Python分组
    lambda r: "📊" in r,  # doc: 有数据分组
]))

# 场景10: get_section含子标题
r = get_section("15_Python基础函数.md", "基础函数")
results.append(test("场景10: get_section子标题", r, [
    lambda r: "init" in r,  # doc: 含子函数
    lambda r: "run" in r,  # doc: 含子函数
    lambda r: "###" in r,  # doc: 含子标题
]))

passed = sum(results)
total = len(results)
print(f"\n{'='*40}")
print(f"结果: {passed}/{total} 场景通过")
if passed == total:
    print("🎉 所有场景测试通过！MCP 服务状态良好。")
