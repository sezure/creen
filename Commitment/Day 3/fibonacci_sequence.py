a = 0
b = 1
for i in range(1, 21):
    a=b
    b=a+b
    print(b, a+b)
    if i % 5 == 0:
        print()