import os, sys
# #注意就是下面的 if 语句
# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

# # import others
import requests
from parsel import Selector
from random import randint
from MyQR import myqr


class Beauty(object):
    def __init__(self):
        self.html = []

    def get_html(self):
        for i in range(0, 5):
            page = randint(1, 10000)
            url = 'http://www.nenmp.com/' + '1' + '/' + str(page) + '.html'
            response = requests.get(url)
            response.encoding = 'utf-8'
            all_html = response.text
            self.html.append(all_html)

    def download(self):
        path = r'C:\Users\Administrator\Desktop\beauty'
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)
        else:
            os.chdir(path)
        sel = Selector(self.html[randint(0, 5)])
        img_s = sel.css('body > div:nth-child(2) > div > div.col-md-9 > div > img')
        a = 1
        for img in img_s:
            url = img.css('img::attr(src)').extract_first()
            name = img.css('img::attr(alt)').extract_first()
            # print(url, name)
            myqr.run(words=url, version=2, save_name='beauty{}.jpg'.format(a), save_dir=r'C:\Users\Administrator\Desktop\beauty')
            a = a + 1
            print(a)

if __name__ == '__main__':
    dog = Beauty()
    dog.get_html()
    dog.download()
