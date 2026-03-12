## 基金增值数据函数（付费）

### FndGetEtfConstituents - 查询ETF最新成分股

查询某只 ETF 在最新交易日的成分股持有情况和现金替代信息

注意：vip特色数据权益，股票实盘客户已享有，非股票实盘客户可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndEtfConstituents> FndGetEtfConstituents(string symbol);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | ETF 代码 | Y | 无 | 必填，只能输入一个 symbol, 如：SZSE.159919 |

返回值：

`FndEtfConstituents` 结构列表，参见`FndEtfConstituents`定义与`GMDataList`类的用法。

示例：

```
FndGetEtfConstituents("SHSE.510050")

```

注意：

1. 只返回上交所、深交所的成分股，不提供其余交易所的成分股票。

### FndGetStockPortfolio - 查询基金资产组合（股票投资组合）

查询某只基金在指定日期的基金资产组合（股票投资组合）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndPortfolioStockInfo> FndGetStockPortfolio(string symbol, int reportType, string startDate = null, string endDate = null);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]，如：SZSE.161133 |
| reportType | int | 报表类别 | Y | 无 | 公布持仓所在的报表类别，必填，可选： 1:第一季度 2:第二季度 3:第三季报 4:第四季度 6:中报 12:年报 |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`FndPortfolioStockInfo` 结构列表，参见`FndPortfolioStockInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetStockPortfolio("SHSE.510300", 1)

```

注意：

1. 

仅提供场内基金（ETF、LOF、FOF-LOF）的资产组合数据。

2. 

当`startDate == endDate`时，取离`endDate`最近公告日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### FndGetBondPortfolio - 查询基金资产组合（债券投资组合）

查询某只基金在指定日期的基金资产组合（债券投资组合）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndPortfolioBondInfo> FndGetBondPortfolio(string symbol, int reportType, string startDate = null, string endDate = null);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]，如：SZSE.161133 |
| reportType | int | 报表类别 | Y | 无 | 公布持仓所在的报表类别，必填，可选： 1:第一季度 2:第二季度 3:第三季报 4:第四季度 6:中报 9:前三季报 12:年报 |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`FndPortfolioBondInfo` 结构列表，参见`FndPortfolioBondInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetBondPortfolio("SHSE.510300", 1)

```

注意：

1. 

仅提供场内基金（ETF、LOF、FOF-LOF）的资产组合数据。

2. 

当`startDate == endDate`时，取离`endDate`最近公告日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### FndGetFundPortfolio - 查询基金资产组合（基金投资组合）

查询某只基金在指定日期的基金资产组合（基金投资组合）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndPortfolioFundInfo> FndGetFundPortfolio(string symbol, int reportType, string startDate = null, string endDate = null);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]，如：SZSE.161133 |
| reportType | int | 报表类别 | Y | 无 | 公布持仓所在的报表类别，必填，可选： 1:第一季度 2:第二季度 3:第三季报 4:第四季度 6:中报 9:前三季报 12:年报 |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日），%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`FndPortfolioFundInfo` 结构列表，参见`FndPortfolioFundInfo`定义与`GMDataList`类的用法。

注意：

1. 

仅提供场内基金（ETF、LOF、FOF-LOF）的资产组合数据。

2. 

当`startDate == endDate`时，取离`endDate`最近公告日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### FndGetNetValue - 查询基金净值数据

查询某只基金在指定时间段的基金净值数据

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndNetValueInfo> FndGetNetValue(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]如：SZSE.159919 |
| startDate | string | 开始时间 | N | null | 开始时间日期，%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期，%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`FndNetValueInfo` 结构列表，参见`FndNetValueInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetNetValue("SHSE.510300")

```

注意：

1. 

仅提供场内基金（ETF、LOF、FOF-LOF）的净值数据。

2. 

当`startDate == endDate`时，取离`endDate`最近日期的一条数据，
当`startDate < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### FndGetAdjFactor - 查询基金复权因子

查询某只基金在一段时间内的复权因子

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndAdjFactorInfo> FndGetAdjFactor(string symbol, string startDate = null, string endDate = null, string baseDate = null);

```

参数：

``

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]，如：SZSE.159919 |
| startDate | string | 开始时间 | N | null | 开始时间交易日期，%Y-%m-%d 格式， 默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间交易日期，%Y-%m-%d 格式， 默认null表示最新时间 |
| baseDate | string | 复权基准日 | N | null | 前复权的基准日，%Y-%m-%d 格式， 默认null表示最新时间 |

返回值：

`FndAdjFactorInfo` 结构列表，参见`FndAdjFactorInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetAdjFactor("SHSE.510300")

```

注意：

1. 

T+1 日复权因子会二次更新，分别在 T 日 19:00 和 T+1 日 19:00 更新。仅提供场内基金（ETF、LOF、FOF-LOF）的复权因子数据。

2. 

复权价格计算：
`T日后复权价格 = T日不复权价格  T日累计后复权因子`
`T日前复权价格 = T日不复权价格  T日前复权因子`

3. 

上市首日后复权因子合累计后复权因子为 1，最近一次除权除息日后的交易日前复权因子为 1

4. 

前复权基准日`baseDate`应不早于设定的结束日期`endDate`，不晚于最新交易日。若设定的基准日早于`endDate`则等同于`endDate`，若设定的基准日晚于最新交易日则等同于最新交易日。

5. 

当`startDate` 小于或等于 `endDate` 时取指定时间段的数据,当`startDate` > `endDate`时返回报错.

### FndGetDividend - 查询基金分红信息

查询指定基金在一段时间内的分红信息

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndDividendInfo> FndGetDividend(string symbol, string startDate, string endDate);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol], 如：SZSE.159919 |
| startDate | string | 开始时间 | Y | 无 | 必填，开始时间日期（场内除息日），%Y-%m-%d 格式 |
| endDate | string | 结束时间 | Y | 无 | 必填，结束时间日期（场内除息日），%Y-%m-%d 格式 |

返回值：

`FndDividendInfo` 结构列表，参见`FndDividendInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetDividend("SHSE.510300", "2021-1-1", "2023-1-1")

```

### FndGetSplit - 查询基金拆分折算信息

查询指定基金在一段时间内的拆分折算信息

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 

函数原型：

```
public static GMDataList<FndSplitInfo> FndGetSplit(string symbol, string startDate, string endDate);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 基金代码 | Y | 无 | 必填，只能输入一个基金的[symbol]，如：SZSE.159919 |
| startDate | string | 开始时间 | Y | 无 | 必填，开始时间日期（场内除权日），%Y-%m-%d 格式 |
| endDate | string | 结束时间 | Y | 无 | 必填，结束时间日期（场内除权日），%Y-%m-%d 格式 |

返回值：

`FndSplitInfo` 结构列表，参见`FndSplitInfo`定义与`GMDataList`类的用法。

示例：

```
FndGetSplit("SZSE.161725", "2000-01-01", "2022-09-07")

```

---
     ** ** ** ** ** **
