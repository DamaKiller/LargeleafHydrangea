# 一.作用
在python中可以通过该方法来操作环境变量。  
os.environ是一个环境变量的字典。它的所有操作都是类似于对字典的操作。  
![image](https://user-images.githubusercontent.com/96570699/173003100-751ead08-01e9-4e74-98d6-6325fd193617.png)  

# 二.操作方法
### 1.os.environ.get(key) 
- 该方法通过传入key值，在环境变量中查找对应的环境变量值。若不存在，则返回None。
- os.environ虽然是一个环境变量的字典，但类型并不是`<class ‘dict’>`，不是所有字典的函数都能用。
- 也可以设置默认值，当键存在时返回对应的值，不存在时，返回默认值。`os.environ.get(key, default)`
![image](https://user-images.githubusercontent.com/96570699/173004073-2aeec74b-4e01-44e6-be67-e757f5778cae.png)  ![image](https://user-images.githubusercontent.com/96570699/173004170-ac4f3b92-a5c9-4239-b032-902608de3435.png)

### 2.os.environ.keys()
- 该方法可以查找当前环境下所有的环境变量值。  
![image](https://user-images.githubusercontent.com/96570699/173004532-1c2defaf-f026-40c3-ae29-2d5e06461635.png)

### 3.os.environ[key] = VALUE
- 该方法类似给字典键赋值，key为环境变量名，value为环境变量值。  
- 该方法设置的是临时环境变量。

### 4.os.environ.pop('KEY')
- 删除该环境下KEY的临时环境变量。

### 5.os.environ.clear()
- 该方法会清空当前环境下所有的临时环境变量。
