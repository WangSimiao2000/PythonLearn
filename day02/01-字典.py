"""
字典
    特殊的容器
    {key: value , key: value
    key是唯一的
    value可以储存为任意类型

"""

# 创建字典
dict_1 = dict()

# 创建字典二

dict_2 = {}

dict_3 = {"name": "小鲁班", "武器": "大炮", 100: [1, 2, 3]}

print(dict_3)

# 查找  可以把这个key当成索引下标
print(dict_3["name"])
# print(dict_3["hobby"])  # 如果字典中没有这个Key，查找会报错

# 更改  先确定在字典中有这个key，再赋值就是更改键值对
dict_3[100] = '123'
print(dict_3)

# 添加  在字典中没有这个key，再赋值就是添加键值对
dict_3['hobby'] = '上王者'  # 会产生一个新的key
print(dict_3)

# 删除  根据key来进行定位删除
del dict_3[100]
# dict_3.clear()
print(dict_3)

# 获取所有的key
# print(dict_3.keys())  # 返回的是一个列表
res = dict_3.keys()
res = list(res)
print(res)
print(res[0])

# 获取所有的value
all_value = dict_3.values()
print(type(all_value))
print(all_value)

# 获取所有的key和value
all_item = dict_3.items()
print(all_item)
