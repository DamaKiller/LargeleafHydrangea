# 1.什么是dateframe merge
merge操作类似于数据库当中两张表的join，可以通过一个或者多个key将多个dataframe链接起来。
merge是按照两个dataframe共有的column进行连接，两个dataframe必须具有同名的column。
# 2.merge操作
`pd.merge(left, right, on=None, how='inner', left_on=None, right_on=None, left_index=False, right_index=False, 
          sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
`  
**参数**
- **left和right：** 第一个DataFrame和第二个DataFrame对象，merge只能实现两个DataFrame的合并，无法一次实现多个合并。
- **on：** 指定参考column，要求两个df必须至少有一个相同的column，默认为None以最多相同的column为参考。
- **how：** 合并的方式，默认为inner取参考column的交集，outer取并集保留所有行；outer、left、right中的缺失值都以NaN填充；
  left按照左边对象为参考进行合并即保留左边的所有行，right按照右边对象为参考进行合并即保留右边所有行。  
  ```
  df1 = pd.DataFrame({'key':['A','B','C','D'],
                    'value':[1,2,3,4]})
  df2 = pd.DataFrame({'key':['A','E','F','G'],
                    'value':[5,6,7,8]})
  ```
  **内连接** ![image](https://user-images.githubusercontent.com/96570699/182077851-d5b6ad28-0040-4c49-b889-cd7b65b8e97b.png)
  **外连接** ![image](https://user-images.githubusercontent.com/96570699/182077223-ec005a1f-5672-4000-bca2-724af3449d84.png)  
  **左连接** ![image](https://user-images.githubusercontent.com/96570699/182077939-b9409da9-ed84-466f-81f3-99842912fe95.png)
  **右连接** ![image](https://user-images.githubusercontent.com/96570699/182077982-461b8297-7002-4f55-8d9e-3d7933d37fb8.png)
- **left_on=None和right_on=None：** 以上on是在两个df有相同的column的情况下使用，如果两个df没有相同的column，使用left_on和right_on分别指明左边和右边的参考column。
   ```
   df1 = pd.DataFrame({'index':['A','B','C','D'],
                      'value':[1,2,3,4]})
   df2 = pd.DataFrame({'key':['A','E','F','G'],
                      'value':[5,6,7,8]})
   df3 = pd.merge(df1, df2, how='outer', left_on='index', right_on='key')
   print(df3)
   ```
   ![image](https://user-images.githubusercontent.com/96570699/182079217-205916df-f922-4368-b237-68758612c588.png)
- **left_index和right_index：** 指定是否以索引为参考进行合并, left_index=True 必须和right_index=True共同使用。  
  ```
  df1 = pd.DataFrame({'key':['A','B','C','D'],
                    'value':[1,2,3,4]})
  df2 = pd.DataFrame({'key':['A','E','F','G'],
                    'value':[5,6,7,8]})
  df3 = pd.merge(df1, df2,how='outer',left_index=True, right_index=True)
  print(df3)
  ```
  ![image](https://user-images.githubusercontent.com/96570699/182081620-5a03eb14-d753-481f-bf58-7d95ca15eed2.png)
- **sort：** 合并结果是否按on指定的参考进行排序。
- **suffixed：** 合并后如果有重复column，分别加上什么后缀。如果两者相同的column未被指定为参考列，
  那么结果中这两个相同的column名称会被加上后缀，默认为左右分别为_x和_y,可以通过该参数修改默认后缀。
  ```
  df1 = pd.DataFrame({'key':['A','B','C','D'],
                    'value':['1','2','3','4']})
  df2 = pd.DataFrame({'key':['A','E','F','G'],
                    'value':['5','6','7','8']})
  df3 = pd.merge(df1, df2, on='key', suffixes=('_df1','_df2'))
  print(df3)
  ```
  ![image](https://user-images.githubusercontent.com/96570699/182083056-22d6b133-1032-42ac-9687-e4996a1bfe66.png)
# 3.merge三个以上dateframe
```
df = reduce(lambda x, y: pandas.merge(x, y, on=[column_index], how=连接方式,), dfs)   #dfs为dataframe列表
```

**reduce函数**
`reduce(function, iterable)`
reduce函数会将可迭代数据中的第一个和第二个运算，然后将结果和第三个运算，以此类推。

# 4.merge后可能出现问题
### 1.去掉dateframe中含有NaN的行
**使用`dropna(axis,how,thresh,subset,inplace)`函数**  
> **axis：** 这个参数默认为0，当等于0时代表的是删除空值nan所在的行，当等于1时删除空值所在的列。  
> **how：** 这个参数的值默认为‘any’，表示的是删除空值所在的行或者是列，这个主要看前面的axis参数你设定是0还是1；当参数等于‘all’，表示的是删除一阵行或者是一整列都为空值nan的行或者列，如果你的某一行或某一列，不全为空值的话，则不会删除，即不起作用。    
> **thresh：** 这个参数是一个整数x，意思是保留空值nan的数量小于x的每一行或者是每一列。比如我设置x=2，那么我每一行或者是每一列的非空值的数量大于等于2的行或者列都会被保存，具体是行还是列，那还是看前面的axis参数的设置。  
> **subset：** 这个参数的意思是指定删除特定行或列的空值所在的列或行，如果axis=0，表示如果指定行x中有空值，则删除所在的列；如果axis=1，表示如果指定列x有空值，则删除空值所在的行。  
> **inplace：** 这个参数默认为False，它的意思是你在处理空值nan时，是在原数据上处理还是在先把原数据复制一份，然后在副本上处理，在副本上处理的时候，原数据不受任何影响；如果inplace设置为True，那代表你在原数据上进行处理，原数据直接受影响。  


### 2.对dateframe中含有NaN的行进行填充
**使用`fillna(axis,mthod,limit,inplace)`函数**  
> **axis：** 这个参数取1时，表示按照行来填充，取0时表示按照列来填充。默认为0，即按照列。和dropna函数的刚好相反。  
> **method：** 这个参数的意思是填充的方式，如果为‘ffill’，则是将这个空值的前一个数据复制给这个空值；如果为‘bfill’，则是将这个空值的后一个数据复制给这个空值。如果不用这个参数，不声明即可。  
> **limit：** 这个参数时限制填充的空值的个数，比如某一列有两个空值，我这里指定只填充一个空值，另一个空值不管它。  
> **inplace：** 这个参数默认为False，它的意思是你在处理空值nan时，是在原数据上处理还是在先把原数据复制一份，然后在副本上处理，在副本上处理的时候，原数据不受任何影响；如果inplace设置为True，那代表你在原数据上进行处理，原数据直接受影响。  




