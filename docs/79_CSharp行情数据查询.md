# 数据查询函数

## 行情数据查询函数（免费）

GMApi 静态方法

### Current - 查询当前行情快照

查询当前行情快照，返回tick数据。回测时，返回回测时间点的tick数据

**函数原型:**

```
static GMDataList<Tick> Current(string symbols);

```

**参数：**

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 查询代码，如有多个代码, 中间用 , (英文逗号) 隔开 |
| 返回值 | GMDataList | 一个GMDataList<Tick>对象 |

**示例：**

```
static GMDataList<Tick> currentData = GMApi.Current("SZSE.000001,SZSE.000002");

```

**注意：**

startTime和endTime中月,日,时,分,秒均可以只输入个位数,例:`"2010-7-8 9:40:0"`或`"2017-7-30 12:3:0"`,但若对应位置为零，则`0`不可被省略,如不可输入`"2017-7-30 12:3: "`

### HistoryTicks - 查询历史Tick行情

**函数原型:**

```
static GMDataList<Tick> HistoryTicks(string symbols, string startTime, string endTime, Adjust adjust = Adjust.ADJUST_NONE, string adjustEndTime = null, bool skipSuspended = true, string fillMissing = null)

```

**参数：**

``

``

``````

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 标的代码,若要获取多个标的的历史数据，可以采用中间用 , (英文逗号) 隔开的方法 |
| startTime | string | 开始时间 (%Y-%m-%d %H:%M:%S 格式),其中日线包含start_time数据, 非日线不包含start_time数据 |
| endTime | string | 结束时间 (%Y-%m-%d %H:%M:%S 格式), |
| adjust | Adjust | 复权方式，参见 enum Adjust |
| adjustEndTime | string | 复权基点时间, 默认当前时间 |
| skipSuspended | bool | 是否跳过停牌, 默认跳过 |
| fillMissing | string | 填充方式,  None - 不填充,  'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认None |
| 返回值 | GMDataList | 一个GMDataList<Tick>对象 |

**示例：**

```
GMDataList<Tick> historyTick = GMApi.HistoryTicks("SHSE.000300", "2010-07-28 08:00:00", "2017-07-30 16:00:00")

```

**注意：**

**1.**startTime和endTime中月,日,时,分,秒均可以只输入个位数,例:`"2010-7-8 9:40:0"`或`"2017-7-30 12:3:0"`,但若对应位置为零，则`0`不可被省略,如不可输入`"2017-7-30 12:3: "`

**2.** skipSuspended 和 fillMissing 参数暂不支持

### HistoryBars - 查询历史Bar行情

**函数原型:**

```
static GMDataList<Bar> HistoryBars(string symbols, string frequency, string startTime, string endTime, Adjust adjust = Adjust.ADJUST_NONE, string adjustEndTime = null, bool skipSuspended = true, string fillMissing = null)

```

**参数：**

``

