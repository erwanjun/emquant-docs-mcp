## 两融交易函数

python两融SDK包含在gm3.0.126版本及以上版本，不需要引入新库

### credit_buying_on_margin -  融资买入

**函数原型：**

```
credit_buying_on_margin(position_src, symbol, volume, price, order_type=OrderType_Limit, order_duration=OrderDuration_Unknown,
                            order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 头寸来源仅适用融券融券）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| position_src | int | 头寸来源 取值参考 PositionSrc |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_buying_on_margin(position_src=PositionSrc_L1, symbol='SHSE.600000', volume=100, price=10.67)

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b853062-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 863549, tzinfo=tzfile('PRC')) 200                                                          0    0               0              0             0               0         0                                    0          0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_short_selling - 融券卖出

**函数原型**

```
credit_short_selling(position_src, symbol, volume, price, order_type=OrderType_Limit, order_duration=OrderDuration_Unknown,
                         order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 头寸来源仅适用融券融券）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| position_src | int | 头寸来源 取值参考 PositionSrc |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_short_selling(position_src=PositionSrc_L1, symbol='SHSE.600000', volume=100, price=10.67, order_type=OrderType_Limit,
                               order_duration=OrderDuration_Unknown,
                               order_qualifier=OrderQualifier_Unknown, account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b853062-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 863549, tzinfo=tzfile('PRC')) 201                                                          0    0               0              0             0               0         0                                    0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_repay_cash_directly -  直接还款

**函数原型：**

```
credit_repay_cash_directly(amount, account_id='', sno='', bond_fee_only=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| amount | float | 还款金额 |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |
| sno | str | 合约编号 |
| bond_fee_only | bool | 是否仅偿还利息 |

**返回值：`dict`
**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| actual_repay_amount | float | 实际还款金额 |
| account_id | str | 账号id |
| account_name | str | 账户名称 |

**示例代码：**

```
credit_repay_cash_directly(amount=10000.00, account_id='')

```

**示例返回值：**

```
actual_repay_amount account_id                           account_name
------------------- ------------------------------------ ------------
10000.0             8f30e83f-a7c5-11ea-b510-309c231d28bd 001515018318

```

### credit_repay_share_directly - 直接还券

**函数原型**

```
credit_repay_share_directly(symbol, volume, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：`[dict]`**

请参考 [order](python_object_trade.html#order---委托对象) 返回值字段说明

**示例代码**

```
credit_repay_share_directly(symbol='SHSE.600000', volume=100, account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail price stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at 
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ----- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b86685e-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     100    datetime.datetime(2020, 6, 6, 15, 41, 44, 871536, tzinfo=tzfile('PRC')) 204                                                          0    0               0             0              0               0         0                                    0.0   0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None   
........ ......

```

### credit_get_collateral_instruments -  查询担保证券

查询担保证券，可做担保品股票列表

**函数原型：**

```
credit_get_collateral_instruments(account_id='', df=False)

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |
| df | bool | 是否返回dataframe格式数据。默认 False, 返回list[dict] |

**返回值：**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的 |
| pledge_rate | float | 折算率 |

**示例代码**

```
credit_get_collateral_instruments(account_id='', df=False)

```

**示例返回值**

```
symbol      pledge_rate
----------- -----------
SHSE.010107  0.9
SHSE.010303  0.9
..........   ...

```

### credit_get_borrowable_instruments -  查询可融标的证券

查询标的证券，可做融券标的股票列表

**函数原型：**

```
credit_get_borrowable_instruments(position_src, account_id='', df=False)

```

**参数：**

（参见 头寸来源仅适用融券融券）

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| position_src | int | 头寸来源 取值参考 PositionSrc |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |
| df | bool | 是否返回dataframe格式数据。默认 False, 返回list[dict] |

**返回值：`list[dict]`**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的 |
| margin_rate_for_cash | float | 融资保证金比率 |
| margin_rate_for_security | float | 融券保证金比率 |

**示例代码**

```
credit_get_borrowable_instruments(position_src=PositionSrc_L1, account_id='', df=False)

```

**示例返回值**

```
symbol      margin_rate_for_cash margin_rate_for_security
----------- -------------------- ------------------------
SHSE.510050  1.0                  0.6
SHSE.510160  1.0                  0.6
...........  ...                  ...

```

### credit_get_borrowable_instruments_positions -  查询券商融券账户头寸

查询券商融券账户头寸，可用融券的数量

**函数原型：**

```
credit_get_borrowable_instruments_positions(position_src, account_id='', df=False)

```

**参数：**

（参见 头寸来源仅适用融券融券）

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| position_src | int | 头寸来源 取值参考 PositionSrc |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |
| df | bool | 是否返回dataframe格式数据。默认 False, 返回list[dict] |

**返回值：**
当df = True时， 返回`dataframe`
当df = False时， 返回`list[dict]`

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的 |
| balance | float | 证券余额 |
| available | float | 证券可用金额 |

**示例代码**

```
credit_get_borrowable_instruments_positions(position_src=PositionSrc_L1, account_id='', df=False)

```

**示例返回值**

```
symbol      balance available
----------- ------- -----------
SHSE.600166  700.0   700.0
SHSE.688002  2000.0  2000.0
..........   ......  ......

```

### credit_get_contracts -  查询融资融券合约

东财掘金独立端需要使用功能码查询信用合约

**函数原型：**

```
raw_func(account_id, func_id, func_args)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号id，需要从策略设置里获取 |
| func_id | str | 功能码 |
| func_args | dict | 功能码参数，参考示例 |

**返回值：`dict`**

查询融资负债返回字段 func_args={"creditDirect": "1"}

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| market | str | 交易市场（"1"表示上海市场"SHSE", "0"表示深圳市场"SZSE"） |
| stockCode | str | 证券代码 |
| stockName | str | 证券名称 |
| clearAmount | float | 融资金额 |
| remainPrincipal | float | 未偿还本金金额 |
| overdueFee | float | 未还息费 |
| creditRepay | float | T日之前归还金额 |
| creditTodayRepay | float | T日归还金额 |
| status | str | 合约状态,"0"表示"未偿还", "1"表示"已偿还", "2"表示"到期未平仓" |
| sno | str | 合约编号 |
| orderDate | str | 开仓日期 |
| endDate | str | 负债截止日期 |

查询融券负债返回字段 func_args={"creditDirect": "2"}

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| market | str | 交易市场（"1"表示上海市场"SHSE", "0"表示深圳市场"SZSE"） |
| stockCode | str | 证券代码 |
| stockName | str | 证券名称 |
| matchQuantity | int | 融券数量 |
| fee | float | 融券息费 |
| stockRemain | int | 未还数量 |
| overdueFee | float | 未还息费 |
| remainRightsQuantity | int | 应付权益补偿数量 |
| remainRightsAmount | float | 应付权益补偿金额 |
| transferRightsQuantity | int | 在途权益补偿数量 |
| transferRightsAmount | float | 在途权益补偿金额 |
| stockRepay | int | T日之前归还数量 |
| stockTodayRepay | int | T日归还数量 |
| status | str | 合约状态,"0"表示"未偿还", "1"表示"已偿还", "2"表示"到期未平仓" |
| sno | str | 合约编号 |
| orderDate | str | 开仓日期 |
| endDate | str | 到期日期 |

**示例代码 1**

```
# 查询融资负债
raw_func(account_id="43850371-65fb-4c44-9061-82b9eb391600", func_id="EM_TRADE_API_REQUEST_QUERY_AGREEMENTS",  func_args={"creditDirect": "1"})

```

**示例返回值**

```
{'data': [{'moneyType': '',
   'stockCode': '000001',
   'stockName': '',
   'orderDate': '20211231',
   'orderNo': '',
   'creditDirect': '0',
   'orderQuantity': 0,
   'matchQuantity': 0,
   'orderAmount': '',
   'orderFreezeAmount': '',
   'matchAmount': '',
   'clearAmount': '',
   'status': '0',
   'endDate': '20220630',
   'creditRepay': '',
   'creditTodayRepay': '',
   'fundRemain': 380000.0,
   'stockRepay': 0,
   'stockTodayRepay': 0,
   'stockRemain': 0,
   'stockRemainValue': '',
   'sno': '679388',
   'fee': 0.0,
   'overdueFee': '',
   'feeRepay': '',
   'punishFee': '',
   'punishFeeRepay': '',
   'rights': '',
   'overdueRights': '',
   'rightsRepay': '',
   'profitCost': '',
   'location': '1',
   'closeDate': '',
   'punishDebts': '',
   'punishDebtsRepay': '',
   'punishDebtsUnfreeze': '',
   'punishFeeUnfreeze': '',
   'punishRights': '',
   'punishRightsRepay': '',
   'punishRightsUnfreeze': '',
   'feeUnfreeze': '',
   'overdueFeeUnfreeze': '',
   'rightsQuantity': 0,
   'positionId': '110110017605',
   'originEndDate': '',
   'isExtended': False,
   'remainPrincipal': 380000.0,
   'transferRightsAmount': 0.0,
   'transferRightsQuantity': 0,
   'market': '0',
   'ChannelType': '3',
   'remainRightsAmount': '',
   'remainRightsQuantity': 0},
  {'moneyType': '',
   'stockCode': '300883',
   'stockName': '',
   'orderDate': '20211231',
   'orderNo': '',
   'creditDirect': '0',
   'orderQuantity': 0,
   'matchQuantity': 0,
   'orderAmount': '',
   'orderFreezeAmount': '',
   'matchAmount': '',
   'clearAmount': '',
   'status': '0',
   'endDate': '20220630',
   'creditRepay': '',
   'creditTodayRepay': '',
   'fundRemain': 73600.0,
   'stockRepay': 0,
   'stockTodayRepay': 0,
   'stockRemain': 0,
   'stockRemainValue': '',
   'sno': '679389',
   'fee': 0.0,
   'overdueFee': '',
   'feeRepay': '',
   'punishFee': '',
   'punishFeeRepay': '',
   'rights': '',
   'overdueRights': '',
   'rightsRepay': '',
   'profitCost': '',
   'location': '2',
   'closeDate': '',
   'punishDebts': '',
   'punishDebtsRepay': '',
   'punishDebtsUnfreeze': '',
   'punishFeeUnfreeze': '',
   'punishRights': '',
   'punishRightsRepay': '',
   'punishRightsUnfreeze': '',
   'feeUnfreeze': '',
   'overdueFeeUnfreeze': '',
   'rightsQuantity': 0,
   'positionId': '110110017605',
   'originEndDate': '',
   'isExtended': False,
   'remainPrincipal': 73600.0,
   'transferRightsAmount': 0.0,
   'transferRightsQuantity': 0,
   'market': '0',
   'ChannelType': '3',
   'remainRightsAmount': '',
   'remainRightsQuantity': 0}]}

```

**示例代码 2**

```
# 查询融券负债
raw_func(account_id="43850371-65fb-4c44-9061-82b9eb391600", func_id="EM_TRADE_API_REQUEST_QUERY_AGREEMENTS",  func_args={"creditDirect": "2"})

```

**示例返回值**

```
{'data': [{'moneyType': '',
   'stockCode': '000001',
   'stockName': '',
   'orderDate': '20211231',
   'orderNo': '',
   'creditDirect': '1',
   'orderQuantity': 0,
   'matchQuantity': 0,
   'orderAmount': '',
   'orderFreezeAmount': '',
   'matchAmount': '',
   'clearAmount': '',
   'status': '0',
   'endDate': '20220630',
   'creditRepay': '',
   'creditTodayRepay': '',
   'fundRemain': 0.0,
   'stockRepay': 0,
   'stockTodayRepay': 0,
   'stockRemain': 20000,
   'stockRemainValue': '',
   'sno': '679391',
   'fee': 0.0,
   'overdueFee': '',
   'feeRepay': '',
   'punishFee': '',
   'punishFeeRepay': '',
   'rights': '',
   'overdueRights': '',
   'rightsRepay': '',
   'profitCost': '',
   'location': '1',
   'closeDate': '',
   'punishDebts': '',
   'punishDebtsRepay': '',
   'punishDebtsUnfreeze': '',
   'punishFeeUnfreeze': '',
   'punishRights': '',
   'punishRightsRepay': '',
   'punishRightsUnfreeze': '',
   'feeUnfreeze': '',
   'overdueFeeUnfreeze': '',
   'rightsQuantity': 0,
   'positionId': '110110017605',
   'originEndDate': '',
   'isExtended': False,
   'remainPrincipal': 0.0,
   'transferRightsAmount': 0.0,
   'transferRightsQuantity': 0,
   'market': '0',
   'ChannelType': '3',
   'remainRightsAmount': '',
   'remainRightsQuantity': 0}]}

```

### credit_get_cash -  查询融资融券资金

东财掘金独立端查询信用资金需要使用功能码查询

**函数原型：**

```
raw_func(account_id, func_id, func_args)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号id，需要从策略设置里获取 |
| func_id | str | 功能码 |
| func_args | dict | 功能码参数，参考示例 |

**返回值：`dict`**

| 字段 | 类型 | 名称 |
| --- | --- | --- |
| stockAsset | float | 总市值 |
| asset | float | 总资产 |
| liability | float | 总负债 |
| marginRates | float | 维持担保比例 |
| dbMarginTradeAmt | float | 融资负债 |
| dbShortSellMktVal | float | 融券负债 |
| fundAvailable | float | 资金可用数 |
| marginAvailable | float | 保证金可用数 |
| stockCreditSellAmount | float | 融券卖出所得资金 |
| fundFreeze | float | 预扣资金 |

**示例代码**

```
cash2 = raw_func(account_id="43850371-65fb-4c44-9061-82b9eb391600", func_id="EM_TRADE_API_REQUEST_QUERY_ASSET", func_args={})

```

**示例返回值**

```
{'data': [{'asset': '0.000000',
   'dbMarginTradeAmt': '11893600',
   'dbShortSellMktVal': '1994400.000',
   'fundAvailable': '1000000000.000000',
   'fundBalance': '0.000000',
   'fundFreeze': '-1219904020.000000',
   'liability': '0.000000',
   'marginAvailable': '0.000000',
   'marginRates': '87.840000',
   'stockAsset': '219904020.000000',
   'stockCreditSellAmount': '0.000000'}]}

```

### credit_repay_share_by_buying_share - 买券还券

**函数原型**

```
credit_repay_share_by_buying_share(symbol, volume, price, order_type=OrderType_Limit,
                                       order_duration=OrderDuration_Unknown,
                                       order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_repay_share_by_buying_share(symbol='SHSE.600000', volume=100, price=10.67, order_type=OrderType_Limit,
                                             order_duration=OrderDuration_Unknown,
                                             order_qualifier=OrderQualifier_Unknown,
                                             account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b857e02-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 865536, tzinfo=tzfile('PRC')) 202                                                          0    0               0             0              0               0         0                                    0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_repay_cash_by_selling_share - 卖券还款

**函数原型**

```
credit_repay_cash_by_selling_share(symbol, volume, price, order_type=OrderType_Limit,
                                       order_duration=OrderDuration_Unknown,
                                       order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_repay_cash_by_selling_share(symbol='SHSE.600000', volume=100, price=10.67, order_type=OrderType_Limit,
                                             order_duration=OrderDuration_Unknown,
                                             order_qualifier=OrderQualifier_Unknown,
                                             account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ---------- 
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b85a50a-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 866535, tzinfo=tzfile('PRC')) 203                                                          0    0               0             0              0               0         0                                    0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_buying_on_collateral - 担保品买入

**函数原型**

```
credit_buying_on_collateral(symbol, volume, price,
                                order_type=OrderType_Limit,
                                order_duration=OrderDuration_Unknown,
                                order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：`list[dict]`**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_buying_on_collateral(symbol='SHSE.600000', volume=100, price=10.67, order_type=OrderType_Limit,
                                             order_duration=OrderDuration_Unknown,
                                             order_qualifier=OrderQualifier_Unknown,
                                             account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at 
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b861a31-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 869534, tzinfo=tzfile('PRC')) 207                                                          0    0               0             0              0               0         0                                    0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_selling_on_collateral - 担保品卖出

**函数原型**

```
credit_selling_on_collateral(symbol, volume, price,
                                 order_type=OrderType_Limit,
                                 order_duration=OrderDuration_Unknown,
                                 order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：`list[dict]`**

请参考[order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_selling_on_collateral(symbol='SHSE.600000', volume=100, price=10.67, order_type=OrderType_Limit,
                                             order_duration=OrderDuration_Unknown,
                                             order_qualifier=OrderQualifier_Unknown,
                                             account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status price volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at 
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ----- ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b861a31-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     10.67 100    datetime.datetime(2020, 6, 6, 15, 41, 44, 869534, tzinfo=tzfile('PRC')) 208                                                          0    0               0             0              0               0         0                                    0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None

```

### credit_collateral_in - 担保品转入

**函数原型**

```
credit_collateral_in(symbol, volume, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：`list[dict]`**

请参考 [order](python_object_trade.html#order---委托对象)  返回值字段说明

**示例代码**

```
credit_collateral_in(symbol='SHSE.600000', volume=100, account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail price stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at 
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ----- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b868f72-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     100    datetime.datetime(2020, 6, 6, 15, 41, 44, 872536, tzinfo=tzfile('PRC')) 209                                                          0    0               0             0              0               0         0                                    0.0   0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None 
...... ......

```

### credit_collateral_out - 担保品转出

**函数原型**

```
credit_collateral_out(symbol, volume, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量 |
| account_id | str | 账号id，不填或留空，表示使用默认账号，否则使用指定账号 |

**返回值：`list[dict]`**

请参考 [order](python_object_trade.html#order---委托对象) 返回值字段说明

**示例代码**

```
credit_collateral_out(symbol='SHSE.600000', volume=100, account_id='')

```

**示例返回值**

```
strategy_id                          account_id                           cl_ord_id                            symbol      order_type status volume created_at                                                              order_business account_name order_id ex_ord_id algo_order_id side position_effect position_side order_duration order_qualifier order_src ord_rej_reason ord_rej_reason_detail price stop_price order_style value percent target_volume target_value target_percent filled_volume filled_vwap filled_amount filled_commission updated_at 
------------------------------------ ------------------------------------ ------------------------------------ ----------- ---------- ------ ------ ----------------------------------------------------------------------- -------------- ------------ -------- --------- ------------- ---- --------------- ------------- -------------- --------------- --------- -------------- --------------------- ----- ---------- ----------- ----- ------- ------------- ------------ -------------- ------------- ----------- ------------- ----------------- ----------
3af55cb8-a7c5-11ea-b510-309c231d28bd 8f30e83f-a7c5-11ea-b510-309c231d28bd 2b868f72-a7c9-11ea-b510-309c231d28bd SHSE.600000 1          10     100    datetime.datetime(2020, 6, 6, 15, 41, 44, 872536, tzinfo=tzfile('PRC')) 210                                                          0    0               0             0              0               0         0                                    0.0   0.0        0           0.0   0.0     0             0.0          0.0            0             0.0         0.0           0.0               None 
...... ......

```
     [ ** ](trade_data.html#contextaccountcash---查询当前账户资金) [ ** ](python-credit-trade-api.html#creditbuyingonmargin----融资买入)
