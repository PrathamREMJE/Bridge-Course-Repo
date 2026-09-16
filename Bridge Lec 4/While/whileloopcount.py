num = int(input("Enter a number:"))
i = 0
cond = True
while cond:
    if i % 2 == 0:
        print(i)
    i += 1
    if i > num:
        cond = False
print("Total numbers loop executed:", i)
