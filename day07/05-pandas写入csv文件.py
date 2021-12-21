from pandas import DataFrame
import pandas as pd

df = DataFrame(
    data={
        'name':['Tom','Jerry','joinli'],
        'age':[20,30,40],
        'hobby':['篮球','王者荣耀','英雄联盟']
    },
    index=['first','second','third']
)
# 用pandas写入到csv文件
# sep：写入的分隔符设置
# index=False 不写入索引，默认是写入的
# header=Fasle 不写入列名，默认是写入的
df.to_csv('write.csv', sep=',', index=False, header=True)

# 读取
# data = pd.read_csv('./write.csv')
# print(data)