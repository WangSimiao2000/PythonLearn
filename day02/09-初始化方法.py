"""
初始化方法
    运行类的第一个启动的方法就是初始化方法
    即使我们没有写初始化方法.也会默认继承object类巾的初始化方法

"""


# 创建类
class Student(object):
    def __init__(self, name, age, userid):
        print('这是一个初始化方法')
        print(name, '对象已创建')
        # 在类里面创建属性
        self.name = name
        self.age = age
        self.userid = userid

    def eat(self):
        print(self.name, '正在吃饭')


# 调用类创建对象
zhangsan = Student('张三', 21, '0001')
print(zhangsan.name)
zhangsan.eat()
