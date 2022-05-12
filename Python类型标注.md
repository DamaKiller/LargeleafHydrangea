**Python是动态类型语言，即变量本身在编译期不携带类型信息的语言。**  
int, float, str三种类型可以直接进行标注。  
```
def greeting(name:str) -> str:
    return 'hello ' + name

print(greeting('xiaoli'))   #hello xiaoli
```  
List, Tuple, Dict要想实现类型标注，必须从`typing`包中导入类型。可以用[]来指定内部基础类型,Tuple, Dict也要用[]来指定。  
```
from typing import List

def calling(letter:List[str]) -> str:
    for i in letter:
        print(i, end = ' ')

letter = ['a', 'b', 'c', 'd']   #a b c d 
calling(letter)
```  
除此之外，基础类型是可以相互嵌套的，比如字典的值是列表，列表中存放元组。  
```
def do_nothing(a: Dict[str, List[Tuple[int, int, int]]], ):
  pass
```
还可以指定生成器作为返回对象。`-> Generator`就可以。

