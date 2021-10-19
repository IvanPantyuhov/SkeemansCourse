import random

def choices_of_players():
    values = ['rock', 'scissors', 'paper']

    while True:
        user_choice = input('Make a choice "Rock, Paper, Scissors": ').lower()
        if user_choice not in values:
            print('Wrong value!')
            continue
        else:
            print('YOU: ' + user_choice)
            computers_choice = random.choice(values)
            print(f'COMPUTER: ' + computers_choice)
        return user_choice, computers_choice

def same_values():
    while True:
        user_choice, computers_choice = choices_of_players()
        if user_choice != computers_choice:
            break
        print('Tie, try again')
    return user_choice, computers_choice

def is_won(user_choice, computers_choice):
    if user_choice == 'paper':
        if computers_choice == 'rock':
            return True
        elif computers_choice == 'scissors':
            return False

    elif user_choice == 'rock':
        if computers_choice == 'scissors':
            return True
        elif computers_choice == 'paper':
            return False

    elif user_choice == 'scissors':
        if computers_choice == 'paper':
            return True
        elif computers_choice == 'rock':
            return False

def is_repeat():
    return input("Would you like to play again? (yes/no): ").lower() == 'yes'

def main():
    print('Welcome to the games "ROCK, PAPER & SCISSORS"')
    while True:
        players_selection, computers_selection = same_values()
        if is_won(players_selection, computers_selection):
            print('You won! Congrats')
        else:
            print('Oops! You lose! Well, don\'t be discouraged!')
        if is_repeat():
            continue
        else:
            return print('See you next time')

if __name__ == '__main__':
    main()