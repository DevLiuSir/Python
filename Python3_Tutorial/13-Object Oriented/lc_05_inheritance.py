#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: Inheritance.py
# Datetime: 2018/11/3 17:16
# Software: PyCharm

# -------------- 继承 --------------


# Python同样有限的支持多继承形式。多继承的类定义形如下例: 需要注意圆括号中 父类 的顺序

# 子类拥有父类的所有属性和方法

class Animals:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


# 1.单继承示例
class Dog(Animals):

    def bark(self):
        print("汪汪叫")


# 2.多重继承
class Cat(Dog, Animals):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s飞到天上去玩耍..." % self.name)


# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.bark()

# 调用父类的方法
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

# 创建一个猫对象
cat = Cat('tom')
cat.game()


# 3.方法重写
class Parent:   # 定义父类

    def myMethod(self):
        print('调用父类方法')


class Child(Parent):    # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


'''
super(type[, object-or-type])
参数
    type -- 类。
    object-or-type -- 类，一般是 对象
'''

# super() 函数是用于调用父类(超类)的一个方法。用子类对象调用父类已被覆盖的方法
super(Child, c).myMethod()
