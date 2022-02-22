#去除列表中空字符串的方法
#方法一
a = ['', '1', '', '2', '', '3']
b = [i for i in a if i != '']
print(b)    #['1', '2', '3']

#方法二
a = ['', '1', '', '2', '', '3']
while '' in a:
    a.remove('')
print(a)    #['1', '2', '3']

#方法三
a = ['', '11', '', '22', '', '33']
c = filter(None, a)
print(list(c))    #filter会产生一个迭代器。<filter object at 0x00000208DAC98400> 更推荐该方法，它具有最快的速度


#filter()函数
#filter(function, iterable) function -- 判断函数 iterable -- 可迭代对象
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))    #[1, 3, 5, 7, 9]



#去除列表中以什么为开头的字符串
a = ['#table_1', 'list_1', '#table_2', 'list_2', '#table_3', 'list_3']
b = []
for i in a:
   if not i.startswith('#'):
       b.append(i)
   else:
       pass
print(b)


#startwith()函数
#str1.startswith(str2, beg=0,end=len(string)); str1 -- 检测的字符串 str2 -- 要匹配的字符串 beg -- 可选参数用于设置字符串检测的起始位置 
#                                              strend -- 可选参数用于设置字符串检测的结束位置 （如果检测到字符串则返回True，否则返回False）
str = "this is string example....wow!!!";
print(str.startswith( 'this' ))            #True
print(str.startswith( 'is', 2, 4 ))        #True
print(str.startswith( 'this', 2, 4 ))      #False
