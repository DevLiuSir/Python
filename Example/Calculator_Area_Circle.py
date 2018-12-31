#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Calculator_Area_Circle.py
# Datetime: 2019-07-02 17:22
# Software: PyCharm


# Python 计算圆的面积

'''
圆的面积公式为 ：

s = πr²

公式中 r 为圆的半径。
'''


# 例子1
# 定义一个方法来计算圆的面积
def findArea(r): 
    PI = 3.142
    return PI * (r*r)
  
# 调用方法
print("圆的面积为 %.6f" % findArea(5))


# 例子2
#计算圆的面积
PI = 3.14159265
r = input("输入一个半径 r 的值：")
if r.isdigit(): # 判断是否是数字字符串
    s = PI * pow(float(r),2)
    print("半径为 {} 的圆面积为：{:.3f}".format(r,s))
else:
    print("输入错误！")
