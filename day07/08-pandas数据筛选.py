import pandas as pd


# 读取data4.csv的文件
data = pd.read_csv('./data/data4.csv', sep='|')

# 根据范围进行筛选
# 获取comments 大于10000的所有行
# print(  data[ data['comments'] > 10000  ]  )
# 筛选具体的范围 between(2000,  10000)
# res1 = data.comments.between(2000, 10000)
# print( data[res1] )
# 多个条件进行筛选  并且
# res2 = (data.comments >= 1000) & (data.comments <= 10000)
# print( data[res2])
# 多个条件  或
# res3 = (data.comments <= 1000)  | (data.comments >= 10000)
# print( data[res3] )
# title列 筛选空值   ~
# res4 = pd.isna(data['title'])
# print(data[  ~res4   ])
# 筛选title中包含 小米的数据
res5 = data.title.str.contains('小米', na=False)
# print(res5)
print( data[res5] )