## 通用数据函数（免费）

### SetToken - 设置token

**函数原型**

```
static int SetToken(string token);

```

**参数**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| token | string | 改参数通过 客户端->系统设置->(秘钥管理)token 获得 |
| 返回值 | int | 0 成功， 其他表示错误码 |

**示例**

```
GMApi.SetToken("27cbdfd8cd9b86dea554a5612baa4a8eee");

```

### SetAddr - 设置终端服务地址

设置终端服务地址, 默认本地地址, 可不填

**函数原型：**

```
void SetAddr(string addr)

```

**参数:**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| addr | string | ip+终端端口，如”127.0.0.1:7001” |

**注意：**
**1.**如运行策略与终端不在同一设备上，必须调用此方法，`7001`为终端端口
**2.**不关注策略运行结果，可不启动终端并设置终端服务地址为 `discovery.myquant.cn:7061`

### GetSymbolInfos - 查询标的基本信息

获取指定(范围)交易标的基本信息，与时间无关.

函数原型：

```
public static GMDataList<SymbolInfo> GetSymbolInfos(int secType1, int secType2 = 0, string exchanges = null, string symbols = null)

```

参数：

``

````

````

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| secType1 | int | 证券品种大类 | Y | 无 | 指定一种证券大类，只能输入一个. 证券大类 secType1 清单 1010: 股票， 1020: 基金， 1030: 债券 ， 1040: 期货， 1050: 期权， 1060: 指数，1070：板块. |
| secType2 | int | 证券品种细类 | N | 0 | 指定一种证券细类，只能输入一个. 默认0表示不区分细类，即证券大类下所有细类. 证券细类见 secType2 清单 - 股票 101001:A 股，101002:B 股，101003:存托凭证 - 基金 102001:ETF，102002:LOF，102005:FOF - 债券 103001:可转债，103008:回购 - 期货 104001:股指期货，104003:商品期货，104006:国债期货 - 期权 105001:股票期权，105002:指数期权，105003:商品期权 - 指数 106001:股票指数，106002:基金指数，106003:债券指数，106004:期货指数 - 板块：107001:概念板块 |
| exchanges | string | 交易所代码 | N | null | 输入交易所代码，可输入多个. 采用 string 格式时，多个交易所代码必须用英文逗号分割，如："SHSE,SZSE" 默认null表示所有交易所. 交易所代码清单 SHSE:上海证券交易所，SZSE:深圳证券交易所 ， CFFEX:中金所，SHFE:上期所，DCE:大商所， CZCE:郑商所， INE:上海国际能源交易中心 ，GFEX:广期所 |
| symbols | string | 标的代码 | N | null | 输入标的代码，可输入多个. 采用 string 格式时，多个标的代码必须用英文逗号分割，如："SHSE.600008,SZSE.000002" 默认null表示所有标的. |

返回值：

`SymbolInfo` 结构列表，参见`SymbolInfo`定义与`GMDataList`类的用法。

示例：

```
GetSymbolInfos(1010, 0, null, "SHSE.600008,SZSE.000002")

```

注意：

1. 

`secType1`为必填参数，即一次只能查询一个品种的标的基本信息。

2. 

查询的标的信息根据参列表合`secType1, secType2, exchanges, symbols`取交集，若输入参数之间出现任何矛盾（换句话说，所有的参数限制出满足要求的交集为空)，则返回`空`

3. 

若输入包含无效标的代码`symbols`，则返回只包含有效标的代码对应的数据。

4. 

参列表合示例：

| 查询以下范围 symbol 的基本信息 | secType1 | secType2 | exchanges | symbols |
| --- | --- | --- | --- | --- |
| 查询指定股票 | 1010 | 0 | null | 'SHSE.600008,SZSE.000002' |
| 查询 A 股股票 | 1010 | 101001 | null | null |
| 查询深交所股票 | 1010 | 0 | 'SZSE' | null |
| 查询 ETF | 1020 | 102001 | null | null |
| 查询上交所 LOF | 1020 | 102002 | 'SHSE' | null |
| 查询可转债 | 1030 | 103001 | null | null |
| 查询深交所可转债 | 1030 | 103001 | 'SZSE' | null |
| 查询股指期货 | 1040 | 104001 | null | null |
| 查询商品期货 | 1040 | 104003 | null | null |
| 查询郑商所和大商所期货 | 1040 | 0 | 'CZCE,DCE' | null |
| 查询股票期权 | 1050 | 105001 | null | null |
| 查询上交所股票期权 | 1050 | 105001 | 'SHSE' | null |
| 查询指数期权 | 1050 | 105002 | null | null |
| 查询商品期权 | 1050 | 105003 | null | null |
| 查询上期所商品期权 | 105003 | 0 | 'SHFE' | null |
| 查询股票指数 | 1060 | 106001 | null | null |

