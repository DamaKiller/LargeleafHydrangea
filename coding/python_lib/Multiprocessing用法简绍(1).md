# python全局解释器锁(GIL)
    全局解释器锁
它是在实现Python解析器（CPython）时所引入的一个概念。GIL只在CPython中才有,在其他的python解释器中是没有的，例如：PyPy， Jython等。   
    Python设计之初，为了数据安全。某个线程想要执行，必须先拿到GIL，我们可以把GIL看作是“通行证”，并且在一个Python进程中，
GIL只有一个。拿不到通行证的线程，就不允许进入CPU执行。由于GIL锁存在，Python里一个进程永远只能同时执行一个线程(拿到GIL的线程才能执行)，
这就是为什么在多核CPU上，Python 的多线程效率并不高的根本原因。如果想要充分地使用多核CPU的资源，大部分情况需要使用多进程。    
    
    

# 一.multiprocessing常用组件及功能
## 管理进程模块：
Process（用于创建进程模块）  
Pool（用于创建管理进程池）  
Queue（用于进程通信，资源共享）  
Value，Array（用于进程通信，资源共享）  
Pipe（用于管道通信）  
Manager（用于资源共享）  

## 同步子进程模块：
Condition（条件变量）
Event（事件）
Lock（互斥锁）
RLock（可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞)
Semaphore（信号量）

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
结果：
```
work： 0 <Process name='Process-1' parent=19704 started>
work： 1 <Process name='Process-1' parent=19704 started>
work： 2 <Process name='Process-1' parent=19704 started>
work： 3 <Process name='Process-1' parent=19704 started>
work： 4 <Process name='Process-1' parent=19704 started>
work： 5 <Process name='Process-1' parent=19704 started>
work： 6 <Process name='Process-1' parent=19704 started>
work： 7 <Process name='Process-1' parent=19704 started>
work： 8 <Process name='Process-1' parent=19704 started>
work： 9 <Process name='Process-1' parent=19704 started>
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
结果：
```
4 5 6
1 2 3
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
```
结果：
```
主......
```
# 三.pool进程池模块  
**pool语法结构如下：**   
Pool(processes=None, initializer=None, initargs, maxtasksperchild=None, context)    
processes：使用的工作进程的数量；若processes是None，默认适用os.cpu_count()返回的数量  
initializer：如果 initializer 不为 None，则每个工作进程将会在启动时调用 initializer(*initargs))  
maxtasksperchild：工作进程退出前可以完成的任务数，完成后用一个新的工作进程来替代原进程，让闲置的资源释放，maxtasksperchild默认是None，此意味只要Pool存在工作进程就一直存活  
context:可被用于指定启动的工作进程的上下文。通常一个进程池是使用函数 multiprocessing.Pool() 或者一个上下文对象的 Pool() 方法创建的。在这两种情况下， context 都是适当设置的  
**pool创建的实例对象的常用方法：**  
p.apply( func=?, args=(), kwds={} ):将 func 函数提交给进程池处理。其中 args 代表传给 func 的位置参数，kwds 代表传给 func 的关键字参数。该方法会被阻塞直到 func 函数执行完成，实际上这也就说所谓的同步执行。（同步执行，按照加入进程池的顺序执行事件，每次执行完一个再执行另一个，无法获取返回值。）   
p.apply_async( func=?, args=(), kwds={}, callback=?, error_callback=？ ):这是 apply() 方法的异步版本，该方法不会被阻塞。其中 callback 指定 func 函数完成后的回调函数，error_callback 指定 func 函数出错后的回调函数。（异步执行，同时启动进程池中多个进程执行事件，可以获取事件返回值）  
map(function=？, iterable=？, …):function传的是一个函数名，可以是python内置的，也可以是自定义的。 iterable传的是一个可以迭代的对象，例如列表，元组，字符串这样的，map函数返回结果是一个列表。这个函数的意思就是将function应用于iterable的每一个元素，结果以列表的形式返回。注意到没有，iterable后面还有省略号，意思就是可以传很 多个iterable，如果有额外的iterable参数，并行的从这些参数中取元素，并调用function。其中iterable参数个数可以和其他的iterable参数个数不一致,多进程中的map函数类似于 Python 的 map() 全局函数，只不过此处使用新进程对 iterable 的每一个元素执行 func 函数  
map_async( func=？, iterable=？, …, callback=?, error_callback=? )：这是 map() 方法的异步版本，该方法不会被阻塞。其中 callback 指定 func 函数完成后的回调函数，error_callback 指定 func 函数出错后的回调函数    
p.close():关闭进程池。在调用该方法之后，该进程池不能再接收新任务，它会把当前进程池中的所有任务执行完成后再关闭自己   
p.terminate()：立即中止进程池  
p.join():等待所有进程完成  
注意：  
>调用join之前，先调用close或者terminate方法，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束  
>向进程池对象中添加事件，事件排队执行  
>如果主进程退出，则进程池中所有进程都退出 

示例： 
```
import multiprocessing as mp

