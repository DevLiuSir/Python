#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Calculate_Month_Days.py
# Datetime: 2019-07-02 17:43
# Software: PyCharm


# Python 计算每个月天数

# 以下代码通过导入 calendar 模块来计算每个月的天数：

import calendar

monthRange = calendar.monthrange(2019, 7)

print(monthRange)

'''
    输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
'''

print(calendar.mdays[12])

print("每个月的天数: %s," % calendar.mdays)

