number_1 = input("please enter number1")
number_2 = input("please enter number2")
if number_2 > number_1:
    while number_2 != 0:
        a = number_2 % number_1
        number_1 = number_2
        number_2 = a
    b=(number_1*1)//number_1
    print("最大公约数%d\n最小共倍数%d"%number_1,b)
else:
    while number_1 != 0:
        a = number_2 % number_1
        number_2 = number_1
        number_1 = a
    b = (number_1*1)//number_2
    print("最大公约数%d\n最小共倍数%d"%number_2,b)
          
        
        
        
