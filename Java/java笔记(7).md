# 权限修饰符
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/f183a22f-69e2-4951-8852-c6f15173d240)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/502ed4a2-18ff-4daf-ac36-add7fff0bdda)    
**注**  
空着不写就是`String Name；`这样的，什么修饰符也没有。  
不同包下的子类为如下形式，最下面的Test就是不同包下的无关类：   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/b0e9b879-7c60-4ac4-8301-848339f12566)    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/fd96cdbd-6bfe-4791-893e-19615b32b66e)  


# 代码块
局部代码块跟其他语言一样。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/de7a15e9-1443-4294-b680-481b1c5ab296)   
这种方式不常用，太不灵活，该条语句无论如何都会执行。一般都是提取成一个方法然后调用。    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/b25804e1-f6b3-40a4-9021-5925cbe59f5b)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/33b6ffba-39c0-4570-a76e-ff034a217257)  
该种方法一般用在数据初始化上，只在第一次加载该类的时候执行一次。  


# 抽象类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/14d7a96e-3b56-4f86-90dd-9bc0b811ea77)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/025a739d-cc31-4d6a-b780-c7a0aa09fe30)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/eedcccb6-3e23-4d1d-973b-7ac92f4e7b03)   
**注**    
因为抽象方法中没有执行语句，无法被调用，所以不能实例化。   
抽象类，抽象方法是为了方便管理才出现的，否则每个子类定义一个方法，标准不统一。   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9fdb890c-335f-4b77-a931-d55d1a889d73)   
 










