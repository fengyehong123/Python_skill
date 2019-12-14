# 一个类中实现了 __iter__()方法,这个类可以被迭代
class A:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def __iter__(self):
        # return self.data.__iter__()
        for item in self.data:
            yield item


class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 类的实现类
b1 = B(x=1, y=2)
b2 = B(x=3, y=4)

a = A()
# 把B的实现类放入A当中
a.add(b1)
a.add(b2)

# 因为A类中实现了__iter__(),因此可被直接迭代
for item in a:
    print(item.x, item.y)

"""
1 2
3 4
"""





