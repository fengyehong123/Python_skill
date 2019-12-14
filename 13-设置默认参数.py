class Hi:
    # 设置一个默认的参数值,当未传入这个参数的时候,使用默认值
    def say(self, name, greetings='hello'):
        print('Hi {}, {}'.format(name, greetings))


hi = Hi()
# 部分参数未传入,使用默认值
hi.say(name='Python')  # Hi Python, hello

# 参数指定了数值,使用指定的
hi.say(name='test', greetings='hi hi hi')  # Hi test, hi hi hi


