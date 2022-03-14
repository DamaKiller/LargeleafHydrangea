#推导式不仅可以用来创建列表，还可以用来创建集合和字典。

#创建字典
dict = {x:chr(65+x) for x in range(10)}
print(type(dict))
print(dict)
#结果
#<class 'dict'>
#{0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

#创建集合
set = {x for x in range(20) if x%2==0}
print(type(set))
print(set)
#结果
#<class 'set'>
#{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
