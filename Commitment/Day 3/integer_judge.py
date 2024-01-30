print("please enter a positive number:")
number = int(input())
if number <= 1:
    print("please check your input")
else:
    for i in range(2,number):
        if number%i == 0:
            print("False")
            break  
    else:         
        print("True")