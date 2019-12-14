g = lambda x: x + 1

a = g(1)
print(a)  # 2

b = g(2)
print(b)  # 3

# 当一个函数作为参数传入的时候,可以考虑用lambda表达式来代替函数
data = list(range(20))


def find(filter_func):
    res = []
    for item in data:
        if filter_func(item):
            res.append(item)

    # 返回列表
    return res


def filter_func_1(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(find(filter_func=filter_func_1))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ################################使用lambda表达式#########################################

# 使用lambada表达式来替代当做参数传入的函数
print(find(lambda x: True if x % 2 == 0 else False))


data1 = ['No', 'such', 'file', 'or', 'directory', 'A', 'C']
data1.sort()
# 先按照大小写排序,然后按照字母排序
print(data1)  # ['A', 'C', 'No', 'directory', 'file', 'or', 'such']

data1 = ['No', 'such', 'file', 'or', 'directory', 'A', 'C']
# 通过lambda表达式来改变默认的排序,将所有的元素转换为小写
data1.sort(key=lambda x: x.lower())
print(data1)  # ['A', 'C', 'directory', 'file', 'No', 'or', 'such']
