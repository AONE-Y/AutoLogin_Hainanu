import requests
import time


class AutoLogin(object):
    def __init__(self, url, data):
        self.judge_url = "http://www.baidu.com"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
        }
        self.url = url
        self.data = data

    # 判断是否登录，能否上网
    def judge(self):
        try:
            judge_status = requests.get(url=self.judge_url, headers=self.header, stream=True)
            status = judge_status.raw._connection.sock.getpeername()[0]
            return True
        except Exception:
            print("\033[1;31;40m\t网络断开，正在尝试重新认证！！！\033[0m")
            return False

    # 登录校园网
    def login(self):
        requests.post(url=self.url, headers=self.header, data=self.data)


if __name__ == '__main__':
    url = "http://xywrz.hainanu.edu.cn/eportal/InterFace.do?method=login"
    data = {
        'userId': '123456789',
        'password': '123456789',
        'service': 'default',
        'queryString': '123456789',
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': '',
        'passwordEncrypt': 'true',
    }
    auto_login = AutoLogin(url=url, data=data)
    try:
        while (True):
            i = auto_login.judge()
            if not i:
                auto_login.login()
            time.sleep(60)

    except:
        print("\033[1;31;40m\t校园网认证失败，无法连接到校园网认证服务器，休眠3分钟后再尝试进行认证")
        print("\033[1;31;40m\t可能的原因：" )
        print("        \033[1;31;40m\t1.网线未连接好")
        print("        \033[1;31;40m\t2.校园网服务器出现故障")
        time.sleep(180)
