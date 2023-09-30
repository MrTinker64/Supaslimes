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
