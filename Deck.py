import random

class Deck(object):
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    cards = []

    def __init__(self):
        for suit in self.suits:
            for i in range(1, 14):
                name = ''
                if i == 11:
                    name = 'j'
                elif i == 12:
                    name = 'q'
                elif i == 13:
                    name = 'k'
                elif i == 1:
                    name = 'a'
                else:
                    name = str(i)
                newCardOfaSuit = Card(suit, name)
                self.cards.append(newCardOfaSuit)

    # def getsuit():
    #     choice = floor(random.random() * 3)
    #     self.suit = suits[choice]
    #     return self

    # def getNum():
    #     choice = floor(random.random() * 12 + 2)

    def deal(self):
        length = len(self.cards)
        idx = random.randrange(1, length)
        x = self.cards.pop(idx)
        print 'dealt', x.name, x.suit
        return self

    def DisplayDeck(self):
        for card in self.cards:
            print "This card is a {} of {}.".format(card.name, card.suit)



class Card(object):
    
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

newDeck = Deck()
newDeck.deal().DisplayDeck()
