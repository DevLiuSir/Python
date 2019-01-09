#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Triangle.py
# Datetime: 2019-08-12 18:50
# Software: PyCharm

import turtle


# --------------- 绘制等边三角形 ----------------

p = turtle

line_length = 100           # 线长 100

p.title('等边三角形')
p.penup()                   # 笔抬起
p.forward(-line_length / 2) # x轴向左移动 50， 使得图像居中
p.pendown()                 # 画笔放下

p.pensize(10)               # 画笔的粗为10

for i in range(3):          # 循环语句，循环三次
	p.forward(100)          # 向前走100默认方向为x轴正方向
	p.left(120)             # 左转120°

p.done()