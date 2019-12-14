# 不建议默认的参数是一个list
# 当默认的参数的数据类型是一个list的时候,不过不指定list,会默认使用上一次的list,造成数据污染


def bad_default_arg(s, times, target=[]):
    # 当遍历出来的数据不使用的时候,用 _ 来代替
    for _ in range(times):
        target.append(s)
    return target


# 第一次的函数调用
print(bad_default_arg(s='第一次调用的数据', times=3))  # ['第一次调用的数据', '第一次调用的数据', '第一次调用的数据']

# 再调用一次,因为本次的调用指定了列表的默认参数,因此没有被污染
print(bad_default_arg(s='b', times=3, target=['a']))  # ['a', 'b', 'b', 'b']

# 再调用一次,不指定列表的默认参数,数据被污染,在第一次调用产生数据的基础上进行数据添加
print(bad_default_arg(s='AB', times=2))  # ['第一次调用的数据', '第一次调用的数据', '第一次调用的数据', 'AB', 'AB']


# ############################默认参数是列表的解决方案#################################################
def good_default_arg(s, times, target=None):
    # 首先判断target参数是否为None
    if target is None:
        target = []

    for _ in range(times):
        target.append(s)

    return target


# 函数的第一次调用
print(good_default_arg(s='a', times=3))  # ['a', 'a', 'a']
# 函数的第二次调用
print(good_default_arg(s='B', times=3))  # ['B', 'B', 'B']
# 函数的第三次调用,添加上列表的默认参数,数据并没有被污染
print(good_default_arg(s='a', times=3, target=['FF']))  # ['FF', 'a', 'a', 'a']
