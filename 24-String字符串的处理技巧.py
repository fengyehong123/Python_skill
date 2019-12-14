s = ' Last Checkpoint: a few seconds ago (unsaved changes)'

# 需求: 去掉两端的空格,大写变小写,把括号替换为 #

# 建议通过一步到位的操作
str = s.strip().lower().replace("(", "#").replace(")", "#")
print(str)  # last checkpoint: a few seconds ago #unsaved changes#


s = ['an', 'hours', 'age']

# 需求,改变为这样的格式 an hours age

# 初始方法
a = ""
for i in s:
    a += i
    a += " "

print(a.strip())  # an hours age

# 通过join的方法,一步到位的操作
print(" ".join(s))  # an hours age
