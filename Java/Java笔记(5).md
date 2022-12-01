# 集合
![image](https://user-images.githubusercontent.com/96570699/204971656-1a425cb6-700f-4ae7-8f5c-6060f6c332d3.png)  
![image](https://user-images.githubusercontent.com/96570699/204972782-8adf965a-8730-467d-869a-0217c0fbcf6e.png)  
![image](https://user-images.githubusercontent.com/96570699/204972567-d6506fa5-0698-4b59-84a2-d4447b22abf1.png)  




# 静态变量
![image](https://user-images.githubusercontent.com/96570699/204984503-5374a2de-f483-4bfd-a304-e9f63ad7e02f.png)　　
**注**  
**public和private是访问权限修饰符，用于控制外界对类内部成员的访问。**    
public：表明对象成员是完全共有的，外界可以随意访问。  
private：表明对象成员是完全私有的，不容许外界的任何访问。  

**static和final是控制类成员变化的修饰符。**  
static：静态成员修饰符，其修饰的静态变量脱离具体对象独立存在，在内存中之后一份拷贝，所有的对象都公用这一个存储空间，
所以对static修饰的静态变量进行的修改对该类的所有对象都起作用。static修饰的静态函数代表所有对象的统一操作，
只能调用静态变量。static是针对面向对象中的“多态”而提出来的，static修饰的静态成员不存在多态性。  
final：final用来修饰方法和属性表示特殊的意义。修饰方法时表示方法不能被重写；修饰属性时表示属性不能被改变，
这里属性又分为对象和基本类型，修饰基本类型表示基本类型赋值以后不能再被赋值，修饰对象表示这个属性不能再指向其他对象(引用不变)，但是他指向的这个对象本身还是可以被改变的。  


![image](https://user-images.githubusercontent.com/96570699/204996931-b2f63998-0409-4188-9e0d-1bd416897b3c.png)  
**工具类的定义规范**    
> 1.命名以复数(s)结尾，或者以Utils结尾  
> 如 Objects、Collections、IOUtils、FileUtils  
> 2.构造器私有化   
> 构造器私有化，这样无法创建实例，也无法产生派生类  
> 3.方法使用 static 修饰  
> 因为构造器私有化了，那么对外提供的方法就属于类级别  
> 4.异常需要抛出，不要 try-catch  
> 将异常交给调用者处理  
> 5.工具类不要打印日志  
> 工具类属于公共的，所以不要有定制化日志  
> 6.不要暴露可变属性  
> 工具类属于公共类，所以不要暴露可变的属性;如List集合等(可以返回不可变的集合，或者拷贝一个暴露给调用者，这样调用者修改了集合中元素，不会影响到工具类中的集合元素)  　
![image](https://user-images.githubusercontent.com/96570699/205006077-e0640b04-e03e-4a0f-bcd3-fb10df1078db.png)　　
第一次调用时会把s1的地址赋给this，第二次调用时会把s2的地址赋给s2.  
![image](https://user-images.githubusercontent.com/96570699/205007324-a6622dc5-2b8b-4afc-8d43-299102594874.png)　　




