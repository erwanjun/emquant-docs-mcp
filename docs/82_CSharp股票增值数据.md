## 股票增值数据函数（付费）

注意：vip特色数据权益，股票实盘客户已享有，非股票实盘客户可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 
### StkGetIndustryCategory - 查询行业分类

查询指定行业来源的行业列表

函数原型：

```
public static GMDataList<StkIndustryCategory> StkGetIndustryCategory(string source = null, int level = 0);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| source | string | 行业来源 | N | 'zjh2012' | 'zjh2012'- 证监会行业分类 2012（默认）， 'sw2021'- 申万行业分类 2021 |
| level | int | 行业分级 | N | 1 | 1 - 一级行业（默认），2 - 二级行业，3 - 三级行业 |

返回值：

`StkIndustryCategory` 结构列表，参见`StkIndustryCategory`定义与`GMDataList`类的用法。

示例：

```
StkGetIndustryCategory("sw2021", 2)

```

注意：

1. 证监会行业分类 2012 没有三级行业，若输入`source='zjh2012', level=3`则参数无效，返回空

### StkGetIndustryConstituents - 查询行业成分股

查询指定某个行业的成分股

函数原型：

```
public static GMDataList<StkIndustryConstituent> StkGetIndustryConstituents(string industryCode, string date = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| industryCode | string | 行业代码 | Y | 无 | 需要查询成分股的行业代码，可通过StkGetIndustryCategory获取 |
| date | string | 查询日期 | N | null | 查询行业成分股的指定日期，%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`StkIndustryConstituent` 结构列表，参见`StkIndustryConstituent`定义与`GMDataList`类的用法。

示例：

```
StkGetIndustryConstituents("A", "2022-09-05")

```

注意：

1. 只能指定一个行业代码查询成分股。

### StkGetSymbolIndustry - 查询股票的所属行业

查询指定股票所属的行业

函数原型：

```
public static GMDataList<StkSymbolIndustry> StkGetSymbolIndustry(string symbols, string source = null, int level = 0, string date = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbols | string | 股票代码 | Y | 无 | 多个代码可用 ，多个标的代码必须用英文逗号分割如："SHSE.600008,SZSE.000002" |
| source | string | 行业来源 | N | null | 'zjh2012'- 证监会行业分类 2012（默认）， 'sw2021'- 申万行业分类 2021) |
| level | int | 行业分级 | N | 0 | 1 - 一级行业（默认），2 - 二级行业，3 - 三级行业 |
| date | string | 查询日期 | N | null | 查询行业分类的指定日期，%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`StkSymbolIndustry` 结构列表，参见`StkSymbolIndustry`定义与`GMDataList`类的用法。

示例：

```
StkGetSymbolIndustry("SHSE.600000, SZSE.000002", "zjh2012", 1)

```

注意：

1. 证监会行业分类 2012 没有三级行业，若输入`source='zjh2012', level=3`则参数无效，返回空

### StkGetSectorCategory - 查询板块分类

查询指定类型的板块列表

函数原型：

```
public static GMDataList<StkSectorCategory> StkGetSectorCategory(string sectorType);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| sectorType | string | 板块类型 | Y | 无 | 只能选择一种类型，可选择 1001:市场类 1002:地域类 1003:概念类 |

返回值：

`StkSectorCategory` 结构列表，参见`StkSectorCategory`定义与`GMDataList`类的用法。

示例：

```
StkGetSectorCategory("1003")

```

### StkGetSectorConstituents - 查询板块成分股

查询指定某个板块的成分股

函数原型：

```
public static GMDataList<StkSectorConstituent> StkGetSectorConstituents(string sectorCode);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| sectorCode | string | 板块代码 | Y | 无 | 需要查询成分股的板块代码，可通过StkGetSectorCategory获取 |

返回值：

`StkSectorConstituent` 结构列表，参见`StkSectorConstituent`定义与`GMDataList`类的用法。

示例：

```
StkGetSectorConstituents("007089")

```

注意：

1. 只能指定一个板块代码查询成分股。

### StkGetSymbolSector - 查询股票的所属板块

查询指定股票所属的板块

函数原型：

```
public static GMDataList<StkSymbolSector> StkGetSymbolSector(string symbols, string sectorType);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbols | string | 股票代码 | Y | 无 | 多个代码可用, 多个标的代码必须用英文逗号分割如："SHSE.600008,SZSE.000002" |
| sectorType | string | 板块类型 | Y | 无 | 只能选择一种类型，可选择 1001:市场类 1002:地域类 1003:概念类 |

返回值：

`StkSectorConstituent` 结构列表，参见`StkSectorConstituent`定义与`GMDataList`类的用法。

示例：

```
StkGetSymbolSector("SHSE.600008,SZSE.000002", "1002")

```

### StkGetDividend - 查询股票分红送股信息

查询指定股票在一段时间内的分红送股信息

函数原型：

```
public static GMDataList<StockDividend> StkGetDividend(string symbol, string startDate, string endDate);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 标的代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | Y | 无 | 必填，开始时间日期（除权除息日），%Y-%m-%d 格式 |
| endDate | string | 结束时间 | Y | 无 | 必填，结束时间日期（除权除息日），%Y-%m-%d 格式 |

返回值：

`StockDividend` 结构列表，参见`StockDividend`定义与`GMDataList`类的用法。

示例：

```
StkGetDividend("SHSE.600000", "2022-07-01", "2022-07-31")

```

注意：

1. 当`startDate`小于或等于`endDate` 时取指定时间段的数据,当`startDate`>`endDate`时返回报错.

### StkGetRation - 查询股票配股信息

查询指定股票在一段时间内的配股信息

函数原型：

```
public static GMDataList<StkRation> StkGetRation(string symbol, string startDate = null, string endDate = null);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 标的代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | Y | 无 | 必填, 开始时间日期（除权除息日），%Y-%m-%d 格式 |
| endDate | string | 结束时间 | Y | 无 | 必填, 结束时间日期（除权除息日），%Y-%m-%d 格式 |

返回值：

`StkRation` 结构列表，参见`StkRation`定义与`GMDataList`类的用法。

示例：

```
StkGetRation("SZSE.000728", "2005-01-01", "2022-09-30")

```

注意：

1. 当`startDate` 小于或等于 `endDate` 时取指定时间段的数据,当`startDate` > `endDate`时返回报错.

### StkGetAdjFactor - 查询股票的复权因子

查询某只股票在一段时间内的复权因子

函数原型：

```
public static GMDataList<StkAdjFactor> StkGetAdjFactor(string symbol, string startDate = null, string endDate = null, string baseDate = null);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 标的代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | N | null | 开始时间交易日期，%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间交易日期，%Y-%m-%d 格式，默认null表示最新时间 |
| baseDate | string | 复权基准日 | N | null | 前复权的基准日，%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`StkAdjFactor` 结构列表，参见`StkAdjFactor`定义与`GMDataList`类的用法。

示例：

```
StkGetAdjFactor("SZSE.000651", "2015-01-01", "2022-09-01")

```

注意：

1. 

T+1 日复权因子会二次更新，分别约在 T 日 19:00 和 T+1 日 19:00 更新

2. 

复权价格计算：
`T日后复权价格 = T日不复权价格 * T日累计后复权因子`
`T日前复权价格 = T日不复权价格 * T日前复权因子`

3. 

上市首日后复权因子和累计后复权因子为 1，最近一次除权除息日后的前复权因子为 1

4. 

前复权基准日`baseDate` 应不早于设定的结束日期`endDate`，不晚于最新交易日。若设定的基准日早于`endDate`则等同于`endDate`，若设定的基准日晚于最新交易日则等同于最新交易日。

5. 

当`startDate`小于或等于 `endDate` 时取指定时间段的数据,当`startDate` > `endDate`时返回报错.

### StkGetShareholderNum - 查询股东户数

查询上市公司股东总数，A 股股东、B 股股东、H 股股东总数

函数原型：

```
public static GMDataList<StkShareholderNum> StkGetShareholderNum(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 股票代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日期），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日期），%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`StkShareholderNum` 结构列表，参见`StkShareholderNum`定义与`GMDataList`类的用法。

示例：

```
StkGetShareholderNum("SZSE.002594", "2022-01-01", "2022-08-01")

```

注意：

当`startDate == endDate`时，取离`endDate`最近公告日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### StkGetTopShareholder - 查询十大股东

查询上市公司前十大股东的持股情况，包括持股数量，所持股份性质等

函数原型：

```
public static GMDataList<StkShareholder> StkGetTopShareholder(string symbol, string startDate = null, string endDate = null, bool tradableHolder = false);

```

参数：

``

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 股票代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | N | null | 开始时间日期（公告日期），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（公告日期），%Y-%m-%d 格式，默认null表示最新时间 |
| tradableHolder | bool | 是否流通股东 | N | false | false-十大股东（默认）、true-十大流通股东 默认false表示十大股东 |

返回值：

`StkShareholder` 结构列表，参见`StkShareholder`定义与`GMDataList`类的用法。

示例：

```
StkGetTopShareholder("SHSE.603906", "2022-06-01", "2022-08-01")

```

注意：

当`startDate == endDate`时，取离`endDate`最近公告日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

### StkGetShareChange - 查询股本变动

查询上市公司的一段时间内公告的股本变动情况

函数原型：

```
public static GMDataList<StkShareChange> StkGetShareChange(string symbol, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 股票代码 | Y | 无 | 必填，只能填一个股票标的 |
| startDate | string | 开始时间 | N | null | 开始时间日期（发布日期），%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期（发布日期），%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`StkShareChange` 结构列表，参见`StkShareChange`定义与`GMDataList`类的用法。

示例：

```
StkGetShareChange("SHSE.605090", "2020-01-01", "2022-10-01")

```

注意：

当`startDate == endDate`时，取离`endDate`最近发布日期的一条数据，
当`startDat < endDate`时，取指定时间段的数据，
当`startDate > endDate`时，返回报错。

---
     ** ** ** ** ** **
