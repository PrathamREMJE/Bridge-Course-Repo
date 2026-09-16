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