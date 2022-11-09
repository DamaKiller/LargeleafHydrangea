# 面向对象
### 类
***  
![image](https://user-images.githubusercontent.com/96570699/200767500-0f109079-f561-4d1e-b321-1d1583c48a89.png)  
![image](https://user-images.githubusercontent.com/96570699/200767873-221fa7c4-e96c-4da9-9e9c-1cd6d98012fd.png)  
![image](https://user-images.githubusercontent.com/96570699/200768187-28fbf311-825d-46db-b0e2-fa1a8245f8e4.png)  
![image](https://user-images.githubusercontent.com/96570699/200768489-f0880d9b-0efe-4553-a28f-4962adbc3cb0.png)  
![image](https://user-images.githubusercontent.com/96570699/200769244-f57fbca5-a52d-4487-93c9-8d602ea4ba86.png)  
![image](https://user-images.githubusercontent.com/96570699/200769959-1768b35e-8ef3-486b-9b56-2864876f0bba.png)  
若给成员属性添加了值，则以后创建的对象该属性都为该值，所以不建议。  
![image](https://user-images.githubusercontent.com/96570699/200770209-9a93c249-4536-4eda-b7cf-a28dac06348c.png)  


### 封装
***  
![image](https://user-images.githubusercontent.com/96570699/200773595-1e046112-3c88-41d2-b390-a3991e2882c5.png)  
![image](https://user-images.githubusercontent.com/96570699/200776247-e333c84f-b3a6-4d27-8a87-58dcae69897c.png)  
比如人关门，开门和关门的两个行为要定义在门这个对象中，因为人只是给了门一个作用力，而门开着还是关着是门自己的状态。  
![image](https://user-images.githubusercontent.com/96570699/200777821-31f3a068-3ca2-4fb6-b64f-733e7a33f502.png)  
![image](https://user-images.githubusercontent.com/96570699/200779538-3b246c5f-f5fa-4964-9384-1f6eefeab8da.png)  
![image](https://user-images.githubusercontent.com/96570699/200780673-2ba8d39b-a91d-460f-b4f7-ffb13995ba89.png)  
可以设置一个set和get方法来对成员属性进行设置和查找，这样就可以对成员属性的合法性进行校验，加了private之后，外面就不能对它进行更改，只能调用类中的方法对它进行更改。  
![image](https://user-images.githubusercontent.com/96570699/200784175-f3f8b996-64cd-4dcb-bbe2-8e460a488848.png)  


### this
***  
![image](https://user-images.githubusercontent.com/96570699/200785584-9aab5d08-310a-4158-94a7-7287ad666890.png)   
Java当不加this时，当成员和局部属性名字一样时，会采用就近原则，哪一个近输出哪一个，加上this后就会输出成员属性当中的值。  






