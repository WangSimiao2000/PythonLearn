"""
类、对象/实例、实例化
    类:
        类别、物以聚类。有相同属性、相同行为的事务统称为类
    对象:
        在类中的一个具体事例成为对象。
    实例化:
        从类生成到对象的一个过程。

    定义类
        class 自定义类名()
            定义属性
            定义行为

"""


# 创建一个学生类
class Student:
    # 定义属性
    name = ""
    age = 0
    userid = ""

    # 定义行为
    def eat(self):
        # self : 谁调用这个方法，谁就是self
        # 1. ZhangSan调用了eat方法
        # 2. ZhangSan就是这个self
        # 3. ZhangSan有name属性、age属性、eat方法
        # 4. self也有这些方法
        print(self.name, '正在吃饭')

    def sleep(self):
        print(self.name, '正在休息')


# 创建对象
ZhangSan = Student()

# 对象访问属性
# 对象名.属性名
ZhangSan.name = "张三"
ZhangSan.age = 21
ZhangSan.userid = "0001"
print(ZhangSan.name)

# 对象访问行为方法
# 对象名.方法名() 记得加括号 不加括号意思为查看一些方法信息
ZhangSan.eat()
ZhangSan.sleep()

# 定义第二个对象
LiSi = Student()
LiSi.name = "李四"
LiSi.age = 18
LiSi.userid = "0002"
LiSi.eat()
