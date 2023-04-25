# JS的书写位置
### 内部JS
![image](https://user-images.githubusercontent.com/96570699/234169382-2fac81fa-bc1d-4020-b9b6-0cc2a9816194.png)  


### 外部JS
![image](https://user-images.githubusercontent.com/96570699/234170598-f24c9189-173a-40a3-bf39-556bbfa71205.png)  


### 内联JS
![image](https://user-images.githubusercontent.com/96570699/234170746-69424cce-8347-48ea-8b1f-c009fbbaec75.png)  


# JS的输入输出
## 输出
### alert()
`alert('弹出内容')` 弹出警告框并在里面显示内容。  
写几个alert就弹出几个警告框。  

### document.write()
```
document.write('div标签')      # 将内容写到HTML文档的<body></body>当中
document.write('<h1>一级标题</h1>')    # 可以解析标签内容
```

### console.log()
` console.log('控制台输出内容')` 该方法弹出内容只能在浏览器调试工具的控制台当中看到。  
![image](https://user-images.githubusercontent.com/96570699/234182660-a7cba66a-e9fc-47b6-ae08-be51b04379a0.png)  


## 输入
### prompt()
![image](https://user-images.githubusercontent.com/96570699/234183072-68d71d02-1467-4ae3-aa43-a57b87c565b7.png)  


# JS的执行顺序
![image](https://user-images.githubusercontent.com/96570699/234183958-93185933-b83b-4cda-b255-86377cd224c1.png)  


# 变量
# 变量的基本使用
![image](https://user-images.githubusercontent.com/96570699/234185392-6f21f9fc-9566-422a-a88c-d0eb3792b1c7.png)  
let不能声明重名的变量，要更新它只要重新给它赋值即可。   
# 变量的赋值
```
# 第一种
let age
age = 18
# 第二种
let age = 18
# 声明多个变量
let age = 18, uname = 'USER'
```
**注：let和var的区别**  
![image](https://user-images.githubusercontent.com/96570699/234191125-58b99d0a-1e4a-47f9-999b-7622256389e8.png)  


# 数组变量
![image](https://user-images.githubusercontent.com/96570699/234191509-3369f09a-f787-4853-91f6-65989f2888cc.png)  
![image](https://user-images.githubusercontent.com/96570699/234194252-d27ba351-faf6-4a3c-9ba0-5393ca073a7a.png)  


# 常量
![image](https://user-images.githubusercontent.com/96570699/234209802-04741ec7-6a9f-44d3-8bee-09d833fa825e.png)  
常量不允许`const a`这样声明，声明的时候必须进行赋值初始化。   



