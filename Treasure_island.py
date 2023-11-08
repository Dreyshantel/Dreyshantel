print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Type "right" or "left" ').lower()

if choice1 == "left":
    #game continues
    choice2 = input('you are at the lake. Type "swim" to swim across the lake. Type "wait" to wait for a boat.  ').lower()
    if choice2 == "wait":
    #game continues
        choice3 = input("The house at the island has three doors. Which one do you want to open? Red, Yellow or Blue.  ").lower()
        if choice3 == "red":
            print("You entered a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You won!")
        elif choice3 == "blue":
            print("You entered a room full of snakes. Game Over.")
    else:
        print("You were attacked by an angry crocodile. Game Over.")
else:
    print("You fell into a hole. Game Over.")