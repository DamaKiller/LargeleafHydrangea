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
![image](https://user-images.githubusercontent.com/96570699/200790037-92f7455f-81df-4bc3-aca7-1e0e68369d5e.png)   


### 构造方法
***  
![image](https://user-images.githubusercontent.com/96570699/200791013-48fcd0d4-7cf0-4812-a4a1-9e541b758180.png)  
![image](https://user-images.githubusercontent.com/96570699/200792797-42b2c7ba-7d4f-49c1-a18d-343c341a09ef.png)  
![image](https://user-images.githubusercontent.com/96570699/200793595-8d853892-4f0e-4df4-8e29-afc15d343390.png)  
传入参数就会调用带参构造，给成员属性赋值，不传入参数就会调用空参构造，一般两种构造方法都要写。  
![image](https://user-images.githubusercontent.com/96570699/200794360-6476cd24-61d6-4601-8898-0af6bf027a0e.png)   
![image](https://user-images.githubusercontent.com/96570699/200795117-7fb62e98-27e7-455a-891f-9524abd22ab5.png)  
![image](https://user-images.githubusercontent.com/96570699/200795430-be3b1cbc-87a6-45fd-942b-7c3cfefa3cf9.png)   


### 标准的JavaBean类
***  
![image](https://user-images.githubusercontent.com/96570699/200987811-41604f1c-aab1-4354-8ece-4e8ac749ea7e.png)  
![image](https://user-images.githubusercontent.com/96570699/200991176-7444f487-5903-42aa-a28b-06aaa279e7a5.png)  
Java Bean是编写胶水代码的惯用模式或约定。这些约定包括getXxx、setXxx、isXxx、addXxxListener、XxxEvent等。遵守上述约定的类可以用于若干工具或库。   



# 字符串
***  
![image](https://user-images.githubusercontent.com/96570699/201052705-d9eca90e-48b8-4790-99ce-14db9e45f7e9.png)   
![image](https://user-images.githubusercontent.com/96570699/201247879-0c54fd77-1cb5-4668-8b1a-04e29ab5ca59.png)  


### StringBuilder
***  
![image](https://user-images.githubusercontent.com/96570699/202139445-646ca01c-4679-4bf1-b113-45055d390904.png)  
![image](https://user-images.githubusercontent.com/96570699/202140039-957bf5dc-9e25-40f3-901b-522d193b8b91.png)  
![image](https://user-images.githubusercontent.com/96570699/202140266-56ae50a2-b13f-4e8a-b685-068b5a888a96.png)  
![image](https://user-images.githubusercontent.com/96570699/202140752-a19e3218-ee70-4343-ab62-c86c5f3e81c1.png)   
再往容器中添加字符串就会添加再'ABC'的后面。  
![image](https://user-images.githubusercontent.com/96570699/202141545-fc81cc4f-53b6-4de0-906d-8d363990acc1.png)  
![image](https://user-images.githubusercontent.com/96570699/202144046-acd8c395-75e7-42d0-8769-6c4d6a0e5093.png)    
![image](https://user-images.githubusercontent.com/96570699/202144140-b8bec5ab-a954-4a4b-8916-c6105ee93c9a.png)  
**结果**  
![image](https://user-images.githubusercontent.com/96570699/202144293-07885dac-0c27-4979-9f13-d302724431c3.png)  
**结果**  
![image](https://user-images.githubusercontent.com/96570699/202144345-9fbb4e36-a8ae-4c42-a873-67fbf700dc4e.png)  
![image](https://user-images.githubusercontent.com/96570699/202144677-a5fe5035-b684-4be3-81b5-a3f71f0fdafe.png)  
 **注**  
 使用完之后要将他变回字符串类型。  
![image](https://user-images.githubusercontent.com/96570699/202145663-4a86dec0-bee2-4521-89a5-83baa0e469c1.png)   


### StringJoiner
***  
![image](https://user-images.githubusercontent.com/96570699/204950080-230ec11f-8136-41e0-a87a-e5e96eb2d28c.png)  
![image](https://user-images.githubusercontent.com/96570699/204950144-4ac03aa6-6db1-4a6c-b7c9-b43423f70043.png)  
![image](https://user-images.githubusercontent.com/96570699/204950213-51ae26f0-2886-466a-80de-f069bd70d3c4.png)  
![image](https://user-images.githubusercontent.com/96570699/204951300-83b05c2f-7de6-4d2d-9ade-c6874ff322cf.png)  


### 字符串原理
***  
![image](https://user-images.githubusercontent.com/96570699/204952427-c6565026-902e-4115-9590-c0fb0a53a339.png)  
![image](https://user-images.githubusercontent.com/96570699/204952790-629f2126-ae53-48cd-88e5-f68805791d9c.png)  
![image](https://user-images.githubusercontent.com/96570699/204953792-57ccbc27-2346-47e9-8e7d-def4c0aed9b4.png)  



