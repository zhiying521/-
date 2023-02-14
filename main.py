from r_w_f import read_dl
from x_z import login,register,quit
def strat():
    content1=read_dl('d_l.txt')
    while True:
        operation=input(content1+'\n'+'请输入(1~3)中的一个数字：')
        if operation=='1':
            login()
        elif operation=='2':
            n=register()
            if n==1:
                return
        elif operation=='3':
            quit()
            return
        else:
            print('输入有误！')
if __name__=='__main__':
    strat()