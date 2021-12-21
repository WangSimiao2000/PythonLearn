
import pandas as pd

# 乘积操作
df = pd.read_csv('./data/data8.csv', sep='|')
res = df.price * df.num
print(res)
# 添加列
df['result'] = res
print(df, type(df))