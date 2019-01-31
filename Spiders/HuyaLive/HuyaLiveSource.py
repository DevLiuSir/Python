#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: HuyaLiveSource.py
# Datetime: 2018/12/21 13:17
# Software: PyCharm


import requests
import re
import json

from lxml import etree

# 虎牙直播类
class HuyaLive:

    # 定义构造方法
    def __init__(self):
        self.id = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }


    def get_m3u8(self):
        '''
        获取m3u8链接, 并写入text文件
        :return:
        '''
        for id in self.id:
            # 直播间URL
            url = "https://www.huya.com/" + id
            response = requests.get(url, headers=self.headers)
            html = response.text
            # title = re.findall("<title>.*|\r\n</title>", html)[0]
            html_etree = etree.HTML(html)
            # 获取直播间名称
            title = html_etree.xpath('//h1[@id="J_roomTitle"]/text()')[0]
            title = re.sub("<title>|</title>|\r|\n", "", title)
            regex = re.compile(r"{\"status\"(.*)};")  # 匹配{}格式的内容
            strs = re.findall(regex, html)

            try:
                a = list(list(strs)[0])
                a[4] = "{"
                str = "".join(a[4:])
                str = json.loads(str)
                streamName = "/" + str['data'][0]['gameStreamInfoList'][1]['sStreamName']
                m3u8 = str['data'][0]['gameStreamInfoList'][1]['sHlsUrl']
                # flv = str['data'][0]['gameStreamInfoList'][1]['sFlvUrl']
                print(title, "\t\t\t\t", m3u8 + streamName + ".m3u8")
            except:
                print(url, "直播间没有人直播噢, 不信你去看看 网址为%s" % url)
                continue

            self.write_text(m3u8 + streamName + ".m3u8", title)



    def get_romId(self):
        '''
        获取房间 id
        '''

        # 总页面: 4页
        totalPage = 4

        for i in range(1, totalPage + 1):
            # 一起看api url
            yiqikan_Api = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2135&tagAll=0&page={i}'
            # xingshow_api = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page={i}'

            response = requests.get(yiqikan_Api, headers=self.headers).text
            html = json.loads(response)                 # 将已编码的 JSON 字符串, 解码为 Python 对象
            ids = html['data']['datas']                 # 根据 datas 的key, 取出内容
            for id in ids:                              # 遍历 ids列表内容
                self.id.append(id['profileRoom'])       # 默认id列表添加 profileRoom key的内容


    def write_text(self, m3u8, title):
        '''
        写入文本. 已追加的形式,存储筛选后的内容
        :param m3u8:  m3u8链接
        :param title: 直播房间源名称
        :return:
        '''

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
        str = '#EXTINF:0,' + title + '\n' + m3u8
        with open('/Users/liuchuan/Desktop/虎牙直播.txt', 'a+') as f:
            f.write(str + '\n')      # write: 写入本地, write 只能写入文本


if __name__ == '__main__':
    huya = HuyaLive()
    huya.get_romId()
    huya.get_m3u8()