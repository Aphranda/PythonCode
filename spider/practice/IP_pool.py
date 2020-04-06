import requests
import re
import threading


def obtain_one():
    for i in range(300, 400):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, headers=headers)
        html = response.text
        IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
        ports = re.findall(r'<td>(\d+)</td>', html, re.S)
        for ip in zip(IPs, ports):
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
    for i in range(70, 100):
        url = 'https://www.xicidaili.com/nn/{}/'.format(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        response = requests.get(url, headers=headers)
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
                print(ip, 'YES')
                with open('ip.text', mode='a+') as f:
                    f.write(":".join(ip) + "\n")
            except Exception as e:
                print(ip, "No")


if __name__ == '__main__':
    t = threading.Thread(target=obtain_one)
    s = threading.Thread(target=obtain_two)
    t.start()
    s.start()