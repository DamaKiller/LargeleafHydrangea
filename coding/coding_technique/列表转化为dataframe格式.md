# 一维列表转化为dataframe会成为一列数据
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

# 二维列表转化为dataframe会成为一行数据
二维列表是将其他列表当做列表的元素放在一个列表当中，也就是列表的嵌套。
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

# 二位列表
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

