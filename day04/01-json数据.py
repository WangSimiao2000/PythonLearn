"""
json数据
    轻量级的数据交互方式
    跟python中的字典格式类似

    json数据是双引号,单引号不行

"""

import json

json_1 = '{"name":"尼古拉斯·赵四"}'
print(json_1)
print(type(json_1))

# json转化成字典格式
data = json.loads(json_1)
print(data)
print(type(data))

# json数据是单引号的情况
# json_2 = "{'name':'法外狂徒·张三'}"
# print(json_2)
# print(type(json_2))
# data2 = json.loads(json_2)
# print(data2)

# 转化成json数据
dict_1 = {"name":"尼古拉斯·赵四"}
res1 = json.dumps(dict_1,ensure_ascii=False)
print(res1)
print(type(res1))

dict_2 = {'name':'法外狂徒·张三'}
res2 = json.dumps(dict_2,ensure_ascii=False)
print(res2)
print(type(res2))
