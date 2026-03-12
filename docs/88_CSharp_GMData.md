## GMData

### GMData 类定义

**GMData** 模板类是所有返回类数据函数的标准返回， 表示一个对象数据。类声明如下:

```
public class GMData<T>
{
    public T data;                 //数据
    public int status;             //状态码， 0表示成功， 其它表示错误码
}

```

### 使用举例

```
//获取深交所最新的代码信息
GMData<DataTable> ds = GMApi.GetInstruments(null, "SZSE");
if(ds.status == 0)
{
    var dt = ds.data;
    for (int i = 0; i < dt.Rows.Count; i++)
    {
        Console.WriteLine("{0},{1},{2} ", dt.Rows[i]["symbol"], dt.Rows[i]["sec_level"], dt.Rows[i]["pre_close"]);
    }
}

```
     ** ** ** ** ** **
