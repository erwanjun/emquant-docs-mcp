常见的策略结构主要包括3类，如下图所示。

![](images/attach_164a635b8a0f0a12.jpg)

用户可以根据策略需求选择相应的策略结构

## 定时任务示例

以下代码的内容是：在每个交易日的14：50：00 市价买入200股浦发银行股票：

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 每天14:50 定时执行algo任务,
    # algo执行定时任务函数，只能传context参数
    # date_rule执行频率，目前暂时支持1d、1w、1m，其中1w、1m仅用于回测，实时模式1d以上的频率，需要在algo判断日期
    # time_rule执行时间， 注意多个定时任务设置同一个时间点，前面的定时任务会被后面的覆盖
    schedule(schedule_func=algo, date_rule='1d', time_rule='14:50:00')

def algo(context):
    # 以市价购买200股浦发银行股票， price在市价类型不生效
    order_volume(symbol='SHSE.600000', volume=200, side=OrderSide_Buy,
                 order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0)

# 查看最终的回测结果
def on_backtest_finished(context, indicator):
    print(indicator)

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: [init](python_basic.html#init---初始化策略) , 使用 [schedule](python_basic.html#schedule---定时任务配置) 函数进行定时任务配置

2. 配置任务, 到点会执行该任务

3. 执行策略

## 数据事件驱动示例

在用subscribe()接口订阅标的后，后台会返回tick数据或bar数据。每产生一个或一组数据，就会自动触发on_tick()或on_bar()里面的内容执行。比如以下范例代码片段，订阅浦发银行频率为1天和60s的bar数据，每产生一次bar，就会自动触发on_bar()调用，打印获取的bar信息：

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 订阅浦发银行, bar频率为一天和一分钟
    # 订阅订阅多个频率的数据，可多次调用subscribe
    subscribe(symbols='SHSE.600000', frequency='1d')
    subscribe(symbols='SHSE.600000', frequency='60s')

def on_bar(context, bars):

    # 打印bar数据
    print(bars)

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: init, 使用subscribe函数进行数据订阅

2. 实现一个函数: on_bar, 来根据数据推送进行逻辑处理

3. 执行策略

## 时间序列数据事件驱动示例

策略订阅代码时指定数据窗口大小与周期, 平台创建数据滑动窗口, 加载初始数据, 并在新的bar到来时自动刷新数据。

on_bar事件触发时, 策略可以取到订阅代码的准备好的时间序列数据。

以下的范例代码片段是一个非常简单的例子， 订阅浦发银行的日线和分钟bar, bar数据的更新会自动触发on_bar的调用, 每次调用`context.data`来获取最新的50条分钟bar信息：

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 订阅浦发银行, bar频率为一天和一分钟
    # 指定数据窗口大小为50
    # 订阅订阅多个频率的数据，可多次调用subscribe
    subscribe(symbols='SHSE.600000', frequency='1d', count=50)
    subscribe(symbols='SHSE.600000', frequency='60s', count=50)

def on_bar(context, bars):
    # context.data提取缓存的数据滑窗, 可用于计算指标
    # 注意：context.data里的count要小于或者等于subscribe里的count
    data = context.data(symbol=bars[0]['symbol'], frequency='60s', count=50, fields='close,bob')

    # 打印最后5条bar数据（最后一条是最新的bar）
    print(data.tail())

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: [init](python_basic.html#init---初始化策略) , 使用 [subscribe](python_subscribe.html#subscribe---行情订阅) 函数进行数据订阅

2. 实现一个函数: [on_bar](python_data_event.html#on_bar---bar数据推送事件) , 来根据数据推送进行逻辑处理, 通过 `context.data` 获取数据滑窗

3. 执行策略

## 多个标的数据事件驱动示例

策略订阅多个标的, 并且要求同一频度的数据到齐后, 再触发事件.

以下的范例代码片段是一个非常简单的例子， 订阅浦发银行和平安银行的日线bar, 在浦发银行bar和平安银行bar到齐后会自动触发on_bar的调用：

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 同时订阅浦发银行和平安银行,数据全部到齐再触发事件
    # wait_group是否需要等待全部代码的数据到齐再触发事件
    # wait_group_timeout超时时间，从返回第一个bar开始计时， 默认是10s，超时后的bar不再返回
    subscribe(symbols='SHSE.600000,SZSE.000001', frequency='1d', count=5, wait_group=True, wait_group_timeout='10s')

def on_bar(context, bars):
    for bar in bars:
        print(bar['symbol'], bar['eob'])

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: [init](python_basic.html#init---初始化策略) , 使用 [subscribe](python_subscribe.html#subscribe---行情订阅) 函数进行数据订阅多个代码， 设置wait_group=True

2. 实现一个函数: [on_bar](python_data_event.html#on_bar---bar数据推送事件) , 来根据数据推送(多个代码行情)进行逻辑处理

3. 执行策略

## 选择回测模式/实时模式运行示例

东方财富量化3策略只有两种模式, 回测模式(backtest)与实时模式(live)。在加载策略时指定mode参数。

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 订阅浦发银行的tick
    subscribe(symbols='SHSE.600000', frequency='60s')

def on_bar(context, bars):
    # 打印当前获取的bar信息
    print(bars)

if __name__ == '__main__':
    # 在终端仿真交易和实盘交易的启动策略按钮默认是实时模式，运行回测默认是回测模式，在外部IDE里运行策略需要修改成对应的运行模式
    # mode=MODE_LIVE 实时模式, 回测模式的相关参数不生效
    # mode=MODE_BACKTEST  回测模式

    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_LIVE,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: [init](python_basic.html#init---初始化策略) , 使用 [subscribe](python_subscribe.html#subscribe---行情订阅) 函数进行数据订阅代码

2. 实现一个函数: [on_bar](python_data_event.html#on_bar---bar数据推送事件) , 来根据数据推送进行逻辑处理

3. 选择对应模式，执行策略

## 提取数据研究示例

如果只想提取数据，无需实时数据驱动策略, 无需交易下单可以直接通过数据查询函数来进行查询。

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

# 可以直接提取数据，东方财富量化终端需要打开，接口取数是通过网络请求的方式，效率一般，行情数据可通过subscribe订阅方式
# 设置token， 查看已有token ID,在用户-密钥管理里获取
set_token('your token_id')

# 查询历史行情, 采用定点复权的方式， adjust指定前复权，adjust_end_time指定复权时间点
data = history(symbol='SHSE.600000', frequency='1d', start_time='2020-01-01 09:00:00', end_time='2020-12-31 16:00:00',
               fields='open,high,low,close', adjust=ADJUST_PREV, adjust_end_time='2020-12-31', df=True)
print(data)

```

整个过程只需要两步:

1. set_token 设置用户token，  如果token不正确, 函数调用会抛出异常

2. 调用数据查询函数， 直接进行数据查询

## 回测模式下高速处理数据示例

本示例提供一种在init中预先取全集数据，规整后索引调用的高效数据处理方式，能够避免反复调用服务器接口导致的低效率问题，可根据该示例思路，应用到其他数据接口以提高效率.

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):
    # 在init中一次性拿到所有需要的instruments信息
    instruments = get_history_instruments(symbols='SZSE.000001,SZSE.000002', start_date=context.backtest_start_time,end_date=context.backtest_end_time)
    # 将信息按symbol,date作为key存入字典
    context.ins_dict = {(i.symbol, i.trade_date.date()): i for i in instruments}
    subscribe(symbols='SZSE.000001,SZSE.000002', frequency='1d')

def on_bar(context, bars):
    print(context.ins_dict[(bars[0].symbol, bars[0].eob.date())])

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

整个策略需要三步:

1. 设置初始化函数: [init](python_basic.html#init---初始化策略) , 一次性拿到所有需要的instruments信息， 将信息按symbol,date作为key存入字典， 使用 [subscribe](python_subscribe.html#subscribe---行情订阅) 函数进行数据订阅代码

2. 实现一个函数: [on_bar](python_data_event.html#on_bar---bar数据推送事件) , 来根据数据推送进行逻辑处理

3. 执行策略

## 实时模式下动态参数示例

本示例提供一种通过策略设置动态参数，可在终端界面显示和修改，在不停止策略的情况下手动修改参数传入策略方法.

```
# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *
import numpy as np
import pandas as pd

'''动态参数，是指在不终止策略的情况下，东方财富量化终端UI界面和策略变量做交互，
    通过add_parameter在策略代码里设置动态参数，终端UI界面会显示对应参数
'''

def init(context):
    # log日志函数，只支持实时模式，在仿真交易和实盘交易界面查看，重启终端log日志会被清除，需要记录到本地可以使用logging库
    log(level='info', msg='平安银行信号触发', source='strategy')
    # 设置k值阀值作为动态参数
    context.k_value = 23
    # add_parameter设置动态参数函数，只支持实时模式，在仿真交易和实盘交易界面查看，重启终端动态参数会被清除，重新运行策略会重新设置
    add_parameter(key='k_value', value=context.k_value, min=0, max=100, name='k值阀值', intro='设置k值阀值',
                  group='1', readonly=False)

    # 设置d值阀值作为动态参数
    context.d_value = 20
    add_parameter(key='d_value', value=context.d_value, min=0, max=100, name='d值阀值', intro='设置d值阀值',
                  group='2', readonly=False)

    print('当前的动态参数有', context.parameters)
    # 订阅行情
    subscribe(symbols='SZSE.002400', frequency='60s', count=120)

def on_bar(context, bars):

    data = context.data(symbol=bars[0]['symbol'], frequency='60s', count=100)

    kdj = KDJ(data, 9, 3, 3)
    k_value = kdj['kdj_k'].values
    d_value = kdj['kdj_d'].values

    if k_value[-1] > context.k_value and d_value[-1] < context.d_value:
        order_percent(symbol=bars[0]['symbol'], percent=0.01, side=OrderSide_Buy, order_type=OrderType_Market, position_effect=PositionEffect_Open)
        print('{}下单买入， k值为{}'.format(bars[0]['symbol'], context.k_value))

# 计算KDJ
def KDJ(data, N, M1, M2):
    lowList= data['low'].rolling(N).min()
    lowList.fillna(value=data['low'].expanding().min(), inplace=True)
    highList = data['high'].rolling(N).max()
    highList.fillna(value=data['high'].expanding().max(), inplace=True)
    rsv = (data['close'] - lowList) / (highList - lowList) * 100
    data['kdj_k'] = rsv.ewm(alpha=1/M1).mean()
    data['kdj_d'] = data['kdj_k'].ewm(alpha=1/M2).mean()
    data['kdj_j'] = 3.0 * data['kdj_k'] - 2.0 * data['kdj_d']
    return data

# 动态参数变更事件
def on_parameter(context, parameter):
    # print(parameter)
    if parameter['name'] == 'k值阀值':
        # 通过全局变量把动态参数值传入别的事件里
        context.k_value = parameter['value']
        print('{}已经修改为{}'.format(parameter['name'], context.k_value))

    if parameter['name'] == 'd值阀值':
        context.d_value = parameter['value']
        print('{}已经修改为{}'.format(parameter['name'], context.d_value))

def on_account_status(context, account):
    print(account)

if __name__ == '__main__':
    '''
    strategy_id策略ID,由系统生成
    filename文件名,请与本文件名保持一致
    mode实时模式:MODE_LIVE回测模式:MODE_BACKTEST
    token绑定计算机的ID,可在系统设置-密钥管理中生成
    backtest_start_time回测开始时间
    backtest_end_time回测结束时间
    backtest_adjust股票复权方式不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
    backtest_initial_cash回测初始资金
    backtest_commission_ratio回测佣金比例
    backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='07c08563-a4a8-11ea-a682-7085c223669d',
        filename='main.py',
        mode=MODE_LIVE,
        token='2c4e3c59cde776ebc268bf6d7b4c457f204482b3',
        backtest_start_time='2020-09-01 08:00:00',
        backtest_end_time='2020-10-01 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=500000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```

## level2数据驱动事件示例

本示例提供level2行情的订阅， 包括逐笔成交、逐笔委托、委托队列
仅券商托管版本支持

```
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

def init(context):

    # 订阅浦发银行的逐笔成交数据
    subscribe(symbols='SHSE.600000', frequency='l2transaction')
    # 订阅平安银行的逐笔委托数据（仅支持深市标的）
    subscribe(symbols='SZSE.000001', frequency='l2order')
    # 订阅平安银行的委托队列数据
    subscribe(symbols='SZSE.000001', frequency='tick')

def on_l2order(context, order):
    # 打印逐笔成交数据
    print(order)

def on_l2transaction(context, transition):
    # 打印逐笔委托数据
    print(transition)

def on_tick(context, tick):
    # 打印tick和委托队列数据
    print(tick)

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
    '''
    run(strategy_id='strategy_id',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2020-11-01 08:00:00',
        backtest_end_time='2020-11-10 16:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)

```
     [ ** ](./) [ ** ](quickstart.html#定时任务示例)
