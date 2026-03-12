## 数据订阅

### subscribe - 行情订阅

订阅行情, 可以指定symbol, 数据滑窗大小, 以及是否需要等待全部代码的数据到齐再触发事件。

**函数原型:**

```
subscribe(symbols, frequency='1d', count=1, wait_group=False, wait_group_timeout='10s', unsubscribe_previous=False)

```

**参数：**

（参见 symbol）````

（参见 行情数据）

``（参见 数据滑窗）

````````

``````


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | str or list | 订阅标的代码, 支持字串格式，如有多个代码, 中间用 , (英文逗号) 隔开, 也支持 ['symbol1', 'symbol2'] 这种列表格式 |
| frequency | str | 频率,  支持 'tick', '60s', '300s', '900s' 等, 默认'1d', 详情见股票行情数据 |
| count | int | 订阅数据滑窗大小, 默认1 ,详情见数据滑窗 |
| wait_group | bool | 是否需要等待全部代码的数据到齐再触发事件, 默认False不到齐。设置为True则等待订阅标的eob相同的bar全部到齐再被调用。该参数只对Bar数据有效。 |
| wait_group_timeout | str | 超时时间设定, 支持s结尾表示单位秒, 默认10s |
| unsubscribe_previous | bool | 是否取消过去订阅的symbols, 默认False不取消, 输入True则取消所有原来的订阅。 |
| fields | str | 指定返回对象字段, 如有多个字段, 中间用, 隔开, 默认所有, 具体字段见:tick 对象 和 bar 对象 ，在 subscribe 函数中指定的字段越少，context.data查询速度越快 |
| format | str | 返回格式，默认"df", "df": 数据框格式，返回dataframe（默认）,"row": 原始行式组织格式，返回list[dict]（当用户对性能有要求时, 推荐使用此格式）, "col": 列式组织格式，返回dict 。 |

**返回值：**

`None`

**示例：**

```
def init(context):
    # 同时订阅600519的tick数据和分钟数据
    subscribe(symbols='SHSE.600519', frequency='tick', count=2)
    subscribe(symbols='SHSE.600519', frequency='60s', count=2)

def on_tick(context,tick):
    print('收到tick行情---', tick)

def on_bar(context,bars):
    print('收到bar行情---', bars)
    data = context.data(symbol='SHSE.600519', frequency='60s', count=2)
    print('bar数据滑窗---', data)

```

**注意：**

**1.** subscribe 支持多次调用，支持同一标的不同频率订阅。订阅后的数据储存在本地，需要通过 context.data 接口调用或是直接在 on_tick 或 on_bar 中获取。

**2.** 在实时模式下，最新返回的数据是**不复权**的。

**3.** 订阅函数subscribe里面指定字段越少，查询速度越快，目前效率是row > col > df。

**4.** 当subscribe的format指定col时，tick的quotes字段会被拆分，只返回买卖一档的量和价，即只有bid_p，bid_v, ask_p和ask_v。

**5.** 在回测模式下，subscribe使用wait_group=True时，等待的标的需要下个时间到期。例如订阅60s的频率A和B标的，当天第一条bar数据是在09:32:00推送eob为09:31:00的A和B的bar，因为需要走到09:32:00才能确认09:31:00的全部bar是否到齐。在实时模式下，会根据实时到齐时间推送。

### unsubscribe - 取消订阅

取消行情订阅, 默认取消所有已订阅行情

**函数原型:**

```
unsubscribe(symbols='*', frequency='60s')

```

**参数：**

（参见 symbol）````
``

（参见 行情数据）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | str or list | 标的代码, 支持字串格式，如果有多个代码, 中间用 , (英文逗号) 隔开；*表示所有, 默认退订所有代码  也支持 ['symbol1', 'symbol2'] 这种列表格式的参数 |
| frequency | str | 频率,  支持 'tick', '60s', '300s', '900s' 等, 默认'1d', 详情见股票行情数据 |

**返回值:**

`None`

**示例：**

```
unsubscribe(symbols='SHSE.600000,SHSE.600004', frequency='60s')

```

**注意：**
如示例所示代码，取消`SHSE.600000,SHSE.600004`两只代码`60s`行情的订阅，若`SHSE.600000`同时还订阅了`"300s"`频度的行情，该代码不会取消该标的此频度的订阅
     [ ** ](python_basic.html#timerstop---停止定时器) [ ** ](python_subscribe.html#subscribe---行情订阅)
