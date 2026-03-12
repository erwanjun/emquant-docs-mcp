# API介绍

## 基础函数

### init - 初始化策略

初始化策略, 策略启动时自动执行。可以在这里初始化策略配置参数。

**函数原型:**

```
init(context)

```

**参数：**

（参见 上下文对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context | 上下文，全局变量可存储在这里 |

**示例：**

```
def init(context):
    # 订阅bar
    subscribe(symbols='SHSE.600000,SHSE.600004', frequency='30s', count=5, wait_group=True, wait_group_timeout='5s')
    # 增加对象属性，如:设置一个股票资金占用百分比
    context.percentage_stock = 0.8

```

**注意：**
`回测模式下init函数里不支持交易操作，仿真模式和实盘模式支持`

### schedule - 定时任务配置

在指定时间自动执行策略算法, 通常用于选股类型策略

**函数原型:**

```
schedule(schedule_func, date_rule, time_rule)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| schedule_func | function | 策略定时执行算法 |
| date_rule | str | n + 时间单位， 可选'd/w/m' 表示n天/n周/n月 |
| time_rule | str | 执行算法的具体时间 (%H:%M:%S 格式) |

**返回值:**

`None`

**示例：**

```
def init(context):
    #每天的19:06:20执行策略algo_1
    schedule(schedule_func=algo_1, date_rule='1d', time_rule='19:06:20')
    #每月的第一个交易日的09:40:00执行策略algo_2
    schedule(schedule_func=algo_2, date_rule='1m', time_rule='9:40:00')

def algo_1(context):
    print(context.symbols)

def algo_2(context):
    order_volume(symbol='SHSE.600000', volume=200, side=OrderSide_Buy, order_type=OrderType_Market, position_effect=PositionEffect_Open)

```

**注意：**

1.time_rule的时,分,秒均可以只输入个位数，例:`'9:40:0'`或`'14:5:0'`,但若对应位置为零，则0不可被省略，比如不能输入`'14:5: '`

2.目前暂时支持`1d`、`1w`、`1m`

### run - 运行策略

**函数原型:**

```
run(strategy_id='', filename='', mode=MODE_UNKNOWN, token='', backtest_start_time='',
    backtest_end_time='', backtest_initial_cash=1000000,
    backtest_transaction_ratio=1, backtest_commission_ratio=0,
    backtest_slippage_ratio=0, backtest_adjust=ADJUST_NONE, backtest_check_cache=1,
    serv_addr='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| strategy_id | str | 策略id |
| filename | str | 策略文件名称 |
| mode | int | 策略模式MODE_LIVE(实时)=1MODE_BACKTEST(回测) =2 |
| token | str | 用户标识 |
| backtest_start_time | str | 回测开始时间(%Y-%m-%d %H:%M:%S格式) |
| backtest_end_time | str | 回测结束时间(%Y-%m-%d %H:%M:%S格式) |
| backtest_initial_cash | double | 回测初始资金, 默认1000000 |
| backtest_transaction_ratio | double | 回测成交比例, 默认1.0, 即下单100%成交 |
| backtest_commission_ratio | double | 回测佣金比例, 默认0 |
| backtest_slippage_ratio | double | 回测滑点比例, 默认0 |
| backtest_adjust | int | 回测复权方式(默认不复权)ADJUST_NONE(不复权)=0ADJUST_PREV(前复权)=1ADJUST_POST(后复权)=2 |
| backtest_check_cache | int | 回测是否使用缓存：1 - 使用， 0 - 不使用；默认使用 |
| serv_addr | str | 终端服务地址, 默认本地地址, 可不填，若需指定应输入ip+端口号，如"127.0.0.1:7001" |
| backtest_match_mode | int | 回测撮合模式： 1-实时撮合：在当前bar的收盘价/当前tick的price撮合，0-延时撮合：在下个bar的开盘价/下个tick的price撮合，默认是模式0 |

**返回值:**

`None`

**示例：**

```
run(strategy_id='strategy_1', filename='main.py', mode=MODE_BACKTEST, token='token_id',
    backtest_start_time='2016-06-17 13:00:00', backtest_end_time='2017-08-21 15:00:00')

```

**注意：**

**1.** run函数中，`mode=1`也可改为`mode=MODE_LIVE`，两者等价，`backtest_adjust`同理

**2.** backtest_start_time和backtest_end_time中月,日,时,分,秒均可以只输入个位数，例:`'2016-6-7 9:55:0'`或`'2017-8-1 14:6:0'`,但若对应位置为零，则0不可被省略,比如不能输入`"2017-8-1 14:6: "`

**3.** filename指运行的py文件名字，如该策略文件名为Strategy.py,则此处应填"Strategy.py"

### stop - 停止策略

停止策略，退出策略进程

**函数原型:**

```
stop()

```

**返回值:**

`None`

**示例：**

```
#若订阅过的代码集合为空，停止策略
if not context.symbols:
   stop()

```

### timer - 设置定时器

设定定时器的间隔秒数，每过设定好的秒数调用一次计时器 timer_func()，直到 timer_stop()结束定时器为止。
（仿真、实盘场景适用，回测模式下不生效）

**函数原型：**

```
timer(timer_func, period, start_delay)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| timer_func | function | 在 timer 设置的时间到达时触发的事件函数 |
| period | int | 定时事件间隔毫秒数，设定每隔多少毫秒触发一次定时器，范围在 [1,43200000] |
| start_delay | int | 等待秒数(毫秒)，设定多少毫秒后启动定时器，范围在[0,43200000] |

**返回值：** **dict**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| timer_status | int | 定时器设置是否成功，成功=0，失败=非 0 错误码（timer_id 无效）。 |
| timer_id | int | 设定好的定时器 id |

### timer_stop - 停止定时器

停止已设置的定时器

**函数原型：**

```
timer_stop(timer_id)

```

**参数：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| timer_id | int | 要停止的定时器 id |

**返回值：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| is_stop | bool | 是否成功停止，True or False |

**示例：**

```
def init(context):
    # 每隔1分钟执行ontime_1, 即时启动
    context.timerid_1 = timer(timer_func=ontimer_1, period=60000, start_delay=0)
    context.counter_1 = 0

    # 每隔半小时执行ontime_2, 5分钟之后启动
    context.timerid_2 = timer(timer_func=ontimer_2, period=300000, start_delay=0)
    print('启动定时器2：', context.now)
    context.counter_2 = 0

def ontimer_1(context):
    # 定时器执行次数计数
    context.counter_1 += 1
    # 定时器执行逻辑
    print('定时器1：', context.now)

def ontimer_2(context):
    # 定时器执行次数计数
    context.counter_2 += 1
    # 定时器执行逻辑（如查询账户资金）
    cash = context.account().cash

    print('定时器2：', context.now)

    # 按执行次数条件停止定时器
    if context.counter_1 >= 5:
        ret1 = timer_stop(context.timerid_1['timer_id'])
        if ret1:
            print("结束1分钟定时器")

    if context.counter_2 >= 10:
        ret2 = timer_stop(context.timerid_2['timer_id'])

```

**注意：**

**1.** 仿真、实盘场景适用，回测模式下不生效

**2.** period 从前一次事件函数开始执行时点起算，若下一次事件函数需要执行时，前一次事件函数没运行完毕，等待上一个事件执行完毕再执行下一个事件。

     [ ** ](python_object_trade.html#algoorder---算法委托母单对象) [ ** ](python_basic.html#基础函数)
