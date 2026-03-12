## 交易成员函数

### GetAccounts - 查询交易账号

用于查询交易账号配置信息。多用于实盘时，策略同时关联多个交易账号的时候，获取所有交易账号的信息，所返回的账号id(`accounId`)用于后续各个交易api的入参， 即指定操作某个交易账户。
如果关联的交易账号只有一个， 一般用不到此函数。

**函数原型:**

```
GMDataList<Account> GetAccounts();

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | GMDataList<Account> | 一个GMDataList结构 |

### orderVolume - 按指定量委托

按指定量委托, 如果调用成功，后续委托单状态变化将会触发on_order_status回调。

**函数原型:**

```
GMData<Order> OrderVolume(string symbol, int volume, OrderSide side, OrderType orderType, PositionEffect positionEffect, double price = 0, string account = null)

```

**参数：**

``

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| volume | int | 委托数量 |
| side | OrderSide | 委托方向 参见 enum OrderSide |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| positionEffect | PositionEffect | 开平类型 参见 enum PositionSide |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 GetAccounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//以11块的价格限价买入10000股浦发银行
GMData<Order> o = orderVolume("SHSE.600000", 10000, OrderSide.OrderSide_Buy, OrderType.OrderType_Limit, PositionEffect.PositionEffect_Open， 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 若下单数量输入有误，终端会拒绝此单，并显示`委托量不正确`。股票买入最小单位为`100`，卖出最小单位为`1`,如存在不足100股的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

### OrderValue - 按指定价值委托

按指定价值委托, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调。

**函数原型:**

```
GMData<Order> OrderValue(string symbol, double value, OrderSide side, OrderType orderType, PositionEffect positionEffect, double price = 0, string account = null)

```

**参数：**

``

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| value | int | 股票价值 |
| side | OrderSide | 委托方向 参见 enum OrderSide |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| positionEffect | PositionEffect | 开平类型 参见 enum PositionSide |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 GetAccounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//下限价单，以11元每股的价格买入价值为100000元的SHSE.600000, 根据volume = value / price,计算并取整得到volume = 9000
GMData<Order> o = order_value("SHSE.600000", 100000, OrderSide.OrderSide_Buy, OrderType.OrderType_Limit, positionEffect.PositionEffect_Open， 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据指定价值计算购买标的数量，即`value/price`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

### OrderPercent - 按总资产指定比例委托

按总资产指定比例委托, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调。

**函数原型:**

```
GMData<Order> OrderPercent(string symbol, double percent, OrderSide side, OrderType orderType, PositionEffect positionEffect, double price = 0, string account = null)

```

**参数：**

``

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| percent | double | 委托占总资产比例 |
| side | OrderSide | 委托方向 参见 enum OrderSide |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| positionEffect | PositionEffect | 开平类型 参见 enum PositionSide |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 GetAccounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//当前总资产为1000000。下限价单，以11元每股的价格买入SHSE.600000,期望买入比例占总资产的10%，根据volume = nav * precent / price 计算取整得出volume = 9000

GMData<Order> o = OrderPercent("SHSE.600000", 0.1, OrderSide.OrderSide_Buy, OrderType.OrderType_Limit, PositionEffect.PositionEffect_Open， 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据指定比例计算购买标的数量,即`(nav*precent)/price`,股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

### OrderTargetVolume - 调仓到目标持仓量

调仓到目标持仓量, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调。

**函数原型:**

```
GMData<Order> OrderTargetVolume(string symbol, int volume, OrderSide positionSide, OrderType orderType, double price = 0, string account = null)

```

**参数：**

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| volume | int | 期望的最终数量 |
| positionSide | PositionSide | 持仓方向 参见 enum PositionSide) |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 GetAccounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//当前SHSE.600000多方向持仓量为0，期望持仓量为10000，下单量为期望持仓量 - 当前持仓量 = 10000

GMData<Order> o = OrderTargetVolume("SHSE.600000", 10000, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

```
//600000浦发银行需要全部卖出时，volume设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标持有量（volume）到0，底层就会执行卖出

GMData<Order> o = OrderTargetVolume("SHSE.600000", 0, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据目标数量计算下单数量，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则订单会被拒绝，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

**6.** 股票交易position_side 仅支持设置多方向。

### OrderTargetValue - 调仓到目标持仓额

调仓到目标持仓额, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调。

**函数原型:**

```
GMData<Order> OrderTargetValue(string symbol, double value, PositionSide positionSide, OrderType orderType, double price = 0, string account = null)

```

**参数：**

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| value | int | 期望的股票最终价值 |
| positionSide | PositionSide | 持仓方向 参见 enum PositionSide) |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 get_accounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//当前SHSE.600000多方向当前持仓量为0，目标持有价值为100000的该股票，根据value / price 计算取整得出目标持仓量volume为9000，目标持仓量 - 当前持仓量 = 下单量为9000

