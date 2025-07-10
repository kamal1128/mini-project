# This is a simple Rock, Paper, Scissors game in Python.
# The user is prompted to play the game, and they can choose between rock, paper, scissors.


import random

def play_game(user_choice):
    computer = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(f"---------Both chose {user_choice}. It's a tie!---------")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"---------You win! {user_choice} beats {computer_choice}.---------")
    else:
        print(f"---------You lose! {computer_choice} beats {user_choice}.---------")


# Main game loop
response = input("Hi there! Do you want to play ROCK PAPER SCISSORS game? (yes/no): ").strip().lower()

if response == "no":
    print("OKEY, Let's play next time...")

elif response == "yes":
    print("OKEY, Let's BEGIN...")
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    
    if user_choice in ["rock", "paper", "scissors"]:
        play_game(user_choice)
    else:
        print("Invalid choice! Please choose rock, paper, or scissors.")

else:
    print("You should enter yes or no only.")

print("Thanks for playing! Goodbye!")

