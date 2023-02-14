import json
from r_w_f import read_jn,write_jn
from t_o import Techear
from Student import student
# techer_information={}

def login():
    #读取对象文件中的数据，若数据为空，默认为字典。
    techer_information=read_jn('x_f.json') if read_jn('x_f.json') else {}
    while True:
        techer_name=input('请输入账号:')
        password=input('请输入密码:')
        if 2<len(techer_name)<6 and 7<len(password)<12 and password.isalnum():
            t=Techear(techer_name,password)
            '''
            创建teacher对象
            '''
            if t.t_f(techer_information):
                print('该账号已注册！请登录')
                return
            else:
                techer_information[t.name]=t.password
                choice=input('是否还要录入信息(yes/no):')
                if choice=='yes':
                    continue
                else:
                    write_jn('x_f.json',techer_information)
                    return
        else:
            print('输入账号或密码格式不正确,请重新输入！')

def register():
    techer_information = read_jn('x_f.json') if read_jn('x_f.json') else {}
    teacher_name=input('请输入登录的账号：')
    if teacher_name in techer_information:
        teacher_password=input('请输入登录密码：')
        d=Techear(teacher_name,teacher_password)
        if techer_information[teacher_name]==d.password:
            return student(teacher_name)
    else:
        print('登录失败，该账号还未注册，请先注册！')

def quit():
    pass