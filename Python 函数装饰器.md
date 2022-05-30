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
print(sayhello)   #<function say_hello at 0x00000121D87E51F0>   这里没有在使用小括号，因为我们并不是在调用say_hello函数,而是将它放在变量里
```
