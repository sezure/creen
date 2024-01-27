# 行注释
# print()

# type()
# a = 'fsdfds'
# a = True
# print(type(a))

# b = '1221'
# b = 2
# b = True # 1 
# print(type(int(b)))
# print(type(str(b)))

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
elif username == 'sean' or 'jack': # else if
    print('身份不对！')