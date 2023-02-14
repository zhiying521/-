from t_o import Student
from r_w_f import write_jn,read_jn
list=[]
def l_s(z):
    print('学生信息如下：')
    for i in z:
        print('\t学号：{s_id},姓名：{name},年龄：{age},性别；{sex},电话号码：{phone_n}'.format(**i))
def add(y):
    while True:
        dict=read_jn(y+'.json')
        name=input('请输入学生姓名：')
        age=int(input('请输入学生年龄：'))
        sex=input('请输入学生性别：')
        phone_n=input('请输入学生电话号码：')
        #创建一个学生类，字符串zfill方法,在字符串前补0
        if not dict:
            s_id='stu'+'1'.zfill(4)
        else:
            s_id='stu000{}'.format(dict['num']+1)
        s=Student(s_id,name,age,sex,phone_n)
        if not dict:
            dict={}
            list.append(s.__dict__)
            dict['all_student']=list
            dict['num']=len(list)
        else:
            dict['all_student'].append(s.__dict__)
            dict['num']+=1
        write_jn(y+'.json',dict)
        number=input('添加成功！'+'\n'+'1.继续'+'\n'+'2.返回'+'\n'+'请选择(1~2):')
        if number=='1':
            pass
        else:
            break
    #也可以进行创建对象
def check(y):
    dict1 = read_jn(y + '.json')
    s_i=dict1.get('all_student',{})#如果读取的字典为空，则获取的是个空字典
    if not s_i:
        print('该老师还未添加学员，请添加！')
        return
    n=input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他:返回\n请选择：')
    if n=='1':
        l_s(s_i)
    elif n=='2':
        name=input('请输入查找同学的名字：')
        students=[]
        for j in s_i:
            if j['name']==name:
                students.append(j)
                '''
                上面代码的简写版：students=filter(lambda j:j['name']==name,s_i)
                '''
        if len(students)>0:
            l_s(students)
        else:
            print('查无此人！请添加')

    elif n=='3':
        number=input('请输入学生的学号:')
        new_number='stu000'+number
        #filter结果是一个filter类，它是一个可迭代对象.
        print(s_i)
        d=(filter(lambda k:k['s_id']==new_number,s_i))#<filter object at 0x000001C149234FA0>:内存地址
        l_s(d)
    else:
        return
def alter():
    pass
def delete(y):
    #字典删除方式：del(字典名[key])
    list=[]
    key=value=''
    dict3=read_jn(y+'.json')
    d_s=dict3.get('all_student',{})
    if not d_s:
        print('该老师还未添加学员，请添加！')
        return
    d_n=input('1.按姓名删除\n2.按学号删除\n其他:返回\n请选择(1~2):')
    if d_n=='1':
        value=input('请输入学生姓名：')
        key='name'
    elif d_n=='2':
        value=input('请输入学生的学号:')
        key='s_id'
    else:
        pass
    d_t=filter(lambda x:x.get(key,"")!=value,d_s)#get方法报错的话返回default=
    for i in d_t:
        list.append(i)
    dict4={'all_student':list,'num':len(list)}
    write_jn(y+'.json',dict4)
