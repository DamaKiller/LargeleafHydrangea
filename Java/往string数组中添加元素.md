```
String[] array = new String[]{"element1", "element2", "element3"};
array = Arrays.copyOf(array, array.length + 1);    #复制一个原数组，并将它的长度+1
array[array.length - 1] = "element4";    #将最后的索引赋值为想要添加的元素
```     
因为java中数组长度在定义时就已经设定好，所以不能在后面直接添加元素。    
`Arrays.copyOf(数组名，扩容后长度)：数组扩容`  此方法可以用于扩容，也可以用于缩容，改变其第二个参数即可.  

