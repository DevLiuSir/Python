#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 06_Identity_Operators.py
# Datetime: 2019/4/15 21:11
# Software: PyCharm


'''
------------ Python身份运算符 ----------------
# 身份运算符用于比较两个对象的存储单元

is          :如果两个变量都是同一个对象，则返回true。a是b
is not      :如果两个变量都不相同，则返回true。a不是b

'''

a = 10
b = a
print("is : ", a is b)
print("is not : ", a is not b)