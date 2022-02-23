#示例数据
import pandas

a = [{'c1':11, 'c2':22}, {'c1':33, 'c2':44 }, {'c1':55, 'c2':66 }]
df = pandas.DataFrame(a)
print(df)
#结果
#   c1  c2
#0  11  22
#1  33  44
#2  55  66

#按行遍历(iterrows():)
#按行遍历，将DataFrame的每一行迭代为(index, Series)对，可以通过row[列名]对元素进行访问。
for index, row in df.iterrows():
    print(index)    #输出行索引    
#结果
#0
#1
#2

for index, row in df.iterrows():
    print(row['c1'], row['c2'])    #通过列名，输出每一行的值
#结果
#11 22
#33 44
#55 66

#按列遍历(iteritems():)
#按列遍历，将DataFrame的每一列迭代为(index, Series)对，可以通过row[行名]对元素进行访问。
for index, row in df.iteritems():
    print(index)    #输出列索引
#结果
#c1
#c2

for index, row in df.iteritems():
    print(row[0], row[1], row[2])    #通过行名，输出每一列的值
#结果
#11 33 55
#22 44 66

#按行遍历(itertuples():)
#DataFrame.itertuples(self, index=True, name='Pandas')    index：bool, 默认为 True。若为True，则将索引作为元组的第一个元素返回。  name：str 或 None, 默认为 “Pandas”。返回的namedtuple的名称，或者返回None以返回常规元组。
#返回值：一个迭代器，用于遍历DataFrame中每一行的namedtuple，第一个字段可能是索引，而后面的字段是列值。
for row in df.itertuples():
    print(row)    
#结果：
#Pandas(Index=0, c1=11, c2=22)
#Pandas(Index=1, c1=33, c2=44)
#Pandas(Index=2, c1=55, c2=66)

#通过设置index参数为False时，我们可以删除索引作为元组的第一个元素：
#Pandas(c1=11, c2=22)
#Pandas(c1=33, c2=44)
#Pandas(c1=55, c2=66)

#改变name参数，我们为产生的namedtuple设置自定义名称：
#cat(Index=0, c1=11, c2=22)
#cat(Index=1, c1=33, c2=44)
#cat(Index=2, c1=55, c2=66)
