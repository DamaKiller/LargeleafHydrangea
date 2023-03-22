##### loc方法
# 基本语法
df.loc [row selection, column selection]                                                    #定位行和列 loc用的是中括号，不是小括号。  
df.loc [row selection]                                                                      #只定位行,它返回的数据类型是Series，若想要Dataframe类型，
                                                                                            #用df.loc [[row selection]]
df.loc [:, column selection]                                                                #只定位列 不要忘了要在行索引的位置上加上':',返回的数据类型也是Series，
                                                                                            #但它不能用上一个嵌套列表方法，用df[[column selection]]
df.loc [row selection, [column selection, column selection, ...]]                           #选择单行多列 多个列索引要写在列表当中，返回的数据类型是Series.
df.loc [[row selection, row selection, ...], column selection]                              #选择单列多行 多个行索引要写在列表当中，返回的数据类型是Series.
df.loc [row selection] = [***, ***, ***...]                                                 #将row selection这一行赋值
df.loc [row selection] = ***                                                                #将row selection这一行全部赋值一个值

# 进阶用法
df.loc[df[column selection]>value, column selection]                                        #可以写表达式，查找大于某个值并且是某列的所有行,
                                                                                            #不写后面的column selection就是满足条件的所有数据                                         
df.loc[df[column selection]==value, column selection]                                       #查找等于某个值并且是某列的所有行，不写后面的column selection就是满足条件的所有数据 
df.loc[df[(column selection]==value) & (column selection]==value),
      [column selection, column selection, column selection]]                               #查找符合多个条件的指定列
df.loc[column selection, [column selection, column selection, ...]] = [value, value, ...]   #可以通过这种方法将对指定列赋值

#注 loc和at的区别：loc可以取多个值，at只能取一个格子里面的值（类似于loc的定位行列的用法）

       
##### iloc方法
# iloc函数使用的是行号和列号而不是行索引和列索引，除此之外和loc函数没有区别
df.iloc [：, 0：2]                                                                           #选择第一行第一二两列的数据

# 注
print(type(df.iloc [0]))                                                                    #<class 'pandas.core.series.Series'>  类型是Series
print(type(df.iloc [[0]]))                                                                  #<class 'pandas.core.frame.DataFrame'>  通过传递列表可转为DataFrame

##### at函数
df.at[row selection, column selection]                                                      #取第row selection行，第column selection的列
df.at[row selection, column selection] = value                                              #可以赋值

##### iat函数
# 使用行号和列号，除此之外跟at函数没有区别

       
##### isin()方法  
# 返回的结果是根据从isin函数传入的列表(li)，筛选出与列表中包含的数值或字符串相同的数据记录, 用法有点类似sql中的"in"  
data = {'state':['Dalian','Beijing','Tianjin','Wuhan'],
            'year':[2000,2001,2002,2003],
            'pop':[1.2,1.1,2.5,3.0]}
dataframe = pd.DataFrame(data, columns=['state', 'year', 'pop'])
    state  year  pop
0   Dalian  2000  1.2
1  Beijing  2001  1.1
2  Tianjin  2002  2.5
3    Wuhan  2003  3.0

# 简单的筛选方法
dataframe[dataframe['pop'] > 2.0]
     state  year  pop
2  Tianjin  2002  2.5
3    Wuhan  2003  3.0
       
# 多重条件筛选 
dataframe[(dataframe['pop']>2.0)&(dataframe['state']=='Tianjin')
     state  year  pop
2  Tianjin  2002  2.5
          
# 用isin来实现
# 简单的筛选方法
dataframe[dataframe['state'].isin(['Tianjin'])]
     state  year  pop
2  Tianjin  2002  2.5 

# 多重条件筛选
dataframe[(dataframe['state'].isin(['Beijing']))|(dataframe['pop']==dataframe['pop'].min())]
     state  year  pop
1  Beijing  2001  1.1   
       

##### ~isin()方法
# 结果与isin()相反，筛选出不在这里面的数据。         
dataframe[~(dataframe['state'].isin(['Beijing']))|~(dataframe['pop']==dataframe['pop'].min())]
     state  year  pop
0   Dalian  2000  1.2
2  Tianjin  2002  2.5
3    Wuhan  2003  3.0
     
          
##### contains ()方法
# 相当与SQL 中的contains的用法，能灵活地对字符串的数据进行筛选。
# 筛选出所有名称中还有'***'的数据记录
dataframe[dataframe['state'].str.contains('jing')]
     state  year  pop
1  Beijing  2001  1.1       
          
     
