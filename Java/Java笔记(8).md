# 接口
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/3457ce74-d0a7-43a4-a4bb-1835c0af2b9e)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/540f3baa-9a0b-469e-a5d4-c8275f5b6def)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/e3a9855c-84a5-4027-8a61-3ac6251a4367)  
默认修饰符就算不加上java也会自动给加上，只不过不显示。  
当继承的两个接口当中有相同的方法时只需要重写其中一个就可以了。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9416c2f7-6ede-46d4-9522-a2f42a13de6b)  
如何想实现了最下面接口的方法，则需要将最下面接口的父类方法都实现才可以。    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/8b0108be-58ba-4fa3-b88d-cda6f2d46da1)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/6ee0f096-c80f-4a08-bb7c-f50f5ea219d5)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/e0ed4739-f2eb-4677-8248-b257d6eae3ad)     
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/568bd5df-ed54-4fc7-b6b4-217345411bf6)    
如果只需要接口中的一个方法，可以单独写一个类来空实现这个接口中的所有方法，然后再写类来继承这个类，单独重写需要的那个方法即可。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/6cf4d322-cc2b-4665-a811-3451807da2d5)   


# 内部类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/08a1b05d-d9f6-4319-b161-34f6e6f6ade0)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/268acf85-7b0e-485b-84b0-3a21514a6a5c)    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/d189788f-4454-4bb8-ab4c-db8e80bc77e5)　　
单独定义一个引擎类没有什么意义,但是又不能给它放到车类里面。   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/cc7ffa8d-df40-440e-8284-1ca5437f5126)    


### 成员内部类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/266f40b4-0e96-4795-b2d2-5fc930f750e6)    
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/09153c91-4d5f-4f0a-868a-46efcad8174a)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/3718e1ac-12f1-4116-9738-4d7c7dc9e033)　　　

第二种定义一个方法返回内部类对象，然后调用这个方法就可以了，该方法一般用在内部类是protect类型的时候。   　　
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/7ec6dc04-c692-4847-8a26-912e96ef0b03)　　 　　
输出内部类中的变量值的方法。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/2d5aa210-9c1e-44e7-8916-0d7f12ede570)   
外部类名.this.变量名可以获取外部变量名。   


### 静态内部类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/3750bad5-a9c4-4d04-8436-74848e6ff389)   　　
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/10318c25-df04-482d-a812-c11fae82cd27)　　　　
直接NEW一个内部类对象。  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/65b0a325-dbe2-4bff-921e-751180ff65d7)   


### 局部内部类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/1ddfa4de-9d16-4189-a913-a6959c918d92)  
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/3e09aa9f-d668-465b-a279-ec303cfa8dc5)  


### 匿名内部类
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/9f2792c7-c5aa-4667-9a51-682f6843bc4f)   
![image](https://github.com/DamaKiller/LargeleafHydrangea/assets/96570699/fd55f0ca-3a5f-408f-a7c7-665c68efb628)  
那个用紫色框起来的类才是真正的内部类，他其实实现了接口，所以需要重写接口中的方法、new创建了后面的匿名对象，空的括号表示用了空参构造创建了后面的对象，这其实是创建了一个对象。     



















