## 动态参数成员函数

### AddParameters - 添加参数

添加动态参数， 添加成功后， 参数将在终端上显示。

**函数原型:**

```
int AddParameters(List<Parameter> parameters)
int AddParameters(Parameter parameter)

```

**参数：**

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| parameters | List | Parameter列表 |
| parameter | Parameter | 一个Parameter对象 |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### DelParameters - 删除参数

删除动态参数

**函数原型:**

```
int DelParameters(string keys)

```

**参数：**

````

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| keys | string | 对应参数的键值, 多个参数使用,间隔，如key1,key2,... |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### SetParameters - 设置参数

设置参数值

**函数原型:**

```
int SetParameters(List<Parameter> parameters)
int SetParameters(Parameter parameter)

```

**参数：**

``

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| parameters | List | Parameter列表 |
| parameter | Parameter | Parameter对象 |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### GetParameters - 获取参数

获取参数值

**函数原型:**

```
GMDataList<Parameter> GetParameters()

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | GMDataList | 一个GMDataList对象 |

### SetSymbols - 设置标的

设置交易标的， 设置成功后， 标的将在终端上显示。

**函数原型:**

```
int SetSymbols(string symbols);

```

**参数：**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| symbols | string | symbol列表，逗号分隔 |
| 返回值 | int | 成功返回0， 失败返回错误码 |

### GetSymbols - 获取标的

获取交易标的

**函数原型:**

```
GMDataList<string> GetSymbols()

```

**参数：**

``

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| 返回值 | GMDataList | 一个GMDataList对象 |

     ** ** ** ** ** **
