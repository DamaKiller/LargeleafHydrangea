x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}  # 若key相同，则y覆盖x
# 该语法只在python3.5之后的版本中可用
z = {**x, **y}
print(z)
