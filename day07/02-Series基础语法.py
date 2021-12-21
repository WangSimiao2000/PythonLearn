
"""

自定义series对象
"""
from pandas import Series

#data: series的数据
#index： 数据对应的索引，可以自定义，当然也可以重复，但是不建议重复
# 索引如果不指定，默认会从0，1，2，3....一直类推 自己创建
one = Series(
    data=['尼古拉斯·赵四','法外狂徒·张三','爱新觉罗·王五'],
    # index=['a','b','c']
)
# print(one, type(one))

#2 传入列表中的字典元素 生成series对象
two = Series(
    data=[
        {'name':'法外狂徒','age':30,'nickname':'张三'},
        {'name':'法外狂徒','age':30,'nickname':'张三'},
    ]
)
# print(two, type(two))

# 3 d直接给data赋值字典，索引就是key，value是数据
thire = Series(
    data={
        'name':'张三','age':30,'nickname':'法外狂徒'
    }
)
print(thire, type(thire))

#4 根据索引查询对应的数据
# print( thire['name'] )
# print( thire['name' : 'age'] , type(thire))

#5 添加数据, 添加Series对象
four = thire.append(  Series(data=['伊丽莎白·翠花'], index=['a'])   )
# print(four,  type(four))

#6 根据索引删除
four = four.drop('age')
print(four)

#7 获取所有的索引和数值
print(  four.index,  four.values)