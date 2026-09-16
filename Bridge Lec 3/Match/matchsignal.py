c = str(input("Enter Choice"))
match c:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Steady")
    case "Green":
        print("Go")
    case _:
        print("Wrong Choice")
