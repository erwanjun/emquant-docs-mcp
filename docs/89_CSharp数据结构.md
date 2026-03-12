# 数据结构

## 数据类

### Tick - Tick结构

逐笔行情数据

```
public class Tick
{
    public string symbol;                  //symbol

    public DateTime createdAt;             //时间
    public float price;                    //最新价
    public float open;                     //开盘价
    public float high;                     //最高价
    public float low;                      //最低价
    public double cumVolume;               //成交总量
    public double cumAmount;               //成交总金额/最新成交额，累计值
    public System.Int64 cumPosition;       //合约持仓量（期），累计值
    public double lastAmount;              //瞬时成交额
    public int lastVolume;                 //瞬时成交量
    public int tradeType;                  //交易类型，对应多开，多平等类型
    public Quote[] quotes;                 //报价, 下标从0开始，0-表示第一档，1-表示第二档，依次类推

};

```

#### 报价`Quote`

```
public class Quote
{
    public float bidPrice;            //本档委买价
    public System.Int64 bidVolume;    //本档委买量
    public float askPrice;            //本档委卖价
    public System.Int64 askVolume;    //本档委卖量
};

```

### Bar - Bar结构

bar数据是指各种频率的行情数据

```
public class Bar
{
    public string symbol;
    public DateTime bob;            //bar的开始时间
    public DateTime eob;            //bar的结束时间
    public float open;              //开盘价
    public float close;             //收盘价
    public float high;              //最高价
    public float low;               //<最低价
    public double volume;           //成交量
    public double amount;           //成交金额
    public float preClose;          //昨收盘价，只有日频数据赋值

    public System.Int64 position;   //持仓量
    public string frequency;        //bar频度
};

```

### SymbolInfo - 标的交易静态信息

```
public struct SymbolInfo
{
    //标的代码
    public string symbol;
    //证券品种大类
    public int secType1;
    //证券品种细类
    public int secType2;
    //板块
    public int board;
    //交易所代码
    public string exchange;
    //交易所标的代码
    public string secId;
    //交易所标的名称
    public string secName;
    //交易所标的简称
    public string secAbbr;
    //最小变动单位
    public double priceTick;
    //交易制度
    public int tradeN;
    //上市日期
    public DateTime listedDate;
    //退市日期
    public DateTime delistedDate;
    //标的资产
    public string underlyingSymbol;
    //行权方式
    public string optionType;
    //期权保证金计算参数1
    public double optionMarginRatio1;
    //期权保证金计算参数2
    public double optionMarginRatio2;
    //合约类型
    public string callOrPut;
    //可转债开始转股日期
    public DateTime conversionStartDate;
}

```

### Symbol - 标的交易信息

```
public struct Symbol
{
    public DateTime trade_date;
    // 合约调整
    public bool is_adjusted;
    // 是否停牌
    public bool is_suspended;
    // 持仓量
    public long position;
    // 结算价
    public double settle_price;
    // 昨结算价
    public double pre_settle;
    // 昨收盘价
    public double pre_close;
    // 涨停价
    public double upper_limit;
    // 跌停价
    public double lower_limit;
    // 换手率
    public double turn_rate;
    // 复权因子
    public double adj_factor;
    // 保证金比例
    public double margin_ratio;
    // 转股价
    public double conversion_price;
    // 行权价
    public double exercise_price;
    // 合约乘数
    public long multiplier;
    // 包含 info 中的字段
    public SymbolInfo info;
    // 是否ST
    public bool is_st;
    // 做市 市场分层 '0'-基础层，'1'-创新层，'2'-北交所
    public int market_level;
    // 做市 做市商数量 有做市商提供做市服务的证券，返回其做市商数量；没有做市商提供做市服务的返回0
    public int total_market_makers;
    // 做市 交易方式 'T'-协议交易方式，'M'-做市交易方式，'B'-集合竞价+连续竞价交易方式，'C'集合竞价交易方式，'P'-发行方式
    public string trade_type;
    // 做市 买数量单位 单笔做市买入申报数量是unit_volume_buy的整数倍
    public int unit_volume_buy;
    // 做市 卖数量单位 单笔做市卖出申报数量是unit_volume_sell的整数倍
    public int unit_volume_sell;
}

```

### TradeDate - 年度交易日历

```
public struct TradeDate
{
    //自然日期, 查询年份的自然日日期
    public DateTime date;
    //交易日期
    public DateTime tradeDate;
    //下一交易日
    public DateTime nextTradeDate;
    //上一交易日
    public DateTime preTradeDate;
}

```

### TradingSession - 交易时段

