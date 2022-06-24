# 一.闭包简绍
简单来说，闭包就是外部函数中定义一个内部函数，内部函数引用外部函数中的变量，外部函数的返回值是内部函数，这样就可以使用函数内部定义的变量。  

# 二.定义条件
- 必须有一个内嵌函数
- 内嵌函数必须引用外部函数中的变量
- 外部函数的返回值必须是内嵌函数

# 三.作用
- 闭包将外层函数内的局部变量和外层函数的外部连接起来。
- 将外层函数的变量持久地保存在内存中。
```
def position(direction = [100, 100]):
    def change_position(pos, step):
        new_x = direction[0] + pos[0]*step
        new_y = direction[1] + pos[1]*step
        direction[0] = new_x
        direction[1] = new_y
        return direction
    return change_position

player = position()
print(player([1,0], 10))
print(player([0,2], 10))    #这说明position中的direction变量一直在内存中，没有被清除。
```
![image](https://user-images.githubusercontent.com/96570699/175453757-9c7645a1-ee63-4ef6-b8e6-bd204353f8bf.png)  
**注**  
*1.position是change_position的父函数，而change_position被赋给了一个全局变量`direction`，这导致change_position始终在内存中，
而change_position的存在依赖于position，因此position也始终在内存中，不会在调用结束后，被垃圾回收机制（garbage collection）回收。
这样外层函数变量direction就持久地保存在内存中。*  
*2.外层函数中的参数，不一定要有，据情况而定，但是一般情况下都会有并在内函数中使用到。*  
```
def func(a,b):
    def add(x):
        return a*x + b
    return add

test = func(1, 2)
print(test(5))
```  
![image](https://user-images.githubusercontent.com/96570699/175457064-9afce007-0edd-4bfb-a346-7425baa02bc5.png)  

# 四.闭包与装饰器的区别
**闭包和装饰器的区别：** 闭包传递的是变量，而装饰器传递的是函数，除此之外没有任何区别，或者说装饰器是闭包的一种，它只是传递函数的闭包
