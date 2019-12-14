# 元祖的创建

# 创建方法一:
a = (1, 2, 3, 'Python', 5, 6)
print(a)  # (1, 2, 3, 'Python', 5, 6)

# 创建方法二:
b = 1, '你好', [1, 2, 3]
print(b)  # (1, '你好', [1, 2, 3])

# 注意点
c = 1,  # 因为添加了一个逗号,所以不是赋值了一个数字给变量,而是创建了一个元素为一个的元素赋值给变量
print(c)  # (1,)

# 元祖的解析
A = (1, 2, 3)
a, b, c = A
print(a)  # 1
print(b)  # 2
print(c)  # 3

# 如果元祖中有三个元素,但是只想解析两个元素的话,只需要添加一个下划线就可以了,下划线代表解析出的元素不使用
d, e, _ = A
print(d)
print(e)
print(_)  # 3


a = [1, 2, 3, 4]
# 可以获取出下标和下标所对应的元素
for index, value in enumerate(a):
    print(index, value)
"""
0 1
1 2
2 3
3 4
"""

for item in enumerate(a):
    print(item)
"""
(0, 1)
(1, 2)
(2, 3)
(3, 4)
"""

# Python中的数据交换
x = 1
y = 2
#  Python中的数据交换, x, y = y, x   ===> y, x 相当于创建了一个元祖,然后元祖被x 和 y 进行了解析,从而完成了数据的交换
x, y = y, x
