import requests
import re
import os

# url = 'https://video.pearvideo.com/mp4/adshort/20191212/cont-1631515-11841227-114109_adpkg-ad_hd.mp4'
# response = requests.get(html)
# with open('name', mode='wb') as f:
#     f.write(response.content)
url = 'https://www.pearvideo.com/category_8'
response = requests.get(url)
response = response.text
url_list = re.findall('video_\d+', response, re.S)
# print(url_list)
for url in url_list:
    html = 'https://www.pearvideo.com/%s' % url
    response = requests.get(html)
    response_list = response.text
    #print(response_list)
    video_url = re.findall(r'srcUrl="(.*?)"', response_list, re.S)[0]
    print(video_url)
    video = requests.get(video_url)
    #print(video)
    name = re.findall(r'<title>(.*?)</title>', response_list, re.S)[0]
    print(html, name)
    os.chdir("F:\Aphrodite\Video")
    with open(str(name) + '.MP4', mode='wb') as f:
        f.write(video.content)
