"""
切割
2021-11-14
"""
str1 = "2021-11-14"
y = str1[0:4]
m = str1[5:7]
d = str1[-2:]
print(d)
res = str1.split('-')
print(res)
str2 = "9:57:10"
print(  str2.split(':') )

"""
去除首尾空格

"""
str1 = " \n\n \r\t\t\r     hello  world  \n   "
print(str1)
print(str1[6:-5])
# 去除两边空格
res = str1.strip()
print(res)
# 去除左边的空格换行
lres = str1.lstrip()
print(lres)
# 去除右边的
rres = str1.rstrip()
print(rres)

"""
替换
replace(  定位到替换的位置  ，  替换成什么   )
"""
str1 = "我是：XXX"
print(str1)
res = str1.replace('XXX', '张三').replace('我', '你')
print(res)
str1 = '     hello world    '
print(str1)
res = str1.replace('l', 'X')
print(res)

"""
格式化输出
%s   传递转化字符串
%d   传递转化成整数
%f   传递转化成小数 默认保留六位
%.2f

"""
str1 = "我是： %s"
print(str1)
print(str1 % '法外狂徒·张三')
print(str1 % '尼古拉斯·赵四')
print(str1 % ['生活有判头'])
str1 = "我的薪资是： %d 美元"
print(str1)
print(str1 % 1000)
print(str1 % 999.9)
str1 = "我的房间面积是：  %f 平米"
str1 = "我的房间面积是：  %.4f 平米"
print(str1)
print(str1 % 150)
print(str1 % 150.23)
print(str1 % 150.123456789)

"""
format
"""
str1 = "我是:{}， 我在：{}， 我喜欢：{}"
print(str1)
print(str1.format('李四', '河南', '跑步'))
