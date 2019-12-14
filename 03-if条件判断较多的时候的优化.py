import random
from enum import Enum


# 定义一个常量类
class Condition(Enum):
    A = 1
    B = 2
    C = 3
    D = 4


values = [1, 2, 3, 4]
choice = Condition(random.choice(values))

"""if choice == Condition.A or choice == Condition.B or choice == Condition.C:
    print('go to step one')
else:
    print('go to step two')
"""
# 先判断少的情况,然后判断多的情况
if choice == Condition.D:
    print("go to step two")
else:
    print("go to step one")

print("==================")
values = [1, 2, 3, 4]
choice = Condition(random.choice(values))

# 优化之前
if choice == Condition.A or choice == Condition.B:
    print('go to step one')
else:
    print('go to step two')

# 第一种优化,把可能的情况放在列表中,判断情况是否在列表中,这种速度最快
options = [Condition.A, Condition.B]
if choice in options:
    print('go to step one')
else:
    print('go to step two')

# 第二种优化,把可能的情况放在集合中,这种方式的速度高于直接判断,低于放在列表中
options = {Condition.A, Condition.B}
if choice in options:
    print('go to step one')
else:
    print('go to step two')

print("#"*20) # ------------------------------------------------------------------------------
# 直接判断
import time
choice = Condition.C
start_time = time.time()
for i in range(0, 1000000):
    if choice == Condition.A or choice == Condition.B or choice == Condition.C:
        pass
    else:
        pass
end_time = time.time()
print(end_time - start_time)  # 0.4547841548919678

# 放到列表中
choice = Condition.C
start_time = time.time()
options = [Condition.A, Condition.B, Condition.C]
for i in range(0, 1000000):
    if choice in options:
        pass
    else:
        pass
end_time = time.time()
print(end_time - start_time)  # 0.09374809265136719

# 放到集合中
import time
choice = Condition.C
start_time = time.time()
options = {Condition.A, Condition.B, Condition.C}
for i in range(0, 1000000):
    if choice in options:
        pass
    else:
        pass
end_time = time.time()
print(end_time - start_time)  # 0.26628756523132324
