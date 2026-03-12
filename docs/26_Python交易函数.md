## 交易函数

### order_volume - 按指定量委托

**函数原型:**

```
order_volume(symbol, volume, side, order_type,position_effect, price=0,order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown,account='')

```

**参数：**

（参见 委托方向）

（参见 委托类型）

（参见 开平仓类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 数量(指股数) |
| side | int | 参见订单委托方向 |
| order_type | int | 参见订单委托类型 |
| position_effect | int | 参见开平仓类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见 委托时间属性 |
| order_qualifier | int | 参见 委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

```
order_volume(symbol='SHSE.600000', volume=10000, side=OrderSide_Buy, order_type=OrderType_Limit, position_effect=PositionEffect_Open, price=11)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 10000, 'value': 110000.0, 'percent': 5.5e-05, 'target_volume': 10000, 'target_value': 110000.0, 'target_percent': 5.5e-05, 'filled_volume': 10000, 'filled_vwap': 11.0011, 'filled_amount': 110010.99999999999, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 11.0011, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 若下单数量输入有误，终端会拒绝此单，并显示`委托量不正确`。股票买入最小单位为`100`，卖出最小单位为`1`,如存在不足100股的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 输入无效参数报`NameError`错误，缺少参数报`TypeError`错误。

**6.**关于`side`与`position_effect`字段的使用说明
做多（买开）：`side=OrderSide_Buy ，position_effect=PositionEffect_Open`
平仓（卖平）：`side=OrderSide_Sell  ，position_effect=PositionEffect_Close`  

做空（卖开）：`side=OrderSide_Sell ，position_effect=PositionEffect_Open` 
平仓（买平）：`side=  OrderSide_Buy ，position_effect=PositionEffect_Close`

### order_value - 按指定价值委托

**函数原型:**

```
order_value(symbol, value, side,order_type, position_effect, price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown,account='')

```

**参数：**

（参见 委托方向）

（参见 委托类型）

（参见 开平仓类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| value | int | 股票价值 |
| side | int | 参见订单委托方向 |
| order_type | int | 参见订单委托类型 |
| position_effect | int | 参见开平仓类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见 委托时间属性 |
| order_qualifier | int | 参见 委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

下限价单，以11元每股的价格买入价值为100000的SHSE.600000,根据volume = value / price,计算并取整得到volume = 9000

```
order_value(symbol='SHSE.600000', value=100000, price=11, side=OrderSide_Buy, order_type=OrderType_Limit, position_effect=PositionEffect_Open)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 9000, 'value': 100000.0, 'percent': 5e-05, 'target_volume': 9000, 'target_value': 99000.0, 'target_percent': 4.95e-05, 'filled_volume': 9000, 'filled_vwap': 11.0011, 'filled_amount': 99009.9, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 9.90099, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据指定价值计算购买标的数量，即`value/price`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单,计算使用价格为最新一个tick中的最新价，price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数报TypeError错误。

### order_percent - 按总资产指定比例委托

**函数原型:**

```
order_percent(symbol, percent, side,order_type, position_effect, price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account='')

```

**参数：**

（参见 委托方向）

（参见 委托类型）

（参见 开平仓类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| percent | double | 委托占总资产比例 |
| side | int | 参见订单委托方向 |
| order_type | int | 参见订单委托类型 |
| position_effect | int | 参见开平仓类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见 委托时间属性 |
| order_qualifier | int | 参见 委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

当前总资产为1000000。下限价单，以11元每股的价格买入SHSE.600000,期望买入比例占总资产的10%，根据volume = nav * precent / price 计算取整得出volume = 9000

```
order_percent(symbol='SHSE.600000', percent=0.1, side=OrderSide_Buy, order_type=OrderType_Limit, position_effect=PositionEffect_Open, price=11)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 18181800, 'value': 200000000.0, 'percent': 0.1, 'target_volume': 18181800, 'target_value': 199999800.0, 'target_percent': 0.0999999, 'filled_volume': 18181800, 'filled_vwap': 11.0011, 'filled_amount': 200019799.98, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 20001.979998, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据指定比例计算购买标的数量,即`(nav*precent)/price`,股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单，计算使用价格为最新一个tick中的最新价，price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数报TypeError错误。

**6.** 期货实盘时，percent是以交易所保证金水平计算得到的，并非真实保证金水平。

### order_target_volume - 调仓到目标持仓量

**函数原型:**

```
order_target_volume(symbol, volume, position_side, order_type, price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account='')

