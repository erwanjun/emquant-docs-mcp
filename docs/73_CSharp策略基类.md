# 策略基类

## 基类原型

### 策略类简介

策略类集成了行情、交易和事件的接口，用户的策略都从此类继承实现自己的业务逻辑。每个进程只能实例化一个策略类对象。

### 策略类定义

```
public class Strategy
{
    //策略基类构造函数
    //token：
    //strategy_id：策略ID
    //mode：运行模式
    public Strategy(string token, string strategyId, int mode);

//=====================================策略参数类函数=====================================
    //添加参数
    public int AddParameters(Parameter param);

    //删除参数
    public int DelParameters(string keys);

    //获取标的
    public GMDataList<string> GetSymbols();

    //设置标的
    public int SetSymbols(string symbols);

    //设置回测参数
       public int SetBacktestConfig(string startTime, string endTime, double initialCash = 1000000, double transactionRatio = 1, double commissionRatio = 0, double slippageRatio = 0, int adjust = 0, int checkCache = 1);

    //设置参数
    public int SetParameters(List<Parameter> parameters);

//=======================================交易函数================================================
    //查询交易账号
    public GMDataList<Account> GetAccounts();

    //查询资金
    public GMDataList<Cash> GetCash(string account = null);

    //查询成交
    public GMDataList<ExecRpt> GetExecutionReports(string account = null);

    //查询委托
    public GMDataList<Order> GetOrders(string account = null);

    //查询持仓
    public GMDataList<Position> GetPosition(string account = null);

    //查询未结委托
    public GMDataList<Order> GetUnfinishedOrders(string account = null);

    //委托撤单， 
    public int OrderCancel(string clOrdIds);

    //撤销所有委托
    public void OrderCancelAll();

    //平当前所有可平持仓
    public GMDataList<Order> OrderCloseAll();

    //按总资产指定比例委托
    public GMData<Order> OrderPercent(string symbol, double percent, int side, int orderType, int positionEffect, double price = 0, string account = null);

    //调仓到目标持仓比例（总资产的比例）
    public GMData<Order> OrderTargetPercent(string symbol, double percent, int positionSide, int orderType, double price = 0, string account = null);

    //调仓到目标持仓额
    public GMData<Order> OrderTargetValue(string symbol, double value, int positionSide, int orderType, double price = 0, string account = null);

    //调仓到目标持仓量
    public GMData<Order> OrderTargetVolume(string symbol, int volume, int positionSide, int orderType, double price = 0, string account = null);

    //按指定价值委托
    public GMData<Order> OrderValue(string symbol, double value, int side, int orderType, int positionEffect, double price = 0, string account = null);

    //按指定量委托
    public GMData<Order> OrderVolume(string symbol, int volume, OrderSide side, OrderType orderType, PositionEffect positionEffect, double price = 0, string account = null);

//=====================================基础函数=================================
    //运行策略
    public int Run();

    //定时任务
    public int Schedule(string dataRule, string timeRule);

    //停止策略
    public int Stop();

    //当前事件
    public long Now();

    //设置token
    public int SetToken(string token);

    //设置运行模式
    public int SetMode(StrategyMode mode);

    //设置策略ID
    public int SetStrategyId(string strategyId);

    //查询指定账户状态
    public AccountStatus GetAccountStatus(string accountId);

    //查询所有账户状态
    public List<AccountStatus> GetAccountStatus()

//====================================数据函数=============================================
    //订阅行情
    public int Subscribe(string symbols, string frequency, bool unsubscribePrevious = false);

    //退订行情
    public int Unsubscribe(string symbols, string frequency);

//========================================事件函数==============================================
    //初始化完成
    public virtual void OnInit();

    //实盘账号状态变化
    public virtual void OnAccountStatus(AccountStatus accountStatus);

    //收到bar行情
    public virtual void OnBar(Bar bar);

    //cash发生变化
    public virtual void OnCashStatus(Cash order);

    //错误事件
    public virtual void OnError(int errorCode, string errorMsg);

    //执行回报
    public virtual void OnExecutionReport(ExecRpt rpt);

    //回测结束
    public virtual void OnBacktestFinished(Indicator indicator);

    //数据库已连接
    public virtual void OnMarketDataConnected();

    //数据库断开
    public virtual void OnMarketDataDisconnected();

    //委托发生变化
    public virtual void OnOrderStatus(Order order);

    //运行时参数发生变化
    public virtual void OnParameter(List<Parameter> param);

    //position发生变化
    public virtual void OnPosition(Position position);

    //定时任务触发
    public virtual void OnSchedule(string dataRule, string timeRule);

    //策略结束
    public virtual void OnStop();

    //收到tick行情
    public virtual void OnTick(Tick tick);

    //交易已连接
    public virtual void OnTradeDataConnected();

    //交易断开
    public virtual void OnTradeDataDisconnected();
}

```
     ** ** ** ** ** **
