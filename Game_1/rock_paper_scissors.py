import random

values = ['rock', 'paper', 'scissors']
print('Welcome to the games "ROCK, PAPER & SCISSORS"')

while True:
    user = input('Make a choice "Rock, Paper, Scissors": ').lower()
    computer = random.choice(values)
    print(f"\nYou chose {user.upper()}, computer chose {computer.upper()}.\n")

    if user == computer:
        print("Tie, try again")
        continue
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win.\n")
        else:
            print("Paper covers rock! You lose.\n")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers the rock! You win.\n")
        else:
            print("Scissors cuts paper! You lose.\n")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cut paper! You win.\n")
        else:
            print("Rock smashes scissors! You lose.\n")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        continue
    else:
        print('See you next time')
        break