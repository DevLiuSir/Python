#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: LoopStatement.py
# Datetime: 2019-03-24 23:49
# Software: PyCharm


# Python3 循环语句
# Python中的循环语句有 for 和 while。

'''

========================== while 循环 =================
Python中while语句的一般形式：

while 判断条件：
    语句
    
'''


# 使用了 while 来计算 1 到 100 的总和：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1-%d 的总和为: %d" % (n,sum))

# 无限循环
# 我们可以通过设置条件表达式永远不为 false 来实现无限循环
# var = 1
# while var == 1 :  # 表达式永远为 true
#    num = int(input("输入一个数字  :"))
#    print ("你输入的数字是: ", num)
#
# print ("Good bye!")

# 你可以使用 CTRL+C 来退出当前的无限循环。无限循环在服务器上客户端的实时请求非常有用。

'''

while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：

'''

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


'''
简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
'''

# flag = 1
# while (flag): print ('Python已经成为世界上最受欢迎的语言!')
# print ("Good bye!")

# 无限循环你可以使用 CTRL+C 来中断循环

'''

====================== for 语句 ==========================
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：
for 临时变量 in 序列:
    代码1
else:
    代码2

'''

languages = ["C", "C++", "Perl", "Python"] 
for x in languages:
    print (x)


# break 语句用于跳出当前循环体
sites = ["Baidu", "Google", "Apple", "Taobao"]

for site in sites:
    if site == "Apple":
        print("Python教程!")
        break                       # 当某个条件成立，终止此循环
    print("循环数据 " + site)
else:
    print("没有循环数据!")

print("完成循环!")



'''
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
'''
for i in range(5):
    print(i)

# 使用range指定区间的值
for i in range(5, 9):
    print(i)
 

#  结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])


# 使用range()函数来创建一个列表
list(range(5))

'''
======================== break 和 continue 语句及循环中的 else子句 ======================

break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
'''
for letter in 'Apple':     # 第一个实例
   if letter == 'A':
      break
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print ("Good bye!")

'''
============================ pass 语句 =================================
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句
'''
for letter in 'Python': 
   if letter == 'o':
      pass  # 等待键盘中断 (Ctrl+C)
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")


# 例子： 一行输出8个星， 重复打印8行
def Print_Stars():

    # 重复打印8行星
    j = 0
    while j < 8:
        # 一行星星的打印
        i = 0
        while i < 8:
            # 一行内的星星不能换行， 取消print默认结束符\n
            print('*', end='')
            i += 1
        # 每行结束要换行，这里借助一个空的print语句， 利用print默认结束符换行
        print()
        j += 1

Print_Stars()