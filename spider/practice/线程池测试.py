import requests

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
        except Exception as e:
            print(ip, "No")