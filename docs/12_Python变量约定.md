# 变量约定

## symbol - 代码标识

东方财富量化代码(**symbol**)是东方财富量化平台用于唯一标识交易标的代码,

格式为：**交易所代码.交易标代码**, 比如深圳平安的**symbol**，示例：`SZSE.000001`（注意区分大小写）。代码表示可以在东财掘金量化终端的仿真交易或交易工具中进行查询。

![](images/attach_163e07077adc2677.png)

#### 交易所代码

目前东方财富量化支持国内的2个交易所, 各交易所的代码缩写如下：

| 市场中文名 | 市场代码 |
| --- | --- |
| 上交所 | SHSE |
| 深交所 | SZSE |

#### 交易标的代码

交易表代码是指交易所给出的交易标的代码, 包括股票（如600000）, 期权(如10002498）, 指数（如000001）, 基金（如510300）等代码。

具体的代码请参考交易所的给出的证券代码定义。

#### symbol示例

| 市场中文名 | 市场代码 | 示例代码 | 证券简称 |
| --- | --- | --- | --- |
| 上交所 | SHSE | SHSE.600000 | 浦发银行 |
| 深交所 | SZSE | SZSE.000001 | 平安银行 |

## mode - 模式选择

策略支持两种运行模式,需要在`run()`里面指定，分别为实时模式和回测模式。

### 实时模式

实时模式需指定 **mode = MODE_LIVE**

订阅行情服务器推送的实时行情，也就是交易所的实时行情，只在交易时段提供，常用于仿真和实盘。

### 回测模式

回测模式需指定 **mode = MODE_BACKTEST**

订阅指定时段、指定交易代码、指定数据类型的历史行情，行情服务器将按指定条件全速回放对应的行情数据。适用的场景是策略回测阶段，快速验证策略的绩效是否符合预期。

## context - 上下文对象

context是策略运行上下文环境对象，该对象将会在你的算法策略的任何方法之间做传递。用户可以通过context定义多种自己需要的属性，也可以查看context固有属性，context结构如下图：

![](images/attach_163e0724ee0db372.png)

### context.symbols - 订阅代码集合

通过subscribe行情订阅函数， 订阅代码会生成一个代码集合

**函数原型：**

```
context.symbols

```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| set(str) | 订阅代码集合 |

**示例：**

```
subscribe(symbols=['SHSE.600519', 'SHSE.600419'], frequency='60s')
context.symbols

```

**返回：**

```
{'SHSE.600519', 'SHSE.600419'}

```

### context.now - 当前时间

实时模式返回当前本地时间, 回测模式返回当前回测时间

**函数原型：**

```
context.now

```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| datetime.datetime | 当前时间(回测模式下是策略回测的当前历史时间， 实时模式下是用户的系统本地时间) |

**示例：**

```
context.now

```

**返回：**

```
2020-09-01 09:40:00+08:00

```

### context.data - 数据滑窗

获取订阅的[bar](python_object_data.html#bar---bar对象)或[tick](python_object_data.html#tick---tick对象)滑窗，数据为包含当前时刻推送bar或tick的前count条`bar`或者`tick`数据

**原型：**

```
context.data(symbol,frequency,count,fields)

```

**参数：**

（参见 数据订阅）

``（参见 bar对象）（参见 tick对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码(只允许单个标的的代码字符串) |
| frequency | str | 频率，所填频率应包含在subscribe订阅过频率中。 |
| count | int | 滑窗大小，正整数，此处count值应小于等于subscribe中指定的count值 |
| fields | str | 所需bar或tick的字段,如有多属性, 中间用,隔开,具体字段见:bar,tick |

**返回值：**

**当subscribe的format="df"（默认）时，返回dataframe**

| 类型 | 说明 |
| --- | --- |
| dataframe | tick 的 dataframe 或者 bar 的 dataframe |

**示例：**

```
def init(context):
    subscribe(symbols='SHSE.600519', frequency='60s', count=50, fields='symbol, close, eob', format='df')

def on_bar(context,bars):
    data = context.data(symbol=bars[0]['symbol'], frequency='60s', count=10)
    print(data.tail())

```

**输出：**

```
                symbol    close                       eob
5  SHSE.600519  1629.96 2024-01-22 14:56:00+08:00
6  SHSE.600519  1627.25 2024-01-22 14:57:00+08:00
7  SHSE.600519  1627.98 2024-01-22 14:58:00+08:00
8  SHSE.600519  1642.00 2024-01-22 15:00:00+08:00
9  SHSE.600519  1632.96 2024-01-23 09:31:00+08:00

```

**subscribe的format ="row"时，返回list[dict]**

| 类型 | 说明 |
| --- | --- |
| list[dict] | 当frequency='tick'时，返回tick列表：[{tick_1}, {tick_2},  ..., {tick_n}]，列表长度等于滑窗大小，即n=count， 当frequency='60s', '300s', '900s', '1800s', '3600s'时，返回bar列表：[{bar_1}, {bar_2}, {bar_n}, ..., ] ，列表长度等于滑窗大小，即n=count |

**示例：**

```
def init(context):
    subscribe(symbols='SHSE.600519', frequency='tick', count=50, fields='symbol, price, quotes,created_at', format='row')

def on_tick(context, tick):
    data = context.data(symbol=tick['symbol'], frequency='tick', count=3)
    print(data)

```

**输出：**

```
[{'symbol': 'SHSE.600519', 'price': 1642.0, 'quotes': [{'bid_p': 1640.0, 'bid_v': 100, 'ask_p': 1642.0, 'ask_v': 4168}, {'bid_p': 1634.52, 'bid_v': 300, 'ask_p': 1642.01, 'ask_v': 100}, {'bid_p': 1633.0, 'bid_v': 100, 'ask_p': 1642.06, 'ask_v': 100}, {'bid_p': 1632.96, 'bid_v': 100, 'ask_p': 1642.08, 'ask_v': 200}, {'bid_p': 1632.89, 'bid_v': 100, 'ask_p': 1642.2, 'ask_v': 200}], 'created_at': datetime.datetime(2024, 1, 22, 15, 1, 51, 286000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai'))}, {'symbol': 'SHSE.600519', 'price': 1642.0, 'quotes': [{'bid_p': 1640.0, 'bid_v': 100, 'ask_p': 1642.0, 'ask_v': 4168}, {'bid_p': 1634.52, 'bid_v': 300, 'ask_p': 1642.01, 'ask_v': 100}, {'bid_p': 1633.0, 'bid_v': 100, 'ask_p': 1642.06, 'ask_v': 100}, {'bid_p': 1632.96, 'bid_v': 100, 'ask_p': 1642.08, 'ask_v': 200}, {'bid_p': 1632.89, 'bid_v': 100, 'ask_p': 1642.2, 'ask_v': 200}], 'created_at': datetime.datetime(2024, 1, 22, 15, 1, 54, 280000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai'))}, {'symbol': 'SHSE.600519', 'price': 0.0, 'quotes': [{'bid_p': 0.0, 'bid_v': 0, 'ask_p': 0.0, 'ask_v': 0}, {'bid_p': 0.0, 'bid_v': 0, 'ask_p': 0.0, 'ask_v': 0}, {'bid_p': 0.0, 'bid_v': 0, 'ask_p': 0.0, 'ask_v': 0}, {'bid_p': 0.0, 'bid_v': 0, 'ask_p': 0.0, 'ask_v': 0}, {'bid_p': 0.0, 'bid_v': 0, 'ask_p': 0.0, 'ask_v': 0}], 'created_at': datetime.datetime(2024, 1, 23, 9, 14, 1, 91000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai'))}]

```

**subscribe的format ="col"时，返回dict**

| 类型 | 说明 |
| --- | --- |
| dict | 当frequency='tick'时，返回tick数据（symbol为str格式，其余字段为列表，列表长度等于滑窗大小count），当frequency='60s', '300s', '900s', '1800s', '3600s'时，返回bar数据（symbol和frequency为str格式，其余字段为列表，列表长度等于滑窗大小count） |

**示例：**

```
def init(context):
    subscribe(symbols='SHSE.600519', frequency='tick', count=10, fields='symbol, price, bid_p, created_at', format='col')

def on_tick(context, tick):
    data = context.data(symbol=tick['symbol'], frequency='tick', count=10)
    print(data)

```

**输出：**

```
{'symbol': 'SHSE.600519', 'price': [1642.0, 1642.0, 1642.0, 1642.0, 1642.0, 1642.0, 1642.0, 1642.0, 1642.0, 0.0], 'bid_p': [1640.0, 1640.0, 1640.0, 1640.0, 1640.0, 1640.0, 1640.0, 1640.0, 1640.0, 0.0], 'created_at': [datetime.datetime(2024, 1, 22, 15, 1, 12, 280000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 21, 277000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 24, 278000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 33, 280000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 36, 282000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 39, 279000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 48, 283000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 51, 286000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 22, 15, 1, 54, 280000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai')), datetime.datetime(2024, 1, 23, 9, 14, 1, 91000, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'Asia/Shanghai'))]}

```

**注意：**

**1.** 只有在**订阅**后，此接口才能取到数据，如未订阅数据，则返回报错。

**2.** symbol 参数只支持输入**一个**标的。

**3.** count 参数必须**小于或等于**订阅函数里面的 count 值。

**4.** fields 参数必须在订阅函数subscribe里面指定的 fields 范围内。指定字段越少，查询速度越快，目前效率是row > col > df。

**5.** 当subscribe的format指定col时，tick的quotes字段会被拆分，只返回买卖一档的量和价，即只有bid_p，bid_v, ask_p和ask_v。

### context.account - 账户信息

可通过此函数获取账户资金信息及持仓信息。

**原型：**

```
context.account(account_id=None)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账户信息，默认返回默认账户, 如多个账户需指定account_id |

**返回值：**

返回类型为[account - 账户对象](python_object_trade.html#account---账户对象)。

*示例-获取当前持仓：*

```
# 所有持仓
Account_positions = context.account().positions()
# 指定持仓
Account_position = context.account().position(symbol='SHSE.600519',side = PositionSide_Long)

```

**返回值：**

（参见 持仓对象）

| 类型 | 说明 |
| --- | --- |
| list[position] | 持仓对象列表 |

** 注意： **
没有持仓的情况下， 用context.account().positions()查总持仓， 返回空列表， 用context.account().position()查单个持仓，返回None

**输出**

```
# 所有持仓输出
[{'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'symbol': 'SHSE.600419', 'side': 1, 'volume': 2200, 'volume_today': 100, 'vwap': 16.43391600830338, 'amount': 36154.61521826744, 'fpnl': -2362.6138754940007, 'cost': 36154.61521826744, 'available': 2200, 'available_today': 100, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 30, 9, 40, tzinfo=tzfile('PRC')), 'account_name': '', 'vwap_diluted': 0.0, 'price': 0.0, 'order_frozen': 0, 'order_frozen_today': 0, 'available_now': 0, 'market_value': 0.0, 'last_price': 0.0, 'last_volume': 0, 'last_inout': 0, 'change_reason': 0, 'change_event_id': '', 'has_dividend': 0}, {'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'symbol': 'SHSE.600519', 'side': 1, 'volume': 1100, 'vwap': 1752.575242219682, 'amount': 1927832.7664416502, 'fpnl': -110302.84700805641, 'cost': 1927832.7664416502, 'available': 1100, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 15, 9, 40, tzinfo=tzfile('PRC')), 'account_name': '', 'volume_today': 0, 'vwap_diluted': 0.0, 'price': 0.0, 'order_frozen': 0, 'order_frozen_today': 0, 'available_today': 0, 'available_now': 0, 'market_value': 0.0, 'last_price': 0.0, 'last_volume': 0, 'last_inout': 0, 'change_reason': 0, 'change_event_id': '', 'has_dividend': 0}]
# 指定持仓输出
{'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'symbol': 'SHSE.600519', 'side': 1, 'volume': 1100, 'vwap': 1752.575242219682, 'amount': 1927832.7664416502, 'fpnl': -110302.84700805641, 'cost': 1927832.7664416502, 'available': 1100, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 15, 9, 40, tzinfo=tzfile('PRC')), 'account_name': '', 'volume_today': 0, 'vwap_diluted': 0.0, 'price': 0.0, 'order_frozen': 0, 'order_frozen_today': 0, 'available_today': 0, 'available_now': 0, 'market_value': 0.0, 'last_price': 0.0, 'last_volume': 0, 'last_inout': 0, 'change_reason': 0, 'change_event_id': '', 'has_dividend': 0}

```

*示例-获取当前账户资金：*

```
context.account().cash

```

**返回值：**

（参见 资金对象）

| 类型 | 说明 |
| --- | --- |
| dict[cash] | 资金对象字典 |

**输出**

```
{'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'nav': 1905248.2789094353, 'pnl': -94751.72109056474, 'fpnl': -94555.35135529494, 'frozen': 1963697.3526980684, 'available': 36106.277566661825, 'cum_inout': 2000000.0, 'cum_trade': 1963697.3526980684, 'cum_commission': 196.3697352698069, 'last_trade': 1536.1536610412597, 'last_commission': 0.153615366104126, 'created_at': datetime.datetime(2020, 9, 1, 8, 0, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 30, 9, 40, tzinfo=tzfile('PRC')), 'account_name': '', 'currency': 0, 'order_frozen': 0.0, 'balance': 0.0, 'market_value': 0.0, 'cum_pnl': 0.0, 'last_pnl': 0.0, 'last_inout': 0.0, 'change_reason': 0, 'change_event_id': ''}

```

*示例-获取账户连接状态：*

```
context.account().status

```

**输出**

```
state: 3

```

### context.parameters - 动态参数

获取所有动态参数

**函数原型：**

```
context.parameters

```

**返回值：**

（参见 动态参数设置）

| 类型 | 说明 |
| --- | --- |
| dict | key为动态参数的key, 值为动态参数对象， 参见动态参数设置 |

*示例-添加动态参数和查询所有设置的动态参数*

```
add_parameter(key='k_value', value=context.k_value, min=0, max=100, name='k值阀值', intro='k值阀值',group='1', readonly=False)

context.parameters

```

**输出**

```
{'k_value': {'key': 'k_value', 'value': 80.0, 'max': 100.0, 'name': 'k值阀值', 'intro': 'k值阀值', 'group': '1', 'min': 0.0, 'readonly': False}}

```

### context.xxxxx - 自定义属性

通过自定义属性设置参数， 随context全局变量传入策略各个事件里

```
context.my_value = 100000000

```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any type | 自定义属性 |

*示例-输出自定义属性*

```
print(context.my_value)

```

**输出**

```
100000000

```
     [ ** ](python_frame.html#策略入口) [ ** ](python_concept.html#symbol---代码标识)
