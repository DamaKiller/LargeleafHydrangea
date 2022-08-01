# 一.如何获取命令行参数
可以使用argv函数，它属于sys模块。

# 二.使用
```
args = sys.argv   #sys.argv返回的就是命令行参数
```
sys.argv 返回的是一个列表，第1项是当前的文件名，后面的项依次表示参数项。
例如：python3 文件名 参数1 参数2 参数3， 列表中就是[文件名， 参数1， 参数2， 参数3]。

# 三.其他方面的应用
### 1.pytest测试中
```
def test_1():
  argv_1 = '1'
  argv_2 = '2'
  argv_3 = '3'
  sys.argv = [''] + [argv_1] + [argv_2] + [argv_3]
  with pytest.raises(SystemExit):
      runpy.run_module(运行文件名, run_name='__main__', alter_sys=True)  #alter_sys=True加上该命令后就要可以将上述环境变量传到运行文件当中
```
