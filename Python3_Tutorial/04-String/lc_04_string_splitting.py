#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_04_string_splitting.py
# Datetime: 2018/11/13 00:01
# Software: PyCharm


# --------- 字符串切片 -----------

'''
句法
这是简单的Python Substring语法。

string[start:end]：获取从索引开头  到  结尾-1的所有字符

string[:end]：获取从字符串开头到结尾1的所有字符

string[start:]：获取从索引  开头  到字符串结尾的所有字符

'''


"""
list[P1:P2:P3]
　　　　 两个冒号分隔开三个参数，P1(切片开始的位置)，P2(切片结束的位置+1)，P3（步长默认为 1，可以省略不写，步长也可以为负）
        正序：从前到后下标为 0 1 2 3 ...
        倒序：从后到前下标为 -1 -2 -3 -4 ...
"""



str = "Hello, World!"
print(str)
print(str[0])              # 输出字符串第一个字符
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print(str[2:5:2])



# 负索引: 子字符串
'''
在python中，还支持负索引。如果您通过-1索引，则最后一个字符将得到。如果为负– 2，-3，...。那么倒数第二，倒数第三...等等。
'''

print(str[-2:5:-2])


print("获取字符串的最后一个字符:", str[-1])  # 在索引中传递-1，这是一个负索引
# 最后一个字符
l = len(str)
print("最后一个字符:", str[l - 1])

print("str[0:3]", str[0:3])             # 获取字符串的前3个字符, 0可以省略
print("str[:3]", str[:3])
print("str[1:3]", str[1:3])
print("str[-1]", str[-1])
print("str[-2:]", str[-2:])
print("str[-2:-1]", str[-2:-1])

print(str[::3])
