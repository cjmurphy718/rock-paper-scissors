# this is the "game.py" file...
import random


print("Rock, Paper, Scissors, Shoot!")
print ("--------")

# USER INPUTS

user_input = input("Please make a selection ('rock', 'paper', 'scissors')")
user_input = user_input.lower()
valid_options = ["rock", "paper", "scissors"]
print ("---------")

# You chose: 'rock'
print(f"You chose: '{user_input}' ")

# VALIDATE USER INPUTS

valid_options = ["rock", "paper", "scissors"]

#breakpoint{}

if user_input not in valid_options:
    print("Oops! Invalid, try again")
    exit ()


# COMPUTER CHOICE

valid_options=["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)
print ("-------")


# DETERMINE THE WINNER

if user_input==computer_choice:
    print("Tie game!")
elif user_input=="paper":
    if computer_choice=="Scissors":
        print("Scissors cut paper. You lose!")
    else:
        print("Paper covers rock. You win!")
elif user_input=="scissors":
    if computer_choice=="Paper":
        print("Scissors cut paper. You win!")
    else:
        print("Rock crushes scissors. You lose!")
elif user_input=="rock":
    if computer_choice=="scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose!")

print("Great game! Type python game.py to play again.")
