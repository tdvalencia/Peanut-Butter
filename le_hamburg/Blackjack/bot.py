import random as r
from .card import Card

class Bot():
    def __init__(self):
        self.cards = []

    def play(self):
        self.deal()

        while True:
            if self.total() < 18:
                self.hit()
            else:
                break

    def hit(self):
        c = Card(r.randrange(1,13))
        if c.name == 'ace' and self.cards and self.cards[0].value <= 10:
            c.value = c.setValue('aceEl')
            self.cards.append(c)
        elif c.name == 'ace' and not self.cards:
            c.value = c.setValue('aceEl')
            self.cards.append(c)
        else:
            self.cards.append(c)
        # print(self.cards)

    def deal(self):
        for x in range(0, 2):
            c = Card(r.randrange(1, 13))

            if c.name == 'ace' and self.cards and self.cards[0].value <= 10:
                c.value = c.setValue('aceEl')
                self.cards.append(c)
            elif c.name == 'ace' and not self.cards:
                c.value = c.setValue('aceEl')
                self.cards.append(c)
            else:
                self.cards.append(c)

    def ace(self):
        pass

    def total(self):
        result = 0
        for card in self.cards:
            result += card.value
        return result