
from pandas import DataFrame
import pandas as pd

#1 读取data1.csv文件的数据
df = pd.read_csv('./data/data1.csv')
# print(df, type(df))
# NaN 就是一些空值
# 删除数据表中的缺失值
df = df.dropna()
print(df, type(df))

# 进行行列筛选
#loc
# print( df.loc[ 1 , 'key':'value' ] )

# iloc
print( df.iloc[ 1:3 , : ])