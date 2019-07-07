#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Lottery.py
# Datetime: 2019-09-29 22:19
# Software: PyCharm


import random

'''
random.random():    函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。

random.uniform():   正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。

random.randint():   随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值，python random.randint。

random.choice():    可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。

random.shuffle():   如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。

random.sample():    可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
'''



#  --------------------------------- Python 彩票随机选号功能 ----------------------------



# ============== 双色球 =================
#
# “双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。红色球号码从1–33中选择；蓝色球号码从1–16中选择。

list_red = [x for x in range(1, 34)]           # 1~33红色球序列
red_ball = random.sample(list_red, 6)          # 随机选取6个红球
red_ball.sort()                                # 对选取的6个红球排序

blue_balll = random.randint(1, 16)             # 随机选取1-16中, 任意1个蓝球

# red_ball.append(blue_balll)

print('双色球:', red_ball, end=' + ')
print(blue_balll)


# =============== 大乐透 =====================
#
# “大乐透”的玩法是“35选5加12选2”，也就是前面35个数字选5个，后面12个数字选2个。
import random

list_red = [x for x in range(1, 36)]        # 1~35红色球序列
list_blue = [x for x in range(1, 13)]       # 1~12蓝色球序列

res_red = random.sample(list_red, 5)        # 随机选取5个红球
res_blue = random.sample(list_blue, 2)      # 随机选取2个红球

res_red.sort()                              # 对选取的5个红球排序
res_blue.sort()                             # 对选取的2个蓝球排序

res = res_red
print(r'大乐透:', res, end=' + ')
print(res_blue)



# ================ 福彩3D ================
# 百位
hundreds = [x for x in range(0, 9)]
# 十位
tens = [x for x in range(0, 9)]
# 个位
ones_unit = [x for x in range(0, 9)]

res_hundreds = random.sample(hundreds, 1)       # 0-9随机取1个红球，百位
res_tens = random.sample(tens, 1)               # 0-9随机取1个红球，十位
res_ones_unit = random.sample(ones_unit, 1)     # 0-9随机取1个红球，个位

lis = res_hundreds + res_tens + res_ones_unit
print(f'福彩3D: {lis}')
