# 事务
![image](https://user-images.githubusercontent.com/96570699/192137565-a1948959-356e-4d5d-a685-24003d21374b.png)  


### 三个基本命令
![image](https://user-images.githubusercontent.com/96570699/192137656-97d7eaab-bf30-4543-993e-1e65df0bca13.png)  
![image](https://user-images.githubusercontent.com/96570699/192137727-5e63e239-346b-4475-8d01-b5092cc5be0f.png)  
muliti类似于sql中的start transaction，discard类似于sql中的rollback。    
![image](https://user-images.githubusercontent.com/96570699/192137790-764232e3-77c0-404a-86c5-c01547836e97.png)  
这个queued就是表明命令已经放到队列当中等待被执行。  
![image](https://user-images.githubusercontent.com/96570699/192138018-cc4ee67e-3e16-4756-a95f-1bd57321caf7.png)  
两个ok表明两条命令都执行成功。当执行玩exec之后，此前的事务就结束了，类似于commit。    
