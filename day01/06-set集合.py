"""

"""
# 创建方式
set_1 = set()
print(set_1)
print(type(set_1))

set_2 = {'周一', '周二', '周三', '周四', '周五', '周五', '周五'}
print(set_2)

# 随机
res = set_2.pop()
print('弹出的内容是：', res)

# 删除
set_2.remove('周五')
print(set_2)

# 添加
set_2.add('周六')
print(set_2)

# 更改
set_2.update(['周天'])
print(set_2)

# 查找
# 同列表和元组
