import requests
import re

url = 'http://www.aixiashu.com/2/2397/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # 译码
html = response.text  # 找到A标签
title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html, re.S)[0]
#print(title)
#print(html)
dl = re.findall(r'<div id="list">.*?</dl> ', html, re.S)  # 获取每一张的信息（章节，UR）re.S .可以匹配非可见字符
chapter_info_list = re.findall(R'<dd><a href="(.*?)">(.*?)<', html, re.S)
#print(chapter_info_list)
#set a new file
fb = open('%s.txt' % title, 'w', encoding='utf-8')
#循环列表，提取每一张信息，然后下载章节。
for chapter_info in chapter_info_list:
    #chapter_title = chapter_info[1]
    #chapter_url = chapter_info[0]
    chapter_url, chapter_title = chapter_info
    chapter_url = "http://www.aixiashu.com%s" %chapter_url
    #print(chapter_info)
    #print(chapter_url, chapter_title)
    chapter_response = requests.get(chapter_url, headers=headers)
    chapter_response.encoding = 'utf-8'
    #print(chapter_response)
    chapter_html = chapter_response.text   #下载章节内容
    chapter_content = re.findall(r'<div id="content">(.*?)</div>', chapter_html, re.S)[0]
    chapter_content = chapter_content.replace(' ', '')
    chapter_content = chapter_content.replace('&nbsp;', '')#数据整理
    chapter_content = chapter_content.replace('<br/>', '')
    #数据持久
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)



