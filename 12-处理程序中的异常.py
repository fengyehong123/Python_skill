class Check:

    @classmethod
    def check_network(cls):
        return True

    @classmethod
    def check_download_url(cls):
        return True

    @classmethod
    def check_access_allowed(cls):
        return True

    # 假设发生异常
    @classmethod
    def check_dns(cls):
        return False


# 为每一种方法考虑一种异常
class ConnectionError(Exception):
    pass


class DownloadURLError(Exception):
    pass


class PermissionError(Exception):
    pass


class DNSError(Exception):
    pass


def download_file():
    if not Check.check_network():
        raise ConnectionError("Cannot connect to network")
    if not Check.check_download_url():
        raise DownloadURLError("Invalid URL")
    if not Check.check_access_allowed():
        raise PermissionError("Cannot access resource (permission denied)")
    if not Check.check_dns():
        raise DNSError("No DNS")

    return ['c', 'o', 'o', 'l']


if __name__ == '__main__':
    try:
        print(download_file())
    # 捕捉考虑到的异常
    except DNSError:
        print('xxxx DNS error')
    # 捕捉没有考虑到的异常
    except Exception as e:
        print('download error: {}'.format(e))

    # 发生已知异常和未知的异常都可以进行捕捉,从而保证程序的正常运行
    print('xxxxxxx')
