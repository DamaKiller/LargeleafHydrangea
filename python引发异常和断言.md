# assert的作用
python `assert`断言是声明其布尔值必须为真的判定，如果发生异常就说明表达式为假。用来测试表示式，其返回值为`False`，就会触发异常。  

## assert断言的语法格式
`assert 表达式, '输出信息'`

## 例子
`assert 2 == 1, '二不等于一'`  
**结果：** ![image](https://user-images.githubusercontent.com/96570699/170164680-fb9f51ca-0a5d-41bf-bfc4-03155c93735b.png)  

```
a = 0
assert a
```
**结果：**![image](https://user-images.githubusercontent.com/96570699/170165371-2e8ce73c-cb3a-4b97-b9bd-7c6d9ddd9e8c.png)  

# raise的作用
当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，**raise后面的语句将不能执行**。  

## raise语法格式
`raise 错误名(reason)`

## 例子
```
a = 0
if a == 0:
    raise Exception("Invalid a", a)
```
**结果：**![image](https://user-images.githubusercontent.com/96570699/170173986-3567f442-34c2-4127-bc5f-b5afc6b61567.png)  

**注:** 捕获异常类型会从上往下执行，如果都没有对应的类型错误，才执行到“Exception”，可以写多个exept来捕获异常。
```
except ValueError as e:
    print("ValueError", e)
except IndexError as e:
    print("IndexError", e)
except Exception as e:
    print("Exception", e)
```
