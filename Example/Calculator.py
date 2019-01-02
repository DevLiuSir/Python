#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: Calculator.py
# Datetime: 2019-07-01 17:22
# Software: PyCharm


# Python 简单计算器实现

"""
简单的计算器: 包括两个数基本的加减乘除运输
"""

# 定义函数
def add(x, y):
    # 相加
    return  x + y

def subtract(x ,y):
    # 相减
    return  x - y

def multiply(x, y):
    # 相乘
    return  x * y

def divide(x, y):
    # 相除
    return x / y

# 用户输入
print("选择运算: ")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("请输入你的选择(1/2/3/4): ")

num1 = int(input("请输入第一个数字: "))
num2 = int(input("请输入第二个数字: "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":

    if num2 != 0:
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("分母不能为0")
else:
    print("非法输入")

