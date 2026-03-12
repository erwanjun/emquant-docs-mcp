## 典型场景

### 空策略

```
//////////////////////////////////////////////////////////////////////////
//空策略
using GMSDK;

namespace example
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");
            //订阅行情数据
            Subscribe("SHSE.600000", "tick");
            return;
        }

        public override void OnTick(Tick tick)
        {
            System.Console.WriteLine("{0,-50}{1}", "代码", tick.symbol);
            System.Console.WriteLine("{0,-50}{1}", "时间", tick.createdAt);
            System.Console.WriteLine("{0,-50}{1}", "最新价", tick.price);
            System.Console.WriteLine("{0,-50}{1}", "开盘价", tick.open);
            System.Console.WriteLine("{0,-50}{1}", "最高价", tick.high);
            System.Console.WriteLine("{0,-50}{1}", "最低价", tick.low);
            System.Console.WriteLine("{0,-50}{1}", "成交总量", tick.cumVolume);
            System.Console.WriteLine("{0,-50}{1}", "成交总额/最新成交额,累计值", tick.cumAmount);
            System.Console.WriteLine("{0,-50}{1}", "合约持仓量(期), 累计值", tick.cumPosition);
            System.Console.WriteLine("{0,-50}{1}", "瞬时成交额", tick.lastAmount);
            System.Console.WriteLine("{0,-50}{1}", "瞬时成交量", tick.lastVolume);
            System.Console.WriteLine("{0,-50}{1}", "(保留)交易类型, 对应多开, 多平等类型", tick.tradeType);
            System.Console.WriteLine("{0,-50}{1}", "一档委买价", tick.quotes[0].bidPrice);
            System.Console.WriteLine("{0,-50}{1}", "一档委买量", tick.quotes[0].bidVolume);
            System.Console.WriteLine("{0,-50}{1}", "一档委卖价", tick.quotes[0].askPrice);
            System.Console.WriteLine("{0,-50}{1}", "一档委卖量", tick.quotes[0].askVolume);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097-8b27-11e8-b6af-94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2017-07-25 8:20:00", "2018-07-25 17:30:00");
            s.Run();
            System.Console.WriteLine("回测完成！");
            System.Console.Read();
        }
    }
}

```

### 定时任务

```
//////////////////////////////////////////////////////////////////////////
//定时任务
//策略描述：
    典型如选股交易。比如，策略每日收盘前10分钟执行：选股->决策逻辑->交易->退出。可能无需订阅实时数据。

using GMSDK;

namespace example_schedule
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");

            //设置定时任务
            Schedule("1d", "13:24:00");
            return;
        }

        //定时任务触发事件
        public override void OnSchedule(string data_rule, string timeRule)
        {
            //购买200股浦发银行股票
            GMData<Order> o = OrderValue("SHSE.600000", 200, OrderSide.OrderSide_Buy, OrderType.OrderType_Market, PositionEffect.PositionEffect_Open, 0);
            if (o.status == 0)   //该判断仅表示函数调用无异常
            {
                //
            }
        }

        //回测完成后收到绩效报告
        public override void OnBacktestFinished(Indicator indicator)
        {
            System.Console.WriteLine("OnBacktestFinished：");
            System.Console.WriteLine("{0,-50}{1}", "账号ID：", indicator.accountId);
            System.Console.WriteLine("{0,-50}{1}", "累计收益率：", indicator.pnlRatio);
            System.Console.WriteLine("{0,-50}{1}", "年化收益率：", indicator.pnlRatioAnnual);
            System.Console.WriteLine("{0,-50}{1}", "夏普比率：", indicator.sharpRatio);
            System.Console.WriteLine("{0,-50}{1}", "最大回撤：", indicator.maxDrawdown);
            System.Console.WriteLine("{0,-50}{1}", "风险比率：", indicator.riskRatio);
            System.Console.WriteLine("{0,-50}{1}", "开仓次数：", indicator.openCount);
            System.Console.WriteLine("{0,-50}{1}", "平仓次数：", indicator.closeCount);
            System.Console.WriteLine("{0,-50}{1}", "盈利次数：", indicator.winCount);
            System.Console.WriteLine("{0,-50}{1}", "亏损次数：", indicator.loseCount);
            System.Console.WriteLine("{0,-50}{1}", "胜率：", indicator.winRatio);
            System.Console.WriteLine("{0,-50}{1}", "指标创建时间：", indicator.createdAt);
            System.Console.WriteLine("{0,-50}{1}", "指标变更时间：", indicator.updatedAt);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097 - 8b27 - 11e8 - b6af - 94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2016-07-11 17:20:00", "2017-07-11 17:30:00");
            s.Run();
            System.Console.WriteLine("回测完成！");
            System.Console.Read();
        }
    }
}

```

