#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: mao.py
# Datetime: 2019/11/22 15:49
# Software: PyCharm



import json
import re
import requests

from multiprocessing import Pool
from requests.exceptions import RequestException



# 请求头
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,ja;q=0.7,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}



def getOnePage(url):
    '''
    获取一页数据（html页面）
    :param url: 网址
    '''

    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parseOnePage(html):
    '''
    解析数据
    :param html: 网址
    :return:
    '''


    # re.compile: 编译表达式构造匹配模式
    # pattern: 正则中的模式字符串。

    # 定义正则表达式
    regx = r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'\
           +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'\
           +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'

    # 编译表达式构造匹配模式
    pattern = re.compile(regx, re.S)

    # 在页面中匹配电影信息, findall:返回的是列表
    items = re.findall(pattern, html)

    for item in items:
        # 相当于return一个字典
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

def writeToFile(content):
    '''
    写入文件
    :param content:
    :return:
    '''

    with open('maoyan.txt', 'a', encoding='utf-8') as f:
        # 数据转换成json格式的字符串
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    '''
    主函数
    :param offset:
    :return:
    '''

    url = 'http://maoyan.com/board/4?offset=' + str(offset)

    html = getOnePage(url)

    for item in parseOnePage(html):
        # print(item)
        writeToFile(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(0, 10)])
    pool.close()
    pool.join()
