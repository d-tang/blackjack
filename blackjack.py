from player import Player
from blackjackdeck import Deck

class blackjack(object):
    def __init__ (self):
        self.player1 = self.create_player("Player 1")
        self.Dealer = self.create_player("Dealer")

    def create_player(self, name):
        return Player(name)

    def initiategame(self):
        deck = Deck()
        deck.shuffle()
        for i in range(2):
            self.player1.receive_cards(deck.draw_card())
            self.Dealer.receive_cards(deck.draw_card())

    def check_Dealer_hand(self):
        if self.Dealer.hand_values < 17:
            self.Dealer.receive_cards(deck.draw_card())

    def checkIfBuster(self):
        if self.Dealer.hand_values > 21 and self.player1.hand_values>21:
            return ("Tie")
        elif self.Dealer.hand_values > 21:
            return ("Player 1 wins")
        elif self.player1.hand_values > 21:
            return ("Dealer wins")

    def playgame(self):
        pass
