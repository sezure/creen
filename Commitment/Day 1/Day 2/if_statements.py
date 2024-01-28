### 
x = float(input ())
a = x*3-5
b = x+2
c = x*8+3
if a>1:
    print(a)
elif -1<a>=1: # 此处条件出错，
    print(b)
elif c<-1:
    print(c)


###
print ("please enter your achievement")
a = float(input()) # 可以把上面print的字符串放进input函数中
if a>=90:
    print("A")
elif 90>a<=80: # 此处条件出错
    print("B")
elif 80<a>=70: # 此处条件出错
    print("C")
elif 70<a>=60: # 此处条件出错
    print("C")
elif a<60:
    print("E")

# 以下是一个参考代码，对比一下：
# -----
score = float(input("请输入百分制成绩："))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"

print("等级制成绩为：", grade)
# -----

###
import math # 不要导入库
t=input()
y=input()
u=input()
s=(t+y+u)/2
if t+y>u:
    print(t+y+u,math.squrt(s*(s-t)(s-y)(s-u)))
else:
    print("False")