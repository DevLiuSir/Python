#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Meitulu.py
# Datetime: 2019-07-13 01:23
# Software: PyCharm

import requests
import re
import os
import time

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


# 定制请求头
HEADERS = {
    'referer': 'https://www.meitulu.com/t/changtui/',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}



def load_webpage_data(url):
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
    response = requests.get(url=url, verify=True, headers=HEADERS, timeout=None)

    # 编码
    response.encoding = 'utf-8'

    # print("状态码:", (response.status_code))

    # 获取网页源码
    html = response.text

    # 打印页面内容
    # print(html)
    # response.raise_for_status()  #如果状态不是200，则引发异常
    try:
        if response.status_code == 200:  # 如果状态码为：200，访问成功，返回网页源码，否返回none
            return html
        return None
    except requests.ConnectTimeout:
        print('连接远程服务器超时异常！')



def Filter_data(html):
    '''
    筛选html内容,返回列表
    :param html: 网页源码
    :return:
    '''

    # re.compile: 编译表达式构造匹配模式
    # pattern: 正则中的模式字符串。

    """
    <a href="https://www.meitulu.com/item/18357.html" target="_blank"><img src="https://mtl.ttsqgs.com/images/img/18357/0.jpg" alt="[LIGUI丽柜] 网络丽人 佳怡 - 黑丝长腿女警制服[78]" width="220" height="300" original="https://mtl.ttsqgs.com/images/img/18357/0.jpg"></a>
    """

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

        link = n[0]  # 取第0个链接: 套图的链接
        name = n[2]  # 取第2个元素：套图名称

        get_details_set(link, name)
        # print(link)
        # print(name)


def save_images(image_url, dst_path):
    '''
    保存图片到本地
    :param image_url: 图片地址
    :param dst_path: 保存路径
    :return:
    '''
    try:
        req = requests.get(url=image_url, headers=HEADERS)
        with open(dst_path, "wb+") as f:    # 将下载的图片保存到对应的路径
            f.write(req.content)
            print(f"[INFO]: 已保存图片文件: {dst_path}")
            f.close()
    except requests.exceptions.RequestException as e:
        raise e


def make_dir(folder_name):
    """
    新建文件夹并切换到该目录下
    :param folder_name: 文件夹名称
    :return:
    """

    # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    # path = os.path.join(Dir_PATH, folder_name)

    # 根据文件名，检查路径是否存在？
    # 如果目录已经存在，就不用再次爬取，避免重复，提高效率。存在返回 Flase，否则反之
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)    # 如果不存在路径，根据 folder_name 创建文件夹
        # os.chdir(folder_name)       # 改变当前工作目录
        return True
    
    # print("文件夹已经存在！")
    return False



def delete_empty_dir(save_dir):
    '''
    如果程序半路中断的话，可能存在已经新建好文件夹, 但是仍没有下载的图片的情况.
    但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    :param save_dir:  已经保存的文件夹
    :return:
    '''
    if os.path.exists(save_dir):
          if os.path.isdir(save_dir):
              for d in os.listdir(save_dir):
                  path = os.path.join(save_dir, d)     # 组装下一级地址
                  if os.path.isdir(path):
                      delete_empty_dir(path)      # 递归删除空文件夹
          if not os.listdir(save_dir):
              os.rmdir(save_dir)
              print(f"remove the empty dir: {save_dir}")
    else:
        print("Please start your performance!")     # 请开始你的表演

    



def get_details_set(photoSetLink, picture_name):
    '''
    获取套图详情页面信息
    :param photoSetLink: 套图链接
    :param picture_name: 套图名称
    :return:
    '''

    # 1. 请求美图录，拿到HTML数据
    response = requests.get(url=photoSetLink, headers=HEADERS)

    # 2. 抽取想要的数据: 图片标题 \ 图片链接
    html = etree.HTML(response.content)

    # 从当前节点获取 标签为 img 下的 alt 元素
    # alt_list = html.xpath('//div/center/img/@alt')

    # 从当前节点获取 标签为 img 下的 src 元素
    # src_list = html.xpath('//div/center/img/@src')

    # 获取a标签下的所有文本
    next_list = html.xpath('//div[@id="pages"]/a/text()')
    # 下一页URL
    next_url =  html.xpath('//div[@id="pages"]/a/@href')


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


        big_images = load_webpage_data(splice_after_url)

        html = etree.HTML(big_images)

        # 从当前节点获取 标签为 img 下的 alt 元素
        alt_list = html.xpath('//div/center/img/@alt')

        # 从当前节点获取 标签为 img 下的 src 元素
        src_list = html.xpath('//div/center/img/@src')

        '''
        zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
        我们可以使用 list() 转换来输出列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        '''
        for alt, src in zip(alt_list, src_list):

            # 文件路径名
            # fileName = f'Girls/{picture_name}'
            fileName = f'/Users/liuchuan/Desktop/Girls/{picture_name}'

            # 目录名
            dirname = f'{fileName}/{alt}.jpg'

            make_dir(fileName)

            save_images(src, dirname)


def run():
    """
    主运行函数
    :return:
    """

    for n in range(1, 35):  # 总共有34页数据, 循环获取网址

        # 1.获取所有的网址
        url = ''

        if n <= 1:
            url = 'https://www.meitulu.com/t/changtui/'
        else:
            url = 'https://www.meitulu.com/t/changtui/'+str(n)+'.html'

        # 2.根据所有网址，加载页面内容
        html = load_webpage_data(url)

        # 3.筛选数据(获取美女套图封面、链接、名称)
        Filter_data(html)


if __name__ == '__main__':

    pool = Pool(10)  # 开了10个进程，同时执行的只有3个，其它7个处于挂起状态
    pool.map(run(), [i for i in range(30)])
    pool.close()    # 关闭进程池（pool），使其不在接受新的任务。
    pool.join()     # 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。
