from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # This will hold the player's cards.
        self.points = 0
        
    def receive_cards(self, cards):
        self.hand += cards
        
    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            raise ValueError(f"{card} not in player's hand!")
    
    def resetHand(self):
        self.hand = []
        
    def sort_hand(self):
        self.hand.sort(key=lambda card: (Deck.SUITS.index(card.suit), Deck.RANKS.index(card.rank)), reverse=True)
                
    def add_points(self, points):
        self.points += points
        
    def __repr__(self):
        return f"{self.name}, {self.points} points: {self.hand}"
    
if __name__ == "__main__":
    deck = Deck()
    player1 = Player("Avi")
    deck.shuffle()
    player1.receive_cards(deck.draw(13))
    player1.sort_hand()
    player1.add_points_from_hand()
    print(player1)
        
