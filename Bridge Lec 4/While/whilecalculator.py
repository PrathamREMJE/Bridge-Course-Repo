a = int(input("Enter Number 1"))
b = int(input("Enter Number 2"))
c = str(input("Enter Choice"))
match c:
    case "+":
        print("Addition",a+b)
    case "-":
        print("Subtraction",a-b)
    case "*":
        print("Multiplication",a*b)
    case "/":
        if((a == 0) | (b == 0)):
            print("Unable Division Zero")
        else:
            print("Division",a/b)
    case "!":
        fact_array = [a, b]

        for cur_num in fact_array:
            ans = 1

            while cur_num > 0:
                ans = ans * cur_num
                cur_num -= 1

            print("Factorial:", ans)
    case _:
        print("Wrong Choice")   