#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Initialization_method.py
# Datetime: 2018/11/3 16:39
# Software: PyCharm


# ----------- 初始化方法 -----------

# 创建一个名为Person的类，使用__init __（）函数为名称和年龄分配值：
class Person:

    # __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 26)
print(p1.name)
print(p1.age)

# 注意：使用类名（）创建对象的时候，会自动调用初始化方法 __init__()