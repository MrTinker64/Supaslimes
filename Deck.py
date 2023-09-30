import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank == "Ace":
            self.numrank = 14
        elif rank == "King":
            self.numrank = 13
        elif rank == "Queen":
            self.numrank = 12
        elif rank == "Jack":
            self.numrank = 11
        else:
            self.numrank = int(rank)

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.SUITS for rank in self.RANKS]

    def resetDeck(self):
        self.cards.clear
        self.cards = [Card(suit, rank) for suit in self.SUITS for rank in self.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, numberOfCards):
        drawnCards = []
        for i in range(numberOfCards):
            if self.cards:
                drawnCards.append(self.cards.pop())
            else:
                raise ValueError("Deck is empty!")
        return drawnCards

    def __repr__(self):
        return f"Deck({self.cards})"

if __name__ == "__main__":
    # Example usage:
    card = Card("Spades", "Ace")
    rank, of, suit = input("Card: ").split()
    card2 = Card(suit, rank)
    if card.__dict__ == card2.__dict__:
        print("Yay!")
    else:
        print("Boo :(")