def sum2(x, **kwargs):
    print(x, kwargs)


# 传入多个参数
sum2(x=1, a=2,b=3,c=4)  # 1 {'a': 2, 'b': 3, 'c': 4}


def sum3(x, y):
    return x + y


# 字典的解析式,把字典解析为位置参数
print(sum3(**{'x': 1, 'y': 2}))  # 3
