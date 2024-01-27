##
x = float(input ())
a = x*3-5
b = x+2
c = x*8+3
if a>1:
    print(a)
elif -1<a>=1:
    print(b)
elif c<-1:
    print(c)


###
print ("please enter your achievement")
a = float(input())
if a>=90:
    print("A")
elif 90>a<=80:
    print("B")
elif 80<a>=70:
    print("C")
elif 70<a>=60:
    print("C")
elif a<60:
    print("E")


###
import math
t=input()
y=input()
u=input()
s=(t+y+u)/2
if t+y>u:
    print(t+y+u,math.squrt(s*(s-t)(s-y)(s-u)))
else:
    print("False")