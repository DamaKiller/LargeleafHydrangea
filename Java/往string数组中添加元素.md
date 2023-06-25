```
String[] array = new String[]{"element1", "element2", "element3"};
array = Arrays.copyOf(array, array.length + 1);    #复制一个原数组，并将它的长度+1
array[array.length - 1] = "element4";    #将最后的索引赋值为想要添加的元素
```     
因为java中数组长度在定义时就已经设定好，所以不能在后面直接添加元素。    

