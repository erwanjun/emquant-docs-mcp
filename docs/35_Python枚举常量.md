# 枚举常量

## OrderStatus - 委托状态

```
OrderStatus_Unknown = 0
OrderStatus_New = 1                   # 已报
OrderStatus_PartiallyFilled = 2       # 部成
OrderStatus_Filled = 3                # 已成
OrderStatus_Canceled = 5              # 已撤
OrderStatus_Rejected = 8              # 已拒绝
OrderStatus_PendingNew = 10           # 待报
OrderStatus_Expired = 12              # 已过期

```

## OrderSide - 委托方向

```
OrderSide_Unknown = 0
OrderSide_Buy = 1             # 买入
OrderSide_Sell = 2            # 卖出

```

## OrderType - 委托类型

```
用于映射OrderDuration和OrderQualifier的参数组合，推荐下单时直接指定OrderType，可无需额外指定OrderDuration和OrderQualifier

OrderType_Unknown = 0
OrderType_Limit = 1            # 限价委托 (全部交易所支持)
OrderType_Market = 2           # 市价委托 （上期所和上能所不支持，中金所远期合约不支持，可转债不支持，上交所需要填上price保护限价）

# 终端3.18.0.0以上新增
# 上交所
OrderType_Limit = 1           # 限价
OrderType_Market = 2       # 市价(默认五档即成转限)
OrderType_Market_BOC = 20  # 市价对方最优价格(best of counterparty)
OrderType_Market_BOP = 21  # 市价己方最优价格(best of party)
OrderType_Market_B5TC = 24 # 市价最优五档剩余撤销(best 5 then cancel)
OrderType_Market_B5TL = 25 # 市价最优五档剩余转限价(best 5 then limit)

# 深交所
OrderType_Limit = 1           # 限价
OrderType_Market = 2       # 市价（默认对方最优价）
OrderType_Market_BOC = 20  # 市价对方最优价格(best of counterparty)
OrderType_Market_BOP = 21  # 市价己方最优价格(best of party)
OrderType_Market_FAK = 22  # 市价即时成交剩余撤销(fill and kill)
OrderType_Market_FOK = 23  # 市价即时全额成交或撤销(fill or kill)
OrderType_Market_B5TC = 24 # 市价最优五档剩余撤销(best 5 then cancel)

```

## OrderDuration - 委托时间属性

仅在实盘模式生效，具体执行模式请参考交易所给出的定义

```
OrderDuration_Unknown = 0
OrderDuration_FAK = 1           # 即时成交剩余撤销(fill and kill)
OrderDuration_FOK = 2           # 即时全额成交或撤销(fill or kill)
OrderDuration_GFD = 3           # 当日有效(good for day)
OrderDuration_GFS = 4           # 本节有效(good for section)
OrderDuration_GTD = 5           # 指定日期前有效(goodltilldate)
OrderDuration_GTC = 6           # 撤销前有效(goodtillcancel)
OrderDuration_GFA = 7           # 集合竞价前有效(good for auction)
OrderDuration_AHT = 8           # 盘后定价交易(after hour trading)

```

## OrderQualifier - 委托成交属性

仅在实盘模式生效，具体执行模式请参考交易所给出的定义

```
OrderQualifier_Unknown = 0
OrderQualifier_BOC     = 1            # 对方最优价格(best of counterparty)
OrderQualifier_BOP     = 2            # 己方最优价格(best of party)
OrderQualifier_B5TC    = 3            # 最优五档剩余撤销(best 5 then cancel)
OrderQualifier_B5TL    = 4            # 最优五档剩余转限价(best 5 then limit)

```

[]()

## OrderBusiness - 委托业务类型

```
OrderBusiness_NORMAL = 0           # 普通交易。默认值为空，以保持向前兼容

OrderBusiness_STOCK_BUY = 1        # 股票,基金,可转债买入（映射OrderSide_Buy和PositionEffect_Open）
OrderBusiness_STOCK_SELL = 2       # 股票,基金,可转债卖出（映射OrderSide_Buy和PositionEffect_Close）

OrderBusiness_IPO_BUY = 100        # 新股申购    100

OrderBusiness_CREDIT_BOM = 200      # 融资买入(buying on margin)
OrderBusiness_CREDIT_SS = 201       # 融券卖出(short selling)
OrderBusiness_CREDIT_RSBBS = 202    # 买券还券(repay share by buying share)
OrderBusiness_CREDIT_RCBSS = 203    # 卖券还款(repay cash by selling share)
OrderBusiness_CREDIT_DRS = 204      # 直接还券(directly repay share)

# 直接还款: 不通过委托，参考接口...
OrderBusiness_CREDIT_CPOM = 205     # 融资平仓(close position on margin)
OrderBusiness_CREDIT_CPOSS = 206    # 融券平仓(close position on short selling)
OrderBusiness_CREDIT_BOC = 207      # 担保品买入(buying on collateral)
OrderBusiness_CREDIT_SOC = 208      # 担保品卖出(selling on collateral)
OrderBusiness_CREDIT_CI = 209       # 担保品转入(collateral in)
OrderBusiness_CREDIT_CO = 210       # 担保品转出(collateral out)

OrderBusiness_BOND_CONVERTIBLE_CALL = 402        #可转债转股
OrderBusiness_BOND_CONVERTIBLE_PUT = 403         #可转债回售
OrderBusiness_BOND_CONVERTIBLE_PUT_CANCEL = 404  #可转债回售撤销

```

