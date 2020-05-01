#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Errors_and_exceptions.py
# Datetime: 2019-08-17 02:50
# Software: PyCharm


# Python3 错误和异常

'''
作为 Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
Python 有两种错误很容易辨认：语法错误和异常。
语法错误
Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例
while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax

这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号（:）。

语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

'''

'''
try语句按照如下方式工作；
首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
'''


# 错误 error
# 异常 exception
try :
    num = int(input('Please input number:'))
    result = 1 / num
    print(result)
except ZeroDivisionError as error:  # 不能被0整除(输入0时,打印的错误信息)
    print(error)
except ValueError as error:         # 类型错误(输入非数字时,打印的错误信息)
    print(error)


'''
try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

else 子句将在 try 子句没有发生任何异常的时候执行。

'''


# 以下实例在 try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句，读取文件内容：

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。