from Player import Player

class BridgePlayer(Player):
    def add_points_from_hand(self):
        for card in self.hand:
            if card.rank == "Ace":
                self.points += 4
            elif card.rank == "King":
                self.points += 3
            elif card.rank == "Queen":
                self.points += 2
            elif card.rank == "Jack":
                self.points += 1
