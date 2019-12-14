# Java中一般这样添加属性
class A:
    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return "my name is {}, I'm {} years old".format(self.name, self.age)


a = A()
# 如果不初始化name属性的话,会报错
a.set_name('Python')
a.set_age(27)
print(a)  # my name is Python, I'm 27 years old

# Python中初始化属性的正确姿势
class A1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "my name is {}, I'm {} years old".format(self.name, self.age)


a = A1(name='Python', age=27)
print(a)  # my name is Python, I'm 27 years old


# 定义类属性,类属性通过类名和对象名都能直接访问

class A2:
    name = 'Python'
    age = 27

    def __str__(self):
        return "my name is {}, I'm {} years old".format(self.name, self.age)

# 通过类名称直接访问类属性
print(A2.name)  # Python
print(A2.age)  # 27

# 通过对象名称直接访问类属性
obj = A2()
print(obj.name)  # Python
print(obj.age)  # 27
