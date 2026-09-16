num = int(input("Enter number"))    #in match case we use it for our choice comparison while if elif for conditions

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Sunday")