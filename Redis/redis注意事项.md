**1.redis 取出的结果默认是字节，我们可以设定 decode_responses=True 改成字符串。
下图结果中的b，就是提示结果为字节类型。 redis 各个数据库中可以有相同的key，它们各自独立。**
![image](https://user-images.githubusercontent.com/96570699/177068358-1c56b3ec-d8ae-4bd5-8fdc-976b66fa7326.png)  
**2.redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，在每次使用redis都进行连接的话会拉低redis的效率，
都知道redis是基于内存的数据库，效率贼高，所以每次进行连接比真正使用消耗的资源和时间还多。
所以为了节省资源，减少多次连接损耗， 连接池的作用相当于缓存了多个客户端与redis服务端的连接，
当有新的客户端来进行连接时，此时，只需要去连接池获取一个连接即可， 实际上连接池就是把一个连接共享给多个客户端，可以说是广播，要用的话就去接收。**
```
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r_1 = redis.StrictRedis(connection_pool=pool)
r_2 = redis.StrictRedis(connection_pool=pool)
print(r_1.get('my_age'))
print(r_2.get('my_name'))
print(r_1.client_list())
print(r_2.client_list())
```
![image](https://user-images.githubusercontent.com/96570699/177069485-17e3dab2-5cf1-46cb-ad3a-a0544489ecfb.png)  

