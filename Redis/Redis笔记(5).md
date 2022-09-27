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


