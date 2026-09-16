#ATM Menu
start = True
bal = 1000
while(start):
    c = str(input("Enter Choice"))
    match c:
        case "Check Balance":
            print(bal)
        case "Deposit":
            amt = int(input("Enter amount to Deposit"))
            bal += amt
            print("Amount Deposited")
        case "Withdraw":
            amt = int(input("Enter amount to Withdraw"))
            if(amt >= bal):
                print("Low Balance")
            else:
                bal -= amt
                print("Amount Withdrawn")
        case "Exit":
            print("Exitted")
            start = False
        case _:
            print("Wrong Choice")