```

**参数：**

（参见 持仓方向）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 期望的最终数量 |
| position_side | int | 表示将多仓还是空仓调到目标持仓量，参见 持仓方向 |
| order_type | int | 参见 订单类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见  委托时间属性 |
| order_qualifier | int | 参见  委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

当前SHSE.600000多方向持仓量为0，期望持仓量为10000，下单量为期望持仓量 - 当前持仓量 = 10000

```
order_target_volume(symbol='SHSE.600000', volume=10000, position_side=PositionSide_Long, order_type=OrderType_Limit, price=13)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 13.0, 'order_style': 1, 'volume': 10000, 'value': 130000.0, 'percent': 6.5e-05, 'target_volume': 10000, 'target_value': 130000.0, 'target_percent': 6.5e-05, 'filled_volume': 10000, 'filled_vwap': 13.0013, 'filled_amount': 130013.0, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 13.0013, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

600000浦发银行需要全部卖出时，volume设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标持有量（volume）到0，底层就会执行卖出

```
order_target_volume(symbol='SHSE.600000', volume=0, position_side=PositionSide_Long, order_type=OrderType_Limit, price=11)

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，订单会被拒绝，`终端无显示，无回报`。回测模式可参看order_reject_reason。

**2.** 根据目标数量计算下单数量，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则订单会被拒绝，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`,上期所昨仓不能平掉。应研究需要，股票也支持卖空操作。

**4.** Order_type优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。若OrderTpye_Limit限价单价格错误，终端拒绝此单，显示委托价格错误。`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数报Typeerror错误。

**6.** 股票交易position_side 仅支持设置多方向。

### order_target_value - 调仓到目标持仓额

**函数原型:**

```
order_target_value(symbol, value, position_side, order_type, price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account='')

```

**参数：**

（参见 持仓方向）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| value | int | 期望的股票最终价值 |
| position_side | int | 表示将多仓还是空仓调到目标持仓量，参见 持仓方向 |
| order_type | int | 参见 订单类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见  委托时间属性 |
| order_qualifier | int | 参见  委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

当前SHSE.600000多方向当前持仓量为0，目标持有价值为100000的该股票，根据value / price 计算取整得出目标持仓量volume为9000，目标持仓量 - 当前持仓量 = 下单量为9000

```
order_target_value(symbol='SHSE.600000', value=100000, position_side=PositionSide_Long, order_type=OrderType_Limit, price=11)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 9000, 'value': 100000.0, 'percent': 5e-05, 'target_volume': 9000, 'target_value': 100000.0, 'target_percent': 5e-05, 'filled_volume': 9000, 'filled_vwap': 11.0011, 'filled_amount': 99009.9, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 9.90099, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

600000浦发银行需要全部卖出时，value设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标持有价值（value）到0，底层就会执行卖出

```
order_target_value(symbol='SHSE.600000', value=0, position_side=PositionSide_Long, order_type=OrderType_Limit, price=11)

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，订单会被拒绝，`终端无显示，无回报`。回测模式可参看order_reject_reason。

**2.** 根据目标价值计算下单数量，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则本地拒绝此单，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`，目前不可修改。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单，计算使用价格为最新一个tick中的最新价，price参数失效。若OrderTpye_Limit限价单价格错误，终端拒绝此单，显示委托价格错误。`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数报Typeerror错误。

**6.** 股票交易position_side 仅支持设置多方向。

### order_target_percent - 调仓到目标持仓比例（总资产的比例）

**函数原型:**

```
order_target_percent(symbol, percent, position_side, order_type, price=0, order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown, account='')

```

**参数：**

（参见 持仓方向）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| percent | double | 期望的最终占总资产比例 |
| position_side | int | 表示将多仓还是空仓调到目标持仓量，参见 持仓方向 |
| order_type | int | 参见 订单类型 |
| price | float | 价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| order_duration | int | 参见  委托时间属性 |
| order_qualifier | int | 参见  委托成交属性 |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

当前总资产价值为1000000，目标为以11元每股的价格买入SHSE.600000的价值占总资产的10%，根据volume = nav * percent / price 计算取整得出应持有9000股。当前该股持仓量为零，因此买入量为9000

```
order_target_percent(symbol='SHSE.600000', percent=0.1, position_side=PositionSide_Long, order_type=OrderType_Limit, price=11)

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 1, 'status': 3, 'price': 11.0, 'order_style': 1, 'volume': 18181800, 'value': 200000000.0, 'percent': 0.1, 'target_volume': 18181800, 'target_value': 199999800.0, 'target_percent': 0.1, 'filled_volume': 18181800, 'filled_vwap': 11.0011, 'filled_amount': 200019799.98, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 20001.979998, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

