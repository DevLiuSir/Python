#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: ChinaHackers
# File: Mzitu.py
# Datetime: 2019-01-23 15:43
# Software: PyCharm


'''
python库:
    http请求：requests
    图片提取：bs4
    存储相关: os

'''

import requests
from bs4 import BeautifulSoup
import os
import time


url = 'https://www.mzitu.com/'

headers = {
    'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1554082833; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1554098016',
    'referer': 'https://www.mzitu.com/172429',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


# 获取每组照片的url
def get_url(url, headers):

    # 1. 请求妹子图拿到网站数据
    # 用get方法打开url并发送headers
    response = requests.get(url, headers = headers)

    # 用bs4库，创建对象，解析网页 lxml
    soup = BeautifulSoup(response.text,'lxml')

    # 在网页源码中，寻找target标签
    for i in soup.find_all(target = '_blank'):

        if i.select('img'):
            # 图片的链接
            img_url = i.get('href')

            get_second_parse(img_url, headers)

            time.sleep(2)

            print(img_url)

    if soup.select('a.next.page-numbers')[0].get('href'):
        # 下一页链接
        next_url = soup.select('a.next.page-numbers')[0].get('href')
        # 根据下一页链接，下载每组图片
        get_url(next_url, headers)



# 下载每张照片
def get_second_parse(list_url, headers):
        count = 1
        try:
            name_text = BeautifulSoup(requests.get(list_url, headers = headers).text,'lxml')
            name = name_text.select('.main-title')[0].get_text()

            for i in range(1, 21):

                page_url = list_url + '/' + str(i)

                res = requests.get(page_url, headers = headers)

                print(page_url)

                soup = BeautifulSoup(res.text,'lxml')

                print('正在下载{}第{}张图片'.format(name,count))

                print(soup.select('.main-image p a img')[0].get('src'))

                if soup.select('.main-image p a img')[0].get('src'):

                    url = soup.select('.main-image p a img')[0].get('src')

                    filename = 'meizitu/{}'.format(name)

                    # 根据文件名，检查路径是否存在？
                    if not os.path.exists(filename):
                        # 如果不存在路径，根据filename创建文件
                        os.makedirs(filename)

                    print(filename)

                    dirname ='%s/%s.jpg' % (filename, count)

                    with open(dirname, 'wb+') as jpg:

                        jpg.write(requests.get(url,headers =headers).content)

                    count +=1

                    print(url)
        except:
                None



if __name__=='__main__':
    get_url(url, headers)

