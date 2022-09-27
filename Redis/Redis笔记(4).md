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
***  
![image](https://user-images.githubusercontent.com/96570699/192147724-acff5b00-3ecf-4587-b448-4d864e273928.png)   


# 持久化
### RDB方式
***  
![image](https://user-images.githubusercontent.com/96570699/192149793-96ec031a-836f-479e-ade7-3028d7bcb865.png)  
![image](https://user-images.githubusercontent.com/96570699/192322069-db6637af-ff04-4852-95c3-4bffb6304445.png)   
![image](https://user-images.githubusercontent.com/96570699/192322167-308156ac-25ce-475e-9270-52d245ebfdbd.png)  
![image](https://user-images.githubusercontent.com/96570699/192322271-d9117ca6-24ee-48bd-bb82-c59630e2b19b.png) 


### 设置
***  
![image](https://user-images.githubusercontent.com/96570699/192322646-42d1d0af-5c74-4ca7-9df8-26bff3fc692d.png)  
![image](https://user-images.githubusercontent.com/96570699/192322980-f6e14cca-c897-44ae-a306-e39d73ec15e4.png)  
![image](https://user-images.githubusercontent.com/96570699/192322732-cc7a936e-358e-4e16-b3d1-43f3b10a8ddd.png)  
![image](https://user-images.githubusercontent.com/96570699/192299286-91e132f0-c473-4d44-9a83-c057ba7f03b8.png)  
![image](https://user-images.githubusercontent.com/96570699/192299389-26b9e3a8-0d45-4d4f-8223-e16024a7ee84.png)  
当硬盘满了的时候，无法写入，就会关闭redis。  
![image](https://user-images.githubusercontent.com/96570699/192299707-d72eafbc-9bdb-45ff-8bcc-a3ef6406e23f.png)  
![image](https://user-images.githubusercontent.com/96570699/192299765-b915e7a9-e0fb-4999-919b-527fba37b363.png)  
![image](https://user-images.githubusercontent.com/96570699/192300260-da08857d-95dd-412f-8983-8925fef27f91.png)  
![image](https://user-images.githubusercontent.com/96570699/192300367-f674622b-b6bd-48ed-9d65-65e91f312d05.png)  
检查是否有损坏，因为有损坏的数据进行持久化是没有意义的。   
![image](https://user-images.githubusercontent.com/96570699/192302556-e66fe1bd-4554-48d5-8341-a5bdc4a362d4.png)  
![image](https://user-images.githubusercontent.com/96570699/192303100-633f6433-fbcb-44cb-bced-f143db425351.png)  
bgsave会自动保存。  
当设置30秒更新三个key进行持久化操作，当在第20秒时就更新了三个key，此时就会进行持久化操作，并重新开始计时。  
设置在20秒内更新3个key就会进行持久化操作，当在20秒内更新了超过这个值的数量key后，就会将这5个值进行持久化操作，并重新开始计时。 
![image](https://user-images.githubusercontent.com/96570699/192309177-1c4bdba8-f629-41aa-92e5-167170958c1a.png)  
![image](https://user-images.githubusercontent.com/96570699/192308439-da9ef50b-a0df-47fa-930d-f5cdbeb3f1f2.png)  


### 特点
***  
![image](https://user-images.githubusercontent.com/96570699/192314752-092c9ab0-309d-490d-a62d-c2a8020c5f1a.png)  
数据可能会丢失是因为在还没到持久化的时间时服务器挂掉了，此时还没有备份，则哪些数据就会丢失。  
![image](https://user-images.githubusercontent.com/96570699/192314821-9f3b89d7-508b-4d5b-9ea0-d9452f723ab2.png)  


### rdb备份过程
***  
将备份的文件备份好，当redis挂掉之后重启就会在备份位置找该文件进行恢复操作。  
![image](https://user-images.githubusercontent.com/96570699/192320417-23e3e5d4-5771-4a89-84c7-94b059c61f0f.png)  




### AOF方式
***  
![image](https://user-images.githubusercontent.com/96570699/192441664-4a73685e-eb33-47b7-a2a4-4de422b42be8.png)  
所有的增删改操作。  
![image](https://user-images.githubusercontent.com/96570699/192447755-d8701a58-a7bd-4604-9a2b-7ea669cf4381.png)  
![image](https://user-images.githubusercontent.com/96570699/192451220-35677031-0629-4f47-8e00-a77ef927a9d3.png)  
![image](https://user-images.githubusercontent.com/96570699/192447916-dc38f92b-1eb1-4cbe-9381-16e50deaea2f.png)  
![image](https://user-images.githubusercontent.com/96570699/192451360-4b14659f-f328-4ce5-8b32-3621119f11c3.png)  
文件的生成位置和rdb文件的生成位置一致。  


### AOF备份过程
***  
![image](https://user-images.githubusercontent.com/96570699/192452592-9ea3d7d6-a0ce-4be3-8db3-12cb3335a502.png)  
![image](https://user-images.githubusercontent.com/96570699/192453482-cfee76f7-8819-4ec5-bfa9-1ddbb72892f9.png)   
跟RDB方式一样，都是备份好文件然后重启就会在备份位置找该文件进行恢复操作。  
![image](https://user-images.githubusercontent.com/96570699/192453762-cb70a94f-4ee8-4958-ae79-6aaf31b92498.png)  
![image](https://user-images.githubusercontent.com/96570699/192455059-e951c629-9a79-415d-86a8-21bd71ee01c3.png)  
当备份文件里面有错误的时候，连接就会拒绝。  
![image](https://user-images.githubusercontent.com/96570699/192455331-414f2f1e-e98e-4f8d-9e95-5d3bc71739ce.png)  
执行修复文件后，就会将比对结果在命令行上显示出来，输入y就会进行修复。  


### 设置
***  
![image](https://user-images.githubusercontent.com/96570699/192456626-8800ef37-4d83-42be-9804-02aa332f8994.png)  
![image](https://user-images.githubusercontent.com/96570699/192457243-f9442b51-2c0d-4315-aaf6-b50d87ed1448.png)  
![image](https://user-images.githubusercontent.com/96570699/192457321-8a70d240-2745-420e-bf1f-0a4b69ce4bd3.png)  
![image](https://user-images.githubusercontent.com/96570699/192457588-e92cce67-1710-474c-bdb4-f4294a691c4c.png)     
![image](https://user-images.githubusercontent.com/96570699/192458096-b824d835-f5ea-4c5b-9da0-ce238ece98b3.png)   
重写是将之前的各种操作压缩成一条语句，中间的其他查找查询都忽略。
![image](https://user-images.githubusercontent.com/96570699/192458208-3d3c68fd-1dc0-4c34-b5f9-99a388b96da8.png)  
![image](https://user-images.githubusercontent.com/96570699/192458305-25f6fcda-a409-4931-ab00-8509ec4a338a.png)  
意思是大于64m的一倍，就是128m。  
![image](https://user-images.githubusercontent.com/96570699/192458626-77f14792-4ccf-4778-899e-c302283c2f28.png)  
**重写流程**  
![image](https://user-images.githubusercontent.com/96570699/192458958-53168e10-f11d-4849-8f38-403346a99177.png)  


### 流程
***  
![image](https://user-images.githubusercontent.com/96570699/192459243-4ca89d63-f76d-4384-9ec9-13a1e7ecefe9.png)  
![image](https://user-images.githubusercontent.com/96570699/192459873-7c10f018-6165-4a0c-9d2d-9a6bd27e7abc.png)  


### 特点
***  
![image](https://user-images.githubusercontent.com/96570699/192460023-9c4084fa-90e1-431d-b364-77f4e4dabfaa.png)  
![image](https://user-images.githubusercontent.com/96570699/192460063-90745c7b-5051-4a60-a68d-998bf1ba6f0d.png)  
因为它记录的是你的操作，不是数据，所以需要更多的空间，并且记录东西多，恢复速度比较慢。  
![image](https://user-images.githubusercontent.com/96570699/192460452-df01e82d-fcb1-46cc-8307-37cb473e1074.png)  


### 总结
***  
![image](https://user-images.githubusercontent.com/96570699/192460676-38298342-024d-4beb-810b-2b2b87e1738b.png)  
![image](https://user-images.githubusercontent.com/96570699/192460894-fab6a446-a570-4fc6-b593-17225cc471de.png)  

