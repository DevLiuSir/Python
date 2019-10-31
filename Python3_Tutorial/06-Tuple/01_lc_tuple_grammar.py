#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 01_lc_tuple_grammar.py
# Datetime: 2018/11/16 21:53
# Software: PyCharm



# ---------- Python3 元组 ---------

'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

'''

tup1 = ('Google', 'Apple', 'Microsoft', 'Amazon')
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"    #  不需要括号也可以
print(type(tup3))


# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup4 = (100)
print(type(tup4))           # 不加逗号，类型为整型

tup5 = (100,)
print(type(tup5))           # 加上逗号，类型为元组

# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等
