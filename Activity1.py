import random #importing module
playing = True  #initialise
number = str(random.randint(10,20)) #random in-built function
 
print("i willagenerate a number from 10 to 20 and you ahve to the number one digit at a time.")
print("the game ends when you gets 1 hero!")
#iterate loop till the conditon is true
while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was" ,number)
        break

    else:
        print("your guess isn't quite right, try again.  \n")
        