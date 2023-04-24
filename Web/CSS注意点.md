# CSS在html文件中的位置
在HTML文件中CSS样式都写在head标签当中。  
![image](https://user-images.githubusercontent.com/96570699/233316666-0bb4f235-c96f-4ca1-b7d7-cd59b1c00c3f.png)    


# CSS的引入方式
![image](https://user-images.githubusercontent.com/96570699/233890054-d217a95d-d194-4612-a4d2-33a336866024.png)  


**内嵌式写法：**    
```
<style>
    element {
      属性名：属性值
    }
</style> 
```  
**外联式写法**　　
```
element {
  属性名：属性值
}

# 想引用样式的文件
<head>
    <link rel="stylesheet" href="CSS文件地址">
</head>
```
**行内式写法**
```
<div style="color:green; font-size: 50px;"></div>
```

