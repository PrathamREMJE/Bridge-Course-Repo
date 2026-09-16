# write a program to swap two variable without a third variable, using arithmetic operations

org_str = int(input("Enter first num"))
ano_str = int(input("Enter second num"))

org_str = org_str + ano_str
ano_str = org_str - ano_str
org_str = org_str - ano_str
print("After swap:",org_str,ano_str)
