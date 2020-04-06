import requests
import re

# 爬取IP
# 替换IP去请求
# 拿到数据 <td>36.25.40.89</td> <td>9999</td>
for i in range(1, 100):
    url = 'https://www.xicidaili.com/nn/{}/'.format(i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    IPs = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html, re.S)
    ports = re.findall(r'<td>(\d+)</td>', html, re.S )
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
                f.write(":".join(ip))
        except Exception as e:
            print(ip, "No")
