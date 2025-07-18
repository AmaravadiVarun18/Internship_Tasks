import random

user_win=0
computer_win=0
option=["rock","paper","scissors"]

while True:
    user_input=input("Type rock/paper/scissors or q from quit: ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue

    computer_number=random.randint(0,2)
    computer_guess=option[computer_number]
    print("Computer pickes",computer_guess,".")

    if user_input==computer_guess:
        print("Both are same guess Try again!!..")

    elif user_input=="rock" and computer_guess=="scissors":
        print("You Win!!..")
        user_win+=1

    elif user_input=="paper" and computer_guess=="rock":
        print("You Win!!..")
        user_win+=1

    elif user_input=="scissors" and computer_guess=="paper":
        print("You Win!!..")
        user_win+=1
    else:
        print("You lost!!..")
        computer_win+=1
print("You win ",user_win,"times..")
print("Computer Wins ",computer_win,"Times")
print("your game is UP !!..")
    
