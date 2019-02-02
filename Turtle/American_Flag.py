#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: American.py
# Datetime: 2019/12/29 22:41
# Software: PyCharm


import turtle as t

# ========================  绘制美国国旗  ======================

# 绘制美国红旗
class AmericanFlag:


    def __init__(self, n):
        """
        :param n: 五星红旗的放大倍数，建议为 5 倍
        """

        # length_and_width[0]: 长度
        # length_and_width[1]: 宽度

        # 设置国旗的长和宽:
        self.length_and_width = [i * n for i in [190, 100]]

        # 条纹的宽度: 国旗的宽度的 1 / 13
        self.stripe_width = self.length_and_width[1] / 13

        # 条纹的长度: 国旗的长度
        self.stripe_Length = self.length_and_width[0]

        # 蓝色矩形的长度: 占据国旗长度比例: 2 / 5
        self.blue_rectangle_length = self.length_and_width[0] * (2 / 5)

        # 蓝色矩形宽度: 7条 红白条纹 的 宽度
        self.blue_rectangle_width = self.stripe_width * 7

        # 星的官方数据直径: K = 0.0616
        self.star_diameter = self.blue_rectangle_length * 0.0616
        # 蓝色矩形长度的 12 / 1
        self.blue_rectangle_length_12 = self.blue_rectangle_length / 12
        # 蓝色矩形宽度的 10 / 1
        self.blue_rectangle_width_10 = self.blue_rectangle_width / 10



    def even(self, n):
        '''
        确定数字是否为奇数或偶数
        :param n: 传入数字
        :return: True/False
        '''
        if n % 2 == 0:
            return True
        else:
            return False



    def draw_red_and_white_stripes(self, t, height, width, x, y):
        '''
        根据 条纹的高度 \ 宽度 和 画笔的 X \ Y，绘制红白条纹
        :param t: turtle对象
        :param height: 条纹的高度
        :param width: 宽度
        :param x: 画笔turtle的 x
        :param y: 画笔turtle的 y
        '''
        for stripe in range(13):        # 美国国旗: 7道红色横条、6道白色横条，
            if self.even(stripe):
                t.pencolor("red")
                t.fillcolor("red")      # 红色条纹
            else:
                t.pencolor("white")     # 白色条纹
                t.fillcolor("white")
            t.begin_fill()

            for side in range(2):       # 循环来回绘制条纹
                t.forward(width)
                t.left(90)
                t.forward(height)
                t.left(90)
            t.end_fill()
            y += height
            t.goto(x, y)



    def draw_blue_rectangle(self, t):
        '''
        绘制包含星星的蓝色矩形
        :param t: turtle对象
        '''
        t.setheading(0)
        t.pendown()
        t.pencolor("blue")                          # 画笔颜色
        t.fillcolor("blue")                         # 填充颜色
        t.begin_fill()
        t.forward(self.blue_rectangle_length)       # 向当前画笔方向移动 蓝色矩形的长度
        t.right(90)                                 # 顺时针移动 90°
        t.forward(self.blue_rectangle_width)        # 蓝色矩形宽度: 7条 红白条纹的宽度
        t.right(90)
        t.forward(self.blue_rectangle_length)
        t.right(90)
        t.forward(self.blue_rectangle_width)        # 向当前画笔方向移动 7条条纹的高度
        t.end_fill()



    def draw_star(self, t):
        '''
        绘制白色星星
        :param t: turtle对象
        '''
        t.setheading(36)                # 设置当前朝向为angle角度。angle为正：逆时针旋转，angle为负：顺时针旋转
        count = 0
        t.pendown()
        t.pencolor("white")
        t.begin_fill()
        t.fillcolor("white")
        while count < 5:
            t.forward(20)
            t.left(144)

            """
            # 解决画五角星没有填充
            t.forward(10)
            t.right(72)
            t.forward(10)
            t.left(144)
            """
            count += 1
        t.end_fill()


    def draw_fifty_stars(self, t, x, y):
        '''
        绘制50个星星
        :param t: turtle对象
        :param x: 星星的 x
        :param y: 星星的 y
        '''

        # 50颗白色的星： 1行6颗，共5行， 一行5颗， 共4行， 共9行

        # 星星总数: 50颗
        stars_total_num = 50

        count = 0

        # 星星数量
        stars_num = 0

        t.penup()

        while stars_num < stars_total_num:
            if count % 6 == 0:                      # 1行6颗
                # x += 40
                # y -= 25
                # x += self.star_diameter
                # y -= self.star_diameter
                x += self.blue_rectangle_length_12
                y -= self.blue_rectangle_width_10
                t.goto(x, y)
            elif count % 11 == 0:                   # 1行5颗
                # x -= 40
                # y -= 25
                # x -= self.star_diameter
                # y -= self.star_diameter
                x -= self.blue_rectangle_length_12
                y -= self.blue_rectangle_width_10
                t.goto(x, y)
                count = 0
            self.draw_star(t)
            t.setheading(0)
            t.penup()
            # t.forward(80)
            t.forward(self.blue_rectangle_length_12 * 2)
            stars_num += 1
            count += 1





    def run(self):
        '''
        主函数入口
        '''

        t.speed(0)
        t.setup(self.length_and_width[0], self.length_and_width[1])  # 设置窗口尺寸
        t.bgcolor(0, 0, 0)

        x = -self.length_and_width[0] / 2
        y = -self.length_and_width[1] / 2

        # 设置绘制标志的初始位置: 位于底部左小角
        t.goto(x, y)

        print(x, y)
        print(self.length_and_width)
        print(t.position())
        print(self.star_diameter)
        print("==================")
        print(self.blue_rectangle_width_10)
        print(self.blue_rectangle_length_12)

        self.draw_red_and_white_stripes(t, self.stripe_width, self.stripe_Length, x, y)
        self.draw_blue_rectangle(t)

        (x, y) = t.position()
        self.draw_fifty_stars(t, x, y)
        t.hideturtle()
        t.done()



if __name__ == '__main__':
    american = AmericanFlag(5)
    american.run()