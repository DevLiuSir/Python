#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: read_and_write_json.py
# Datetime: 2019/12/25 04:19
# Software: PyCharm


import requests
import json



def write_to_local_json(html, path):
    '''
    根据URL返回的数据, 和用户提供的路径，写入本地json文件
    :param html: URL
    :param path: 写入路径
    :return: json
    '''
    r = requests.get(html)
    with open(path, 'w+') as f:
        json.dump(r.json(), f, ensure_ascii=False)
        print('写入本地完成 ！！！  ')
    return r.json()




def read_to_local_json(path):
    '''
    读取本地json文件
    :param path: 路径
    :return:
    '''
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == '__main__':

    url = 'http://yingshi.m.jinerkan.com/v3/api/tags'

    dirname = '/Users/liuchuan/Desktop/test.json'

    write_to_local_json(url, dirname)

    j = read_to_local_json(dirname)

    print(j)
