import requests
import parsel
import os
dir_name = 'images'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    # 切换工作目录
    os.chdir(dir_name)
else:
    os.chdir(dir_name)

def download_image(url_picture, name_picture):
    suffix = url_picture.split('.')[-1]
    picture = requests.get(url_picture)
    try:
        # 获取后缀名
         with open(name_picture + '.' + suffix, mode='wb') as f:
             f.write(picture.content)
             # 指定路径
    except OSError as e:
         print(e)

for page in range(1, 10):
    url = 'https://www.fabiaoqing.com/biaoqing/lists/page/' + str(page) + '.html'
    # headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    sel = parsel.Selector(html)  # css选择器前端 css选择器是写html的
    # 冒号：伪类选择器 ：：属性选择器 . 类选择器
    # print(sel.css('img.ui.image.lazy::attr(data-original)').extract()) #手写输入
    # 建立循环目录
    # 二次提取
    img_s = sel.css('#bqb > div.ui.segment.imghover > div > a > img')  # 粘贴复制输入
    for img in img_s:
        # 提取URL属性
        url_picture = img.css('img::attr(data-original)').extract_first()
        # 提取name属性
        name_picture = img.css('img::attr(title)').extract_first()
        print(name_picture)
        download_image(url_picture, name_picture)