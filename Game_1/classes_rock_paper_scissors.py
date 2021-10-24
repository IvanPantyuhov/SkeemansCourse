import random

possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)


class Game_Rock_Paper_Scissors:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer


    def Game(self):
        print('Welcome to the games "ROCK, PAPER & SCISSORS"')
        if player == computer:
            print("Tie, try again")
        elif player == "Rock":
            if computer == "Paper":
                return "You lose!{1} covers{0}" .format(self.computer,self.player)
            else:
                return "You win!{0} smashes{1}" .format(self.player ,self.computer)
        elif player == "Paper":
            if computer == "Scissors":
                return "You lose!{1} cut {0}" .format(self.computer,self.player)
            else:
                return "You win! {0} covers {1}" .format(self.player ,self.computer)
        elif player == "Scissors":
            if computer == "Rock":
                return "You lose...{1} smashes {0}" .format(self.computer,self.player)
            else:
                return "You win!{1} cut {0}" .format(self.player ,self.computer)
        print("Game end")

if __name__ == '__main__':
    player = input('Welcome to the games "ROCK, PAPER & SCISSORS"')

    if player!="rock" and player!="paper" and player!="scissors":
            print("That's not a valid play. Check your spelling!")

    else:
        print(f"\nYou chose {player}, computer chose {computer}.\n")
        playing = Game_Rock_Paper_Scissors(player ,computer)
        playing.Game()
