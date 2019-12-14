name = "张三"
age = 27

# 方法一:
print("我的名字叫 %s ,我今年 %d 岁了" % (name, age))  # 我的名字叫 张三 ,我今年 27 岁了

# 方法二:
print("我的名字叫 {} ,我今年 {} 岁了".format(name, age))  # 我的名字叫 张三 ,我今年 27 岁了
print("我的名字叫 {1} ,我今年 {0} 岁了".format(age, name))  # 我的名字叫 张三 ,我今年 27 岁了
print("我的名字叫 {a} ,我今年 {b} 岁了".format(a=name, b=age))  # 我的名字叫 张三 ,我今年 27 岁了

# 方法三:
# python3.6版本之后,在字符串前面加上 f ,{}中可以直接写变量名称
print(f"我的名字叫 {name} ,我今年 {age} 岁了啊")  # 我的名字叫 张三 ,我今年 27 岁了啊


class Test(object):
    nameA = "李四"
    ageA = 56


print(f"我的名字叫 {Test.nameA} ,我今年 {Test.ageA} 岁了啊")  # 我的名字叫 李四 ,我今年 56 岁了啊

