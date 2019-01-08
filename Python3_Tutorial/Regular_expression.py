"""
Python3 正则表达式
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
"""

'''

^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。

'''

import re

str = "Hello World"
pattern = re.findall('W..l', str)   # . 只能代替任意一个字符
print(pattern)

pattern2 = re.findall('H^^^o', str)
print(pattern2)


# re.match函数
'''
re.match 尝试从字符串的起始位置匹配一个模式，匹配成功re.match方法返回一个匹配的对象.
         如果不是起始位置匹配成功的话，match()就返回none。

函数语法：
re.match(pattern, string, flags=0)
'''

print(re.match('https', 'https://github.com/ChinaHackers').span())          # 在起始位置匹配
print(re.match('ChinaHackers', 'https://github.com/ChinaHackers'))          # 不在起始位置匹配



"""
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

# re.search方法
'''
re.search 扫描整个字符串并返回第一个成功的匹配。

函数语法：re.search(pattern, string, flags=0)

函数参数说明：
参数         描述
pattern     匹配的正则表达式
string	    要匹配的字符串。
flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

匹配成功re.search方法返回一个匹配的对象，否则返回None。
'''
# https://github.com/ChinaHackers

print(re.search('https', 'https://github.com/ChinaHackers').span())                # 在起始位置匹配
print(re.search('ChinaHackers', 'https://github.com/ChinaHackers').span())         # 不在起始位置匹配


# 检索和替换

'''
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
语法：re.sub(pattern, repl, string, count=0, flags=0)

参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
前三个为必选参数，后两个为可选参数。
'''

phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)


# compile 函数
'''
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
语法格式为：
   re.compile(pattern[, flags])
参数：
   pattern : 一个字符串形式的正则表达式
   flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
   re.I 忽略大小写
   re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
   re.M 多行模式
   re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
   re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
   re.X 为了增加可读性，忽略空格和' # '后面的注释
'''


string = 'http://i.weather.com.cn/images/cn/sjztj/2017/06/10/10204947/C8504.jpg'

regx = r'\d+'  # 定义图片正则表达式
pattern = re.compile(regx)  # 编译表达式构造匹配模式, 查找数字
images = re.findall(pattern, repr(string))  # 在页面中匹配图片链接
print(images)