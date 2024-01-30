#import the random module
import random

#create variable for user_choice, possible_choice and computer_choice
user_choice = input("Enter a choice(rock, paper, scissors): \n")
possible_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choice)

print(f"\n you chose {user_choice}, computer chose {computer_choice}")

# using the if, elif and else statement to check and determine the winner
continue_game = True

while True:
    if user_choice == computer_choice:
        print(f"computer chose {user_choice}, it's a tie.")

    if user_choice == "rock":
        if computer_choice == "scissors":
            print("rock smashes scissors, you won.")
        else:
            print("paper cover rock, you lose.")

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper cover rock, you won.")
        else:
            print("scissors cut paper, you lose.")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("scissors cut paper, you won.")
        else:
            print("rock smashes scissors, you lose.")

    if input("Type 'y' to continue game, type n to restart.") ==  'y':
        user_choice = input("Enter a choice(rock, paper, scissors): \n")
    else:
        continue_game = False
        print("game over")
        break