### 数据事件驱动

```
//////////////////////////////////////////////////////////////////////////
//数据事件驱动
//策略描述：
//典型如选股交易策略。比如，策略每日收盘前10分钟执行：选股->决策逻辑->交易->退出。可能无需订阅实时数据

using GMSDK;

namespace example_dataevent
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件， 进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");

            //订阅浦发银行，bar频率为一天
            Subscribe("SHSE.600000", "1d");
            return;
        }

        //重写OnBar事件
        public override void OnBar(Bar bar)
        {
            System.Console.WriteLine("OnBar：");
            System.Console.WriteLine("{0, -50}{1}", "代码：", bar.symbol);
            System.Console.WriteLine("{0, -50}{1}", "bar的开始时间：", bar.bob);
            System.Console.WriteLine("{0, -50}{1}", "bar的结束时间：", bar.eob);
            System.Console.WriteLine("{0, -50}{1}", "开盘价：", bar.open);
            System.Console.WriteLine("{0, -50}{1}", "收盘价：", bar.close);
            System.Console.WriteLine("{0, -50}{1}", "最高价：", bar.high);
            System.Console.WriteLine("{0, -50}{1}", "最低价：", bar.low);
            System.Console.WriteLine("{0, -50}{1}", "成交量：", bar.volume);
            System.Console.WriteLine("{0, -50}{1}", "成交金额：", bar.amount);
            System.Console.WriteLine("{0, -50}{1}", "前收盘价：", bar.preClose);
            System.Console.WriteLine("{0, -50}{1}", "持仓量：", bar.position);
            System.Console.WriteLine("{0, -50}{1}", "bar频度：", bar.frequency);
        }
    }
    class Program
    { 
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097 - 8b27 - 11e8 - b6af - 94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2016-07-11 17:20:00", "2017-07-11 17:30:00");
            s.Run();
            System.Console.WriteLine("回测完成！");
            System.Console.Read();
        }
    }
}

```

### 默认交易账号

```
//////////////////////////////////////////////////////////////////////////
//默认账号交易
//策略描述：
//默认账号进行交易，下单时不指定account

using GMSDK;

namespace example_defaccount
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");
            Subscribe("SHSE.600000,SZSE.000001", "1d");

            return;
        }

        //重写OnBar事件
        public override void OnBar(Bar bar)
        {
            //不指定account 使用默认账户下单
            OrderVolume(bar.symbol, 200, OrderSide.OrderSide_Buy, OrderType.OrderType_Market, PositionEffect.PositionEffect_Open, 0);
        }

        //回测完成后收到绩效报告
        public override void OnBacktestFinished(Indicator indicator)
        {
            System.Console.WriteLine("OnBacktestFinished：");
            System.Console.WriteLine("{0,-50}{1}", "账号ID：", indicator.accountId);
            System.Console.WriteLine("{0,-50}{1}", "累计收益率：", indicator.pnlRatio);
            System.Console.WriteLine("{0,-50}{1}", "年化收益率：", indicator.pnlRatioAnnual);
            System.Console.WriteLine("{0,-50}{1}", "夏普比率：", indicator.sharpRatio);
            System.Console.WriteLine("{0,-50}{1}", "最大回撤：", indicator.maxDrawdown);
            System.Console.WriteLine("{0,-50}{1}", "风险比率：", indicator.riskRatio);
            System.Console.WriteLine("{0,-50}{1}", "开仓次数：", indicator.openCount);
            System.Console.WriteLine("{0,-50}{1}", "平仓次数：", indicator.closeCount);
            System.Console.WriteLine("{0,-50}{1}", "盈利次数：", indicator.winCount);
            System.Console.WriteLine("{0,-50}{1}", "亏损次数：", indicator.loseCount);
            System.Console.WriteLine("{0,-50}{1}", "胜率：", indicator.winRatio);
            System.Console.WriteLine("{0,-50}{1}", "指标创建时间：", indicator.createdAt);
            System.Console.WriteLine("{0,-50}{1}", "指标变更时间：", indicator.updatedAt);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097 - 8b27 - 11e8 - b6af - 94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2016-07-11 17:20:00", "2017-07-11 17:30:00");
            s.Run();
            System.Console.WriteLine("回测完成！");
            System.Console.Read();
        }
    }
}

```

