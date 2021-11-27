"""
元组
    常用的存储单元
    ()  <class 'tuple'>

    特点
        元组内的元素是不可以改变的


"""
#创建  方法一
tuple_1 = tuple()
print(tuple_1)
print(type(tuple_1))
# 创建方法二
tuple_2 = ()
print(tuple_2)
print(type(tuple_2))


tuple_3 = ('貂蝉','杨玉环','王昭君','西施')
# 查找
print(tuple_3[0])
print( tuple_3[0:3]) # 元组范围提取，返回的也是元组类型

# 再当前这个元组中 是不能更改、删除、添加


# 转换类型
# 元组转化成列表
list_1 = list(tuple_3)
print(list_1)
list_1.append('妲己')
print(list_1)
# 列表转化成元组
tuple_3 = tuple(list_1)
print(tuple_3)


# 进行拼接
tuple_3 += ('唐伯虎',)
# tuple_3 = tuple_3 + ()
print(tuple_3)

# res = ('唐伯虎',)  #再只有一个元素的时候，后面要加一个英文逗号
# print(res)
# print( type(res) )