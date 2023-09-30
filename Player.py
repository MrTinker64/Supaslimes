from Deck import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # This will hold the player's cards.
        
    def receive_card(self, card):
        self.hand.append(card)
        
    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            raise ValueError(f"{card} not in player's hand!")
        
    def sort_hand(self):
        # This assumes the Card class has a method to determine its order.
        self.hand.sort(key=lambda card: (Deck.SUITS.index(card.suit), Deck.RANKS.index(card.rank)))
        
    def __repr__(self):
        return f"{self.name}: {self.hand}"
    
if __name__ == "__main__":
    deck = Deck()
    player1 = Player("Avi")
    deck.shuffle()
    for _ in range(13):
        player1.receive_card(deck.draw())
    player1.sort_hand()
    print(player1)
        