```
public struct TradingSession
{
    //交易时间
    public struct Session
    {
        public string start;
        public string end;
    }

    //标的代码
    public string symbol;
    //交易所代码
    public string exchange;
    //连续竞价时段
    public List<Session> timeTrading;
    //集合竞价时段
    public List<Session> timeAuctions;
}

```

### ContractExpireRestDays - 合约到期剩余天数

```
public struct ContractExpireRestDays
{
    //日期
    public string date;
    //标的代码
    public string symbol;
    //
    public string daysToExpire;
}

```

### IndustryCategory - 行业分类

```
public struct IndustryCategory
{
    // 行业代码
    public string industryCode;
    // 行业名称
    public string industryName;
}

```

### IndustryConstituent - 行业成分股

```
public struct IndustryConstituent
{
    // 行业代码
    public string industryCode;
    // 行业名称
    public string industryName;
    // 成分股票代码, 格式: exchange.secId
    public string symbol;
    // 成分股票名称
    public string secName;
    // 纳入日期, 本地时间
    public DateTime dateIn;
    // 剔除日期, 本地时间
    public DateTime dateOut;
}

```

### SymbolIndustry - 股票所属行业

```
public struct SymbolIndustry
{
    // 股票代码, 格式: exchange.secId
    public string symbol;
    // 股票名称
    public string secName;
    // 行业代码
    public string industryCode;
    // 行业名称
    public string industryName;
}

```

### SectorCategory - 板块分类

```
public struct  SectorCategory
{
    //版块代码
    public string sectorCode;
    //版块名称
    public string sectorName;
}

```

### SectorConstituent - 板块成分股

```
public struct SectorConstituent
{
    // 板块代码
    public string sectorCode;
    // 板块名称
   public string sectorName;
    // 股票代码, 格式: exchange.sec_id
  public  string symbol;
    // 成分股票名称
   public  string secName;
}

```

### SymbolSector - 股票所属板块

```
public struct SymbolSector
{
    // 股票代码, 格式: exchange.sec_id
    public string symbol;
    // 股票名称
    public string secName;
    // 板块代码
    public string sectorCode;
    // 板块名称
    public string sectorName;
}

```

### IndexConstituent - 指数成分股

```
public struct IndexConstituent
{
    // 指数代码
    public string index;
    // 成分股代码
    public string symbol;
    // 成分股权重
    public double weight;
    // 交易日期, 本地时间, 格式为: YYYY-MM-DD
    public DateTime date;
    //总市值
    public double marketValueTotal;
    //流通市值
    public double marketValueCirc;
}

```

### StockDividend - 股票分红送股信息

```
public struct StockDividend
{
    // 股票代码
    public string symbol;
    // 分配方案, 如现金分红, 送股, 配股, 转增
    public string schemeType;
    // 公告日, 本地时间
    public DateTime pubDate;
    // 除权除息日, 本地时间
    public DateTime exDate;
    // 股权登记日, 本地时间
    public DateTime equityRegDate;
    // 现金红利发放日(派息日), 本地时间, 格式为: YYYY-MM-DD
    public DateTime cashPayDate;
    // 送（转增）股份到账日, 本地时间, 格式为: YYYY-MM-DD
    public DateTime shareAcctDate;
    // 红股上市日, 送（转增）股份上市交易日, 本地时间, 格式为: YYYY-MM-DD
    public DateTime shareLstDate;
    // 税后红利（元/10股）
    public double cashAfTax;
    // 税前红利（元/10股）
    public double cashBfTax;
    // 送股比例, 10:X
    public double bonusRatio;
    // 转增比例, 10:X
    public double convertRatio;
    // 盈余公积金转增比例, 10:X
    public double surRsvRatio;
    // 资本公积金转增比例, 10:X
    public double capRsvRatio;
    // 股本基准日
    public string baseDate;
    // 股本基数(基准股本)
    public double baseShare;
    // 配股比例
    public double rationRatio;
    // 配股价格
    public double rationPrice;
}

```

### StockRation - 股票配股信息

```
public struct StockRation
{
    // 标的代码
    public string symbol;
    // 公告日
    public DateTime pubDate;
    //股权登记日
    public DateTime equityRegDate;
    //除权除息日
    public DateTime ex_date;
    //配股比例
    public double rationRatio;
    //配股价格
    public double rationPrice;
}

```

### AdjFactor - 股票复权因子

