#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_01_condition_control.py
# Datetime: 2018/11/3 23:39
# Software: PyCharm


# Python3 条件控制

'''
    Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
'''

# if 语句
# Python中if语句的一般形式如下所示：

'''
if  条件1:
      语句1
elif 条件2:
      语句2
else:
     语句3
'''

# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

'''
注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
'''

age = int(input("请输入年龄: "))
if age <= 2:
    print('婴儿')
elif age <= 5:
    print('幼儿')
elif age <= 12:
    print('儿童')
elif age <= 18:
    print('少年')
elif age <= 40:
    print('青年')
elif age <= 59:
    print('中年')
else:
    print('老年')

# ------ if 嵌套 --------
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")
