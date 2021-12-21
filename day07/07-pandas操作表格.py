import  pandas as pd


#1 读取表格数据
# sheet_name : 读取某个工作薄
# sheet_name获取多个工作薄 默认是字典格式
# data = pd.read_excel('./data/3.xlsx', sheet_name=['data', 'data2'])
# print(data, type(data))
# print(data['data'])


# data = pd.read_csv('./data/data.csv')
# print(data)
# # 去除重复内容
# data = data.drop_duplicates()
# print(data)



data = pd.read_csv('./data/data2.csv')
# 使用字符串的一些方法， 替换、 去除首尾空格
# print(data, type(data))

name = data['name'].str.strip().str.replace('J','j').str.replace('n','N')
print(name, type(name))