## 交易事件

### on_order_status - 委托状态更新事件

响应委托状态更新事情，下单后及委托状态更新时被触发。

**注意：**

**1.** 交易账户重连后，会重新推送一遍交易账户登录成功后查询回来的所有委托的最终状态，防止断线期间有委托状态变化没有推送。

**2.** 撤单拒绝，会推送撤单委托的最终状态。

**3.** 回测模式下，交易事件顺序与实时模式一致，委托状态 待报 和 已报 是虚拟状态，不会更新持仓和资金。已成状态后才会更新持仓和资金。

**函数原型:**

```
on_order_status(context, order)

```

**参数：**

（参见 上下文对象）

（参见 委托对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context | 上下文 |
| order | order | 委托 |

**示例：1**

```
def on_order_status(context, order):
    print(order)

```

**输出：**

```
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 18181800, 'value': 200000000.0, 'percent': 0.1, 'target_volume': 18181800, 'target_value': 199999800.0, 'target_percent': 0.1, 'filled_volume': 18181800, 'filled_vwap': 11.0011, 'filled_amount': 200019799.98, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 20001.979998, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}

```

**示例：2**

```
def init(context):
    # 记录委托id
    context.cl_ord_id = {}
    order_list = get_orders()
    context.cl_ord_id = {i['cl_ord_id']: {'status': i['status'], 'filled_volume': i['filled_volume']} for i in order_list if order_list}

def on_bar(context, bars):
    # 记录下单后对应的委托id，方便在on_order_status里追踪，实时模式下下单后会立刻返回10待报状态，其他状态需要通过on_order_status事件监控
    order = order_volume(symbol=symbol, volume=volume, side=OrderSide_Sell, order_type=OrderType_Limit,
                             position_effect=PositionEffect_CloseToday,
                             price=price_1)
    context.cl_ord_id[order[0]['cl_ord_id']] = {}
    context.cl_ord_id[order[0]['cl_ord_id']]['status'] = order[0]['status']
    context.cl_ord_id[order[0]['cl_ord_id']]['filled_volume'] = order[0]['filled_volume']

def on_order_status(context, order):
    # 过滤非此策略下单的委托和重复状态的委托
    if order.strategy_id == context.strategy_id and order.cl_ord_id in context.cl_ord_id.keys():
        if order.status != context.cl_ord_id[order.cl_ord_id]['status']:
            context.cl_ord_id[order.cl_ord_id]['status'] = order['status']
            context.cl_ord_id[order.cl_ord_id]['filled_volume'] = order['filled_volume']
        else:
            # 部分成交状态时，根据已成交量判断order是不是最新的
            if order.status == 2 and order.filled_volume != context.cl_ord_id[order.cl_ord_id]['filled_volume']:
                context.cl_ord_id[order.cl_ord_id]['filled_volume'] = order['filled_volume']
            else:
                return

    # 可在后面执行其他处理逻辑
    print(order)

```

**输出：**

```
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 18181800, 'value': 200000000.0, 'percent': 0.1, 'target_volume': 18181800, 'target_value': 199999800.0, 'target_percent': 0.1, 'filled_volume': 18181800, 'filled_vwap': 11.0011, 'filled_amount': 200019799.98, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 20001.979998, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}

```

### on_execution_report - 委托执行回报事件

响应委托被执行事件，委托成交或者撤单拒绝后被触发。

**注意：**

**1.** 交易账户重连后，会重新推送一遍交易账户登录成功后查询回来的所有执行回报，防止在交易账户断线期间有执行回报没有推送。

**2.** 撤单拒绝后，会推送撤单拒绝执行回报，可以根据 exec_id 区分

**函数原型:**

```
on_execution_report(context, execrpt)

```

**参数：**

（参见 上下文对象）

（参见 回报对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context | 上下文 |
| execrpt | execrpt | 回报 |

**示例：**

```
def init(context):
    # 记录成交id
    context.exec_id = []
    exec_rpt_list = get_execution_reports()

    context.exec_id = [i['exec_id'] for i in exec_rpt_list if exec_rpt_list]

def on_execution_report(context, execrpt):
    # 过滤掉非此策略和成交类型不是15（成交）的回报
    if execrpt.exec_type == 15 and execrpt.exec_id not in context.exec_id and execrpt.strategy_id == context.strategy_id:
        context.exec_id.append(execrpt.exec_id)
        # 后面可以执行其他处理逻辑
        print(execrpt)

```

**输出：**

```
{'strategy_id': 'e41dec22-2d72-11eb-b043-00ff5a669ee2', 'cl_ord_id': '000000247', 'symbol': 'SHSE.600000', 'position_effect': 1, 'side': 1, 'exec_type': 15, 'price': 12.640000343322754, 'volume': 200, 'amount': 2528.000068664551, 'account_id': '', 'account_name': '', 'order_id': '', 'exec_id': '', 'order_business': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'commission': 0.0, 'cost': 0.0, 'created_at': None}

```

### on_account_status - 交易账户状态更新事件

响应交易账户状态更新事件，交易账户状态变化时被触发。
**函数原型:**

```
def on_account_status(context, account):
    print(account)

```

**参数：**

（参见 上下文对象）

（参见 交易账户状态）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context | 上下文 |
| account | object,  包含account_id(账户id), account_name(账户名),AccountStatus(账户状态) | 交易账户状态对象，仅响应 已连接，已登录，已断开 和 错误  事件。 |

**示例：**

```

def init(context):
    # 主动查交易账户状态
    if context.account().status.state != 3:
        my_news = '账户未登录，状态：{}， 错误信息：{}'.format(context.account().status.state,
                                                           context.account().status.error.info)
        print(my_news)

# 系统主动推送交易状态
def on_account_status(context, account):
    if account['status']['state'] == 5:
        print('账户已断开')

    elif account['status']['state'] == 3:
        print('账户已连接')

    else:
        print('{}账户状态未知， account:{}'.format(context.now, account))

```

**输出：**

```
账户已断开

```
     [ ** ](python_algo_trade.html#algoorderbatch---批量算法交易委托) [ ** ](python_trade_event.html#onorderstatus---委托状态更新事件)
