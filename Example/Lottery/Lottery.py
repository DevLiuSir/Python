#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Lottery.py
# Datetime: 2019-09-29 22:19
# Software: PyCharm


#  --------------------------------- Python 彩票随机选号功能 -----------



# ============== 双色球 =================
#
# “双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。红色球号码从1–33中选择；蓝色球号码从1–16中选择。

import random

list_red = [x for x in range(1, 34)]           # 1~33红色球序列
red_ball = random.sample(list_red, 6)          # 随机选取6个红球
red_ball.sort()                                # 对选取的6个红球排序

blue_balll = random.randint(1, 16)             # 随机选取1个蓝球

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