```
public struct AdjFactor
{
    // 交易日期
    public DateTime tradeDate;
    // 当日后复权因子, T日后复权因子=T-1日的收盘价/T日前收价
    public double adjFactorBwd;
    // 当日累计后复权因子, T日累计后复权因子=T日后复权因子*T-1日累计后复权因子
    // （第一个累计后复权因子=第一个后复权因子）
    public double adjFactorBwdAcc;
    // 当日前复权因子, T日前复权因子=T日后复权因子/复权基准日后复权因子
    public double adjFactorFwd;
    // 当日累计前复权因子, T日累计前复权因子=T日后复权因子
    // T-1日累计前复权因子=T日后复权因子*T-1日后复权因子
    // （第一个累计前复权因子=最新累计后复权因子）
    public double adjFactorFwdAcc;
}

```

### ShareholderNum - 股东户数

```
public struct ShareholderNum
{
    // 股票代码
    public string symbol ;
    // 股票名称
    public string secName;
    // 公告日期
    public DateTime pubDate ;
    // 截止日期
    public DateTime expiryDate ;
    // 股东总数
    public long totalShare ;
    // A股股东总数
    public long totalShareA ;
    // 流通B股股东总数
    public long totalShareB ;
    // 流通H股股东总数
    public long totalShareH ;
    // 其他股东户数
    public long otherShare ;
    // 优先股股东总数（表决权恢复）
    public long totalSharePfd ;
    // 股东户数（含融资融券）
    public long totalShareMgn ;
    // 股东户数（不含融资融券）
    public long totalShareNoMgn ;
}

```

### Shareholder - 十大股东

```
public struct Shareholder
{
    // 股票代码
    public string symbol;
    // 股票名称
    public string secName;
    // 公告日期
    public DateTime pubDate;
    // 截止日期
    public DateTime expiryDate;
    // 股东名称
    public string holderName;
    // 股东序号（名次）
    public int holderRank;
    // 股东类型
    public string holderType;
    // 股东性质
    public string holderAttr;
    // 股份类型(股份性质)
    public string shareType;
    // 持有数量（股）
    public double shareNum;
    // 持股比例1, 持股占总股本比例（%）
    public double shareRatio1;
    // 持股比例2, 持股占已上市流通股比例（%）
    public double shareRatio2;
    // 质押股份数量, 股权质押涉及股数（股）
    public double sharePledge;
    // 冻结股份数量, 股权冻结涉及股数（股）
    public double shareFreeze;
}

```

### ShareChange - 股本变动

```
public struct ShareChange
{
    // 股票代码
    public string symbol;
    // 公司名称
    public string companyName;
    // 发布日期
    public DateTime pubDate;
    // 股本变动日期
    public DateTime chgDate;
    // 股本变动原因
    public string chgReason;
    // 股本变动事件
    public string chgEvent;
    // 总股本, 未流通股份+已流通股份, 单位: 股
    public double shareTotal;
    // 未流通股份
    public double shareTotalNlf;
    // 发起人股份: 国有发起人股 + 发起社会法人股 + 其他发起人股份, 单位: 股
    public double shareProm;
    // 国有发起人股: 国家持股+国有法人股, 单位: 股
    public double sharePromState;
    // 国家股
    public double shareState;
    // 国有法人股
    public double shareStateLp;
    // 发起社会法人股: 境内社会法人股+境外法人股, 单位: 股
    public double sharePromSoc;
    // 境内社会法人股
    public double shareDcLp;
    // 境外法人股
    public double shareOsLp;
    // 其他发起人股份
    public double sharePromOther;
    // 募集人股份: 募集国家股+募集境内法人股+募集境外法人股, 单位: 股
    public double shareRs;
    // 募集国家股
    public double shareRsState;
    // 募集境内法人股: 募集境内国有法人股+募集境内社会法人股, 单位: 股
    public double shareRsDcLp;
    // 募集境内国有法人股
    public double shareRsStateLp;
    // 募集境内社会法人股
    public double shareRsSocLp;
    // 募集境外法人股
    public double shareRsOsLp;
    // 内部职工股
    public double shareEmpNlf;
    // 优先股
    public double sharePfdNlf;
    // 其他未流通股份
    public double shareOthNlf;
    // 流通股份
    public double shareCirc;
    // 无限售条件股份
    public double shareTtlUnl;
    // 人民币普通股（A股）
    public double shareAUnl;
    // 境内上市外资股（B股）
    public double shareBUnl;
    // 境外上市外资股（H股）
    public double shareHUnl;
    // 其他已流通股份
    public double shareOthUnl;
    // 有限售条件股份
    public double shareTtlLtd;
    // 一般有限售条件股份: 限售国家持股+ 限售国有法人持股+ 限售其他内资持股+ 限售外资持股+ 锁定股份+ 高管持股, 单位: 股
    public double shareGenLtd;
    // 限售国家持股
    public double shareStateLtd;
    // 限售国有法人持股
    public double shareStateLpLtd;
    // 限售其他内资持股: 限售境内非国有法人持股+限售境内自然人持股, 单位: 股
    public double shareOthDcLtd;
    // 限售境内非国有法人持股
    public double shareNstDcLpLtd;
    // 限售境内自然人持股
    public double shareDcNpLtd;
    // 限售外资持股: 限售境外法人持股+限售境外自然人持股, 单位: 股
    public double shareFornLtd;
    // 限售境外法人持股
    public double shareOsLpLtd;
    // 限售境外自然人持股
    public double shareOsNpLtd;
    // 锁定股份
    public double shareLkLtd;
    // 高管持股(原始披露)
    public double shareGmLtd;
    // 配售法人持股: 战略投资者配售股份+一般法人投资者配售+ 证券投资基金配售股份, 单位: 股
    public double sharePlcLpLtd;
    // 战略投资者配售股份
    public double sharePlcSiLtd;
    // 一般法人投资者配售股份
    public double sharePlcLpGenLtd;
    // 证券投资基金配售股份
    public double sharePlcFndLtd;
    // 限售流通A股
    public double shareALtd;
    // 限售流通B股
    public double shareBLtd;
    // 限售流通H股
    public double shareHLtd;
    // 其他限售股份
    public double shareOthLtd;
    // 变动股份上市日
    public DateTime shareListDate;
}

```

