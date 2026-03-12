# 枚举常量

## OrderStatus - 委托状态

```
enum OrderStatus
{
    OrderStatus_Unknown = 0,
    OrderStatus_New = 1,                   //已报
    OrderStatus_PartiallyFilled = 2,       //部成
    OrderStatus_Filled = 3,                //已成
    OrderStatus_Canceled = 5,              //已撤
    OrderStatus_Rejected = 8,              //已拒绝
    OrderStatus_PendingNew = 10,           //待报
    OrderStatus_Expired = 12,              //已过期

};

```

## OrderSide - 委托方向

```
enum OrderSide
{
    OrderSide_Unknown = 0,
    OrderSide_Buy = 1,         //买入
    OrderSide_Sell = 2,        //卖出
};

```

## sectype---标的类别

```
enum SecType
{
SEC_TYPE_STOCK = 1,         //股票
SEC_TYPE_FUND = 2,          //基金
SEC_TYPE_INDEX = 3,         //指数
SEC_TYPE_FUTURE = 4,        //期货
SEC_TYPE_OPTION = 5,        //期权
SEC_TYPE_CONFUTURE = 10     //虚拟合约
}

```

## OrderType - 委托类型

```
enum OrderType
{
    OrderType_Unknown = 0,
    OrderType_Limit = 1,         //限价委托
    OrderType_Market = 2,        //市价委托
};

```

## ExecType - 执行回报类型

```
enum ExecType
{
    ExecType_Unknown = 0,
    ExecType_Trade = 15,                   //成交
    ExecType_CancelRejected = 19,          //撤单被拒绝
};

```

## PositionEffect - 开平仓类型

```
enum PositionEffect
{
    PositionEffect_Unknown = 0,
    PositionEffect_Open = 1,              //开仓
    PositionEffect_Close = 2,             //平仓,具体语义取决于对应的交易所
    PositionEffect_CloseToday = 3,        //平今仓
    PositionEffect_CloseYesterday = 4,    //平昨仓
};

```

## PositionSide - 持仓方向

```
enum PositionSide
{
    PositionSide_Unknown = 0,
    PositionSide_Long = 1,    //多方向
    PositionSide_Short = 2,   //空方向
};

```

## OrderRejectReason - 订单拒绝原因

```
enum OrderRejectReason
{
    OrderRejectReason_Unknown = 0,                           //未知原因
    OrderRejectReason_RiskRuleCheckFailed = 1,               //不符合风控规则 
    OrderRejectReason_NoEnoughCash = 2,                      //资金不足
    OrderRejectReason_NoEnoughPosition = 3,                  //仓位不足
    OrderRejectReason_IllegalAccountId = 4,                  //非法账户ID
    OrderRejectReason_IllegalStrategyId = 5,                 //非法策略ID
    OrderRejectReason_IllegalSymbol = 6,                     //非法交易代码
    OrderRejectReason_IllegalVolume = 7,                     //非法委托量
    OrderRejectReason_IllegalPrice = 8,                      //非法委托价
    OrderRejectReason_AccountDisabled = 10,                  //交易账号被禁止交易
    OrderRejectReason_AccountDisconnected = 11,              //交易账号未连接
    OrderRejectReason_AccountLoggedout = 12,                 //交易账号未登录
    OrderRejectReason_NotInTradingSession = 13,              //非交易时段
    OrderRejectReason_OrderTypeNotSupported = 14,            //委托类型不支持
    OrderRejectReason_Throttle = 15,                         //流控限制
    OrderRejectReason_SymbolSusppended = 16,                 //交易代码停牌
    OrderRejectReason_Internal = 999,                        //内部错误

    CancelOrderRejectReason_OrderFinalized = 101,            //委托已完成
    CancelOrderRejectReason_UnknownOrder = 102,              //未知委托
    CancelOrderRejectReason_BrokerOption = 103,              //柜台设置
    CancelOrderRejectReason_AlreadyInPendingCancel = 104,    //委托撤销中
};

```

## CashPositionChangeReason - 仓位变更原因

```
enum CashPositionChangeReason
{
    CashPositionChangeReason_Unknown = 0,
    CashPositionChangeReason_Trade = 1,      //交易
    CashPositionChangeReason_Inout = 2,      //出入金/出入持仓
    CashPositionChangeReason_Dividend = 3,   //分红送股
};

```

## AccountState - 交易账户状态

```

enum AccountState
{
    State_UNKNOWN = 0,       //未知
    State_CONNECTING = 1,    //连接中
    State_CONNECTED = 2,     //已连接
    State_LOGGEDIN = 3,      //已登录
    State_DISCONNECTING = 4, //断开中
    State_DISCONNECTED = 5,  //已断开
    State_ERROR = 6          //错误
};

```

## StrategyMode - 策略模式

```

public enum StrategyMode
{
    MODE_UNDEF = 0,          //未定义， 策略不会运行
    MODE_LIVE = 1,           //实盘与仿真模式
    MODE_BACKTEST = 2        //回测模式
};

```

## Adjust - 复权方式

```
public enum Adjust
{
    ADJUST_NONE = 0,        //(不复权)
    ADJUST_PREV = 1,        //(前复权)
    ADJUST_POST = 2         //(后复权)
}

```
     ** ** ** ** ** **