### 显示指定交易账号

```
//////////////////////////////////////////////////////////////////////////
//显示指定交易账号
//策略描述：
//下单时指定交易账号，account参数传账号id或者账号标题

using GMSDK;

namespace example_defaccount
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");
            Subscribe("SHSE.600000,SZSE.000001", "1d");

            return;
        }

        //重写OnBar事件
        public override void OnBar(Bar bar)
        {
            //不指定account 使用默认账户下单
            OrderVolume(bar.symbol, 200, OrderSide.OrderSide_Buy, OrderType.OrderType_Market, PositionEffect.PositionEffect_Open, 0, ba8785aa-8641-11e8-98cb-7085c223669d);
        }

        //回测完成后收到绩效报告
        public override void OnBacktestFinished(Indicator indicator)
        {
            System.Console.WriteLine("OnIndicator：");
            System.Console.WriteLine("{0,-50}{1}", "账号ID：", indicator.accountId);
            System.Console.WriteLine("{0,-50}{1}", "累计收益率：", indicator.pnlRatio);
            System.Console.WriteLine("{0,-50}{1}", "年化收益率：", indicator.pnlRatioAnnual);
            System.Console.WriteLine("{0,-50}{1}", "夏普比率：", indicator.sharpRatio);
            System.Console.WriteLine("{0,-50}{1}", "最大回撤：", indicator.maxDrawdown);
            System.Console.WriteLine("{0,-50}{1}", "风险比率：", indicator.riskRatio);
            System.Console.WriteLine("{0,-50}{1}", "开仓次数：", indicator.openCount);
            System.Console.WriteLine("{0,-50}{1}", "平仓次数：", indicator.closeCount);
            System.Console.WriteLine("{0,-50}{1}", "盈利次数：", indicator.winCount);
            System.Console.WriteLine("{0,-50}{1}", "亏损次数：", indicator.loseCount);
            System.Console.WriteLine("{0,-50}{1}", "胜率：", indicator.winRatio);
            System.Console.WriteLine("{0,-50}{1}", "指标创建时间：", indicator.createdAt);
            System.Console.WriteLine("{0,-50}{1}", "指标变更时间：", indicator.updatedAt);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097 - 8b27 - 11e8 - b6af - 94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2016-07-11 17:20:00", "2017-07-11 17:30:00");
            s.Run();
            System.Console.WriteLine("回测完成！");
            System.Console.Read();
        }
    }
}

```

### 模式选择

