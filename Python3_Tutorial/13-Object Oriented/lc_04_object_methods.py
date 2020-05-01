#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Object_Methods.py
# Datetime: 2018/11/3 16:48
# Software: PyCharm


# ------------- 类的方法 --------------

# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

class People:

    # 定义基本属性
    name = ''
    age = 0
    __weight = 0     # 定义私有属性,私有属性在类外部无法直接进行访问, 下划线变量为： 私有属性

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s说: 我今年%d岁,体重%d千克。" % (self.name, self.age, self.__weight))

# 实例化类
p = People('小明', 28, 68)
p.speak()


# 8.类的专有方法：

"""
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方

"""