## 交易类

### Account - 账户结构

```
public class Account
{
    public string accountId;              //账号ID
    public string accountName;            //账户登录名
    public string title;                  //账号名称
    public string intro;                  //账号描述
    public string comment;                //账号备注
};

```

### AccountStatus - 账户状态结构

```
public class AccountStatus
{
    public string accountId;             //账号ID
    public string accountName;           //账户登录名
    public int state;                    //账户状态
    public int errorCode;                //错误码
    public string errorMsg;              //错误信息
};

```

### Order - 委托结构

```
public class Order
{
    public string strategyId;                     //策略ID                   
    public string accountId;                      //账号ID                                      
    public string accountName;                    //账户登录名                                  
    public string clOrdId;                        //委托客户端ID        
    public string orderId;                        //委托柜台ID                                  
    public string exOrdId;                        //委托交易所ID                                
    public string symbol;                         //symbol                                      
    public int side;                              //买卖方向，取值参考enum OrderSide            
    public int positionEffect;                    //开平标志，取值参考enum PositionEffect       
    public int positionSide;                      //持仓方向，取值参考enum PositionSide         

    public int orderType;                         //委托类型，取值参考enum OrderType            
    public int orderDuration;                     //委托时间属性，取值参考enum OrderDuration    
    public int orderQualifier;                    //委托成交属性，取值参考enum OrderQualifier   
    public int orderSrc;                          //委托来源，取值参考enum OrderSrc             

    public int status;                            //委托状态，取值参考enum OrderStatus          
    public int ordRejReason;                      //委托拒绝原因，取值参考enum OrderRejectReason
    public string ordRejReasonDetail;             //委托拒绝原因描述                            

    public double price;                          //委托价格                                    
    public double stopPrice;                      //委托止损/止盈触发价格                       

    public int orderStyle;                        //委托风格，取值参考 enum OrderStyle          
    public Int64 volume;                          //委托量                                      
    public double value;                          //委托额                                      
    public double percent;                        //委托百分比                                  
    public Int64 targetVolume;                    //委托目标量                                  
    public double targetValue;                    //委托目标额                                  
    public double targetPercent;                  //委托目标百分比                              

    public Int64 filledVolume;                    //已成量                                      
    public double filledVwap;                     //已成均价                                    
    public double filledAmount;                   //已成金额                                    
    public double filledCommission;               //已成手续费                                  

    public DateTime createdAt;                    //委托创建时间                                
    public DateTime updatedAt;                    //委托更新时间  
};

```

### ExecRpt - 回报结构

```
public class ExecRpt
{
    public string strategyId;                  //策略ID                
    public string accountId;                   //账号ID                                                       
    public string accountName;                 //账户登录名                                                                                                    
    public string clOrdId;                     //委托客户端ID                                                                                                  
    public string orderId;                     //委托柜台ID                                                                                                    
    public string execId;                      //委托回报ID                                                                                                    
    public string symbol;                      //symbol                                                                                                        

    public int positionEffect;                 //开平标志，取值参考enum PositionEffect                                                                         
    public int side;                           //买卖方向，取值参考enum OrderSide                                                                              
    public int ordRejReason;                   //委托拒绝原因，取值参考enum OrderRejectReason                                                                  
    public string ordRejReasonDetail;          //委托拒绝原因描述                                                                                              
    public int execType;                       //执行回报类型, 取值参考enum ExecType                                                                           

    public double price;                       //委托成交价格                                                                                                  
    public Int64 volume;                       //委托成交量                                                                                                    
    public double amount;                      //委托成交金额                                                                                                  
    public double commission;                  //委托成交手续费                                                                                                
    public double cost;                        //委托成交成本金额  
    public DateTime createdAt;                 //回报创建时间

};

```

### Cash - 资金结构

