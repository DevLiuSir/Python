#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: ASCII.py
# Datetime: 2019-07-02 17:22
# Software: PyCharm


# Python 十进制转二进制、八进制、十六进制

# ASCII 进制
# 进制之间的转换

"""
bin(): 返回整数的二进制表示。
oct(): 返回整数的八进制表示。
hex(): 返回整数的十六进制表示。

"""

dec = int(input("请输入数字: "))

print("十进制数为: ", dec)

print("转换为二进制为: ", bin(dec))

print("转换成八进制为: ", oct(dec))

print("转换成十六进制为: ", hex(dec))
