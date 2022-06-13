# 一.区别
>redis-py提供两个类Redis和StrictRedis用于实现Redis的命令,StrictRedis用于实现大部分官方的命令,并使用官方的语法和命令(比如,SET命令对应与StrictRedis.set方法)。Redis是StrictRedis的子类,用于向后兼容旧版本的redis-py。 简单说,官方推荐使用StrictRedis方法。

>**Pool:连接连接池的区别**  
>Redis的连接池的方法:  
>`pool = redis.ConnectionPool(host=‘localhost’, port=6379, db=0)`  
>`r = redis.Redis(connection_pool=pool)`  
>StrictRedis的连接池的实现方式:  
>`pool = redis.ConnectionPool(host=‘127.0.0.1’, port=6379)`  
>`r = redis.StrictRedis(connection_pool=pool)`





