### 2014-06-01 advanced

### Prepare libraries
import random

### Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return str(self.value) + " of " + self.suit

### Deck class
class Deck:
    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []
            for s in ["Hearts", "Clubs", "Diamonds", "Spades"]:
                for v in range(2,15):    #because an ace is a high value in war, I'm including 14 and excluding 1
                    self.cards.append( Card(v,s) )
    def splitOffCards(self, num):
        ## check if there are enough cards
        if num > len(self.cards):
            print("ERROR!")
        else:
            cards = []
            for n in range(num):
                cards.append(self.cards.pop())
            return Deck(cards)
    def shuffle(self):
        random.shuffle(self.cards) # mutate cards part of the object
    def draw(self):
        return self.cards.pop()    #
    def addCardTop(self, card):
        self.cards.append(card)    # end is the top
    def addCardBottom(self, card):
        self.cards = [card] + self.cards #

### WarEngine class (abstract)
class WarEngine:
    def __init__(self):
        ## Create a full deck for player 1
        self.p1_deck = Deck()
        ## Shuffle
        self.p1_deck.shuffle()
        ## give half to player 2
        self.p2_deck = self.p1_deck.splitOffCards(26)
    def start(self):
        ## while both people have cards
        while self.p1_deck.cards and self.p2_deck.cards:
            c1 = self.p1_deck.draw()
            c2 = self.p2_deck.draw()
            print("P1: " + str(c1.value) +  " of " + c1.suit, "P2: " + str(c2.value) + " of " + c2.suit)
            wagered = Deck([c1,c2])
            while c1.value == c2.value:
                print("WAR!")
                for n in range(3):
                    if len(self.p1_deck.cards) > 1:
                        wagered.addCardBottom(self.p1_deck.draw())
                    if len(self.p2_deck.cards) > 1:
                        wagered.addCardBottom(self.p2_deck.draw())
                c1 = self.p1_deck.draw()
                c2 = self.p2_deck.draw()
                wagered.addCardBottom(c1)
                wagered.addCardBottom(c2)
                print("P1: " + str(c1.value) +  " of " + c1.suit, "P2: " + str(c2.value) + " of " + c2.suit)
            if c1.value > c2.value:
                for c in wagered.cards:
                    self.p1_deck.addCardBottom(c)
            else:
                for c in wagered.cards:
                    self.p2_deck.addCardBottom(c)
            print("P1 has", len(self.p1_deck.cards))
            print("P2 has", len(self.p2_deck.cards))
            #input("Press enter to begin the next round.")
            print()
        ## at the game end
        print("The winner is " + ("p1" if self.p1_deck.cards else "p2"))

### Create a game engine instance
game = WarEngine()
### execution
game.start()

