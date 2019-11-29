#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_03_string_formatting.py
# Datetime: 2018/11/12 23:46
# Software: PyCharm



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


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
print ("我叫: %s, 今年 %d 岁!" % ('小明', 10))

# 因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。

# 但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().



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


# ------- f-String格式化 -----------
'''
相比较占位符的方式，python3.6版本新增了 f-String 格式化的方式，
比较简单易懂，这是目前我用的最多的方式，推荐使用这种方式。
'''

name = 'jack'
age = 20
print(f'Hello, {name}. You are {age}.')

# 大写的F也适用
girls = 'rose'
print(F'Hello, {girls}.')

salary = 6.6666
print(f'{salary:.2f}')