GMData<Order> o = OrderTargetValue("SHSE.600000", 100000, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

```
//600000浦发银行需要全部卖出时，value设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标持有价值（value）到0，底层就会执行卖出

GMData<Order> o = OrderTargetValue("SHSE.600000", 0, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据目标数量计算下单数量，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则订单会被拒绝，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

**6.** 股票交易position_side 仅支持设置多方向。

### OrderTargetPercent - 调仓到目标持仓比例（总资产的比例）

调仓到目标持仓比例（总资产的比例）, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调。

**函数原型:**

```
GMData<Order> OrderTargetPercent(string symbol, double percent, PositionSide positionSide, OrderType orderType, double price = 0, string account = null)

```

**参数：**

``

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 标的代码，只能单个标的 |
| percent | double | 期望的最终占总资产比例 |
| positionSide | PositionSide | 持仓方向 参见 enum PositionSide) |
| orderType | OrderType | 委托类型 参见 enum OrderType |
| price | double | 委托价格（限价委托时的委托价，沪市市价委托的市价保护价，多位小数时会四舍五入，股票只保留两位，基金只保留三位） |
| account | string | 实盘账号id,关联多实盘账号时填写，可以从 get_accounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | Order | 一个Order结构, 如果函数调用失败， Order.status 值为 OrderStatus_Rejected, Order.ordRejReasonDetail 为错误原因描述, 其它情况表示函数调用成功，Order.clOrdId 为本次委托的标识，可用于追溯订单状态或撤单 |

**示例：**

```
//当前总资产价值为1000000，目标为以11元每股的价格买入SHSE.600000的价值占总资产的10%，根据volume = nav * percent / price 计算取整得出应持有9000股。当前该股持仓量为零，因此买入量为9000

GMData<Order> o = OrderTargetPercent("SHSE.600000", 0.1, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

```
//600000浦发银行需要全部卖出时，percent设置为0，position_side设置为PositionSide_Long，表示把600000浦发银行的多方向持仓（股票只有多方向）调整到目标持有比例（percent）到0，底层就会执行卖出

GMData<Order> o = OrderTargetPercent("SHSE.600000", 0, PositionSide.PositionSide_Long, OrderType.OrderType_Limit, 11);

```

**注意：**

**1.** 仅支持一个标的代码，若交易代码输入有误，终端会拒绝此单，并显示`委托代码不正确`。

**2.** 根据目标比例计算下单数量，为占`总资产(nav）`比例，系统判断开平仓类型。若下单数量有误，终端拒绝此单，并显示`委托量不正确`。若实际需要买入数量为0，则本地拒绝此单，`终端无显示，无回报`。股票买卖最小单位为`100`，不足100部分`向下取整`，如存在不足100的持仓一次性卖出;期货买卖最小单位为`1`，`向下取整`。

**3.** 若仓位不足，终端会拒绝此单，显示`仓位不足`。平仓时股票默认`平昨仓`，期货默认`平今仓`。应研究需要，`股票也支持卖空操作`。

**4.** OrderType优先级高于price,若指定OrderTpye_Market下市价单，使用价格为最新一个tick中的最新价，price参数失效。则price参数失效。若OrderTpye_Limit限价单，仿真模式价格错误，终端拒绝此单，显示委托价格错误，`回测模式下对价格无限制`。

**5.** 函数调用成功并不意味着委托已经成功，只是意味委托单已经成功发出去， 委托是否成功根据OnOrderStatus，或 GetOrder来判断。

**6.** 股票交易position_side 仅支持设置多方向。

### OrderCloseAll - 平当前所有可平持仓

平当前所有可平持仓, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调

**函数原型:**

```
GMDataList<Order> OrderCloseAll()

```

**参数：**

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | GMDataList<order> | 一个GMDataList<order>对象 |

### OrderCancel - 委托撤单

撤销单个委托单, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调

**函数原型:**

```
int OrderCancel(string clOrdIds, string account = null)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| clOrdIds | string | 委托单的客户id, 可以在下单或查单时获得 |
| account | string | 实盘账号id, 关联多实盘账号时填写，可以从 GetAccounts获取，也可以从终端实盘账号配置里拷贝。如果策略只关联一个账号，可以设置为null |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### OrderCancelAll - 撤销所有委托

撤销所有委托, 如果调用成功，后续委托单状态变化将会触发OnOrderStatus回调

**函数原型:**

```
int OrderCancelAll();

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### GetOrders - 查询所有委托

查询所有委托单

**函数原型:**

```
GMDataList<Order> GetOrders(string account = null)

```

**参数：**

``

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account | string | 账号ID accountId, 如果输入为null, 则返回所有账号的委托 |
| 返回值 | GMDataList<Order> | 一个GMDataList<order>对象 |

### GetUnfinishedOrders - 查询未结委托

查询所有未结委托

**函数原型:**

```
GMDataList<Order> GetUnfinishedOrders(string account = null)

```

**参数：**

``

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account | string | 账号IDaccountId, 如果输入为null, 则返回所有账号的委托 |
| 返回值 | GMDataList<Order> | 一个GMDataList<order>对象 |

### GetExecutionReports - 查询成交

查询所有成交

**函数原型:**

```
GMDataList<ExecRpt> GetExecutionReports(string account = null)

```

**参数：**

``

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account | string | 账号ID accountId, 如果输入为null, 则返回所有账号的成交 |
| 返回值 | GMDataList<ExecRpt> | 一个GMDataList<ExecRpt>对象 |

### GetCash - 查询资金

查询资金

**函数原型:**

```
GMDataList<Cash> GetCash(string account = null)

```

**参数：**

``

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account | string | 账号IDaccountId, 如果输入为NULL, 则返回所有账号的资金 |
| 返回值 | GMDataList<Cash> | 一个GMDataList<Cash>对象 |

### GetPosition - 查询持仓

查询所有持仓

**函数原型:**

```
GMDataList<Position> GetPosition(string account = null)

```

**参数：**

``

``
``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account | string | 账号IDaccountId, 如果输入为null, 则返回所有账号的持仓 |
| 返回值 | GMDataList<Position> | 一个GMDataList<Position>对象 |

     ** ** ** ** ** **
