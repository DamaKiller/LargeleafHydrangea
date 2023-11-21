# 一.ORM与SQLAlchemy 简介
ORM 全称 Object Relational Mapping, 翻译过来叫对象关系映射。简单的说，ORM 将数据库中的表与面向对象语言中的类建立了一种对应关系。
这样，我们要操作数据库，数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。  


# 二.配置连接
```
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# 数据库配置格式： 'mysql://user:password@localhost:port/dbname'
# postgresqlのDBの設定
DATABASE = 'postgresql://%s:%s@%s:%s/%s' % (
    "imp_ext06",
    "sspiAuth",
    "localhost",
    "5432",
    "str"
)

# 首先需要连接数据库
ENGINE  = create_engine(
    DATABASE,  # 数据库配置  
    client_encoding="utf8",  
    poolclass=NullPool,
    echo=False  
)

```
**常用的create_engine的参数:**   
> echo=False -- 如果为True，引擎将记录所有语句以及 repr() 其参数列表的默认日志处理程序。  
> enable_from_linting -- 默认为True。如果发现给定的SELECT语句与将导致笛卡尔积的元素取得链接，则将发出警告。  
> client_encoding -- 默认为 utf-8。  
> hide_parameters -- 布尔值，当设置为True时，SQL语句参数将不会显示在信息日志中，也不会格式化为 StatementError 对象。  
> max_overflow=10 --  超出 pool_size 后可允许的最大连接数，默认为 10, 这 10 个连接在使用过后，不放在 pool 中，而是被真正关闭的。    
> pool_size=5 -- 连接数大小，默认为 5。  
> pool_timeout=30 -- 获取连接的超时阈值，默认为 30 秒。  
> poolclass=NullPool -- 禁用了SQLAlchemy提供的数据库连接池。SQLAlchemy 就会在执行 session.close() 后立刻断开数据库连接。当然，如果没有被调用 session.close()，则数据库连接不会被断开，直到程序终止。   
> plugins -- 要加载的插件名称的字符串列表。  


# 三.创建会话
通过scoped_session再去创建 Session ，返回的是同一个 Session 。
```
session = scoped_session(
    # ORM执行时的设定。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)
```



# 四.声明映射
在Python中创建的一个类,都对应着数据库中的一张表，类的每个属性，就是这个表的字段名。这种的类对应于数据库中表的类，就称为映射类，
我们要创建一个映射类，是基于基类定义的，每个映射类都要继承这个基类 **declarative_base()**。
```
from sqlalchemy.ext.declarative import declarative_base

# 只要有了这个“基”类，就可以根据它定义任意数量的映射类。
Base = declarative_base()
```









