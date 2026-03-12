## 行情数据查询函数（免费）

### current - 查询当前行情快照

查询当前行情快照，返回tick数据。回测时，返回回测当前时间点的tick数据

**函数原型:**

```
current(symbols, fields='')

```

**参数：**

（参见 代码标识）

（参见 tick对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | str or list | 查询代码，如有多个代码, 中间用 , (英文逗号) 隔开, 也支持 ['symbol1', 'symbol2'] 这种列表格式 ，使用参考symbol |
| fields | str | 查询字段, 默认所有字段具体字段见:Tick |

**返回值:**
`list[dict]`

**示例：**

```
current_data = current(symbols='SZSE.000001')

```

**输出：**

```
[{'symbol': 'SZSE.000001', 'open': 16.200000762939453, 'high': 16.920000076293945, 'low': 16.149999618530273, 'price': 16.559999465942383, 'quotes': [{'bid_p': 16.549999237060547, 'bid_v': 209200, 'ask_p': 16.559999465942383, 'ask_v': 296455}, {'bid_p': 16.540000915527344, 'bid_v': 188900, 'ask_p': 16.56999969482422, 'ask_v': 374405}, {'bid_p': 16.530000686645508, 'bid_v': 44900, 'ask_p': 16.579999923706055, 'ask_v': 187220}, {'bid_p': 16.520000457763672, 'bid_v': 20800, 'ask_p': 16.59000015258789, 'ask_v': 102622}, {'bid_p': 16.510000228881836, 'bid_v': 37700, 'ask_p': 16.600000381469727, 'ask_v': 337002}], 'cum_volume': 160006232, 'cum_amount': 2654379585.66, 'last_amount': 14153832.0, 'last_volume': 854700, 'trade_type': 7, 'created_at': datetime.datetime(2020, 10, 15, 15, 0, 3, tzinfo=tzfile('PRC'))}]

```

**注意：**

**1.** 若输入包含无效标的代码，则返回的列表只包含有效标的代码对应的`dict`

**2.** 若输入代码正确，但查询字段中包括错误字段，返回的列表仍包含对应数量的`dict`，但每个`dict`中除有效字段外，其他字段的值均为`空字符串/0`

**3.** 回测只返回symbol、price和created_at字段，实时模式返回全部字段

**4.** 集合竞价阶段还没有成交时，tick 行情快照的有效字段只有盘口报价quotes。

**5.** 回测模式下，如果订阅行情再调用current，会返回订阅频度（tick，分钟bar，日线）回测当前时刻的最新价格，超出历史行情权限会报错中止回测；如果不订阅行情直接调用current，会返回回测当前时刻最近的日线收盘价。

### history - 查询历史行情

**函数原型:**

```
history(symbol, frequency, start_time, end_time, fields=None, skip_suspended=True, 
        fill_missing=None, adjust=ADJUST_NONE, adjust_end_time='', df=True)

```

**参数：**

``****``（参见 代码标识）

（参见 行情数据）

（参见 tick对象）（参见 bar对象）

``````

``````

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码,若要获取多个标的的历史数据，可以采用中间用 , (英文逗号) 隔开的方法，但不能是list类型的输入参数，使用时参考symbol |
| frequency | str | 频率,  支持 'tick', '1d', '60s'等, 默认 '1d', 详情见股票行情数据 |
| start_time | str or datetime.datetime | 开始时间 (%Y-%m-%d %H:%M:%S 格式), 也支持datetime.datetime格式, 其中日线包含start_time数据, 非日线不包含start_time数据 |
| end_time | str or datetime.datetime | 结束时间 (%Y-%m-%d %H:%M:%S 格式), 也支持datetime.datetime格式 |
| fields | str | 指定返回对象字段, 如有多个字段, 中间用, 隔开, 默认所有,具体字段见:Tick对象或者Bar对象 |
| skip_suspended | bool | 是否跳过停牌, 默认跳过 |
| fill_missing | str or None | 填充方式,  None - 不填充,  'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认None |
| adjust | int | ADJUST_NONE or 0: 不复权, ADJUST_PREV or 1: 前复权, ADJUST_POST or 2: 后复权   默认不复权 |
| adjust_end_time | str | 复权基点时间, 默认当前时间 |
| df | bool | 是否返回 dataframe格式,默认 False, 返回list[dict] |

