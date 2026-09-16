num = int(input("Enter a number:"))

i = 0
even_count = 0
cond = True
while cond:
    if i > num:
        cond = False
    else:
        if i % 2 == 0:
            even_count += 1
        i += 1
print("Total Even Count:", even_count)