### FundamentalsBalance - 资产负债表

```
public struct FundamentalsBalance
{
    // 股票代码
    public string symbol;
    // 发布日期
    // 在指定时间段[开始时间,结束时间]内的最新发布日期,
    // 若数据类型选择合并原始(data_type=101)，则返回原始发布的发布日期
    // 若数据类型选择合并调整(data_type=102)，则返回调整后最新发布日期
    public DateTime pubDate;
    // 报告截止日期，财报统计的最后一天
    public DateTime rptDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 资产负债表
    public Dictionary<string, string> data;
}

```

### FundamentalsCashflow - 利润表

```
public struct FundamentalsCashflow
{
    // 股票代码
    public string symbol;
    // 发布日期
    // 在指定时间段[开始时间,结束时间]内的最新发布日期,
    // 若数据类型选择合并原始(data_type=101)，则返回原始发布的发布日期
    // 若数据类型选择合并调整(data_type=102)，则返回调整后最新发布日期
    public DateTime pubDate;
    // 报告截止日期，财报统计的最后一天
    public DateTime rptDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 利润表
    public Dictionary<string, string> data;
}

```

### FundamentalsIncome - 现金流量表

```
public struct FundamentalsIncome
{
    // 股票代码
    public string symbol;
    // 发布日期
    // 在指定时间段[开始时间,结束时间]内的最新发布日期,
    // 若数据类型选择合并原始(data_type=101)，则返回原始发布的发布日期
    // 若数据类型选择合并调整(data_type=102)，则返回调整后最新发布日期
    public DateTime pubDate;
    // 报告截止日期，财报统计的最后一天
    public DateTime rptDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 现金流量表
    public Dictionary<string, string> data;
}

```

### FinancePrime - 财务主要指标

```
public struct FinancePrime
{
    // 股票代码
    public string symbol;
    // 发布日期
    // 在指定时间段[开始时间,结束时间]内的最新发布日期,
    // 若数据类型选择合并原始(data_type=101)，则返回原始发布的发布日期
    // 若数据类型选择合并调整(data_type=102)，则返回调整后最新发布日期
    public DateTime pubDate;
    // 在指定时间段[开始时间,结束时间]内的报告截止日期，
    // 报告截止日期，财报统计的最后一天
    public DateTime rptDate;
    // 报表类型
    public int rptType;
    // 数据类型
    public int dataType;
    // 相应指定查询 fields字段的值. 字典key值请参考 财务主要指标
    public  Dictionary<string, string> data;
}

```

### FinanceDeriv - 财务衍生指标

```
public struct FinanceDeriv
{
    // 股票代码
    public string symbol;
    // 发布日期
    // 在指定时间段[开始时间,结束时间]内的最新发布日期,
    // 若数据类型选择合并原始(data_type=101)，则返回原始发布的发布日期
    // 若数据类型选择合并调整(data_type=102)，则返回调整后最新发布日期
    public DateTime pubDate;
    // 在指定时间段[开始时间,结束时间]内的报告截止日期，
    // 报告截止日期，财报统计的最后一天
    public DateTime rptDate;
    // 报表类型
    public int rptType;
    // 数据类型
    public int dataType;
    // 相应指定查询 fields字段的值. 字典key值请参考 财务衍生指标
    public Dictionary<string, string> data;
}

```

