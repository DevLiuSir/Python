#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 2.py
# Datetime: 2019/11/3 23:49
# Software: PyCharm


import time

print("欢迎使用BMI计算程序".center(44, "-"))

name = input("请键入您的姓名:")
height = eval(input("请键入您的身高(m):"))
weight = eval(input("请键入您的体重(kg):"))
gender = input("请键入你的性别(F/M):")

BMI = float(float(weight) / (float(height) ** 2))

if BMI <= 18.4:
    print("姓名:", name, "身体状态: 偏瘦")
elif BMI <= 23.9:
    print("姓名:", name, "身体状态: 正常")
elif BMI <= 27.9:
    print("姓名:", name, "身体状态: 超重")
else:
    print("姓名:", name, "身体状态: 肥胖")

# 格式化成2019-03-20 11:45:39形式
nowtime = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if gender == "F":
    print(f'感谢 {name} 女士, 在 {nowtime} 使用本程序, 祝您身体健康!')
elif gender == "M":
    print(f'感谢 {name} 男士, 在 {nowtime} 使用本程序, 祝您身体健康!')
