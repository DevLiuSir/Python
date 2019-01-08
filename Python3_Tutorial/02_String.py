#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: String.py
# Datetime: 2019-06-28 15:59
# Software: PyCharm


"""
字符串(String)

    字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
    创建字符串很简单，只要为变量分配一个值即可。例如：
"""


'''
python字符串格式化符号:
    符   号	描述
    %c	 格式化字符及其ASCII码
    %s	 格式化字符串
    %d	 格式化整数
    %u	 格式化无符号整型
    %o	 格式化无符号八进制数
    %x	 格式化无符号十六进制数
    %X	 格式化无符号十六进制数（大写）
    %f	 格式化浮点数字，可指定小数点后的精度
    %e	 用科学计数法格式化浮点数
    %E	 作用同%e，用科学计数法格式化浮点数
    %g	 %f和%e的简写
    %G	 %f 和 %E 的简写
    %p	 用十六进制数格式化变量的地址

'''

'''
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

'''


var1 = 'Hello World!'
var2 = "Runoob"

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""


str = 'ChinaHackers'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')
print('hello\npython')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\npython')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
print ("我叫: %s, 今年 %d 岁!" % ('小明', 10))
# 因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
# 但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().    




'''
字符串内建函数:
capitalize():   将字符串的第一个字符转换为大写.

isalnum():      方法检测字符串是否由字母和数字组成。如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
islower():      如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False.
isnumeric():    如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace():      如果字符串中只包含空白，则返回 True，否则返回 False.
lower():        转换字符串中所有大写字符为小写.
max(str):       返回字符串 str 中最大的字母。
min(str):       返回字符串 str 中最小的字母。
upper():        转换字符串中的小写字母为大写

center(width, fillchar):    返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string)):     返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    
bytes.decode(encoding="utf-8", errors="strict"):    Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
                                                    这个 bytes 对象可以由 str.encode() 来编码返回。
    
encode(encoding='UTF-8',errors='strict'):   以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

endswith(suffix, beg=0, end=len(string)):   检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.


'''

str = "the swift programming language !"
str1 = "python"
str2 = "HELLO World"
str3 = "wwdc2019"  # 字符串没有空格
print ("将字符串的第一个字母变成大写,其他字母变小写: ", str.capitalize())
print("最小字符: ", min(str1))
print("最大字符: ", max(str1))
print("转换字符串中所有小写字符为大写: ", str2.upper())
print("转换字符串中所有大写字符为小写: ", str2.lower())
print(str3.isalnum())



# ------------------------ 字符串翻转 ------------------------
# 给定一个字符串，然后将其翻转，逆序输出。

# 实例 1：使用字符串切片
str = 'Python'
print(str[::-1])

# 实例 2：使用 reversed()
print(''.join(reversed(str)))


# -------------------------- 输出格式美化 -----------------------
# str.format() 的基本使用

# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
print('{}网址： "{}!"'.format('Apple官网', 'www.apple.com'))


# 在括号中的数字, 用于指向传入对象在 format() 中的位置，如下所示：
print('{0} 和 {1}'.format('Google', 'Apple'))   # Google 和 Apple
print('{1} 和 {0}'.format('Google', 'Apple'))   # Apple 和 Google

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址：{site}'.format(name = '苹果官网', site = 'www.apple.com'))       # 苹果官网网址：www.apple.com

import math
print('常量 PI 的值近似为: {}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为: {0:.3f}。'.format(math.pi))
# 常量 PI 的值近似为 3.142。