#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: BingWallpapers.py
# Datetime: 2019/12/26 22:52
# Software: PyCharm

import re
import os
import requests
from time import sleep



#必应壁纸爬虫
class BingWallpapersSpider:


    def __init__(self):
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        # 主要URL
        self.base_url = 'https://bing.ioliu.cn/'

    def get_picture_url(self, index=1):
        '''
        根据分页索引，获取图片URL, 图片名称。
        :param index: 索引
        :return: 图片URL, 名称
        '''
        # 判断url规律
        url = ''
        if index < 2:
            url = self.base_url
        else:
            url = f'{self.base_url}?p={index}'

        response = requests.get(url, headers=self.headers).text

        # re.compile: 编译表达式构造匹配模式
        # pattern: 正则中的模式字符串。
        # 定义正则表达式
        regx = r'<img.*?src="(.*?)">'
        regx2 = r'<h3>(.*?)</h3>'

        # 编译表达式构造匹配模式
        pattern = re.compile(regx, re.S)
        pattern2 = re.compile(regx2, re.S)

        """
        findall: 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        """
        # 在页面中匹配图片链接、图片名称, findall:返回的是列表
        urls = re.findall(pattern, response)
        names = re.findall(pattern2, response)

        return urls, names


    def save_images(self, image_url, dst_path):
        '''
        保存图片到本地
        :param image_url: 图片地址
        :param dst_path: 保存路径
        :return:
        '''
        print(image_url)
        try:
            req = requests.get(url=image_url, headers=self.headers)
            with open(dst_path, "wb+") as f:  # 将下载的图片保存到对应的路径
                f.write(req.content)
                print(f"[INFO]: 已保存图片文件: {dst_path}")
        except requests.exceptions.RequestException as e:
            raise e


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
        # print("文件夹已经存在！")
        return False



    def get_total_page(self):
        '''
        获取总页数
        '''
        response = requests.get(self.base_url, headers=self.headers).text
        regx3 = r'.*?上一页</a><span>(.*?)</span>.*?'
        pattern3 = re.compile(regx3, re.S)
        total_p = re.findall(pattern3, response)[0].split('/')[-1]  # 取第0哥元素，分割字符串
        total_pag = total_p.lstrip()       # string.lstrip(): 截掉 string 左边的空格
        return total_pag



    def get_bing_wallpapers(self, index):
        '''
        根据用户输入的页码， 获取必应壁纸
        :param index: 页码
        '''
        picture_urls = self.get_picture_url(index)

        '''
        zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
        我们可以使用 list() 转换来输出列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        '''
        for image_url, image_name in zip(picture_urls[0], picture_urls[1]):

            # 去掉非法字符
            new_image_name = image_name.split()[0]

            # 文件路径名
            filename = f'/Users/liuchuan/Desktop/BingWallpapers'
            # 目录名
            dirname = f'{filename}/{new_image_name}.jpg'

            self.make_dir(filename)
            self.save_images(image_url, dirname)



    def run(self):
        '''
        主入口函数
        '''
        print("*" * 94)
        print("*" * 20 + "    必应壁纸下载工具, 本工具未经资源站授权    " + "*" * 33)
        print("*" * 20 + f"    目前资源站收容页数为{self.get_total_page()}, 当前仅提供1920x1080分辨率下载  " + "*" * 20)
        print("*" * 94)

        i = 1
        sleep(0.1)
        index = eval(input(f"请输入你要下载的页数,（共有{self.get_total_page()}页）:  "))
        while i <= index:
            print(f"当前第{i}页, 共需要下载{index}页")
            self.get_bing_wallpapers(i)
            i += 1

        print("下载完成,将在3秒后关闭...")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("0")


if __name__ == '__main__':
    bing = BingWallpapersSpider()
    bing.run()
