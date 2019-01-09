#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Python_Turtle.py
# Datetime: 2019-07-03 00:19
# Software: PyCharm


import turtle   # Turtle库是Python语言中一个很流行的绘制图像的函数库
import time


'''
 绘图命令
操纵海龟绘图有着许多的命令,这些命令可以划分为3种:一种为运动命令，一种为画笔控制命令,还有一种是全局控制命令

(1)画笔运动命令:

命令	                         说明
turtle.forward(distance)   : 向当前画笔方向移动distance像素长
turtle.backward(distance)  : 向当前画笔相反方向移动distance像素长度
turtle.right(degree)	   : 顺时针移动degree°
turtle.left(degree)	       : 逆时针移动degree°
turtle.pendown()	       : 移动时绘制图形,缺省时也为绘制
turtle.goto(x,y)	       : 将画笔移动到坐标为x,y的位置
turtle.penup()	           : 移动时不绘制图形,提起笔，用于另起一个地方绘制时用
turtle.speed(speed)	       : 画笔绘制的速度范围[0,10]整数
turtle.circle()	           : 画圆,半径为正(负),表示圆心在画笔的左边(右边)画圆


(2)画笔控制命令:

命令	                              说明
turtle.pensize(width)	        : 绘制图形时的宽度
turtle.pencolor()	            : 画笔颜色
turtle.fillcolor(colorstring)	: 绘制图形的填充颜色
turtle.color(color1, color2)	: 同时设置 画笔颜色 和 填充颜色 pencolor=color1, fillcolor=color2
turtle.filling()	            : 返回当前是否在填充状态
turtle.begin_fill()	            : 图形准备开始填充
turtle.end_fill()	            : 填充完成；
turtle.hideturtle()	            : 隐藏箭头显示；
turtle.showturtle()	与 hideturtle() 函数对应


(3) 全局控制命令

命令	                说明
turtle.clear()	    : 清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()	    : 清空窗口，重置turtle状态为起始状态
turtle.undo()	    : 撤销上一个turtle动作

turtle.isvisible()	: 返回当前turtle是否可见.如果海龟显示返回 True，如果海龟隐藏返回 False。
turtle.hideturtle() : 使海龟不可见。当你绘制复杂图形时这是个好主意，因为隐藏海龟可显著加快绘制速度。
turtle.showturtle() : 使海龟可见。


stamp()	            : 复制当前图形
turtle.write(s[,font=("font-name",font_size,"font_type")]): 写文本，s为文本内容，font是字体的参数，里面分别为字体名称，
                                                            大小和类型；font为可选项, font的参数也是可选项

(4) 外观
turtle.shape(name=None)
参数
name -- 一个有效的形状名字符串
设置海龟形状为 name 指定的形状名，如未指定形状名则返回当前的形状名。
name 指定的形状名应存在于 TurtleScreen 的 shape 字典中。
多边形的形状初始时有以下几种: "arrow", "turtle", "circle", "square", "triangle", "classic"。
要了解如何处理形状请参看 Screen 方法 register_shape()。

turtle.shape('classic')
turtle.shape("turtle")

'''


'''
# 描述: 以给定半径画圆
参数:
radius(半径); 半径为正(负),表示圆心在画笔的左边(右边)画圆
extent(弧度) (optional);
steps (optional) (做半径为radius的圆的内切正多边形,多边形边数为steps)

turtle.circle(radius, extent=None, steps=None)


举例:
circle(50) # 整圆;
circle(50, steps = 3) # 三角形;
circle(120, 180) # 半圆


'''


# screensize(): 参数分别为画布的宽(单位像素), 高, 背景颜色
turtle.screensize(500, 500, "white")
turtle.speed(10)            # 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
turtle.begin_fill()         # 图形准备开始填充
turtle.color('red', 'yellow')

for _ in range(50):
    turtle.forward(200)     # 向当前画笔方向移动 200 像素长度  
    turtle.left(170)        # 逆时针移动 170°

turtle.end_fill()   # 填充完成
turtle.mainloop()   # 启动事件循环 -调用Tkinter的mainloop函数。必须是乌龟图形程序中的最后一个语句。