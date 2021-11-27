"""
字符串
    <class 'str'>

    单引号
    双引号
    三引号

    区别：
    单引号/双引号：保存单行的数据
    三引号：保存多行数据

"""

name = '马可波罗'
name_1 = "王昭君"
name_2 = """李白"""
name_3 = ''''''
str_1 = """妲己说：
来陪妲己玩耍吧！"""
str_num = "1234567"
print(name)
print(str_1)
print(str_num)
print(type(str_num))

# 索引下标示例
str_2 = "好看的皮囊千篇一律，有趣的灵魂万里挑一"
print(str_2)
# 单个字符提取
# 正序：0、1、2、3、4……
# 倒序：-1、-2、-3、-4……
# str_2[下标数值]
print(str_2[0])
print(str_2[1])
print(str_2[18])
print(str_2[-1])
print(str_2[-2])

# 范围提取
# str_2[ 起始下标 : 结束下标+1 ]
# 左闭右开原则
# 0 <= 范围提取 < 3
print(str_2[0:3])
print(str_2[0:5])
print(str_2[:])  # 打印所有的内容：不写起始位置且不写结束位置，默认是从开头到结尾
print(str_2[:5])  # 不写起始位置，默认从开头位置开始
print(str_2[0:])  # 不写结束位置，默认到结束位置结束
print(str_2[::])  # 同print(str_2[:])，打印所有内容

# 步长 step
print(str_2[::1])  # 步长为1
print(str_2[::2])  # 步长为2
print(str_2[::3])  # 步长为3
print(str_2[::-1])  # 步长负值：控制正反序
str_3 = str_2[0:5]  # 前五个字单独成一个字符串
print(str_3[::-1])  # 新字符串倒序
print(str_2[0:5][::-1])  # 前五个字倒序：链式写法
