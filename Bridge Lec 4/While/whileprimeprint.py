num = int(input("Enter a number:"))
i = 1
cond = True
while cond:
    if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
        if(i == 2) or (i == 3) or (i == 5) or (i == 7):
            print(i)
        i += 1
        continue
    elif i > num:
        cond = False
    else:
        print(i)
        i += 1