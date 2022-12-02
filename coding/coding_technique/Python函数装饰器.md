# 一.简绍
## 什么是装饰器
装饰器指的是定义一个函数，该函数用来为其他的函数添加功能。简单来说就是扩展原来函数功能的一种函数。  
## 为什么要用装饰器
装饰器可以在不修改对象源代码以及调用方式的前提下为被装饰对象添加新功能。它经常被用于插入日志，性能测试，事务处理，缓存，权限校验等场景。  
有了装饰器，就可抽出大量与函数本身无关的雷同代码并重复使用。提高了程序的可重复利用率，并增加了程序的可读性。
## 特点
(1) 自动把下面修饰的原函数当成参数传递给装饰器  
(2) 把返回的新函数去替换原函数  
## python中的函数
```
def say_hello(name = 'song'):
    return f'hello {name}'
print(say_hello())    #hello song
```
甚至可以将一个函数赋值给一个变量  
```
def say_hello(name = 'song'):
    return f'hello {name}'

sayhello = say_hello
print(sayhello)   #<function say_hello at 0x00000121D87E51F0>   
#这里没有在使用小括号，因为我们并不是在调用say_hello函数。这里返回的是函数体内存地址。
#而是将它放在变量里,python中一切皆是对象，函数也不例外。
```
**在函数中定义函数**
```
def hi():
    def greeting():
        return 'now you are in greeting function'
    def welcome():
        return 'now you are in welcome function'
    print(greeting())
    print(welcome())
    return 'now you are in hi function'

print(hi())
#now you are in greeting function
#now you are in welcome function
#now you are in hi function 
```
**在函数中返回函数**
```
def hi(name = 'song'):
    def greeting():
        return 'now you are in greeting function'
    def welcome():
        return 'now you are in welcome function'
    if name == 'song':
        return greeting()
    else:
        return welcome()

print(hi())
#now you are in greeting function
print(hi)
#<function hi at 0x000001EC4D1C51F0>
```
**将函数作为参数传递**
```
def greet():
    return 'you are in greet function'
def do_before_greet(func):
    print('now you are in do_before_greet')
    return func
print(do_before_greet(greet()))
# now you are in do_before_greet
# you are in greet function
print(do_before_greet(greet))
# now you are in do_before_greet
# <function greet at 0x000001EABA1051F0>
```
**函数内省:即可以访问的函数的部分属性**
```
print(dir(print))   #可以使用该方法查看一个函数的所有内省
```
![image](https://user-images.githubusercontent.com/96570699/171336414-a5fe2115-c426-4d7e-a07b-645799f3bd5a.png)

```
print(print.__doc__)
```
![image](https://user-images.githubusercontent.com/96570699/171336324-413dca62-6b22-4e04-af00-cb1b3d8eea94.png)


**装饰器的等价写法**
```
def decorator(func):
    def wrapTheFunction():
        print('do some work before executing func()')
        func()
        print('do some work after executing func()')
    return wrapTheFunction

def a_function_need_decoration():
    print('this is a_function_need_decoration')

function_and_decoration = decorator(a_function_need_decoration)
function_and_decoration()
#这正是 python 中装饰器做的事情！它们封装一个函数，并且用这样或者那样的方式来修改它的行为。并且不修改原函数的调用方式和源代码。
```

# 二.装饰器
**函数装饰器**
使用装饰器完成之前的代码。
用`@+装饰器函数名字`放在需要被装饰函数的上方即可，现在直接调用a_function_need_decoration即可实现装饰器的功能！
这是非常Pythonic的写法，不用每次调用function_and_decoration。
```
def decorator(func):
    def wrapTheFunction():
        print('do some work before executing func()')
        func()
        print('do some work after executing func()')
    return wrapTheFunction

@decorator
def a_function_need_decoration():
    print('this is a_function_need_decoration')

# function_and_decoration = decorator(a_function_need_decoration)
a_function_need_decoration()    #装饰器只不过一个简短的方式来生成一个被装饰的函数。装饰器的作用跟上面那句被注释的代码的作用是一样的。
```
**类装饰器**  
相比于函数装饰器，类装饰器具有灵活度大，高内聚，封装性等优点。使用类装饰器，可以使用内部的__call__方法，当使用@形式将装饰器附加到函数上时，就会调用此方法。
```
class decorator_class():
    def __init__(self, func):
        self._func = func
    def __call__(self):
        print(f'{self._func.__name__} 即将运行')
        self._func()
        print(f'{self._func.__name__} 运行结束')
@ decorator_class
def function_1():
    print('this is function_1')

function_1()
```

# 三.例子
**用来验证，被用于django和flask架构中。**
```
def auth(func):
    def account():
        name = input('输入用户名： ').strip()
        pwd = input('输入密码： ').strip()
        if name == 'song' and pwd == 'song':
            res = func(name)
            return res
        else:
            return '账号密码错误'
    return account

@auth
def welcome(name = 'song'):
    return f'welcome {name}'
print(welcome())
```
![image](https://user-images.githubusercontent.com/96570699/171544820-79e34044-3a7d-404f-96d3-84c9810a95da.png)  

**被修饰的函数带有参数**
```
def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print(f'被装饰函数 {func.__name__} 即将被执行')
        func(*args, **kwargs)
        print(f'被装饰函数 {func.__name__} 执行完毕')
    return wrapper_func

@ decorator_func
def add(x, y):
    print(f'{x} 和 {y} 的结果为 {x + y}')

add(2, 3)
```
![image](https://user-images.githubusercontent.com/96570699/171347505-7d71b034-c4c2-4735-b244-36c57199a080.png)  

**输出日志**
```
import logging
def taking_logging(func):
    def wrapper_func(*args, **kwargs):
        logging.warning(f'被装饰函数 {func.__name__} 即将被执行')
        func(*args, **kwargs)
    return wrapper_func

@ taking_logging
def function_1():
    print(f'this is function_1')

@ taking_logging
def function_2():
    print('this is function_2')
function_1()
function_2()
```
![image](https://user-images.githubusercontent.com/96570699/171537565-7e52a14f-a6ed-4c54-9938-2efda2a7c531.png)  

**带有参数的装饰器**
```
def taking_loglevel(level):
    def taking_logging(func):
        def wrapper_func(*args, **kwargs):
            if level == 'warn':
                logging.warning(f'被装饰函数 {func.__name__} 即将被执行')
                return func(*args, **kwargs)
        return wrapper_func
    return taking_logging

@ taking_loglevel(level = 'warn')
def function_1(name = 'song'):
    print('this is %s' %name)

function_1()
```
![image](https://user-images.githubusercontent.com/96570699/171540626-0d0c3722-cfb0-4bc3-abf8-b75c1efb9e3b.png)  
taking_loglevel是允许带参数的装饰器。它实际上是对原有装饰器的函数封装，并返回一个装饰器。可以将它理解为一个带有参数的闭包。

# 四.functools.wraps
使用装饰器的缺点就是原函数的元信息不见了。比如函数的__name__，docstring，参数列表等。在装饰器实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。  
一般定义装饰器的话可以不用考虑这点,但是如果多个函数被两个装饰器装饰时就报错,因为两个函数名一样,第二个函数再去装饰的话就报错。  
**副作用**
```
def logged(func):
    def with_logging(*args, **kwargs):
        '''decorator'''
        print(f'{func.__name__} 正在运行')
        return func(*args, **kwargs)
    return with_logging


@logged
def welcome(name = 'song'):
    return f'welcome {name}'
print(welcome.__name__, welcome.__doc__)
```
![image](https://user-images.githubusercontent.com/96570699/171774092-8074a681-e44b-4537-9d23-75ae52b7867f.png)  
**加上wraps后**
```
import functools

def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        '''decorator'''
        print(f'{func.__name__} 正在运行')
        return func(*args, **kwargs)
    return with_logging

@logged
def welcome(name = 'song'):
    '''welcome'''
    return f'welcome {name}'
print(welcome.__name__, welcome.__doc__)
```
![image](https://user-images.githubusercontent.com/96570699/171774453-59725ec0-9dc2-40f7-831f-8a2b7d88668c.png)

# 五.装饰器的顺序
```
@a
@b
@c
def f():
```
等效于
```
f = a(b(c(f)))
```
