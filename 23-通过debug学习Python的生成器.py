"""
# 原始的斐波那契额数列
def fib(n):
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)
    return numbers
print(fib(10))
"""


# 需求,找出第一个超过1000的数字
def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        # 函数中添加了yield,这个函数就变成了生成器
        yield current


for item in fib():
    print(item, end=",")
    """
    1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,
    """
    if item > 1000:
        break

