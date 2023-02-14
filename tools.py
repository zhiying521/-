import hashlib
# 加密
def encrys(passwd):
    h=hashlib.md5()
    h.update(passwd.encode('utf8'))
    return h.hexdigest()