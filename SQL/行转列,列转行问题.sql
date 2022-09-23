# 行转列
# 例子

输入：  
Products table:  
+------------+--------+--------+--------+  
| product_id | store1 | store2 | store3 |  
+------------+--------+--------+--------+  
| 0          | 95     | 100    | 105    |  
| 1          | 70     | null   | 80     |  
+------------+--------+--------+--------+  
输出：  
+------------+--------+-------+  
| product_id | store  | price |  
+------------+--------+-------+  
| 0          | store1 | 95    |  
| 0          | store2 | 100   |  
| 0          | store3 | 105   |  
| 1          | store1 | 70    |  
| 1          | store3 | 80    |  
+------------+--------+-------+  
# 解释：产品0在store1，store2,store3的价格分别为95,100,105。产品1在store1，store3的价格分别为70,80。在store2无法买到。   

select
    product_id,
    'store1' store,   #在该列填入store1字符串
    store1 price
from
    Products
where
    store1 is not null
union   #先一列一列处理然后将他们的结果合并
select
    product_id,
    'store2' store,
    store2 price
from
    Products
where
    store2 is not null
union
select
    product_id,
    'store3' store,
    store3 price
from
    Products
where
    store3 is not null




# 列转行
输入：  
Products：
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store2 | null  |
| 1          | store3 | 80    |
+------------+--------+-------+
输出： 
+------------+--------+--------+--------+  
| product_id | store1 | store2 | store3 |  
+------------+--------+--------+--------+  
| 0          | 95     | 100    | 105    |  
| 1          | 70     | null   | 80     |  
+------------+--------+--------+--------+  

SELECT 
    product_id,
    SUM(IF(store = 'store1', price, NULL))  store1,
    SUM(IF(store = 'store2', price, NULL))  store2,
    SUM(IF(store = 'store3', price, NULL))  store3 
FROM
    Products
GROUP BY 
    product_id ;

#在查询语句中使用了group by，select后面只能出现聚合函数、常量或者group by分组字段。所以在此要加上sum()函数,没有别的用处，只是用作查询。  

