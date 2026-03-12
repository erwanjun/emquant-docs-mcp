## 动态参数

动态参数仅在**仿真交易和实盘交易**下生效， 可在终端设置和修改。

动态参数通过策略调用接口实现策略和东方财富量化界面参数交互， 在不停止策略运行的情况下，界面修改参数（移开光标，修改就会生效）会对策略里的指定变量做修改

![动态参数](images/attach_16408fc9e3c9fed6.png)

### add_parameter - 增加动态参数

**函数原型:**

```
add_parameter(key, value, min=0, max=0, name='', intro='', group='', readonly=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | str | 参数的键 |
| value | double | 参数的值 |
| min | double | 最小值 |
| max | double | 最大值 |
| name | str | 参数名称 |
| intro | str | 参数说明 |
| group | str | 参数的组 |
| readonly | bool | 是否为只读参数 |

**返回值:**

`None`

**示例：**

```
context.k_value = 80
add_parameter(key='k_value', value=context.k_value, min=0, max=100, name='k值阀值', intro='调整k值', group='1', readonly=False)

```

### set_parameter - 修改已经添加过的动态参数

**注意：**需要保持key键名和添加过的动态参数的key一致，否则不生效，无报错

**函数原型:**

```
set_parameter(key, value, min=0, max=0, name='', intro='', group='', readonly=False)

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | str | 参数的键 |
| value | double | 参数的值 |
| min | double | 最小值 |
| max | double | 最大值 |
| name | str | 参数名称 |
| intro | str | 参数说明 |
| group | str | 参数的组 |
| readonly | bool | 是否为只读参数 |

**返回值:**

`None`

**示例：**

```
context.k_xl = 0.3
set_parameter(key='k_value', value=context.k_xl, min=0, max=1, name='k值斜率', intro='调整k值斜率', group='1', readonly=False)

```

### on_parameter - 动态参数修改事件推送

**函数原型:**

```
on_parameter(context, parameter)

```

**参数：**

（参见 上下文对象）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| context | context | 上下文 |
| parameter | dict | 当前被推送的动态参数对象 |

**示例：**

```
def on_parameter(context, parameter):
    print(parameter)

```

**输出：**

```
{'key': 'k_value', 'value': 80.0, 'max': 100.0, 'name': 'k值阀值', 'intro': '调整k值', 'group': '1', 'min': 0.0, 'readonly': False}

```

### context.parameters - 获取所有动态参数

返回数据类型为字典, key为动态参数的key, 值为动态参数对象

**示例：**

```
print(context.parameters)

```

**输出：**

```
{'k_value': {'key': 'k_value', 'value': 80.0, 'max': 100.0, 'name': 'k值阀值', 'intro': 'k值阀值', 'group': '1', 'min': 0.0, 'readonly': False}, 'd_value': {'key': 'd_value', 'value': 20.0, 'max': 100.0, 'name': 'd值阀值', 'intro': 'd值阀值', 'group': '1', 'min': 0.0, 'readonly': False}}

```
     [ ** ](python_trade_event.html#onaccountstatus---交易账户状态更新事件) [ ** ](python_parameter.html#addparameter---增加动态参数)
