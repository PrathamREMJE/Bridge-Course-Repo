a = int(input("Enter num"))
b = int(input("Enter num"))
c = int(input("Enter num"))
if((a >= b) & (a >= c)):
    print(a)
elif((b >= a) & (b >= c)):
    print(b)
else:
    print(c)
