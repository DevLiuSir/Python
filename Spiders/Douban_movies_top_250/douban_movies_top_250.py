#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: douban_movies_top_250.py
# Datetime: 2019/11/23 15:13
# Software: PyCharm


import re
import requests
import openpyxl
import pandas as pd
import pprint

from multiprocessing import Pool
from lxml import etree
from requests.exceptions import RequestException


# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}


def download_all_htmls():
    """
    下载所有列表页面的HTML，用于后续的分析
    """

    htmls = []          # 网址list，用于保存返回到所有网址

    # 构造分页数字列表
    page_indexs = range(0, 250, 25)     # 从0开始，到250结束，步长为 25

    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls


def parseOnePage(html):
    '''
    解析数据
    :param html: 网址
    :return: 电影清单list
    '''
    film_list = []      # 电影清单list, 用于保存抽取后的数据

    # 抽取想要的数据: 图片标题 \ 图片链接等等
    url = etree.HTML(html)
    all = url.xpath('//div[@class="article"]/ol/li')    # 所有的数据都在li标签下,我们一这个为总节点

    for detail in all:

        title = detail.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]         # 电影名字
        rating_num = detail.xpath('.//span[@class="rating_num"]/text()')[0]     # 评分
        comment_sum = detail.xpath('.//div[@class="star"]/span[4]/text()')[0]   # 评论人数
        ranking = detail.xpath('.//div[@class="pic"]/em/text()')[0]             # 排名

        # 主演信息中, 有太多非法符号你需要删除
        # strip(): 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

        workers = detail.xpath('.//div[@class="bd"]/p/text()')[0].strip()       # 工作人员(找到影片相关内容：导演，主演，年份，地区，类别)
        release_time = detail.xpath('.//div[@class="bd"]/p/text()')[1].strip()  # 上映时间
        quote = detail.xpath('.//p[@class="quote"]/span/text()')                # 引言  由于有的电影没有引言,不判断会报错

        if len(quote) == 0:
            quote = '暂无引言'
        else:
            quote = quote[0]

        film_list.append({
            "排名": ranking,
            "电影名称": title,
            "上映时间": release_time,
            "工作人员": workers,
            "评分": rating_num,
            "评论人数": comment_sum.replace("人评价", ""),
            "描述": quote
        })

    return film_list


def run():

    # 执行爬取
    htmls = download_all_htmls()

    # print(htmls[0])
    # pprint.pprint(parseOnePage(htmls[0]))

    # 执行所有的HTML页面的解析
    all_datas = []

    for html in htmls:
        all_datas.extend(parseOnePage(html))

    df = pd.DataFrame(all_datas)

    # 这两个参数的默认设置都是False
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)

    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    pd.set_option('display.width', 300)         # 横向最多显示多少个字符
    pd.set_option('max_colwidth', 40)           # 设置value的显示长度为100，默认为50

    print(df)

    # pandas 写入csv文件
    df.to_csv("豆瓣电影TOP250.csv", encoding='utf-8', index=False, header=True)
    print("写入完成!")

    # pandas读取csv文件
    # deee = pd.read_csv('豆瓣电影TOP250.csv', encoding="utf-8")  # 奇怪的编码


    # 写入 Excel文件
    # index：默认为True，显示index，当index=False 则不显示行索引（名字）
    # df.to_excel("豆瓣电影TOP250.xls", encoding='utf-8', index=False, header=True)
    # print("写入完成!")



if __name__ == '__main__':
    run()