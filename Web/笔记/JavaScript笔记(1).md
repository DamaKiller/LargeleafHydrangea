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


# JS的数据类型
![image](https://user-images.githubusercontent.com/96570699/234214582-e22512f3-b866-4952-9a83-13f013c34aae.png)  
### 数字类型（Number）
![image](https://user-images.githubusercontent.com/96570699/234215108-a6cdd92a-8925-4f97-ab39-4e1815a39e6c.png)  
![image](https://user-images.githubusercontent.com/96570699/234217948-e2c951c0-748b-4163-bcfc-e9a365cb9bf8.png)  


### 字符串类型（string）
![image](https://user-images.githubusercontent.com/96570699/234221864-4978f834-8ca9-4305-8ccc-d32c74804d04.png)   
JS的字符串也能通过+号进行拼接（只要其中一边是字符串都会按照字符串来拼接，EX：`'string' + 1`结果是string1）。   
**JS的`f'{}'`方法：**  `'今年我${变量}岁了'`  在python中用f和{}，JS中用$和{}来使用。  


### 布尔类型（boolean）
![image](https://user-images.githubusercontent.com/96570699/234226763-bfe1c828-303e-4a05-9c4a-3098efcb1565.png)  


### 未定义类型(undefined)
![image](https://user-images.githubusercontent.com/96570699/234228705-f4ff6333-674a-4c11-a105-baca75ef5c9f.png)  


### 空类型(null)
![image](https://user-images.githubusercontent.com/96570699/234229315-6488248c-74a6-4390-9b5b-f51f40a51851.png)  
用`typeof(obj)`来查看它是object类型。  
**检测数据类型方法:**   
![image](https://user-images.githubusercontent.com/96570699/234231523-595c2e2c-ebe4-4d58-bc0d-bca1ccf2f746.png)  


### 隐式转换和显示转换
**由`prompt`和表单取过来的值默认都是字符串类型**  
**隐式转换**   
![image](https://user-images.githubusercontent.com/96570699/234244474-7f34c61b-b80b-4211-af07-8e1430d8200c.png)    
在隐式转换中 '2'+2 是22， '2'-2是0, +'123'是正的123的意思。    


**显示转换**  
![image](https://user-images.githubusercontent.com/96570699/234245753-403f2d66-10c9-47ef-8ee6-edfdf8625090.png)  




