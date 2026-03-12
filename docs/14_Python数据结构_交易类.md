# 数据结构

## 交易类

### Account - 账户对象

[](#cash---资金对象)

[](#position---持仓对象)（参见 positionside   持仓方向）

[](#position---持仓对象)

（参见 交易账户状态）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | str | 账户id，实盘时用于指定交易账户 |
| title | str | 账户标题，实盘时用于指定账户名称 |
| cash | dict | 资金字典 |
| positions(symbol='', side=None) | list | 持仓情况 列表, 默认全部持仓, 可根据单一symbol（类型str）, side 参数可缩小查询范围 |
| position(symbol, side) | dict | 持仓情况 查询指定单一symbol（类型str）及持仓方向的持仓情况 |
| status | dict | 交易账户状态 查询交易账户连接状态 |

### Order - 委托对象

（参见 委托状态）

（参见 委托方向）

（参见 开平仓类型）

（参见 持仓方向）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

（参见 委托业务类型）

（参见 订单拒绝原因）


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| strategy_id | str | 策略ID |
| account_id | str | 账号ID |
| account_name | str | 账户登录名 |
| cl_ord_id | str | 委托客户端ID，下单生成，固定不变（东方财富量化维护，下单唯一标识） |
| order_id | str | 委托柜台ID（系统字段，下单不会立刻生成，委托报到柜台才会生成） |
| ex_ord_id | str | 委托交易所ID（系统字段，下单不会立刻生成，委托报到柜台才会生成） |
| algo_order_id | str | 算法单ID |
| symbol | str | 标的代码 |
| status | int | 委托状态 取值参考 OrderStatus |
| side | int | 买卖方向 取值参考 OrderSide |
| position_effect | int | 开平标志 取值参考 PositionEffect |
| position_side | int | 持仓方向 取值参考 PositionSide |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| order_business | int | 委托业务属性 取值参考 OrderBusiness |
| ord_rej_reason | int | 委托拒绝原因 取值参考 OrderRejegectReason |
| ord_rej_reason_detail | str | 委托拒绝原因描述 |
| position_src | int | 头寸来源（系统字段） |
| volume | int | 委托量 |
| price | float | 委托价格 |
| value | int | 委托额 |
| percent | float | 委托百分比 |
| target_volume | int | 委托目标量 |
| target_value | int | 委托目标额 |
| target_percent | float | 委托目标百分比 |
| filled_volume | int | 已成量  （一笔委托对应多笔成交为累计值） |
| filled_vwap | float | 已成均价，公式为(price*(1+backtest_slippage_ratio)) （仅股票实盘支持，期货实盘不支持） |
| filled_amount | float | 已成金额，公式为(filled_volume*filled_vwap) （仅股票实盘支持，期货实盘不支持） |
| created_at | datetime.datetime | 委托创建时间 |
| updated_at | datetime.datetime | 委托更新时间 |

### ExecRpt - 回报对象

（参见 委托方向）

（参见 开平仓类型）

（参见 委托业务类型）

（参见 委托风格）

（参见 订单拒绝原因）

（参见 执行回报类型）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| strategy_id | str | 策略ID |
| account_id | str | 账号ID |
| account_name | str | 账户登录名 |
| cl_ord_id | str | 委托客户端ID |
| order_id | str | 委托柜台ID |
| exec_id | str | 委托交易所ID |
| symbol | str | 委托标的 |
| side | int | 买卖方向 取值参考 OrderSide |
| position_effect | int | 开平标志 取值参考 PositionEffect |
| order_business | int | 委托业务属性 OrderBusiness |
| order_style | int | 委托风格 OrderStyle |
| ord_rej_reason | int | 委托拒绝原因 取值参考 OrderRejectReason |
| ord_rej_reason_detail | str | 委托拒绝原因描述 |
| exec_type | int | 执行回报类型 取值参考 ExecType |
| price | float | 成交价格 |
| volume | int | 成交量 |
| amount | float | 成交金额 |
| cost | float | 成交成本金额（仅期货实盘支持，股票实盘不支持） |
| created_at | datetime.datetime | 回报创建时间 |

### Cash - 资金对象

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号ID |
| account_name | str | 账户登录名 |
| currency | int | 币种 |
| nav | float | 总资金 |
| fpnl | float | 浮动盈亏 |
| frozen | float | 持仓占用资金 （仅期货实盘支持，股票实盘不支持） |
| order_frozen | float | 冻结资金 |
| available | float | 可用资金 |
| market_value | float | 市值  （仅股票实盘支持，期货实盘不支持） |
| balance | float | 资金余额 |
| created_at | datetime.datetime | 资金初始时间 |
| updated_at | datetime.datetime | 资金变更时间 |

### Position - 持仓对象

（参见 持仓方向）


``


``

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号ID |
| account_name | str | 账户登录名 |
| symbol | str | 标的代码 |
| side | int | 持仓方向 取值参考 PositionSide |
| volume | int | 总持仓量; 如果要得到昨持仓量，公式为 (volume - volume_today) |
| volume_today | int | 今日持仓量 |
| vwap | float | 持仓均价 new_vwap=((position.vwap * position.volume)+(trade.volume*trade.price))/(position.volume+trade.volume) （实盘时，期货跨天持仓，会自动变成昨结价，仿真是开仓均价） |
| vwap_open | float | 开仓均价（期货适用，实盘适用） |
| amount | float | 持仓额 (volume*vwap*multiplier) |
| price | float | 当前行情价格（回测时值为0） |
| fpnl | float | 持仓浮动盈亏 ((price - vwap) * volume * multiplier) （基于效率的考虑，回测模式fpnl只有仓位变化时或者一天更新一次,仿真模式3s更新一次, 回测的price为当天的收盘价） （根据持仓均价计算） |
| fpnl_open | float | 浮动盈亏（期货适用， 根据开仓均价计算） |
| cost | float | 持仓成本 (vwap * volume * multiplier * margin_ratio) |
| order_frozen | int | 挂单冻结仓位 |
| order_frozen_today | int | 挂单冻结今仓仓位(仅上期所和上海能源交易所标的支持) |
| available | int | 非挂单冻结仓位 ，公式为(volume - order_frozen); 如果要得到可平昨仓位，公式为 (available - available_today) |
| available_today | int | 非挂单冻结今仓位，公式为 (volume_today - order_frozen_today)(仅上期所和上海能源交易所标的支持) |
| available_now | int | 当前可用仓位 （实盘适用） |
| credit_position_sellable_volume | int | 可卖担保品数 |
| created_at | datetime.datetime | 建仓时间（实盘不支持） |
| updated_at | datetime.datetime | 仓位变更时间（实盘不支持） |

### Indicator - 绩效指标对象

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| account_id | str | 账号ID |
| pnl_ratio | float | 累计收益率 (pnl/cum_inout) |
| pnl_ratio_annual | float | 年化收益率 (pnl_ratio/自然天数*365) |
| sharp_ratio | float | 夏普比率           （[E(Rp)-Rf]/δp,E(Rp) = mean(pnl_ratio),Rf = 0,δp = std(pnl_ratio) ) |
| max_drawdown | float | 最大回撤 max_drawdown=max（Di-Dj）/Di；D为某一天的净值（j>i) |
| risk_ratio | float | 风险比率 （持仓市值/nav） |
| calmar_ratio | float | 卡玛比率 |
| open_count | int | 开仓次数 |
| close_count | int | 平仓次数 |
| win_count | int | 盈利次数（平仓价格大于持仓均价vwap的次数） |
| lose_count | int | 亏损次数 （平仓价格小于或者等于持仓均价vwap的次数） |
| win_ratio | float | 胜率 (win_count / (win_count + lose_count)) |
| created_at | datetime.datetime | 指标创建时间 |
| updated_at | datetime.datetime | 指标变更时间 |

### algoOrder - 算法委托母单对象

（参见 委托状态）

（参见 委托方向）

（参见 开平仓类型）

（参见 持仓方向）

（参见 委托类型）

（参见 委托时间属性）

（参见 委托成交属性）

（参见 委托业务类型）

（参见 委托风格）

（参见 订单拒绝原因）

（参见 算法单状态）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| strategy_id | str | 策略 ID |
| account_id | str | 账号 ID |
| account_name | str | 账户登录名 |
| cl_ord_id | str | 委托客户端 ID，下单生成，固定不变（掘金维护，下单唯一标识） |
| order_id | str | 委托柜台 ID（系统字段，下单不会立刻生成，委托报到柜台才会生成） |
| ex_ord_id | str | 委托交易所 ID（系统字段，下单不会立刻生成，委托报到柜台才会生成） |
| symbol | str | 标的代码 |
| status | int | 委托状态 取值参考 OrderStatus |
| side | int | 买卖方向 取值参考 OrderSide |
| position_effect | int | 开平标志 取值参考 PositionEffect |
| position_side | int | 持仓方向 取值参考 PositionSide |
| order_type | int | 委托类型 取值参考 OrderType |
| order_duration | int | 委托时间属性 取值参考 OrderDuration |
| order_qualifier | int | 委托成交属性 取值参考 OrderQualifier |
| order_business | int | 委托业务属性 取值参考 OrderBusiness |
| order_style | int | 委托风格属性 取值参考 OrderStyle |
| ord_rej_reason | int | 委托拒绝原因 取值参考 OrderRejegectReason |
| ord_rej_reason_detail | str | 委托拒绝原因描述 |
| position_src | int | 头寸来源（系统字段） |
| volume | int | 委托量 |
| price | float | 委托价格 |
| value | int | 委托额 |
| percent | float | 委托百分比 |
| target_volume | int | 委托目标量 |
| target_value | int | 委托目标额 |
| target_percent | float | 委托目标百分比 |
| filled_volume | int | 已成量 （一笔委托对应多笔成交为累计值） |
| filled_vwap | float | 已成均价，公式为(price*(1+backtest_slippage_ratio)) （期货实盘不支持） |
| filled_amount | float | 已成金额，公式为(filled_volume*filled_vwap) （期货实盘不支持） |
| filled_commission | float | 已成手续费，（实盘不支持） |
| created_at | datetime.datetime | 委托创建时间 |
| updated_at | datetime.datetime | 委托更新时间 |
| algo_name | str | 算法名称 |
| algo_params | dict | 算法参数 |
| algo_status | int | 算法单状态 取值参考 AlgoOrderStatus |
| algo_comment | str | 算法单备注 |

     [ ** ](python_object_data.html#l2transaction---level2-逐笔成交) [ ** ](python_object_trade.html#account---账户对象)
