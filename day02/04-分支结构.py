"""
分支结构
    if 条件表达式:
        代码块……
    else
        代码块……

    条件表达式
        只返回两个值
            True:正数、负数、不包含0、其他的所有不为null的类型(字符串、列表、集合、set、元组)
            False:0、null、所有为空的类型(字符串、列表、集合、set、元组)

"""
a = 1
if a < 2:
    print('正确')
else:
    print('错误')
if []:
    print('正确')
else:
    print('错误')
if [0]:
    print('正确')
else:
    print('错误')
if 1 < 2 and 3 < 2:
    print('正确')
else:
    print('错误')
if [] or [0]:
    print('正确')
else:
    print('错误')
if not []:
    print('正确')
else:
    print('错误')

"""

"""
if True:
    print('第一条件表达正确')
elif True:
    print('第二条件表达正确')
elif True:
    print('第三条件表达正确')
else:
    print('错误')

"""
嵌套

"""
a = 5
b = 10
if a < b and a % 10 <= 50:
    a += 10  # 15
    b *= 5  # 50
    if a == b:
        print('正确')
    else:
        print('错误')
