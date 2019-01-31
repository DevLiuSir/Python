#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Dytt.py
# Datetime: 2019-07-08 18:27
# Software: PyCharm



import requests     # 网络请求模块
import re           # 提取数据
import time         # time.sleep()
from lxml import etree

# 电影天堂:     https://www.dytt8.net/


# 爬虫类
class Spider(object):


    def load_webpage_data(self, url):
        """
        加载指定url页面的内容
        :param url: 链接
        :return:
        """
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        response = requests.get(url=url, headers=Headers)
        response.encoding = 'gb2312'        # 编码
        print("状态码:", (response.status_code))
        html = response.text

        # r.raise_for_status()  #如果状态不是200，则引发异常
        try:
            if response.status_code == 200:  # 如果状态码为：200，访问成功，返回网页源码，否返回none
                return html
            return None
        except requests.ConnectTimeout:
            print('连接远程服务器超时异常！')


    def parse_webpage(self, html):
        """
        筛选html内容,返回列表
        :param html:
        :return:
        """

        # re.compile: 编译表达式构造匹配模式
        # pattern: 正则中的模式字符串。

        # <a href = "/html/gndy/dyzz/20190702/58786.html" class ="ulink" > 2019年剧情传记《最佳敌人》BD中英双字幕 </a >

        # 定义正则表达式
        regx = r'<a href="(.*?)" class="ulink">(.*?)</a>'

        # 编译表达式构造匹配模式
        pattern = re.compile(regx)

        # 在页面中匹配电影链接
        item_list = re.findall(pattern, html)   # findall:返回的是列表

        return item_list


    def join_movies_detail_url(self, item_list):
        '''
        拼接电影详情页码的url
        :param item_list: 匹配的电影链接列表
        :return:
        '''

        for li in item_list:

            # 拼接电影详情页码的url
            base_url = 'https://www.dytt8.net'+li[0]

            # 电影详情页面
            movie_details_url = self.load_webpage_data(base_url)

            regx2 = r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>'

            pattern2 = re.compile(regx2)

            # 文档传输协议
            ftp = re.findall(pattern2, movie_details_url)

            self.write_text(ftp)


    def write_text(self, list):
        """
        写入文本. 已追加的形式,存储筛选后的内容
        :param list: 筛选后的数据, 列表形式
        :return:
        """
        # 遍历匹配成功的链接
        for content in list:

            print(content)

            '''
            # 关于open()的mode参数：
            # 'r'：读
            # 'w'：写
            # 'a'：追加
            # 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
            # 'w+' == w+r（可读可写，文件若不存在就创建）
            # 'a+' ==a+r（可追加可写，文件若不存在就创建）
            # 对应的，如果是二进制文件，就都加一个b就好啦：
            # 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
            '''
            with open("/Users/liuchuan/Desktop/dytt.text", 'a+', encoding='utf-8') as f:

                # write: 写入本地, write 只能写入文本
                f.write(content+"\n")


    def get_max_page_number(self):
        '''
        获取最大页码
        :return: 最大页码
        '''
        baseURL = 'https://www.dytt8.net/html/gndy/dyzz/index.html'

        content = self.load_webpage_data(baseURL)

        # 抽取想要的数据: 图片标题 \ 图片链接等等
        url = etree.HTML(content)

        # 字符串列表
        all = url.xpath("//div[@class='x']//option/text()")  # 所有的数据都在li标签下,我们一这个为总节点

        # 数字列表
        # 使用内置map返回一个map对象，再用list将其转换为列表
        number = list(map(int , all))       # Python3 中 列表字符串 转 数字

        # 获取列表最大值
        max_list = max(number)

        return max_list


if __name__ == '__main__':

    # 实例化类对象
    my_spider = Spider()

    # 最大页码
    max_number = my_spider.get_max_page_number()

    # print(max_number)

    for n in range(1, max_number + 1):      # 循环获取所有网址

        # 1.获取所有的网址
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'

        # 2.根据网址，下载页面内容
        html = my_spider.load_webpage_data(url)

        # 3.根据html，筛选数据
        item_list = my_spider.parse_webpage(html)

        # 4.拼接url
        my_spider.join_movies_detail_url(item_list)