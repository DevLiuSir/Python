#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: entrypoint.py
# Datetime: 2019/12/31 02:25
# Software: PyCharm

from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'dytt'])

# spider_cmd = 'scrapy crawl dytt8_spider -t dytt.txt'