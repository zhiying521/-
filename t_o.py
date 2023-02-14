from tools import encrys


class Techear():
    def __init__(self, name, password):
        self.name = name
        self.password = encrys(password)  # 将密码进行加密

    def t_f(self, data):
        return self.name in data


class Student():
    def __init__(self, s_id,name, age, sex, phone_n):
        self.s_id=s_id
        self.name = name
        self.age = age
        self.sex = sex
        self.phone_n = phone_n
