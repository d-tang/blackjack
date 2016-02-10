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
        self.print_value()
        self.checkIfBuster()

    def check_Dealer_hand(self):
        if self.Dealer.hand_values < 17:
            self.Dealer.receive_cards(deck.draw_card())

    def Ask_for_hit(self):
        ans = raw_input("Another Card (y,n)")
        if ans == 'y':
            self.player1.receive_cards(deck.draw_card())
            self.check_Dealer_hand()
            self.print_value()
        else:
            old_value = 0
            while old_value != self.Dealer.totalhand:
                old_value = self.Dealer.totalhand
                self.check_Dealer_hand()
            self.determine_winner()

    def determine_winner():
        if self.player1.totalhand == self.Dealer.totalhand:
            print ("Tie")
        elif self.player1.totalhand > self.Dealer.totalhand:
            print ("Player 1 wins")
        elif self.player1.totalhand < self.Dealer.totalhand:
            print ("Dealer wins")

    def checkIfBuster(self):
        if self.Dealer.hand_values > 21 and self.player1.hand_values>21:
            return ("Tie")
        elif self.Dealer.hand_values > 21:
            return ("Player 1 wins")
        elif self.player1.hand_values > 21:
            return ("Dealer wins")

    def print_value(self):
        print "Your hand value is: %d" %, self.player1.totalhand
        return

    def playgame(self):
        
        pass
