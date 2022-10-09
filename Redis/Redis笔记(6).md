# 缓存穿透
***  
![image](https://user-images.githubusercontent.com/96570699/194767722-2999fdb7-20f7-4fb6-81f4-56dc2cf961ef.png)    
突然间有大量的访问数据库请求，并且redis中大部分都查不到，就去查询数据库，造成数据库压力过大崩溃，这就是缓存穿透。  

### 如何产生
1.redis查询不到数据。  
2.非正常的访问，比如大量搜索不存在的key。这种情况可能遭到了攻击。    


### 解决方案
![image](https://user-images.githubusercontent.com/96570699/194768098-16f67e6e-6b18-49c8-9178-21ca4ba74ec4.png)  
![image](https://user-images.githubusercontent.com/96570699/194768251-09bc12cf-06ff-4b90-a77f-82ed07e6e0cf.png)  




# 缓存击穿
### 现象
![image](https://user-images.githubusercontent.com/96570699/194768411-6c8ab37c-dce0-47d2-820f-8828b60fe6cb.png)  
数据库突然遭到大量的访问，但是redis中并没有出现出现大量key过期的现象，并且redis正常运行。  


### 原因
1.redis中某个key过期，但之后突然大量访问这个key，此时redis中不存在这个key，所以只好去访问数据库。  、


### 解决方案
![image](https://user-images.githubusercontent.com/96570699/194768755-a97c923e-1bd6-4e33-80a8-fd614bb1f1eb.png)  
![image](https://user-images.githubusercontent.com/96570699/194768868-36f1e9b5-23db-47da-8709-e57eabdf58bb.png)  
![image](https://user-images.githubusercontent.com/96570699/194768844-acfd24a1-f8b8-481c-9f25-1c0962b33b40.png)  
使用锁一定会降低效率。  




# 缓存雪崩
![image](https://user-images.githubusercontent.com/96570699/194768952-072586d3-fffe-4078-a658-5318d7e363f0.png)  
和击穿的区别是击穿是某个热门key过期，而雪崩是大量key过期。  


### 解决方案
![image](https://user-images.githubusercontent.com/96570699/194769173-2d05ff82-eacd-4f7a-b047-a1a1366b0fd6.png)  
![image](https://user-images.githubusercontent.com/96570699/194769246-ce99c17e-f903-473e-ab1f-bb44718a01d7.png)  


