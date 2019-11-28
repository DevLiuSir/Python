#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: lc_02_for_loop.py
# Datetime: 2018/11/3 23:20
# Software: PyCharm


'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)


# break 语句用于跳出当前循环体
sites = ["Baidu", "Google","Apple","Taobao"]
for site in sites:
    if site == "Apple":
        print("Python教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
range()函数
如果你需要遍历数字序列，其默认值 从0开始， 可以使用内置range()函数。它会生成数列
'''
for i in range(3):
    print(i)

print("==============")

# 使用range指定区间的值
for i in range(6, 9):
    print(i)

#  结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 使用range()函数来创建一个列表
list(range(5))

'''
break和continue语句及循环中的else子句
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
'''
for letter in 'Apple':  # 第一个实例
    if letter == 'A':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

'''
pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句
'''
for letter in 'Python':
    if letter == 'o':
        pass    # 等待键盘中断 (Ctrl+C)
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
