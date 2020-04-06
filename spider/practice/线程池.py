import requests
import re
import threading
import random


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, page):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.page = page

    def run(self):
        """西刺代理爬取主体函数"""
        with open('ip.text') as f:
            a = list()
            for line in f.readlines():
                clear = line.replace('\n', '')
                a.append(clear)
        for i in range(self.page, self.page + 19):
            url = 'https://www.xicidaili.com/nn/{}/'.format(i)
            random.shuffle(a)
            proxies = {
                "http": "http://" + a[0],
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                              "/78.0.3904.108 Safari/537.36",
            }
            response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
            html = response.text
            IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
            ports = re.findall(r'<td>(\d+)</td>', html, re.S)

            for ip in zip(IPs, ports):
                # print(ip)
                proxies = {
                    "http": "http://" + ip[0] + ':' + ip[1],
                    "https": "http://" + ip[0] + ':' + ip[1],
                }
                try:
                    res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                    print(ip, 'YES', self.name)
                    with open('ip.text', mode='a+') as f:
                        f.write(":".join(ip) + "\n")
                except Exception as e:
                    print(ip, "No", self.name)


if __name__ == '__main__':
    my_thread = MyThread
    thread1 = my_thread(1, "Thread-1", 120)  # page: 起始页20，终止页39
    thread2 = my_thread(2, "Thread-2", 140)
    thread3 = my_thread(3, "Thread-3", 160)
    thread4 = my_thread(4, "Thread-4", 180)
    thread5 = my_thread(5, "Thread-5", 200)
    thread6 = my_thread(6, "Thread-6", 220)
    thread7 = my_thread(7, "Thread-7", 240)
    thread8 = my_thread(8, "Thread-8", 260)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()