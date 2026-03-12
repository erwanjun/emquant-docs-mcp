## 基金交易函数

### `fund_etf_buy` - ETF申购

仅在**实盘**中可以使用

```
fund_etf_buy(symbol, volume, price, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 申购数量 |
| price | float | 申购价格 |
| account_id | str | 账户 ID，不指定则使用默认账户 |

返回值 `List[Dict]`

### `fund_etf_redemption` - ETF赎回

仅在**实盘**中可以使用

```
fund_etf_redemption(symbol, volume, price, account_id='')

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbol | str | 标的代码 |
| volume | int | 赎回数量 |
| price | float | 赎回价格 |
| account_id | str | 账户 ID，不指定则使用默认账户 |

返回值 `List[Dict]`
     [ ** ](python_algo_trade.html#算法交易函数) [ ** ](python_etf_trade_api.html#fundetfredemption---etf赎回)
