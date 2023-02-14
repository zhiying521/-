import json

base_file='j_m'#能够在主函数中进行修改文件
def read_dl(file_name):
    try:
        with open(base_file+'/'+file_name,encoding='utf8') as stream:
            content=stream.read()
            return content
    except Exception as e:
        print(e)
def write_jn(file_name,t_i):
    try:
        with open(base_file+'/'+file_name,'w',encoding='utf8')as stream1:
            json.dump(t_i,stream1,ensure_ascii=False)
    except Exception as e:
        print(e)
def read_jn(file_name):
    try:
        with open(base_file+'/'+file_name,'r',encoding='utf8')as stream3:
            return json.load(stream3)
    except Exception as e:
        return None