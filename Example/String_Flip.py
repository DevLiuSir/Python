#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: String_Flip.py
# Datetime: 2019-07-02 17:12
# Software: PyCharm


# Python 字符串翻转
# 给定一个字符串，然后将其翻转，逆序输出。

# 实例 1：使用字符串切片
str = 'Python'
print(str[::-1])

# 实例 2：使用 reversed()
print(''.join(reversed(str)))
