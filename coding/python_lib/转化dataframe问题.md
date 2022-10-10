# 列表转化为dataframe
## 一维列表转化为dataframe会成为一列数据
```
import pandas
a = [1, 2, 3, 4, 5]
df_a = pandas.DataFrame(a)
print(df_a)
```
结果：
```
#   0
#0  1
#1  2
#2  3
#3  4
#4  5
```
**注**  
在输出dataframe时，若列数，行数太多中间会默认省略变成省略号，可以使用   
`pandas.set_option('display.width', None)  #输出列数无限制`  
`pandas.set_option('display.max_rows', None) #输出行数无限制`   

## 二维列表转化为dataframe会成为一行数据
二维列表是将其他列表当做列表的元素放在一个列表当中，也就是列表的嵌套。通过该方法可以将一个列表转化为一行数据。可以在后边加上`columns=column_index, index=index_index`来设置列，行索引的名。
```
import pandas
a = [1, 2, 3, 4, 5]
df_a = pandas.DataFrame([a])
print(df_a)
```
结果：
```
#  0  1  2  3  4
#0  1  2  3  4  5
```

##  二维列表
```
my_list = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list)
```
结果：
```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
![image](https://user-images.githubusercontent.com/96570699/155255688-c45c2362-dccd-4696-9dcb-88beff8dc8a6.png)
由图可以看，my_list[0]对应的就是[1,2,3]，因此我们在访问1的时候，他对应的坐标就为（0,0），我们可以通过索引访问，即my_list[0][0],它的值对应的就是1，其他值访问的方式和它一样，像元素9对应的访问方式就为my_list[2][2]。

# csv转化为dataframe
## csv文件中有空值
若csv文件中有空值，则转化为dataframe格式时该空值处会变成缺失值NaN，有时不需要NaN值，则可以用该语句将之去除。  
![image](https://user-images.githubusercontent.com/96570699/175261178-ce174723-c4df-45d4-9492-70953bd18e92.png)  
```
item = data.fillna('')    #data为每行csv数据
```
![image](https://user-images.githubusercontent.com/96570699/175261402-352da6b2-d1d3-4c3a-bfe0-6c8e0e634b0c.png)

# dateframe的merge问题
## merge三个以上dateframe
```
df = reduce(lambda x, y: pandas.merge(x, y, on=[column_index], how=连接方式,), dfs)   #dfs为dataframe列表
```

**reduce函数**
`reduce(function, iterable)`
reduce函数会将可迭代数据中的第一个和第二个运算，然后将结果和第三个运算，以此类推。