### DailyValuation - 交易衍生指标-估值类

```
public struct DailyValuation
{
    // 股票代码
    public string symbol;
    // 交易日期
    public DateTime tradeDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 交易衍生指标-估值类
    public Dictionary<string, string> data;
}

```

### DailyMktvalue - 交易衍生指标-市值类

```
public struct DailyMktvalue
{
    // 股票代码
    public string symbol;
    // 交易日期
    public DateTime tradeDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 交易衍生指标-市值类
    public Dictionary<string, string> data;
}

```

### DailyBasic - 交易衍生指标-基础类

```
public struct DailyBasic
{
    // 股票代码
    public string symbol;
    // 交易日期
    public DateTime tradeDate;
    // 相应指定查询 fields字段的值. 字典key值请参考 交易衍生指标-基础类
    public Dictionary<string, string> data;
}

```

### ContinuousContractsInfo - 期货连续合约映射

```
public struct ContinuousContractsInfo
{
    // 标的代码
    public string symbol;
    // 交易日期
    public DateTime tradeDate;
}

```

### FutContractInfo - 期货标准品种信息

```
public struct FutContractInfo
{
    // 交易品种  --交易品种名称，如：沪深300指数，铝
    public string productName;
    // 交易代码  --交易品种代码，如：IF，AL
    public string productCode;
    // 合约标的 --如：SHSE.000300， AL
    public string underlyingSymbol;
    // 合约乘数  --如：200，5
    public int multiplier;
    // 交易单位  --如：每点人民币200元，5吨/手
    public string tradeUnit;
    // 报价单位   --如：指数点，元（人民币）/吨
    public string priceUnit;
    // 价格最小变动单位  --如：0.2点，5元/吨
    public string priceTick;
    // 合约月份  --如：当月、下月及随后两个季月，1～12月
    public string deliveryMonth;
    // 交易时间  --如：“9:30-11:30，13:00-15:00”，“上午9:00－11:30 ，下午1:30－3:00和交易所规定的其他交易时间”
    public string tradeTime;
    // 涨跌停板幅度  --每日价格最大波动限制，如：“上一个交易日结算价的±10%”，“上一交易日结算价±3%”
    public string priceRange;
    // 最低交易保证金  --交易所公布的最低保证金比例，如：“合约价值的8%”，“合约价值的5%”
    public string minimumMargin;
    // 最后交易日   -- 如：“合约到期月份的第三个星期五，遇国家法定假日顺延”，“合约月份的15日（遇国家法定节假日顺延，春节月份等最后交易日交易所可另行调整并通知）”
    public string lastTradeDate;
    // 交割日期  --如：“同最后交易日”，“最后交易日后连续三个工作日”
    public string deliveryDate;
    // 交割方式  --如：现金交割，实物交割
    public string deliveryMethod;
    // 交易所名称 --上市交易所名称，如：中国金融期货交易所，上海期货交易所
    public string exchangeName;
    // 交易所代码  --上市交易所代码，如：CFFEX，SHFE
    public string exchange;

}

```

### FutTransactionRanking - 期货每日成交持仓排名

```
public struct FutTransactionRanking
{
// 期货合约代码  --必填，使用时参考symbol
public string symbol;
    // 交易日期  --
    public DateTime tradeDate;
    // 期货公司会员简称
    public string memberName;
    // 排名指标
    public string indicator;
    // 排名指标数值  --单位：手。视乎所选的排名指标indicator，分别为：成交量（indicator为'volume'时）持买单量（indicator为'long'时）持卖单量（indicator为‘short’时）
    public int indicatorNumber;
    // 排名指标比上交易日增减  --单位：手
    public int indicatorChange;
    // 排名名次
    public int ranking;
    // 排名名次比上交易日增减
    public int rankingChange;
    // 判断 ranking_change 的值是否为空
    public bool rankingChangeIsNull;
}

```

### WarehouseReceiptInfo - 期货仓单数据

