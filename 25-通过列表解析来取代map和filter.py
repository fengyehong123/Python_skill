the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_odd(number):
    return number % 2 == 1


# 参数一: 判断的函数 参数二: 源数据 filter() 函数用来起到过滤的作用
odd_numbers = filter(is_odd, the_list)
# 得到一个可迭代对象
print(odd_numbers)  # <filter object at 0x0000024F12A800B8>
for i in odd_numbers:
    print(i, end=" ")  # 1 3 5 7 9

# 可以通过lambda表达式来代替函数
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: True if x % 2 == 1 else False, the_list)))  # [1, 3, 5, 7, 9]

# 可以通过列表解析式来代替filter()函数
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = [i for i in the_list if i % 2 == 1]
print(m)  # [1, 3, 5, 7, 9]

# map()函数,用来对可迭代对象中的每一个数据进行操作
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map(lambda x: x * 2, the_list))  # <map object at 0x0000015DFC939080>

for i in map(lambda x: x * 2, the_list):
    print(i, end=" ")  # 2 4 6 8 10 12 14 16 18 20

# 通过列表解析式来代替map()函数
print([i * 2 for i in the_list])  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
