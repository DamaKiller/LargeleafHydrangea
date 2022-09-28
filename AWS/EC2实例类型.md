# 实例类型
![image](https://user-images.githubusercontent.com/96570699/192721373-b95c8898-8c81-4acb-8852-5df08658c95e.png)  
T类型是突发性的实例，cpu不是满性能的，他有一个基准性能，在基准性能比较低的状态运行时会累计一个积分，当遇到突发状况时，会用积分抵扣，
来提高性能，当积分用完，就会降到低性能来运行，比较适合小的项目，对性能没啥要求的。   
M就是标准型的实例。   
![image](https://user-images.githubusercontent.com/96570699/192722811-f28d012b-11cf-41fb-8b1a-f6560185131d.png)  
C代表计算优化型，5表示第五代（适用于其他实例，比如t2就表示第二代突发型），d表示加的格外功能（d是格外的ssd），'.'后面是是实例的大小18xlarge就是实例的大小。  
![image](https://user-images.githubusercontent.com/96570699/192729143-44a5e86e-4469-49e4-8cee-123a2e59095b.png)  
R代表内存优化型，很多种系统需要分享它的内存，需要一个超大的内存，就需要该类型。  
![image](https://user-images.githubusercontent.com/96570699/192729351-a522840b-cf41-450d-ad17-05cf57d05a4f.png)  
存储优化型，是为了存储大量的数据，就需要该类型，越往后性能越强。  
![image](https://user-images.githubusercontent.com/96570699/192729388-a0335b03-a17c-4cbf-99a9-83681682eab9.png)  
该类型是为了需要机器学习，深度计算准备的，FEGA是给半导体用的。  