**返回值:参考[Tick对象](python_object_data.html#tick---tick对象)或者[Bar对象](python_object_data.html#bar---bar对象)。**

当df = True时， 返回

| 类型 | 说明 |
| --- | --- |
| dataframe | tick的dataframe 或者 bar的dataframe |

**示例：**

```
history_data = history(symbol='SHSE.000300', frequency='1d', start_time='2010-07-28',  end_time='2017-07-30', fields='open, close, low, high, eob', adjust=ADJUST_PREV, df= True)

```

**输出：**

```
          open      close        low       high                       eob
0     2796.4829  2863.7241  2784.1550  2866.4041 2010-07-28 00:00:00+08:00
1     2866.7720  2877.9761  2851.9961  2888.5991 2010-07-29 00:00:00+08:00
2     2871.4810  2868.8459  2844.6819  2876.1360 2010-07-30 00:00:00+08:00
3     2868.2791  2917.2749  2867.4500  2922.6121 2010-08-02 00:00:00+08:00
4     2925.2539  2865.9709  2865.7610  2929.6140 2010-08-03 00:00:00+08:00

```

当df = False时， 返回

| 类型 | 说明 |
| --- | --- |
| list | tick 列表  或者 bar 列表 |

**注意：**

```
history_data = history(symbol='SHSE.000300', frequency='1d', start_time='2017-07-30',  end_time='2017-07-31', fields='open, close, low, high, eob', adjust=ADJUST_PREV, df=False)

```

**输出：**

```
[{'open': 3722.42822265625, 'close': 3737.873291015625, 'low': 3713.655029296875, 'high': 3746.520751953125, 'eob': datetime.datetime(2017, 7, 31, 0, 0, tzinfo=tzfile('PRC'))}]

```

**1.**返回的`list/DataFrame`是以参数`eob/bob`的升序来排序的，若要获取多标的的数据，通常需进一步的数据处理来分别提取出每只标的的历史数据

**2.**start_time和end_time中月,日,时,分,秒均可以只输入个位数,例:`'2010-7-8 9:40:0'`或`'2017-7-30 12:3:0'`,但若对应位置为零，则`0`不可被省略,如不可输入`'2017-7-30 12:3: '` 获取数据目前采用前后闭区间的方式，即会获取前后两个时间节点的数据，使用时务必注意这点

**3.**若输入无效标的代码，返回`空列表/空DataFrame`

**4.**若输入代码正确，但查询字段包含无效字段，返回的列表、DataFrame只包含
`eob、symbol`和输入的其他有效字段

**5.** skip_suspended 和 fill_missing 参数暂不支持

**6.** 单次返回数据量最大返回33000, 超出部分不返回

**7.** start_time和end_time输入不存在日期时，会报错details = "failed to parse datetime"

### history_n - 查询历史行情最新n条

**函数原型:**

```
history_n(symbol, frequency, count, end_time=None, fields=None, skip_suspended=True, 
          fill_missing=None, adjust=ADJUST_NONE, adjust_end_time='', df=False)

```

**参数：**

（参见 代码标识）

（参见 行情数据）

``
（参见 tick对象）（参见 bar对象）

````````

``````

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码(只允许单个标的的代码字符串)，使用时参考symbol |
| frequency | str | 频率,  支持 'tick', '1d', '60s'等, 默认 '1d', 详情见股票行情数据 |
| count | int | 数量(正整数) |
| end_time | str or datetime.datetime | 结束时间 (%Y-%m-%d %H:%M:%S 格式), 也支持datetime.datetime格式 |
| fields | str | 指定返回对象字段, 如有多个字段, 中间用, 隔开, 默认所有,具体字段见:Tick对象或者Bar对象 |
| skip_suspended | bool | 是否跳过停牌, 默认跳过 |
| fill_missing | str or None | 填充方式, None - 不填充, 'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认 None |
| adjust | int | ADJUST_NONE or 0: 不复权, ADJUST_PREV or 1: 前复权, ADJUST_POST or 2: 后复权   默认不复权 |
| adjust_end_time | str | 复权基点时间, 默认当前时间 |
| df | bool | 是否返回dataframe 格式, 默认False, 返回list[dict] |

**返回值:参考[Tick对象](python_object_data.html#tick---tick对象)或者[Bar对象](python_object_data.html#bar---bar对象)。**

当df = True时，返回

| 类型 | 说明 |
| --- | --- |
| dataframe | tick的dataframe 或者 bar的dataframe |

**示例：**

```
history_n_data = history_n(symbol='SHSE.600519', frequency='1d', count=100, end_time='2020-10-20 15:30:00', fields='symbol, open, close, low, high, eob', adjust=ADJUST_PREV, df=True)

```

**输出：**

```
 symbol       open  ...       high                       eob
0   SHSE.600519  1350.2278  ...  1350.3265 2020-05-22 00:00:00+08:00
1   SHSE.600519  1314.6434  ...  1350.8010 2020-05-25 00:00:00+08:00
2   SHSE.600519  1354.0629  ...  1354.1321 2020-05-26 00:00:00+08:00
3   SHSE.600519  1343.3086  ...  1344.2970 2020-05-27 00:00:00+08:00
4   SHSE.600519  1322.5214  ...  1331.3878 2020-05-28 00:00:00+08:00

```

当df = False时， 返回

| 类型 | 说明 |
| --- | --- |
| list | tick 列表 或者 bar 列表 |

**示例：**

```
history_n_data = history_n(symbol='SHSE.600519', frequency='1d', count=2, end_time='2020-10-20 15:30:00', fields='symbol, open, close, low, high, eob', adjust=ADJUST_PREV, df=False)

```

**输出：**

```
[{'symbol': 'SHSE.600519', 'open': 1725.0, 'close': 1699.0, 'low': 1691.9000244140625, 'high': 1733.97998046875, 'eob': datetime.datetime(2020, 10, 19, 0, 0, tzinfo=tzfile('PRC'))}, {'symbol': 'SHSE.600519', 'open': 1699.989990234375, 'close': 1734.0, 'low': 1695.0, 'high': 1734.969970703125, 'eob': datetime.datetime(2020, 10, 20, 0, 0, tzinfo=tzfile('PRC'))}]

```

**注意：**

**1.**返回的`list/DataFrame`是以参数`eob/bob`的升序来排序的

**2.**若输入无效标的代码，返回`空列表/空DataFrame`

**3.**若输入代码正确，但查询字段包含无效字段，返回的列表、DataFrame只包含
`eob、symbol`和输入的其他有效字段

**4.**end_time中月,日,时,分,秒均可以只输入个位数,例:`'2017-7-30 20:0:20'`,但若对应位置为零，则`0`不可被省略,如不可输入`'2017-7-30 20: :20'`

**5.** skip_suspended 和 fill_missing 参数暂不支持

**6.** 单次返回数据量最大返回33000, 超出部分不返回

**7.** start_time和end_time输入不存在日期时，会报错details = "Can't parse string as time: 2020-10-40 15:30:00"

### context.data - 数据滑窗

**函数原型:**

```
context.data(symbol, frequency, count)

```

**参数：**

（参见 代码标识）

（参见 行情数据）

``
（参见 tick对象）（参见 bar对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码(只允许单个标的的代码字符串)，使用时参考symbol |
| frequency | str | 频率, 支持 'tick', '1d', '15s', '30s' 等,需和subscribe函数中指定的频率保持一致。详情见股票行情数据 |
| count | int | 滑窗大小(正整数)，需小于等于subscribe函数中count值 |
| fields | str | 指定返回对象字段, 如有多个字段, 中间用, 隔开, 默认所有,具体字段见:Tick对象或者Bar对象 |

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

     [ ** ](python_data_event.html#onl2order---逐笔委托事件) [ ** ](python_select_api_history.html#current---查询当前行情快照)
