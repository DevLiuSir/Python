#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: ProgressBar.py
# Datetime: 2018/11/22 14:59
# Software: PyCharm


# ================ 进度条 ===========


import time

length = 1000
for i in range(1, length + 1):
    percent = i / length
    bar = '▉' * int(i // (length / 50))
    time.sleep(0.01)
    print('\r进度条：|{:<50}|{:>7.1%}'.format(bar, percent), end='')
print('\n')