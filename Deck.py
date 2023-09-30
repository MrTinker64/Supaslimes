import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.SUITS for rank in self.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, numberOfCards):
        drawnCards = []
        for i in range(numberOfCards):
            if self.cards:
                drawnCards += self.cards.pop()
            else:
                raise ValueError("Deck is empty!")
        return drawnCards

    def __repr__(self):
        return f"Deck({self.cards})"

if __name__ == "__main__":
    # Example usage:
    deck = Deck()
    deck.shuffle()
    card = deck.draw()
    print(card)