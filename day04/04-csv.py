# 是一个动态数据页面，请求方式是post
# 请求参数

import csv

file = open('蔬菜大全.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer(file)
csv_file.writerow(['菜品名称', '最低价', '最高价', '平均价', '产地', '单位', '发布时间'])
