# 默认值为false的数据类型
false_value = [
    False,
    [],
    {},
    '',
    0,
    0.0,
    None
]

for value in false_value:
    # bool()  将结果转换为布尔类型
    # 一般的判断数据类型是true还是false的方法
    # print("{} is {}".format(value, bool(value)))

    # 推荐的判断方法,如果value的值为true就打印True,否则就打印false
    print(True if value else False)

""" 结果
False is False
[] is False
{} is False
 is False
0 is False
0.0 is False
None is False
"""

print("==============")


class MyType(object):

    def __init__(self):
        self.value = []

    def add(self, x):
        self.value.append(x)

    def __bool__(self):
        return bool(self.value)


my_type = MyType()
print(bool(my_type))  # False

my_type.add(1)
print(bool(my_type))  # True

print("==============")

# 一个空列表
a = []

# 一般做法
if a == []:
    print("列表为空")

b = []
# 推荐做法,因为空列表的值 为 false 负负得正来进行判断
if not b:
    print("b is empty")




