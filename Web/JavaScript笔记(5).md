# 事件
![image](https://user-images.githubusercontent.com/96570699/236617470-66167774-9508-4594-b233-e2cc3bf79aae.png)  
![image](https://user-images.githubusercontent.com/96570699/236617503-a60c5c97-1214-49b5-9277-58bae0054a72.png)  


### 事件监听的版本
![image](https://user-images.githubusercontent.com/96570699/236983210-71cd774f-c495-4401-95c8-1270c9fe0db6.png)  
![image](https://user-images.githubusercontent.com/96570699/236982938-e0e8c13c-5e68-4dc9-87e0-c05e9bdc990d.png)  
比如上面这个事件在下面再写一个同名的弹出22，上面那个弹出11的就会被覆盖。  


### 事件类型
![image](https://user-images.githubusercontent.com/96570699/236983863-74a4b1a3-51e1-46a2-9075-25f58b8727e3.png)  
获得光标举例就是在搜索框中点击时弹出下拉选项，就是获得光标事件。  
![image](https://user-images.githubusercontent.com/96570699/236986681-6eb10292-8670-48fc-8100-a4fc8b986fe4.png)    
![image](https://user-images.githubusercontent.com/96570699/236986705-19cb3968-00c4-4c79-918b-1f44cc261c35.png)  
这样就可以获得用户输入的内容。  


# 事件对象
![image](https://user-images.githubusercontent.com/96570699/236989615-3c4e08fb-6474-4c06-a5bd-24fa6fec7016.png)   
![image](https://user-images.githubusercontent.com/96570699/236990115-f5afebff-c6a0-4c3a-8692-bb13355bc476.png)  
![image](https://user-images.githubusercontent.com/96570699/236990266-cc3121dd-9c38-4655-91a3-979497c5a917.png)  
这就是点击事件返回的点击事件对象。   
![image](https://user-images.githubusercontent.com/96570699/236999423-1d696947-4acd-470b-85f1-8e1f18a08ab0.png)    
![image](https://user-images.githubusercontent.com/96570699/237000290-3a6483e7-834c-4d64-95e5-b8c9ad7cb500.png)    
这就是键盘事件返回的键盘事件对象。  
可以使用事件对象中的参数进行操作。  


# 环境对象
![image](https://user-images.githubusercontent.com/96570699/237007217-0b09e100-2404-4c47-bff8-7365ae9dd9ba.png)  
![image](https://user-images.githubusercontent.com/96570699/237006696-40196ac5-63b2-4e17-a974-cb79e766863d.png)  
在这里前面的window在平常时被省略了。  
**举例：**![image](https://user-images.githubusercontent.com/96570699/237007592-c7ba3bcd-98ce-4a02-890d-8b9fdc04f544.png)  
事件监听对象监听谁this就指向谁。  


# 回调函数
![image](https://user-images.githubusercontent.com/96570699/237008503-99b11f6a-9b08-4ec4-9e4a-52de58395715.png)  
一般用在就是满足条件就调用的函数上。   


# 事件流
![image](https://user-images.githubusercontent.com/96570699/237012748-a19cbe33-dafb-43ae-b56d-9943e82af87c.png)   
![image](https://user-images.githubusercontent.com/96570699/237014479-fcc2a918-d56b-47e3-b86d-a1cc9f56744f.png)   
一般都是用事件流。  


### 事件捕获
![image](https://user-images.githubusercontent.com/96570699/237042234-30e096c9-816c-46b1-828a-d36ee7ad0b88.png)  


### 事件冒泡
![image](https://user-images.githubusercontent.com/96570699/237042827-e60c3bee-0f47-473a-86ac-bd2d645f8ef2.png)  
注意是同名时间，就是点击事件和经过事件不能同时触发。    


### 阻止冒泡和传播
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/52d4df75-dca5-45cc-920f-1ebf368f9ec8)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/7b62288c-48a0-419b-82b4-3c9f667e8e4a)  


### 解绑事件
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/03925c18-c4ab-41f7-ae3b-4a08159998c8)    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9000ccdd-3256-472f-8ea1-5e398076c70e)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/654ec3c1-1c71-4b9b-9c02-181f4f4aa5e4)  






