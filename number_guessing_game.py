import random

top_of_range=input("Type a number in the range of 1-100: ")#by default python gives a string
# taken a range
if top_of_range.isdigit():
    top_of_range=int(top_of_range)# convert string to int 
    if top_of_range <=0:
       print("please type a number larger than 0 next time.") #if number is below 0
       quit()
    elif top_of_range>100:
       print("please type in range of 1-100 in next type")
       quit()
    else:
        pass
else:
    print("please type a number next time")# if it is not a number
    quit()
       
random_number=random.randint(0,top_of_range)

guesses=0
while True:
    guesses += 1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
       user_guess=int(user_guess)# convert string to int 
    else:
        print("please type a number next time")
        continue
    if user_guess == random_number:
        print("You got it!!..")
        break
    elif user_guess > random_number:
        print("You were above the number!!")
    else:
        print("You were below the number!!")

print("You got it in ",guesses,"guesses")