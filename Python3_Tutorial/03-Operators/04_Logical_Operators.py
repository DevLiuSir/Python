#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 04_Logical_Operators.py
# Datetime: 2019/4/15 11:05
# Software: PyCharm

'''
------------ Python逻辑运算符 ----------------
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	    逻辑表达式	描述	实例
and:	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or:	        x or y	    布尔"或" - 如果 x 是 True，它返回 x的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not:	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''

a = 10
b = 20

if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if ( a and b ):
   print ("3 - 变量 a 和 b 都为 true")
else:
   print ("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4 - 变量 a 和 b 都不为 true")

if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")