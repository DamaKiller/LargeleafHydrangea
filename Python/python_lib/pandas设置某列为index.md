# set_index()
`DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`  
set_index仅适用于DataFrame, 作用是重新设置 DataFrame的行索引。  
> **keys：** 列标签或列标签/数组列表，需要设置为索引的列. 例如：['index_1', 'index_2']  
> **drop：** 默认为True，删除用作新索引的列.  
> **append：** 是否将列附加到现有索引，默认为False.  
> **inplace：** 输入布尔值，表示当前操作是否对原数据生效，默认为False.  
> **verify_integrity：** 检查新索引的副本。否则，请将检查推迟到必要时进行。将其设置为false将提高该方法的性能，默认为false。  

## 例子
```
data = {'state':['Dalian','Beijing','Tianjin','Wuhan'],
            'year':[2000,2001,2002,2003],
            'pop':[1.5,4.7,3.6,2.4]}
dataframe = pd.DataFrame(data, columns=['state', 'year', 'pop'])
# 结果
     state  year  pop
0   Dalian  2000  1.5
1  Beijing  2001  4.7
2  Tianjin  2002  3.6
```
**将state列作为索引**  
```
## drop=True
df_new = dataframe.set_index('state',drop=True, append=False, inplace=False, verify_integrity=False)
print(df_new)
# 结果
         year  pop
state
Dalian   2000  1.5
Beijing  2001  4.7
Tianjin  2002  3.6
Wuhan    2003  2.4

## drop=False
df_new = dataframe.set_index('state',drop=False, append=False, inplace=False, verify_integrity=False)
print(df_new)
# 结果
           state  year  pop
state
Dalian    Dalian  2000  1.5
Beijing  Beijing  2001  4.7
Tianjin  Tianjin  2002  3.6
Wuhan      Wuhan  2003  2.4

## append=True
df_new = dataframe.set_index('state',drop=True, append=True, inplace=False, verify_integrity=False)
print(df_new)
# 结果(原来的索引和新索引一起被保留下来了)
           year  pop
  state
0 Dalian   2000  1.5
1 Beijing  2001  4.7
2 Tianjin  2002  3.6
3 Wuhan    2003  2.4

```

# reset_index()
`DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')`    
> **level：** 数值类型可以为int、str、tuple或list，默认无，仅从索引中删除给定级别。默认情况下移除所有级别。控制了具体要还原的那个等级的索引.  
> **drop：** 当指定drop=False时，则索引列会被还原为普通列；否则，经设置后的新索引值被会丢弃。默认为False.  
> **inplace：** 输入布尔值，表示当前操作是否对原数据生效，默认为False.  
> **col_level：** 数值类型为int或str，默认值为0，如果列有多个级别，则确定将标签插入到哪个级别。默认情况下，它将插入到第一级.  
> **col_fill：** 对象，默认''，如果列有多个级别，则确定其他级别的命名方式。如果没有，则重复索引名.  

**注**  
reset_index（）还原可分为两种类型，第一种是对原来的数据表进行reset；第二种是对使用过set_index()函数的数据表进行reset。  
## 第一种：对原来的数据表进行reset处理
```
data = {'state':['Dalian','Beijing','Tianjin','Wuhan'],
            'year':[2000,2001,2002,2003],
            'pop':[1.5,4.7,3.6,2.4]}
dataframe = pd.DataFrame(data, columns=['state', 'year', 'pop'])
# 结果
     state  year  pop
0   Dalian  2000  1.5
1  Beijing  2001  4.7
2  Tianjin  2002  3.6

## drop=False
df_new = dataframe.reset_index(drop=False)
print(df_new)
# 结果(添加了列名为index的新列，同时在新列上进行重置索引。)
   index    state  year  pop
0      0   Dalian  2000  1.5
1      1  Beijing  2001  4.7
2      2  Tianjin  2002  3.6
3      3    Wuhan  2003  2.4

## drop=True
df_new = dataframe.reset_index(drop=True)
print(df_new)
# 结果
     state  year  pop
0   Dalian  2000  1.5
1  Beijing  2001  4.7
2  Tianjin  2002  3.6
3    Wuhan  2003  2.4
# 输出结果和原来的数据表没有区别。但是其实在这个时候是有操作的，是在原有的索引列重置索引，同时不另外添加新列.
# 这个常用于索引的重置，在进行数据删减处理的时候能派上很大的用场.
```

## 第二种：对使用过set_index()函数的数据表进行reset
```
data = {'state':['Dalian','Beijing','Tianjin','Wuhan'],
            'year':[2000,2001,2002,2003],
            'pop':[1.5,4.7,3.6,2.4]}
dataframe = pd.DataFrame(data, columns=['state', 'year', 'pop'])
# 结果
     state  year  pop
0   Dalian  2000  1.5
1  Beijing  2001  4.7
2  Tianjin  2002  3.6

## drop=True
df_new = dataframe.set_index('state',drop=True, append=False, inplace=False, verify_integrity=False)
df_new = dataframe.reset_index(drop=True)
print(df_new)
# 结果(刚刚经过处理后的新索引被删除了)
   year  pop
0  2000  1.5
1  2001  4.7
2  2002  3.6
3  2003  2.4

## drop=False
df_new = df_new.reset_index(drop=False)
print(df_new)
# 结果(被作为索引的列被还原成原来的样子)
     state  year  pop
0   Dalian  2000  1.5
1  Beijing  2001  4.7
2  Tianjin  2002  3.6
3    Wuhan  2003  2.4
```
**注**  
对Empty的dataframe进行reset_index,即使他有coloum索引，它也只会剩下index一列，即：
```    
    index
0   
```










