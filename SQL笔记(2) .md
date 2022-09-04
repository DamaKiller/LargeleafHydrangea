# 子查询
![image](https://user-images.githubusercontent.com/96570699/188269723-cf6f0566-6f1d-4fa9-ae2f-7c81153d855a.png)  
### 1.where子句中的子查询
![image](https://user-images.githubusercontent.com/96570699/188273472-769e5f73-8a7c-43d1-9d01-2d79caece8b3.png)  
![image](https://user-images.githubusercontent.com/96570699/188273561-344d9b98-3843-42a9-ab87-1fefc807cd6b.png)  


### 2.from子句中的子查询
![image](https://user-images.githubusercontent.com/96570699/188273893-2158496f-8235-4b6b-826b-af7452f3aa8c.png)  
![image](https://user-images.githubusercontent.com/96570699/188274152-2e9127e4-a311-4102-8b5b-7ad112215a26.png)  
一定要把from中子查询avg（）函数的结果起别名，否则会在下一步where语句中报错。  
![image](https://user-images.githubusercontent.com/96570699/188274224-05ae8628-7777-4692-b93b-f9082e533aa4.png)  


### 3.select子句中的子查询
这种查询不需要连接表。  
![image](https://user-images.githubusercontent.com/96570699/188314341-c5068cc6-aff5-4a5d-925c-54c1df845416.png)  
![image](https://user-images.githubusercontent.com/96570699/188314360-7a70c53d-5f66-4523-ad26-0613c4c14775.png)  
这条子查询返回四个结果，所以会报错。  
![image](https://user-images.githubusercontent.com/96570699/188314530-4aa072e6-a87c-4193-9ae7-dca6f6ba7ec5.png)  




# union-合并结果
![image](https://user-images.githubusercontent.com/96570699/188315253-5882aa37-7f89-465d-9bb0-324cb1141e4e.png)  
![image](https://user-images.githubusercontent.com/96570699/188315580-1e92b5a2-4b8b-4884-8e00-4ed9bc2dea90.png)  
![image](https://user-images.githubusercontent.com/96570699/188315694-0060a67d-861b-43f2-a3b2-4f9da6ddf3fe.png)  
这种写法在sql中可以，但是在oracle中不行，要求列数和数据类型都要相同。  
![image](https://user-images.githubusercontent.com/96570699/188315717-5fb8d547-2271-41a5-bab2-27379c89b2f7.png)  




# limit（开始位置， 长度）-限制条数
![image](https://user-images.githubusercontent.com/96570699/188316501-3cfaf58f-060f-4679-a56a-90a39d0af060.png)  
![image](https://user-images.githubusercontent.com/96570699/188315879-4e5b77aa-44de-483d-b5f6-07e8c4d76bcc.png)  
![image](https://user-images.githubusercontent.com/96570699/188316360-1c4a7d91-f2ad-4571-af89-523e74e178c5.png)  
![image](https://user-images.githubusercontent.com/96570699/188316517-92792994-6f07-425d-8f08-89252e914b16.png)  




# 创建表及数据类型
![image](https://user-images.githubusercontent.com/96570699/188318563-899b8008-5a60-4bfe-a6ad-b70f0e5c5890.png)    
varchar和char最长长度为255，date和datetime为固定长度。    
![image](https://user-images.githubusercontent.com/96570699/188318580-b3300726-7d21-4954-b3a7-1caf43ffe907.png)  
![image](https://user-images.githubusercontent.com/96570699/188318619-9a817207-7fea-43b7-ad14-a4112a53a524.png)  
![image](https://user-images.githubusercontent.com/96570699/188318543-17f3330d-8ce9-47a2-a35e-62c42b6dff4d.png)    




# 删除表
![image](https://user-images.githubusercontent.com/96570699/188318531-8d512378-8a2b-4d34-927e-d48770de4130.png)  




