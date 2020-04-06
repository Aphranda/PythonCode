import requests
import threading
import random


class MyThread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        """西刺代理爬取主体函数"""
        with open(r'spider\practice\ip.text') as f:
            a = list()
            b = 0
            for line in f.readlines():
                clear = line.replace('\n', '')
                a.append(clear)
        while True:
            url = r'https://csydtg.980cje.com/s/11/3148/28eab.html?uid=9126000000879'
            random.shuffle(a)
            proxies = {
                "http": "http://" + a[0],
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                "/78.0.3904.108 Safari/537.36",
            }
            try:
                response = requests.get(url, proxies=proxies, headers=headers)
                data = response.content.decode()
                b += 1
                print(b, a[0], type(data))
            except Exception as e:
                print('None')
                pass


if __name__ == '__main__':
    my_thread = MyThread
    thread1 = my_thread(1, "Thread-1")  # page: 起始页20，终止页39
    thread2 = my_thread(2, "Thread-2")
    thread3 = my_thread(3, "Thread-3")
    thread4 = my_thread(4, "Thread-4")
    thread5 = my_thread(5, "Thread-5")
    thread6 = my_thread(6, "Thread-6")
    thread7 = my_thread(7, "Thread-7")
    thread8 = my_thread(8, "Thread-8")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
