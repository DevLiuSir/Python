#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: ChineseFlag.py
# Datetime: 2019/01/29 00:55
# Software: PyCharm


# ====================== 绘制五星红旗 =================

import turtle as t                  # 导入turtle模块, 并使用别名t
from math import pi, cos, atan      # 导入math模块


# 五星红旗
class ChineseFlag:

    def __init__(self, n):
        """
        :param n: 五星红旗的放大倍数，建议为 20倍
        """
        # 设置红旗的长和宽
        self.long_width = [i * n for i in [30, 20]]

        # 设置原点的调整位移
        self.x_y = [i * n for i in [-15, 10]]

        # 设置五个星星的外切圆边长
        self.r = [i * n for i in [3, 1, 1, 1, 1]]

        # 设置五个星星的中心点
        self.center = [i * n for j in [(5, -5), (10, -2), (12, -4), (12, -7), (10, -9)] for i in j]

        # 设置五个星星的调整角度
        self.rotation = [0,
                         -(atan(3 / 5) / pi * 180 + 18),
                         atan(3 / 5) / pi * 180 - atan(1 / 6) / pi * 180,
                         atan(1 / 6) / pi * 180 + atan(2 / 7) / pi * 180,
                         atan(4 / 5) / pi * 180 - atan(2 / 7) / pi * 180]


    def draw_starts(self, r, x, y, rotation):
        """
        绘制五角星
        :param r: 包围五角星的圆的半径
        :param x: 五角星的横坐标
        :param y: 五角星的纵坐标
        :param rotation: 调整五角星的角度
        """
        # 由圆的半径求五角星边长
        c = (2 * r ** 2 - 2 * r ** 2 * cos((144 / 180) * pi)) ** (1 / 2)
        t.pu()            # turtle.penup() 别名turtle.pu()　　　画笔抬起，不留下痕迹
        t.goto(x, y)
        t.right(rotation)
        t.left(162)
        t.forward(r)
        t.right(162)
        t.pd()             # turtle.pendown() 别名turtle.pd()　　画笔落下，留下痕迹
        print(f'五角星的圆的半径: {r}')

        # 填充黄色
        color = (232 / 255, 255 / 255, 8 / 255)
        t.pencolor(color)
        t.begin_fill()
        t.fillcolor(color)
        for i in range(5):
            t.forward(r)  # 向前走75默认方向为x轴正方向
            t.left(72)  # 左转 72度
            t.forward(r)
            t.right(180 - 36)
        t.end_fill()



    def draw_flag_face(self, long, width):
        '''
        绘制国旗旗面, 并填充红色
        :param long: 长
        :param width: 宽
        '''
        color = (226 / 255, 2 / 255, 18 / 255)  # 红色填充
        t.speed(1)
        t.pencolor(color)                       # 画笔颜色
        t.begin_fill()                          # 开始绘制
        t.fillcolor(color)
        for i in range(2):
            t.forward(long)     # 向当前画笔方向移动 long 像素长度
            t.right(90)         # 顺时针移动 90°
            t.forward(width)    # 向当前画笔方向移动 width 像素长度
            t.right(90)         # 继续顺时针移动 90°, 形成一个长方形.
        t.end_fill()

    def main(self):
        t.speed(0)      # 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快
        t.hideturtle()  # 隐藏龟图标
        t.showturtle()
        t.penup()
        t.goto(self.x_y[0], self.x_y[1])    # 指从当前的点, 指向 括号内 所给坐标
        t.pendown()

        self.draw_flag_face(self.long_width[0], self.long_width[1])

        for i in range(5):
            self.draw_starts(self.r[i],
                             self.center[i * 2] + self.x_y[0],
                             self.center[i * 2 + 1] + self.x_y[1],
                             self.rotation[i])
        t.done()


if __name__ == "__main__":
    flag = ChineseFlag(20)
    flag.main()
