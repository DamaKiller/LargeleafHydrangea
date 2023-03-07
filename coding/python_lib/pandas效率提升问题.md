# 场景一
从外界信息源筛选数据合并到现有的dateframe当中。   
**第一想法：**  
> 循环处理，筛选出符合数据，然后做成一行dateframe合并到现有dateframe当中。  
```
dataframe_first = ***
for info in data_info:
    if info ***:
      data_dataframe = pd.Dataframe(info, coloum=[***], index=[***])
      pd.concat([dataframe_first, data_dataframe])
```


**效率做法：**  
> 循环处理，筛选出符合数据，然后放到一个外界字典当中，然后最后将该字典做成dataframe，然后和初始dataframe合并。  
> 这样做可以避免多次调用pd.concat， 该方法随着dataframe的增大效率越来越慢， 这样做只需要调用一次该方法即可。 
> 将数据存储到字典或列表中，直接做成dateframe比先做成dateframe，然后再一个个往里面插值要快。   
```
dataframe_first = ***
data_info_dict = {
  ***_1:[],
  ***_2:[]
}
for info in data_info:
    if info ***:
      ***_1.append(info[***_1])
      ***_2.append(info[***_2])
data_dataframe = pd.Dataframe(data_info_dict, coloum=[***_1, ***_2], index=[***])    
pd.concat([dataframe_first, data_dataframe])
```





