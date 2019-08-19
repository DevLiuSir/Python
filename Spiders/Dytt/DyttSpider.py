#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: DyttSpider.py
# Datetime: 2018/12/25 23:16
# Software: PyCharm


import requests
import re
from lxml import etree
from multiprocessing import Pool



# 爬虫类
class DyttSpider:


    def __init__(self):
        # 请求头
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


    def get_all_htmls(self, max_num):
        '''
        下载所有列表页面的HTML，用于后续的分析
        :return: 所有URL
        '''
        htmls = []  # 网址list，用于保存返回到所有网址

        # 构造分页数字列表, 循环获取所有网址
        page_indexs = range(1, max_num + 1)
        for idx in page_indexs:
            url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_' + str(idx) + '.html'
            htmls.append(url)
        return htmls


    def load_webpage_data(self, url):
        """
        加载指定url页面的内容
        :param url: 链接
        :return: 网页源码
        """
        response = requests.get(url=url, headers=self.headers)
        response.encoding = 'gb2312'        # 编码
        # print("状态码:", (response.status_code))
        try:
            if response.status_code == 200:  # 如果状态码为：200，访问成功，返回网页源码，否返回none
                return response.text
            return None
        except requests.ConnectTimeout:
            print('连接远程服务器超时异常！')


    def parse_webpage(self, html):
        """
        筛选html内容,返回列表
        :param html: 需要解析的URL
        :return: 电影链接列表
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


    def get_ftp_url(self, item_list):
        '''
        获取ftp下载链接
        :param item_list: 匹配的电影链接列表
        :return: 筛选后的ftp下载链接
        '''
        # 1.遍历电影链接列表
        for li in item_list:

            # 1.1.拼接电影详情页码的url
            base_url = 'https://www.dytt8.net'+li[0]

            # 2. 加载电影详情页面
            movie_details_url = self.load_webpage_data(base_url)

            # 3.清洗数据
            regx2 = r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href=".*?">(.*?)</a></td>'
            pattern2 = re.compile(regx2)
            # 文档传输协议
            ftp = re.findall(pattern2, movie_details_url)

            return ftp



    def write_text(self, list):
        """
        写入文本. 已追加的形式,存储筛选后的内容
        :param list: 筛选后的数据, 列表形式
        """
        # 遍历匹配成功的链接
        for content in list:

            # print(content)

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
            with open("/Users/liuchuan/Desktop/dytt.txt", 'a+', encoding='utf-8') as f:
                print(f"[INFO]: 已保存: {content}")
                f.write(content+"\n")           # write: 写入本地, write 只能写入文本
                f.close()


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

    print('*' * 32)
    print('*' * 10 + ' 电影天堂爬虫 ' + '*' * 10)
    print('*' * 32)

    # 实例化类对象
    my_spider = DyttSpider()

    # 最大页码
    max_number = my_spider.get_max_page_number()

    # 1.获取所有的网址
    all_html = my_spider.get_all_htmls(max_number)

    # 1.1.遍历网址
    for html in all_html:

        # 2.根据网址，加载页面内容
        webpage_source = my_spider.load_webpage_data(html)

        # 3.根据html，筛选数据
        item_list = my_spider.parse_webpage(webpage_source)

        # 4.拼接url
        ftp = my_spider.get_ftp_url(item_list)

        # 5.写入文本
        my_spider.write_text(ftp)
