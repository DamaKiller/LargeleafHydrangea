# 有序集合
***
![image](https://user-images.githubusercontent.com/96570699/191677593-81a2c138-7214-4901-8338-e23584219fc2.png)  


### 常用命令 
#### zadd命令
***  
![image](https://user-images.githubusercontent.com/96570699/191678207-b6949a2f-3109-4e48-a164-8c59831e1536.png)  
![image](https://user-images.githubusercontent.com/96570699/191678772-ea2dd055-8eac-496a-a107-ac2755f825eb.png)  
![image](https://user-images.githubusercontent.com/96570699/191678444-91a1db7a-dbba-42b1-9c5a-a999a711dea4.png)  


#### zrangebyscore和zrevrangebyscore命令
***  
![image](https://user-images.githubusercontent.com/96570699/191679630-71a87566-57ed-480f-8a15-a9b7ef6b6532.png)  
![image](https://user-images.githubusercontent.com/96570699/191679092-f5079ff1-70b6-4043-a79a-f3b535e19b24.png)  
改命令会自动从小到大排列。  
![image](https://user-images.githubusercontent.com/96570699/191679480-e11bf807-8b4b-41a0-b3a0-ff939fb0b6a2.png)  


#### zrem，zcount，zank命令
***  
![image](https://user-images.githubusercontent.com/96570699/191683301-462c866b-715f-40bd-9b8d-36db61611d9a.png)  
![image](https://user-images.githubusercontent.com/96570699/191682974-398062fb-5b87-49fc-991e-e0cde0ff1bb0.png)  
![image](https://user-images.githubusercontent.com/96570699/191683097-87aa9bc1-76f9-4152-8aa0-bd35d28cbc96.png)  


### 数据结构
***  
![image](https://user-images.githubusercontent.com/96570699/191684074-8b14fa05-3a4a-4a90-902c-6badab0966f8.png)  
![image](https://user-images.githubusercontent.com/96570699/191684366-579ca651-0208-4907-9fd0-d9bab512615d.png)  
![image](https://user-images.githubusercontent.com/96570699/191684893-7f837af7-9762-46fb-aa74-f17fb7fc445a.png)  
![image](https://user-images.githubusercontent.com/96570699/191685078-4f0221f8-12de-43c9-95d0-cd3c4ebe4f0f.png)  




# 配置文件详解
### redis.conf(redis.windows.conf WINDOW系统下的文件名)
***  
![image](https://user-images.githubusercontent.com/96570699/191701348-77e44b6b-2df2-46a5-acd8-d6b40aec6a36.png)  
![image](https://user-images.githubusercontent.com/96570699/191693792-21d5dfe9-9647-4c69-9588-541f55b0436c.png)  
这部分是redis中一些单位的设置方式。   
***  
![image](https://user-images.githubusercontent.com/96570699/191702668-fab7177e-b35e-4da5-be31-c52b26595c5c.png)  
如果不改，则只能通过本地进行访问。想要进行远程连接只要将其注释掉就可以了，然后重启服务。    
***  
![image](https://user-images.githubusercontent.com/96570699/191704393-a5451dcb-dede-4d70-8448-6b07a9820cef.png)   
这个设置需要结合blind设置一块设置，设置完之后就可进行远程访问。  
***  
![image](https://user-images.githubusercontent.com/96570699/191705341-16ac3bcf-ef84-480a-8e98-b45ed533e9ba.png)  
***  
![image](https://user-images.githubusercontent.com/96570699/191705558-8b0ea997-52ea-4332-9869-12176b8c02de.png)  
![image](https://user-images.githubusercontent.com/96570699/191705678-9d6306d0-28f3-45cd-b51b-fe876170d1f9.png)  
默认为511。    
***  
![image](https://user-images.githubusercontent.com/96570699/191706395-f7f9b7cc-b265-41e5-8178-a954fba6be27.png)  
设置多长时间不操作退出，默认为0永不超时，以秒为单位。  
***  
![image](https://user-images.githubusercontent.com/96570699/191709007-45dfbd1b-25bf-4cc1-b7e1-7b39f2582049.png)  
每过多长时间进行检测，检测连接是否有操作，没有则关闭。  
***  
![image](https://user-images.githubusercontent.com/96570699/191709910-3cdf3018-36e2-42ab-a137-6225986e5d5d.png)  
***  
![image](https://user-images.githubusercontent.com/96570699/191710455-2ae4c38d-91cf-4bc0-b750-152d904dc9db.png)  
设置redis的log等级。  
***  
![image](https://user-images.githubusercontent.com/96570699/191711136-7bacd081-1370-4216-a82b-13099dba130a.png)  
设置log文件输出路径。  
***  
![image](https://user-images.githubusercontent.com/96570699/191712030-641bba9f-a9e3-49ed-89d1-5c082346cac6.png)  
设置默认数据库数量。  
***  
![image](https://user-images.githubusercontent.com/96570699/191712713-53a01ed8-ff58-430d-a090-292962123c1e.png)  
设置密码。
***  
![image](https://user-images.githubusercontent.com/96570699/191713271-ebd43f63-26fc-4e2e-ac25-0b6e74da3ba5.png)  
***
![image](https://user-images.githubusercontent.com/96570699/191713548-86e88134-89b3-411b-b74e-ce3395e598c4.png)  
***
![image](https://user-images.githubusercontent.com/96570699/191714537-fc574755-4cd4-4992-8478-4f575ae9d4f7.png)  
***




# 发布和订阅
### 简绍
***  
![image](https://user-images.githubusercontent.com/96570699/191917036-9d8eab32-7dad-4af0-b414-f30772ca7caf.png)   

