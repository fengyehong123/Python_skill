# 定义自定义的异常


# 定义异常的基类
class MyException(Exception):
    pass


# 具体的异常继承异常的基类
class NameTooShort(MyException):
    pass


class NameTooLong(MyException):
    pass


class NameNotFound(MyException):
    pass
