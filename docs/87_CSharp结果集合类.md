# 结果集合类

## GMDataList

### GMDataList 类定义

** GMDataList **模板类是所有返回列表型数据函数的标准返回， 表示一个列表数据存储。类声明如下:

```
public class GMDataList<T>
{
    public List<T> data;           //数据
    public int status;             //状态码， 0表示成功， 其它表示错误码
}

```

### 使用举例

```
//查询一段tick行情
GMDataList<Tick> dl = GMApi.HistoryTicks("SHSE.600000", "2018-07-16 09:30:00", "2018-07-16 10:30:00");

if (dl.status == 0) //判断查询是否成功
{
    //遍历行情数组
    foreach(var v in dl.data)
    {
        Console.WriteLine("{0} {1}", v.symbol, v.price);
    }
}

```
     ** ** ** ** ** **
