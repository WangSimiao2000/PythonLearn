import pandas as pd


#1导入文件
df1 = pd.read_csv('./data/data6-1.csv', sep='|')
df2 = pd.read_csv('./data/data6-2.csv', sep='|')
df3 = pd.read_csv('./data/data6-3.csv', sep='|')

# 进行拼接
# reset_index: 是重置索引
# drop = True: 把之前原来的索引index列删掉，重置索引
# drop = False: 保留原来的index作为一列，重置索引
newDf = pd.concat( [df1, df2, df3] ).reset_index(drop=True)
print(newDf)
print(type(newDf), newDf.index, newDf.columns)