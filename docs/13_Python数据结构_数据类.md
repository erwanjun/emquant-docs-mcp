# 数据结构

## 数据类

### Tick - Tick对象

快照行情数据

（参见 symbol）

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| open | float | 日线开盘价 |
| high | float | 日线最高价 |
| low | float | 日线最低价 |
| price | float | 最新价 |
| cum_volume | long | 成交总量/最新成交量,累计值（日线成交量） |
| cum_amount | float | 成交总金额/最新成交额,累计值 （日线成交金额） |
| cum_position | int | 合约持仓量(只适用于期货),累计值（股票此值为0） |
| trade_type | int | 交易类型（只适用于期货）  1: '双开', 2: '双平', 3: '多开', 4: '空开', 5: '空平', 6: '多平', 7: '多换', 8: '空换' |
| last_volume | int | 瞬时成交量 |
| last_amount | float | 瞬时成交额（郑商所last_amount为0） |
| created_at | datetime.datetime | 创建时间 |
| quotes | [] (list of dict) | 股票提供买卖5档数据, list[0]~list[4]分别对应买卖一档到五档, level2行情对应的是list[0]~list[9]买卖一档到十档注意：可能会有买档或卖档报价缺失，比如跌停时无买档报价（bid_p和bid_v为0），涨停时无卖档报价(ask_p和ask_v为0); 其中每档报价quote结构如下： |

#### 报价`quote` - (dict类型)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bid_p | float | 买价 |
| bid_v | int | 买量 |
| ask_p | float | 卖价 |
| ask_v | int | 卖量 |
| bid_q | dict | 委买队列 包含（total_orders （int）委托总个数, queue_volumes (list) 委托量队列），仅level2行情支持 |
| ask_q | dict | 委卖队列 包含（total_orders （int）委托总个数, queue_volumes (list) 委托量队列），仅level2行情支持 |

**注意**： 

1、tick是分笔成交数据，股票频率为3s, 指数5s, 包含集合竞价数据，股票早盘集合竞价数为09:15:00-09:25:00的tick数据

2、涨停时， 没有卖价和卖量， ask_p和ask_v用0填充，跌停时，没有买价和买量，bid_p和bid_v用0填充

3、queue_volumes 委托量队列，只能获取到最优第一档的前50个委托量（不活跃标的可能会不足50个）

### Bar - Bar对象

bar数据是指各种频率的行情数据

（参见 symbol）

（参见 行情数据）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| frequency | str | 频率, 支持多种频率, 具体见股票行情数据 |
| open | float | 开盘价 |
| close | float | 收盘价 |
| high | float | 最高价 |
| low | float | 最低价 |
| amount | float | 成交额 |
| volume | long | 成交量 |
| position | long | 持仓量（仅期货） |
| bob | datetime.datetime | bar开始时间 |
| eob | datetime.datetime | bar结束时间 |

**注意：**
不活跃标的，没有成交量是不会生成bar

### L2Order - Level2 逐笔委托

（参见 symbol）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| side | str | 委托方向，深市：’1’买， ‘2’卖， ‘F’借入， ‘G’出借， 沪市：’B’买，’S’卖 |
| price | float | 委托价 |
| volume | int | 委托量 |
| order_type | str | 委托类型，深市：’1’市价， ‘2’限价， ‘U’本方最优，沪市：’A’新增委托订单，’D’删除委托订单 |
| order_index | int | 委托编号 |
| created_at | datetime.datetime | 创建时间 |

### L2Transaction - Level2 逐笔成交

（参见 symbol）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| side | str | 委托方向，沪市：B – 外盘,主动买, S – 内盘,主动卖, N – 集合竞价，深市无此字段 |
| price | float | 成交价 |
| volume | int | 成交量 |
| exec_type | str | 成交类型，深市：’4’撤单，’F’成交， 沪市无此字段 |
| exec_index | int | 成交编号 |
| ask_order_index | int | 叫卖委托编号 |
| bid_order_index | int | 叫买委托编号 |
| created_at | datetime.datetime | 创建时间 |

     [ ** ](python_concept.html#contextxxxxx---自定义属性) [ ** ](python_object_data.html#数据类)
