"""

Python3 JSON 数据解析:

JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：

json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。

"""

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'ChinaHackers',
    'url': 'https://chinahackers.github.io'
}

json_str = json.dumps(data)
print("\n")
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)



# 将 JSON 对象转换为 Python 字典

data2 = json.loads(json_str)
print("\n")
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])
