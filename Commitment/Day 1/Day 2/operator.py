###F->C
print("please enter fahrenheit")
F = int(input())
print("centigrade is:",(F-32)/1.8) # 建议修改： 将公式这一段单独赋予它一个变量


###
r=2
pai=3.1416
C=print(r*2*pai,"C=2pai r")
S=print(pai*r**2,"S=pai r**2")
#以上10、11行不需要赋予变量C、S，因为print()函数本身会打印输出，此处出错。

###
print("please enter number of years")
years = int(input())
a = years % 4
b = years % 100
if a == 0 and b != 0:
    print("True")
else: 
    print("False")