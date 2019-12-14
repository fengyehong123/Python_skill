for _ in range(5):
    print('hello world')

# 我们值关系打印的结果,不关系打印的次数的时候
"""
hello world
hello world
hello world
hello world
hello world
"""

# 列表解析的时候使用
a = ['A', 1, 'abc']
x, _, z = a
print(x)  # A
print(_)  # 1
print(z)  # abc
