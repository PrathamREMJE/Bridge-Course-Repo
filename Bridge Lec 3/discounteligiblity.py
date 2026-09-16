# write a program to check if a person is eligible for discount the criteria is the must be a student and age must be below 21
#input values to take are role and age

role = input("Enter role")
age = int(input("Enter age"))

print("Eligible:",(role == "student") & (age >21))
