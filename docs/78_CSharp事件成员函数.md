## 事件成员函数

### OnInit - 初始化完成

sdk初始化完成时触发, 用户可以改写此成员函数，在些订阅行情，提取历史数据等初始化操作。

**函数原型:**

```
virtual void OnInit();

```

### OnTick - 收到Tick行情

收到Tick行情时触发

**函数原型:**

```
virtual void OnTick(Tick tick);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| tick | Tick | 收到的Tick行情 |

### OnBar - 收到bar行情

收到bar行情时触发

**函数原型:**

```
virtual void OnBar(Bar bar);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bar | List | 收到的Bar行情 |

### OnOrderStatus - 委托变化

委托变化时触发

**函数原型:**

```
virtual void OnOrderStatus(Order order);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order | Order | 发生变化的委托 |

### OnExecutionReport - 执行回报

收到回报时触发

**函数原型:**

```
virtual void OnExecutionReport(ExecRpt rpt);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| rpt | ExecRpt | 收到的回报 |

### OnParameter - 参数变化

参数变化时触发, 一般是终端修了动态参数

**函数原型:**

```
virtual void OnParameter(List<Parameter> param);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| param | List | 变化的参数 |

### OnSchedule - 定时任务触发

预设任务时间条件符合时触发

**函数原型:**

```
virtual void OnSchedule(string dataRule, string timeRule);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| dataRule | string | 设置的 dataRule |
| timeRule | string | 设置的 timeRule |

### OnBacktestFinished - 回测完成后收到绩效报告

回测完成后收到绩效报告时触发

**函数原型:**

```
virtual void OnBacktestFinished(Indicator indicator);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| dataRule | Indicator | 设置的 dataRule |

### OnAccountStatus - 实盘账号状态变化

实盘账号状态变化时触发, 比如实盘账号登录，退出登录等

**函数原型:**

```
virtual void OnAccountStatus(AccountStatus accountStatus);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| accountStatus | AccountStatus | 对应变化的账号 |

### OnError - 错误产生

有错误产生时触发, 比如网络断开。

**函数原型:**

```
virtual void OnError(int errorCode, string errorMsg);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errorCode | int | 错误码 |
| errorMsg | string | 错误信息 |

### OnStop - 收到策略停止信号

终端点击停止策略时触发

**函数原型:**

```
virtual void OnStop();

```

### OnMarketDataConnected - 数据服务已经连接上

数据服务已经连接时触发

**函数原型:**

```
virtual void OnMarketDataConnected();

```

### OnTradeDataConnected - 交易已经连接上

交易已经连接时触发

**函数原型:**

```
virtual void OnTradeDataConnected();

```

### OnMarketDataDisconnected - 数据连接断开了

数据连接断开时触发

**函数原型:**

```
virtual void OnMarketDataDisconnected();

```

### OnTradeDataDisconnected - 交易连接断开了

交易连接断开时触发

**函数原型:**

```
virtual void OnTradeDataDisconnected();

```
     ** ** ** ** ** **
