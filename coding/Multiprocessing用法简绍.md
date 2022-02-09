# 一.multiprocessing常用组件及功能
## 管理进程模块：
Process（用于创建进程模块）  
Pool（用于创建管理进程池）  
Queue（用于进程通信，资源共享）  
Value，Array（用于进程通信，资源共享）  
Pipe（用于管道通信）  
Manager（用于资源共享）  

## 同步子进程模块：
Condition  
Event  
Lock  
RLock  
Semaphore  

# 二.Process模块
**Process语法结构如下：**` Process(group=None, target=None, name=None, args=(), kwargs={}) `  
target：如果传递了函数的引用，这个子进程就执行这里(函数)的代码  
args：给target指定的函数传递的参数，以元组的方式传递  
kwargs：给target指定的函数传递命名参数  ,以字典的方式传递
name：给进程设定一个名字，可以不设定   
group：指定进程组，大多数情况下用不到  

**Process创建的实例对象的常用方法：**  
p.start()：启动子进程实例（创建子进程）  
p.is_alive()：判断子进程p是否仍然运行，返回True 
p.join([timeout])：主线程阻塞,等待子进程p终止后再继续,timeout可选
p.terminate()：强制终止进程p，可能产生僵尸进程和死锁  

**Process创建的实例对象的常用属性：**  
p.daemon：让子进程以守护进程方式运行,必须在p.start()之前设置
p.name：当前进程的别名，默认为Process-N，N为从1开始递增的整数  
p.pid：当前进程的pid（进程号）  
需要注意的是start()，join()，is_alive()， terminate()方法只能由创建进程对象的过程调用 

示例：
```
import multiprocessing

def work1():
    for i in range(10):
    print("work：" , i, multiprocessing.current_process())  #.current_process()为进程名称获取方法

if __name__ == '__main__':
    process_1 = multiprocessing.Process(group=None, target=work1)
    process_1.start()
```  
```
import multiprocessing

def test(a, b, c):
    print(a, b, c)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=test, args=(1,2,3))
    p1.start()
    
    p2 = multiprocessing.Process(target=test, args=(4,), kwargs={'b':5, 'c':6}) #两种给子进程传递参数的方法
    p2.start()
```

**获取进程pid方法：**  
有两种方法可以获取    
1）multiprocessing.current_process().pid  
2）使用import os模块的getpid()  

*注意：进程间不共享全局变量*
```
import multiprocessing

num = 100

def test_1():
    global num
    num += 1
    print('now num: ', num)

def test_2():
    print('now num', num)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=test_1)
    p1.start()
    
    p2 = multiprocessing.Process(target=test_2)
    p2.start()
```
结果为：
> now num:  101  
> now num:  100  
> 由运行结果可以看出，work函数对num1的修改，在work2中并没有获取到，而还是原来的100，所以，进程之间是不能够共享变量的  

**守护主进程**  
python中默认进程是非守护的，此时假如设置了多个进程，主进程非守护，要等待所有子进程运行结束才能退出；  
当设置了守护主进程，如：进程对象p.daemon = True，此时主进程结束子进程就得结束；  
上面提出，子进程没结束主进程就可以强制将其结束，显然在大多数情景不能符合生产需要，我们就可以将子进程设置join()从而实现子进程执行完主进程才能执行，join一旦执行会阻塞主进程，join的子进程以后不影响其他进程的并行运行：join之前的进程都会并行执行，join之后的进程也会在解阻塞后继续并行运行。  
关于守护进程需要强调两点：  
其一：守护进程会在主进程代码执行结束后就终止  
其二：守护进程内无法再开启子进程,否则抛出异常  
> 如果我们有两个任务需要并发执行，那么开一个主进程和一个子进程分别去执行就ok了  
> 如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。主进程代码运行结束，守护进程随即终止。
```
from multiprocessing import Process
import time,random

def task(name):
    print('%s is piaoing' %name)
    time.sleep(random.randrange(1,3))
    print('%s is piao end' %name)

if __name__ == '__main__':
    p=Process(target=task,args=('egon',))
    p.daemon=True #一定要在p.start()前设置
    p.start()
    print('主......') #只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了
#运行结果:子进程还没来得及打印,主进程就结束了,子进程也就结束了
主......
```
# 三.pool进程池模块
**pool语法结构如下：** Pool(processes=None, initializer=None, initargs, maxtasksperchild=None)
processes：使用的工作进程的数量；若processes是None，默认适用os.cpu_count()返回的数量  
initializer：若initializer是None，则每一个工作进程在开始的时候就会调用initializer(*initargs)  
maxtasksperchild：工作进程退出前可以完成的任务数，完成后用一个新的工作进程来替代原进程，让闲置的资源释放，maxtasksperchild默认是None，此意味只要Pool存在工作进程就一直存活  
**pool创建的实例对象的常用方法：**  
p.apply( func=?, args=(), kwds={} ):将 func 函数提交给进程池处理。其中 args 代表传给 func 的位置参数，kwds 代表传给 func 的关键字参数。该方法会被阻塞直到 func 函数执行完成，实际上这也就说所谓的同步执行。（同步执行，按照加入进程池的顺序执行事件，每次执行完一个再执行另一个，无法获取返回值。）   
p.apply_async( func=?, args=(), kwds={}, callback=?, error_callback=？ ):这是 apply() 方法的异步版本，该方法不会被阻塞。其中 callback 指定 func 函数完成后的回调函数，error_callback 指定 func 函数出错后的回调函数。（异步执行，同时启动进程池中多个进程执行事件，可以获取事件返回值）  
p.map(func, iterable[, chunksize=None]):
p.close():关闭进程池。在调用该方法之后，该进程池不能再接收新任务，它会把当前进程池中的所有任务执行完成后再关闭自己   
p.terminate()：立即中止进程池  
p.join():等待所有进程完成  
注意：  
>调用join之前，先调用close或者terminate方法，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束  
>向进程池对象中添加事件，事件排队执行  
>如果主进程退出，则进程池中所有进程都退出  


