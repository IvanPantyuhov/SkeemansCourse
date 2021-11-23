from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        return ()

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        for i in self.cards:
            print(i)


    def shuffle(self):
        if len(self.cards) < 52:
            shuffle(self.cards)
            return self.cards
        else:
            return ("Only full decks can be shuffled")

    def deal(self):
        if len(self.cards) = 0:
            return self.cards.pop()
        else:
            return ("All cards have been dealt")

deck = Deck()
deck.shuffle()
