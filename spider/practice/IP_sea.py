import requests
import re
import threading
import random


with open('ip.text') as f:
    a = list()
    for line in f.readlines():
        clear = line.replace('\n', '')
        a.append(clear)
        # print(a)
print(a)
# for single in a:
#     print(single)
#     proxies = {
#         "http": "http://" + single[0],
#         "https": "http://" + single[0],
#     }
#     try:
#         test = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
#         pass
#     except Exception as e:
#         a.remove(single)


def obtain_one():
    for i in range(900, 1000):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
            # "https": "http://" + a[1],
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
        html = response.text
        # print(html)
        IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
        ports = re.findall(r'<td>(\d+)</td>', html, re.S)
        # print(IPs)
        # print(ports)
        for ip in zip(IPs, ports):
            # print(ip)
            proxies = {
                "http": "http://" + ip[0] + ':' + ip[1],
                "https": "http://" + ip[0] + ':' + ip[1],
            }
            try:
                res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                print(ip, 'YES')
                with open('ip.text', mode='a+') as f:
                    f.write(":".join(ip) + "\n")
            except Exception as e:
                print(ip, "No")


def obtain_two():
    for i in range(800, 900):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
            # "https": "http://" + a[1],
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
        html = response.text
        # print(html)
        IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
        ports = re.findall(r'<td>(\d+)</td>', html, re.S)
        # print(IPs)
        # print(ports)
        for ip in zip(IPs, ports):
            # print(ip)
            proxies = {
                "http": "http://" + ip[0] + ':' + ip[1],
                "https": "http://" + ip[0] + ':' + ip[1],
            }
            try:
                res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                print(ip, 'YES')
                with open('ip.text', mode='a+') as f:
                    f.write(":".join(ip) + "\n")
            except Exception as e:
                print(ip, "No")


def obtain_three():
    for i in range(200, 300):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
            # "https": "http://" + a[1],
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
        html = response.text
        # print(html)
        IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
        ports = re.findall(r'<td>(\d+)</td>', html, re.S)
        # print(IPs)
        # print(ports)
        for ip in zip(IPs, ports):
            # print(ip)
            proxies = {
                "http": "http://" + ip[0] + ':' + ip[1],
                "https": "http://" + ip[0] + ':' + ip[1],
            }
            try:
                res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                print(ip, 'YES')
                with open('ip.text', mode='a+') as f:
                    f.write(":".join(ip) + "\n")
            except Exception as e:
                print(ip, "No")

def obtain_four():
    for i in range(300, 400):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
            # "https": "http://" + a[1],
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=3)
        html = response.text
        # print(html)
        IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
        ports = re.findall(r'<td>(\d+)</td>', html, re.S)
        # print(IPs)
        # print(ports)
        for ip in zip(IPs, ports):
            # print(ip)
            proxies = {
                "http": "http://" + ip[0] + ':' + ip[1],
                "https": "http://" + ip[0] + ':' + ip[1],
            }
            try:
                res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
                print(ip, 'YES')
                with open('ip.text', mode='a+') as f:
                    f.write(":".join(ip) + "\n")
            except Exception as e:
                print(ip, "No")

if __name__ == '__main__':
    t = threading.Thread(target=obtain_one)
    s = threading.Thread(target=obtain_two)
    k = threading.Thread(target=obtain_three)
    b = threading.Thread(target=obtain_four)
    t.start()
    s.start()
    k.start()
    b.start()

