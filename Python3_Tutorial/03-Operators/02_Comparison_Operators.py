#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 02_Comparison_Operators.py
# Datetime: 2019/4/15 10:50
# Software: PyCharm

'''
------------ Python比较运算符 ----------------
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True.
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。

'''

a = 10
b = 4
print("Equal : ", 10 == 4)
print("Not equal : ", 10 != 4)
print("Greater than : ", 10 > 4)
print("Less than : ", 10 < 4)
print("Greater than or equal to : ", 10 >= 4)
print("Less than or equal to: ", 10 <= 4)