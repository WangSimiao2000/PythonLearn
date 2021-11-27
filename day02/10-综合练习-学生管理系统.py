"""
    1. 欢迎界面
        1)添加学生
        2)查看学生
        3)修改学生信息
        4)删除学生信息
        5)退出系统
    2. 添加学生
        通过input输入添加
        添加到对象里(列表、字典、集合)进行保存
        每个对象是一个学生信息，总的所有对象要保存在列表/集合里
    3. 查看学生
        集合里面有没有学生的对象信息
        如果有，那就遍历展示
        如果没有，那就提示没有信息，退出
    4. 修改学生信息
        集合里面有没有学生的对象信息
        如果有
            通过学号来定位查找学生，再进行更改
        如果没有
            需要提示没有信息，返回
    5. 删除学生信息
        集合里面有没有学生的对象信息
        如果有
            通过学号来定位查找学生，再进行删除
        如果没有
            需要提示没有信息，返回
    6. 退出系统
        直接结束程序
"""
import os


# 学生保存的对象
class Student:
    def __init__(self, name, age, userid):
        self.name = name
        self.age = age
        self.userid = userid


# 针对学生管理的信息
class StudentManage():

    def __init__(self):
        # 创建保存学生对象的容器
        self.data = set()

    def deleteStudent(self):
        # 删除学生信息
        if self.data:
            userid = input("请输入想要删除的学生的学号:")
            flag = False
            for stu in self.data:
                if stu.userid == userid:
                    flag = True
                    break
            if flag:
                print("{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid))
                self.data.remove(stu)
                print("删除成功")
            else:
                print("未查找到该学号为{}的学生".format(userid))
        else:
            print("当前系统中没有学生信息，需要先添加")
        text = input("按任意键返回主菜单:")
        if text != "":
            return

    def updateStudent(self):
        # 更新学生信息
        if self.data:
            userid = input("请输入想要修改的学生的学号:")
            flag = False
            for stu in self.data:
                if stu.userid == userid:
                    flag = True
                    break
            if flag:
                print("{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid))
                name = input("请输入学生姓名")
                stu.name = name
                age = input("请输入学生年龄")
                stu.age = age
                print("{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid))
            else:
                print("未查找到该学号为{}的学生".format(userid))
        else:
            print("当前系统中没有学生信息，需要先添加")
        text = input("按任意键返回主菜单:")
        if text != "":
            return


    def showStudent(self):
        # 查看学生信息
        if self.data:
            for stu in self.data:
                print("{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid))
        else:
            print('当前系统中无学生信息，需要先添加')
        text = input("按任意键返回主菜单:")
        if text != "":
            return

    def addStudent(self):
        # 添加学生信息
        name = input('请输入学生姓名:')
        age = input('请输入学生年龄:')
        userid = input('请输入学生学号:')
        # 创建学生对象
        stu = Student(name, age, userid)
        # 通过set集合添加学生信息
        self.data.add(stu)
        print("{}\t\t\t{}\t\t\t{}".format(stu.name, stu.age, stu.userid))
        print('添加成功!')
        text = input("按任意键返回主菜单:")
        if text != "":
            return

    def run(self):
        # 启动入口
        while True:
            os.system("cls")
            print('欢迎来到学生管理系统')
            print('1. 添加学生信息')
            print('2. 查看学生信息')
            print('3. 修改学生信息')
            print('4. 删除学生信息')
            print('5. 退出学生管理系统')
            num = input('请输入你要运行的操作:')
            print( num )
            if num == '1':
                os.system("cls")
                print('添加学生信息')
                self.addStudent()
            elif num == '2':
                os.system("cls")
                print('查看学生信息')
                self.showStudent()
            elif num == '3':
                os.system("cls")
                print('修改学生信息')
                self.updateStudent()
            elif num == '4':
                os.system("cls")
                print('删除学生信息')
                self.deleteStudent()
            elif num == '5':
                print('退出学生管理系统')
                break
                # return


sm = StudentManage()
sm.run()
