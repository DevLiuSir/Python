#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: i4_wallpapers.py
# Datetime: 2020/1/6 15:02
# Software: PyCharm


import requests
import re
import os
from lxml import etree


# 爱思壁纸爬虫
class i4Wallpapers:


    def __init__(self):
        self.headers = {
            'Referer': 'https://www.i4.cn/ring_1_0_1.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.base_url = 'https://www.i4.cn/wper_1_0_0_1.html'
        self.main_url = 'https://www.i4.cn/'


    def load_webpage_data(self, url):
        '''
        加载网页数据
        :param url: 网页链接
        :return:
        '''

        # urllib 或 requests 在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为True。
        # 如果你想为请求添加HTTP头部，只要简单地传递一个 字典 给 headers 参数
        # 实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3。
        # timeout： 超时时间。如果需要让 request 永远等待，则传入一个 None 作为 timeout 的值。
        # timeout单位：秒。
        response = requests.get(url=url, verify=True, headers=self.headers, timeout=None)
        response.encoding = 'utf-8'  # 编码
        # 获取网页源码
        html = response.text
        try:
            if response.status_code == 200:  # 如果状态码为：200，访问成功，返回网页源码，否返回none
                return html
            return None
        except requests.ConnectTimeout:
            print('连接远程服务器超时异常！')


    def get_root_category(self):
        '''
        获取壁纸主分类
        :return: 分类主链接
        '''

        response = requests.get(self.base_url, headers=self.headers)
        response.encoding = 'utf-8'
        html = etree.HTML(response.content)

        # 导航名称
        navigation_name = html.xpath('//div[@class="content_nav"]/a/text()')
        # 导航链接
        navigation_link = html.xpath('//div[@class="content_nav"]/a/@href')

        # 获取导航中的分类: 导航列表最后一个值
        # 分类主名称
        # root_category_name = navigation_name[-1]
        # 分类主链接
        root_category_link = self.main_url + navigation_link[-1]

        return root_category_link


    def get_sub_category(self, root_category_html):
        '''
        根据主分类URL， 获取主分类下面的所有子分类
        :param root_category_html: 主分类URL
        :return: 分类名称列表、分类链接列表
        '''
        html = self.load_webpage_data(root_category_html)

        # 分类子名称
        class_names = etree.HTML(html).xpath('//div[@class="class"]/a/text()')
        # 分类子链接
        class_links = etree.HTML(html).xpath('//div[@class="class"]/a/@href')

        all_names = []  # 分类名称列表
        all_links = []  # 分类链接列表

        for link, class_name in zip(class_links, class_names):
            sub_category_link = self.main_url + link  # 子分类链接
            all_names.append(class_name)
            all_links.append(sub_category_link)
        return all_names, all_links


    def get_all_images(self, sub_category_link, root_category_name):
        '''
        根据子分类链接获取所有图片
        :param sub_category_link: 子分类链接
        :param root_category_name: 主分类名称
        :return:
        '''
        content_list = self.load_webpage_data(sub_category_link)
        big_picture_url_list = etree.HTML(content_list).xpath('//div[@class="kbox"]/div[@class="list wper_play iphonex"]/a/@href')
        big_picture_name_list = etree.HTML(content_list).xpath('//div[@class="kbox"]/div[@class="list wper_play iphonex"]/a/@title')

        for big_url, big_picture_name in zip(big_picture_url_list, big_picture_name_list):

            # 详情名称使用_下划线代替空格,防止创建文件夹错误
            detail_name = big_picture_name.replace(' ', '_')
            detail_url = self.main_url + big_url

            # print(detail_name)
            # print(detail_url)

            self.get_big_picture(detail_url, detail_name, root_category_name)


    def get_big_picture(self, url, picture_name, folder_name):
        '''
        获取大图
        :param url: 下载页面的URL
        :param picture_name: 图片名称
        :param folder_name:  文件名称
        :return:
        '''
        html = self.load_webpage_data(url)

        # findall: 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        # 在页面中匹配图片链接
        picture_list = re.findall('src="https://d-paper.i4.cn/(.*?).jpg', html)

        for picture in picture_list:
            download_url = 'https://d-paper.i4.cn/' + picture + '.jpg'
            print(download_url)

            # 文件路径名
            fileName = f'/Users/liuchuan/Desktop/i4_Wallpapers/{folder_name}'

            # 目录名
            dirname = f'{fileName}/{picture_name}.jpg'

            self.make_dir(fileName)
            self.save_images(download_url, dirname)


    def save_images(self, image_url, dst_path):
        '''
        保存图片到本地
        :param image_url: 图片地址
        :param dst_path: 保存路径
        '''
        try:
            req = requests.get(url=image_url, headers=self.headers)
            with open(dst_path, "wb+") as f:  # 将下载的图片保存到对应的路径
                f.write(req.content)
                print(f"[INFO]: 已保存图片文件: {dst_path}")
                f.close()
        except requests.exceptions.RequestException as e:
            raise e


    def make_dir(self, folder_name):
        """
        新建文件夹并切换到该目录下
        :param folder_name: 文件夹名称
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



if __name__ == '__main__':

    i4_wallpapers = i4Wallpapers()
    root_category = i4_wallpapers.get_root_category()
    sub_category = i4_wallpapers.get_sub_category(root_category)

    print(sub_category[0])

    # sub_category[0]:  分类名称
    # sub_category[1]:  分类链接
    for class_name, sub_category_link in zip(sub_category[0], sub_category[1]):
        i4_wallpapers.get_all_images(sub_category_link, class_name)
