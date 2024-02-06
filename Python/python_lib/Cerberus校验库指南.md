# 一.Cerberus库简绍
Cerberus是一个Python的第三方包，用于校验指定的数据结构中是否满足要求，例如传进来一个列表，它是否超过了长度限制，是否都为某种数据结构等等。  


# 二.基本使用
主要使用当中的Validator这个类来进行校验，校验器规则可以编写一个Schema参数来初始化，Schema是一个字典类型，它描述了输入数据的格式和规则。  
```
from cerberus import Validator

# 校验器规则
student_shema = {
    'name' : {'type' : 'string', 'required' : True, 'empty' : False,'nullable': True,'regex':'^[a-zA-Z]*$'},
     # 'required'表示是否可以不传这个参数， 'empty'表示是否可以为空,'nullable'表示该值是否可以传入null或none值。
    'age' : {'type' : 'integer', 'required' : True, 'empty' : False,'nullable': True, 'regex':'^[0-9]*$', 'min' : 18, 'max' : 65},
     # 'regex'为正则表达式，该参数需满足的规则，'min'和'max'为对应参数的最小值和最大值
    'email' : {'type' : 'string', 'required' : True, 'empty' : False,'nullable': True, 'regex':'^.+@.+\\..+$'}
}

# 实例化一个Validator
v = Validator(student_shema)

student_a = {
    'name' : 'song', 'age' : 25, 'email':'1209941366@qq.com'
}   # 结果符合

student_b = {
    'name' : 'song', 'age' : 15, 'email':'1209941366@qq.com'
}   # 15小于最小值，结果不符合

if v.validate(student_a):
    print('符合要求')
else:
    print('不符合要求')
```


# 三.进阶使用
```
from cerberus import Validator

# 校验器规则
student_shema = {
    'name' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^[a-zA-Z]*$'},
    'age' : {'type' : 'integer', 'required' : True, 'empty' : False, 'regex':'^[0-9]*$', 'min' : 18, 'max' : 65},
    'email' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^.+@.+\\..+$'},
    # 字典类型
    'address' : {
                    'type': 'dict',
                    'required': True,
                    'schema': {
                        'street': {'type': 'string', 'required': True},
                        'city': {'type': 'string', 'required': True},
                        'state': {'type': 'string', 'required': True},
                        'zipcode': {'type': 'string', 'required': True}
                    }
                },
    # 列表类型
    'hobbies': {'type': 'list', 'schema': {'type': 'string', 'empty': False}},
    # 列表中嵌套字典类型
    'family_members': {'type': 'list',
                       'schema': {'type': 'dict',
                                  'schema': {'name': {'type': 'string', 'required': True, 'empty': False},
                                             'relationship': {'type': 'string', 'required': True, 'empty': False}
                                             }
                                 }
                       }
}

# 实例化一个Validator
v = Validator(student_shema)

student_a = {
    'name':'song', 'age':25, 'email':'1209941366@qq.com',
    'address':{'street':'光中街道', 'city':'大连市', 'state':'辽宁', 'zipcode':'116100'},
    'hobbies':['看漫画'], 'family_members':[{'name':'sun', 'relationship':'mother'}]
}   # 结果符合

if v.validate(student_a):
    print('符合要求')
else:
    print('不符合要求')
```


# 四.自定义规则
Cerberus允许你添加自定义规则（validators），这些规则可以用于验证不符合标准验证函数所支持的自定义类型。添加自定义规则允许你轻松扩展验证器，以适应任何特殊需求。
```
import re
from cerberus import Validator

# 自定义校验器，该处需要传三个参数，field和error定义在该处出现错误时返回的错误信息。
def phone_number(field, value, error):
    regex = r'^[0-9]{11}'
    if not re.match(regex, value):
        error(field, "错误电话号码")

# 校验器规则
student_shema = {
    'name' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^[a-zA-Z]*$'},
    'age' : {'type' : 'integer', 'required' : True, 'empty' : False, 'regex':'^[0-9]*$', 'min' : 18, 'max' : 65},
    'email' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^.+@.+\\..+$'},
    'phone': {'type': 'string', 'required': True, 'empty': False, 'validator': phone_number}
    # 编写一个自定义校验器函数phone_number
}

# 实例化一个Validator
v = Validator(student_shema)

student_a = {
    'name':'song', 'age':25, 'email':'1209941366@qq.com', 'phone':'19999999999'
}   # 结果符合

if v.validate(student_a):
    print('符合要求')
else:
    print('不符合要求')
```

# 五.异常处理
在使用Cerberus验证数据时，我们可能会遇到多种异常情况，如验证失败、Schema格式错误等。Cerberus提供了多种异常处理方式：  
**`Validator.errors`**  
如果某次验证失败，可以调用Validator.errors方法，获取出错的字段及相应的错误信息  
```
import re
from cerberus import Validator

def phone_number(field, value, error):
    regex = r'^[0-9]{11}'
    if not re.match(regex, value):
        error(field, "错误电话号码")

# 校验器规则
student_shema = {
    'name' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^[a-zA-Z]*$'},
    'age' : {'type' : 'integer', 'required' : True, 'empty' : False, 'regex':'^[0-9]*$', 'min' : 18, 'max' : 65},
    'email' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^.+@.+\\..+$'},
    'phone': {'type': 'string', 'required': True, 'empty': False, 'validator': phone_number}
}

# 实例化一个Validator
v = Validator(student_shema)

student_a = {
    'name':'song', 'age':25, 'email':'1209941366@qq.com', 'phone':'1999999999'
}   # 电话号码位数不对,结果为 {'phone': ['错误电话号码']}

if not v.validate(student_a):
    errors = v.errors
    print(errors)
```

**Validator.document_error_tree**  
Validator.document_error_tree方法提供了一个详细的错误树形结构。  
```
import re
from cerberus import Validator

def phone_number(field, value, error):
    regex = r'^[0-9]{11}'
    if not re.match(regex, value):
        error(field, "错误电话号码")

# 校验器规则
student_shema = {
    'name' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^[a-zA-Z]*$'},
    'age' : {'type' : 'integer', 'required' : True, 'empty' : False, 'regex':'^[0-9]*$', 'min' : 18, 'max' : 65},
    'email' : {'type' : 'string', 'required' : True, 'empty' : False, 'regex':'^.+@.+\\..+$'},
    'phone': {'type': 'string', 'required': True, 'empty': False, 'validator': phone_number}
}

# 实例化一个Validator
v = Validator(student_shema)

student_a = {
    'name':'song', 'age':15, 'email':'1209941366@qq.com', 'phone':'1999999999'
}   

if not v.validate(student_a):
    errors = v.document_error_tree
    print(errors)
```
结果：  
```
[],{'age': [ValidationError @ 0x2a1ca065cd0 ( document_path=('age',),
    schema_path=('age', 'min'),code=0x42,constraint=18,value=15,info=() )],{},
    'phone': [ValidationError @ 0x2a1ca00dfd0 ( document_path=('phone',),
    schema_path=(),code=0x0,constraint=None,value="1999999999",info=('错误电话号码',) )],{}}
```









