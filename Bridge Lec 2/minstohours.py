# Program to convert minutes into hours 
min = int(input("Enter minutes: "))
remaning_min = min % 60
hours = min // 60
print(min,"is ",hours ,"Hours and ",remaning_min,"minutes")