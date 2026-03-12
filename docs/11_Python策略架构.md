# 策略程序架构

## 东方财富量化策略程序初始化

通过[init函数](python_basic.html#init---初始化策略)初始化策略,策略启动即会自动执行。在init函数中可以：

- 

定义全局变量
通过添加[context](python_concept.html#context---上下文对象)包含的属性可以定义全局变量，如context.x,该属性可以在全文中进行传递。

- 

定义调度任务
可以通过[schedule](python_basic.html#schedule---定时任务配置)配置定时任务，程序在指定时间自动执行策略算法。

- 

准备历史数据
通过[数据查询函数](python_select_api_history.html#---行情数据查询函数)获取历史数据

- 

订阅实时行情
通过[subscribe](python_subscribe.html#subscribe---行情订阅)订阅行情，用以触发行情事件处理函数。

## 行情事件处理函数

- 

处理盘口`tick`数据事件
通过[on_tick](python_data_event.html#on_tick---tick数据推送事件)响应tick数据事件，可以在该函数中继续添加自己的策略逻辑,如进行数据计算、交易等

- 

处理分时`bar`数据事件
通过[on_bar](python_data_event.html#on_bar---bar数据推送事件)响应bar数据事件，可以在该函数中继续添加自己的策略逻辑，如进行数据计算、交易等

## 交易事件处理函数

- 

处理回报`execrpt`数据事件
当交易委托被执行后会触发[on_execution_report](python_trade_event.html#on_execution_report---委托执行回报事件)，用于监测`委托执行状态`.

- 

处理委托`order`委托状态变化数据事件
当[订单状态](python_enum_constant.html#OrderStatus---委托状态)产生变化时会触发[on_order_status](python_trade_event.html#on_order_status---委托状态更新事件)，用于监测`委托状态`变更.

- 

处理账户`account`交易账户状态变化数据事件
当[交易账户状态](python_enum_constant.html#accountstatus---交易账户状态)产生变化时会触发[on_account_status](python_trade_event.html#onaccountstatus---交易账户状态更新事件)，用于监测`交易账户委托状态`变更.

## 其他事件处理函数

- 

处理`error`错误事件
当发生异常情况时触发[错误事件](python_other_event.html#onerror---错误事件)，并返回[错误码和错误信息](python_err_code.html#错误码)

- 

处理动态参数`parameter`动态参数修改事件
当[动态参数](python_parameter.html#addparameter---增加动态参数)产生变化时会触发[on_parameter](python_parameter.html#onparameter---动态参数修改事件推送)，用于监测动态参数修改.

- 

处理绩效指标对象`Indicator`回测结束事件
在回测模式下，回测结束后会触发[on_backtest_finished](python_other_event.html#onbacktestfinished---回测结束事件)，并返回回测得到的[绩效指标对象](python_object_trade.html#indicator---绩效指标对象).

- 

处理实时行情网络连接成功事件
当实时行情网络连接成功时触发[实时行情网络连接成功事件](python_other_event.html#onmarketdataconnected---实时行情网络连接成功事件).

- 

处理实时行情网络连接断开事件
当实时行情网络连接断开时触发[实时行情网络连接断开事件](python_other_event.html#onmarketdatadisconnected---实时行情网络连接断开事件).

- 

处理交易通道网络连接成功事件
当交易通道网络连接成功时触发[交易通道网络连接成功事件](python_other_event.html#ontradedataconnected---交易通道网络连接成功事件).

- 

处理交易通道网络连接断开事件
当交易通道网络连接断开时触发[交易通道网络连接断开事件](python_other_event.html#ontradedatadisconnected---交易通道网络连接断开事件).

## 策略入口

[run函数](python_basic.html#run---运行策略)用于启动策略，策略类交易类策略都需要run函数。在只需提取数据进行研究（即仅使用数据查询函数时）的情况下可以不调用run函数，在策略开始调用[set_token](python_other_api.html#settoken%20-%20设置token)即可

- 

用户`token`ID
用户身份的唯一标识，token位置参见终端-系统设置界面-密钥管理（token）

- 

策略ID`strategy_id`
策略文件与终端连接的纽带，是策略的身份标识。每创建一个策略都会对应生成一个策略id，创建策略时即可看到。

- 

策略工作模式
策略支持两种运行[模式](python_concept.html#mode---模式选择), 实时模式和回测模式,实时模式用于仿真交易及实盘交易，回测模式用于策略研究，用户需要在运行策略时选择模式.

     [ ** ](quickstart.html#level2数据驱动事件示例) [ ** ](python_frame.html#东方财富量化策略程序初始化)
