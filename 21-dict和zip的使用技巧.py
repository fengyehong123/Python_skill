# 基本的方式创建字典
a = {'a': 1, 'b': 2}
print(a)  # {'a': 1, 'b': 2}

# 通过dict()创建一个字典
b = dict()
print(b)  # {}

c1 = dict(ab=1, cd=2)
print(c1)  # {'ab': 1, 'cd': 2}

# 只需要向dict()中传入可迭代对象,就可以生成字典
# 可迭代对象
x = (['A', 1], ('B', 2))
c2 = dict(x)
print(c2)  # {'A': 1, 'B': 2}


# zip()函数的用法
# 可迭代对象x和y的数据一一对应
x = (1, 2, 3, 4)
y = ['a', 'b', 'c', 'd']
print(zip(x, y))  # <zip object at 0x0000022FA3915248>
for i in zip(y, x):
    print(i)
# 产生可迭代的元祖
"""
('a', 1)
('b', 2)
('c', 3)
('d', 4)
"""

print(dict(zip(x, y)))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
