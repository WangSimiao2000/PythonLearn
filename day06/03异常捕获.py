"""

异常捕获
try:
    专门捕获异常的代码块
except:
    可以进行打印提示信息
"""
# print('程序开始')
# a = 5
# try:
#     print(0)
#     # 执行代码
#     print('能执行到这里')
# except Exception as e:
#     print('我是一个错误，我捕获了： ',e)
#
# print('程序结束')


## 手动抛出异常进行捕获
# print('程序开始')
# try:
#     raise NameError('当前名称错误')
# except NameError as e:
#     print(e)
# print('程序结束')
raise  TypeError('当前类型名称报错')