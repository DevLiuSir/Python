#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: DevLiuSir
# Contact: liuchuan910927@hotmail.com
# File: 01_basicSyntax.py
# Datetime: 2019/4/15 00:01
# Software: PyCharm


#注释
# Python中单行注释以 # 开头
# 多行注释可以用多个 # 号，还有 ''' 和 """：


# 第一个注释
print("This is first python programming!\n")

# 第二个注释
print ("Hello, Python!")

# 1、单引号（'''）

'''
第三注释
第四注释
'''

# 2、双引号（"""）

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""

'''
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
实例(Python 3.0+)
'''

if True:
    print ("True")
else:
    print ("False")

"""
字符串(String)

转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
"""

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""


str='ChinaHackers'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nDevLiuSir')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nDevLiuSir')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


# 导入 sys 模块

import sys

print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)