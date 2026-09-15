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

# org_str = int(input("Enter first num"))
# ano_str = int(input("Enter second num"))

# org_str = org_str + ano_str
# ano_str = org_str - ano_str
# org_str = org_str - ano_str
# print("After swap:",org_str,ano_str)

#For git Lecture this comment was added

# New comment added new


#Conditional Programming

# is_Raining = False

# if is_Raining == True:
#     print("Raining Outside")
# else:
#     print("Not Raining")


# age = int(input("Enter age"))
# if(age > 18):
#     print("Eliigible to Vote")
# else:
#     print("Not Eligible to Vote")  

# num = int(input("Enter number"))
# if(num == 1):
#     print("Monday")
# elif(num == 2):
#     print("Tuesday")
# elif(num == 3):
#     print("Wednesday")
# elif(num == 4):
#     print("Thursday")
# elif(num == 5):
#     print("Friday")
# elif(num == 6):
#     print("Saturday")
# else:
#     print("Sunday")


# num = int(input("Enter number"))    in match case we use it for our choice comparison while if elif for conditions

# match num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case _:
#         print("Sunday")


# num = int(input("Enter number"))
# if(num % 2 == 0):
#     print("Even")   
# else:
#     print("Odd")


# age = int(input("Enter age"))
# amt = int(input("Enter Price"))
# if(age < 12):
#     discount = (amt * 10)/100
#     amt -= discount
#     print("10% Discount Allowed\n Total Price:",amt)
# else:
#     print("Total Price:",amt)

# marks = int(input("Enter Marks"))
# if((marks >= 90) & (marks <=100)):
#     print("O")
# elif((marks > 80) & (marks < 90)):
#     print("A")
# elif((marks > 65) & (marks < 80)):
#     print("B")
# elif((marks > 35) & (marks < 65)):
#     print("C")
# elif(marks < 35):
#     print("F")
# else:
#     print("Wrong number")


# num = int(input("Enter num"))
# if(num > 0):
#     print("Positive")
# elif(num == 0):
#     print("No Sign")
# else:
#     print("Negative")


# a = int(input("Enter num"))
# b = int(input("Enter num"))
# c = int(input("Enter num"))
# if((a >= b) & (a >= c)):
#     print(a)
# elif((b >= a) & (b >= c)):
#     print(b)
# else:
#     print(c)

# year = int(input("Enter Year"))
# if(year % 4 == 0):
#     print("Leap Year")
# else:
#     print("Not")

# a = int(input("Enter Number 1"))
# b = int(input("Enter Number 2"))
# c = str(input("Enter Choice"))
# match c:
#     case "+":
#         print("Addition",a+b)
#     case "-":
#         print("Subtraction",a-b)
#     case "*":
#         print("Multiplication",a*b)
#     case "/":
#         if((a == 0) | (b == 0)):
#             print("Unable Division Zero")
#         else:
#             print("Division",a/b)
#     case _:
#         print("Wrong Choice")


# c = str(input("Enter Choice"))
# match c:
#     case "Red":
#         print("Stop")
#     case "Yellow":
#         print("Steady")
#     case "Green":
#         print("Go")
#     case _:
#         print("Wrong Choice")

#ATM Menu
# start = True
# bal = 1000
# while(start):
#     c = str(input("Enter Choice"))
#     match c:
#         case "Check Balance":
#             print(bal)
#         case "Deposit":
#             amt = int(input("Enter amount to Deposit"))
#             bal += amt
#             print("Amount Deposited")
#         case "Withdraw":
#             amt = int(input("Enter amount to Withdraw"))
#             if(amt >= bal):
#                 print("Low Balance")
#             else:
#                 bal -= amt
#                 print("Amount Withdrawn")
#         case "Exit":
#             print("Exitted")
#             start = False
#         case _:
#             print("Wrong Choice")


# Rock Paper Scissors
user1 = input("User 1, enter your sign: ")
user2 = input("User 2, enter your sign: ")
if user1 == user2:
    print("Draw")

elif user1 == "rock" and user2 == "scissors":
    print("User1 wins")

elif user1 == "paper" and user2 == "rock":
    print("User1 wins")

elif user1 == "scissors" and user2 == "paper":
    print("User1 wins")

else:
    print("User2 wins")