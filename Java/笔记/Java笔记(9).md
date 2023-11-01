# HashMap
就是所谓的字典。  
HashMap允许Key和Value都为null。
HashMap如果插入相同的Key，则后面的value将会覆盖前面的Value。
```
public class test_java_7 {
    public static void main(String[] args) {
        Map<String, Object> hasMap = new HashMap<String, Object>();

        hasMap.put("name", "zhangsan");
        hasMap.put("age", 20);
        hasMap.put("addr", "北京市");
        hasMap.put(null, null);
        hasMap.put("info", null);
        hasMap.put(null, "who");

        Set<String> setKey=hasMap.keySet();

#用for-each方法遍历
        for(String i: setKey){
            Object str=hasMap.get(i);
            System.out.println("Key的值为："+i+"    "+"Value的值为："+str);
        }

    }
}
```
**注**  
java中foreach,可以认为是增强版的for语句循环，它可以减少代码量，但是不是所有的foreach都可以代替for循环。  
```
for（元素类型type  元素变量value  ：遍历对象obj）{
     引用x的java语句
}

# 例子
# 输出1维数组
        int[] array = {1, 2, 3};

        for (int i : array) {
            System.out.println(i);
        }

# 输出2维数组
        int[][] array = {{1, 2, 3}, {5, 6, 7}};

        for (int[] i : array) {
            for(int y : i) {
                System.out.println(y);
            }
        }

```




### 调用keySet方法遍历
调用keySet()方法，Set<>泛型约束应与Key的数据类型一致.将所有的Key整理成一个集合。  


### HashMap调用entrySet()方法遍历
<Key,Value>键值对，在Java语言中又被称之为Entry/entry，HashMap.Entry就相当于Student.name，若name的数据类型为String，则Student.name的数据类型为String,
同理若<key,value>中key的数据类型为String，value的数据类型为Object，则HashMap.Entry的数据类型为<String, Object>，在这里就是<String, Object>.   
`Set<HashMap.Entry<String, Object>> setHas = hasMap.entrySet();` 代码的意思为将HashMap中所有(Key,Value)值存入Set集合.  
```
        # 就可以用for-each语句打印出来  
        for (HashMap.Entry<String, Object> i : setHas) {
           System.out.println("Key的值为：" + i.getKey() + "    " + "Value的值为：" + i.getValue());
        }
```

