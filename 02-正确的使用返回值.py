def test_connection():
    return True


def get():
    return ['user1', 'user2']  # 如果列表为空的情况下,直接打印空列表会打印false


def get_user_list():
    if not test_connection():
        return None
    else:
        # 如果能连接上的话,就去获取用户的列表
        return get()


user_list = get_user_list()
# if not user_list:  # 如果是这样的话,数据库连接成功,但是获取到的用户列表不为none,为空列表[]的情况下,也会判定为false
if user_list is None:  # 只有用户列表为none的情况才能说明连接出现错误
    print("connection error")
else:
    print("user list: ", user_list)

