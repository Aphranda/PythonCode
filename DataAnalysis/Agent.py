import requests
import random


class MyResponse(object):
    def __init__(self, url):
        self.url = url
        self.ip = []

    def ip_check(self):
        with open('ip.text', mode='r') as f:
            a = list()
            for line in f.readlines():
                clear = line.replace('\n', '')
                a.append(clear)
        for ip in a:
            proxies = {
                "http": "http://" + str(ip),
                "https": "http://" + str(ip),
            }
            print(proxies)
            try:
                res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                print(ip, 'YES')
                self.ip.append(ip)
            except Exception as e:
                print(ip, "No")

    def response(self):
        url = self.url
        random.shuffle(self.ip)
        proxies = {
            "http": "http://" + self.ip[0],
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                          "/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
        html = response.text
        print(html)
        return html


if __name__ == '__main__':
    url = 'https://cxps.szpsq.org.cn/yqfk/view/mobileapp/publicinspect/index.html#/'
    response = MyResponse(url)
    response.ip_check()
    response.response()
