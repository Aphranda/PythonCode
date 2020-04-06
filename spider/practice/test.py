import tkinter
import os
import pygame
import time
from urllib.request import urlretrieve
from selenium import webdriver


def display(item):
    os.chdir('E:\music')
    song_name = item['song_name']
    file = str(song_name) + '.mp3'
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def stop(item):
    os.chdir('E:\music')
    song_name = item['song_name']
    file = str(song_name) + '.mp3'
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load(file)
    pygame.mixer.music.stop()


def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    # https://music.163.com/#/search/m/?s=%E7%BB%BF%E8%89%B2&type=1
    # https://music.163.com/song/media/outer/url?id={}.mp3
    print(song_url)
    # 下载歌曲
    os.chdir('E:\\')
    os.makedirs('music', exist_ok=True)
    path = 'music\{}.mp3'.format(song_name)
    # 文本框
    text.insert(tkinter.END, '歌曲：{}.正在下载'.format(song_name))
    # 文本框滚动
    text.see(tkinter.END)
    # 文本更新
    text.update()

    urlretrieve(song_url, path)
    # 文本框
    text.insert(tkinter.END, '歌曲：{}.下载完毕'.format(song_name))
    # 文本框滚动
    text.see(tkinter.END)
    # 文本更新
    text.update()


def get_music_name():
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    # 神隐模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    # 获取歌曲ID
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    # print(a_id)
    song_id = a_id.split('=')[-1]
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name
    song_load(item)


def display_music():
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    # 神隐模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    # 获取歌曲ID
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    # print(a_id)
    song_id = a_id.split('=')[-1]
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name
    display(item)


def stop_music():
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    # 神隐模式
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    # 获取歌曲ID
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    # print(a_id)
    song_id = a_id.split('=')[-1]
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name
    stop(item)


root = tkinter.Tk()
# add title
root.title('Music Download')
# config windows size
root.geometry('520x420')
# lable
lable = tkinter.Label(root, text='请输入下载歌曲：', font=('华文行楷', 20))
# config lable位置
lable.grid()
# display windows
# input
entry = tkinter.Entry(root, font=('隶书', 20), width=20)
entry.grid(row=0, column=1)
# list box
text = tkinter.Listbox(root, font=('隶书', 16), width=45, height=15)
# 框横跨两列
text.grid(row=1, columnspan=2)
# 下载按钮
button1 = tkinter.Button(root, text='开始下载', font=('隶书', 15), command=get_music_name)
button1.grid(row=2, column=0, sticky=tkinter.W)
# 推出按钮
button2 = tkinter.Button(root, text='退出程序', font=('隶书', 15), command=root.quit)
button2.grid(row=2, column=1, sticky=tkinter.E)
button3 = tkinter.Button(root, text='播放歌曲', font=('隶书', 15), command=display_music)
button3.grid(row=2, column=0, sticky=tkinter.E)
button4 = tkinter.Button(root, text='停止播放', font=('隶书', 15), command=stop_music)
button4.grid(row=2, column=1, sticky=tkinter.W)


root.mainloop()

# 打包
# pyinstall -F(路径）-w（去除命令行窗口）-i（图表路径）
