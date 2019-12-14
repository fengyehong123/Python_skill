from .custom_exception import NameTooShort


def validated(name):
    if len(name) < 10:
        raise NameTooShort("名字太短了!")


try:
    validated('test')
except NameTooShort as e:
    print(e)
