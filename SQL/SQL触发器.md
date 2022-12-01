# 触发器
***  
- 触发器是与表有关的数据库对象
- 可以在insert，update，delete之前或之后触发并执行触发器中定义的SQL语句
- 这种特性可以协助应用系统在数据库端确保数据的完整性，日志记录，数据校验等操作
- 通过使用别名NEW和OLD来引用触发器中发生变化的内容记录


### 触发器分类
#### insert型触发器
***  
- OLD:无(因为插入前无数据)
- NEW:NEW表示将要或者已经新增的数据


#### update型触发器
***  
- OLD:OLD表示修改之前的数据
- NEW:NEW表示将要或者已经修改后的数据


#### delete型触发器
***  
- OLD:OLD表示将要或者已经删除的数据
- NEW:无(因为删除后状态无数据)


### 创建触发器
***  
delimiter $
create trigger 触发器名称
before|after insert|update|delete
on 表名
for each row
begin
触发器要执行的功能;
end$
delimiter ;


### 查看和删除触发器
#### 查看触发器
***  
`show triggers;`


#### 删除触发器
***  
`drop trigger 触发器名称;`









