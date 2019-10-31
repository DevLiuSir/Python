#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: 03_lc_modify_tuple.py
# Datetime: 2018/11/16 22:43
# Software: PyCharm


# -------- 修改元组 -------------
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.06)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup_3 = tup1 + tup2
print("tup3 = ", tup_3)


tup5 = ('Google', 'Apple', 'Microsoft', 'Amazon')

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

del tup1;
print ("删除后的元组 tup : ")
# print (tup1)


# 计算元素个数: len(tuple)
tuple1 = ('Google', 'Apple', 'Taobao')
print("元组的个数为: ",len(tuple1))

# 将列表转换为元组。tuple(seq)
list1= ['Google', 'Taobao', 'Apple', 'Baidu']
tuple1 = tuple(list1)
print("将列表转换为元组: ",tuple1)



# count(): 返回指定值出现在元组的次数。
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5))

# index(): 搜索元组以寻找指定的值，并返回其位置的位置。
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)