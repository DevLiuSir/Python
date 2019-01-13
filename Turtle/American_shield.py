#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: American_shield.py
# Datetime: 2019-08-12 20:56
# Software: PyCharm

# ------------ 绘制美国队长 -> 盾牌-----------

import turtle
import math


def shield():
    '''
    该函数的作用是画一个美国队长的盾牌
    '''

    # 设置标题
    turtle.title('美国队长盾牌')

    # 设置画布背景
    turtle.bgcolor('#FFFFFF')

    # 设置画笔速度
    turtle.speed(10)

    # 依次填充同心圆
    fill_circle('#FF0000', 230)
    fill_circle('#FFFFFF', 178)
    fill_circle('#FF0000', 129)
    fill_circle('#0000FF', 75)

    # 绘制五角星
    draw_five('#FFFFFF', 75)

    # 以下代码，将画好的图案按指定格式保存到当前文件目录
    # windows 可以使用.jpg格式，或.ps，MAC使用eps格式，或.ps

    # turtle.getscreen()： 返回绘制着海龟的海龟屏幕对象, 获取该对象后就可以调用海龟屏幕对象的一些方法了
    ts = turtle.getscreen()

    # screen.getcanvas() | turtle.getcanvas()： 返回海龟屏幕TurtleScreen的画布对象实例
    '''
    Postscript既是一种页面描述语言，也是一种高级解释型脚本语言。由于它与设备的无关性，使得它无论在那种平台上，
    都能忠实的再现原貌，从而被广泛应用于打印出版行业，同时由于它是一种解释型脚本，所以它也可以像一般编程语言一样用来解决某些问题。
    '''
    # 保存画布，名为：shield.eps
    ts.getcanvas().postscript(file = "shield.eps")

    # 启动事件循环，必须是乌龟图形程序中的最后一个语句
    # 如果没有这个语句，代码运行完成后，窗口直接消失。
    turtle.done()


def draw_circle(radium):
    '''
    该函数的作用是画一个圆线
    :param radium：半径
    '''
    # 画笔定位到圆点（将位置和方向恢复到初始状态,位置初始坐标为（0,0））
    turtle.home()

    # 提笔
    turtle.penup()

    # 向前移动指定的半径
    turtle.forward(radium)

    # 落笔
    turtle.pendown()

    # 偏转角度
    turtle.setheading(90)

    # 画一个指定半径的圆
    turtle.circle(radium)

    # 提笔
    turtle.penup()


def fill_circle(color, r1):
    '''
    该函数的作用是，画一个圆环，有指定的填充色和半径
    :param color:颜色
    :param r1:半径
    '''
    # 设置画笔颜色
    turtle.pencolor(color)

    # 设置填充颜色
    turtle.fillcolor(color)

    # 开始填充
    turtle.begin_fill()

    # 画圆线
    draw_circle(r1)

    # 结束填充
    turtle.end_fill()

# 画并填充五角星
def draw_five(color, radium):
    '''
    该函数的作用是画一个五角星
    :param color:颜色
    :para radium:
    '''

    # 五边形内角和公式： 180 * (5 - 2)
    '''
    
    内角和公式： x = 180 * (n - 2); 公式描述：公式中n为多边形的边数。

    连接5个顶点得到一个正5边形
    由内角和公式：可知 每个角度数为 180 * (5 - 2) / 5 = 108 度
    
    180 - (180 - 108) * 2 = 36
    '''


    # 五边形度每个角度
    pentagon_degress = 180 * (5 - 2) / 5

    # 五角星的内角
    inner_degree = 180 - (180 - pentagon_degress) * 2

    # 五角星的外角
    outward_degree = 180 - inner_degree

    # 画笔定位到圆点
    turtle.home()

    # 提笔
    turtle.penup()

    # 偏转90度
    turtle.setheading(90)

    # 向前移动90个像素
    turtle.forward(radium)

    # 偏转288度. 设置当前朝向为 288 角度。
    turtle.setheading(288)

    # 落笔
    turtle.pendown()

    # radians(): 将角度转换为弧度
    # sin():返回的x弧度的正弦值。数值在 -1 到 1 之间。

    long_side = (math.sin(math.radians(36)) * radium) / math.sin(math.radians(126))

    # 设置画笔颜色
    turtle.pencolor(color)

    # 设置填充颜色
    turtle.fillcolor(color)

    # 开始填充
    turtle.begin_fill()

    for i in range(10): # 画10次线

        turtle.forward(long_side)
        if i % 2 == 0:
            turtle.left(72)
        else:
            turtle.right(outward_degree)

    # 结束填充
    turtle.end_fill()

    # 提笔
    turtle.penup()




if __name__ == '__main__':
    # 运行主函数
    shield()