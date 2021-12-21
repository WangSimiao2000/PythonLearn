
import pandas as pd

# 自定义列名
# names
df1 = pd.read_csv('./data/data7-1.csv', sep='|', names=['id','comments','title'])
df2 = pd.read_csv('./data/data7-2.csv', sep='|', names=['otherid','oldPrice','newPrice'])
# 合并多个表格，需要由公共的列 id
# newDf = pd.merge(df1, df2)
# print(newDf)
# print(newDf.index, newDf.columns)
# 如果列名不相同，两个df也可以合并(left_on和right_on)
# left_on 和 right_on分辨对应用于匹配的列
newDf = pd.merge(df1, df2, left_on='id', right_on='otherid')
print(newDf)
print(newDf.index, newDf.columns)