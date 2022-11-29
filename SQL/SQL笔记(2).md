# 子查询
![image](https://user-images.githubusercontent.com/96570699/188269723-cf6f0566-6f1d-4fa9-ae2f-7c81153d855a.png)  
在 SELECT 语句中，子查询总是从内向外处理。即先把子查询的select的语句执行完再执行外围的select语句。  
作为子查询的 SELECT 语句只能查询单个列。企图检索多个列将返回错误。  
### 1.where子句中的子查询
*** 
![image](https://user-images.githubusercontent.com/96570699/188273472-769e5f73-8a7c-43d1-9d01-2d79caece8b3.png)  
![image](https://user-images.githubusercontent.com/96570699/188273561-344d9b98-3843-42a9-ab87-1fefc807cd6b.png)  


### 2.from子句中的子查询
*** 
![image](https://user-images.githubusercontent.com/96570699/188273893-2158496f-8235-4b6b-826b-af7452f3aa8c.png)  
![image](https://user-images.githubusercontent.com/96570699/188274152-2e9127e4-a311-4102-8b5b-7ad112215a26.png)  
一定要把from中子查询avg（）函数的结果起别名，否则会在下一步where语句中报错。  
![image](https://user-images.githubusercontent.com/96570699/188274224-05ae8628-7777-4692-b93b-f9082e533aa4.png)  


### 3.select子句中的子查询
*** 
这种查询不需要连接表。  
![image](https://user-images.githubusercontent.com/96570699/188314341-c5068cc6-aff5-4a5d-925c-54c1df845416.png)  
![image](https://user-images.githubusercontent.com/96570699/188314360-7a70c53d-5f66-4523-ad26-0613c4c14775.png)  
这条子查询返回四个结果，所以会报错。  
![image](https://user-images.githubusercontent.com/96570699/188314530-4aa072e6-a87c-4193-9ae7-dca6f6ba7ec5.png)  




# union-合并结果
*** 
![image](https://user-images.githubusercontent.com/96570699/188315253-5882aa37-7f89-465d-9bb0-324cb1141e4e.png)  
![image](https://user-images.githubusercontent.com/96570699/188315580-1e92b5a2-4b8b-4884-8e00-4ed9bc2dea90.png)  
![image](https://user-images.githubusercontent.com/96570699/188315694-0060a67d-861b-43f2-a3b2-4f9da6ddf3fe.png)  
这种写法在sql中可以，但是在oracle中不行，要求列数和数据类型都要相同。  
![image](https://user-images.githubusercontent.com/96570699/188315717-5fb8d547-2271-41a5-bab2-27379c89b2f7.png)  
**union和unionall的区别**  
union在进行合并后会去掉重复的元素，所以会对所产生的结果集进行排序运算，删除重复的记录再返回结果。  
union all则只是简单地将两个结果集合并后就返回结果。因此，如果返回的两个结果集中有重复的数据，那么返回的结果就会包含重复的数据。  
在执行查询操作时，union all要比union快很多，所以，如果可以确认合并的两个结果集中不包含重复的数据，那么最好使用union all。  
**union后的排序方法**  
将union后的结果当作一个临时表，然后对该临时表进行排序查询。(不要忘了给该临时表起别名，否则会报错)  
在用 UNION 组合查询时，只能使用一条 ORDER BY 子句，它必须位于最后一条 SELECT 语句之后。对于结果集，不存在用一种方式排序一部分，而又用另一种方式排序另一
部分的情况，因此不允许使用多条 ORDER BY 子句。  




# limit（开始位置， 长度）-限制条数
*** 
![image](https://user-images.githubusercontent.com/96570699/188316501-3cfaf58f-060f-4679-a56a-90a39d0af060.png)  
![image](https://user-images.githubusercontent.com/96570699/188315879-4e5b77aa-44de-483d-b5f6-07e8c4d76bcc.png)  
![image](https://user-images.githubusercontent.com/96570699/188316360-1c4a7d91-f2ad-4571-af89-523e74e178c5.png)  
![image](https://user-images.githubusercontent.com/96570699/188316517-92792994-6f07-425d-8f08-89252e914b16.png)  
**注**   
`offset`该关键字可以让SQL跳过几条数据。例如`limit 1 offset 2`就是跳过两条数据之后查找一条。   
MySQL、MariaDB和 SQLite可以把 LIMIT 4 OFFSET 3 语句简化为 LIMIT 3,4。使用这个语法，逗号之前的值对应 OFFSET，逗号之后的值对应LIMIT（反着的，要小心）。  




# 创建表及数据类型
*** 
![image](https://user-images.githubusercontent.com/96570699/188318563-899b8008-5a60-4bfe-a6ad-b70f0e5c5890.png)    
varchar和char最长长度为255，date和datetime为固定长度。    
![image](https://user-images.githubusercontent.com/96570699/188318580-b3300726-7d21-4954-b3a7-1caf43ffe907.png)  
![image](https://user-images.githubusercontent.com/96570699/188318619-9a817207-7fea-43b7-ad14-a4112a53a524.png)  
![image](https://user-images.githubusercontent.com/96570699/188318543-17f3330d-8ce9-47a2-a35e-62c42b6dff4d.png)    




# 删除表
*** 
![image](https://user-images.githubusercontent.com/96570699/188318531-8d512378-8a2b-4d34-927e-d48770de4130.png)  




# insert
*** 
![image](https://user-images.githubusercontent.com/96570699/188667042-0826c73e-590a-4f37-ba99-f4b2f1170130.png)  
![image](https://user-images.githubusercontent.com/96570699/188667228-eea270b4-01b0-491d-8075-946d7dfdc525.png)  
![image](https://user-images.githubusercontent.com/96570699/188667509-ffb6d9d3-35ad-4371-a880-ba05b6357e5f.png)  
可以使用default关键字来指定默认值  
![image](https://user-images.githubusercontent.com/96570699/188669094-c03b062a-bff4-4175-ac82-a71ce02740f3.png)  
![image](https://user-images.githubusercontent.com/96570699/188669281-052d99db-8f5a-4f24-ba05-5d3d848fb3ef.png)  
![image](https://user-images.githubusercontent.com/96570699/188670229-f2ac1c39-315a-4ea0-a6e8-195dc1ce9af5.png)  


### 格式化
*** 
![image](https://user-images.githubusercontent.com/96570699/188877147-d8d83ec9-c5e2-4041-a431-8bc82a5cc325.png)  
![image](https://user-images.githubusercontent.com/96570699/188877301-4b0d106c-7b55-4058-ba73-692e193ad680.png)  
![image](https://user-images.githubusercontent.com/96570699/188877504-b0364ace-7ca2-44fa-9f29-4b02817bcb61.png)  
![image](https://user-images.githubusercontent.com/96570699/188878370-7b15d2e6-0c66-4e59-b237-047a6652a9d7.png)    
![image](https://user-images.githubusercontent.com/96570699/188879646-faf2231d-0806-4167-9b23-7d28746d222c.png)  
![image](https://user-images.githubusercontent.com/96570699/188882636-a354a339-409a-433e-b9e9-1da4f6860ffc.png)  
![image](https://user-images.githubusercontent.com/96570699/188883123-97e94af8-9548-42e1-a871-185575992e90.png)  
![image](https://user-images.githubusercontent.com/96570699/188883238-1c2e26c7-06e8-44c1-9227-5d842d9fa66c.png)  
![image](https://user-images.githubusercontent.com/96570699/188883634-c32e447d-4905-4e3b-ade2-e3ee4a874aec.png)  
![image](https://user-images.githubusercontent.com/96570699/188889233-3bc77fa6-9da3-4c62-abc1-8ad5b43f2a91.png)  
**date和datetime的区别**  
![image](https://user-images.githubusercontent.com/96570699/188890379-cd496132-1cf9-498e-9c7b-5907b63740ab.png)  
![image](https://user-images.githubusercontent.com/96570699/188891630-727d883f-e27c-4041-8f16-27955d0cc468.png)  
![image](https://user-images.githubusercontent.com/96570699/188892570-b2d83c92-fdfd-4039-8bbb-ce4c3a084bf5.png)       


### 插入多条语句
*** 
![image](https://user-images.githubusercontent.com/96570699/189480318-8b143910-a906-4a23-9d83-8fb52ca8da8f.png)  




# update
*** 
![image](https://user-images.githubusercontent.com/96570699/188894163-9df403dd-237f-4b3b-8c1d-2375ed40ff23.png)  




# delete
*** 
![image](https://user-images.githubusercontent.com/96570699/188920536-fba6cefe-8a52-4f7a-b5b3-8b6de65f4659.png)  
![image](https://user-images.githubusercontent.com/96570699/189484267-18981eff-9b2f-422c-b97d-7a7af7090d9f.png)  
![image](https://user-images.githubusercontent.com/96570699/189484159-c818177f-807c-4f21-b85e-0e38ae0effd1.png)  
![image](https://user-images.githubusercontent.com/96570699/189484288-3d7aa096-d202-4144-b1d8-5a101f388a84.png)  
![image](https://user-images.githubusercontent.com/96570699/189484235-7510d329-df0c-472d-b6bf-5bbefad94a41.png)  
![image](https://user-images.githubusercontent.com/96570699/189484787-00683493-8381-4f7a-9252-147c8f58c663.png)  
**注**  
delete操作多张表时，`delete from table1, table2 where table1.字段 = table2.字段`，要这么写。  
它的执行方法是从table1中取第一条数据然后到table2中进行比对，发现有满足条件的就删掉，接下来再去除第二条，第三条，依次类推。  




# 快速复制表
*** 
![image](https://user-images.githubusercontent.com/96570699/189480685-203b0ae7-72dc-449e-8dd0-49d14ce15000.png)  
![image](https://user-images.githubusercontent.com/96570699/189480695-c9aa035c-ef46-4a1b-ab8c-ebbbcc81b71f.png)  
将部分查询结果创建成一张表  
![image](https://user-images.githubusercontent.com/96570699/189480809-6a7df5a0-6905-4695-aba9-6d1a2b1a45de.png)  
![image](https://user-images.githubusercontent.com/96570699/189480780-586d9c2f-1fbc-4a45-a62f-ab6fdc459502.png)  


# 将查询的结果插入到表中
*** 
查询的结果要符合表的结构才能插。  
![image](https://user-images.githubusercontent.com/96570699/189483350-a6422185-7977-4e69-84cb-a45ba219b634.png)
