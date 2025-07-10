# This is a simple Rock, Paper, Scissors game in Python.
# The user is prompted to play the game, and they can choose between rock, paper, scissors.


def play_game(user_choice):
        
    import random
    computer = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer)
    if user_choice == computer_choice:
        print(f"---------Both chose {user_choice}. It's a tie!---------")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"---------You win! {user_choice} beats {computer_choice}.---------")
    else:
        print(f"---------You lose! {computer_choice} beats {user_choice}.---------")




response = input("Hi there! Do you want to play ROCK PAPER SCISSORS game ? (yes/no):")

if response.lower() == "no":
    print("OKEY, Let's play next time...")

elif response.lower() == "yes":
    print("OKEY, Let's BEGIN...")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")

else:
    print("You should enter yes or no only")

play_game(user_choice)
print("Thanks for playing! Goodbye!")
