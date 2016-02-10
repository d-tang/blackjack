import blackjackdeck
import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.playerhand = []
        self.totalhand  = 0

    def receive_card(self, card):
        self.playerhand.append(card)
        self.hand_values(card)

    def receive_cards(self, cards):
        self.playerhand.append(cards)
        self.hand_values(cards)

    def hand_values(self, card):
            self.totalhand+= blackjackdeck.Card.value_dict[card.number]
#