### GetSymbols - 查询指定交易日多标的交易信息

获取指定交易日多个标的交易信息，包括基本信息及日度数据.

函数原型：

```
public static GMDataList<SymbolContent> GetSymbols(int secType1, int secType2 = 0, string exchanges = null, string symbols = null, bool skipSuspended = true, bool skipSt = true, string tradeDate = null);

```

参数：

``

````

````

``

````

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| secType1 | int | 证券品种大类 | Y | 无 | 指定一种证券大类，只能输入一个. 证券大类 secType1 清单 1010: 股票， 1020: 基金， 1030: 债券 ， 1040: 期货， 1050: 期权， 1060: 指数，1070：板块. |
| secType2 | int | 证券品种细类 | N | 0 | 指定一种证券细类，只能输入一个. 默认0表示不区分细类，即证券大类下所有细类. 证券细类见 secType2 清单 - 股票 101001:A 股，101002:B 股，101003:存托凭证 - 基金 102001:ETF，102002:LOF，102005:FOF - 债券 103001:可转债，103008:回购 - 期货 104001:股指期货，104003:商品期货，104006:国债期货 - 期权 105001:股票期权，105002:指数期权，105003:商品期权 - 指数 106001:股票指数，106002:基金指数，106003:债券指数，106004:期货指数 - 板块：107001:概念板块 |
| exchanges | string | 交易所代码 | N | null | 输入交易所代码，可输入多个. 采用 string 格式时，多个交易所代码必须用英文逗号分割，如："SHSE,SZSE"  默认null表示所有交易所. 交易所代码清单 SHSE:上海证券交易所，SZSE:深圳证券交易所 ， CFFEX:中金所，SHFE:上期所，DCE:大商所， CZCE:郑商所， INE:上海国际能源交易中心 ，GFEX:广期所 |
| symbols | string | 标的代码 | N | null | 输入标的代码，可输入多个. 采用 string 格式时，多个标的代码必须用英文逗号分割，如："SHSE.600008,SZSE.000002"  默认null表示所有标的. |
| skipSuspended | bool | 跳过停牌 | N | true | 是否跳过全天停牌，默认true跳过 |
| skipSt | bool | 跳过 ST | N | true | 是否跳过包含 ST 的股票：ST, ST, SST, SST, 默认true跳过 |
| tradeDate | string | 交易日期 | N | null | 交易日期，%Y-%m-%d 格式，默认null取最新截面(包含退市标的) |

返回值：

`SymbolContent` 结构列表，参见`SymbolContent`定义与`GMDataList`类的用法。

示例：

```
GetSymbols(secType1=1010, 0, null, "SHSE.600008,SZSE.000002")

```

注意：

1. 

`secType1`为必填参数，即一次只能查询一个品种的标的最新交易日信息。

2. 

查询的标的信息根据参列表合`secType1, secType2, exchanges, symbols`取交集，若输入参数之间出现任何矛盾（换句话说，所有的参数限制出满足要求的交集为空)，则返回`空`

3. 

若输入包含无效标的代码`symbols`，则返回只包含有效标的代码对应的数据。

4. 

获取全 A 股票代码示例`GetSymbols(1010, 101001)`

5. 

可转债的到期日(退市日期)为`delistedDate`，转股价值为`转股价值 = 转股数股价 = (100/可转债转股价)  股价`

### GetHistorySymbol - 查询指定标的多日交易信息

获取指定标的多个历史交易日的交易信息，包括基本信息及日度数据.

函数原型：

```
public static GMDataList<SymbolContent> GetHistorySymbol(string symbol, string startDate, string endDate);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | string | 标的代码 | Y | 无 | 输入标的代码，只能输入一个. |
| startDate | string | 开始时间 | Y | null | 开始时间日期，%Y-%m-%d 格式. |
| endDate | string | 结束时间 | Y | null | 结束时间日期，%Y-%m-%d 格式. |

返回值：

`SymbolContent` 结构列表，参见`SymbolContent`定义与`GMDataList`类的用法。

示例：

```
GetHistorySymbol("SZSE.000002", "2022-09-01", "2022-09-30")

