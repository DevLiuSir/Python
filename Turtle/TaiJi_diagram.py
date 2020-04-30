#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: TaiJi_diagram.py
# Datetime: 2019/12/22 02:21
# Software: PyCharm



# =============== 绘制太极图 ===================

import turtle as t      # 导入turtle模块, 并使用别名t



def draw_TJ_diagram(radius):
    '''
    绘制太极图
    :param radius: 圆的半径
    '''
    t.screensize(radius * 2, radius, "green")   # 画布长、宽、背景色 长宽单位为像素
    t.pensize(1)                                # 画笔宽度
    t.pencolor('black')                         # 画笔颜色
    t.speed(10)                                 # 画笔移动速度

    # 太极图填充色 1 白色 -1 黑色
    TJ_color = {1: 'white', -1: 'black'}
    color_list = [1, -1]

    # 先画半边，再画另一边
    for c in color_list:
        t.fillcolor(TJ_color.get(c))        # 获取该半边的填充色
        t.begin_fill()                      # 开始填充
        t.circle(radius / 2, 180)
        t.circle(radius, extent = 180)
        t.circle(radius / 2, -180)
        t.end_fill()                        # 结束填充 上色完成

        # 绘制该半边的鱼眼
        t.penup()                           # 提起画笔，移动不留痕
        t.goto(0, radius / 3 * c)           # 移动到该半边的鱼眼的圆上 radius/3*c 表示移动到哪边
        t.pendown()                         # 放下画笔，移动留痕
        t.fillcolor(TJ_color.get(-c))       # 获取鱼眼填充色, 与该半边相反
        t.begin_fill()
        t.circle(-radius / 6, 360)          # 半径正负, 代表逆时针和顺时针画
        t.end_fill()

        # 回到原点，为下一循环的开始做准备
        t.penup()
        t.goto(0, 0)
        t.pendown()

    draw_text(radius)



def draw_text(r):
    '''
    绘制文本
    :param r: 圆的半径
    '''
    t.penup()
    t.goto(0, -r - 50)                      # 移动到该半边的鱼眼的圆上 -r - 50 表示移动到哪边
    t.pendown()
    t.write("太极图 made by DevLiuSir", font=('Arial', 12, 'normal'))



if __name__ == '__main__':
    draw_TJ_diagram(200)
    input('Press Enter to exit...')         # 防止程序运行完成后就自动关闭窗口
