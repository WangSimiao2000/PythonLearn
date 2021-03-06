"""
函数
    用过哪些函数
        sort()
        print()
        input()
        type()
        len()
    什么是函数
        有特定功能、完成指定任务的一段代码块
    为什么使用函数
        可以隐藏代码的实现
        提高代码复用性
        提高代码的可读性，可维护性
    函数的定义
        def 自定义变量名(参数1,参数2......)
            函数体
            return
    参数
        形参:形式上的参数，并没有实际的意义。也可以称之为占位符。
        实参:实际的参数值，在调用函数地方出现
    传递参数
        位置传递:按照位置的先后顺序进行传递参数
        关键字传递:在调用地方，传递变量值，通过变量名称去定义函数地方去找寻，看看有没有关键字
            如果有关键字，则会把变量赋值给关键字
    return
        返回类型不用事先声明
        返回多个值

"""


# 创建加法函数
def addition(a, b):
    # 使用参数a加上参数b得出结果赋值给变量c
    c = a + b
    # return c, c, c, c, c, c
    # return {1, 2, 3, 4, 5}
    # return '法外狂徒·张三'
    return c


# 调用函数
print('传入参数')
res = addition(10, 20)
print(res)
print(type(res))

res_2 = addition(b=30, a=50)
print(res_2)
