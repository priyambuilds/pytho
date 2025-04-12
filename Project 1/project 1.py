#sname water gun
#1 = snake
#2 = water
#3 = gun
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "s", -1: "w", 0: "g"}
you = youdict[youstr] #this is the value of your choice
print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if computer == you:
    print("It's a tie!")
else:
    if computer == 1 and you == 0:
        print("You win!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 0 and you == -1:
        print("You win!")
    else:
        print("Invalid input!")
    
