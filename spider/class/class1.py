import requests
import re
import time
url = 'http://www.jianlaixiaoshuo.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0", }
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text
title = re.findall(r'<title>(.*?)</title>', html, re.S)
fb = open('%s.txt' % title, 'w', encoding='utf-8')
#print(html)
#print(title)
dl = re.findall(r'<dt class="title">.*?</dl>', html, re.S)[0]
#print(dl)
chapter_info_list = re.findall(r'<dd><a href="(.*?)" target="_blank">(.*?)</a></dd>', dl)
#print(chapter_info_list)
for chapter_info in chapter_info_list:
    time.sleep(1)
    chapter_url, chapter_title = chapter_info
    chapter_url = "http://www.jianlaixiaoshuo.com%s" % chapter_url
    #print(chapter_url, chapter_title)
    content_response = requests.get(chapter_url, headers=headers)
    content_response.encoding = 'utf-8'
    content_html = content_response.text
    #print(content_html)
    content_word = re.findall(r'<div id="BookText">(.*?)</div>', content_html, re.S)[0]
    content_word = content_word.replace('</p>', '')
    content_word = content_word.replace('<p>', '')
    content_word = content_word.replace('&#8212;', '')
    content_word = content_word.replace("&#8211;", '')
    fb.write(chapter_title)
    fb.write(content_word)
    fb.write('\n')
    print(chapter_url)
