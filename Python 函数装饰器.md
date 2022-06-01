# 一.简绍
## 什么是装饰器
装饰器指的是定义一个函数，该函数用来为其他的函数添加功能。简单来说就是扩展原来函数功能的一种函数。  
## 为什么要用装饰器
装饰器可以在不修改对象源代码以及调用方式的前提下为被装饰对象添加新功能。
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
