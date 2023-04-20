# HTML固定结构
![image](https://user-images.githubusercontent.com/96570699/232649866-4ec67486-8b61-4c9a-bb8b-5a619d851456.png)   
按！+Tab可以快速格式化出标准html格式  


# 标签注意点
![image](https://user-images.githubusercontent.com/96570699/232661182-b0386463-e1b5-4bf7-b10e-07ad5e8e9a5d.png)   
**例如**  `双标签：<strong> </strong> <div> </div>   单标签： <br> <hr> `   
有需要包裹内容的就是双标签， 不用包裹内容的就是单标签。  
**标签速查表：**  [https://www.w3school.com.cn/html/html_quick.asp  ](https://www.runoob.com/html/html-quicklist.html)   
超链接标签的链接是网页地址就跳转到网页，本地的html文件地址就是打开该文件页面，`<a href="#">空页面</a>`就是空连接。    
**表格标签完整写法：**  
```
<table border="1" width="***" height="***">
  <caption>表格大标题</caption>
  <!--表格头-->
  <thead>   
      <tr>
        <th>表格标题</th>
        <th>表格标题</th>
      </tr>
  </thead>
  <!--表格主体-->
  <tbody>
      <tr>
        <td>表格数据</td>  <!--<td colspan='2'>表格数据</td> 就会将这两个单元格合并-->
        <td>表格数据</td>
      </tr>
  </tbody>
  <!--表格尾-->
  <tfoot>
      <tr>
        <td>表格数据</td>
        <td>表格数据</td>
      </tr>
  </tfoot>
</table>
```    
表格内合并时，上下合并保留上面的，左右合并保留左边的。  跨行合并用`rowspan`，跨列合并用`colspan`，只有同一个结构中的单元格可以合并，不能跨结构合并（thead，tbody，tfoot ）。    
表单标签内可以加`<input type="text" placeholder="请输入内容">`属性添加提示内容。     
单选表单`<input type="radio" name="gender" checked>男 <input type="radio" name="gender">女`当中必须加相同的name属性才能实现单选否则两个都能被选中，加上checked使其默认被选中。      
`<input type="file" multiple>`可以实现多个文件上传功能。    
`<input type="button" value="普通按钮">`可以添加一个普通按钮，并添加js代码添加功能。       
重置按钮必须放在表单域里才能重置对应的内容。    
`<input type="radio" name="gender" id="man"> <label for="man">男</label> `或 `<label><input type="radio" name="gender" id="man"> 男</label> `该标签可以实现点击男文字也可以选中该按钮。     
网页布局用`<div> </div>`和`<span> </span>`标签，div一行只能放置一个， span一行可以放置多个。  
一个空格的字符实体为`&nbsp;`  








