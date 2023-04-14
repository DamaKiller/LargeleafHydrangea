# 输出每个月的日期
```
year = 2023
month = 3
start_day = datetime(year, month, 1)
end_day = datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
date_list = []
while start_day <= end_day:
    date_list.append(datetime.strftime(start_day, '%Y-%m-%d'))
    start_day += timedelta(days=1)
    
# 结果
['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05', 
'2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09', '2023-03-10', 
'2023-03-11', '2023-03-12', '2023-03-13', '2023-03-14', '2023-03-15',
'2023-03-16', '2023-03-17', '2023-03-18', '2023-03-19', '2023-03-20',
'2023-03-21', '2023-03-22', '2023-03-23', '2023-03-24', '2023-03-25', 
'2023-03-26', '2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31']
```


# datetime常用方法查询
### 创建一个datetime类型的时间
```
year = 2023
month = 4
day = 1
hour = 0
minute = 0
second = 0

test_datetime = datetime.datetime(year, month, day, hour, minute, second)
print(test_datetime)            # 2023-04-01 00:00:00
print(type(test_datetime))      # <class 'datetime.datetime'>
```


### 对datetime进行增减
```
year = 2023
month = 4
day = 1
hour = 0
minute = 0
second = 0

test_datetime = datetime.datetime(year, month, day, hour, minute, second)
print(test_datetime)        # 2023-04-01 00:00:00
test_datetime = test_datetime + datetime.timedelta(hours=10, minutes=10, seconds=10)
print(test_datetime)        # 2023-04-01 10:10:10
```


### 字符串和datetime类型来回转换
```
str = '2023-04-01 00:00:00'
time_datetime = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
print(time_datetime)            # 2023-04-01 00:00:00
print(type(time_datetime))      # <class 'datetime.datetime'>
timestr = time_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(timestr)                  # 2023-04-01 00:00:00
print(type(timestr))            # <class 'str'>
```




