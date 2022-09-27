# 主从复制
### 简绍
![image](https://user-images.githubusercontent.com/96570699/192503994-bb579fa9-da98-4cee-b887-8cf16a3cef88.png)  
![image](https://user-images.githubusercontent.com/96570699/192504054-28d3f12e-ec39-4055-a7c0-2281faa0bf9f.png)  
主服务器进行写操作，从服务器进行读操作，减轻服务器压力。  
多个从服务器可以在一个服务器挂掉后快速切换到另一个，提升稳定性。  
只能有一个主服务器，主服务器多了就不知道听谁的了。  
![image](https://user-images.githubusercontent.com/96570699/192504389-d502010f-6f59-4183-9aa0-d50fa476623c.png)  
当只有一台主机的时候，可以使用集群来解决，当一台主机挂掉，可以快速切换到另一个。  
![image](https://user-images.githubusercontent.com/96570699/192505888-2c657c91-0c9a-4987-aae1-62451d226b67.png)  


### 配置一主多从
![image](https://user-images.githubusercontent.com/96570699/192560216-8d2f35c4-3fe8-4fe4-b1dc-38a77c4f83ed.png)  
创建三个端口号不同的配置文件，include公共部分，。  
![image](https://user-images.githubusercontent.com/96570699/192558668-af75ea23-a5cd-4f41-8691-212cb715d1a9.png)  
通过改写include文件路径来实现继承公共部分。  
三个配置文件要如下这么写。  
![image](https://user-images.githubusercontent.com/96570699/192557888-270afd2a-8c1e-4a91-b14a-0dbfbdec222d.png)  
![image](https://user-images.githubusercontent.com/96570699/192557964-f71d3f76-aab7-4a06-a543-311a0e287add.png)  
![image](https://user-images.githubusercontent.com/96570699/192558022-49e118b4-040c-4a26-88f1-bc49e93dbc25.png)  
开启三个redis服务。  
![image](https://user-images.githubusercontent.com/96570699/192570357-9fe97686-837b-40a9-ba30-66d2c88dc8cd.png)  
查看三个redis服务是否启动。  
![image](https://user-images.githubusercontent.com/96570699/192570418-70f9ffb1-8050-4edc-83ab-fe9da1ccd054.png)  
可以通过该命令查看主从服务器信息。  
![image](https://user-images.githubusercontent.com/96570699/192571076-4ef771ab-4bc5-41b9-b193-cf0d0314debe.png)  
配置主从服务器关系，使之成为6379的从机。  
![image](https://user-images.githubusercontent.com/96570699/192571268-230ec920-26eb-48e5-8af0-40ac4429dd0a.png)  
![image](https://user-images.githubusercontent.com/96570699/192572023-b73c1856-6be3-491e-8b69-313eb0162bad.png)  
![image](https://user-images.githubusercontent.com/96570699/192572667-bdb48725-21e1-4272-97e0-66f274cb795d.png)  





