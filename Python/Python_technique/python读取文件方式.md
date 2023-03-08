# read方法
作用：读取整个文件，将文件内容放到一个字符串变量中，包括换行符。  
缺点：如果文件过大，尤其是大于内存时，无法使用`read()`方法。  
注：可以使用`f.read().splitlines()`来返回一个只有文件内容没有换行符的列表。  
`str.splitlines([keepends])`  
Python splitlines() 按照行界符('\r', '\r\n', \n'等)分隔，返回一个包含各行作为元素的列表，默认不包含行界符。  
keepends -- 在输出结果里是否保留换行符，默认为 False，不包含换行符，如果为 True，则保留换行符。

# readline方法
作用：`readline()`方法每次读取一行，返回的是一个字符串对象。  
缺点：比readlines慢得多。

# readlines方法
作用：读取所有行然后把它们作为一个字符串列表返回。  


