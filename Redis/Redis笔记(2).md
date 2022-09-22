# 列表
### 简绍
***
单键多值的意思的key为一个，但可以有多个值。即key为name但value为jack，lucy，sam等。    
redis中的列表数据结构其实就是个双向链表，
![image](https://user-images.githubusercontent.com/96570699/190911535-896c97cd-395c-45b4-9e57-0407d5a2d1ea.png)  


### 列表常用命令
#### lpush和rpush，lrange命令
***
![image](https://user-images.githubusercontent.com/96570699/191027519-aaa51e88-25cb-4a02-9df0-80a708eba6b9.png)  
![image](https://user-images.githubusercontent.com/96570699/191027557-c03f1fba-9c5b-4164-a275-fbcbdbf8b246.png)  
![image](https://user-images.githubusercontent.com/96570699/191024620-8645ec1b-caff-4397-9a36-fe5f1c31b9d5.png)  
注意存放方式类似于栈，后进先出。  
![image](https://user-images.githubusercontent.com/96570699/191027178-c851cdb2-9227-4204-b263-4a716c4149be.png)  
rpush跟lpush一样。  
![image](https://user-images.githubusercontent.com/96570699/191027745-44f9cdb8-680e-442a-a029-6ca69105cdd4.png)  
![image](https://user-images.githubusercontent.com/96570699/191028002-ad3fbf75-4b15-428f-aa94-474a297df8f7.png)  


#### lpop和rpop，rpoplpush命令
***
![image](https://user-images.githubusercontent.com/96570699/191028104-73050b97-1470-4c17-99f9-ec3c6f4da861.png)  
值在键在，值光键亡的意思是当值都被取出时该键就不存在了。  
![image](https://user-images.githubusercontent.com/96570699/191028197-14743c12-2798-417a-8185-abfd9a22da93.png)  
![image](https://user-images.githubusercontent.com/96570699/191029307-e6c2dd80-bb9a-471c-a40d-0cb658aa59e1.png)  
![image](https://user-images.githubusercontent.com/96570699/191030007-242cefc4-33cb-4c93-b3a7-db5423f4b104.png)  
![image](https://user-images.githubusercontent.com/96570699/191030178-ad99b84a-6e29-4844-b9cc-3e2c42abb190.png)  


#### index和llen命令
***
![image](https://user-images.githubusercontent.com/96570699/191030416-785d1275-5eca-4dbb-90d8-9269303ebf10.png)  
![image](https://user-images.githubusercontent.com/96570699/191030641-5d93c812-9dc9-4d77-9466-4ffc467f7259.png)  
![image](https://user-images.githubusercontent.com/96570699/191030339-ffa9c71b-6517-4052-b272-888fb71d07a2.png)  
![image](https://user-images.githubusercontent.com/96570699/191030546-4fb1a838-5bd0-4467-b9ca-127a3c042427.png)  
![image](https://user-images.githubusercontent.com/96570699/191030580-d8b90ebd-e8af-440a-afa8-523aa640f54d.png)  


#### linsert..after/before和lrem，lset命令
***
![image](https://user-images.githubusercontent.com/96570699/191030871-f937dfa7-f1a5-4140-8cb1-fe34f8f9b906.png)  
![image](https://user-images.githubusercontent.com/96570699/191031670-6260a247-3c98-41a6-858e-1feceb3383c7.png)  
![image](https://user-images.githubusercontent.com/96570699/191032028-ccb5717b-d841-4bcb-8eee-53ff53e5e579.png)  
![image](https://user-images.githubusercontent.com/96570699/191032251-8b48f0cf-a120-4468-8260-c4b11fe7f6e5.png)  


### 数据结构
***
![image](https://user-images.githubusercontent.com/96570699/191034793-9d3fcc98-39ff-4b7b-9d07-ab1f812d9a50.png)  
![image](https://user-images.githubusercontent.com/96570699/191034586-c8827215-2f66-4a2c-ad0c-ac00c3e8a79e.png)  




# 集合
### 简绍
***
![image](https://user-images.githubusercontent.com/96570699/191059411-84ab24e1-33e3-44da-8ea9-e7dbb317e147.png)  
![image](https://user-images.githubusercontent.com/96570699/191059517-06d157e1-a573-423c-983a-16987d5c49fc.png)  


### 集合常用命令
#### sadd和smembers命令
***
![image](https://user-images.githubusercontent.com/96570699/191060533-cc644138-557c-4288-af11-7ef137212847.png)  
![image](https://user-images.githubusercontent.com/96570699/191060406-b6f63374-8dd7-4fe4-9a9c-fb96300f757b.png)  


#### sismember命令
***
![image](https://user-images.githubusercontent.com/96570699/191060969-e9f15ec5-7033-44c7-b003-91e0bfe9a8d0.png)  
![image](https://user-images.githubusercontent.com/96570699/191060827-f602fca9-13a2-4acb-8ea9-21b44865bcb1.png)  


#### scard命令
***
![image](https://user-images.githubusercontent.com/96570699/191061153-d1ad6e3c-08fc-4b22-9a69-8a0e6ec4d24b.png)  
![image](https://user-images.githubusercontent.com/96570699/191061099-fa87b4fd-3704-4eec-a3db-de8d236c1c99.png)  


#### srem和spop命令
***
![image](https://user-images.githubusercontent.com/96570699/191061522-09cf616c-d3ab-40d3-8a82-92e64e49af9e.png)  
![image](https://user-images.githubusercontent.com/96570699/191061289-981640fa-4855-44dd-8f45-4a6d29dcba52.png)  
![image](https://user-images.githubusercontent.com/96570699/191061474-915d4bd0-b953-45b5-ba7d-720104a0db54.png)  


#### srandmember和smove命令
***
![image](https://user-images.githubusercontent.com/96570699/191063888-abbc10a1-aabd-4e87-ac01-bcf5acb5f55a.png)  
![image](https://user-images.githubusercontent.com/96570699/191061818-8a84b483-d86b-48f2-ac5a-5273f646d776.png)  
![image](https://user-images.githubusercontent.com/96570699/191061728-613d26f9-6513-4a6b-8358-5f009025da2f.png)  
![image](https://user-images.githubusercontent.com/96570699/191063822-73bad633-76b0-4078-8a66-0ee9b572179c.png)  


#### sinter，sunion，sdiff命令
***
![image](https://user-images.githubusercontent.com/96570699/191064232-b348e398-776f-4389-a672-77a78a646ce4.png)  
![image](https://user-images.githubusercontent.com/96570699/191064282-ea12e0f4-6901-41c9-93ae-bac032d0c8c8.png)  
![image](https://user-images.githubusercontent.com/96570699/191064344-fdeb3f4c-6701-409d-8445-ca8faf1e19a0.png)  


### 数据结构
***
![image](https://user-images.githubusercontent.com/96570699/191064446-ffd9765a-199a-44a3-a280-19a6a4004e76.png)  


# 哈希
***
![image](https://user-images.githubusercontent.com/96570699/191544602-454e289e-c1bf-42b5-a855-5d418558ec4d.png)  
![image](https://user-images.githubusercontent.com/96570699/191544279-7b02defd-e0da-4ac3-9d67-aa872efee630.png)  
![image](https://user-images.githubusercontent.com/96570699/191544745-a5536c84-454a-4990-b693-e36fd3d2744c.png)  
![image](https://user-images.githubusercontent.com/96570699/191545086-e16f9c4d-32be-49a9-a2ce-c4088d106318.png)  
![image](https://user-images.githubusercontent.com/96570699/191546438-b40f1141-e56a-4a49-9301-0d30c62bc247.png)  
只不过value是一段映射关系。  




### 常用命令
*** 
#### hset和hget命令
![image](https://user-images.githubusercontent.com/96570699/191548312-e63f905d-91ca-4fe5-8d6d-8de31d100530.png)  
![image](https://user-images.githubusercontent.com/96570699/191548273-48ed9200-966b-4b7a-b1bc-dbace531f0ae.png)  


#### hmset命令
*** 
![image](https://user-images.githubusercontent.com/96570699/191548977-5d16e5cc-1213-439d-a297-7b90ee608b57.png)  
![image](https://user-images.githubusercontent.com/96570699/191549088-b1d2cde2-bc18-4f10-976c-4dd940622d85.png)  


#### hexists命令
*** 
![image](https://user-images.githubusercontent.com/96570699/191549561-b9b4285f-1730-4bae-84f0-aba668f2b76b.png)  
![image](https://user-images.githubusercontent.com/96570699/191549242-7240a890-0325-4218-a784-2a21090ebb33.png)   
0表示不存在，1表示存在。   


#### hkeys和hvals命令
*** 
![image](https://user-images.githubusercontent.com/96570699/191550291-d363988a-d3c0-40fc-b399-6804d3bdc2b2.png)  
![image](https://user-images.githubusercontent.com/96570699/191550225-5ff72292-57ee-461d-9003-d32932b6d335.png)  


#### hsetnx命令
*** 
![image](https://user-images.githubusercontent.com/96570699/191551781-a6343504-1a9e-42f9-9c43-9cb8014da94e.png)  
![image](https://user-images.githubusercontent.com/96570699/191552295-052fd20d-483a-4002-8c3b-abf28b178750.png)  


### 数据结构
***
![image](https://user-images.githubusercontent.com/96570699/191552573-6920d38f-3cbf-4442-8631-02eae185c5ae.png)

