d = {
    'zhao': 68,
    'qian': 80,
    'sun': 72,
    'li': 90,
    'zhou': 83,
    'wu': 79,
    'zheng': 62,
    'wang': 87
}

# 字典.items()可以获取出 可迭代对象
print(d.items())
"""
dict_items([('zhao', 68), ('qian', 80), ('sun', 72), ('li', 90), ('zhou', 83), ('wu', 79), ('zheng', 62), ('wang', 87)])
"""

# print(d.items().sort(key=lambda x: x[1]))

# 通过lambda表达式,根据字典的value进行排序,默认是从小到大进行排序,通过 reverse=True 反转,从而从大到小进行排序
obj = sorted(d.items(), key=lambda y: y[1], reverse=True)
print(obj)
"""
[('li', 90), ('wang', 87), ('zhou', 83), ('qian', 80), ('wu', 79), ('sun', 72), ('zhao', 68), ('zheng', 62)]
"""

# 通过dict()函数,把可迭代对象转换为字典,从而实现根据字典的键从大到小进行排列
print(dict(obj))
"""
{'li': 90, 'wang': 87, 'zhou': 83, 'qian': 80, 'wu': 79, 'sun': 72, 'zhao': 68, 'zheng': 62}
"""

# 根据key进行排序
NN = {
    'zhao': 68,
    'qian': 80,
    'sun': 72,
    'li': 90,
    'zhou': 83,
    'wu': 79,
    'zheng': 62,
    'wang': 87
}

print(dict(sorted(NN.items(), key=lambda x: x[0], reverse=False)))
"""
{'li': 90, 'qian': 80, 'sun': 72, 'wang': 87, 'wu': 79, 'zhao': 68, 'zheng': 62, 'zhou': 83}
"""



