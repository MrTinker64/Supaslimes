from Player import Player

class BridgePlayer(Player):
    def add_points_from_hand(self):
        initialPoints = 0
        for card in self.hand:
            if card.rank == "Ace":
                initialPoints += 4
            elif card.rank == "King":
                initialPoints += 3
            elif card.rank == "Queen":
                initialPoints += 2
            elif card.rank == "Jack":
                initialPoints += 1
        return initialPoints

                
class HeartsPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.tricks = []
    
    def recieve_trick(self, trick):
        self.tricks += trick
        
    def count_points(self):
        for card in self.tricks:
            if card.suit == "Heart":
                self.points += 1
            if card == "Queen of Spades":
                self.points += 13
            self.tricks.clear()
