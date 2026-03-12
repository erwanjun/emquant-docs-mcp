# 策略基类

## 基本成员函数

### Strategy - 构造函数

构造策略对象。

**函数原型:**

```
Strategy();
Strategy(string token, string strategyId, StrategyMode mode);

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| token | string | 系统权限密钥,可在终端系统设置-密钥管理中生成 |
| strategyId | string | 策略ID,在终端中获取 |
| mode | StrategyMode | 策略模式，参见 enum StrategyMode |

**注意事项：**

- 一个进程只能构造一个策略对象。

### Run - 运行策略

运行策略。只有调用Run后，才会驱动所有的事件，如行情接入与交易事件。

**函数原型:**

```
int Run();

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | int | 如果策略正常退出返回0， 非正常退出返回错误码 |

**注意事项：**

调用Run会阻塞线程，策略进入事件驱动状态，所以所有初始操作（如读配置文件，分配缓冲区等）都应该在Run之前完成，如果run退出，意味着策略运行结束，整个进程应该就此退出。

### Stop - 停止策略

用于停止策略， 也就是如果调用Run()之后， 在某个事件响应中调用Stop, 这是Run就是退出，并返回0。

**函数原型:**

```
void Stop();

```

### SetToken - 设置用户token

**函数原型:**

```
int SetToken(string token)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| token | string | 系统权限密钥,可在终端系统设置-密钥管理中生成 |

**注意事项:**
不管是从构造函数传入还成员函数传入，`token`, `strategyId`, `mode` 都是必须要设置的参数。

### SetMode - 设置运行模式

**函数原型**

```
int SetMode(StrategyMode mode)

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| mode | StrategyMode | 策略运行模式，参见StrategyMode |

**注意事项:**
不管是从构造函数传入还成员函数传入，`token`, `strategyId`, `mode` 都是必须要设置的参数

### SetStrategyId - 设置策略ID

**函数原型：**

```
int SetStrategyId(string strategyId)

```

**注意事项:**
不管是从构造函数传入还成员函数传入，`token`, `strategyId`, `mode` 都是必须要设置的参数

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| strategyId | string | 策略ID,在终端中获取 |

### GetAccountStatus - 获取策略所有账户状态

**函数原型：**

```
List<AccountStatus> GetAccountStatus()

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | List | AccountStatus 列表 |

**示例:**

```
//获取当策略所有账户状态
var status_l = GetAccountStatus();
//遍历账户
foreach (var status in status_l)
{
    //打印 AccountStatus 字段
    System.Console.WriteLine("accountId: {0}, accountName: {1}, state: {2}, errorCode: {3}, errorMsg: {4}", status.accountId, status.accountName, status.state, status.errorCode, status.errorMsg);
}

```

### GetAccountStatus - 获取指定账户状态

**函数原型：**

```
AccountStatus GetAccountStatus(string accountId)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | AccountStatus | 账户状态结构 |

### Schedule - 预设定时任务

在指定时间自动执行策略算法, 通常用于选股类型策略。Schedule一般在OnInit中调用。如果Schedule预设成功，那么达成预设时间条件时，OnSchedule会被调用，并在OnSchedule的参数中返回设置的`dataRule`和`timeRule`。Schedule可以调用多次，设置多个不同定时任务。

**函数原型:**

```
int Schedule(string dataRule, string timeRule);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| dataRule | string | n + 时间单位， 可选’d/w/m’ 表示n天/n周/n月 |
| timeRule | string | 执行算法的具体时间 (%H:%M:%S 格式) |
| 返回值 | int | 预设成功返回0， 预设失败返回错误码 |

**示例：**

```

    #每天的19:06:20执行
    Schedule(dateRule="1d", timeRule="19:06:20")

    #每月的第一个交易日的09:40:00执行
    Schedule(dateRule="1m", time_rule="9:40:00")

```

**注意事项：**

- 现在`dataRule`暂只支持 1d,1w,1m， 任意n后续会支持。

### Now - 获取当前时间

**函数原型:**

```
DateTime Now();

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | DateTime | 当前时间 |

**注意事项：**

- 实时模式下，返回当前的系统时间。回测模式下，返回当前的回测时间点。格式是DateTime。

### SetBacktestConfig - 设置回测参数

如果mode设置为回测模式，则在调用Run之前，需要先设置本函数设置回测参数。在实时模式下，该调用被忽略。

**函数原型:**

```
int SetBacktestConfig(
    string startTime,
    string endTime,
    double initialCash = 1000000,
    double transactionRatio = 1,
    double commissionRatio = 0,
    double slippageRatio = 0,
    Adjust    adjust = 0,
    int    checkCache = 1
);

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| startTime | string | 回测开始时间(%Y-%m-%d %H:%M:%S格式) |
| endTime | string | 回测结束时间(%Y-%m-%d %H:%M:%S格式) |
| initialCash | double | 回测初始资金, 默认1000000 |
| transactionRatio | double | 回测成交比例, 默认1.0, 即下单100%成交 |
| commissionRatio | double | 回测佣金比例, 默认0 |
| slippageRatio | double | 回测滑点比例, 默认0 |
| adjust | Adjust | 复权方式，参见 enum Adjust |
| checkCache | int | 回测是否使用缓存：1 - 使用， 0 - 不使用；默认使用 |

**注意：**
startTime和endTime中月,日,时,分,秒均可以只输入个位数，例:`"2016-6-7 9:55:0"`或`"2017-8-1 14:6:0"`,但若对应位置为零，则0不可被省略,比如不能输入`"2017-8-1 14:6: "`
     ** ** ** ** ** **
