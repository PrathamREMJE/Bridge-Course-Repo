marks = int(input("Enter Marks"))
if((marks >= 90) & (marks <=100)):
    print("O")
elif((marks > 80) & (marks < 90)):
    print("A")
elif((marks > 65) & (marks < 80)):
    print("B")
elif((marks > 35) & (marks < 65)):
    print("C")
elif(marks < 35):
    print("F")
else:
    print("Wrong number")
