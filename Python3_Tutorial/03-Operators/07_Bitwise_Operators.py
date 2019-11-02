#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 07_Bitwise_Operators.py
# Datetime: 2019/4/15 11:15
# Software: PyCharm

'''
------------ Python位运算符 ----------------

按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13。

&:  按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0。
    (a & b) 输出结果 12 ，二进制解释： 0000 1100

|:  按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
    (a | b) 输出结果 61 ，二进制解释： 0011 1101


^:	按位异或运算符：当两对应的二进位相异时，结果为1。
	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001


<<:	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
	a << 2 输出结果 240 ，二进制解释： 1111 0000

>>:	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数。
	a >> 2 输出结果 15 ，二进制解释： 0000 1111

'''

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b         # 12 = 0000 1100
print ("1 - c 的值为：", c)

c = a | b         # 61 = 0011 1101
print ("2 - c 的值为：", c)

c = a ^ b         # 49 = 0011 0001
print ("3 - c 的值为：", c)

c = ~a            # -61 = 1100 0011
print ("4 - c 的值为：", c)

c = a << 2        # 240 = 1111 0000
print ("5 - c 的值为：", c)

c = a >> 2        # 15 = 0000 1111
print ("6 - c 的值为：", c)