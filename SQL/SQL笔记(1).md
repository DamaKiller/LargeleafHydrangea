# 了解数据库
![image](https://user-images.githubusercontent.com/96570699/183578267-7872c5f8-4a92-4324-828c-88ca7e5cd7e9.png)  
![image](https://user-images.githubusercontent.com/96570699/183582627-f1f19c0b-8796-454f-a3dc-ec773ccf97e0.png)  


**端口号**  
***  
端口号的主要作用是表示一台计算机中的特定进程所提供的服务。网络中的计算机是通过IP地址来代表其身份的，它只能表示某台特定的计算机，
但是一台计算机上可以同时提供很多个服务，如数据库服务、FTP服务、Web服务等，我们就通过端口号来区别相同计算机所提供的这些不同的服务。
在同一台计算机上端口号不能重复，否则，就会产生端口号冲突。端口是通过端口号来标记的，端口号只有整数，范围是从0 到65535。


![image](https://user-images.githubusercontent.com/96570699/183595764-42af9531-5b9a-43a9-a1b9-a6028897288e.png)    
![image](https://user-images.githubusercontent.com/96570699/183596936-5480c736-281f-4059-acc6-e689760331b0.png)  
![image](https://user-images.githubusercontent.com/96570699/183598480-7f858ade-2bc6-4714-b420-2cc6912c4b55.png)  
![image](https://user-images.githubusercontent.com/96570699/183599268-8878dc25-c59d-4e47-81f4-b322d68c574e.png)  



# 简单查询
### 1.查看表结构 
***  
`desc 表名;`(describe缩写为desc)  


### 2.查看数据库版本
***  
`select version();`


### 3.查询一个字段
***  
![image](https://user-images.githubusercontent.com/96570699/183606625-49ad12d8-b48a-4318-bab5-a5fc684dc2d4.png)  


### 4.查询多个字段
***  
![image](https://user-images.githubusercontent.com/96570699/183607694-8c62913e-a2f4-407d-b9e3-d2e5089f7a23.png)  
`select 字段名1, 字段名2 from 表名;`


### 5.查询所有字段  
***  
![image](https://user-images.githubusercontent.com/96570699/183608944-6a8f01e1-e337-44e1-9301-75c8ebdbb401.png)  
![image](https://user-images.githubusercontent.com/96570699/183609397-8c36be80-145a-4f9c-b049-7509d8bf01e1.png)  


### 6.给查询的列起别名
***  
`select 字段名 from 表名 as 别名`  
`select 字段名 别名 from 表名`  
`select 字段名 '别 名' from 表名`  
**注**  
`select`只负责查询不会对原字段进行修改，它只是将查询结果显示为别名，不会更改原表的列名。  
可以在查询的字段名后加一个空格然后再加上别名也可以实现给查询字段起别名，当别名中有空格时可以加上单引号（双引号也可以）来保留空格，中文也要用单引号括起来。  
![image](https://user-images.githubusercontent.com/96570699/183616185-ac31ec22-ede6-496c-90a4-9876985b5373.png)  
查询的字段可以用数学运算符。`select age*10 from 表名`，查询出的结果字段为age*10，可以起别名来修改。



# 条件查询
***  
![image](https://user-images.githubusercontent.com/96570699/183618911-cacb7d48-604c-438d-9cb0-89a13e8834ce.png)  
![image](https://user-images.githubusercontent.com/96570699/183795898-e16c6775-3db6-47be-bd68-4ec024312fa0.png)  
**注**   
使用`between and`必须遵顼左小右大的原则，即and左为小的数，右为大的数。并且是闭区间。  
between...and...可以用来判断时间间隙，即between '2022-01-01' and '2023-01-01'，判断的是在22年的时间，右边要用下一年的一月一日。  
![image](https://user-images.githubusercontent.com/96570699/183840559-f2df2a20-bd5e-4787-ac0e-6e04bf071a8e.png)  
![image](https://user-images.githubusercontent.com/96570699/183848801-ab4e8360-0bde-4a08-bee6-9a58f0fca2c2.png)  
**正确写法**  
![image](https://user-images.githubusercontent.com/96570699/183849146-2633162b-4718-4799-ac45-b26af8885b42.png)  
**可以用小括号改变优先级**  
![image](https://user-images.githubusercontent.com/96570699/183851779-0f15434e-91bb-4ccc-80bc-2173383b7fb0.png)  
**要表示区间用`between and`或者`<= >=`来表示。`not in`就表示不在这几个值当中**   



# 模糊查询
***  
![image](https://user-images.githubusercontent.com/96570699/183853344-8b7d13be-fd58-4f6b-bf4a-1243a102c735.png)  
![image](https://user-images.githubusercontent.com/96570699/183853578-13fa2cca-c4c6-4bd0-a42a-b703693a1a6b.png)  
![image](https://user-images.githubusercontent.com/96570699/183854134-8b6b822c-ebcb-4da1-a610-0e7726e94e4b.png)  
![image](https://user-images.githubusercontent.com/96570699/183857019-46c95282-4991-4573-94a4-13bad95ecfc7.png)  




# 排序
![image](https://user-images.githubusercontent.com/96570699/183858089-95269b64-bc4a-46af-ab96-e2f4050a9604.png)  
### 1.指定降序操作(desc)  
***  
![image](https://user-images.githubusercontent.com/96570699/183858455-984f5537-a523-40ca-bb89-a46addd1b37b.png)  


### 2.指定升序操作(asc)  
***  
![image](https://user-images.githubusercontent.com/96570699/183859495-10ed55e6-0c67-4053-87b2-7d87a7327206.png)  


### 3.多个字段排序操作
***  
![image](https://user-images.githubusercontent.com/96570699/183861024-f388f5cf-29fa-4ee5-9175-9931c80a92b7.png)  


### 4.根据位置进行排序操作
***  
![image](https://user-images.githubusercontent.com/96570699/183861721-55817985-0b67-432a-8b24-4ec858d9e14d.png)


### 5.SQL执行优先级
***  
先执行FROM,明确数据的来源，它是从哪张表取来的。  
再执行WHERE,对数据进行筛选。  
再执行GROUP BY,对数据进行分组分类。  
在执行HAVING,对分组后的数据进行再筛选。  
再执行SELECT，对数据进行分组分类。  
再执行ORDER BY,对最终的结果进行排序。  
再执行LIMIT，对查询结果进行分页处理。  




# 数据处理函数（单行处理函数-一行一行处理）
### 1.LOWER-转换小写
***  
![image](https://user-images.githubusercontent.com/96570699/183868055-86c25789-adf1-4952-b056-88610b897133.png)  
同样结果的字段名是`Lower（ename）`可以给它起别名。  


### 2.UPPER-转换大写
***  
![image](https://user-images.githubusercontent.com/96570699/183868601-08a4d41e-65d7-4987-83f0-cdc86892be1b.png)  


### 3.substr-取子串
***  
![image](https://user-images.githubusercontent.com/96570699/185858046-9ff45e65-1a15-49f2-9efc-67f387215178.png)


### 4.length-取长度
***  
![image](https://user-images.githubusercontent.com/96570699/185859252-87e33dbf-a56a-4b5d-bf94-1cb1d8878d52.png)


### 5.rand()-生成随机数
**默认生成的随机数是小于1的**   
***  
![image](https://user-images.githubusercontent.com/96570699/186802229-9d95a6cd-1e03-41b3-8953-882b9e30e3c3.png)  
**生成100以内的随机数**  
![image](https://user-images.githubusercontent.com/96570699/186803364-3bb5e7b1-88db-4368-ba51-7347347a0f4f.png)  


###  6.ifnull(数据，被当作那个值)-空处理函数
***  
![image](https://user-images.githubusercontent.com/96570699/186808884-03f1e654-d136-4138-9490-e44776539d3c.png)  
![image](https://user-images.githubusercontent.com/96570699/186809356-985ff6fe-9d72-4b28-b413-ecd5b0186e34.png)  
![image](https://user-images.githubusercontent.com/96570699/187110559-bf2f14bd-8700-4960-982e-44c3589be536.png)  


###  7.case...when...then...when...then...else..end-模拟if语句
***  
不加else条件，会默认返回null。  
Case函数只返回第一个符合条件的值，剩下的Case部分将会被自动忽略。  
![image](https://user-images.githubusercontent.com/96570699/187442887-3836db7b-3c3a-4217-9a52-68a9c5f75441.png)  
**两种写法**  
**第一种**  
![image](https://user-images.githubusercontent.com/96570699/187444919-a325a8e5-2085-435e-8821-775159ffb30f.png)  
**第二种**  
![image](https://user-images.githubusercontent.com/96570699/187445304-43ff4f77-2277-41a1-85f5-25c1e4925f14.png)  
![image](https://user-images.githubusercontent.com/96570699/191673942-eb50ad25-0f78-4601-8f02-0982c490a4e6.png)  
![image](https://user-images.githubusercontent.com/96570699/191674075-df43a6cd-1a9f-4546-a5b7-fd2ee3030414.png)  
![image](https://user-images.githubusercontent.com/96570699/191674254-2234f73d-9146-40b6-84a4-638cabcc5212.png)  
![image](https://user-images.githubusercontent.com/96570699/191674208-0de820e7-ccb1-4f9e-8f7f-a82895b8dbdd.png)  


### 8.IF(expr1,expr2,expr3)
***  
expr1 的值为TRUE，则返回值为 expr2。  
expr1 的值为FALSE，则返回值为 expr3。  
其中，expr1是判断条件，expr2和expr3是符合expr1的自定义的返回结果。  
**互换性别案列**  
![image](https://user-images.githubusercontent.com/96570699/191675095-547ab406-444c-4ced-9e9c-8e85b06e511a.png)  




# 分组函数-多行处理函数
***  
![image](https://user-images.githubusercontent.com/96570699/187447259-278edd02-b68c-4b86-9101-2f51c7c2eb95.png)  
**分组函数注意点**  
![image](https://user-images.githubusercontent.com/96570699/187449785-32a46c36-8116-48af-85f7-aad6348126da.png)  
![image](https://user-images.githubusercontent.com/96570699/187453011-fbcf04fa-547e-4fd9-9a64-11e42ed53601.png)  
![image](https://user-images.githubusercontent.com/96570699/187452753-4d0a38a2-b3e5-4223-b95e-87f6ee9565bd.png)  
![image](https://user-images.githubusercontent.com/96570699/187457053-1b471b9c-6f26-45a7-a2e3-70a0098646f9.png)  
![image](https://user-images.githubusercontent.com/96570699/187486508-1a932561-8f34-42d7-b3f5-8f8cf4cdfe39.png)  
![image](https://user-images.githubusercontent.com/96570699/187457523-97458777-7e5a-4aa5-8bbc-cd9a6c818b50.png)  


### 分组查询
***  
![image](https://user-images.githubusercontent.com/96570699/187459907-e40db954-2075-481e-b1ef-472a815b1137.png)
![image](https://user-images.githubusercontent.com/96570699/187815969-b136450f-d99e-4f7c-912a-7bdba4a031f3.png)  
![image](https://user-images.githubusercontent.com/96570699/187816063-81815763-088c-4de6-8024-00f765d94156.png)  
![image](https://user-images.githubusercontent.com/96570699/187816216-b3394295-ef1c-4596-8c02-5f0a91aee78f.png)  
![image](https://user-images.githubusercontent.com/96570699/187816872-0be33d85-fecb-4524-802c-636ecfac3900.png)  
![image](https://user-images.githubusercontent.com/96570699/187817210-76d94025-a923-4530-9b8e-77d81a918d82.png)  
但是该种写法效率比较低，分组处理过的数据一部分是无效处理，可以先用where过滤出大于3000的数据再进行分组处理。where是先筛选再分组，having是先分组再筛选。    
![image](https://user-images.githubusercontent.com/96570699/187817595-7316c13a-0c70-4294-84e7-9dd8f7a57ead.png)  
![image](https://user-images.githubusercontent.com/96570699/187823246-bc5d36e7-e482-4c7e-b124-0c16751e8806.png)  
![image](https://user-images.githubusercontent.com/96570699/187823301-83dde1b7-1cb6-4d84-ba9d-9005330dc41a.png)  
![image](https://user-images.githubusercontent.com/96570699/187825267-59fa76f1-6b5f-4c45-be52-2ce916931eca.png)  
**注**  
使用group by之后，SELECT子句只能存在（常数, 聚合函数, GROUP BY子句中指定的列名）三种元素。  
GROUP BY子句中使用列的别名会引发错误，其原因就是SQL语句在DBMS内部的执行顺序造成的：SELECT子句在GROUP BY子句之后执行。  


### distinct-去重
***  
![image](https://user-images.githubusercontent.com/96570699/187845828-f1ba3933-cffd-4e39-87b3-beb9088d2809.png)  
![image](https://user-images.githubusercontent.com/96570699/187856111-abd2c552-208f-4d8b-9522-10e2c18f2a93.png)  
它可以用在分组函数当中，去重后计数。  
![image](https://user-images.githubusercontent.com/96570699/187856404-3264a3bb-c891-4b38-9586-c6a8867cd05a.png)  
放在第二位，前面的name比后面的job字段数据多，导致出错。  
![image](https://user-images.githubusercontent.com/96570699/189159619-52acdbcc-074f-44bf-80ab-663018717d63.png)  
**注**   
只能在SELECT 语句中使⽤，不能在 INSERT, DELETE, UPDATE 中使⽤。   




# 连接查询
***  
![image](https://user-images.githubusercontent.com/96570699/187857970-2b5966a5-df2b-4142-b484-51c12cbef804.png)  
![image](https://user-images.githubusercontent.com/96570699/187858241-49ba76ab-d309-4862-9316-a65c247c6193.png)  


### 1.笛卡尔积现象
***  
![image](https://user-images.githubusercontent.com/96570699/187863220-3f39921e-c2a5-4156-92c6-228c38f26a81.png)  
就是不加任何连接条件，直接从两张表中查找数据，就会出现这种情况。  
![image](https://user-images.githubusercontent.com/96570699/187863359-a572a903-eb34-48eb-aa62-271a49e6dc8b.png)  
![image](https://user-images.githubusercontent.com/96570699/187864288-be774130-9ab2-465a-9750-4b8933a18188.png)  
![image](https://user-images.githubusercontent.com/96570699/187867216-cde1abe3-f62e-4310-862d-7c7d6dea07bb.png)  
这种写法会去两个表中分表查找这两个字段，效率太低，现已经不用，为sql92的语法。  


### 2.内连接之等值连接
***  
条件是等量关系，所以被称作等值连接。  
![image](https://user-images.githubusercontent.com/96570699/188127064-d95c00f6-8a30-4bf6-b9ae-9fdb811fe882.png)  
![image](https://user-images.githubusercontent.com/96570699/188128438-412e688c-296b-4cfc-bec5-76b1f1401d6e.png)   
戴着inner可读性更好，一眼就能看出来是内连接。  
![image](https://user-images.githubusercontent.com/96570699/188127804-0075ebf0-ba6e-4e30-85e2-3cd50557bd64.png)  


### 3.内连接之非等值连接
***  
条件不是等量条件。
![image](https://user-images.githubusercontent.com/96570699/188129526-adf6bcc3-583e-433e-a5f9-8e8e153da2d7.png)  
该处省略了inner。  
![image](https://user-images.githubusercontent.com/96570699/188151019-cd83e906-280d-495c-b5bf-f9c94665c9eb.png)


### 4.内连接之自连接
***  
先查询员工编号，员工名，领导编号  
![image](https://user-images.githubusercontent.com/96570699/188266030-74dd7097-babf-41a2-80a3-1c2f9fc5ad8b.png)  
![image](https://user-images.githubusercontent.com/96570699/188266125-7fb0e220-dcbe-45af-9556-21db60f8eb8d.png)  
![image](https://user-images.githubusercontent.com/96570699/188266133-017356aa-1be8-425c-9e9a-33b62edc866c.png)  
员工的领导编号等于领导的员工编号，没有KING是因为其没有领导    
![image](https://user-images.githubusercontent.com/96570699/188266367-4eb458bf-1c41-490e-b369-a15cac6c4044.png)  
![image](https://user-images.githubusercontent.com/96570699/188266416-3aa1671b-b0e4-4a17-9246-cd04a6050926.png)  
内连接没有主次关系，能匹配上就查出来，没有匹配的就不显示。  


### 5.外连接
***  
![image](https://user-images.githubusercontent.com/96570699/188266944-97530c95-e5c0-41a6-8680-ef510459b70c.png)   
没有匹配的数据则自动填充null。  
会将主表的所有select字段全部查询出来，即使不满足on条件也会查询出来。  
![image](https://user-images.githubusercontent.com/96570699/188266985-e23eb558-94ad-4f2d-aeb7-bcaa4debecc1.png)  
![image](https://user-images.githubusercontent.com/96570699/188267034-997c59d5-cfaf-4e8d-92e7-11df60c75876.png)  


### 6.多张表连接
***  
![image](https://user-images.githubusercontent.com/96570699/188267480-4827e56f-c493-4f61-9ea7-044bc0dafded.png)  
![image](https://user-images.githubusercontent.com/96570699/188267681-efcfac3a-0e9b-4999-b531-db3555d9e50b.png)  
![image](https://user-images.githubusercontent.com/96570699/188267839-c3768d03-d0a7-40d7-8369-9d6c6e152aea.png)  
![image](https://user-images.githubusercontent.com/96570699/188268213-a6f848f8-f254-402b-8998-96e2f6df7606.png)  
![image](https://user-images.githubusercontent.com/96570699/188268738-8f65039f-1609-41fe-ae2f-549b99a21273.png)    
![image](https://user-images.githubusercontent.com/96570699/188268718-dfe6c3d0-70a1-496c-aa04-ecc14bb3a101.png)  

