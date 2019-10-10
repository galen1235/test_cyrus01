

import requests
import json
class RunMain:
    """无构造器"""
    def send_get(self, url, headers):
        res = requests.get(url=url, headers=headers)
        return res

    def send_post(self, url,headers, data):
        res = requests.post(url=url, headers= headers,data=data)
        return res

    def run_main(self, url, method, headers,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, headers)
        else:
            res = self.send_post(url,headers, data)
        return res.text.encode('utf-8').decode('unicode_escape')


if __name__ == '__main__':
    url = 'http://pre.xinyao888.net/api/auth/login'
    headers = {'Content-Type': 'application/vnd.sc-api.v1.json',
               'Origin': 'http://pre.xinyao888.net'}
    data = {"username":"will00","password":"d3ad4cee4afad22711421f651119d0d4","validcode":"","saveUser":False,"grant_type":"password","client_id":"10000002","nonce":"483ded0133ce1b28e1f0b911b0dd89a3"}
    run = RunMain()  # 先实例化，实例化时不需要带参数
    print(run.run_main(url, 'post', headers,data))