# 简单上手实用
例子： 
```
import logging

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
```
结果：  
```
WARNING:root:warn message
ERROR:root:error message
CRITICAL:root:critical message
```
默认情况下，logging模块将日志打印到屏幕上(stdout)，日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)，日志格式如下所示：  
![image](https://user-images.githubusercontent.com/96570699/154846843-498c2f39-5ab6-459f-aaa7-0775b7eb77e7.png)
日志级别：  
![image](https://user-images.githubusercontent.com/96570699/154847064-9cdef204-01c0-4a5a-b850-9848df06a1ae.png)

# 简单配置使用
loggging模块提供了两种使用logging模块的方式
- 第一种方式是使用logging提供的模块级别的函数  
- 第二种方式是使用Logging日志系统的四大组件  
注：其实，logging所提供的模块级别的日志记录函数也是对logging日志系统相关类的封装而已。 

**第一种方法**  
logging模块定义的模块级别的常用函数：
```
logging.debug(msg, *args, **kwargs)    #创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)    #创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)    #创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)    #创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)    #创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)    #创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)    #对root logger进行一次性配置
```
注：其中`logging.basicConfig(**kwargs)`函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息，其他几个都是用于记录各个级别日志的函数。

**第二种方式**
logging模块的四大组件：  
> loggers    提供应用程序代码直接使用的接口  
> handlers    用于将日志记录发送到指定的目的位置  
> filters    提供更精细的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）  
> formatters    用于控制日志信息的最终输出格式  
注：logging模块提供的模块级别的那些函数实际上也是通过这几个组件的相关实现类来记录日志的，只是在创建这些类的实例时设置了一些默认值。  