[](../faq/583.html#订阅问题)

``

``````

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 标的代码,若要获取多个标的的历史数据，可以采用中间用 , (英文逗号) 隔开的方法 |
| frequency | string | 频率,  支持 '1d', '60s'等, 默认 '1d', 详情见订阅频率 |
| startTime | string | 开始时间 (%Y-%m-%d %H:%M:%S 格式),其中日线包含start_time数据, 非日线不包含start_time数据 |
| endTime | string | 结束时间 (%Y-%m-%d %H:%M:%S 格式), |
| adjust | Adjust | 复权方式，参见 enum Adjust |
| adjustEndTime | string | 复权基点时间, 默认当前时间 |
| skipSuspended | bool | 是否跳过停牌, 默认跳过 |
| fillMissing | string | 填充方式,  None - 不填充,  'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认None |
| 返回值 | GMDataList | 一个GMDataList<Bar>对象 |

**示例：**

```
//获取1分钟的bar
GMDataList<Bar> historyBar = GMApi.HistoryBars("SHSE.000300", "60s", "2010-07-28 08:00:00", "2017-07-30 16:00:00");

//获取60分钟的bar
GMDataList<Bar> historyBar = GMApi.HistoryBars("SHSE.000300", "3600s", "2010-07-28 08:00:00", "2017-07-30 16:00:00");

//获取日线
GMDataList<Bar> historyBar = GMApi.HistoryBars("SHSE.000300", "1d", "2010-07-28 08:00:00", "2018-07-30 16:00:00");

```

**注意：**

**1.**startTime和endTime中月,日,时,分,秒均可以只输入个位数,例:`"2010-7-8 9:40:0"`或`"2017-7-30 12:3:0"`,但若对应位置为零，则`0`不可被省略,如不可输入`"2017-7-30 12:3: "`

**2.** skipSuspended 和 fillMissing 参数暂不支持

### HistoryTicksN - 查询最新n条Tick行情

**函数原型:**

```
static GMDataList<Tick> HistoryTicksN(string symbols, int n, string endTime = null, Adjust adjust = Adjust.ADJUST_NONE, string adjustEndTime = null, bool skipSuspended = true, string fillMissing = null)

```

**参数：**

``

``

``````

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 标的代码(只允许单个标的的代码字符串) |
| n | int | 获取行情的数量 |
| endTime | string | 从指定时间开始，往前取行情, 如果为NULL, 那么为当前时间开始（回测模式下为当前回测时间点） |
| adjust | Adjust | 复权方式，参见 enum Adjust |
| adjustEndTime | string | 复权基点时间, 默认当前时间 |
| skipSuspended | bool | 是否跳过停牌, 默认跳过 |
| fillMissing | string | 填充方式,  None - 不填充,  'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认None |
| 返回值 | GMDataList | 一个GMDataList<Tick>对象 |

**示例：**

```

//获取沪深300最新10条tick
GMDataList<Tick> ticks = GMApi.HistoryTicksN("SHSE.000300", 10);

```

**注意：**

**1.**endTime中月,日,时,分,秒均可以只输入个位数,例:`"2010-7-8 9:40:0"`或`"2017-7-30 12:3:0"`,但若对应位置为零，则`0`不可被省略,如不可输入`"2017-7-30 12:3: "`

**2.** skipSuspended 和 fillMissing 参数暂不支持

### HistoryBarsN - 查询最新n条Bar行情

**函数原型:**

```
static GMDataList<Bar> HistoryBarsN(string symbols, string frequency, int n, string endTime = null, Adjust adjust = Adjust.ADJUST_NONE, string adjustEndTime = null, bool skipSuspended = true, string fillMissing = null)

```

**参数：**

[](../faq/583.html#订阅问题)

``

``

``````

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | 标的代码(只允许单个标的的代码字符串) |
| frequency | string | 频率,  支持 '1d', '60s'等, 默认 '1d', 详情见订阅频率 |
| n | int | 获取行情的数量 |
| endTime | string | 从指定时间开始，往前取行情, 如果为NULL, 那么为当前时间开始（回测模式下为当前回测时间点） |
| adjust | Adjust | 复权方式，参见 enum Adjust |
| adjustEndTime | string | 复权基点时间, 默认当前时间 |
| skipSuspended | bool | 是否跳过停牌, 默认跳过 |
| fillMissing | string | 填充方式,  None - 不填充,  'NaN' - 用空值填充, 'Last' - 用上一个值填充, 默认None |
| 返回值 | GMDataList | 一个GMDataList<Bar>对象 |

**示例：**

```

//获取沪深300最新10条1分钟bar
GMDataList<Bar> bars = GMApi.HistoryBarsN("SHSE.000300", "60s", 10);

```

**注意：**

**1.**endTime中月,日,时,分,秒均可以只输入个位数,例:`"2010-7-8 9:40:0"`或`"2017-7-30 12:3:0"`,但若对应位置为零，则`0`不可被省略,如不可输入`"2017-7-30 12:3: "`

**2.** skipSuspended 和 fillMissing 参数暂不支持

---
     ** ** ** ** ** **
