#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: List.py
# Datetime: 2019-03-24 04:59
# Software: PyCharm


'''
Python3 列表
Python列表，列表文字用方括号[]编写。列表是Python中的一种数据结构，它是一个可变（可更改），有序的元素序列。
Python列表以','逗号分隔的括号中存储数据。它是Python中使用最频繁且功能最多的数据类型之一。
列表的数据项不需要具有相同的类型
'''


# 1.创建一个列表，只要把逗号分隔的不同的数据项, 使用方括号括起来即可
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。

thislist = ["apple", "banana", "cherry"]
print("thislist:", thislist)

# 负索引意味着从结尾开始，-1表示最后一个项目，-2表示最后一个项目等。
print(thislist[-1])

# 2.访问列表中的值
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：

list3 = ['Google', 'Runoob', 1997, 2000]
list4 = [1, 2, 3, 4, 5, 6, 7]

print("list3[0]: ", list3[0])
print("list4[1:5]: ", list4[1:5])

# 3.更新列表
# 你可以对列表的数据项进行修改或更新
list5 = ['MicroSoft', 'Google', 'Apple', 'Amazon']
print("第三个元素为: ", list5[2])

list5[2] = "Alibaba"
print("修改后的第三个元素为: ", list5[2])


# 你也可以使用append()方法来添加列表项
list5.append('Facebook')
print(list5)


# 要在指定的索引处添加项，请使用insert（）方法：
list5.insert(5, 'Intel')


# 检查项目是否存在
# 要确定列表中是否存在指定的项，请使用 in 关键字：
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No.")



# 4.删除列表元素
list8 = [1986, 2018, 1997, 2000]
print ("原始列表 : ", list8)

# 可以使用 del 语句来删除列表的的元素
del list8[2]
print("删除后的列表为:", list8)


# remove（）方法删除指定的项：
list8.remove(2000)

# pop（）方法删除指定的索引（如果未指定索引，则删除最后一项）：
list8.pop()
print(list8)


# 5.有几种方法可以在Python中连接或连接两个或多个列表。
# 最简单的方法之一是使用+运算符。
list_one = ["a", "b" , "c"]
list_two = [1, 2, 3]

list_three = list_one + list_two
print("list_three: ", list_three)

# 另一种连接两个列表的方法: 将list2中的所有项逐个追加到list1中：
for x in list_two:
    list_one.append(x)
print(list_one)



# 或者您可以使用extend（）方法，其目的是将元素从一个列表添加到另一个列表：
list_one.extend(list_two)
print(list_one)



# 6.列表函数 & 方法

# 列表元素个数
len(list8)

# 返回列表元素最大值
max(list8)

# 返回列表元素最小值
min(list8)

# 复制列表
list9 = list8.copy
print("list9: ", list9)


thislist2 = ["apple", "banana", "cherry"]
mylist = list(thislist2)
print("mylist:", mylist)

# 反向列表中元素: reverse() 函数用于反向列表中元素。
list8.reverse()
print ("列表反转后: ", list8)

# 清空列表
list8.clear()
print(list8)


'''
sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
语法
sort()方法语法：
list.sort( key=None, reverse=False)
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
'''

aList = ['Google', 'Apple', 'Taobao', 'Facebook']
aList.sort()
print("升序:", aList)

aList.sort(reverse=True)
print("降序: ", aList)
