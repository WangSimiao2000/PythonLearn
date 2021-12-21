
from pandas import DataFrame

df = DataFrame(
    data={
        'name':['Tom','Jerry','joinli'],
        'age':[20,30,40],
        'hobby':['篮球','王者荣耀','英雄联盟']
    },
    index=['first','second','third']
)
print(df,   type(df))

#2 根据列明进行筛选，单列类型是Series
# print( df['name']  , type(df['name']))
#3 切片使用
# print(  df[0:2]) #左闭右开的规则， 从0 到1
#4 进行行定位查询，
# print( df['first']  )
# print( df['first':'second']) #没有左闭右开，从哪到哪

# loc方法和iloc方法
# pandas筛选行列的主要办法就是loc和iloc方法来同时支持行列筛选
# 区别： loc 根据列名、索引名称筛选，   iloc 根据位置下标进行筛选
# loc和iloc都遵循 先行后列的原则

#5.1 行默认， 只对列进行操作
# print(   df.loc[ : , ['name'] ]   )
#5.2 行索引和列名进行同时筛选，(行索引是first到second的所有行)
# print(  df.loc[ 'first':'second' , ['age'] ]  )
# 不能根据位置筛选，只能根据行索引和列名进行筛选
# print(  df.loc[  0:2 ,  ['age'] ])
# 5.3  获取单行的内容， 列是默认所有
# print( df.loc[ 'first' ,  : ]   )
# 某行某列
print(  df.loc[ ['first', 'third']  , ['name', 'hobby'] ]   )


# iloc方法 按照位置进行筛选
# print( df.iloc[ 0:2  , 0:2  ]   )
#  找 某行，某列值
# print( df.iloc[ [0,2] , [0, 2] ]  )