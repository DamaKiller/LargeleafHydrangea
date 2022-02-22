#获取该脚本的绝对路径
import os
a = os.path.realpath(__file__)
print(a)      #当前结果为C:\Users\ZZ0C2R672\Desktop\project\test.py


#获取该脚本的上一级文件夹目录
import os
a = os.path.dirname(os.path.realpath(__file__))
print(a)    #C:\Users\ZZ0C2R672\Desktop\project
