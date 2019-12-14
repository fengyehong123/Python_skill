class Network:
    def is_url_valid(self):
        return True
    def is_dns_work(self):
        return True
    def is_user_valid(self):
        return


# 优化之前的代码,层次太多,阅读起来很困难
def download_nested():
    # 如果网络地址合法的话
    if Network.is_url_valid():
        # 如果dns工作的话
        if Network.is_dns_work():
            # 如果用户合法的话
            if Network.is_user_valid():
                print('start downloading.....')
            else:
                print('user invalid')
        else:
            print('dns error')
    else:
        print('url invalid')


# 优化之后的代码,代码扁平化,更加容易阅读
def download_flat():
    if not Network.is_url_valid():
        print('url invalid')
        return
    elif not Network.is_dns_work():
        print('dns error')
        return
    elif not Network.is_user_valid():
        print('user invalid')
        return

    # 当前面的几步都通过校验之后,下载才会开始
    print('start downloading.....')