```
public struct WarehouseReceiptInfo
{
    // 交易日期 --
    public DateTime tradeDate;
    // 期货交易所代码 --期货品种对应交易所代码，如：CFFEX，SHFE
    public string exchange;
    // 期货交易所名称 --上市交易所名称，如：中国金融期货交易所，上海期货交易所
    public string exchangeName;
    // 交易代码 --交易品种代码，如：IF，AL
    public string productCode;
    // 交易品种 --交易品种名称，如：沪深300指数，铝
    public string productName;
    // 注册仓单数量 --
    public int onWarrant;
    // 仓单单位 -- 仅支持郑商所品种
    public string warrantUnit;
    // 仓库名称 --
    public string warehouse;
    // 期货库存 --
    public int futureInventory;
    // 期货库存增减 --
    public int futureInventoryChange;
    // 可用库容量 --
    public int warehouseCapacity;
    // 可用库容量增减 --
    public int warehouseCapacityChange;
    // 库存小计 --
    public int inventorySubtotal;
    // 库存小计增减 --
    public int inventorySubtotalChange;
    // 有效预报 --仅支持郑商所品种
    public int effectiveForecast;
    // 升贴水 --
    public int premium;
}

```

### TransactionRankingInfo - 期货每日成交持仓排名

```
public struct TransactionRankingInfo
{
    // 沽购类型
    public string callOrPut;
    // 交易日期
    public string tradeDate;
    // 会员公司简称
    public string memberName;
    // indicator_number :排名指标数值 --单位：手。视乎所选的排名指标indicator，分别为：
    // 成交量（indicator为'volume'时）
    // 持买单量（indicator为'long'时）
    // 持卖单量（indicator为‘short’时）
    public int indicatorNumber;
    // 排名指标比上交易日增减 --单位：手
    public int indicatorChange;
    // 排名名次 --指标具体排名
    public int ranking;
    // 排名名次比上交易日增减
    public int rankingChange;
}

```

### EtfConstituents - ETF基金成分股

```
public struct EtfConstituents
{
    // ETF代码
    public string etf;
    // ETF名称
    public string etfName;
    // 交易日期
    public DateTime tradeDate;
    // 成分股代码
    public string symbol;
    // 股票数量
    public double amount;
    // 现金替代标志
    public string cashSubsType;
    // 固定替代金额
    public double cashSubsSum;
    // 现金替代溢价比例 --单位：%
    public double cashPremiumRate;
}

```

### PortfolioStockInfo - 基金资产组合（股票投资组合）

```
public struct PortfolioStockInfo
{
    // 基金代码  --查询资产组合的基金代码
    public string fund;
    // 基金名称
    public string fundName;
    // 公告日期  --在指定时间段[开始时间,结束时间]内的公告日期
    public DateTime pubDate;
    // 报告期 -- 持仓截止日期
    public DateTime periodEnd;
    // 股票代码
    public string symbol;
    // 股票名称
    public string secName;
    // 持仓股数
    public double holdShare;
    // 持仓市值
    public double holdValue;
    // 占净值比例  --单位：%
    public double nvRate;
    // 占总股本比例 --单位：%
    public double ttlShareRate;
    // 占流通股比例 --单位：%s
    public double circShareRate;
}

```

### PortfolioBondInfo - 基金资产组合（债券投资组合）

```
public struct PortfolioBondInfo
{
    // 基金代码  --查询资产组合的基金代码
   public  string fund;
    // 基金名称
    public string fundName;
    // 公告日期  --在指定时间段[开始时间,结束时间]内的公告日期
    public DateTime pubDate;
    // 报告期 -- 持仓截止日期
    public DateTime periodEnd;
    // 债券代码
    public string symbol;
    // 债券名称
    public string secName;
    // 持仓数量
    public double holdShare;
    // 持仓市值
    public double holdValue;
    // 占净值比例 --单位：%
    public double nvRate;
}

```

### PortfolioFundInfo - 基金资产组合（基金投资组合）

```
public struct PortfolioFundInfo
{
    // 基金代码  --查询资产组合的基金代码
   public string fund;
    // 基金名称
    public string fundName;
    // 公告日期  --在指定时间段[开始时间,结束时间]内的公告日期
    public DateTime pubDate;
    // 报告期 -- 持仓截止日期
    public DateTime periodEnd;
    // 基金代码
    public string symbol;
    // 基金名称
    public string secName;
    // 持有份额
    public double holdShare;
    // 期末市值
    public double holdValue;
    // 占净值比例 --单位：%
    public double nvRate;
}

```

### NetValueInfo - 基金净值

```
public struct NetValueInfo
{
    // 基金代码  --查询净值的基金代码
    public string fund;
    // 交易日期
    public DateTime tradeDate;
    // 单位净值  --T日单位净值是每个基金份额截至T日的净值（也是申赎的价格）
    public double unitNv;
    // 累计单位净值  --T日累计净值是指，在基金成立之初投资该基金1元钱，在现金分红方式下，截至T日账户的净值
    public double unitNvAccu;
    // 复权单位净值  --T日复权净值是指，在基金成立之初投资该基金1元钱，在分红再投资方式下，截至T日账户的净值
    public double unitNvAdj;
}

```

