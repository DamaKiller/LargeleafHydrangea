# 一.Redis简绍
![image](https://user-images.githubusercontent.com/96570699/190893779-148e61ed-0620-4f1f-b558-f4869210da98.png)  
ACID为事务的四个特性。


### 适用场景 
***
![image](https://user-images.githubusercontent.com/96570699/190893815-f881e27e-324d-47fd-9663-81ac1812c014.png)  


### 不适用场景   
***
![image](https://user-images.githubusercontent.com/96570699/190893842-ad732a0e-a74f-4cfc-a917-e7defa6f44f4.png)  


### 文件功能
***
![image](https://user-images.githubusercontent.com/96570699/190893513-9c935789-467c-454d-8032-c49a5c293279.png)  

 
### 简绍
***
![image](https://user-images.githubusercontent.com/96570699/190893987-ad8e8341-a52e-4c71-af94-af7bd4d18da9.png)  
**单线程+多路IO复用**  
![image](https://user-images.githubusercontent.com/96570699/190894436-8229209e-ec63-423c-a903-a8138ea6927d.png)  
乘客委托黄牛去火车站买票，每个人买的票都是不一样的，黄牛去买票这一操作是单线程的，其他买票的乘客在这期间就去干别的事，不会造成资源的浪费。  




# 二.Redis常用命令
***
![image](https://user-images.githubusercontent.com/96570699/190895249-bedc865e-5d0a-4acb-9066-6fd074a10a54.png)  
unlink并不是立刻删掉，而是会在后续慢慢删掉（异步操作）  
![image](https://user-images.githubusercontent.com/96570699/190895427-dec1bef0-d91c-4ede-966b-194d08727c56.png)  
![image](https://user-images.githubusercontent.com/96570699/190895560-4fb8945f-757c-48eb-8cca-9557646d8fa0.png)  



### keys *
***
![image](https://user-images.githubusercontent.com/96570699/190895023-cf096d6d-4e40-4736-acc3-319cdb8afb3e.png)  


### exists key（key为想查找的key的名字）
***
![image](https://user-images.githubusercontent.com/96570699/190895084-4a1fd459-1587-416e-89a4-90f4952821e0.png)  


### type key（key为想查找的key的名字）
***
![image](https://user-images.githubusercontent.com/96570699/190895175-788ced61-48b1-4c8f-9bf6-8289f988535c.png)  


### del key（key为想删除的key的名字）
***
![image](https://user-images.githubusercontent.com/96570699/190895207-fd4477f3-4c85-4974-ae98-187fb1a0b585.png)


### expire（key 时间）和 ttl key（key为想查找的key的名字）
***
![image](https://user-images.githubusercontent.com/96570699/190895307-5472a803-ac15-4e73-a319-1a4dfb8f630a.png)  
没有设置过期时间就是永不过期。  


### select num（num为像切换的数据库）
***
![image](https://user-images.githubusercontent.com/96570699/190895643-40175f43-47bd-4299-a318-41a0bc150194.png)  


### dbsize
***
![image](https://user-images.githubusercontent.com/96570699/190895655-8a5b0b11-d458-477c-bef3-a818abddfbd9.png)  






# 三.Redis数据类型
## string
### String简绍
***
![image](https://user-images.githubusercontent.com/96570699/190895802-1874e334-c856-4b34-a088-800ea93a0b78.png)  


### String常用命令
#### set和get命令
***
![image](https://user-images.githubusercontent.com/96570699/190897482-b12c500c-0567-44f5-9438-abcdf848ee91.png)  
![image](https://user-images.githubusercontent.com/96570699/190897943-16a4fe31-6b1b-4bc9-a5d0-283dcb993d36.png)  
![image](https://user-images.githubusercontent.com/96570699/190897449-8452e83d-7586-49bb-a26d-b3ffe559975d.png)  
![image](https://user-images.githubusercontent.com/96570699/190897509-40f0eb82-321d-4865-9d72-391e8289004e.png)  
![image](https://user-images.githubusercontent.com/96570699/190897546-d1fd2104-d912-4a52-be2c-c2e0975feb18.png)  
`set k1 v1 EX 60 NX`想要变更参数时这么写。  
重复设置值，会将原有的key-value更新。  
![image](https://user-images.githubusercontent.com/96570699/190898039-5255deca-1424-43ba-8996-9b2f43ae9ad5.png)  
![image](https://user-images.githubusercontent.com/96570699/190898024-23777100-8a5b-4c22-ba26-d9e757888853.png)    


#### append命令
***
![image](https://user-images.githubusercontent.com/96570699/190897931-be1f4807-86a2-4e12-bfea-9f0e99e002c8.png)  
![image](https://user-images.githubusercontent.com/96570699/190897885-4e3e92b7-6c6b-4c17-a6f6-08130a5f86f3.png)  


#### strlen命令
***
![image](https://user-images.githubusercontent.com/96570699/190897982-951b3278-35a9-49da-aed9-e42eb7a92563.png)  
![image](https://user-images.githubusercontent.com/96570699/190897955-26b42240-a76d-4185-8450-04084c3559e2.png)  


#### incr和decr命令
***
![image](https://user-images.githubusercontent.com/96570699/190898180-d434508b-1365-4e8a-8555-84bbae86136d.png)  
![image](https://user-images.githubusercontent.com/96570699/190898867-706f1573-91be-46fb-b5a8-d97f8df7aef0.png)  
![image](https://user-images.githubusercontent.com/96570699/190898232-cbbc0369-fc5e-4957-bce5-cfbf92ba10a2.png)  
![image](https://user-images.githubusercontent.com/96570699/190898168-8e8f7fcb-2044-451b-b12b-49d4c1b31732.png)  
![image](https://user-images.githubusercontent.com/96570699/190898198-549ca340-e41d-492e-b265-33dbee120e60.png)  
![image](https://user-images.githubusercontent.com/96570699/190898808-4c8a0e0a-5318-43fa-a2a4-f87a9a7a7de7.png)  
**特性**  
![image](https://user-images.githubusercontent.com/96570699/190901142-512e3f30-f9a4-4f15-a98a-a364e46131bf.png)  
就是在一个操作中对其加一，另一个操作中对其减一，他们之间不会互相影响。不会因为另外一个操作导致另外一个操作的值被更改。  


#### mset和mget命令
***
![image](https://user-images.githubusercontent.com/96570699/190910528-b7cec5ca-edb3-47d3-9887-30beffe4f9c8.png)  
![image](https://user-images.githubusercontent.com/96570699/190907128-0bb75e79-6cd5-4067-bfc3-8f42050c3c00.png)  


#### msetnx命令
***
![image](https://user-images.githubusercontent.com/96570699/190910567-e586f2d5-2970-4513-b203-513f2eab65c8.png)  
![image](https://user-images.githubusercontent.com/96570699/190910138-ab5b206b-00f0-4596-8b68-fa355a062d48.png)  
这条命令只要有一个存在就不会执行。只有全部存在才会执行。    
![image](https://user-images.githubusercontent.com/96570699/190910512-11fa6c48-9186-4e56-83c9-dc6c74e81345.png)  


#### getrange和setrange命令
***
![image](https://user-images.githubusercontent.com/96570699/190910787-367ca706-1dbf-491d-b6ab-6100cb4bfcd0.png)  
![image](https://user-images.githubusercontent.com/96570699/190910666-49458047-d94e-4891-9552-5ede75a9bf35.png)  
![image](https://user-images.githubusercontent.com/96570699/190910757-94185a52-1931-49bd-a1da-7c460f6c1de8.png)  

  
#### setex和getset命令
***
![image](https://user-images.githubusercontent.com/96570699/190910969-01a86349-9623-47d6-b858-20cf150b8905.png)  
![image](https://user-images.githubusercontent.com/96570699/190910844-afee912f-0051-4ada-824d-ad4213becb6a.png)  
![image](https://user-images.githubusercontent.com/96570699/190910935-df62dbf5-44a8-4b06-a20a-4414be88f1a0.png)  


### string数据结构
***
string的数据结构是简单的动态字符串，它采用预分配的冗余空间的方式来减少内存的频繁分配。  
![image](https://user-images.githubusercontent.com/96570699/190911072-b425aaea-d11b-44d9-b77f-9108eb07a21f.png)  

