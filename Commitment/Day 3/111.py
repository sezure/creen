num_1 = int(input("please enter a positive number 1:"))
num_2 = int(input("please enter a positive number 2:"))
if num_1<0 or num_2 < 0:
    print("please check your numbers")
else:     
    for i in range(1, min(num_1, num_2)):
        if num_1 % i == 0 and num_2 % i == 0:
            k = i
    a = max(num_1,num_2) 
    b = num_1*num_2+1
    for j in range(a, b , a):
        if j % num_1 == 0 and j % num_2 == 0:
            c = j
            break
    print(f"min num:{k},max number:{c}")        