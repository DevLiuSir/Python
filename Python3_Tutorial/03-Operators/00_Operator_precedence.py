#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 00_Operator_precedence.py
# Datetime: 2019/4/15 11:23
# Software: PyCharm

'''
------------ Python运算符优先级 ----------------
以下是从最高到最低优先级的所有运算符：
**                          :	指数 (最高优先级)
~ + -	                    :   按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //                    :	乘，除，取模和取整除
+ -	                        :   加法减法
>> <<	                    :   右移，左移运算符
&	                        :   位 'AND'
^ |	                        :   位运算符
<= < > >=	                :   比较运算符
<> == !=	                :   等于运算符
= %= /= //= -= += *= **=    :   赋值运算符
is is not	                :   身份运算符
in not in	                :   成员运算符
not or and	                :   逻辑运算符
'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)

e = (a + b) * (c / d)    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)

e = a + (b * c) / d      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)