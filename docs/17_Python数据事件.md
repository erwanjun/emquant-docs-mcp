## 数据事件

**数据事件是阻塞回调事件函数，通过subscribe函数订阅， 主动推送**

### on_tick - tick数据推送事件

接收tick分笔数据， 通过subscribe订阅tick行情，行情服务主动推送tick数据

**函数原型:**

```
on_tick(context, tick)

```

**参数：**

（参见 上下文对象）

（参见 tick对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context对象 | 上下文 |
| tick | tick对象 | 当前被推送的tick |

**示例：**

```
def on_tick(context, tick):
    print(tick)

```

**输出：**

```
{'symbol': 'SHSE.600519', 'created_at': datetime.datetime(2020, 9, 2, 14, 7, 23, 620000, tzinfo=tzfile('PRC')), 'price': 1798.8800048828125, 'open': 1825.0, 'high': 1828.0, 'low': 1770.0, 'cum_volume': 2651191, 'cum_amount': 4760586491.0, 'cum_position': 0, 'last_amount': 179888.0, 'last_volume': 100, 'trade_type': 0, 'receive_local_time': 1602751345.262745}

```

### on_bar - bar数据推送事件

接收固定周期bar数据， 通过subscribe订阅bar行情，行情服务主动推送bar数据

**函数原型:**

```
on_bar(context, bars)

```

**参数：**

（参见 上下文对象）

（参见 bar对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context对象 | 上下文对象 |
| bars | list(bar) | 当前被推送的bar列表 |

**示例：**

```
def on_bar(context, bars):
    for bar in bars:
        print(bar)

```

**输出：**

```
{'symbol': 'SHSE.600519', 'eob': datetime.datetime(2020, 9, 30, 15, 15, 1, tzinfo=tzfile('PRC')), 'bob': datetime.datetime(2020, 9, 30, 0, 0, tzinfo=tzfile('PRC')), 'open': 1660.0, 'close': 1668.5, 'high': 1691.9000244140625, 'low': 1660.0, 'volume': 2708781, 'amount': 4536012540.0, 'pre_close': 1652.2999267578125, 'position': 0, 'frequency': '1d', 'receive_local_time': 1602751647.923199}

```

**注意：**

**1.**若在subscribe函数中订阅了多个标的的bar，但[wait_group](python_subscribe.html#wait_group)参数值为False,则多次触发On_bar,每次返回只包含单个标的list长度为1的bars;若参数值为True,则只会触发一次On_bar,返回包含多个标的的bars。

**2.**bar在本周期结束时间后才会推送，标的在这个周期内无交易则不推送bar。

### on_l2transaction - 逐笔成交事件

接收逐笔成交数据（L2行情时有效）

**函数原型:**

```
on_l2transaction(context, transaction)

```

**参数：**

（参见 上下文对象）

（参见 level2 逐笔成交）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context对象 | 上下文对象 |
| transaction | L2Transaction对象 | 收到的逐笔成交行情 |

**示例：**

```
def on_l2transaction(context, transaction):
    print(transaction)

```

**输出：**

```
{'symbol': 'SZSE.300003', 'volume': 300, 'created_at': datetime.datetime(2020, 11, 24, 9, 38, 16, 50, tzinfo=tzfile('PRC')), 'exec_type': '4', 'side': '', 'price': 0.0}

```

### on_l2order - 逐笔委托事件

接收逐笔委托数据（L2行情时有效）

**函数原型:**

```
on_l2order(context, l2order)

```

**参数：**

（参见 context    上下文对象）

（参见 level2）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context对象 | 上下文对象 |
| l2order | L2Order对象 | 收到的逐笔委托行情 |

**示例：**

```
def on_l2order(context, l2order):
    print(l2order)

```

**输出：**

```
{'symbol': 'SZSE.300003', 'side': '1', 'price': 29.350000381469727, 'volume': 2400, 'created_at': datetime.datetime(2020, 11, 24, 9, 38, 16, 80, tzinfo=tzfile('PRC')), 'order_type': '2'}

```
     [ ** ](python_subscribe.html#unsubscribe---取消订阅) [ ** ](python_data_event.html#ontick---tick数据推送事件)
