#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Dytt.py
# Datetime: 2019-07-08 18:27
# Software: PyCharm



import requests     # 网络请求模块
import re           # 提取数据
import time         # time.sleep()

# 电影天堂:     https://www.dytt8.net/

# 定义一个Spider类，并且添加一个加载页面的成员方法
class Spider(object):


    # 加载网页数据
    def load_webpage_data(self, url):
        """
        下载指定url页面的内容
        :param url: 链接
        :return:
        """

        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        response = requests.get(url = url, headers = header)

        # 编码
        response.encoding = 'gb2312'

        print("状态码:", (response.status_code))

        html = response.text

        # 打印页面内容
        # print(html)

        # 返回页面内容
        return html



    # 解析网页
    def parse_webpage(self, html):

        """
        筛选html内容,返回列表
        :param html:
        :return:
        """

        # <div class="co_content8">.......</div>

        # 定义图片正则表达式, re.compile: 编译表达式构造匹配模式
        # pattern: 正则中的模式字符串。
        # pattern = re.compile(r'<div class="co_content8">(.*?)</div>', re.S)

        # <a href = "/html/gndy/dyzz/20190702/58786.html" class ="ulink" > 2019年剧情传记《最佳敌人》BD中英双字幕 </a >

        # 定义正则表达式
        regx = r'<a href="(.*?)" class="ulink">(.*?)</a>'

        # 编译表达式构造匹配模式
        pattern = re.compile(regx)

        # 在页面中匹配电影链接
        item_list = re.findall(pattern, html)   # findall:返回的是列表

        return item_list


    # 拼接电影详情页码的url
    def join_movies_detail_url(self, item_list):

        for li in item_list:

            # 拼接电影详情页码的url
            base_url = 'https://www.dytt8.net'+li[0]
            # print(base_url)

            # 电影详情页面
            movie_details_url = self.loadPage(base_url)
            # print(movie_details_url)

            regx2 = r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>'

            pattern2 = re.compile(regx2)

            # 文档传输协议
            ftp = re.findall(pattern2, movie_details_url)

            self.write_text(ftp)


    # 写入文本
    def write_text(self, list):

        """
        已追加的形式,存储筛选后的内容
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




if __name__ == '__main__':

    # 实例化类对象
    my_spider = Spider()

    for n in range(1,198):  # 总共有197页数据, 循环获取网址

        # 1.获取所有的网址
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'

        # 2.根据网址，下载页面内容
        html = my_spider.load_webpage_data(url)

        # 3.根据html，筛选数据
        item_list = my_spider.parse_webpage(html)

        # 4.拼接url
        join_url = my_spider.join_movies_detail_url(item_list)

        # print(join_url)
