#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 05_Membership_Operators.py
# Datetime: 2019/4/15 11:09
# Software: PyCharm


'''
------------ Python成员运算符 ----------------

运算符	        描述	                                            实例
in	            如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	        如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

'''

colorList = ["red", "yellow", "black"]

print("red" in colorList)
print("orange" in colorList)
print("red" not in colorList)
