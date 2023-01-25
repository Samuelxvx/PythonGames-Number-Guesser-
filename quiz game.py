print("Welcome to my Game")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Lets play than :) ")

answer = input("What dose CPU stand for? ").lower()
if answer == "central processing unit":
    print("CORRECT!!!!")
    score += 1
else:
    print("INCORRECT!! :( ")

answer = input("What dose GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("CORRECT!!!!")
    score += 1
else:
    print("INCORRECT!! :( ")

answer = input("What dose RAM stand for? ").lower()
if answer == "ramdom access memory ":
    print("CORRECT!!!!")
    score += 1
else:
    print("INCORRECT!! :( ")

answer = input("What dose PSU stand for? ").lower()
if answer == "power suppy":
    print("CORRECT!!!!")
    score += 1
else:
    print("INCORRECT!! :( ")


print ("You got " + str(score) + "Question Correct!" )