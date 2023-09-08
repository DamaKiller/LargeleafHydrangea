# 集合
![image](https://user-images.githubusercontent.com/96570699/204971656-1a425cb6-700f-4ae7-8f5c-6060f6c332d3.png)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/ea014019-743e-4699-b327-d37edf69e69a)  
![image](https://user-images.githubusercontent.com/96570699/204972782-8adf965a-8730-467d-869a-0217c0fbcf6e.png)   
**注**  
直接打印数组变量会将数组的地址值打印出来，用`Arrays.toString(数组名)`，多维数组用`Arrays.deepToString()`可以输出带元素的数组, 直接打印集合变量会打出一个空集合。   
![image](https://user-images.githubusercontent.com/96570699/204972567-d6506fa5-0698-4b59-84a2-d4447b22abf1.png)   
**创建二维数组：**    
格式1： 数组类型[][] 数组名 = new 数组类型[一维数组的个数][每一个一维数组中元素的个数];  Ex：int[][] arr=new int[3][2];  
格式2： 数据类型[][] 数组名 = new 数据类型[一维数组的个数][];这一次没有直接给出一维数组的元素个数，可以动态的给出.    
Ex：int[][] arr=new int[3][];  arr[0] = new int[2]; arr[1]= new int[3]; arr[2]=new int[1];    
格式3： 数据类型[][] 变量名=new 数据类型[][]{{元素...},{元素...},{元素...}};  数据类型[][] 变量名={{元素...},{元素...},{元素...}};  
Ex：int[][] arr={{1,2,3},{4,6},{6}};     
**注**  
数组长度是固定的，length属性只能获取数组定义的长度，不是实际存储元素的多少，数组创建完后就不能修改其长度。  
而集合会自动扩容减容，当增加元素时，长度自动加一，减少一个元素时，长度减一。  
实际操作中基本上不关注返回值，`list.add(元素); list.remove(元素);`即可。   
而当需要使用被删除或增加的元素时， `String str = list.remove(元素索引); String str = list.set(元素索引, 元素);(返回被修改的元素)`  





# 静态变量，静态方法
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9c388558-4362-4895-823d-31d3b2a536d5)   
**注**  
优先于类，是对象只有在new之后才会在内存中出现，而静态对象在加载该类后就会在内存中出现。   
**public和private是访问权限修饰符，用于控制外界对类内部成员的访问。**    
public：表明对象成员是完全共有的，外界可以随意访问。  
private：表明对象成员是完全私有的，不容许外界的任何访问。  

**static和final是控制类成员变化的修饰符。**  
static：静态成员修饰符，其修饰的静态变量脱离具体对象独立存在，在内存中之后一份拷贝，所有的对象都公用这一个存储空间，   
所以对static修饰的静态变量进行的修改对该类的所有对象都起作用。static修饰的静态函数代表所有对象的统一操作只能调用静态变量。  
就是被static修饰的变量或方法对所有创建的对象的来说，都是相同的，都是同一个值。static是针对面向对象中的“多态”而提出来的，static修饰的静态成员不存在多态性。   
Ex:类名调用`Phone.brand = 'apple'`  
final：final用来修饰方法和属性表示特殊的意义。修饰方法时表示方法不能被重写；修饰属性时表示属性不能被改变，  
这里属性又分为对象和基本类型，修饰基本类型表示基本类型赋值以后不能再被赋值，修饰对象表示这个属性不能再指向其他对象(引用不变)，但是他指向的这个对象本身还是可以被改变的。  


![image](https://user-images.githubusercontent.com/96570699/204996931-b2f63998-0409-4188-9e0d-1bd416897b3c.png)  
**工具类的定义规范**    
> 1.命名以复数(s)结尾，或者以Utils结尾  
> 如 Objects、Collections、IOUtils、FileUtils  
> 2.构造器私有化   
> 构造器私有化，这样无法创建实例对象，也无法产生派生类。  
> 3.方法使用 static 修饰  
> 因为构造器私有化了，那么对外提供的方法就属于类级别，也方便调用。   
> 4.异常需要抛出，不要 try-catch  
> 将异常交给调用者处理  
> 5.工具类不要打印日志  
> 工具类属于公共的，所以不要有定制化日志  
> 6.不要暴露可变属性  
> 工具类属于公共类，所以不要暴露可变的属性;如List集合等(可以返回不可变的集合，或者拷贝一个暴露给调用者，这样调用者修改了集合中元素，不会影响到工具类中的集合元素)  　
![image](https://user-images.githubusercontent.com/96570699/205006077-e0640b04-e03e-4a0f-bcd3-fb10df1078db.png)　　
第一次调用时会把s1的地址赋给this，第二次调用时会把s2的地址赋给s2，只不过this被隐藏了，调用其他方法也一样，这是虚拟机自动赋值的，自己更改不了.
> 因为在该方法内没有重名的变量，所以this被省略不写。  
> 因为静态方法和静态变量是共享的，所以在设计时就把this省略了,因为共享的变量和方法都是相同的，所以静态对象不能访问非静态的内容（加this也不行，因为静态方法中没有this）。  
![image](https://user-images.githubusercontent.com/96570699/205007324-a6622dc5-2b8b-4afc-8d43-299102594874.png)　　
![image](https://user-images.githubusercontent.com/96570699/205008245-eaa48d6c-de7f-4a16-a2b8-15ebb19d522e.png)  
![image](https://user-images.githubusercontent.com/96570699/205009588-514f17be-16ad-40cc-a804-9d3b7b75ce40.png)   
  



# main方法
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/62d8e8f0-40c0-44a9-afb8-16a46d924375)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/90d89abd-02f7-4f63-af2e-9aa06738a978)  
可以在配置文件中设置args的值。现在已经不用该方式了，现在用的时Scanner。    


 