## ExecType - 执行回报类型

```
ExecType_Unknown = 0
ExecType_Trade = 15                   # 成交
ExecType_CancelRejected = 19          # 撤单被拒绝

```

## PositionEffect - 开平仓类型

```
PositionEffect_Unknown = 0
PositionEffect_Open = 1                  # 开仓
PositionEffect_Close = 2                 # 平仓, 具体语义取决于对应的交易所
PositionEffect_CloseToday = 3            # 平今仓
PositionEffect_CloseYesterday = 4        # 平昨仓

```

## PositionSide - 持仓方向

```
PositionSide_Unknown = 0
PositionSide_Long = 1            # 多方向
PositionSide_Short = 2           # 空方向

```

## OrderRejectReason - 订单拒绝原因

```
OrderRejectReason_Unknown = 0                          # 未知原因
OrderRejectReason_RiskRuleCheckFailed = 1              # 不符合风控规则
OrderRejectReason_NoEnoughCash = 2                     # 资金不足
OrderRejectReason_NoEnoughPosition = 3                 # 仓位不足
OrderRejectReason_IllegalAccountId = 4                 # 非法账户ID
OrderRejectReason_IllegalStrategyId = 5                # 非法策略ID
OrderRejectReason_IllegalSymbol = 6                    # 非法交易标的
OrderRejectReason_IllegalVolume = 7                    # 非法委托量
OrderRejectReason_IllegalPrice = 8                     # 非法委托价
OrderRejectReason_AccountDisabled = 10                 # 交易账号被禁止交易
OrderRejectReason_AccountDisconnected = 11             # 交易账号未连接
OrderRejectReason_AccountLoggedout = 12                # 交易账号未登录
OrderRejectReason_NotInTradingSession = 13             # 非交易时段
OrderRejectReason_OrderTypeNotSupported = 14           # 委托类型不支持
OrderRejectReason_Throttle = 15                        # 流控限制

```

## CancelOrderRejectReason - 取消订单拒绝原因

```
CancelOrderRejectReason_OrderFinalized = 101           # 委托已完成
CancelOrderRejectReason_UnknownOrder = 102             # 未知委托
CancelOrderRejectReason_BrokerOption = 103             # 柜台设置
CancelOrderRejectReason_AlreadyInPendingCancel = 104   # 委托撤销中

```

## OrderStyle - 委托风格

```
OrderStyle_Unknown = 0
OrderStyle_Volume = 1                                  # 按指定量委托
OrderStyle_Value = 2                                   # 按指定价值委托
OrderStyle_Percent = 3                                 # 按指定比例委托
OrderStyle_TargetVolume = 4                            # 调仓到目标持仓量
OrderStyle_TargetValue = 5                             # 调仓到目标持仓额
OrderStyle_TargetPercent = 6                           # 调仓到目标持仓比例

```

## CashPositionChangeReason - 仓位变更原因

```
CashPositionChangeReason_Unknown = 0
CashPositionChangeReason_Trade = 1            # 交易
CashPositionChangeReason_Inout = 2            # 出入金 / 出入持仓

```

## SecType - 标的类别

```
SEC_TYPE_STOCK = 1                          # 股票
SEC_TYPE_FUND = 2                           # 基金
SEC_TYPE_INDEX = 3                          # 指数
SEC_TYPE_FUTURE = 4                         # 期货
SEC_TYPE_OPTION = 5                         # 期权
SEC_TYPE_CREDIT = 6                         # 信用交易
SEC_TYPE_BOND = 7                           # 债券
SEC_TYPE_BOND_CONVERTIBLE = 8               # 可转债
SEC_TYPE_CONFUTURE = 10                     # 虚拟合约

```

## AccountStatus - 交易账户状态

```
State_UNKNOWN = 0                        #未知
State_CONNECTING = 1                     #连接中
State_CONNECTED = 2                      #已连接
State_LOGGEDIN = 3                       #已登录
State_DISCONNECTING = 4                  #断开中
State_DISCONNECTED = 5                   #已断开
State_ERROR = 6                          #错误

```

## PositionSrc - 头寸来源(仅适用融券融券)

```
PositionSrc_Unknown = 0
PositionSrc_L1 = 1                      #普通池
PositionSrc_L2 = 2                      #专项池

```

## AlgoOrderStatus 算法单状态,暂停/恢复算法单时有效

```
AlgoOrderStatus_Unknown = 0,
AlgoOrderStatus_Resume = 1,                  #恢复母单
AlgoOrderStatus_Pause = 2,                   #暂停母单
AlgoOrderStatus_PauseAndCancelSubOrders = 3  #暂停母单并撤子单

```
     [ ** ](python_other_event.html#ontradedatadisconnected---交易通道网络连接断开事件) [ ** ](python_enum_constant.html#orderstatus---委托状态)
