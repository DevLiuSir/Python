#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: JJ_Wallpapers.py
# Datetime: 2018/1/13 05:55
# Software: PyCharm


import re
import os
import requests
import bs4

from lxml import etree
from multiprocessing import Pool


# 娟娟壁纸爬虫
class JuanWallpapersSpider:

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

        self.main_url = 'http://www.jj20.com'

        self.pic_main_url = 'http://pic.jj20.com'


    def load_webpage_data(self, url):
        '''
        加载网页数据
        :param url: 网页链接
        :return: 网页源码
        '''
        """
        urllib 或 requests 在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为True。
        如果你想为请求添加HTTP头部，只要简单地传递一个 字典 给 headers 参数
        实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3。
        timeout： 超时时间。如果需要让 request 永远等待，则传入一个 None 作为 timeout 的值。
        timeout单位：秒。
        """
        response = requests.get(url=url, verify=False, headers=self.headers, timeout=None)
        response.encoding = 'gb2312'            # 编码
        html = response.text                    # 获取网页源码
        try:
            if response.status_code == 200:     # 如果状态码为：200，访问成功，返回网页源码，否返回none
                return html
            return None
        except requests.ConnectTimeout:
            print('连接远程服务器超时异常！')


    def get_wallpapers_category(self):
        '''
        获取壁纸分类信息
        :return: 分类名称、分类链接、分类尺寸
        '''
        response = self.load_webpage_data(self.main_url)

        # 壁纸分类名称
        wallpapers_category_name = etree.HTML(response).xpath('//div[@class="g-class-top"]/a/text()')

        # 壁纸分类链接
        wallpapers_category_link = etree.HTML(response).xpath('//div[@class="g-class-top"]/a/@href')

        # 壁纸尺寸分类
        wallpapers_size_category = etree.HTML(response).xpath('//div[@class="g-class-cc"]/a/text()')

        # 壁纸尺寸链接
        wallpapers_size_link = etree.HTML(response).xpath('//div[@class="g-class-cc"]/a/@href')

        # print(wallpapers_category_name)
        # print(wallpapers_category_link)
        # print(wallpapers_size_category)
        # print(wallpapers_size_link)

        all_names = []              # 分类名称列表
        all_links = []              # 分类链接列表
        all_category_size = []      # 尺寸分类

        for link, name, size in zip(wallpapers_size_link, wallpapers_category_name, wallpapers_size_category):
            all_links.append(link)
            all_names.append(name)
            all_category_size.append(size)

        return all_links, all_names, all_category_size


    def get_user_specified_wallpaper_size_link(self, wallpaper_resolution):
        '''
        获取用户指定壁纸尺寸的链接
        :param wallpaper_resolution: 壁纸分辨率
        :return: 指定壁纸尺寸的链接
        '''
        response = j_wallpapers.load_webpage_data(self.main_url)
        soup = bs4.BeautifulSoup(response, "html.parser")

        link_list = []
        # 解析信息标签结构，查找所有a标签，且每个a标签中href中包含关键字 (wallpapers_size)
        for x in soup.find_all('a', string=re.compile(wallpaper_resolution)):
            link = x.get('href')
            link_list.append(link)
        return link_list


    def get_specified_category_picture(self, category_link):
        '''
        获取指定分类下的图片
        :param category_link: 分类链接
        :return:
        '''
        # 5k分辨率下的URL
        five_k_url = self.main_url + category_link

        # 最大页码
        max_page = self.get_total_page(five_k_url)

        # 拼接后的所有URL
        splice_after_url_list = self.get_url_of_all_pages_in_gallery(max_page, five_k_url)

        for url in splice_after_url_list:

            response = self.load_webpage_data(url)

            result_list = re.findall('<a href="(.*?)">(.*?)</a>(.*?)<ins>(.*?)</ins>', response)

            for result in result_list:

                # 详情壁纸URL
                wallpapers_detail_url = self.main_url + result[0]

                # 详情壁纸名称
                wallpapers_detail_name = result[1]

                # 壁纸数量
                number_of_wallpapers = result[2]

                # 壁纸时间
                wallpaper_time = result[3]

                # 文件名
                filename = wallpapers_detail_name + number_of_wallpapers

                # print(filename)
                # print(wallpapers_detail_url)
                # print(wallpapers_detail_name)
                # print(number_of_wallpapers)

                # 图片数
                pic_num = number_of_wallpapers.replace('(', "").replace('张)', '')

                # 拼接后的所有URL
                splice_after_urls = self.get_url_of_all_pages_in_gallery(pic_num, wallpapers_detail_url)

                for url in splice_after_urls:

                    # 图片名称
                    picture_name = url.split('/')[-1].replace('.html', '')

                    self.get_big_picture(url, picture_name, filename)


    def get_big_picture(self, url, picture_name, folder_name):
        '''
        获取大图
        :param url: 下载页面的URL
        :param picture_name: 图片名称
        :param folder_name:  文件名称
        :return:
        '''
        rep = self.load_webpage_data(url)
        urls = re.findall("<script>var id='(.*?)';</script>", rep)
        for url in urls:
            # 下载图片URL
            download_url = self.pic_main_url + url
            # print(download_url)

            # 文件路径名
            fileName = f'/Users/liuchuan/Desktop/Juan_Wallpapers/{folder_name}'

            # 目录名
            dirname = f'{fileName}/{picture_name}.jpg'

            self.make_dir(fileName)
            self.save_images(download_url, dirname)


    def get_url_of_all_pages_in_gallery(self, max_pages_number, need_spliced_url):
        '''
        根据网页里下一页的规律, 利用拼接，获取图集里所有页面URL
        :param max_pages_number:  网页中最大页码
        :param need_spliced_url:  需要拼接的主要URL
        :return: 拼接后的所有URL列表
        '''
        # 定义一个列表，用来存储拼接后的所有URL
        all_urls = []

        # 定义一个变量，用来存储拼接后的URL
        splice_after_url = ""

        # 获取所有页面URL
        count = 1
        while count <= int(max_pages_number):
            if count <= 1:
                splice_after_url = need_spliced_url
            else:   # 替换字符串
                splice_after_url = str(need_spliced_url).replace('.html', f'_{count}.html')
            count += 1
            all_urls.append(splice_after_url)

        return all_urls


    def get_total_page(self, html):
        '''
        获取总页数
        :param html:
        :return: 总页数
        '''
        content = self.load_webpage_data(html)
        total_pages = re.findall(r'<strong>(.*?)</strong>页', content)
        total_page = max(total_pages)
        return total_page


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

    j_wallpapers = JuanWallpapersSpider()

    wallpapers_category = j_wallpapers.get_wallpapers_category()

    # wallpapers_category[0]:    分类链接
    # wallpapers_category[1]:    分类名称
    # wallpapers_category[2]:    分类尺寸

    print(wallpapers_category[2])

    # 壁纸尺寸
    wallpapers_size = input('输入你想要下载的壁纸尺寸: ')

    print(f'下载的壁纸分辨率: {wallpapers_size}')

    category_links = j_wallpapers.get_user_specified_wallpaper_size_link(wallpapers_size)

    for category_link in category_links:

        j_wallpapers.get_specified_category_picture(category_link)

    print('当前图集所有图片已下载完成......')
