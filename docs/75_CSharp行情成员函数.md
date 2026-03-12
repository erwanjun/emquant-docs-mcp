## 行情成员函数

### subscribe - 订阅行情

订阅行情推送，实时模式下订阅实时行情推送，回测模式下订阅历史行情推送。订阅tick会触发OnTick回调，订阅bar则触发OnBar回调。

**函数原型:**

```
int Subscribe(string symbols, string frequency, bool unsubscribePrevious = false);

```

**参数：**

``

[](../data/stock.html#行情数据)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 订阅标的代码列表, 字符串格式，如有多个代码, 中间用,(英文逗号) 隔开 |
| frequency | string | 频率,  支持 'tick', '60s', '300s', '900s' 等, 默认'1d', 详情见股票行情数据 |
| unsubscribePrevious | bool | 是否取消过去订阅的symbols, 默认false不取消, 输入true则取消所有原来的订阅。 |
| 返回值 | int | 订阅成功返回0， 订阅失败返回错误码 |

**示例：**

```
//订阅 SHSE.600000和 SZSE.000001 两个标的的tick行情
Subscribe(symbols="SHSE.600000,SHSE.600004", frequency="tick");

//订阅 SHSE.600000和 SZSE.000001 两个标的的1分钟bar
Subscribe(symbols="SHSE.600000,SHSE.600004", frequency="60s");

```

### unsubscribe - 退订行情

退订已经订阅行情推送， 与Subscribe作用相返。

**函数原型:**

```
int unsubscribe(string symbols, string frequency);

```

**参数：**

``

[](../data/stock.html#行情数据)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 退订标的代码列表, 字符串格式，如有多个代码, 中间用,(英文逗号) 隔开 |
| frequency | string | 频率,  支持 'tick', '60s', '300s', '900s' 等, 默认'1d', 详情见股票行情数据 |
| 返回值 | int | 退订成功返回0， 退订失败返回错误码 |

**示例：**

```
//退订 SHSE.600000和 SZSE.000001 两个标的的tick行情
Unsubscribe(symbols="SHSE.600000,SHSE.600004", frequency="tick");

```
     ** ** ** ** ** **