600000浦发银行需要全部卖出时，percent设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标比例（percent）到0，底层就会执行卖出

```
order_target_percent(symbol='SHSE.600000', percent=0, position_side=PositionSide_Long, order_type=OrderType_Limit, price=11)

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，订单会被拒绝，`终端无显示，无回报`。回测模式可参看order_reject_reason。

**2.** 根据目标比例计算下单数量，为占`总资产(nav）`比例，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则本地拒绝此单，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端拒绝此单，`显示仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`，目前不可修改。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单，计算使用价格为最新一个tick中的最新价，price参数失效。若OrderTpye_Limit限价单价格错误，终端拒绝此单，显示委托价格错误。`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数报Typeerror错误。

**6.** 期货实盘时，percent是以交易所保证金水平计算得到的，并非真实保证金水平。

**7.** 股票交易position_side 仅支持设置多方向。

### order_batch - 批量委托接口

**函数原型:**

```
order_batch(orders, combine=False, account='')

```

**参数：**

（参见 委托对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| orders | list[order] | 委托对象列表，其中委托至少包含交易接口的必选参数，参见委托 |
| combine | bool | 是否是组合单, 默认不是（预留字段，目前无效） |
| account | account id or account name or None | 帐户 |

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

```
    order_1 = {'symbol': 'SHSE.600000', 'volume': 100, 'price': 11, 'side': 1,
               'order_type': 2, 'position_effect':1}
    order_2 = {'symbol': 'SHSE.600004', 'volume': 100, 'price': 11, 'side': 1,
               'order_type': 2, 'position_effect':1}
    orders = [order_1, order_2]
    batch_orders = order_batch(orders, combine=True)
    for order in batch_orders:
        print(order)

```

**返回：**

```
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'order_type': 2, 'status': 3, 'price': 10.280000686645508, 'order_style': 1, 'volume': 100, 'filled_volume': 100, 'filled_vwap': 10.281028686714173, 'filled_amount': 1028.1028686714174, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 0.10281028686714173, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'position_side': 0, 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0, 'value': 0.0, 'percent': 0.0, 'target_volume': 0, 'target_value': 0.0, 'target_percent': 0.0}
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000001', 'symbol': 'SHSE.600004', 'side': 1, 'position_effect': 1, 'order_type': 2, 'status': 3, 'price': 15.050000190734863, 'order_style': 1, 'volume': 100, 'filled_volume': 100, 'filled_vwap': 15.051505190753936, 'filled_amount': 1505.1505190753935, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 0.15051505190753936, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'position_side': 0, 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0, 'value': 0.0, 'percent': 0.0, 'target_volume': 0, 'target_value': 0.0, 'target_percent': 0.0}
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000002', 'symbol': 'SHSE.600000', 'side': 1, 'position_effect': 1, 'order_type': 2, 'status': 3, 'price': 10.180000305175781, 'order_style': 1, 'volume': 100, 'filled_volume': 100, 'filled_vwap': 10.1810183052063, 'filled_amount': 1018.10183052063, 'created_at': datetime.datetime(2020, 9, 2, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 2, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 0.101810183052063, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'position_side': 0, 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0, 'value': 0.0, 'percent': 0.0, 'target_volume': 0, 'target_value': 0.0, 'target_percent': 0.0}
{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000003', 'symbol': 'SHSE.600004', 'side': 1, 'position_effect': 1, 'order_type': 2, 'status': 3, 'price': 14.819999694824219, 'order_style': 1, 'volume': 100, 'filled_volume': 100, 'filled_vwap': 14.8214816947937, 'filled_amount': 1482.14816947937, 'created_at': datetime.datetime(2020, 9, 2, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 2, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 0.148214816947937, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'position_side': 0, 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0, 'value': 0.0, 'percent': 0.0, 'target_volume': 0, 'target_value': 0.0, 'target_percent': 0.0}

```

**注意：**

**1.** 每个order的symbol仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 若下单数量输入有误，终端会拒绝此单，并显示`委托量不正确`。`下单数量严格按照指定数量下单`，需注意股票买入最小单位为100。

**3.** 若仓位不足，终端会拒绝此单，`显示仓位不足`。应研究需要，`股票也支持卖空操作`。

**4.** Order_type优先级高于price,若指定OrderType_Market下市价单，则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 输入无效参数报NameError错误，缺少参数不报错，可能会出现下单被拒。

### order_cancel - 撤销委托

**函数原型:**

```
order_cancel(wait_cancel_orders)

```

**参数：**

（参见 委托对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| wait_cancel_orders | list[str] | 委托对象列表 or 单独委托对象，至少包含cl_ord_id， 参见委托 |

**示例：**

```
# 先查未结委托，再把未结委托全部撤单，
unfin_order = get_unfinished_orders()
order_cancel(wait_cancel_orders=unfin_order)

# 也可循环未结委托，找到对应的cl_ord_id撤单
# unfin_order = get_unfinished_orders()
# for order in unfin_order:
#     order_cancel(wait_cancel_orders=order)

```

### order_cancel_all - 撤销所有委托

**函数原型:**

```
order_cancel_all()

```

**示例：**

```
order_cancel_all()

```

### order_close_all - 平当前所有可平持仓

**注意:**不支持市价委托类型的委托，会被柜台拒绝

**函数原型:**

```
order_close_all()

```

**示例：**

```
order_close_all()

```

### get_unfinished_orders - 查询日内全部未结委托

**函数原型:**

```
get_unfinished_orders()

```

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

```
get_unfinished_orders()

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600519', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 2, 'status': 3, 'price': 1792.0, 'order_style': 1, 'volume': 100, 'value': 179200.0, 'percent': 8.96e-05, 'target_volume': 100, 'target_value': 179200.0, 'target_percent': 8.96e-05, 'filled_volume': 100, 'filled_vwap': 1792.1792, 'filled_amount': 179217.92, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 17.921792000000003, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

### get_orders - 查询日内全部委托

**函数原型:**

```
get_orders()

```

**返回值:**

（参见 委托对象）

| 类型 | 说明 |
| --- | --- |
| list[order] | 委托对象列表，参见委托 |

**示例：**

```
get_orders()

```

**返回：**

```
[{'strategy_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'account_id': 'd7443a53-f65b-11ea-bb9d-484d7eaefe55', 'cl_ord_id': '000000000', 'symbol': 'SHSE.600519', 'side': 1, 'position_effect': 1, 'position_side': 1, 'order_type': 2, 'status': 3, 'price': 1792.0, 'order_style': 1, 'volume': 100, 'value': 179200.0, 'percent': 8.96e-05, 'target_volume': 100, 'target_value': 179200.0, 'target_percent': 8.96e-05, 'filled_volume': 100, 'filled_vwap': 1792.1792, 'filled_amount': 179217.92, 'created_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'updated_at': datetime.datetime(2020, 9, 1, 9, 40, tzinfo=tzfile('PRC')), 'filled_commission': 17.921792000000003, 'account_name': '', 'order_id': '', 'ex_ord_id': '', 'algo_order_id': '', 'order_business': 0, 'order_duration': 0, 'order_qualifier': 0, 'order_src': 0, 'position_src': 0, 'ord_rej_reason': 0, 'ord_rej_reason_detail': '', 'stop_price': 0.0}]

```

### get_execution_reports - 查询日内全部执行回报

**函数原型:**

```
get_execution_reports()

```

**返回值:**

（参见 回报对象）

| 类型 | 说明 |
| --- | --- |
| list[execrpt] | 回报对象列表， 参见成交回报 |

**示例：**

```
get_execution_reports()

```

**返回：**

```
[{'strategy_id': '004beb61-1282-11eb-9313-00ff5a669ee2', 'account_id': '3acc8b6e-af54-11e9-b2de-00163e0a4100', 'account_name': '3acc8b6e-af54-11e9-b2de-00163e0a4100', 'cl_ord_id': '49764a82-14fb-11eb-89df-00ff5a669ee2', 'order_id': '4a06f925-14fb-11eb-9e8a-00163e0a4100', 'exec_id': '573b108b-14fb-11eb-9e8a-00163e0a4100', 'symbol': 'SHSE.600714', 'position_effect': 1, 'side': 1, 'exec_type': 15, 'price': 5.579999923706055, 'volume': 900, 'amount': 5021.999931335449, 'created_at': datetime.datetime(2020, 10, 23, 14, 45, 29, 776756, tzinfo=tzfile('PRC')), 'commission': 5.0, 'cost': 5021.999931335449, 'ord_rej_reason': 0, 'ord_rej_reason_detail': ''}]

```

### ipo_buy - 新股申购

仅在**实盘**中可以使用

**函数原型:**

```
ipo_buy(symbol, volume, price, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 申购数量 |
| price | float | 新股发行价 |
| account_id | str | 账户ID，不指定则使用默认账户 |

返回值 `List[Dict]`

### ipo_get_quota - 查询新股申购额度

仅在**实盘**中可以使用

**函数原型:**

```
ipo_get_quota(account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账户ID，不指定则使用默认账户 |

**返回值:**

返回值 `List[Dict[str, Any]]`

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| exchange | str | 市场代码 上交所"SHSE", 深交所”SZSE" |
| quota | float | 可申购数量 |
| SSE_STAR_quota | float | 科创板可申购数量 |

### ipo_get_instruments - 查询当日新股清单

仅在**实盘**中可以使用

**函数原型:**

```
ipo_get_instruments(sec_type, account_id='', df=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| sec_type | int | 标的类型，用以区别获取新股还是新债 |
| account_id | str | 账户ID，不指定则使用默认账户 |
| df | bool | 是否返回 DataFrame |

**返回值:**

返回值 `List[Dict]`

| key | value类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| price | float | 申购价格 |
| min_vol | int | 申购最小数量 |
| max_vol | int | 申购最大数量 |

### ipo_get_match_number - 查询配号

仅在**实盘**中可以使用

**函数原型:**

```
ipo_get_match_number(start_time, end_time, account_id='', df=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| start_time | str | 开始时间， (%Y-%m-%d %H:%M:%S 格式) |
| end_time | str | 结束时间， (%Y-%m-%d %H:%M:%S 格式) |
| account_id | str | 账户ID，不指定则使用默认账户 |
| df | bool | 是否返回 DataFrame |

**返回值:**

返回值 `List[Dict]`

| key | value类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| order_id | str | 委托号 |
| volume | int | 成交数量 |
| match_number | str | 申购配号 |
| order_at | datetime.datetime | 委托日期 |
| match_at | datetime.datetime | 配号日期 |

### ipo_get_lot_info - 中签查询

仅在**实盘**中可以使用

**函数原型:**

```
ipo_get_lot_info(start_time, end_time, account_id='', df=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| start_time | str | 开始时间， (%Y-%m-%d %H:%M:%S 格式) |
| end_time | str | 结束时间， (%Y-%m-%d %H:%M:%S 格式) |
| account_id | str | 账户ID，不指定则使用默认账户 |
| df | bool | 是否返回 DataFrame |

**返回值:**

返回值 `List[Dict]`

| key | value类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| order_at | int | 委托日期 |
| lot_at | int | 中签日期 |
| lot_volume | int | 中签数量 |
| give_up_volume | int | 放弃数量 |
| price | float | 中签价格 |
| amount | float | 中签金额 |
| pay_volume | float | 已缴款数量 |
| pay_amount | float | 已缴款金额 |

### bond_reverse_repurchase_agreement - 国债逆回购

仅在**实盘**中可以使用

```
bond_reverse_repurchase_agreement(symbol, volume, price, order_type=OrderType_Limit,
order_duration=OrderQualifier_Unknown, order_qualifier=OrderQualifier_Unknown, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 认购数量 |
| price | float | 价格 |
| order_type | int | 委托类型 |
| order_duration | int | 委托时间属性 |
| order_qualifier | int | 委托成交属性 |
| account_id | str | 账户ID，不指定则使用默认账户 |

返回值 `List[Dict]`

**注意：**逆回购1张为100元。上海市场最少交易1000张，深圳最少交易10张。且上海数量必须是1000张的整数倍，深圳数量必须是10张的整数倍，也即上海要10万元一个单位的买，深圳一千元一个单位的买。

### bond_convertible_call - 可转债转股

仅在**实盘**中可以使用

```
bond_convertible_call(symbol, volume, price=0.0, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 认购数量 |
| price | float | 价格 |
| account_id | str | 账户ID，不指定则使用默认账户 |

返回值 `List[Dict[Text, Any]]`

### bond_convertible_put - 可转债回售

仅在**实盘**中可以使用

```
bond_convertible_put(symbol, volume, price=0.0, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 认购数量 |
| price | float | 价格 |
| account_id | str | 账户ID，不指定则使用默认账户 |

返回值 `List[Dict[Text, Any]]`

### bond_convertible_put_cancel - 可转债回售撤销

仅在**实盘**中可以使用

```
bond_convertible_put_cancel(symbol, volume, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 认购数量 |
| account_id | str | 账户ID，不指定则使用默认账户 |

返回值 `List[Dict[Text, Any]]`
     [ ** ](python_select_api_bond_vip.html#bndgetamountchange---查询可转债剩余规模变动) [ ** ](python_trade_api.html#ordervolume---按指定量委托)
