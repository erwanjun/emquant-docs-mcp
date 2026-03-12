## 可转债增值数据函数（付费）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 
### BndGetConversionPrice - 查询可转债转股价变动信息

查询可转债一段时间的转股价变动和转股结果

函数原型：

```
public static GMDataList<BndConversionPrice> BndGetConversionPrice(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的[symbol] |
| startDate | string | 开始时间 | N | null | 开始时间日期（转股价格生效日），%Y-%m-%d 格式， 默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（转股价格生效日），%Y-%m-%d 格式， 默认null表示最新时间 |

返回值：

`BndConversionPrice` 结构列表，参见`BndConversionPrice`定义与`GMDataList`类的用法。

示例：

```
BndGetConversionPrice("SZSE.123015")

```

注意：

1. 

本期转股数、累计转股金额、债券流通余额在执行日期收盘后才有数据。

2. 

当`startDate == endDate`时，取离`endDate`最近转股价格生效日期的一条数据，
当`startDate < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### BndGetCallInfo - 查询可转债赎回信息

查询可转债一段时间内的赎回情况

函数原型：

```
public static GMDataList<BndCallInfo> BndGetCallInfo(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的[symbol] |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日），%Y-%m-%d 格式， 默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日），%Y-%m-%d 格式， 默认null表示最新时间 |

返回值：

`BndCallInfo` 结构列表，参见`BndCallInfo`定义与`GMDataList`类的用法。

示例：

```
BndGetCallInfo("SHSE.110041")

```

注意：

当`startDate == endDate`时，取离`endDate`最近公告日的一条数据，
当`startDate < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### BndGetPutInfo - 查询可转债回售信息

查询可转债一段时间内的回售情况

函数原型：

```
public static GMDataList<BndPutInfo> BndGetPutInfo(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的[symbol] |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日），%Y-%m-%d 格式， 默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日），%Y-%m-%d 格式， 默认null表示最新时间 |

返回值：

`BndPutInfo` 结构列表，参见`BndPutInfo`定义与`GMDataList`类的用法。

示例：

```
BndGetPutInfo("SZSE.128015")

```

注意：

当`startDate == endDate`时，取离`endDate`最近公告日的一条数据，
当`startDate < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### BndGetAmountChange - 查询可转债剩余规模变动

查询可转债转股、回售、赎回等事件导致的剩余规模变动的情况

函数原型：

```
public static GMDataList<BndAmountChange> BndGetAmountChange(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的[symbol] |
| startDate | string | 开始时间 | N | null | 开始时间日期（变动日期），%Y-%m-%d 格式， 默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（变动日期），%Y-%m-%d 格式， 默认null表示最新时间 |

返回值：

`BndAmountChange` 结构列表，参见`BndAmountChange`定义与`GMDataList`类的用法。

示例：

```
BndGetAmountChange("SZSE.123015")

```

注意：

1. 

变动类型指定为首发时，返回的剩余金额为发行金额。

2. 

当`startDate == endDate`时，取离`endDate`最近变动日期的一条数据，
当`startDate < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

---
     ** ** ** ** ** **
