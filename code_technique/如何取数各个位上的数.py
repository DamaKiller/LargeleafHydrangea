#以123为例

num = 123
#个位数
low = num % 10 
#十位数
mid = num // 10 % 10
#百位数
high = num // 100
print(low, mid, high)
