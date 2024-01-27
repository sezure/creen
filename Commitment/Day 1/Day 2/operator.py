###F->C
print("please enter fahrenheit")
F = int(input())
print("centigrade is:",(F-32)/1.8)


###
r=2
pai=3.1416
C=print(r*2*pai,"C=2pai r")
S=print(pai*r**2,"S=pai r**2")


###
print("please enter number of years")
years = int(input())
a = years % 4
b = years % 100
if a == 0 and b != 0:
    print("True")
else: 
    print("False")