def test():
    pass

p = mp.Pool(processes = 5) # 创建5条进程

for i in range(10):
    p.apply_async(test) # 向进程池添加任务

p.close() # 关闭进程池，不再接受请求
p.join() # 等待所有的子进程结束
```
> 进程池Pool被创建出来后， p.apply_async(test) 语句不停地循环执行，相当于向进程池中提交了10个请求，它们会被放到一个队列中  
> p = mp.Pool(5) 执行完毕后创建了5条进程，但尚未给它们分配各自的任务；也就意味着，无论有多少任务，实际的进程数只有5条，每次最多5条进程并行  
> 当Pool中有进程任务执行完毕后，这条进程资源会被释放，Pool会按先进先出的原则取出一个新的请求给空闲的进程继续执行  
> 当Pool所有的进程任务完成后，会产生5个僵尸进程，如果主进程/主线程不结束，系统不会自动回收资源，需要调用join函数负责回收  
> 在创建Pool进程池时，若不指定进程的最大数量，默认创建的进程数为系统的内核数量
> 如果采用p.apply(test)阻塞方式添加任务，其每次只能向进程池中添加一条任务，然后for循环会被阻塞等待，直到添加的任务被执行完毕，进程池中的5个进程交替执行新来的任务，此时相当于单进程  

**apply方式添加任务**
```
import  multiprocessing as mp
import os
from time import sleep

def worker(msg):
    print(os.getpid())
    sleep(2)
    print(msg)
    return msg

# 创建进程池对象
p = mp.Pool(processes = 4)#创建4条进程

pool_result = []
for i in range(10):
    msg = 'hello-%d'%i
    r = p.apply(worker,(msg,))#向进程池中添加事件
    pool_result.append(r)

#获取事件函数的返回值
for r in pool_result:
    print('return:',r) 

p.close()#　关闭进程池,不再接受请求
p.join() # 等待进程池中的事件执行完毕，回收进程池
```
结果：
```
8419  
hello-0  
8418  
hello-1  
8420  
hello-2  
8421  
hello-3  
8419  
hello-4  
8418  
hello-5  
8420  
hello-6  
8421  
hello-7
8419
hello-8
8418
hello-9　　　　
return: hello-0　　
return: hello-1　　
return: hello-2　　
return: hello-3　　
return: hello-4　　
return: hello-5　　
return: hello-6　　
return: hello-7　　
return: hello-8　　
return: hello-9　
#这段代码运行较慢，和进程阻塞有关。相当于单线程
```  
**applay_async方式添加任务**
```
import multiprocessing as mp
import os 
from time import sleep 

def worker(msg):
    print(os.getpid())
    sleep(2)
    print(msg)
    return msg

#创建进程池对象
p = mp.Pool(processes = 4) #创建4条进程

pool_result = []
for i in range(10):
    msg = 'hello-%d'%i
    r = p.apply_async(worker,(msg,)) #向进程池中添加事件
    pool_result.append(r)

#获取事件函数的返回值
for r in pool_result:
    print('return:',r)

p.close()#关闭进程池,不再接受请求
p.join()# 等待进程池中的事件执行完毕，回收进程池
```
结果：
```
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e37d68>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e37e80>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e37f98>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e410f0>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41208>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41320>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41438>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41550>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41668>
return: <multiprocessing.pool.ApplyResult object at 0x7f66d0e41780>
8739　　
8740　　
8742　　
8741　　
hello-0　　
hello-3　　
8742　　
hello-1　　
8739　　
8740　　
hello-2　　
8741　　
hello-5　　
8739　　
hello-6　　
8740　　
hello-7　　
hello-4 　
hello-8　　
hello-9　　
#由于这个是异步方式添加任务，所以运行非常快  
#由于for是内置循环函数，执行效率较高，所以在结果的前10行均为for语句执行结果  
#由于任务是异步执行，所以在结果中是“乱序”；并不像applay那样有序打印  
```
**map函数**
```
a = [1,2,3,4,5]

res = map(str,a)
print(res)
```
结果：  
><map object at 0x00000189530DA580>迭代器  
> `print(list(res))` 这样就可以看见其中的内容为 ['1', '2', '3', '4', '5']可以将list(res)保存到一个变量中，方便以后使用

```
a = [1,2,3,4,5]
b = [6,7,8,9,10]

def add(x,y):
    return x,y
res = map(add,a,b)
print(list(res))
```
结果：  
> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
```
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13]

def add(x,y,z):
    return x,y,z
res = map(add,a,b,c)
print(list(res))
```
结果：
> [(1, 6, 11), (2, 7, 12), (3, 8, 13)]
