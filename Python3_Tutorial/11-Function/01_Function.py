#!/usr/bin/python
# -*-coding:utf-8 -*-
#Author: ChinaHackers

'''
Python 函数:

# 函数代码块以 ( def ) 关键词开头，后接函数标识符名称和圆括号()。
# 函数内容以冒号起始，并且缩进
语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
'''

# 定义函数
def hello():
   print("Hello World!")
 
hello()

#函数中带上参数变量:
# 计算面积函数
def area(width, height):
    return width * height
 # 打印字符串
def print_welcome(name):
    print("Welcome to ", name)
 
print_welcome("China")
w = 4
h = 5

print("width = %d" %w)
print("height = %d" %h)
print("area = %d" %area(w, h))

#传可变对象实例
#可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：

# 可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo(age = 50, name = "runoob" )
print ("------------------------")
printinfo(name="runoob" )

# return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：

# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)


# 全局变量 和 局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

total2 = 0 # 这是一个全局变量
# 可写函数说明
def sum2( arg1, arg2 ):
    #返回2个参数的和."
    total2 = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum2( 10, 20 )
print ("函数外是全局变量 : ", total2)



# global 和 nonlocal 关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

# 以下实例修改全局变量 num：

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)  # num = 1
    num = 123
    print(num)  # num = 123
fun1()
print(num)     # num因为已被修改，所以等于 123



# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要（ nonlocal ）关键字了，如下实例：

def outer():
    number = 10
    def inner():
        nonlocal number   # nonlocal关键字声明
        number = 100
        print(number)     # 100
    inner()
    print(number)         # 100
outer()


# 加了星号 * 的参数, 会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def greetPerson(* name):
    print('Hello', name)
  
greetPerson('Runoob', 'Google')

