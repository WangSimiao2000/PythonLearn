def a():
    print('a函数启动')
    d()
    print('a函数结束')


def b():
    print('b函数启动')
    print('b函数结束')


def c():
    print('c函数启动')
    b()
    print('c函数结束')


def d():
    print('d函数启动')
    c()
    print('d函数结束')


a()
# 函数从哪个地方调用，运行执行完之后还会内到调用处
# 栈:先进后出
