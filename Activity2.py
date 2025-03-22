import random

options = ["rock" , "paper" , "sissors"]

user_choice = input("choose rock,papper,sissors:")

computer_choice = random.choice(options)

print("you chose:", user_choice)
print("computer chose:", computer_choice:)

if user_choice == computer_choice:
    print("it's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("rock smaches sissors! you win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("paper covers rock! you win!")
elif user_choice == "sissors" and computer_choice == "paper":
    print("scissors cuts paper! you win!")

else:
    print("you lose!. ")
    