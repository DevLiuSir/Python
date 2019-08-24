#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Meitulu.py
# Datetime: 2019/07/13 01:23
# Software: PyCharm


import requests
import re
import os
from lxml import etree
from multiprocessing import Pool

#  multiprocessing模块Pool类
#  Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求。
#  如果池满，请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求。

"""
1、https://www.meitulu.com/t/changtui/               ：获取主页美女套图链接，名称。
2、https://www.meitulu.com/item/18759.html           ：抓取每一个写真集合的链接(注意是分页的)
3、https://mtl.gzhuibei.com/images/img/18759/1.jpg   ：获取每张图片的地址，下载到本地。
"""



# 美图录爬虫
class MeiTuLuSpider:

    def __init__(self):
        # 请求头
        self.headers = {
            'referer': 'https://www.meitulu.com/t/changtui/',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        # 主要套图URL
        self.base_url = 'https://www.meitulu.com/t/changtui/'

        # 套图详情URL
        self.picture_details_url = 'https://www.meitulu.com'


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
        response.encoding = 'utf-8'     # 编码
        # 获取网页源码
        html = response.text
        try:
            if response.status_code == 200:  # 如果状态码为：200，访问成功，返回网页源码，否返回none
                return html
            return None
        except requests.ConnectTimeout:
            print('连接远程服务器超时异常！')



    def filter_data(self, html):
        '''
        筛选html内容
        :param html: 网页源码
        :return: 套图链接, 套图名称
        '''

        # re.compile: 编译表达式构造匹配模式
        # pattern: 正则中的模式字符串。

        # 定义正则表达式
        regx = r'<a href="(.*?)" target="_blank"><img src="(.*?)" alt="(.*?)".*?</a>'

        # 编译表达式构造匹配模式
        pattern = re.compile(regx)

        """
        findall: 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        """
        # 在页面中匹配图片链接
        picture_list = re.findall(pattern, html)  # findall:返回的是列表

        # 遍历匹配成功的链接
        for n in picture_list:
            link = n[0]     # 取第0个元素: 套图的链接
            # Cover = n[1]    # 去第1个元素: 套图封面
            name = n[2]     # 取第2个元素：套图名称

            return link, name


    def get_details_set(self, photoSetLink, picture_name):
        '''
        获取套图详情页面信息
        :param photoSetLink: 套图链接
        :param picture_name: 套图名称
        :return:
        '''

        # 1. 请求美图录，拿到HTML数据
        response = requests.get(url=photoSetLink, headers=self.headers)

        # 2. 抽取想要的数据: 图片标题 \ 图片链接
        html = etree.HTML(response.content)

        # 2.1.页码数
        next_list = html.xpath('//div[@id="pages"]/a/text()')
        # 2.2.下一页URL
        next_url = html.xpath('//div[@id="pages"]/a/@href')

        next_url.pop()  # 移除最后一个重复的元素

        base_url = next_url[0]      # 基础的URL地址
        max_page = next_list[-2]    # 最大页码
        splice_after_url = ""       # 拼接后的URL

        # 获取所有页面URL
        count = 1
        while count <= int(max_page):
            if count <= 1:
                splice_after_url = photoSetLink
            else:  # 替换字符串
                splice_after_url = str(photoSetLink).replace('.html', f'_{count}.html')
            count += 1

            big_images = self.load_webpage_data(splice_after_url)

            html = etree.HTML(big_images)

            # 大图名称
            alt_list = html.xpath('//div/center/img/@alt')

            # 大图链接
            src_list = html.xpath('//div/center/img/@src')

            '''
            zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
            我们可以使用 list() 转换来输出列表。
            如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
            '''
            for alt, src in zip(alt_list, src_list):
                # 文件路径名
                fileName = f'/Users/liuchuan/Desktop/Girls/{picture_name}'
                # 目录名
                dirname = f'{fileName}/{alt}.jpg'

                self.make_dir(fileName)

                self.save_images(src, dirname)


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


    def get_total_page(self):
        '''
        获取总页数
        :return: 总页数
        '''
        response = requests.get(self.base_url, headers=self.headers)
        response.encoding = 'utf-8'
        html = etree.HTML(response.content)
        # 总页数: 列表倒数第2个元素
        total_p = html.xpath('//div[@id="pages"]/a/text()')[-2]
        return int(total_p)


    def get_all_url(self):
        '''
        获取所有套图URL
        :return: 所有套图URL
        '''
        # 网址list，用于保存返回到所有网址
        urls = []
        for n in range(1, self.get_total_page() + 1):
            url = ''
            if n <= 1:
                url = self.base_url
            else:
                url = self.base_url + str(n) + '.html'
            urls.append(url)
        return urls



    def run(self):
        """
        主运行函数
        """

        # 1.获取所有URL
        all_urls = self.get_all_url()
        # 1.1.遍历网址
        for url in all_urls:
            # 2.根据所有网址，加载页面内容
            html = self.load_webpage_data(url)
            # 3.筛选数据(获取美女套图封面、链接、名称)
            link_and_name = self.filter_data(html)
            # 4.根据套图链接\名称
            self.get_details_set(link_and_name[0], link_and_name[1])




if __name__ == '__main__':

    mei_tu_lu = MeiTuLuSpider()
    mei_tu_lu.run()
