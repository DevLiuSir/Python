#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Set.py
# Datetime: 2019-06-28 17:12
# Software: PyCharm

'''
集合
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式
parame = {value01,value02,...}
或者
set(value)
'''


# 集合的基本操作
# 1、添加元素

# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

thisset = set(("Google", "FaceBook", "Taobao"))
thisset.add("Facebook")
print(thisset)


"""
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

x 可以有多个，用逗号分开。

s.update( x ) 
"""


thisset = set(("Google", "Apple", "Taobao"))
thisset.update({1,3})
print(thisset)

thisset.update([2,4],[5,6])
print(thisset)

# 2、移除元素
'''
语法格式如下：
s.remove( x )
'''
set1 = set(("Google", "Apple", "Taobao"))
set1.remove("Taobao")
print(set1)


'''
还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
s.discard( x )
'''
set2 = set(("Google", "Apple", "Microsoft", "FaceBook", "Amazon", "JD", "BaiDu"))
set2.discard("Alibaba")
print(set2)



'''
也可以设置随机删除集合中的一个元素，语法格式如下：
s.pop()
'''
x = set2.pop()
print("随机删除集合中的一个元素: ", x)

# remove()	移除指定元素
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print("移除指定元素,还剩下: ", fruits)


# 3、计算集合元素个数
'''
语法格式如下：
len(s)
'''

print("集合元素的个数: ", len(set2))

# 4、清空集合
'''
语法格式如下：
s.clear()
'''
set2.clear()


# 4、判断元素是否在集合中存在
'''
语法格式如下：
x in s
'''
print("元素是否在集合中存在: ", "FaceBook" in thisset)