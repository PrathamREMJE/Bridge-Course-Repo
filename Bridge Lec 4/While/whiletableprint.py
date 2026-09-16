num = int(input("Enter a number:"))
i = 1
cond = True
while cond:
    if i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1
    else:
        cond = False
