age = int(input("Enter age"))
amt = int(input("Enter Price"))
if(age < 12):
    discount = (amt * 10)/100
    amt -= discount
    print("10% Discount Allowed\n Total Price:",amt)
else:
    print("Total Price:",amt)
