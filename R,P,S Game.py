import random

print("Welcome to Rock/Paper/Scissor Game!!!!")

user_wins = 0
computer_wins = 0
ties = 0
rounds = 0

options = ["rock", "paper", "scissor"]

while True:
    print("Round:", rounds + 1)
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won this round!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won this round!")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won this round!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")
        ties += 1

    else:
        print("You lost this round!")
        computer_wins += 1

    rounds += 1

print("Thanks for playing Rock/Paper/Scissor Game!")
print("Number of rounds played:", rounds)
print("You won", user_wins, "rounds.")
print("The computer won", computer_wins, "rounds.")
print("Number of ties:", ties)