#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Dictionary.py
# Datetime: 2019-03-24 23:14
# Software: PyCharm


# Python3 字典

'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
'''

# d = {key1 : value1, key2 : value2 }

'''
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''

# 一个简单的字典实例：
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# 也可如此创建字典：
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }


# 访问字典里的值
# 把相应的键放入到方括号中
dict = {'Name': 'ChinaHackers', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict = {'Name': 'ChinaHackers', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;               # 更新 Age
dict['School'] = "qinghua"     # 添加信息
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


# 字典内置函数&方法

# len(dict): 计算字典元素个数，即键的总数。
len(dict)

# str(dict): 输出字典，以可打印的字符串表示
dict = {'Name': 'Tim cook', 'Age': 57, 'Class': 'First'}
str(dict)

# type(variable): 返回输入的变量类型，如果变量是字典就返回字典类型。
type(dict)



# dict.clear():删除字典内所有元素
dict = {'Name': 'Zara', 'Age': 7}
print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))


# dict.copy(): 返回一个字典的浅复制
dict1 =  {'user':'runoob','num':[1,2,3]}

# dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1)
print(dict2)
print(dict3)   # dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