### FndAdjFactorInfo - 基金复权因子

```
public struct FndAdjFactorInfo
{
    // 交易日期    --最新交易日的日期
    public DateTime tradeDate;
    // 当日后复权因子 --T日后复权因子=T-1日的收盘价/T日前收价
    //public double adjFactorBwd;
    // 当日累计后复权因子  --T日累计后复权因子=T日后复权因子*T-1日累计后复权因子（第一个累计后复权因子=第一个后复权因子）
    public double adjFactorBwdAcc;
    // 当日前复权因子   --T日前复权因子=T日后复权因子/复权基准日后复权因子
    public double adjFactorFwd;
    // 当日累计前复权因子  --T日累计前复权因子=T日后复权因子 T-1日累计前复权因子=T日后复权因子*T-1日后复权因子（第一个累计前复权因子=最新累计后复权因子）
    //public double adjFactorFwdAcc;
}

```

### FndDividendInfo - 基金分红信息

```
public struct FndDividendInfo
{
    // 基金代码   --查询分红信息的基金代码
    public string fund;
    // 公告日
    public DateTime pubDate;
    // 方案进度
    public string eventProgress;
    // 派息比例 --10:X，每10份税前分红
    public double dvdRatio;
    // 分配收益基准日
    public DateTime dvdBaseDate;
    // 权益登记日
    public DateTime rtRegDate;
    // 实际除息日
    public DateTime exActDate;
    // 场内除息日
    public DateTime exDvdDate;
    // 场内红利发放日
    public DateTime payDvdDate;
    // 场内红利款账户划出日
    public DateTime transDvdDate;
    // 红利再投资确定日
    public DateTime reinvestCfmDate;
    // 红利再投资份额到账日
    public DateTime riShrArrDate;
    // 红利再投资赎回起始日
    public DateTime riShrRdmDate;
    // 可分配收益 --单位：元
    public double earnDistr;
    // 本期实际红利发放 --单位：元
    public double cashPay;
    // 基准日基金份额净值
    public double baseUnitNv;
}

```

### SplitInfo - 基金拆分折算信息

```
public struct SplitInfo
{
    // 基金代码
    public string fund;
    // 公告日
    public DateTime pubDate;
    // 拆分折算类型
    public string splitType;
    // 拆分折算比例
    public double splitRatio;
    // 拆分折算基准日
    public DateTime baseDate;
    // 拆分折算场内除权日
    public DateTime exDate;
    // 基金份额变更登记日
    public DateTime shareChangeRegDate;
    // 基金披露净值拆分折算日
    public DateTime nvSplitPubDate;
    // 权益登记日
    public DateTime rtRegDate;
    // 场内除权日(收盘价)
    public DateTime exDateClose;
}

```

### ConversionPrice - 可转债转股价变动信息

```
public struct ConversionPrice
{
    // 公告日期
    public DateTime pubDate;
    // 转股价格生效日期
    public DateTime effectiveDate;
    // 执行日期
    public DateTime executionDate;
    // 转股价格 --单位：元
    public double conversionPrice;
    // 转股比例 --单位：%
    public double conversionRate;
    // 单位：股
    public double conversionVolume;
    // 累计转股金额 --单位：万元，累计转债已经转为股票的金额，累计每次转股金额
    public double conversionAmountTotal;
    // 债券流通余额 --单位：万元
    public double bondFloatAmountRemain;
    // 事件类型  --初始转股价，调整转股价，修正转股价
    public string eventType;
    // 转股价变动原因
    public string changeReason;
}

```

### CallInfo - 可转债赎回信息

```
public struct CallInfo
{
    // 公告日 --赎回公告日
    public DateTime pubDate;
    // 赎回日 --发行人行权日（实际），公布的赎回日如遇节假日会顺延为非节假日
    public DateTime callDate;
    // 赎回登记日 --理论登记日，非节假日
    public DateTime recordDate;
    // 赎回资金到账日 --投资者赎回款到账日
    public DateTime cashDate;
    // 赎回类型 --部分赎回，全部赎回
    public string callType;
    // 赎回原因 --1:满足赎回条件，2:强制赎回，3:到期赎回
    public string callReason;
    // 赎回价格 --单位：元/张，每百元面值赎回价格（元），债券面值 加当期应计利息（含税）
    public double callPrice;
    // 赎回金额
    public double callAmount;
    // 是否包含利息  -- 0:不包含，1:包含
    public bool interestIncluded;
}

```

### PutInfo - 可转债回售信息

