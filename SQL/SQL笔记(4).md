# MYSQL逻辑架构
![image](https://user-images.githubusercontent.com/96570699/197377295-be85ff0f-3bb4-48c3-9690-1c452e7e17ed.png)  
![image](https://user-images.githubusercontent.com/96570699/197377383-6fa26f89-092c-4438-b40c-d394df0a41df.png)  


# 存储引擎
![image](https://user-images.githubusercontent.com/96570699/197377473-4ab307e7-9a29-441a-bb2d-ac166562bb0d.png)  
![image](https://user-images.githubusercontent.com/96570699/197377607-1c543972-f30f-48c9-8c52-95cbe7422e2b.png)  


# SQL性能下降的原因
![image](https://user-images.githubusercontent.com/96570699/197378650-02b10a78-7b9b-4a5e-8a7f-fb25780ba638.png)  

 
# 执行顺序
![image](https://user-images.githubusercontent.com/96570699/197378817-12eb5733-8912-4900-924e-8b663c2bfe0e.png)  


# join查询关系
![image](https://user-images.githubusercontent.com/96570699/197379087-063fe437-7f31-4d23-9010-91ef04133349.png)  
SQL不支持full语法了，可以使用union合并结果来实现同样的效果。  


# 索引
![image](https://user-images.githubusercontent.com/96570699/197380140-efaa7c6f-79ff-4c1a-8e62-c0ee39e2204a.png)  
![image](https://user-images.githubusercontent.com/96570699/197380545-be6d7744-b3b8-4927-beab-7d98885183e0.png)  
![image](https://user-images.githubusercontent.com/96570699/197397300-3ffae3f1-da1f-4567-825e-767a3ae26d98.png)  
![image](https://user-images.githubusercontent.com/96570699/197397767-525adecd-2ba1-493e-8296-f140dbea030c.png)  


### 优势与劣势
![image](https://user-images.githubusercontent.com/96570699/197398330-9c190c4e-b66d-4792-8c2b-0cc92d92fbb9.png)  
![image](https://user-images.githubusercontent.com/96570699/197398655-e9952222-ee7a-4767-90a8-83e3669c380b.png)  


### 索引类型
![image](https://user-images.githubusercontent.com/96570699/197399014-d6fe695e-ec68-40ad-8f2a-34ef3eb75582.png)  
![image](https://user-images.githubusercontent.com/96570699/197399167-3b362a28-e348-4753-84df-001991216720.png)  
![image](https://user-images.githubusercontent.com/96570699/197399192-9698ac89-0ee2-453a-969d-142b34db4461.png)   


### 底层结构
![image](https://user-images.githubusercontent.com/96570699/197399537-5496c972-b643-44e3-84d7-00e1bf217754.png)  
![image](https://user-images.githubusercontent.com/96570699/197399613-2023f811-0900-4005-847f-3c2915b95e6b.png)  
![image](https://user-images.githubusercontent.com/96570699/197399700-81e2b3b8-fa79-40a7-a09b-411ad377b7b6.png)  
![image](https://user-images.githubusercontent.com/96570699/197399767-d030d7de-9ee5-4058-8f2a-414b95f937d9.png)  


### 应用场景
![image](https://user-images.githubusercontent.com/96570699/197399867-0606944c-e66a-4987-b292-edb419e2ab9f.png)  
**注**  
order by字段最好跟select字段的顺序一样，这样可以提高效率。  
![image](https://user-images.githubusercontent.com/96570699/197400728-13354bad-03c2-4bcf-b5f0-4239ab0f0ee0.png)   
![image](https://user-images.githubusercontent.com/96570699/197400928-811024c0-d657-42a4-9997-5ac81817867e.png)   