```
//////////////////////////////////////////////////////////////////////////
//模式选择
//策略描述：
//策略支持两种运行模式，实时模式和回测模式，用户需要在运行策略时选择模式，实例化策略参数mode=MODE_BACKTEST 表示回测模式，mode=MODE_LIVE表示实时模式

using GMSDK;

namespace example
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");
            //订阅行情数据
            Subscribe("SHSE.600000", "tick");
            return;
        }

        public override void OnTick(Tick tick)
        {
            System.Console.WriteLine("{0,-50}{1}", "代码", tick.symbol);
            System.Console.WriteLine("{0,-50}{1}", "时间", tick.createdAt);
            System.Console.WriteLine("{0,-50}{1}", "最新价", tick.price);
            System.Console.WriteLine("{0,-50}{1}", "开盘价", tick.open);
            System.Console.WriteLine("{0,-50}{1}", "最高价", tick.high);
            System.Console.WriteLine("{0,-50}{1}", "最低价", tick.low);
            System.Console.WriteLine("{0,-50}{1}", "成交总量", tick.cumVolume);
            System.Console.WriteLine("{0,-50}{1}", "成交总额/最新成交额,累计值", tick.cumAmount);
            System.Console.WriteLine("{0,-50}{1}", "合约持仓量(期), 累计值", tick.cumPosition);
            System.Console.WriteLine("{0,-50}{1}", "瞬时成交额", tick.lastAmount);
            System.Console.WriteLine("{0,-50}{1}", "瞬时成交量", tick.lastVolume);
            System.Console.WriteLine("{0,-50}{1}", "(保留)交易类型, 对应多开, 多平等类型", tick.tradeType);
            System.Console.WriteLine("{0,-50}{1}", "一档委买价", tick.quotes[0].bidPrice);
            System.Console.WriteLine("{0,-50}{1}", "一档委买量", tick.quotes[0].bidVolume);
            System.Console.WriteLine("{0,-50}{1}", "一档委卖价", tick.quotes[0].askPrice);
            System.Console.WriteLine("{0,-50}{1}", "一档委卖量", tick.quotes[0].askVolume);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097-8b27-11e8-b6af-94c69161828a", StrategyMode.MODE_LIVE);
            s.Run();
            System.Console.Read();
        }
    }
}

```

### 数据研究

```
//////////////////////////////////////////////////////////////////////////
//数据研究
//策略描述：
//无需实时数据驱动策略，无需交易下单，只是取数据的场景

using GMSDK;

namespace example_datares
{
    public class MyStrategy : Strategy
    {
        public MyStrategy(string token, string strategyId, StrategyMode mode) : base(token, strategyId, mode) { }

        //重写OnInit事件，进行策略开发
        public override void OnInit()
        {
            System.Console.WriteLine("OnInit");

            GMDataList<Tick> ht = GMApi.HistoryTicks("SZSE.000002", "2017-07-11 10:20:00", "2017-07-11 10:30:00");
            if (ht.status == 0)
            {
                foreach (var tick in ht.data)
                {
                    System.Console.WriteLine("{0,-50}{1}", "代码", tick.symbol);
                    System.Console.WriteLine("{0,-50}{1}", "时间", tick.createdAt);
                    System.Console.WriteLine("{0,-50}{1}", "最新价", tick.price);
                    System.Console.WriteLine("{0,-50}{1}", "开盘价", tick.open);
                    System.Console.WriteLine("{0,-50}{1}", "最高价", tick.high);
                    System.Console.WriteLine("{0,-50}{1}", "最低价", tick.low);
                    System.Console.WriteLine("{0,-50}{1}", "成交总量", tick.cumVolume);
                    System.Console.WriteLine("{0,-50}{1}", "成交总额/最新成交额,累计值", tick.cumAmount);
                    System.Console.WriteLine("{0,-50}{1}", "合约持仓量(期), 累计值", tick.cumPosition);
                    System.Console.WriteLine("{0,-50}{1}", "瞬时成交额", tick.lastAmount);
                    System.Console.WriteLine("{0,-50}{1}", "瞬时成交量", tick.lastVolume);
                    System.Console.WriteLine("{0,-50}{1}", "(保留)交易类型, 对应多开, 多平等类型", tick.tradeType);
                    System.Console.WriteLine("{0,-50}{1}", "一档委买价", tick.quotes[0].bidPrice);
                    System.Console.WriteLine("{0,-50}{1}", "一档委买量", tick.quotes[0].bidVolume);
                    System.Console.WriteLine("{0,-50}{1}", "一档委卖价", tick.quotes[0].askPrice);
                    System.Console.WriteLine("{0,-50}{1}", "一档委卖量", tick.quotes[0].askVolume);
                }
            }
            return;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyStrategy s = new MyStrategy("27cbdfd8cd9b86dea554a5612baa4a8eee51af79", "536f1097-8b27-11e8-b6af-94c69161828a", StrategyMode.MODE_BACKTEST);
            s.SetBacktestConfig("2017-07-25 8:20:00", "2018-07-25 17:30:00");
            s.Run();
            System.Console.Read();
        }
    }
}

```
     ** ** ** ** ** **
