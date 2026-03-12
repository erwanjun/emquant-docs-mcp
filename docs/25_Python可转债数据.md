## 可转债增值数据函数（付费）

注意：vip特色数据权益，可前往 [权益中心](https://emt.18.cn/apply/jj-data-apply) 开通
 
### bnd_get_conversion_price - 查询可转债转股价变动信息

查询可转债一段时间的转股价变动和转股结果

**函数原型：**

```
bnd_get_conversion_price(symbol, start_date="", end_date="")

```

**参数：**

（参见 代码标识）


| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | str | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的symbol |
| start_date | str | 开始时间 | N | "" | 开始时间日期（转股价格生效日），%Y-%m-%d 格式， 默认""表示最新时间 |
| end_date | str | 结束时间 | N | "" | 结束时间日期（转股价格生效日），%Y-%m-%d 格式， 默认""表示最新时间 |

**返回值：**`dataframe`

| 字段名 | 类型 | 中文名称 | 说明 |
| --- | --- | --- | --- |
| pub_date | str | 公告日期 | %Y-%m-%d 格式 |
| effective_date | str | 转股价格生效日期 | %Y-%m-%d 格式 |
| execution_date | str | 执行日期 | %Y-%m-%d 格式 |
| conversion_price | float | 转股价格 | 单位：元 |
| conversion_rate | float | 转股比例 | 单位：% |
| conversion_volume | float | 本期转股数 | 单位：股 |
| conversion_amount_total | float | 累计转股金额 | 单位：万元，累计转债已经转为股票的金额，累计每次转股金额 |
| bond_float_amount_remain | float | 债券流通余额 | 单位：万元 |
| event_type | str | 事件类型 | 初始转股价，调整转股价，修正转股价 |
| change_reason | str | 转股价变动原因 | 发行，股权激励，股权分置，触发修正条款，其它变动原因，换股吸收合并， 配股，增发，上市，派息，送股，转增股，修正 |

**示例：**

```
bnd_get_conversion_price(symbol='SZSE.123015')

```

**输出：**

```
pub_date effective_date execution_date  conversion_price  conversion_rate  conversion_volume  conversion_amount_total  bond_float_amount_remain event_type change_reason
0  2022-07-29     2022-08-01     2022-08-01              2.38          42.0168                0.0                      0.0                       0.0      修正转股价     修正,触发修正条款

```

**注意：**

**1.** 本期转股数、累计转股金额、债券流通余额在执行日期收盘后才有数据。

**2.** 当`start_date == end_date`时，取离`end_date`最近转股价格生效日期的一条数据，
当`start_date < end_date`时，取指定时间段的数据，
当`start_date > end_date`时，返回报错。

### bnd_get_call_info - 查询可转债赎回信息

查询可转债一段时间内的赎回情况

**函数原型：**

```
bnd_get_call_info(symbol, start_date="", end_date="")

```

**参数：**

（参见 代码标识）


| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | str | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的symbol |
| start_date | str | 开始时间 | N | "" | 开始时间日期（公告日），%Y-%m-%d 格式， 默认""表示最新时间 |
| end_date | str | 结束时间 | N | "" | 结束时间日期（公告日），%Y-%m-%d 格式， 默认""表示最新时间 |

**返回值：**`dataframe`

| 字段名 | 类型 | 中文名称 | 说明 |
| --- | --- | --- | --- |
| pub_date | str | 公告日 | 赎回公告日，%Y-%m-%d 格式 |
| call_date | str | 赎回日 | 发行人行权日（实际），%Y-%m-%d 格式 |
| record_date | str | 赎回登记日 | 理论登记日，%Y-%m-%d 格式 |
| cash_date | str | 赎回资金到账日 | 投资者赎回款到账日 |
| call_type | str | 赎回类型 | 部分赎回，全部赎回 |
| call_reason | str | 赎回原因 | 满足赎回条件，强制赎回，到期赎回 |
| call_price | float | 赎回价格 | 单位：元/张，每百元面值赎回价格，即债券面值加当期应计利息（含税） |
| interest_included | bool | 是否包含利息 | False-不包含，True-包含 |

**示例：**

```
bnd_get_call_info(symbol='SHSE.110041')

```

**输出：**

```
     pub_date   call_date record_date cash_date call_type call_reason  call_price  interest_included
0  2021-10-18  2021-11-05  2021-11-04      None      全部赎回        强制赎回     101.307               True

```

**注意：**

当`start_date == end_date`时，取离`end_date`最近公告日的一条数据，
当`start_date < end_date`时，取指定时间段的数据，
当`start_date > end_date`时，返回报错。

### bnd_get_put_info - 查询可转债回售信息

查询可转债一段时间内的回售情况

**函数原型：**

```
bnd_get_put_info(symbol, start_date="", end_date="")

```

**参数：**

（参见 代码标识）


| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | str | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的symbol |
| start_date | str | 开始时间 | N | "" | 开始时间日期（公告日），%Y-%m-%d 格式， 默认""表示最新时间 |
| end_date | str | 结束时间 | N | "" | 结束时间日期（公告日），%Y-%m-%d 格式， 默认""表示最新时间 |

**返回值：**`dataframe`

| 字段名 | 类型 | 中文名称 | 说明 |
| --- | --- | --- | --- |
| pub_date | str | 公告日 | 回售公告日，%Y-%m-%d 格式 |
| put_start_date | str | 赎回日 | 投资者行权起始日，%Y-%m-%d 格式 |
| put_end_date | str | 赎回登记日 | 投资者行权截止日，%Y-%m-%d 格式 |
| cash_date | str | 赎回资金到账日 | 投资者回售款到账日 |
| put_reason | str | 回售原因 | 满足回售条款，满足附加回售条款 |
| put_price | float | 回售价格 | 单位：元/张，每百元面值回售价格（元），即债券面值加当期应计利息（含税） |
| interest_included | bool | 是否包含利息 | False-不包含，True-包含 |

**示例：**

```
bnd_get_put_info(symbol='SZSE.128015')

```

**输出：**

```
     pub_date put_start_date put_end_date   cash_date put_reason  put_price  interest_included
0  2022-06-09     2022-06-16   2022-06-22  2022-06-29     满足回售条款    100.039               True

```

**注意：**

当`start_date == end_date`时，取离`end_date`最近公告日的一条数据，
当`start_date < end_date`时，取指定时间段的数据，
当`start_date > end_date`时，返回报错。

### bnd_get_amount_change` - 查询可转债剩余规模变动

查询可转债转股、回售、赎回等事件导致的剩余规模变动的情况

**函数原型：**

```
bnd_get_amount_change(symbol, start_date="", end_date="")

```

**参数：**

（参见 代码标识）


| 参数名 | 类型 | 中文名称 | 必填 | 默认值 | 参数用法说明 |
| --- | --- | --- | --- | --- | --- |
| symbol | str | 可转债代码 | Y | 无 | 必填，只能输入一个可转债的symbol |
| start_date | str | 开始时间 | N | "" | 开始时间日期（变动日期），%Y-%m-%d 格式， 默认""表示最新时间 |
| end_date | str | 结束时间 | N | "" | 结束时间日期（变动日期），%Y-%m-%d 格式， 默认""表示最新时间 |

**返回值：**`dataframe`

| 字段名 | 类型 | 中文名称 | 说明 |
| --- | --- | --- | --- |
| pub_date | str | 公告日 | %Y-%m-%d 格式 |
| change_date | str | 变动日期 | %Y-%m-%d 格式 |
| change_type | str | 变动类型 | 首发，增发，转股，赎回，回售(注销)，到期 |
| change_amount | float | 本次变动金额 | 单位：万元 |
| remain_amount | float | 剩余金额 | 变动后金额，单位：万元 |

**示例：**

```
bnd_get_amount_change(symbol='SZSE.123015')

```

**输出：**

```
     pub_date change_type change_date  change_amount  remain_amount
0  2022-10-10          转股  2022-09-30           8.91       10004.18

```

**注意：**

**1.** 变动类型指定为首发时，返回的剩余金额为发行金额。

**2.** 当`start_date == end_date`时，取离`end_date`最近变动日期的一条数据，
当`start_date < end_date`时，取指定时间段的数据，
当`start_date > end_date`时，返回报错。

     [ ** ](python_select_api_fund_vip.html#fndgetsplit---查询基金拆分折算信息) [ ** ](python_select_api_bond_vip.html#bndgetconversionprice---查询可转债转股价变动信息)
