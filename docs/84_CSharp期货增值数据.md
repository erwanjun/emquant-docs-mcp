## 期货增值数据函数（付费）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 
### FutGetContractInfo - 查询期货标准品种信息

查询交易所披露的期货标准品种的合约规格/合约文本

函数原型：

```
public static GMDataList<FutContractInfo> FutGetContractInfo(string productCodes);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| productCodes | string | 品种代码 | Y | 无 | 必填，交易品种代码，如：IF，AL 多个代码可用 ，多个标的代码必须用英文逗号分割，如：IF, AL |

返回值：

`FutContractInfo` 结构列表，参见`FutContractInfo`定义与`GMDataList`类的用法。

示例：

```
FutGetContractInfo("IF")

```

### FutGetTransactionRankings - 查询期货每日成交持仓排名

查询期货合约每日成交量/持买单量/持卖单量排名

函数原型：

```
public static GMDataList<FutTransactionRanking> FutGetTransactionRankings(string symbols, string tradeDate = null, string indicator = null);

```

参数：

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbols | string | 期货合约代码 | Y | 无 | 必填，期货真实合约代码 |
| tradeDate | string | 交易日期 | N | null | 交易日期，%Y-%m-%d 格式，默认null表示最新交易日 |
| indicators | string | 排名指标 | N | null | 排名指标，即用于排名的依据，可选：'volume'-成交量排名（默认）, 'long'-持买单量排名, 'short'-持卖单量排名, 支持一次查询多个排名指标，如有多个指标，中间用英文逗号分隔, 默认None表示成交量排名 |

返回值：

`FutTransactionRanking` 结构列表，参见`FutTransactionRanking`定义与`GMDataList`类的用法。

示例：

```
FutGetTransactionRankings("SHFE.ag2212", "2022-10-10", "volume")

```

注意：

1. 

当上一交易日没有进入前 20 名，`rankingChange`返回 0.

2. 

数据日频更新，当日更新前返回前一交易日的排名数据，约在交易日 20 点左右更新当日数据。

### FutGetWarehouseReceipt - 查询期货仓单数据

查询交易所在交易日期货品种的注册仓单数量、有效预报

- 期货仓单是指由期货交易所指定交割仓库，按照期货交易所指定的程序，签发的符合合约规定质量的实物提货凭证。记录了交易所所有期货实物的库存情况以及变更情况。

函数原型：

```
public static GMDataList<FutWarehouseReceiptInfo> FutGetWarehouseReceipt(string productCode, string startDate = null, string endDate = null);

```

参数：

``

``

| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| productCode | string | 品种代码 | Y | 无 | 必填，只能填写一个交易品种代码，如：AL |
| startDate | string | 开始时间 | N | null | 开始时间日期，%Y-%m-%d 格式，默认null表示最新时间 |
| endDate | string | 结束时间 | N | null | 结束时间日期，%Y-%m-%d 格式，默认null表示最新时间 |

返回值：

`FutWarehouseReceiptInfo` 结构列表，参见`FutWarehouseReceiptInfo`定义与`GMDataList`类的用法。

示例：

```
FutGetWarehouseReceipt("AL", "2023-06-20", "2023-06-29")

```

注意：

1. 

支持郑商所、大商所、上期所和上海国际能源交易中心的期货品种。

2. 

注册仓单数量每日更新，其余数据上期所一周一披露，郑商所一天一披露。

3. 

当`startDate` 小于或等于 `endDate` 时, 取指定时间段的数据,当 `startDate` > `endDate` 时, 返回报错。

---
     ** ** ** ** ** **
