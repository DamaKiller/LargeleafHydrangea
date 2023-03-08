# 一.简绍
该语法是在3.6版本加入的,使用时需注意。  
for/while-else它的用法是正常执行（不是通过break跳出循环）完for循环中的操作后，再执行else中的语句。

# 二.for-else例子
```
a = [1,2,3,4,5]
for i in a:
    print(i)
else:
    print('done')
```
![image](https://user-images.githubusercontent.com/96570699/185845579-8ea95760-bf79-4402-ab6a-81b5a78b4e84.png)

```
a = [1,2,3,4,5]
for i in a:
    if i == 2:
        continue
    print(i)
else:
    print('done')
```
![image](https://user-images.githubusercontent.com/96570699/185846018-054d6d7f-aaf4-460d-a881-f51e8f0590d3.png)

```
a = [1,2,3,4,5]
for i in a:
    if i == 2:
        break
    print(i)
else:
    print('done')
```
![image](https://user-images.githubusercontent.com/96570699/185846204-98458e68-1750-4cd0-8f36-a3a66626c6ee.png)

**注**  
空列表会直接执行else中的语句。
```
a = []
for i in a:
    print(i)
else:
    print('done')
```
![image](https://user-images.githubusercontent.com/96570699/185847161-16f7374a-d2b7-4014-859f-61ef932dce27.png)

# 三.while-else循环
```
a = 0
while a < 6:
    print(a)
    a += 1
else:
    print('done')
```

```
a = 0
while a < 6:
    if a == 2:
        break
    print(a)
    a += 1
else:
    print('done')
```
![image](https://user-images.githubusercontent.com/96570699/185850607-18e25fad-7829-49fb-8121-7a4ae88719a2.png)


