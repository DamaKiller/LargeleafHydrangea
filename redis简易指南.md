# 一.操作前准备
首先，操作前需在本机安装好redis和python redis包。
redis安装地址：https://github.com/tporadowski/redis/releases
pip安装命令:pip install redis
其次，将下载好的redis压缩文件解压，运行当中的redis-server.exe文件，启动redis服务，并且该cmd窗口在操作期间不能关闭。

# 二.操作
### 1.简单运行
```
import redis

r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0)    #host也可以写成`host='localhost'`，port为本机的端口号，
                                                                  #db为选中的第几个数据库，默认创建16个数据库，编号为0~15
r.set('my_age', '24')
print(r.get('my_age'))
```
![image](https://user-images.githubusercontent.com/96570699/173307976-92db3ea2-ede6-460b-a353-59b0140cb9db.png)  
**注：**  
**redis 取出的结果默认是字节，我们可以设定 `decode_responses=True` 改成字符串。上图结果中的b，就是提示结果为字节类型。** 
**redis 各个数据库中可以有相同的key，它们各自独立。**
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.get('my_age'))
```
![image](https://user-images.githubusercontent.com/96570699/173308339-38940cda-3929-4f58-972f-0c9669426f17.png)  

### 2.redis连接池
redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，在每次使用redis都进行连接的话会拉低redis的效率，
都知道redis是基于内存的数据库，效率贼高，所以每次进行连接比真正使用消耗的资源和时间还多。所以为了节省资源，减少多次连接损耗，
连接池的作用相当于缓存了多个客户端与redis服务端的连接，当有新的客户端来进行连接时，此时，只需要去连接池获取一个连接即可，
实际上连接池就是把一个连接共享给多个客户端，可以说是广播，要用的话就去接收。  
```
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r_1 = redis.StrictRedis(connection_pool=pool)
r_2 = redis.StrictRedis(connection_pool=pool)
print(r_1.get('my_age'))
print(r_2.get('my_name'))
print(r_1.client_list())
print(r_2.client_list())
```
![image](https://user-images.githubusercontent.com/96570699/173310824-70ee6e2d-84b0-4e5e-81cc-8abad49bfa74.png)  

### 3.redis的常用基本命令-String
#### 1.set命令
在 Redis 中设置值，默认不存在则创建，存在则修改。  
**`set(name, value, ex=None, px=None, nx=False, xx=False)`**  
- ex - 过期时间（秒）,这里若设定过期时间是3秒，3秒后键的值就变成None。
- px - 过期时间（毫秒），这里若设定过期时间是3豪秒，3毫秒后，键的值就变成None。
- nx - 如果设置为True，则只有key不存在时，当前set操作才执行。如果键不存在，那么输出是True；如果键已经存在，输出是None
- xx - 如果设置为True，则只有key存在时，当前set操作才执行。
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.set('my_name', 'weiyi', nx = True))     #该键不存在
```
![image](https://user-images.githubusercontent.com/96570699/173321096-3da16791-195a-4714-9857-dbdaf11e241d.png)  
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.set('my_name', 'weiyi', xx=True))     #该键已存在
```
![image](https://user-images.githubusercontent.com/96570699/173321694-7395f783-d11e-4f0a-b2aa-e111e0337cae.png)

#### 2.setnx命令
设置值，只有name不存在时，执行设置操作（添加）  
**setnx(name, value)**
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.setnx('fruit', 'apple'))    #该键不存在
```
![image](https://user-images.githubusercontent.com/96570699/173323644-dc68528f-849e-4913-a943-f041783c2ae3.png)    
#### 3.setex命令
设置值,time为过期时间。（数字秒 或 timedelta对象）  
**`setex(name, time, value)`**
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.setex('fruit_other', 2, 'orange')) 
time.sleep(3)
print(r.get('fruit_other'))
```
![image](https://user-images.githubusercontent.com/96570699/173324597-1063f6d9-0f29-4084-8053-ef70f0a656cc.png)  
#### 4.mset命令
批量设置值，传入的参数必须是一个字典。  
**`mset(dict)`**
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
dict = {"a" : "v1", "b" : "v2"}
r.mset(dict)
```
#### 5.mget命令
批量获取值,传入的参数必须是一个列表。  
**`mget(list)`**
```
r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0, decode_responses=True)
print(r.mget(['a', 'b']))
```
![image](https://user-images.githubusercontent.com/96570699/173478522-c44af60f-606c-47a7-9125-161ab3c935c4.png)
