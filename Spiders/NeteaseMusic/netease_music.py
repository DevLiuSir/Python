#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: netease_music.py
# Datetime: 2019/12/23 03:45
# Software: PyCharm

import requests
import os
import re

from lxml import etree
from selenium import webdriver                          # 引入 selenium 的浏览器驱动接口
from selenium.webdriver.chrome.options import Options   # 引入 chrome 选项


# ===== 歌单ID:           http://music.163.com/playlist?id=2042077203
# ===== 电台ID            https://music.163.com/#/djradio?id=527191603
# ===== 单曲ID            https://music.163.com/#/song?id=1359356908
# ===== 下载歌曲链接:      https://music.163.com/#/song/media/outer/url?id={}.mp3


# 网易云音乐爬虫
class NeteaseMusicSpider:


    def __init__(self):
        # 请求头
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
        # 歌单
        self.play_list_url = 'http://music.163.com/playlist?id='
        # 电台
        self.djradio_url = 'https://music.163.com/#/djradio?id='
        # 单曲
        self.single_url = 'https://music.163.com/#/song?id='
        self.session = requests.Session()
        self.session.headers = self.headers


    def selenium_chrome(self, html):
        '''
        使用 Selenium启动Chrome浏览器测试
        :param html: 浏览器需要打开的网址
        :return: WebDriver对象
        '''
        '''
         Chrome-headless 模式: Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。
         webdriver安装路径: macOS：复制webdriver到/usr/local/bin目录下之后,就不需要指定path
        '''
        # 配置Chrome浏览器 (Headless无界面启动模式)
        option = Options()
        option.headless = True                      # 设置是否启动无界面化
        browser = webdriver.Chrome(options=option)  # 打开chrome浏览器 声明 chrome 浏览器
        browser.get(html)                           # 访问网页
        # browser.implicitly_wait(5)                  # 等待5秒, 1秒加载完毕, 5秒是最长时间
        # print(browser.page_source)                # 将源码打印到终端
        return browser



    def download_songs_from_playlist(self, playlist_number):
        '''
        根据歌单ID, 下载歌单里所有歌曲
        :param playlist_number: 歌单ID
        :return:
        '''
        # 歌单播放链接
        url = self.play_list_url + str(playlist_number)

        print(f'歌单播放链接: {url}')

        browser = self.selenium_chrome(url)

        browser.switch_to.frame('g_iframe')

        # 歌曲列表
        music_list = browser.find_element_by_class_name('j-flag')

        # 歌曲链接列表
        song_link_list = music_list.find_elements_by_xpath('.//div[@class="f-cb"]//a')

        # 排名
        rank_list = music_list.find_elements_by_xpath('.//div[@class="hd "]/span')

        # 歌手名称列表
        singer_name_list = music_list.find_elements_by_xpath('.//div[@class="text"]/span[2]')

        # 歌曲名称列表
        song_name_list = music_list.find_elements_by_xpath('.//div[@class="f-cb"]//b')

        '''
            zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
            我们可以使用 list() 转换来输出列表。
            如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        '''
        for link, name, singer_name, rank in zip(song_link_list, song_name_list, singer_name_list, rank_list):

            single_link = link.get_attribute('href')          # 单曲链接
            single_name = name.get_attribute('title')         # 单曲名称
            single_id = single_link.split('=')[-1]            # 分割链接, 取出单曲id
            singer_name = singer_name.get_attribute('title')  # 歌手
            rank_number = rank.text                           # 排名

            # print(rank_number)
            # print(single_link)
            # print(single_id)
            # print(single_name)

            # songname = singer + '-' + song_name
            # return str(song_id), songname
            # return str(single_id), single_name


            print(f'==== 单曲播放链接: {single_link}')

            # 文件路径名
            fileName = f'/Users/liuchuan/Desktop/NeteaseMusic/{single_name}'

            # 目录名
            # dirname = f'{fileName}/{single_name}_{singer_name}.mp3'
            # new_dirname = self.handle_illegal_characters(dirname)

            dirname = f'{fileName}/{rank_number}-{single_name}.mp3'

            self.make_dir(fileName)
            self.download_songs(single_id, dirname)

        browser.quit()      # 退出所有window



    def download_songs_from_djradio(self, djradio_number):
        '''
        根据电台ID, 下载电台里所有歌曲
        :param djradio_number: 电台ID
        :return:
        '''
        # 电台播放链接
        url = self.djradio_url + str(djradio_number)

        print(f'========= 电台播放链接: {url}')

        browser = self.selenium_chrome(url)

        browser.switch_to.frame('g_iframe')

        # 歌曲列表
        djradio_music_list = browser.find_element_by_class_name('n-songtb')

        # 歌曲链接列表
        song_link_list = djradio_music_list.find_elements_by_xpath('.//div[@class="tt f-thide"]/a')

        # 歌曲名称列表
        song_name_list = djradio_music_list.find_elements_by_xpath('.//div[@class="tt f-thide"]/a')

        # 歌曲id
        song_id_list = browser.find_elements_by_tag_name('tr')

        # 排名列表
        rank_list = djradio_music_list.find_elements_by_xpath('.//div[@class="hd"]/span[2]')

        '''
           zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
           我们可以使用 list() 转换来输出列表。
           如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        '''
        for music_id, link, name, rank in zip(song_id_list, song_link_list, song_name_list, rank_list):

            single_link = link.get_attribute('href')                    # 单曲链接
            single_name = name.get_attribute('title')                   # 单曲名称
            rank_number = rank.text                                     # 排名
            single_id = music_id.get_attribute('id').split('-')[-1]     # 分割歌曲动态id，取出单曲id

            # print(f'歌曲排名: {rank_number}')
            # print(single_id)
            print(f'==== 单曲播放链接: {single_link}')

            # 文件路径名
            file_name = f'/Users/liuchuan/Desktop/NeteaseMusic/djradio/{single_name}'
            # 目录名
            dirname = f'{file_name}/{rank_number}-{single_name}.mp3'
            self.make_dir(file_name)
            self.download_songs(single_id, dirname)

        browser.quit()                  # 退出所有window


    def download_single(self, single_number):
        '''
        下载单曲
        :param single_number: 单曲ID
        '''
        # 单曲播放链接
        url = self.single_url + str(single_number)

        print(f'========= 单曲播放链接: {url}')

        browser = self.selenium_chrome(url)

        browser.switch_to.frame('g_iframe')

        # 单曲ID
        single_id = browser.find_element_by_id('content-operation').get_attribute('data-rid')

        # 单曲名称
        single_name = browser.find_element_by_class_name('f-ff2').text

        print(f'单曲名称: {single_name}')

        # 文件路径名
        file_name = f'/Users/liuchuan/Desktop/NeteaseMusic/single/{single_name}'

        # 目录名
        dirname = f'{file_name}/{single_name}.mp3'

        self.make_dir(file_name)

        self.download_songs(single_id, dirname)



    def make_dir(self, folder_name):
        """
        新建文件夹并切换到该目录下
        :param folder_name: 文件夹名称
        :return:
        """
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        # path = os.path.join(Dir_PATH, folder_name)

        # 根据文件名，检查路径是否存在？
        # 如果目录已经存在，就不用再次爬取，避免重复，提高效率。存在返回 Flase，否则反之
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)  # 如果不存在路径，根据 folder_name 创建文件夹
            # os.chdir(folder_name)       # 改变当前工作目录
            return True
        print("文件夹已经存在！")
        return False



    def download_songs(self, song_id, path):
        '''
        根据歌曲id、下载mp3，并保存
        :param song_id: 歌曲ID
        :param path: 保存目录
        :return:
        '''
        # 歌曲下载链接
        song_download_link = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
        print(f'==== 单曲下载链接: {song_download_link}')
        print()

        try:
            req = self.session.get(url=song_download_link, headers=self.headers)
            with open(path, "wb+") as f:                            # 将下载的音乐保存到对应的路径
                f.write(req.content)
                print(f"[INFO]: 已保存音乐文件: {path}")
                f.close()
        except requests.exceptions.RequestException as e:
            raise e



    def handle_illegal_characters(self, str):
        '''
        处理非法字符串
        :param str: 需要处理的字符串
        return: 处理后全新的字符串
        '''
        new_string = re.sub(u'[()（）: ：]', '_', str)     # 替换中文括号（）、冒号：非法字符， 为_下划线。
        return new_string


    def run(self):
        '''
        主入口函数
        '''
        print('*' * 41)
        print('*' * 10 + '  网易云音乐下载小助手  ' + '*' * 10)
        print('*' * 41)
        print("{0:<13}{1:\u3000<13}{2:\u3000<13}".format("1: 歌单", "2: 电台", "3: 单曲"))

        # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
        kw = eval(input("请选择你要下载歌曲类型:  "))

        if kw == 1:
            songlist_id = eval(input('请键入你要下载的歌单ID:  '))
            self.download_songs_from_playlist(songlist_id)
        elif kw == 2:
            djradio_id = eval(input('请键入你要下载的电台ID:  '))
            self.download_songs_from_djradio(djradio_id)
        else:
            single_id = eval(input('请键入你要下载的单曲ID:  '))
            self.download_single(single_id)




if __name__ == '__main__':

    netease_music = NeteaseMusicSpider()
    netease_music.run()
