#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Get_Yesterday_Date.py
# Datetime: 2019-07-02 16:59
# Software: PyCharm


# Python 获取昨天日期

# 导入 datetime 模块来获取昨天的日期：


# datetime.timedelta计算2个时间的时间差：
# datetime.timedelta支持days、seconds、microseconds

# 引入 datetime 模块
import datetime

# 例子1:
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
print(getYesterday())


# 例子2:
def getYesterday2():
        yesterday = datetime.date.today() + datetime.timedelta(-1)
        return yesterday

# 输出
print(getYesterday2())