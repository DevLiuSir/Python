#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 03_Assignment_Operators.py
# Datetime: 2019/4/15 10:58
# Software: PyCharm


'''
------------ Python赋值运算符 ----------------
运算符	描述	        实例
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	    c += a 等效于 c = c + a
-=	减法赋值运算符	    c -= a 等效于 c = c - a
*=	乘法赋值运算符	    c *= a 等效于 c = c * a
/=	除法赋值运算符	    c /= a 等效于 c = c / a
%=	取模赋值运算符	    c %= a 等效于 c = c % a
**=	幂赋值运算符	    c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''


a = 5
b = a
print("Assigns - value of b : ", b)

b += a
print("Add AND - value of b : ", b)

b -= a
print("Subtract AND - value of b : ", b)

b *= a
print("Multiply AND - value of b : ", b)

b /= a
print("Divide AND - value of b : ", b)

b %= a
print("Module AND - value of b : ", b)

b **= a
print("Exponent AND - value of b : ", b)

b //= a
print("Floor Division AND - value of b : ", b)