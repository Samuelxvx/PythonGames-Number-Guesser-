import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time ")
        quit()
else:
    print ("Please type a number next time ")
    quit()

random_number = random.randrange(0, top_of_range)

guesses = 0
while True:
    guesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number")
        continue
    
    if userGuess == random_number:
        print ("YOU GOT IT!!!")
        break
    elif userGuess > random_number:
        print ("Too much")
    else:
        print ("a litle more")

print("You got", guesses, "guesses")
