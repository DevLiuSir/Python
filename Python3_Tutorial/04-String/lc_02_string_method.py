#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_02_string_method.py
# Datetime: 2018/11/12 23:15
# Software: PyCharm


'''
---------------- 字符串内建函数 ------------------

capitalize():   将字符串的第一个字符转换为大写.
isalnum():      方法检测字符串是否由字母和数字组成。如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
islower():      如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False.
isnumeric():    如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace():      如果字符串中只包含空白，则返回 True，否则返回 False.
lower():        转换字符串中所有大写字符为小写.
max(str):       返回字符串 str 中最大的字母。
min(str):       返回字符串 str 中最小的字母。
upper():        转换字符串中的小写字母为大写
str.strip():    返回从开头和结尾删除空格的字符串

str.startswith('eyehunt'):              测试字符串是否以给定字符串开头
str.endswith('eyehunt'):                测试字符串是否以给定字符串结尾
str.replace('old', 'new'):              返回一个字符串，其中所有出现的“旧”已被“新”替换
str.find('Hello'):                      搜索给定的字符串（不是正则表达式）并返回它开始的第一个索引；-1 如果找不到，则返回
str.split('delim'):                     返回由给定分隔符分隔的子字符串列表。
str.len():                              返回字符串的长度。


center(width, fillchar):                返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string)):     返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

bytes.decode(encoding="utf-8", errors="strict"):    Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
                                                    这个 bytes 对象可以由 str.encode() 来编码返回。

encode(encoding='UTF-8',errors='strict'):   以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，
                                            除非 errors 指定的是'ignore'或者'replace'

endswith(suffix, beg=0, end=len(string)):   检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，
                                            如果是，返回 True,否则返回 False.


'''

str = "the swift programming language!"
str1 = "python"
str2 = "HELLO World"
str3 = "wwdc2019"  # 字符串没有空格
print("将字符串的第一个字母变成大写,其他字母变小写: ", str.capitalize())
print("最小字符: ", min(str1))
print("最大字符: ", max(str1))
print("转换字符串中所有小写字符为大写: ", str2.upper())
print("转换字符串中所有大写字符为小写: ", str2.lower())

print("检测字符串是否由字母和数字组成:", str3.isalnum())
print(str2.replace('HELLO', 'Bye'))
print(str2.strip())

print("!是否为字符串开头:", str.startswith('!'))
print("!是否为字符串结尾:", str.endswith('!'))
print(str.find("s"))
print(str.find("B"))

# str.split('delim'):                     返回由给定分隔符分隔的子字符串列表。
str8 = "Hello World, I am Eyehunt"
strSplit = str8.split(",")
print(str8.split(","))
print(strSplit[0])
print("str8:", str8)
print("str8 字符串的长度为: ", len(str8))
