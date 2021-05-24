#!/usr/bin/env python3


'''
枚举类的使用: Python 提供了 Enum 类来实现这个功能
Enum 的成员均为单例（Singleton），并且不可实例化，不可更改
'''

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型: 通过 __members__ 遍历它的所有成员的方法
for name, member in Month.__members__.items():
	
	# member.value 是自动赋给成员的 int 类型的常量，默认是从 1 开始的
	print(name, '---------', member, '----------', member.value)
	
# 直接引用一个常量
print('\n', Month.Jan)


# ****** 自定义类型的枚举 ********

# 但有些时候我们需要控制枚举的类型，那么我们可以 Enum 派生出自定义类来满足这种需要。通过修改上面的例子：

Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
	Jan = 'January'
	Feb = 'February'
	Mar = 'March'
	Apr = 'April'
	May = 'May'
	Jun = 'June'
	Jul = 'July'
	Aug = 'August'
	Sep = 'September '
	Oct = 'October'
	Nov = 'November'
	Dec = 'December'
	
	
if __name__ == '__main__':
	
	print(Month.Jan, '----------',
			Month.Jan.name, '----------', Month.Jan.value)
	for name, member in Month.__members__.items():
		print(name, '----------', member, '----------', member.value)