#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_01_while_loop.py
# Datetime: 2018/11/3 23:11
# Software: PyCharm


# Python3 循环语句
# Python中的循环语句有 for 和 while。


'''
while 循环:Python中while语句的一般形式：

while 判断条件：
    语句
'''


count = 0
while count < 9:
    print("The count is:", count)
    count = count + 1

print("Good bye!")

# 使用了 while 来计算 1 到 100 的总和：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1-%d 的总和为: %d" % (n, sum))


'''

while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：

'''

number = 0
while number < 5:
   print (number, " 小于 5")
   number = number + 1
else:
   print (number, " 大于或等于 5")


# ------ 无限循环 --------

'''
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
'''

# flag = 1
# while (flag): print ('Python已经成为世界上最受欢迎的语言!')
# print ("Good bye!")
# 无限循环你可以使用 CTRL+C 来中断循环


# 我们可以通过设置条件表达式永远不为 false 来实现无限循环
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")
#
# # 你可以使用 CTRL+C 来退出当前的无限循环。无限循环在服务器上客户端的实时请求非常有用。
