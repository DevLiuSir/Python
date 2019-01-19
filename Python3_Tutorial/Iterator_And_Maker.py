#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Iterator_And_Maker.py
# Datetime: 2019-08-18 18:19
# Software: PyCharm


# Python3 迭代器与生成器

# ============ 迭代器 ==========

'''
迭代: Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
可以直接作用于for循环的对象统称为可迭代对象：Iterable，list、tuple、dict、set、str、Generator 等等。
'''

list = [1, 2, 3]

it = iter(list)             # 创建迭代器对象
next_element = next(it)     # 迭代器的下一个元素
print(next_element)


# 使用for循环语句, 遍历迭代器对象
# for x in it:
#     print(x, end = "")


# 也可以使用 next() 函数遍历迭代器对象

import sys  # 引入 sys 模块

# list2 = [5, 6, 7, 8, 9]
# it2 = iter(list2)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()

# 注意： 迭代器的特性：可迭代对象只能被迭代一次




# 创建一个迭代器

'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
更多内容查阅：Python3 面向对象
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
'''


class MyNumbers:
    def __iter__(self):
        self.a = 11
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# ================= 生成器 ==============

# 1、生成器的定义
# 生成器就是一个数据类型，但是这个数据类型可以自动实现迭代器协议

# 2、生成器的表达形式
# 生成器的表达形式有两种：一种是生成器函数，另一种是生成器表达式
# 2.1、生成器函数
# 在函数中使用yield语句替换return函数，当函数碰到了yield时会返回一个相应的值，并记录当前函数运行的状态，
# 在下次调用函数的时候会从当前状态运行函数；如：

def test():
    print("这是1")
    yield 1
    print("这是2")
    yield 2
    print("这是3")
    yield 3

l = test()
print(l.__next__())
print(l.__next__())
print(l.__next__())


# send()方法：
# send()方法和__next__方法实现的功能类似，都是取出生成器中的值，但send()方法需要传递一个参数，可以将该参数传递给yield并赋值给一个变量，如：

def test():
    f = yield 1
    print(f)
    yield 2

t = test()
print(t.__next__())
t.send("yield一个1")

# 练习：将一个普通循环转换为一个生成器，调用__next__不会输出结果
# xxx.send()方法可以给yield传值，但先使用了next()才可使用，或者传一个None,send(None)
# yield可以模拟多任务执行
def He(x):
    for i in range(x):
        yield (i)

pu = He(10)
pu2 = He(20)

for i in pu:
    print(i, end=' ')

print('\n')

for i in pu2:
    print(i, end=' ')

print('\n')