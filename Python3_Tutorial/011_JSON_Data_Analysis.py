#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: liuchuan
# File: JSON_Data_Analysis.py
# Datetime: 2019-07-02 16:31
# Software: PyCharm

# Python3 JSON 数据解析

'''
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：

json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。

'''

"""
Python 编码为 JSON 类型转换对应表：
Python	                                JSON
dict	                                object
list, tuple	                            array
str	                                    string
int, float, int- & float-derived Enums	number
True	                                true
False	                                false
None	                                null
"""
# ---------------------------------------
"""
JSON 解码为 Python 类型转换对应表：
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1) # 对数据进行编码。
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str) # 对数据进行解码。
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])


# 通过输出的结果可以看出，简单类型通过编码后跟其原始的 repr() 输出结果非常相似。

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：


# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data1, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