```
public class Cash
{
    public string accountId;                   //账号ID               
    public string accountName;                 //账户登录名                                                                   

    public int currency;                       //币种                                                                         

    public double nav;                         //净值(cum_inout + cum_pnl + fpnl - cum_commission)                            
    public double pnl;                         //净收益(nav-cum_inout)                                                        
    public double fpnl;                        //浮动盈亏(sum(each position fpnl))                                            
    public double frozen;                      //持仓占用资金                                                                 
    public double orderFrozen;                 //挂单冻结资金                                                                 
    public double available;                   //可用资金                                                                     

    public double balance;                     //资金余额                                                                     

    public double cumInout;                    //累计出入金                                                                   
    public double cumTrade;                    //累计交易额                                                                   
    public double cumPnl;                      //累计平仓收益(没扣除手续费)                                                   
    public double cumCommission;               //累计手续费                                                                   

    public double lastTrade;                   //上一次交易额                                                                 
    public double lastPnl;                     //上一次收益                                                                   
    public double lastCommission;              //上一次手续费                                                                 
    public double lastInout;                   //上一次出入金                                                                 
    public int changeReason;                   //资金变更原因，取值参考enum CashPositionChangeReason                 
    public string changeEventId;               //触发资金变更事件的ID     

    public DateTime createdAt;                 //资金初始时间
    public DateTime updatedAt;                 //资金变更时间

};

```

### Position - 持仓结构

```
public class Position
{
    public string accountId;                //账号ID                            
    public string accountName;              //账户登录名                                                                                       

    public string symbol;                   //symbol                                       
    public int side;                        //持仓方向，取值参考enum PositionSide          
    public Int64 volume;                    //总持仓量; 昨持仓量(volume-volume_today)                                                          
    public Int64 volumeToday;               //今日持仓量                                                                                       
    public double vwap;                     //持仓均价                                                                                         
    public double amount;                   //持仓额(volume*vwap*multiplier)                                                                   

    public double price;                    //当前行情价格                                                                                     
    public double fpnl;                     //持仓浮动盈亏((price-vwap)*volume*multiplier)                                                     
    public double cost;                     //持仓成本(vwap*volume*multiplier*margin_ratio)                                                    
    public Int64 orderFrozen;               //挂单冻结仓位                                                                                     
    public Int64 orderFrozenToday;          //挂单冻结今仓仓位                                                                                 
    public Int64 available;                 //非挂单冻结仓位(volume-order_frozen); 可平昨仓位(available-available_today)                           
    public Int64 availableToday;           //非挂单冻结今仓位(volume_today-order_frozen_today)                                                     
    public Int64 availableNow;             //当前可用仓位      

    public double lastPrice;                //上一次成交价                                                                                     
    public Int64 lastVolume;                //上一次成交量                                                                                     
    public Int64 lastInout;                 //上一次出入持仓量                                                                                 
    public int changeReason;                //仓位变更原因，取值参考enum CashPositionChangeReason 
    public string changeEventId;            //触发资金变更事件的ID                                                                             

    public int hasDividend;                 //持仓区间有分红配送   
    public DateTime createdAt;              //建仓时间（实盘不支持）
    public DateTime updatedAt;              //仓位变更时间（实盘不支持）

};

```

### Indicator - 绩效指标结构

```
public class Indicator
{
    public string accountId;               //账号ID
    public double pnlRatio;                //累计收益率(pnl/cum_inout)
    public double pnlRatioAnnual;          //年化收益率
    public double sharpRatio;              //夏普比率
    public double maxDrawdown;             //最大回撤
    public double riskRatio;               //风险比率
    public int openCount;                  //开仓次数
    public int closeCount;                 //平仓次数
    public int winCount;                   //盈利次数
    public int loseCount;                  //亏损次数
    public double winRatio;                //胜率

    public DateTime createdAt;             //指标创建时间
    public DateTime updatedAt;             //指标变更时间
};

```

### Parameter - 动态参数结构

```

public class Parameter
{
    public string key;                    //参数键
    public double value;                  //参数值
    public double min;                    //可设置的最小值
    public double max;                    //可设置的最大值
    public string name;                   //参数名
    public string intro;                  //参数说明
    public string group;                  //组名
    public bool readonlyFlag;             //是否只读
};

```
     ** ** ** ** ** **
