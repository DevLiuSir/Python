#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: List.py
# Datetime: 2019-03-24 04:59
# Software: PyCharm


'''
Python3 列表
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。

序列都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型
'''


# 1.创建一个列表，只要把逗号分隔的不同的数据项, 使用方括号括起来即可
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
list1 = ['Google', 'Apple', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]


# 2.访问列表中的值
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：

list3 = ['Google', 'Runoob', 1997, 2000]
list4 = [1, 2, 3, 4, 5, 6, 7]

print("list3[0]: ", list3[0])
print("list4[1:5]: ", list4[1:5])

# 3.更新列表
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
list5 = ['MicroSoft', 'Google', 'Apple', 'Amazon']
print("第三个元素为: ", list5[2])
list5[2] = "Alibaba"
print("修改后的第三个元素为: ", list5[2])
print(list5)

# 4.删除列表元素
# 可以使用 del 语句来删除列表的的元素
list8 = [1986, 2018, 1997, 2000]
print ("原始列表 : ", list8)
del list8[2]
print("删除后的列表为:", list8)

# 5.列表函数 & 方法

# 列表元素个数
len(list8)

# 返回列表元素最大值
max(list8)

# 返回列表元素最小值
min(list8)

# 复制列表
list9 = list8.copy
print("list9: ", list9)

# 反向列表中元素: reverse() 函数用于反向列表中元素。
list8.reverse()
print ("列表反转后: ", list8)

# 清空列表
list8.clear()
print(list8)