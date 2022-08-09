# 了解数据库
![image](https://user-images.githubusercontent.com/96570699/183578267-7872c5f8-4a92-4324-828c-88ca7e5cd7e9.png)  
![image](https://user-images.githubusercontent.com/96570699/183582627-f1f19c0b-8796-454f-a3dc-ec773ccf97e0.png)  


**端口号**  
端口号的主要作用是表示一台计算机中的特定进程所提供的服务。网络中的计算机是通过IP地址来代表其身份的，它只能表示某台特定的计算机，
但是一台计算机上可以同时提供很多个服务，如数据库服务、FTP服务、Web服务等，我们就通过端口号来区别相同计算机所提供的这些不同的服务。
在同一台计算机上端口号不能重复，否则，就会产生端口号冲突。端口是通过端口号来标记的，端口号只有整数，范围是从0 到65535。


![image](https://user-images.githubusercontent.com/96570699/183595764-42af9531-5b9a-43a9-a1b9-a6028897288e.png)    
![image](https://user-images.githubusercontent.com/96570699/183596936-5480c736-281f-4059-acc6-e689760331b0.png)  
![image](https://user-images.githubusercontent.com/96570699/183598480-7f858ade-2bc6-4714-b420-2cc6912c4b55.png)  
![image](https://user-images.githubusercontent.com/96570699/183599268-8878dc25-c59d-4e47-81f4-b322d68c574e.png)  


# 简单查询
### 查看表结构 
`desc 表名;`(describe缩写为desc)  

### 查询一个字段
![image](https://user-images.githubusercontent.com/96570699/183606625-49ad12d8-b48a-4318-bab5-a5fc684dc2d4.png)  

### 查询多个字段
![image](https://user-images.githubusercontent.com/96570699/183607694-8c62913e-a2f4-407d-b9e3-d2e5089f7a23.png)  
`select 字段名1, 字段名2 from 表名;`

### 查询所有字段  
![image](https://user-images.githubusercontent.com/96570699/183608944-6a8f01e1-e337-44e1-9301-75c8ebdbb401.png)  
![image](https://user-images.githubusercontent.com/96570699/183609397-8c36be80-145a-4f9c-b049-7509d8bf01e1.png)  

### 给查询的列起别名
`select 字段名 from 表名 as 别名`  
`select 字段名 别名 from 表名`  
`select 字段名 '别 名' from 表名`  
**注**  
`select`只负责查询不会对原字段进行修改，它只是将查询结果显示为别名，不会更改原表的列名。  
可以在查询的字段名后加一个空格然后再加上别名也可以实现给查询字段起别名，当别名中有空格时可以加上单引号（双引号也可以）来保留空格，中文也要用单引号括起来。  
![image](https://user-images.githubusercontent.com/96570699/183616185-ac31ec22-ede6-496c-90a4-9876985b5373.png)  
查询的字段可以用数学运算符。`select age*10 from 表名`，查询出的结果字段为age*10，可以起别名来修改。

# 条件查询
![image](https://user-images.githubusercontent.com/96570699/183618911-cacb7d48-604c-438d-9cb0-89a13e8834ce.png)  




