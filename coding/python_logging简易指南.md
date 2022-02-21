# logging模块的使用方式介绍
loggging模块提供了两种使用logging模块的方式
- 第一种方式是使用logging提供的模块级别的函数  
- 第二种方式是使用Logging日志系统的四大组件  
注：其实，logging所提供的模块级别的日志记录函数也是对logging日志系统相关类的封装而已。 

## 第一种方法
**logging模块定义的模块级别的常用函数：**
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

该函数可接收的关键字参数如下：
|参数名称|描述|
|:---:|:---:|
|filename|指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了|
|filemode|如果指定 filename，则以此模式打开文件(‘r’、‘w’、‘a’)。默认为“a”|
|format|为处理程序使用指定的格式字符串|
|datefmt|使用 time.strftime() 所接受的指定日期/时间格式|
|style|如果指定了格式，则对格式字符串使用此样式。’%’ 用于 printf 样式、’{’ 用于 str.format()、’$’ 用于 string。默认为“%”|
|level|将根记录器级别设置为指定的级别。默认生成的 root logger 的 level 是 logging.WARNING，低于该级别的就不输出了。级别排序：CRITICAL > ERROR > WARNING > INFO > DEBUG。（如果需要显示所有级别的内容，可将 level=logging.NOTSET）|
|stream|使用指定的流初始化 StreamHandler。注意，此参数与 filename 不兼容——如果两者都存在，则会抛出 ValueError|
|handlers|如果指定，这应该是已经创建的处理程序的迭代，以便添加到根日志程序中。任何没有格式化程序集的处理程序都将被分配给在此函数中创建的默认格式化程序。注意，此参数与 filename 或 stream 不兼容——如果两者都存在，则会抛出 ValueError|

例子：
```
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```
结果：  
```
#此时会在my.log日志文件中看到如下输出内容：
05/08/2017 14:29:04 PM - DEBUG - This is a debug log.
05/08/2017 14:29:04 PM - INFO - This is a info log.
05/08/2017 14:29:04 PM - WARNING - This is a warning log.
05/08/2017 14:29:04 PM - ERROR - This is a error log.
05/08/2017 14:29:04 PM - CRITICAL - This is a critical log.
```
- logging.basicConfig()函数是一个一次性的简单配置工具，也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
- 日志器（Logger）是有层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，其名称为'root'，它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的。
- logging.debug(), logging.info()等方法的定义中，除了msg和args参数外，还有一个**kwargs参数。它们支持3个关键字参数: exc_info, stack_info, extra，下面对这几个关键字参数作个说明。
  > exc_info： 其值为布尔值，如果该参数的值设置为True，则会将异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。  
  > stack_info： 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。  
  > extra： 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。  
  ```
  LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
  DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

  logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
  logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
  
  #结果
  
  02/21/2022 10:02:53 AM - WARNING - Tom[47.98.53.222] - Some one delete the log file.
  NoneType: None
  Stack (most recent call last):
  File "c:/Users/ZZ0C2R672/Desktop/project/test_logging.py", line 7, in <module> 
    logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
  ```


## 第二种方式
**logging模块的四大组件：**
|组件名称|对应类名|功能描述|
|:---:|:---:|:---:|
|日志器|loggers|提供应用程序代码直接使用的接口|
|处理器|handlers|用于将日志记录发送到指定的目的位置|
|过滤器|filters|提供更精细的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）|  
|格式器|formatters|用于控制日志信息的最终输出格式|   
它们之间的关系：
> 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；  
> 不同的处理器（handler）可以将日志输出到不同的位置,日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；  
> 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志,每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。  
> 总结：即通过logger这个接口，通过为handler设置filter和formatter来让它工作，输出满足需求的日志。

注：logging模块提供的模块级别的那些函数实际上也是通过这几个组件的相关实现类来记录日志的，只是在创建这些类的实例时设置了一些默认值。  
**Logger类**  
logger对象主要做三个工作：  
> 向应用程序代码提供接口，使应用程序可以在运行时记录日志消息；    
>>`logger = logging.getLogger('name')` name为可选参数，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。  
  
> 基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；  
>> `logger.setLevel(level=logging.INFO)` 此时函数参数为INFO，那么该logger将只会处理INFO、WARNING、ERROR和CRITICAL级别的日志，而DEBUG级别的消息将会被忽略/丢弃。
    
> 将日志消息传送给所有感兴趣的日志handlers或配置filter。       
>> `logger.addHandler(log_handler)`或`Logger.removeHandler()` 为该logger对象添加和移除一个handler对象。 `Logger.addFilter() `或`Logger.removeFilter()` 为该logger对象添加和移除一个filter对象    

# 简单配置使用
**第一种方法例子：** 
```
import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
#也可以这样写
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
```
结果：  
```
WARNING:root:This is a warning log.
ERROR:root:This is a error log.      
CRITICAL:root:This is a critical log.
```
默认情况下，logging模块将日志打印到屏幕上(stdout)，日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)，日志格式如下所示：  
![image](https://user-images.githubusercontent.com/96570699/154871882-8e771e7c-8573-40ae-88e3-f612ef49e70e.png)
日志级别：  
![image](https://user-images.githubusercontent.com/96570699/154847064-9cdef204-01c0-4a5a-b850-9848df06a1ae.png)
