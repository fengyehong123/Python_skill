# 通过列表解析来提高运行的速度

# 找到所有的偶数放到一个List里   [2, 4, 6]
# 方法一:原始的方式
a = [1,2,3,4,5,6,7]
b = []
for item in a:
    if item % 2 == 0:
        b.append(item)
print(b)

# 方法二: 列表解析的方式
c = [item for item in a if item % 2 == 0]
print(c)

# 列表解析的方式更快
a = list(range(50000))
import time
start = time.time()
b = []
for item in a:
    if item%2==0:
        b.append(item)
print(time.time() - start)  # 0.005009174346923828

a = list(range(50000))
start = time.time()
b = [item for item in a if item%2==0]
print(time.time() - start)  # 0.001994609832763672
