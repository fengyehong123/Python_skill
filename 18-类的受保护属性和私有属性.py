class A:

    def __init__(self, name, age):
        self.__name = name
        # 两个下划线起到保护的作用,不能直接通过类名/对象名.__age = ? 的方法进行修改
        self.__age = age
        # 一个下划线并不能起到保护的作用,只能提示开发者,这个属性不能修改
        self._protect_var = 1

    # 可以通过添加方法的方式,在类之外通过方法简介的访问
    # Python中不推荐使用这种java思想的做法,Python中使用装饰器@property来完成getter和setter的操作
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # 通过property来获取属性
    @property
    def name(self):
        return self.__name

    # 通过 @name.setter 来设置属性
    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return "My name is {}, I'm {} years old, protect value={}".format(
            self.__name,
            # 在类的内部可以直接通过 .__age的方式访问
            self.__age,
            self._protect_var
        )


a = A(name='Python', age=27)
print(a)  # My name is Python, I'm 27 years old, protect value=1

# a.__age  AttributeError: 'A' object has no attribute '__age'
# A.__age AttributeError: type object 'A' has no attribute '__age'

# __age属性在类之外的地方使用时,名称已经变更为  _类名称__属性名称  的格式
a._A__age = 30
print(a)  # My name is Python, I'm 30 years old, protect value=1

print(a.get_age())  # 30
a.set_age(100)
print(a.get_age())  # 100

# 通过@property来设置和获取的属性
a.name = 10000000
print(a.name)  # 10000000

