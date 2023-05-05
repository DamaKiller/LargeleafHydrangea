# 函数
![image](https://user-images.githubusercontent.com/96570699/234754125-16030a51-f924-4814-b6e5-6f0d396fd9de.png)  
![image](https://user-images.githubusercontent.com/96570699/234764941-4d3407a2-d7aa-4540-ab5a-a6684dc57eef.png)　　
**注**  
![image](https://user-images.githubusercontent.com/96570699/234766678-8945c6ae-cec6-4eff-84dc-6021451dabfc.png)  
![image](https://user-images.githubusercontent.com/96570699/234766719-3c38d08b-b9d3-4a7b-a811-70a41dd9276c.png)  
JS不传参调用会发生上面这种情况，为了避免发生上面这种情况可以给形参指定默认值。  
![image](https://user-images.githubusercontent.com/96570699/234767421-6c94ec8f-8f95-43ac-a02b-e7160fb44424.png)  
![image](https://user-images.githubusercontent.com/96570699/234769753-16084df5-f1d3-4bc5-a889-f180ad7f3bb8.png)  
![image](https://user-images.githubusercontent.com/96570699/234771673-db12fea0-beb6-4a64-9059-360957ac1780.png)  
**注**  
![image](https://user-images.githubusercontent.com/96570699/234784015-c61c0664-b02e-4449-a212-bbfcea19822f.png)  
此时num的值变成10，注意不要反这种错误，不加let相当于在全局作用域中操作。  
![image](https://user-images.githubusercontent.com/96570699/234784698-35e138d5-0ee4-4137-bb3c-c0c46a87b36e.png)  
但是这样就没问题，它们在各自的局部作用域中操作，在本作用域中不存在该变量就会逐级向上查找。   


### 匿名函数
![image](https://user-images.githubusercontent.com/96570699/234786229-66f16caf-0959-4942-8f69-98f119602776.png)  
![image](https://user-images.githubusercontent.com/96570699/234786611-ae6778ac-7f9b-46c8-a2d7-0a7961ebaad1.png)  
![image](https://user-images.githubusercontent.com/96570699/234787522-e3558e39-c246-4396-82c1-a6982a367d90.png)   
![image](https://user-images.githubusercontent.com/96570699/234788849-e926c06c-cba5-4ca8-894c-2768b6a3ac4b.png)  
![image](https://user-images.githubusercontent.com/96570699/234789748-ca981f2b-d7f4-4842-94c4-74230501a3f0.png)  
第二个括号本质上是在调用前边的函数，后必须加分号隔开，这种执行方式两个括号内部是两个局部作用域，防止了变量污染。    
![image](https://user-images.githubusercontent.com/96570699/234790835-6b0ebd03-e516-4bb0-9c44-eb3cb140b706.png)  
![image](https://user-images.githubusercontent.com/96570699/234791259-f4eeeb9a-185b-4577-9668-61db517a6a01.png)


### 逻辑中断
![image](https://user-images.githubusercontent.com/96570699/234797264-1e5be529-946e-46ba-b225-2b14d0f844b7.png)   
![image](https://user-images.githubusercontent.com/96570699/234797577-a77c2e01-25dd-4c33-a7a4-faa01978a42f.png)     
就是利用短路来赋值。    
![image](https://user-images.githubusercontent.com/96570699/235106102-8f6c2802-7b2f-41d3-9989-723e9c2b9204.png)  
![image](https://user-images.githubusercontent.com/96570699/235108238-895675a4-342e-49a9-a523-7c0765bd9b8f.png)  


# 对象
![image](https://user-images.githubusercontent.com/96570699/235109719-ad2ff15c-6647-41d0-a9ab-81fcffbfb8ba.png)  
![image](https://user-images.githubusercontent.com/96570699/235110277-b39a7701-58a7-42c0-95f4-cf0c0c6adb01.png)  
![image](https://user-images.githubusercontent.com/96570699/235110996-8591e999-faf8-4a21-b38e-98e6f3aa41ea.png)　　
![image](https://user-images.githubusercontent.com/96570699/235111310-3fcc1c86-833d-48b1-8ff0-fd35a6f8ac0e.png)　　
![image](https://user-images.githubusercontent.com/96570699/235112697-604d69ca-810a-4eb5-9c79-7357565828ac.png)　　
![image](https://user-images.githubusercontent.com/96570699/235113471-e7661505-ce7a-45c8-8020-3b4dc1b8ac87.png)　　
![image](https://user-images.githubusercontent.com/96570699/235113947-ae6cebda-0465-421d-84ad-3179e48e17c1.png)　
![image](https://user-images.githubusercontent.com/96570699/235114558-48b28b5a-c9ba-4a7e-ac2f-8b272a601bd8.png)　　
![image](https://user-images.githubusercontent.com/96570699/235114698-263eef2d-1e68-493a-8bf3-6a6c10574e1f.png)　　
![image](https://user-images.githubusercontent.com/96570699/235117164-a73b2e6b-13ed-43d4-95ec-5b7c5699569e.png)　　
![image](https://user-images.githubusercontent.com/96570699/235118294-c4f4a843-58be-4b5f-b978-5b894440cdd5.png)　　
![image](https://user-images.githubusercontent.com/96570699/235120560-3c044be6-1dd4-46d0-8daa-2f9a0344d54e.png)　　
![image](https://user-images.githubusercontent.com/96570699/236091347-ea7b9797-6bba-4168-aec9-3193c3f1765d.png)　　　

![image](https://user-images.githubusercontent.com/96570699/236096099-cfbe694b-896f-4787-ba09-9ae75fa20ac8.png)　　
![image](https://user-images.githubusercontent.com/96570699/236096388-11269a9e-5049-4a76-8e11-21318a0f88cc.png)　　
![image](https://user-images.githubusercontent.com/96570699/236097982-7dc14181-877e-4794-95e1-5e046e4f9cc2.png)　　
想取整数就用向下取整函数即可。  


# 基本数据类型和引用数据类型
![image](https://user-images.githubusercontent.com/96570699/236101278-c8c301c1-cf6d-44bd-a507-fd9d620b23d1.png)  
const创建的引用数据变量是可以往里面增加或删减值的，其实是const创建的对象的地址不可变。   












