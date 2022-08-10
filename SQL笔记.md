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
### 1.查看表结构 
`desc 表名;`(describe缩写为desc)  

### 2.查看数据库版本
`select version();`

### 3.查询一个字段
![image](https://user-images.githubusercontent.com/96570699/183606625-49ad12d8-b48a-4318-bab5-a5fc684dc2d4.png)  

### 4.查询多个字段
![image](https://user-images.githubusercontent.com/96570699/183607694-8c62913e-a2f4-407d-b9e3-d2e5089f7a23.png)  
`select 字段名1, 字段名2 from 表名;`

### 5.查询所有字段  
![image](https://user-images.githubusercontent.com/96570699/183608944-6a8f01e1-e337-44e1-9301-75c8ebdbb401.png)  
![image](https://user-images.githubusercontent.com/96570699/183609397-8c36be80-145a-4f9c-b049-7509d8bf01e1.png)  

### 6.给查询的列起别名
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
![image](https://user-images.githubusercontent.com/96570699/183795898-e16c6775-3db6-47be-bd68-4ec024312fa0.png)  
**注**   
使用`between and`必须遵顼左小右大的原则，即and左为小的数，右为大的数。并且是闭区间。  
![image](https://user-images.githubusercontent.com/96570699/183840559-f2df2a20-bd5e-4787-ac0e-6e04bf071a8e.png)  
![image](https://user-images.githubusercontent.com/96570699/183848801-ab4e8360-0bde-4a08-bee6-9a58f0fca2c2.png)  
**正确写法**  
![image](https://user-images.githubusercontent.com/96570699/183849146-2633162b-4718-4799-ac45-b26af8885b42.png)  
**可以用小括号改变优先级**  
![image](https://user-images.githubusercontent.com/96570699/183851779-0f15434e-91bb-4ccc-80bc-2173383b7fb0.png)  
**要表示区间用`between and`或者`<= >=`来表示。`not in`就表示不在这几个值当中**   



# 模糊查询
![image](https://user-images.githubusercontent.com/96570699/183853344-8b7d13be-fd58-4f6b-bf4a-1243a102c735.png)  
![image](https://user-images.githubusercontent.com/96570699/183853578-13fa2cca-c4c6-4bd0-a42a-b703693a1a6b.png)  
![image](https://user-images.githubusercontent.com/96570699/183854134-8b6b822c-ebcb-4da1-a610-0e7726e94e4b.png)  
![image](https://user-images.githubusercontent.com/96570699/183857019-46c95282-4991-4573-94a4-13bad95ecfc7.png)  



# 排序
![image](https://user-images.githubusercontent.com/96570699/183858089-95269b64-bc4a-46af-ab96-e2f4050a9604.png)  
### 1.指定降序操作(desc)  
![image](https://user-images.githubusercontent.com/96570699/183858455-984f5537-a523-40ca-bb89-a46addd1b37b.png)  

### 2.指定降序操作(asc)  
![image](https://user-images.githubusercontent.com/96570699/183859495-10ed55e6-0c67-4053-87b2-7d87a7327206.png)  

### 3.多个字段排序操作
![image](https://user-images.githubusercontent.com/96570699/183861024-f388f5cf-29fa-4ee5-9175-9931c80a92b7.png)  

### 4.根据位置进行排序操作
![image](https://user-images.githubusercontent.com/96570699/183861721-55817985-0b67-432a-8b24-4ec858d9e14d.png)

### 5.SQL执行优先级
先执行FROM,明确数据的来源，它是从哪张表取来的。  
再执行WHERE,对数据进行筛选。  
再执行GROUP BY,对数据进行分组分类。  
再执行SELECT，对数据进行分组分类。  
再执行ORDER BY,对最终的结果进行排序。  



# 数据处理函数（单行处理函数-一行一行处理）
### 1.LOWER-转换小写
![image](https://user-images.githubusercontent.com/96570699/183868055-86c25789-adf1-4952-b056-88610b897133.png)  
同样结果的字段名是`Lower（ename）`可以给它起别名。  

### 2.UPPER-转换大写
![image](https://user-images.githubusercontent.com/96570699/183868601-08a4d41e-65d7-4987-83f0-cdc86892be1b.png)  


