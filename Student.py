'''
------------------------------
------------------------------
    □□□□欢迎{}来到学生管理系统
    ● 1.添加学生
    ● 2.查看学生
    ● 3.修改学生信息
    ● 4.删除学生信息
    ● 5.返回
------------------------------
------------------------------
'''
from r_w_f import read_dl
from stuent_system import *
def student(x):
    while True:
        opetation = input(read_dl('h_y.txt').format(x)+'\n'+'请输入你的选择(1~5)：')
        if opetation=='1':
            add(x)
        elif opetation=='2':
            check(x)
        elif opetation=='3':
            alter()
        elif opetation=='4':
            delete(x)
        elif opetation=='5':
            return 1
        else:
            print('无法识别功能数字！')