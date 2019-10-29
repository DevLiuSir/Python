#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 01_lc_list_syntax_and_example.py
# Datetime: 2019/4/3 03:25
# Software: PyCharm

'''
Python3 列表
Python列表，列表文字用方括号[]编写。列表是Python中的一种数据结构，它是一个可变（可更改），有序的元素序列。
Python列表以','逗号分隔的括号中存储数据。它是Python中使用最频繁且功能最多的数据类型之一。
列表的数据项不需要具有相同的类型
'''


# 1.创建一个列表，只要把逗号分隔的不同的数据项, 使用方括号括起来即可
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。

thislist = ["apple", "banana", "cherry"]
print("thislist:", thislist)

# 负索引意味着从结尾开始，-1表示最后一个项目，-2表示最后一个项目等。
print(thislist[-1])

