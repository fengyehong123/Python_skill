# 当使用元素存储格式化数据的时候,为了增强程序的可读性,可以使用namedtuple
import collections

# 使用namedtuple之前
students = [
    # id 姓名 分数
    (1, 'ABC', 90),
    (2, 'XYZ', 85),
    (3, 'JKL', 95)
]

for s in students:
    print('name={}, id={}, score={}'.format(
        # 并不能一眼就看出 s[1], s[0], s[2] 分别代表的是什么含义
        s[1], s[0], s[2]
    ))

# 使用namedtuple
Student = collections.namedtuple('StudentAAA', 'id, name, score')
studentTuple = [
    Student(1, 'ABC', 90),
    Student(2, 'XYZ', 85),
    Student(3, 'JKL', 95)
]
print(studentTuple)
"""
[StudentAAA(id=1, name='ABC', score=90), StudentAAA(id=2, name='XYZ', score=85), StudentAAA(id=3, name='JKL', score=95)]
"""

# 增强了可读性,而且运行速度和基本数组基本一致
for s in studentTuple:
    print('name={}, id={}, score={}'.format(
        # 可以使用元祖下标取值和名称取值相结合的方式
        s[1], s.id, s.score
    ))
"""
name=ABC, id=1, score=90
name=XYZ, id=2, score=85
name=JKL, id=3, score=95
"""