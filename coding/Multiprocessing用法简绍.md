# multiprocessing常用组件及功能
## 1.1、管理进程模块：
Process（用于创建进程模块）  
Pool（用于创建管理进程池）  
Queue（用于进程通信，资源共享）  
Value，Array（用于进程通信，资源共享）  
Pipe（用于管道通信）  
Manager（用于资源共享）  

## 1.2、同步子进程模块：
Condition  
Event  
Lock  
RLock  
Semaphore  

# Process 类
Process语法结构如下：` Process(group=None, target=None, name=None, args=(), kwargs={}) `
target：如果传递了函数的引用，这个子进程就执行这里(函数)的代码  
args：给target指定的函数传递的参数，以元组的方式传递  
kwargs：给target指定的函数传递命名参数  
name：给进程设定一个名字，可以不设定   
group：指定进程组，大多数情况下用不到  

Process创建的实例对象的常用方法：  
start()：启动子进程实例（创建子进程）  
is_alive()：判断进程子进程是否还在活着  
join([timeout])：是否等待子进程执行结束，或等待多少秒  
terminate()：不管任务是否完成，立即终止子进程  

Process创建的实例对象的常用属性：  
name：当前进程的别名，默认为Process-N，N为从1开始递增的整数  
pid：当前进程的pid（进程号）  
需要注意的是start()，join()，is_alive()， terminate()方法只能由创建进程对象的过程调用  

获取进程pid方法：
有两种方法可以获取
1）multiprocessing.current_process().pid
2）使用import os模块的getpid()

示例：
````
import multiprocessing

def work1():
    for i in range(10):
    print("work：" , i, multiprocessing.current_process())  #.current_process()为进程名称获取方法

if __name__ == '__main__':
    process_1 = multiprocessing.Process(group=None, target=work1)
    process_1.start()
```