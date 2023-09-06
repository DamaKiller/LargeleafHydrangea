# JDK和JRE
***   
![image](https://user-images.githubusercontent.com/96570699/198244541-36a8a104-0c4b-4b45-967c-8b3aca4623f1.png)  
![image](https://user-images.githubusercontent.com/96570699/198245874-bd5d12a3-5f71-4df3-8936-090cdd8fffd7.png)  
![image](https://user-images.githubusercontent.com/96570699/198246450-f4610c77-91c1-4b6b-9a92-29dc74e24a13.png)  
![image](https://user-images.githubusercontent.com/96570699/198246888-fba28b76-ba2f-432d-9301-2397206260f3.png)  
![image](https://user-images.githubusercontent.com/96570699/210710212-f305ada6-7b8f-46e3-a5dc-ee373cabcbd6.png)  



# 注释
***  
![image](https://user-images.githubusercontent.com/96570699/198247637-c1511aa3-2859-47ac-92c5-1e96321b088d.png)  


# 关键字
***  
![image](https://user-images.githubusercontent.com/96570699/198250192-5624bbc3-1554-4ce2-9e05-643500be9349.png)  
![image](https://user-images.githubusercontent.com/96570699/198250563-bd3b32a7-08d3-4934-91e1-f6da0128ca06.png)  
![image](https://user-images.githubusercontent.com/96570699/198251315-0256b770-0271-43fe-9e17-6117cfcd6dca.png)  
一个编译单元（java文件）可以存在多个类，在编译时产生多个不同的.class文件，.class文件便是程序运行的数据来源。java将public类作为每个编译单元的数据接口，只能有一个， 
并且public的类名必须与文件名相一致。不然不能处理存在多个类的java文件。当一个编译单元（java文件）有多个非public类时，此类可以跟文件名不同，运行时需要对数据来源进行选择。   


# 标识符
自己定义的内容，比如类名，方法名，变量名被称为标识符，HelloWorld案例当中，类名HelloWorld就是标识符。  
![image](https://user-images.githubusercontent.com/96570699/210716439-62d6b7f8-fc3c-41eb-b380-45932fffcec4.png)   


# 常量
***  
![image](https://user-images.githubusercontent.com/96570699/198254412-6c162d70-68ee-4ca8-ab2b-c00390dcd39d.png)  
![image](https://user-images.githubusercontent.com/96570699/198254683-17ec5f28-4f80-40b9-8f31-563841f43547.png)  


# Java中变量的定义方式
***  
![image](https://user-images.githubusercontent.com/96570699/198333851-3bde6342-1663-4649-860e-e9c29f1224e7.png)  
![image](https://user-images.githubusercontent.com/96570699/198336244-255b39c1-c9df-4808-b4aa-7bf33dd7b52f.png)   
![image](https://user-images.githubusercontent.com/96570699/198337171-27d76f4e-7f3b-4d52-82b9-fabf16d1808f.png)  


# 数据类型
![image](https://user-images.githubusercontent.com/96570699/210718596-41061230-4db7-4e85-882a-272246541506.png)  
![image](https://user-images.githubusercontent.com/96570699/210718870-8654651e-be98-4d6d-8150-2d97e63b156d.png)  
![image](https://user-images.githubusercontent.com/96570699/210719978-59225d34-d838-4a75-be60-5a3c52a19223.png)  
在定义long和float等类型时，因为java默认时int类型，所以在int的取值范围内不加L或F，java会自动转换成long或float类型，当超过了int的取值范围就必须要加L或F了。    


# 类的应用
***  
以键盘录入为例。  
![image](https://user-images.githubusercontent.com/96570699/199657892-8f690a6c-2463-4c54-a5eb-239510851ba0.png)   
**注：**   
main方法代表程序运行的起点。  


# 隐式转换和强制转换
### 隐式转换
***  
![image](https://user-images.githubusercontent.com/96570699/199689571-fe174fda-9f21-4707-914e-84b37da2b7e3.png)  
![image](https://user-images.githubusercontent.com/96570699/199690029-c174b3cb-fd05-4329-a1d4-c476f09c1aab.png)  
![image](https://user-images.githubusercontent.com/96570699/199690332-092550bd-776b-43de-b41f-f529fcc9b505.png)  
![image](https://user-images.githubusercontent.com/96570699/199690965-1ea7ae88-1bad-44ce-9dbe-fe2c165cea5e.png)  
char会转换成对应的asc码参与计算。  


### 强制转换
***  
![image](https://user-images.githubusercontent.com/96570699/199692441-4756a323-c20e-484e-9eef-66fb3c337a60.png)  
数据过大进行强转会发生错误(比如long类型转换成int类型，float转换成double类型等)。  
强转时会损失精度，比如12.4转换成int型时会变成12.  


# 运算符
***  
![image](https://user-images.githubusercontent.com/96570699/199869816-764e7c7f-6a20-4aa8-9609-8f5e5a8989a6.png)  
Java中整数和字符串相加会将整数转换成字符串然后再相加，布尔也是。 
![image](https://user-images.githubusercontent.com/96570699/199870147-aaae3f5b-08c7-41b5-aa1f-031291a87f93.png)  
![image](https://user-images.githubusercontent.com/96570699/199871614-54e44c87-aafb-4853-8367-8fde68536025.png)  
![image](https://user-images.githubusercontent.com/96570699/199872244-bf076485-ea92-43f4-aa14-d953ee7e91c6.png)  
自增自减运算符只能对变量使用，不能对常量使用，例如` 30++ `就是错误写法。  
![image](https://user-images.githubusercontent.com/96570699/199872548-395b2eaf-6e60-486c-8841-fc5b075ad64a.png)   
![image](https://user-images.githubusercontent.com/96570699/199872725-38458b07-4a89-406a-a80f-ed55402f8c47.png)  
![image](https://user-images.githubusercontent.com/96570699/199873458-cc454f7b-41d3-4a27-88c4-cbb84cd5ded8.png)  
![image](https://user-images.githubusercontent.com/96570699/199873889-7771d588-7e9f-42c1-a8c2-4a44b02d30cd.png)  
![image](https://user-images.githubusercontent.com/96570699/199874547-c1c3d1bb-2d4c-440c-9c4b-a0b9a7c82856.png)  
强转成什么类型取决于左边是什么类型。  
![image](https://user-images.githubusercontent.com/96570699/199875045-e121fe90-6715-47d3-9043-63438354250c.png)  
![image](https://user-images.githubusercontent.com/96570699/199875578-d805705f-b434-4173-b390-78d4f03aaa33.png)  
![image](https://user-images.githubusercontent.com/96570699/199877137-3aca967a-8f08-423f-85db-73ef2e078e7d.png)  
![image](https://user-images.githubusercontent.com/96570699/199898543-b6f35a8b-0b37-45fd-ba7b-979a8b73b7e3.png)  
![image](https://user-images.githubusercontent.com/96570699/212027275-79526bf4-629e-4f23-adbb-9c2eabfb419f.png)  
![image](https://user-images.githubusercontent.com/96570699/199899618-45aac1f3-9e29-4470-9d76-e3321f3dfd37.png)  
当一个取值范围小的数和一个取值范围大的数相加时，结果为取值范围大的数。  
