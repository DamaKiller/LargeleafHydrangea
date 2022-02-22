#一维数组转化为dataframe会成为一列数据
import pandas
a = [1, 2, 3, 4, 5]
df_a = pandas.DataFrame(a)
print(df_a)

#   0
#0  1
#1  2
#2  3
#3  4
#4  5

#二维数组转化为dataframe会成为一行数据
import pandas
a = [1, 2, 3, 4, 5]
df_a = pandas.DataFrame([a])
print(df_a)
#  0  1  2  3  4
#0  1  2  3  4  5
