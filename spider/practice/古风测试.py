import requests
import parsel
import random
import re
import time

#
# with open('ip.text') as f:
#     a = list()
#     for line in f.readlines():
#         clear = line.replace('\n', '')
#         a.append(clear)
#
#
# def next_page():
#     url = 'https://m.gufengmh8.com/manhua/woshizhizhuyouzenyang/1211110.html'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
#     }
#     random.shuffle(a)
#     proxies = {
#         "http": "http://" + a[1],
#     }
#     response = requests.get(url, headers=headers)
#     pen = response.content.decode('utf-8')
#     data = parsel.Selector(pen)
#     items = data.xpath(r'//div[@class="chapter-content"]//div/a').extract()
#     time.sleep(1)
#     next_html = re.findall(r'href="(.*?)"><img', str(items), re.S)
#     picture_urls = re.findall(r'src="(.*?)" width', str(items), re.S)
#     next_url = 'https://m.gufengmh8.com/' + str(next_html).replace("['", "").replace("']", "")
#     picture_url = str(picture_urls).replace("['", "").replace("']", "")
#     print(next_url, picture_url)
#
#
# if __name__ == '__main__':
#     next_page()

with open('ip.text') as f:
    a = list()
    b = list()
    for line in f.readlines():
        clear = line.replace('\n', '')
        king = {
            "http": "http://" + str(clear),
        }
        print(king)

        try:
            res = requests.get("http://www.baidu.com", proxies=king, timeout=3)
            a.append(clear)
        except Exception as e:
            b.append(clear)
        print(a)
        print(b)
        """
        http://119.101.112.208:9999
        http://223.199.29.6:9999
        http://119.101.114.12:9999
        http://111.177.178.63:9999
        """