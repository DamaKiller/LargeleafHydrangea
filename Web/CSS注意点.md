# CSS在html文件中的位置
在HTML文件中CSS样式都写在head标签当中。  
![image](https://user-images.githubusercontent.com/96570699/233316666-0bb4f235-c96f-4ca1-b7d7-cd59b1c00c3f.png)    


# CSS的引入方式
![image](https://user-images.githubusercontent.com/96570699/233335095-f89b5b44-0042-4d72-ba12-4c87c84f67cb.png)


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


# 类选择器注意事项
![image](https://user-images.githubusercontent.com/96570699/233536785-d9e3d1d7-9aba-48c7-9557-4ce906ce18e2.png)  


# id选择器注意事项
![image](https://user-images.githubusercontent.com/96570699/233546494-93adba7b-0a7e-4006-991b-e0055003ffac.png)   


# 通配符选择器
![image](https://user-images.githubusercontent.com/96570699/233546734-4ad5554f-18d8-48a7-b1fb-f8c59a725061.png)  
它一般用在设置所有边距等共通功能上:![image](https://user-images.githubusercontent.com/96570699/233547181-189a231d-46ad-4160-82f4-c58dac8e49c6.png)   
  

# 样式的层叠问题
![image](https://user-images.githubusercontent.com/96570699/233893017-28433896-337d-4433-aa02-34cc36850ec6.png)   
CSS具有层叠性。  


# 标签注意点
![image](https://user-images.githubusercontent.com/96570699/233896125-4a4e71fa-fd7e-47a0-be99-636cc7e6534f.png)    
`text-decoration:line-through;`可以祛除超链接文字的下划线修饰线。   







