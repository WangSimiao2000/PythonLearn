"""
命名规范：
    不能以数字、字符开头、不能以关键字命名

    英文单词、下划线、数字组合
        first_name_123 = ''
    驼峰式
        FirstName
    小驼峰式
        firstName

    第一次出现变量名：定义
    后续多次出现相同名称：赋值
"""


def JiSuanQi(num_1, flag, num_2):
    ans = 'erro'
    if flag == '+':
        ans = num_1 + num_2
    if flag == '-':
        ans = num_1 - num_2
    if flag == '*':
        ans = num_1 * num_2
    if flag == '/':
        ans = num_1 / num_2
    return ans


ans_ = JiSuanQi(1, '+', 2)
print(ans_)

pycharm idea


