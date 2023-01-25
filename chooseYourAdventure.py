name = input("Type your name: ")
print ("Welcome " ,name,"to this adventure")

answer = input("You are on the road, it end of the way choose left or right?: ").lower()

if answer == "left":
    answer = input("you come to river you can walk around or swin accross?: ")
    if answer == "swin":
        print("you swin and got eaten by shark YOU DIE")
    elif answer == "walk":
        print("you run out of water YOU DIE")
    else:
        print ("Vaild answer YOU DIE")        
elif answer == "right":
    answer = input("you have come to the castle of white king(ENTER/LEAVE): ")
    if answer == "enter":
        print = input("You have meet the king(TALK/FUCK)?:  ")
        if answer == "talk":
            print("king be please to welcome you for a dinner")
        elif answer == "fuck":
            print("king excicute you YOU DIE")
        else:
            print ("Vaild answer YOU DIE")       
    elif answer == "leave":
        print("you go back and king order the soidger to kill you and YOU DIE")
    else:
        print ("Vaild answer YOU DIE")        
else:
    print ("Vaild answer YOU DIE")

print ("THANK YOU FOR PLAYING",name)