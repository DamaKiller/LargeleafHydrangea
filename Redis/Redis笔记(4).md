# 事务
![image](https://user-images.githubusercontent.com/96570699/192137565-a1948959-356e-4d5d-a685-24003d21374b.png)  


### 三个基本命令
***  
![image](https://user-images.githubusercontent.com/96570699/192137656-97d7eaab-bf30-4543-993e-1e65df0bca13.png)  
![image](https://user-images.githubusercontent.com/96570699/192137727-5e63e239-346b-4475-8d01-b5092cc5be0f.png)  
muliti类似于sql中的start transaction，discard类似于sql中的rollback。    
![image](https://user-images.githubusercontent.com/96570699/192137790-764232e3-77c0-404a-86c5-c01547836e97.png)  
这个queued就是表明命令已经放到队列当中等待被执行。  
![image](https://user-images.githubusercontent.com/96570699/192138018-cc4ee67e-3e16-4756-a95f-1bd57321caf7.png)  
两个ok表明两条命令都执行成功。当执行玩exec之后，此前的事务就结束了，类似于commit。    
![image](https://user-images.githubusercontent.com/96570699/192138178-4ad768ff-1297-4bf2-ae8e-58bb1c580239.png)  
discard表明放弃组队。  


### 事务的错误处理
***  
![image](https://user-images.githubusercontent.com/96570699/192138318-ec666eb9-f7d2-4736-b27e-3c3391c7f304.png)  
![image](https://user-images.githubusercontent.com/96570699/192138348-5918096a-44f9-41ce-b95d-886f545276a0.png)  
![image](https://user-images.githubusercontent.com/96570699/192138835-510a875a-39d7-4a87-8c7a-a497c2b47492.png)  
**组队中有错误（都不能执行）**    
![image](https://user-images.githubusercontent.com/96570699/192138881-16b7a63d-d3a6-4491-8443-092e403ece0f.png)   
**组队中没错误（正确的执行，错误的不能执行）**   
![image](https://user-images.githubusercontent.com/96570699/192139221-1e419d7e-de6e-4d8f-b598-2dd5d2424d7e.png)  


### 事务的冲突问题
![image](https://user-images.githubusercontent.com/96570699/192140391-dc2d09e7-6186-4e4f-87bf-efe764688f6c.png)  
#### 悲观锁
***  
![image](https://user-images.githubusercontent.com/96570699/192140495-dbb8a29e-8d0d-4bd3-8449-9571bd6eac07.png)  
![image](https://user-images.githubusercontent.com/96570699/192140477-9411314c-16f8-4d72-84b9-daf0015f47bd.png)  
不能同时多个人进行操作，效率很低。  


#### 乐观锁
***  
![image](https://user-images.githubusercontent.com/96570699/192140665-188c29bf-c1cc-463e-bd9e-22f6b71ecb0a.png)  
![image](https://user-images.githubusercontent.com/96570699/192140678-a1c46bdf-9077-488b-b349-d5d26a96d7d6.png)  


### 演示
#### 乐观锁
*** 
![image](https://user-images.githubusercontent.com/96570699/192147640-735e5dc4-e59d-479c-825a-44f31a681b8b.png)   
![image](https://user-images.githubusercontent.com/96570699/192147613-bd3ffc2e-fe1c-48e8-97e8-14bac635ac15.png)  
![image](https://user-images.githubusercontent.com/96570699/192146599-9f67ffcf-5401-4220-b3e9-d76c64332afc.png)  
![image](https://user-images.githubusercontent.com/96570699/192147193-4f3186ee-2b40-4dd5-af74-b6b5c5fddf07.png)  
然后分别在两个终端执行multi。  
![image](https://user-images.githubusercontent.com/96570699/192147255-7e7ad38d-8156-4e60-89d2-73c9e6cacc88.png)  
在第一个终端中加一个值。  
![image](https://user-images.githubusercontent.com/96570699/192147301-ae3ee189-b231-42de-b892-8bee1a1da216.png)    
在第二个终端中也加一个值。  
![image](https://user-images.githubusercontent.com/96570699/192147338-6d08d390-a839-4ecd-8f7f-274ca54e2b63.png)  
在第一个终端中执行操作，变成110。  
![image](https://user-images.githubusercontent.com/96570699/192147370-34de382d-1e79-4cd6-a3fb-493ef760cee0.png)  
再回到第二个终端执行操作。  
![image](https://user-images.githubusercontent.com/96570699/192147418-2a376246-850e-4ba2-8158-f62fd3c2b0fd.png)  
为空，说明没有执行这个操作，这是乐观锁，第二个终端操作时版本号对不上没有进行操作。  


### 事务的三个特性
![image](https://user-images.githubusercontent.com/96570699/192147724-acff5b00-3ecf-4587-b448-4d864e273928.png)  




# 持久化
### RDB方式
![image](https://user-images.githubusercontent.com/96570699/192149793-96ec031a-836f-479e-ade7-3028d7bcb865.png)  





