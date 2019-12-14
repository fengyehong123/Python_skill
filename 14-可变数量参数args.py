# 原始的方法,只能计算两个参数的值
def sum1(x, y):
    return x + y


print(sum1(1, 2))  # 3


# 可变参数的方式
def sum2(x, *args):
    return x + sum(args)


print(sum2(1, 2, 3, 4, 5))  # 15



