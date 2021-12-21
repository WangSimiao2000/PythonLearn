"""
循环

for循环
    for 自定义表达式 in 可迭代对象
        循环体

"""
list_1 = ['周一', '周二', '周三', '周四', '周五']
for i in list_1:
    print(i)

"""
for(int i = 0 , i < 10 , i++){
    打印
}

"""

"""
while 条件表达式
    循环体
    结束语句
    
    条件表达式为True的时候，会进入while循环
    条件表达式为False的时候，会结束while循环
    结束语句为了控制条件表达式是为True还是为False

"""
a = 1
while a < 10:
    print(a)
    a += 1
# 死循环
# while True:
#     pass


"""
break       :跳出整个循环
continue    :结束当前循环，直接进入下一次循环中

"""





list_1 = ['周一', '周二', '周三', '周四', '周五', '周六']
for i in list_1:
    print(i)
    if i == '周三':
        break

a = 1
while a < 10:
    print(a)
    if a == 5 or a > 5:
        break
    a += 1

list_1 = ['周一', '周二', '周三', '周四', '周五', '周六']
for i in list_1:
    if i == '周三' or i == '周四':
        continue
    else:  # 可以不用打else，continue将会直接跳过
        print(i)

# 只打印5和6
a = 1
while a < 10:
    a += 1
    if a < 5 or a >6:
        continue
    print(a)