```
public struct PutInfo
{
    // 公告日 --赎回公告日
    public DateTime pubDate;
    // 回售起始日 --投资者行权起始日
    public DateTime putStartDate;
    // 回售截止日 --投资者行权截止日
    public DateTime putEndDate;
    // 回售资金到账日 --投资者回售款到账日
    public DateTime cashDate;
    // 回售原因 --1:满足回售条款，2:满足附加回售条款
    public string putReason;
    // 回售价格 --单位：元/张，每百元面值回售价格（元），债券面值 加当期应计利息（含税）
    public double putPrice;
    // 回售金额
    public double putAmount;
    // 是否包含利息  -- 0:不包含，1:包含
    public bool interestIncluded;
}

```

### AmountChange - 可转债剩余规模变动

```
public struct AmountChange
{
    // 公告日
    public DateTime pubDate;
    // 变动类型 --首发、增发、转股 、赎回、回售(注销)、到期
    public string changeType;
    // 变动日期
    public DateTime changeDate;
    // 本次变动金额 --单位：万元
    public double changeAmount;
    // 剩余金额 --变动后金额，单位：万元
    public double remainAmount;
}

```

### OptContractInfo - 期权标的基础信息

```
public struct OptContractInfo
{
    // 交易代码
    public string productCode;
    // 合约标的物名称
    public string underlying;
    // 合约乘数
    public int multiplier;
    // 交易单位
    public string tradeUnit;
    // 报价单位
    public string priceUnit;
    // 价格最小变动单位
    public double priceTick;
    // 合约月份
    public string deliveryMonth;
    // 交易时间
    public string tradeTime;
    // 涨跌幅限制
    public string priceRange;
    // 行权方式
    public string optionType;
    // 行权价格
    public string exercisePriceRule;
    // 最后交易日
    public string lastTradeDate;
    // 交割方式
    public string deliveryMethod;
    // 交易所名称
    public string exchangeName;
    // 交易所代码
    public string exchange;
}

```

### RiskValueInfo - 期权波动率

```
public struct RiskValueInfo
{
    // 交易日期
    public string tradeDate;
    // Delta
    public double delta;
    // Theta
    public double theta;
    // Gamma
    public double gamma;
    // Vega
    public double vega;
    // Rho
    public double rho;
    // 隐含波动率
    public double iv;
}

```

### GetSymbolsByInAtOutReq - 期权档位合约信息

```
public struct GetSymbolsByInAtOutReq
{
    // 合约标的物
    // 参数用法说明:
    // 必填，标的物symbol，全部大写，不指定具体到期月份，
    // 标的物为商品期货的，可参考主力合约代码，如：'CZCE.CF'
    // 标的物为股指的，可填：'CFFEX.IO'，'CFFEX.MO'
    // 标的物为ETF的，可填ETF的symbol，如：'SHSE.510050'
    public string underlyingSymbol;
    // 沽购类型
    // 参数用法说明:
    // 沽购类型，
    // 认购期权（看涨期权，买权）：'C'
    // 认沽期权（看跌期权，卖权）：'P'
    // 默认None表示不区分沽购类型，同时包括认购和认沽
    public string callOrPut;
    // 合约月份
    // 参数用法说明:
    // 合约月份，按到期月份从近至远从小到大排序，支持最近交割的4个月份
    // 可选1，2，3，4
    // 默认None为全部月份
    public int executeMonth;
    // 档位计数
    // 参数用法说明:
    // 档位计数，实值档位为正，虚值档位为负，平值为0，
    // 默认None时为所有档位（含平值）
    public int inAtOut;
    // 交易日期
    // 参数用法说明:
    // 查询时间, 本地时间, 格式为: YYYY-MM-DD
    // 为空时, 表示当前日期
    public string tradeDate;
    // 标的物价格
    // 参数用法说明:
    // 标的物价格，只能输入自定义具体价格
    public double s;
    // 标的物价格类型
    // 参数用法说明:
    // 标的物价格s为None时，此参数才生效。'pre_close'为昨收价（默认），'open'为今开价，'last'为最新价，（3种价格均相对于trade_date时间，trade_date不含分钟就取当日
    // 收盘价，trade_date包含分钟就取该1分钟bar的close）默认None为昨收价。
    public string sType;
    // 调整合约
    // 参数用法说明:
    // 表示是否过滤除权后的调整合约，'M'表示不返回调整合约，只返回标准合约（默认）'A'表示只返回调整合约 ''表示不做过滤都返回
    // 默认None为只返回标准合约。
    public string adjustFlag;
}

```
     ** ** ** ** ** **
