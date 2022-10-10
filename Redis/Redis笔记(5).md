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


### 常用场景
#### 一主两从
当从服务器挂掉重启之后它就会变成主服务器，并不会接着是以前的从服务器。  
![image](https://user-images.githubusercontent.com/96570699/194907129-99ab71fa-a83e-4b9e-8050-9113d0252b6a.png)  
需要将它重新关联到之前的主服务器上，之前主服务上写入的数据也会从头开始复制，不会出现挂掉之后主服务器上写入数据重新关联之后就没有的情况。  
![image](https://user-images.githubusercontent.com/96570699/194907323-45c1648b-be94-49d8-9627-a2c10141f50c.png)  
![image](https://user-images.githubusercontent.com/96570699/194907621-f0185f99-0d12-4c03-8bcf-124c57d28f60.png)  
当主服务器挂掉之后，从服务器还是从服务器，不会变成主服务器，只是主服务器状态哪里变成down。  
![image](https://user-images.githubusercontent.com/96570699/194908159-9f9a6f93-595e-403e-9fb6-96b139b9e30f.png)  
主服务器重启之后它还是会回到主服务器的状态，并且和从服务器的关联也没有断。  
![image](https://user-images.githubusercontent.com/96570699/194908652-d2737969-0bcb-4ee0-9dad-71d6ec9e2748.png)  
**原理**  
![image](https://user-images.githubusercontent.com/96570699/194913232-79d9cdd1-7cb2-49ad-9dd6-45b6df34fa34.png)  
之后都是主服务器主动去和从服务器同步。  