```

注意：

1. 

若输入包含无效标的代码`symbol`，则返回只包含有效标的代码对应的数据。

2. 

停牌时且股票发生除权除息，涨停价和跌停价可能有误差。

3. 

对每个标的，数据根据`tradeDate`的升序进行排序。

4. 

`startDate`和`endDate`，例:`'2010-7-8'或'2017-7-30'`

5. 

当`startDate`大于或者等于 `endDate` 时, 取指定时间段的数据,当 `startDate` > `endDate`时, 返回报错

6. 

可转债的到期日(退市日期)`delistedDate`，转股价值为`转股价值 = 转股数股价 = (100/可转债转股价)  股价`

### GetTradingDatesByYear - 查询年度交易日历

查询一个交易所的指定年份的交易日历.

函数原型：

```
public static GMDataList<TradingDateContent> GetTradingDatesByYear(string exchange, int startYear, int endYear);

```

参数：

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| exchange | string | 交易所代码 | Y | 无 | 只能填写一个交易所代码 交易所代码清单: SHSE:上海证券交易所，SZSE:深圳证券交易所，CFFEX:中金所，SHFE:上期所，DCE:大商所，CZCE:郑商所，INE:上海国际能源交易中心，GFEX:广期所 |
| startYear | int | 开始年份 | Y | 无 | 查询交易日历开始年份（含），yyyy 格式 |
| endYear | int | 结束年份 | Y | 无 | 查询交易日历结束年份（含），yyyy 格式 |

返回值:

`TradingDateContent` 结构列表，参见`TradingDateContent`定义与`GMDataList`类的用法。

示例：

```
GetTradingDatesByYear("SHSE", 2020, 2023)

```

注意：

1. 

`exchange`参数仅支持输入单个交易所代码，若代码错误，会报错

2. 

开始年份必须不晚于结束年份，否则返回`空`

### GetTradingSession - 查询交易时段

查询一个标的所属品种交易时间段.

函数原型：

```
public static GMDataList<TradingSession> GetTradingSession(string symbols);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbols | string | 标的代码 | Y | 无 | 输入标的代码，可输入多个. 多个标的代码必须用英文逗号分割，如："SHSE.600008,SZSE.000002" |

返回值：

`TradingSession` 结构列表，参见`TradingSession`定义与`GMDataList`类的用法。

示例：

```
GetTradingSession("SHFE.au2306")

```

注意：

1. 如果输入不存在的合约代码 symbol，会报错提示"该合约[symbol]不存在"。

### GetContractExpireRestDays - 查询合约到期剩余天数

查询期货合约、期权合约、可转债的到期剩余天数。

函数原型：

```
public static GMDataList<ContractExpireRestDays> GetContractExpireRestDays(string symbols, string startDate, string endDate, bool tradeFlag = false);

```

参数：

``

````

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbols | string | 标的代码 | Y | 无 | 输入标的代码，可输入多个. 多个标的代码必须用英文逗号分割，如："CFFEX.IF2212,CFFEX.IC2212" |
| startDate | string | 开始日期 | Y | 无 | %Y-%m-%d 格式，不早于合约上市日 |
| endDate | string | 结束日期 | Y | 无 | %Y-%m-%d 格式，不早于指定的开始日期，否则返回报错 |
| tradeFlag | bool | 交易日 | N | false | 是否需要按交易日计算，默认false按自然日计算，则返回到期剩余自然日天数; 设置为true按交易日计算，则返回到期剩余交易日天数 |

返回值：

`ContractExpireRestDays` 结构列表，参见`ContractExpireRestDays`定义与`GMDataList`类的用法。

示例：

```
GetContractExpireRestDays("CFFEX.IM2212", "2022-12-12", "2022-12-16", true)

```

注意：

1. 

参数`startDate`和`endDate`必须是yyyy-mm-dd字符串格式

2. 

在到期日当天，到期剩余天数为 0。正数表示距离到期日的剩余天数，0 表示到期日当天，负数表示距离到期日已经过去的天数。

3. 

如果输入不存在的合约代码`symbol`，会报错提示"该合约[symbol]不存在"。

4. 

如果输入的合约代码`symbol`在时间段内的某个日期未上市，在该日期的到期剩余天数返回空。

5. 

用于剩余天数计算的到期日是最后交易日。

---
     ** ** ** ** ** **
