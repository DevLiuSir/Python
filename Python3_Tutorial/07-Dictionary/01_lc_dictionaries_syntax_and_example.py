#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 01_lc_dictionaries_syntax_and_example.py
# Datetime: 2019/4/3 03:02
# Software: PyCharm


# Python3 字典

'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
'''

# d = {key1 : value1, key2 : value2 }

'''
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''

student = {
    "name": "Sam",
    "Father Name": "John",
    "class": 5,
    "Address": "171 Street 4A, Bangalore, India",
}
print(student)
