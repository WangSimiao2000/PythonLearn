from pandas import DataFrame


a = [
    ['a','b','c','d'],
    ['e','f','g','h']
]
# 针对二维列表 写入到DataFrame中会自动创建 列名和索引名  都是从0开始

b = [
    {'name':'Tom','age':20, 'hobby':'玩篮球'},
    {'name':'Jerry','age':30, 'hobby':'王者荣耀'}
]
# 传入列表包含的字典内容， 字典中的key就是列名，key对应的值就是列对应的数据

df = DataFrame( b )
print(df)