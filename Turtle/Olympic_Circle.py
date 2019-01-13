#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Olympic_Circle.py
# Datetime: 2019-08-12 18:27
# Software: PyCharm

# 导入模块并指定别名
import turtle as t

# ********** 绘制奥运五环 ***********

t.title('奥运五环')
t.shape('turtle')  # 设置画笔样式《设置海龟形状》：海龟  "arrow", "turtle", "circle", "square", "triangle", "classic"。
t.showturtle()     # 使海龟可见

t.speed(10)        # 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
t.width(5)         # 确定圆圈的宽度
t.color("blue")    # 确定圆圈的颜色
t.circle(60)       # 确定圆的半径

t.penup()          # 笔抬起
t.forward(140)     # 向当前画笔方向移动 140 像素长度
t.pendown()        # 笔放下
t.color("black")
t.circle(60)

t.penup()
t.forward(140)
t.pendown()
t.color("red")
t.circle(60)

t.penup()
t.goto(210, -50)
t.pendown()
t.color("green")
t.circle(60)

t.penup()
t.goto(60, -50)
t.pendown()
t.color("orange")
t.circle(60)
t.done()
