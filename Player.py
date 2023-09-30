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
        
    def sort_hand(self):
        # This assumes the Card class has a method to determine its order.
        self.hand.sort(key=lambda card: (Deck.SUITS.index(card.suit), Deck.RANKS.index(card.rank)))
        
    def points_from_hand(self):
        for card in self.hand:
            if card.rank == "Ace":
                self.points += 4
            elif card.rank == "King":
                self.points += 3
            elif card.rank == "Queen":
                self.points += 2
            elif card.rank == "Jack":
                self.points += 1
            
        
    def __repr__(self):
        return f"{self.name}, {self.points} points: {self.hand}"
    
if __name__ == "__main__":
    deck = Deck()
    player1 = Player("Avi")
    deck.shuffle()
    for _ in range(13):
        player1.receive_card(deck.draw())
    player1.sort_hand()
    print(player1)
        
