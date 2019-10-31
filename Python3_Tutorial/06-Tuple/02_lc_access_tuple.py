#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 02_lc_access_tuple.py
# Datetime: 2018/11/16 22:07
# Software: PyCharm


# ------------ 访问元组 ---------

# 元组可以使用下标索引来访问元组中的值
tup1 = ('Google', 'Apple', 'Microsoft', 'Amazon')
print(tup1[1])


# 负索引
# 负索引: 是指从头开始，-1指的是最后一项，-2指的是倒数第二项， 依此类推。
print(tup1[-1])