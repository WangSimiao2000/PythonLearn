"""
列表
    <class 'list'>
    使用[]来表示/标识
    常用的存储单元
        增删改查的操作


"""
# 创建列表方法
list_1 = list()
print(list_1)
print(type(list_1))
# 创建列表方法二
list_2 = []
print(list_2)
print(type(list_2))

# 创建一个有内容的列表
list_3 = ['女娲', '吕德华', '瑶瑶', '奕星', '芈月']
# 查看元素个数len()
# print(len(list_3))

# 查找：
print(list_3[1])
print(list_3[-2:])  # 列表进行范围提取，返回的还是列表

# 更改更改元素 先定位查找到这个位置，在重新赋值
list_3[1] = '吕布'
print(list_3)
# 批量更改
list_3[0:2] = ['李白', '王昭君']
print(list_3)
list_3[0:2] = '李'
print(list_3)

# 添加元素
# 1、 append(需要添加的元素)  # 只添加到最后一位
list_3.append('孙悟空')
list_3.append(1000)
list_3.append(3.14159)
list_3.append(True)
list_3.append([1, 2, 3])
print(list_3)
# 2、insert(添加的位置,添加的元素)  # 可以在任意位置添加
list_3.insert(1, '钟馗')
print(list_3)
# 3、extend(需要填入可迭代内容)  # 同时添加多个元素
list_4 = [[], 123, True]
list_3.extend(list_4)
print(list_3)
# 4、拼接
list_3 += ['马可波罗', '鲁班', '伽罗']
print(list_3)

# 删除元素
# remove(需要删除的元素)
list_3.remove('李')
print(list_3)
# del
# del list_3 默认删除整个列表，内存中将不存在list_3变量名
del list_3[-6]
print(list_3)
# clear()
list_3.clear()
print(list_3)

# 排序
list_5 = [4, 7, 6, 9, 8, 5, 2, 1, 3]
# sort方法
# 数字根据大小进行排序
list_5.sort()  # 默认从小到大排列list_5.sort(reverse=False)
print(list_5)
list_5.sort(reverse=True)  # 从大到小排列
print(list_5)
list_5.reverse()  # 排序反转
print(list_5)
# 字符串根据英文单词首字母进行排序,首字母相同根据第二个字母排序，以此类推
list_6 = ['hello', 'world', 'apple', 'yellow', 'red', 'aapple']
list_6.sort()
print(list_6)