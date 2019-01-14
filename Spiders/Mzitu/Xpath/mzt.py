#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: mzt.py
# Datetime: 2019-07-13 20:49
# Software: PyCharm


import requests
from lxml import etree


# 基础url
baseUrl = "https://www.mzitu.com/tag/ugirls/"

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    "Referer": "https://www.mzitu.com/tag/ugirls/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


# 获取美女图片函数
def getGirlsImages():

    # 1. 请求妹子图拿到HTML数据
    response = requests.get(url=baseUrl, headers=header)

    # 2. 抽取想要的数据: 图片标题 \ 图片链接
    html = etree.HTML(response.text)

    # 从当前节点获取 标签为 img,且类属性为 lazy 的所有标签下的 alt元素
    alt_list = html.xpath('//img[@class="lazy"]/@alt')

    # 从当前节点获取 标签为 img,且类属性为 lazy 的所有标签下的 data-original 元素
    src_list = html.xpath('//img[@class="lazy"]/@data-original')

    '''
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
    我们可以使用 list() 转换来输出列表。
    如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
    '''
    for alt, src in zip(alt_list, src_list):

        # 3. 下载图片
        response = requests.get(src, headers=header)

        name = alt + ".jpg"

        # 4. 保存图片
        fileName = 'GirlsPicture/{}'.format(name)

        print("[INFO]: 保存图片文件: %s" % fileName)

        with open(fileName, "wb") as f:
            f.write(response.content)
            f.close()



if __name__ == '__main__':

    getGirlsImages()