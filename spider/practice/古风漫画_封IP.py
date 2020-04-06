import requests
import parsel
import random
import re
import time
import os

if not os.path.exists('F:\Comic'):
    os.makedirs('F:\Comic')
else:
    pass

with open('ip.text') as f:
    a = list()
    for line in f.readlines():
        clear = line.replace('\n', '')
        a.append(clear)


class OldWind:
    def __init__(self, name):
        self.name = name
        self.label = []
        self.page = []
        self.boxes = None
        self.next_url = None

    def box_dict(self):
        url = r'https://m.gufengmh8.com/search/?keywords={}'.format(self.name)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
        }
        print(proxies)
        response = requests.get(url, headers=headers, proxies=proxies)
        html = response.content.decode('utf-8')
        data = parsel.Selector(html)
        items = data.xpath(r'//div[@class="UpdateList"]//div[contains(@class,"t")]//div[@class="itemImg"]//a[@href]').extract()
        # print(items)
        for item in items:
            names = re.findall(r'alt="(.*?)" width', str(item), re.S)
            labels = re.findall(r'href="(.*?)" target', str(item), re.S)
            box = [str(names).replace(r"['", "").replace(r"']", ""), str(labels).replace(r"['", "").replace(r"']", "")]
            self.label.append(box)
        self.boxes = dict(self.label)

    def page_path(self):
        names = list(self.boxes.keys())
        url = self.boxes[names[0]]
        print(names[0], url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }
        random.shuffle(a)
        proxies = {
            "http": "http://" + a[1],
        }
        print(proxies)
        response = requests.get(url, headers=headers, proxies=proxies)
        html = response.content.decode('utf-8')
        data = parsel.Selector(html)
        if data.xpath(r'//div[@class="section4 active"]/div[2]//h3').extract():
            items = data.xpath(
                r'//div[@class="section4 active"]/div[2]/div[@class="list"]//li/a[contains(@href,"t")]').extract()
        else:
            items = data.xpath(
                r'//div[@class="section4 active"]/div[1]/div[@class="list"]//li/a[contains(@href,"t")]').extract()
        for item in items:
            names = re.findall(r'"active">(.*?)</a>', str(item), re.S)
            labels = re.findall(r'href="(.*?)" class', str(item), re.S)
            box = [str(names).replace(r"['\n\t\t\t\t\t\t\t\t\t\t<span>", "").replace(r"</span>\n\t\t\t\t\t\t\t\t\t']", ""), str(labels).replace(r"['", "").replace(r"']", "")]
            self.page.append(box)
        print(self.page)

    def next_page(self):
        os.chdir('E:\Comic')
        htmls = []
        num = len(self.page)
        for i in range(int(num)-1):
            html = str('https://m.gufengmh8.com/' + str(self.page[i][1]))
            htmls.append(html)
        print(htmls)
        for urls in htmls[2:]:  # 调整下载章节
            self.next_url = urls
            path = str(self.next_url.split('.')[2].split(r'/')[-1])
            if not os.path.exists(r'F:\Comic\{}'.format(path)):
                os.makedirs(r'F:\Comic\{}'.format(path))
                os.chdir(r'F:\Comic\{}'.format(path))
            else:
                os.chdir(r'F:\Comic\{}'.format(path))
            while requests.get(self.next_url):
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                }
                random.shuffle(a)
                proxies = {
                    "http": "http://" + a[1],
                }
                print(proxies)
                response = requests.get(self.next_url, headers=headers, proxies=proxies)
                pen = response.content.decode('utf-8')
                data = parsel.Selector(pen)
                items = data.xpath(r'//div[@class="chapter-content"]//div/a').extract()
                time.sleep(1)
                next_html = re.findall(r'href="(.*?)"><img', str(items), re.S)
                picture_urls = re.findall(r'src="(.*?)" width', str(items), re.S)
                self.next_url = 'https://m.gufengmh8.com/' + str(next_html).replace("['", "").replace("']", "")
                picture_url = str(picture_urls).replace("['", "").replace("']", "")
                print(self.next_url, picture_url)
                image = requests.get(picture_url)
                with open(str(picture_url).split('.')[2].split(r'/')[-1] + '.jpg', mode='wb') as file:
                    file.write(image.content)


if __name__ == '__main__':
    name = '蜘蛛侠'
    cartoon = OldWind(name)
    cartoon.box_dict()
    cartoon.page_path()
    cartoon.next_page()