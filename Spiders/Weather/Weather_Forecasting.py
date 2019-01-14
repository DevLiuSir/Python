#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Weather_Forecasting.py
# Datetime: 2019-03-25 15:04
# Software: PyCharm


# 引入requests包和正则表达式包re
import requests
import re


# 定义爬取页面的链接
url = 'http://p.weather.com.cn/2017/06/2720826.shtml#p=7'


def load_page(url):
    '''
    根据URL加载页面
    :param url: 网页地址
    :return:
    '''
    response = requests.get(url)
    data = response.content
    return data


def get_image(html):
    '''
    根据URL地址获取图片数据
    :param html:
    :return:
    '''
    regx = r'http://[\S]*jpg'  # 定义图片正则表达式
    pattern = re.compile(regx)  # 编译表达式构造匹配模式
    get_images = re.findall(pattern, repr(html))  # 在页面中匹配图片链接, get_images 是列表

    num = 1
    # 遍历匹配成功的链接
    for img in get_images:

        image = load_page(img)  # 根据图片链接，下载图片链接

        # 将下载的图片保存到对应的文件夹中
        with open('./Weather/%s.jpg' % num, 'wb') as fb:
            fb.write(image)
            print("正在下载第%s张图片" % num)
            num = num + 1

    print("下载完成！")


if __name__ == '__main__':

    html = load_page(url)
    get_image(html)