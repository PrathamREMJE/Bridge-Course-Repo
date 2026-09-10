# # print('Yo!')

# # print('''Yo!  
# # hello''')

# # three quotes are used to print mutli-line strings. It can also be used to print single line strings. But three used because escape characters are specially treated by three quotes.


# a = 3
# b = 10.0
# c = True
# d = "Hello"

# print(a)  # 3   
# print(b)  # 10
# print(c)  # True
# print(d)  # Hello

# # +,-,/,%,//  - Arithmetic operators     

# a = 6//2.3
# print(a) #(floor division returns whole full number)


# s = int(input("Enter a number: "))
# c = 20
# f = s + c
# print(f)


# >,<,>=,<=,==,!=  - Comparison operators

# &&, ||, !  - Logical operators


# Program to convert minutes into hours 
# min = int(input("Enter minutes: "))
# remaning_min = min % 60
# hours = min // 60
# print(min,"is ",hours ,"Hours and ",remaning_min,"minutes")



# write a program to count you age in days
# age = int(input("Enter your age:"))

# age_in_days = age *365

# print(age,"Years =", age_in_days,"days")

#write a program to check if a number is odd or even
# num = int(input("Enter a number:"))

# print("Number is odd?:", num % 2 != 0)


# write a program to extract the last digit of an number
# numbr = int(input("Enter number"))
# last_num = numbr % 10
# print("Last digit of",numbr,"is", last_num)


# write a program to check if a person is eligible for discount the criteria is the must be a student and age must be below 21
#input values to take are role and age

# role = input("Enter role")
# age = int(input("Enter age"))

# print("Eligible:",(role == "student") & (age >21))

# write a program to swap two variable without a third variable, using arithmetic operations

org_str = int(input("Enter first num"))
ano_str = int(input("Enter second num"))

org_str = org_str + ano_str
ano_str = ano_str - ano_str + org_str
org_str = org_str - ano_str
print("After swap:",org_str,ano_str)

#For git Lecture this comment was added

# New comment added