# 一.匿名函数介绍
Python用lambda语法定义匿名函数，只需用表达式而无需申明。在python中，不通过def来声明函数名字，而是通过 lambda 关键字来定义的函数称为匿名函数。  
在开发当中，一次使用的函数或者是我们不想命名的函数，我们可以写成匿名函数。  
**注：**   
- 匿名的目的就是要没有名字，给匿名函数赋给一个名字是没有意义的。   
- 匿名函数的参数规则、作用域关系与有名函数是一样的。  
- 匿名函数的函数体通常应该是 一个表达式,该表达式必须要有一个返回值。  
- lambda可以省去定义函数的过程，让代码更加精简,而且不用考虑命名问题，但是在PEP8规范里面是不推荐用lambda这种方式的。  
# 二.匿名函数定义规则
lambda 参数：表达式  
**注：**  
- `lambda`的主体是一个表达式，而不是一个代码块。仅仅能在`lambda`表达式中封装有限的逻辑进去。  
- `lambda`函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。  
# 三.使用场景
- 要处理的业务符合`lambda`函数的情况（任意多个参数和一个返回值），并且只有一个地方会使用这个函数，不会在其他地方重用，可以使用`lambda`函数。  
- 需要将函数的值作为参数来传递，大多使用匿名函数，比如函数参数key。  
# 四.匿名函数和普通函数的对比 
```
def sum_func(a, b, c):
    return a + b + c
# 将匿名函数对象赋值给 sum_lambda
sum_lambda = lambda a, b, c: a + b + c
print(sum_func(1, 2, 3))  # 6
print(sum_lambda(1, 2, 3))  # 6
```   
# 五.匿名函数的多种形式
```
# 无参数
lambda_a = lambda :100
print(lambda_a())  # 100
  
# 一个参数
lambda_b = lambda num: num * 10
print(lambda_b(1))  # 10
  
# 多个参数
lambda_c = lambda a, b, c: a + b + c
print(lambda_c(1, 10, 100))  # 111
  
# 表达式分支
lambda_d = lambda x: x if x > 5 else x + 1
print(lambda_d(4))  # 5
print(lambda_d(6))  # 6

#lambda 作为一个参数传递
def sub_func(a, b, func):
    print("a = ", a)
    print("b = ", b)
    print("a - b = ", func(a, b))
sub_func(3, 2, lambda a, b: a - b)  #a =  3 b =  2 a - b =  1

#lambda函数与python内置函数配合使用
member_list = [
    {"price": 9},
    {"price": 999},
    {"price": 99}
]
new_list = sorted(member_list, key=lambda dict_: dict_["price"])
print(new_list)  #  [{'price': 9}, {'price': 99}, {'price': 999}]

number_list = [100, 77, 69, 31, 44, 56]
num_sum = list(map(lambda x: {str(x): x}, number_list))
print(num_sum)  # [{'100': 100}, {'77': 77}, {'69': 69}, {'31': 31}, {'44': 44}, {'56': 56}]

#lambda 作为函数的返回值
def discount_func(discount):
    return lambda price: discount * price
  
p = discount_func(0.8)
print(p)  # <function discount_func.<locals>.<lambda> at 0x00000241352BAC10>
print(p(100))  # 80.0
# 匿名函数可以作为一个函数的返回值，上面函数discount_func返回一个设定了折扣的匿名函数对象，调用这个对象，传入价格，就可以得到折扣后的价格
```
