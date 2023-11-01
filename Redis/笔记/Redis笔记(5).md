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



### 薪火相传
打个比方，就是一个经理管理20来个人，但是他肯定没有这么多精力，所以他可以指派小组长，让小组长来帮他管理。就是他管理两个小组长，然后这两个小组长来管理剩下的组长，这样经理直接管理的人就
两个。在redis中就是主服务器管理两个从服务器，这两个从服务器再去管理其他的服务器，来减轻最开始那个主服务器的压力。但是这也带来了当主服务器挂掉之后剩下服务器瘫痪的问题，但是只要主服务器重启成功，之后就会正常。  
**如何实施：** 一个从服务器下再接一个从服务器。  


### 反客为主
就是主服务器挂掉之后，从服务器升为主服务器，但是必须在主服务器挂掉之后，才能用该方法。  
![image](https://user-images.githubusercontent.com/96570699/195120932-730a1b4d-6564-4861-9a16-e81e13acf8ab.png)  
![image](https://user-images.githubusercontent.com/96570699/195121310-6cdb2a72-0e33-40eb-b477-5f3beab5525d.png)  


### 哨兵模式
![image](https://user-images.githubusercontent.com/96570699/195125695-f371f3ac-0613-42f4-a31b-d11df2b6d66f.png)  
  
**如何配置**  
先搭建完主从服务器。  
![image](https://user-images.githubusercontent.com/96570699/195130710-dc172cc0-8449-4d3e-b335-9a3da81f3807.png)  
1表示有多少个哨兵同意才会切换成主服务器，2就是两个哨兵都同意才会切换。  
![image](https://user-images.githubusercontent.com/96570699/195131710-8b0d6262-fb30-42d2-8f0d-60dcd6324765.png)  
用这个命令启动新建的哨兵文件。  
![image](https://user-images.githubusercontent.com/96570699/195131883-5952ff90-50c1-42ce-926e-b9e10d24f013.png)  
底下为监控的服务器信息，包括它的主机和从机信息。  
![image](https://user-images.githubusercontent.com/96570699/195132553-e07336d8-bf0c-47e0-b9aa-72fc2554db98.png)  
![image](https://user-images.githubusercontent.com/96570699/195133072-9da37907-f448-4103-a516-a2cd7663789a.png)  
当主服务挂掉之后，哨兵就会选出新的主机首先是主机挂掉的信息，之后就会有新主机的信息。  
![image](https://user-images.githubusercontent.com/96570699/195133594-e2b71f5e-ff28-4b5d-8f5c-d7c7e443f830.png)  
![image](https://user-images.githubusercontent.com/96570699/195133837-c77a10d0-f70c-4ff7-9723-8de4b20e0648.png)  
当主服务器重启之后它会变成从服务器，不会变成主服务器。  
![image](https://user-images.githubusercontent.com/96570699/195137711-08501b82-82da-4fb3-8108-bc4d6aefbb81.png)  
![image](https://user-images.githubusercontent.com/96570699/195138105-577e9f21-9fa5-48a2-8b5d-870da78850a3.png)  
![image](https://user-images.githubusercontent.com/96570699/195139337-056d5631-ddb1-49fd-ba39-6f167e68b31f.png)  
6.0版本中改成下面这个。  
![image](https://user-images.githubusercontent.com/96570699/195139543-f6c23c16-326b-469b-9943-a18d3f4d7db2.png)  


